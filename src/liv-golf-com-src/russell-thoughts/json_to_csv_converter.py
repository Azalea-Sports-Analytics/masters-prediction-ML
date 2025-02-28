import json
import pandas as pd
from pathlib import Path


def flatten_player_data(player):
    # Initialize flattened player dict with basic info
    flat_player = {
        'player_id': player['playerId'],
        'first_name': player['playerFirstName'],
        'last_name': player['playerLastName'],
        'is_captain': player['isCaptain'],
        'player_status': player['playerStatus'],
        'player_url': player['playerUrl'],
        'team_name': player['teamName'],
        'team_id': player['teamId'],
        'team_color': player['teamColor'],
        'position': player['position'],
        'position_text': player['position_txt'],
        'final_score': player['score'],
        'player_headshot': player['playerHeadshot']
    }

    # Add round scores
    for round_score in player['roundScores']:
        round_num = round_score['roundNumber']
        flat_player[f'round_{round_num}_score'] = round_score['roundScore']

    # Add performance stats for each round
    for perf in player['performanceByRound']:
        round_num = perf['roundNumber']
        prefix = f'round_{round_num}_'
        flat_player.update({
            f'{prefix}eagles_or_better': perf['totalEagleOrBetter'],
            f'{prefix}birdies': perf['totalBirdie'],
            f'{prefix}bogeys': perf['totalBogey'],
            f'{prefix}double_bogeys_or_worse': perf['totalDoubleBogeyOrWorse'],
            f'{prefix}total_score': perf['totalHolesScore'],
            f'{prefix}start_hole': perf['startHole']
        })

        # Add hole-by-hole details for each round
        holes_data = perf.get('holesPerformance', [])
        # Process each hole's data
        for hole_idx, hole in enumerate(holes_data, 1):
            if 'score' in hole:  # Only add if score is available
                column_name = f"detail-{round_num}-{hole_idx}"
                flat_player[column_name] = hole.get('score')

    return flat_player


def convert_json_to_csv():
    # Read JSON file
    input_path = Path(__file__).parent / 'teamsLeaderboard.json'
    with open(input_path, 'r') as f:
        data = json.load(f)

    # Flatten each player's data
    flattened_data = [flatten_player_data(player) for player in data]

    # Convert to DataFrame
    df = pd.DataFrame(flattened_data)

    # Save to CSV
    output_path = input_path.parent / 'leaderboard_flattened.csv'
    df.to_csv(output_path, index=False)
    print(f"CSV file created at: {output_path}")


if __name__ == "__main__":
    convert_json_to_csv()
