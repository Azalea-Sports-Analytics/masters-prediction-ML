from typing import Any, no_type_check
import sys
import json
import pandas as pd


QUAL_HEADER = [
    "qual_1", "qual_2", "qual_3", "qual_4", "qual_5", "qual_6", "qual_7_A", "qual_7_B",
    "qual_8", "qual_9", "qual_10", "qual_11", "qual_12", "qual_13", "qual_14", "qual_15",
    "qual_16", "qual_17", "qual_18", "qual_19", "qual_20"
]
# !amatuer was misspelled as amatuer in the notebook -- leading to wrong answers
INVIVITE_STATUS_HEADERS = ["amatuer", "firstMasters", "augusta", "inp"]

IDENTITY_HEADERS = ["firstname", "lastname", "country"]


@no_type_check
def one_hut_encode_qualifications(invitees: pd.DataFrame) -> pd.DataFrame:

    invitees['qualifications'] = invitees['qualifications'].str.replace(
        r'\s+', '', regex=True)

    df_encoded = invitees['qualifications'].str.get_dummies(sep=',')

    df_encoded = df_encoded.rename(
        columns=lambda col: 'qual_' + col.replace('-', '_'))

    for col in QUAL_HEADER:
        if col not in df_encoded.columns:
            df_encoded[col] = 0

    return pd.concat([invitees, df_encoded], axis=1)


def process_masters_invites(file_path: str) -> pd.DataFrame:
    with open(file_path, 'r') as file:
        data: dict[str, Any] = json.load(file)
        invitees_list: list[dict[str, Any]] = data["invitees"]

    invitees = pd.DataFrame.from_records(invitees_list)  # type: ignore

    invitees = one_hut_encode_qualifications(invitees)

    # Ensure all INVIVITE_STATUS_HEADERS exist with default 0, then convert them to int
    # invitees = invitees.reindex(columns=invitees.columns.union(
    #     INVIVITE_STATUS_HEADERS), fill_value=0)

    invitees[INVIVITE_STATUS_HEADERS] = invitees[
        INVIVITE_STATUS_HEADERS].astype(int)  # type: ignore

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
