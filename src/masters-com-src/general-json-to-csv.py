import json
import pandas as pd

type FILENAME = str
type INPUT_FILENAME = FILENAME
type OUTPUT_FILENAME = FILENAME
type COLUMN_NAME = str


def messy_json_to_csv(json_file: INPUT_FILENAME, csv_file: OUTPUT_FILENAME,
                      keys: list[str] = [],
                      exploding_column: COLUMN_NAME | None = None,
                      exploding_prefix: str = "",
                      exploding_separator: str = ",",
                      exploding_ignore_regx: str = r"\s+",
                      exploded_column_names: list[COLUMN_NAME] = [],
                      bool_column_names: list[COLUMN_NAME] = []
                      ) -> None:
    if not json_file.endswith('.json'):
        raise ValueError("The input file must have a .json extension")
    if not csv_file.endswith('.csv'):
        raise ValueError("The output file must have a .csv extension")

    with open(json_file, 'r') as file:
        messy_dict = json.load(file)

    if not isinstance(messy_dict, dict):
        raise ValueError("JSON data is not a dictionary")

    simple_dict: dict[str, dict[str, any]
                      ] = messy_dict_to_simple_dict(messy_dict, keys=keys)

    simple_df: pd.dataframe = pd.DataFrame(simple_dict)

    the_exploded_df: pd.dataframe = explode_df(
        simple_df, exploding_column=exploding_column, exploding_prefix=exploding_prefix, exploding_separator=exploding_separator, exploding_ignore_regx=exploding_ignore_regx,
        exploded_column_names=exploded_column_names
    )

    unbooled_df: pd.dataframe = unbooleanize_df(
        the_exploded_df, bool_column_names)

    unbooled_df.to_csv(csv_file, index=False)


def messy_dict_to_simple_dict(messy_dict: dict, keys: list[str] = []) -> dict:
    """
    Converts a nested dictionary into a simpler dictionary by traversing it with a sequence
    of keys. This function is useful when you have a nested JSON-like dictionary and you
    need to isolate a specific sub-dictionary or value based on a series of keys.
    Parameters:
        messy_dict (dict): The original nested dictionary from which to extract the data.
        keys (list[str]): A list of keys representing the path to the desired sub-dictionary
                          or value. The function will successively traverse the dictionary
                          using these keys.
    Returns:
        dict: The resulting dictionary or value after traversing the specified keys.
    Raises:
        ValueError: If any key in the provided path is not found in the current level of the dictionary.
    """

    answer = messy_dict
    for key in keys:
        if key not in messy_dict:
            raise ValueError(f"Key {key} not found in JSON data")
        answer = answer[key]
    return answer


def explode_df(simple_df: pd.dataframe, exploding_column: COLUMN_NAME | None = None, exploding_prefix: str = "", exploding_separator: str = ",",
               exploding_ignore_regx: str = r"\s+", exploded_column_names: list[str] = []) -> pd.dataframe:
    """
              Explodes a specified column of a DataFrame by splitting its string values into multiple columns.

              Parameters:
                  simple_df (pd.DataFrame): The input DataFrame containing the column to be exploded.
                  exploding_column (str | None, optional): The name of the column whose values will be split using the specified separator.
                      If None, the function returns the original DataFrame without any modifications.
                  exploding_prefix (str, optional): A prefix to use when naming new columns created by the explosion. Defaults to an empty string.
                  exploding_separator (str, optional): The delimiter used to split the string values in the exploding column. Defaults to a comma (",").
                  exploding_ignore_regx (str, optional): A regular expression pattern used to ignore certain parts of the strings (such as extra whitespace) during splitting.
                      Defaults to r"\s+".
                  exploded_column_names (list[str], optional): The list of column names to that should be created by splitting.  Any other columns will raise an errors.  Any missing columns (eg: flags that always false in this data set) will be created.

              Returns:
                  pd.DataFrame: A new DataFrame with the specified column exploded into multiple columns. If no exploding_column is provided
                   the original DataFrame is returned.

              Raises:
                  NotImplementedError: Indicates that the core functionality for exploding the DataFrame has not been implemented yet.
              """

    if exploding_column is None:
        return simple_df

    exploded_df = simple_df.copy()

    raise NotImplementedError("port stuff from other file")

    return exploded_df


def unbooleanize_df(booleanize_df: pd.dataframe, bool_column_names: list[str]) -> pd.dataframe:
    """
    replace True/False with 1/0

    Args:
        booleanize_df (pd.DataFrame): The source DataFrame containing booleanized columns.
        bool_column_names (list[str]): A list of column names whose boolean values should be reverted.
                    If empty, no columns will be processed.
    Returns:
        pd.DataFrame: A copy of the original DataFrame if no columns are specified for processing.
                    Otherwise, a copy of the DataFrame with the specified columns reverted to 1/0.
    Raises:
        NotImplementedError: If boolean unconversion for the specified columns is attempted,
                    Indicating that the functionality remains to be implemented.
    """

    if not bool_column_names:
        return booleanize_df
    df = booleanize_df.copy()

    for column_name in bool_column_names:
        raise NotImplementedError("port stuff from other file")
    return df

# TODO: main
# TODO: listing exactly which columns we want in which order
# TODO: lesting
