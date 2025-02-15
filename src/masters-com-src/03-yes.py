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

    # Initialize all qualification columns with 0

    invitees[QUAL_HEADER] = 0

    def set_qualification(row: pd.Series) -> pd.Series:
        qualifications = str(row.get('qualifications', '')).split(',')
        for qual in qualifications:
            qual_key = f"qual_{qual.strip().replace('-', '_')}"
            if qual_key in QUAL_HEADER:
                row[qual_key] = 1
        return row
    # Apply the function to set qualifications
    invitees = invitees.apply(set_qualification, axis=1)
    ###########################################

    # Example qualification headers (only these will be considered)
    # Set of allowed qualification columns

    # # 1. Split qualifications into multiple rows
    # invitees_exploded = invitees.assign(
    #     qualifications=invitees["qualifications"].fillna("").str.split(",")
    # ).explode("qualifications")

    # # 2. Clean qualification column
    # invitees_exploded["qualifications"] = invitees_exploded["qualifications"].str.strip(
    # ).str.replace("-", "_")

    # # 3. One-hot encode valid qualifications
    # qual_dummies = pd.get_dummies(
    #     invitees_exploded["qualifications"], prefix="qual")

    # # 4. Filter to only known qualifications (optional, based on QUAL_HEADER)
    # qual_dummies = qual_dummies.loc[:,
    #                                 qual_dummies.columns.intersection(QUAL_HEADER)]

    # # 5. Aggregate back to original invitees (reset index before grouping)
    # invitees_exploded = invitees_exploded.drop(
    #     columns=["qualifications"]).reset_index()
    # qual_dummies = qual_dummies.reset_index()

    # # 6. Merge the one-hot encoding back
    # invitees_final = invitees_exploded.merge(
    #     qual_dummies.groupby("index").max(),
    #     on="index"
    # ).drop(columns=["index"])

    # print(invitees_final)

    ############################################

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
