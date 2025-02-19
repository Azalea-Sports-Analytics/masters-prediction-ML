"""This script fetches the data for the PGA Tour Yearly Schedules."""

import os
import json
import requests
from datetime import datetime


# API key and payload setup
X_API_KEY = "da2-gsrx5bibzbb4njvhl7t37wqyl4"

# Get data for 2023 up to current year (2025 at time of writing)
years = [i for i in range(2023, datetime.now().year + 1)]
print(years)

for year in years:
    payload = {
        "operationName": "Schedule",
        "variables": {"tourCode": "R", "year": f"{year}"},
        "query": (
            "query Schedule($tourCode: String!, $year: String, $filter: TournamentCategory) {\n  schedule(tourCode: $tourCode, year: $year, filter: $filter) {\n    completed {\n      month\n      year\n      monthSort\n      ...ScheduleTournament\n    }\n    filters {\n      type\n      name\n    }\n    seasonYear\n    tour\n    upcoming {\n      month\n      year\n      monthSort\n      ...ScheduleTournament\n    }\n  }\n}\n\nfragment ScheduleTournament on ScheduleMonth {\n  tournaments {\n    tournamentName\n    id\n    beautyImage\n    champion\n    champions {\n      displayName\n      playerId\n    }\n    championEarnings\n    championId\n    city\n    country\n    countryCode\n    courseName\n    date\n    dateAccessibilityText\n    purse\n    sortDate\n    startDate\n    state\n    stateCode\n    status {\n      roundDisplay\n      roundStatus\n      roundStatusColor\n      roundStatusDisplay\n    }\n    tournamentStatus\n    ticketsURL\n    tourStandingHeading\n    tourStandingValue\n    tournamentLogo\n    display\n    sequenceNumber\n    tournamentCategoryInfo {\n      type\n      logoLight\n      logoDark\n      label\n    }\n    tournamentSiteURL\n    tournamentStatus\n    useTournamentSiteURL\n  }\n}"
        )
    }

    # Send the POST request
    response = requests.post(
        "https://orchestrator.pgatour.com/graphql",
        json=payload,
        headers={"x-api-key": X_API_KEY}
    )
    response.raise_for_status()  # Check for any errors

    # Extract the JSON data
    data = response.json()["data"]["schedule"]

    # Define the relative folder path
    folder_path = os.path.join("data", "pgatour-com-data")

    # Define the full file path for the JSON file
    output_file = os.path.join(folder_path, f"{year}-schedule.json")

    # Save the data as a JSON file with pretty printing
    with open(output_file, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Data successfully saved to {output_file}")