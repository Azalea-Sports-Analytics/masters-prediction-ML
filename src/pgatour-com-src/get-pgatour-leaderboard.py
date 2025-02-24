""" Script for getting PGA Tour Scorecard for each player for one event. To get this data for all events we can run each tournament id from data/pgatour-com-data/{YYYY}-schedule.json  """
import os
import json
import requests
import base64
import gzip

def get_pga_tournament_player_ids(tournament_id):
    # API key and payload setup
    X_API_KEY = "da2-gsrx5bibzbb4njvhl7t37wqyl4"
    payload = {
        "operationName": "LeaderboardCompressedV3",
        "variables": {
            "leaderboardCompressedV3Id": f"{tournament_id}"
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


    # Decompress the payload
    compressed_payload = f"{data}"
    decoded_data = base64.b64decode(compressed_payload)
    decompressed_data = gzip.decompress(decoded_data)
    uncompressed_payload = decompressed_data.decode("utf-8")
    

    # Step 4: Try parsing JSON
    try:
        json_data = json.loads(uncompressed_payload)
        #print(json.dumps(json_data, indent=4))
    except json.JSONDecodeError:
        print("Decompressed data is not valid JSON. Raw output:")
        print(uncompressed_payload)


    # Assuming json_data is your parsed JSON dictionary
    players = json_data["players"]

    # We iterate over each row and ensure we only return the ones with a "player" key. Note: there are rows with no player keys
    # This returns a full list of the IDs playing in this event
    player_ids = [item["player"]["id"] for item in players if "player" in item]
    return player_ids
    

def get_pga_tournament_scores(list_of_player_ids, tournament_id):
    X_API_KEY = "da2-gsrx5bibzbb4njvhl7t37wqyl4"
    for player_id in list_of_player_ids:
        print("---------------------------------------------------------------- New player ")
        payload = {
        "operationName": "ScorecardCompressedV3",
        "variables": {
            "tournamentId": f"{tournament_id}",
            "playerId": f"{player_id}"
        },
        "query": "query ScorecardCompressedV3($tournamentId: ID!, $playerId: ID!) {\n  scorecardCompressedV3(tournamentId: $tournamentId, playerId: $playerId) {\n    id\n    payload\n  }\n}"
        }
        # Send the POST request
        response = requests.post(
            "https://orchestrator.pgatour.com/graphql",
            json=payload,
            headers={"x-api-key": X_API_KEY }
        )

        response.raise_for_status()  # Check for any errors

        # Extract the JSON data
        data = response.json()["data"]["scorecardCompressedV3"]["payload"]

        # Compressed payload from response
        compressed_payload = f"{data}"
        decoded_data = base64.b64decode(compressed_payload)
        decompressed_data = gzip.decompress(decoded_data)
        uncompressed_payload = decompressed_data.decode("utf-8")

        try:
            json_data = json.loads(uncompressed_payload)
            print(json.dumps(json_data, indent=4))
        except json.JSONDecodeError:
            print("Decompressed data is not valid JSON. Raw output:")
            print(uncompressed_payload)



player_ids = get_pga_tournament_player_ids("R2025540")
get_pga_tournament_scores(player_ids, "R2025540")


