import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# Initialize Firefox WebDriver
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get('https://www.livgolf.com/leaderboard')

# Create an explicit wait instance (10 seconds timeout)
wait = WebDriverWait(driver, 10)

# List of years for which to scrape data
years_to_scrape = ["2025", "2024", "2023"]

for year in years_to_scrape:
    try:
        # --------------------------------------------------
        # Step 1: Select the Year from the Year Dropdown
        # --------------------------------------------------
        year_dropdown_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '(//button[@aria-label="Open dropdown"])[1]'))
        )
        year_dropdown_button.click()
        print("Year dropdown opened.")

        year_dropdown_list = wait.until(
            EC.visibility_of_element_located((By.XPATH, '(//ul[@role="listbox"])[1]'))
        )
        print("Year dropdown list is visible.")

        year_option = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f'(//ul[@role="listbox"])[1]//li[.//span[normalize-space()="{year}"]]')
            )
        )
        year_option.click()
        print(f"Year {year} selected.")

        time.sleep(5)  # Allow page to update

        # --------------------------------------------------
        # Step 2: Retrieve the List of Location Names
        # --------------------------------------------------
        location_dropdown_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '(//button[@aria-label="Open dropdown"])[2]'))
        )
        location_dropdown_button.click()
        print("Location dropdown opened.")

        location_dropdown_list = wait.until(
            EC.visibility_of_element_located((By.XPATH, '(//ul[@role="listbox"])[1]'))
        )
        print("Location dropdown list is visible.")

        location_options = location_dropdown_list.find_elements(By.TAG_NAME, "li")
        location_names = [option.text.strip() for option in location_options if option.text.strip()]
        print(f"Locations available for year {year}: {location_names}")

        # (Optional) Close the location dropdown.
        location_dropdown_button.click()
        time.sleep(1)

        # --------------------------------------------------
        # Step 3: Loop Through Each Location and Process Players
        # --------------------------------------------------
        for loc in location_names:
            try:
                # Re-open location dropdown and select the current location.
                location_dropdown_button = wait.until(
                    EC.element_to_be_clickable((By.XPATH, '(//button[@aria-label="Open dropdown"])[2]'))
                )
                location_dropdown_button.click()
                print(f"Location dropdown re-opened for selecting location '{loc}'.")

                location_dropdown_list = wait.until(
                    EC.visibility_of_element_located((By.XPATH, '(//ul[@role="listbox"])[1]'))
                )
                loc_option = location_dropdown_list.find_element(
                    By.XPATH, f'.//li[.//span[normalize-space()="{loc}"]]'
                )
                loc_option.click()
                print(f"Year {year} - Selected location: {loc}")
                time.sleep(3)  # Allow page to update (leaderboard loads)

                # --------------------------------------------------
                # Step 4: Process Each Player on the Page
                # --------------------------------------------------
                players = wait.until(
                                    EC.presence_of_all_elements_located(
                                        (By.XPATH, "//div[contains(@class, 'rounded-3xl') and @data-id]")
                                    )
                                )
                print(players)
                print(f"Found {len(players)} players on the page for year {year} and location {loc}.")

                for player in players:
                    try:
                        # === Modification: Ensure the player's section is expanded ===
                        # Locate the expand button within the player element.
                        # (This button should have an aria-label containing "expand".)
                        expand_btn = player.find_element(By.XPATH, './/button[contains(@aria-label, "expand")]')
                        # If the player is not expanded (aria-pressed="false"), click to expand.
                        if expand_btn.get_attribute("aria-pressed") == "false":
                            expand_btn.click()
                            # Wait until the attribute changes to "true"
                            WebDriverWait(player, 5).until(
                                lambda p: expand_btn.get_attribute("aria-pressed") == "true"
                            )
                            print(f"Player {player.get_attribute('data-id')} expanded.")
                        else:
                            print(f"Player {player.get_attribute('data-id')} already expanded.")
                        # === End modification ===

                        # Step 5: Loop through each round for the player and extract data.
                        round_tabs = player.find_elements(By.CSS_SELECTOR, '[role="tablist"] button[role="tab"]')
                        if not round_tabs:
                            print(f"No round tabs found for player {player.get_attribute('data-id')}.")
                            continue

                        for tab in round_tabs:
                            round_name = tab.text.strip()  # e.g., "Round 1", etc.
                            tab.click()
                            print(f"Selected {round_name} for player {player.get_attribute('data-id')}.")
                            performance_wrapper = wait.until(
                                EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-element="performance-wrapper"]'))
                            )
                            table = performance_wrapper.find_element(By.TAG_NAME, "table")
                            rows = table.find_elements(By.TAG_NAME, "tr")
                            if len(rows) < 4:
                                print(f"Not enough rows for player {player.get_attribute('data-id')} - {round_name}.")
                                continue

                            # Assume table rows:
                            #   rows[0]: Hole numbers
                            #   rows[1]: Yds
                            #   rows[2]: Par
                            #   rows[3]: Score
                            header_cells = rows[0].find_elements(By.TAG_NAME, "td")
                            holes = [cell.text.strip() for cell in header_cells if cell.text.strip()]
                            yds_cells = rows[1].find_elements(By.TAG_NAME, "td")
                            yds = [cell.text.strip() for cell in yds_cells if cell.text.strip()]
                            par_cells = rows[2].find_elements(By.TAG_NAME, "td")
                            par = [cell.text.strip() for cell in par_cells if cell.text.strip()]
                            score_cells = rows[3].find_elements(By.TAG_NAME, "td")
                            score = [cell.text.strip() for cell in score_cells if cell.text.strip()]

                            print(f"Player {player.get_attribute('data-id')} - {round_name}:")
                            print("Hole Numbers:", holes)
                            print("Yds:", yds)
                            print("Par:", par)
                            print("Score:", score)
                            time.sleep(1)
                    except Exception as e:
                        print(f"Error processing player {player.get_attribute('data-id')}: {e}")

                time.sleep(3)

            except Exception as inner_loc_e:
                print(f"An error occurred when processing location '{loc}' for year {year}: {inner_loc_e}")

    except Exception as e:
        print(f"An error occurred for year {year}: {e}")

driver.quit()
