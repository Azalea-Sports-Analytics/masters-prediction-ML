import os
import json
import requests

# API key and payload setup
X_API_KEY = "da2-gsrx5bibzbb4njvhl7t37wqyl4"
payload = {
    "operationName": "PlayerDirectory",
    "variables": {"tourCode": "R"},
    "query": (
        "query PlayerDirectory($tourCode: TourCode!, $active: Boolean) {\n"
        "  playerDirectory(tourCode: $tourCode, active: $active) {\n"
        "    tourCode\n"
        "    players {\n"
        "      id\n"
        "      isActive\n"
        "      firstName\n"
        "      lastName\n"
        "      shortName\n"
        "      displayName\n"
        "      alphaSort\n"
        "      country\n"
        "      countryFlag\n"
        "      headshot\n"
        "      playerBio {\n"
        "        id\n"
        "        age\n"
        "        education\n"
        "        turnedPro\n"
        "      }\n"
        "    }\n"
        "  }\n"
        "}"
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
data = response.json()["data"]["playerDirectory"]["players"]

# Define the relative folder path
folder_path = os.path.join("data", "pgatour-com-data")

# Define the full file path for the JSON file
output_file = os.path.join(folder_path, "players.json")

# Save the data as a JSON file with pretty printing
with open(output_file, "w") as f:
    json.dump(data, f, indent=4)

print(f"Data successfully saved to {output_file}")




