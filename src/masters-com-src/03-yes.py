from typing import Any
import sys
import json
import pandas as pd
assert (pd)

QUAL_HEADER = [
    "qual_1", "qual_2", "qual_3", "qual_4", "qual_5", "qual_6", "qual_7_A", "qual_7_B",
    "qual_8", "qual_9", "qual_10", "qual_11", "qual_12", "qual_13", "qual_14", "qual_15",
    "qual_16", "qual_17", "qual_18", "qual_19", "qual_20"
]
INVIVITE_STATUS_HEADERS = ["amateur", "firstMasters", "augusta", "inp"]
IDENTITY_HEADERS = ["firstname", "lastname", "country"]


def process_masters_invites(file_path: str) -> pd.DataFrame:
    with open(file_path, 'r') as file:
        data: dict[str, Any] = json.load(file)
        invitees_list: list[dict[str, Any]] = data["invitees"]

    invitees = pd.DataFrame.from_records(invitees_list)  # type: ignore

    # Clean spaces and one-hot encode
    invitees['qualifications'] = invitees['qualifications'].str.replace(  # type: ignore
        r'\s+', '', regex=True)  # Remove all spaces
    df_encoded = invitees['qualifications'].str.get_dummies(
        sep=',')  # type: ignore

    df_encoded = df_encoded.rename(
        columns=lambda col: 'qual_' + col.replace('-', '_'))

    for col in QUAL_HEADER:
        if col not in df_encoded.columns:
            df_encoded[col] = 0

    # Concatenate with original DataFrame
    invitees = pd.concat([invitees, df_encoded], axis=1)

    ############################################

    print("Column names:", invitees.columns.tolist())

    # Convert 'amateur', 'firstMasters', and 'augusta' to 1 or 0 if they exist
    for column in INVIVITE_STATUS_HEADERS:
        if column in invitees.columns:
            invitees[column] = invitees[column].astype(int)
        else:
            invitees[column] = 0

    final_columns = IDENTITY_HEADERS + QUAL_HEADER + INVIVITE_STATUS_HEADERS
    invitees_final = invitees[final_columns]

    return invitees_final


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python 03-yes.py <input_json_path> <output_csv_path>")
        sys.exit(1)

    input_json_path = sys.argv[1]
    output_csv_path = sys.argv[2]

    processed_df = process_masters_invites(input_json_path)
    # print(processed_df.head())
    processed_df.to_csv(output_csv_path, index=False)
