from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from datetime import datetime

# Setup WebDriver
service = Service("C:/Windows/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get('https://datagolf.com/datagolf-rankings')
time.sleep(3)

wait = WebDriverWait(driver, 5)

# Function to convert date string to datetime format
def format_week_date(week_date, year):
    return pd.to_datetime(f"{week_date}, {year}")

# Function to extract rankings from the current page
def extract_rankings(week_date):
    rows = driver.find_elements(By.CLASS_NAME, 'datarow')
    data = []
    
    for row in rows:
        try:
            player_id = row.get_attribute('id')
            name = row.find_element(By.CSS_SELECTOR, '.name-col.qual-pop').text
            dg_rank = row.find_element(By.CSS_SELECTOR, '.rank-col.dg-rank-col').text

            # Handle missing WAGR rank
            wagr_rank_element = row.find_elements(By.CSS_SELECTOR, '.rank-col.wagr-rank-col')
            wagr_rank = wagr_rank_element[0].text if wagr_rank_element else "N/A"

            data.append({
                "Week": week_date,
                "ID": player_id,
                "Name": name,
                "DG Rank": dg_rank,
                "OWGR Rank": wagr_rank
            })
        except Exception as e:
            print(f"Error extracting data: {e}")

    return data

# Extract initial ranking data from the loaded page
initial_week = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "the-selected-date"))).text.strip()
initial_week_dt = format_week_date(initial_week, 2025)  # Convert to datetime format
initial_data = extract_rankings(initial_week_dt)

# Click on the date dropdown
date_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'the-selected-date')]")))
date_dropdown.click()
time.sleep(2)  # Allow dropdown to load

# Get all available date options
date_options = driver.find_elements(By.CLASS_NAME, "date-option")
dates = [option.text.strip() for option in date_options]

## List to store weekly ranking data
# List to store weekly ranking data
weekly_data = []

# Start from 2025 and go back to 2023
current_year = 2025
last_month = None  # Track last processed month

for week_date in dates:
    week_date = week_date.strip()  # Ensure no leading/trailing spaces
    print(f"Processing: {week_date}, Year: {current_year}")

    # Stop if we reach November 25, 2024
    if week_date == "December 26" :
        print("Reached December 26, 2022. Stopping.")
        break

    # Extract the month from the date string
    month = week_date.split()[0]  # Extracts "January", "February", etc.

    # Decrement year when transitioning from January to December
    if last_month == "January" and month == "December":
        current_year -= 1  # Decrease the year by 1

    # Store the current month for next iteration check
    last_month = month  # Store the last processed month

    # Convert date string to datetime format
    formatted_week = format_week_date(week_date, current_year)

    # Click on the dropdown each time before selecting a new date
    date_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'the-selected-date')]")))
    date_dropdown.click()
    time.sleep(2)  

    # Get date options again (since the DOM updates after each click)
    date_options = driver.find_elements(By.CLASS_NAME, "date-option")

    # Click on the correct week using JavaScript
    date_found = False
    for option in date_options:
        if option.text.strip() == week_date:
            driver.execute_script("arguments[0].scrollIntoView();", option)  # Scroll into view
            driver.execute_script("arguments[0].click();", option)  # Force JavaScript click
            date_found = True
            time.sleep(3)  # Wait for rankings to load
            break

    if not date_found:
        print(f"Date {week_date} not found! Skipping...")
        continue

    # Extract ranking data for this week
    weekly_data.extend(extract_rankings(formatted_week))

# Close the driver
driver.quit()

# Convert to DataFrame
df = pd.DataFrame(initial_data + weekly_data)  # Append initial data at the end

# Ensure the "Week" column is in datetime format
#df["Week"] = pd.to_datetime(df["Week"])
df["Week"] = pd.to_datetime(df["Week"], format='%d/%m/%Y').dt.strftime('%d/%m/%Y')

print(df.dtypes)  # Check data types to confirm datetime conversion
print(df)

# Save to CSV
df.to_csv("DataGolf_Rankings.csv", index=False)


