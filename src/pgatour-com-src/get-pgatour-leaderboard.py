""" Script for getting PGA Tour Scorecard for each player for one event. To get this data for all events we can run each tournament id from data\pgatour-com-data\{YYYY}-schedule.json  """
import os
import json
import requests
import base64
import gzip

# API key and payload setup
X_API_KEY = "da2-gsrx5bibzbb4njvhl7t37wqyl4"
payload = {
    "operationName": "LeaderboardCompressedV3",
    "variables": {
        "leaderboardCompressedV3Id": "R2025007"
    },
    "query": "query LeaderboardCompressedV3($leaderboardCompressedV3Id: ID!) {\n  leaderboardCompressedV3(id: $leaderboardCompressedV3Id) {\n    id\n    payload\n  }\n}"
}
# Send the POST request
response = requests.post(
    "https://orchestrator.pgatour.com/graphql",
    json=payload,
    headers={"x-api-key": X_API_KEY}
)
response.raise_for_status()  # Check for any errors

# Extract the JSON data
data = response.json()["data"]["leaderboardCompressedV3"]["payload"]

# Compressed payload from response
compressed_payload = f"{data}"

# Step 1: Base64 decode
decoded_data = base64.b64decode(compressed_payload)

# Step 2: Gzip decompress
decompressed_data = gzip.decompress(decoded_data)

# Step 3: Convert bytes to string
uncompressed_payload = decompressed_data.decode("utf-8")

# Step 4: Try parsing JSON
try:
    json_data = json.loads(uncompressed_payload)
except json.JSONDecodeError:
    print("Decompressed data is not valid JSON. Raw output:")
    print(uncompressed_payload)


# Assuming json_data is your parsed JSON dictionary
players = json_data["players"]

# Returns a list of the PGA Tour IDs for that tournament
player_ids = [player["player"]["id"] for player in players if "player" in player]

# Player ID in player IDs
for player_id in player_ids:
    payload = {
    "operationName": "ScorecardCompressedV3",
    "variables": {
        "tournamentId": "R2025007",
        "playerId": f"{player_id}"
    },
    "query": "query ScorecardCompressedV3($tournamentId: ID!, $playerId: ID!) {\n  scorecardCompressedV3(tournamentId: $tournamentId, playerId: $playerId) {\n    id\n    payload\n  }\n}"
    }
    # Send the POST request
    response = requests.post(
        "https://orchestrator.pgatour.com/graphql",
        json=payload,
        headers={"x-api-key": X_API_KEY}
    )

    response.raise_for_status()  # Check for any errors

    # Extract the JSON data
    data = response.json()["data"]["scorecardCompressedV3"]["payload"]


    # Compressed payload from response
    compressed_payload = f"{data}"

    # Step 1: Base64 decode
    decoded_data = base64.b64decode(compressed_payload)

    # Step 2: Gzip decompress
    decompressed_data = gzip.decompress(decoded_data)

    # Step 3: Convert bytes to string
    uncompressed_payload = decompressed_data.decode("utf-8")

    # Step 4: Try parsing JSON
    try:
        json_data = json.loads(uncompressed_payload)
        print(json.dumps(json_data, indent=4))
    except json.JSONDecodeError:
        print("Decompressed data is not valid JSON. Raw output:")
        print(uncompressed_payload)




