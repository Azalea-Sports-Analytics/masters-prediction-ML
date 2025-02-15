# type: ignore
import json
import sys


def compare_difference(extracted_data, original_data):
    """
    Compare two lists of dictionaries as sets.

    Two dictionaries with the same key-value pairs (order-insensitive) are considered the same.

    Returns:
        A list of dictionaries that appear in one list but not the other (symmetric difference).
        The list will be empty if there are no differences.
    """
    set_extracted = {frozenset(d.items()) for d in extracted_data}
    set_originals = {frozenset(d.items()) for d in original_data}

    differences_set = set_extracted.symmetric_difference(set_originals)
    differences = [dict(item) for item in differences_set]
    return differences


def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def compare_originals(extracted_path, originals_path):
    extracted_data = load_json(extracted_path)
    originals_raw = load_json(originals_path)
    originals_data = originals_raw["invitees"]

    comparison_result = compare_difference(extracted_data, originals_data)

    if comparison_result:
        print("The originals in extracted.json and originals-2025.json are identical.")
    else:
        print("The originals in extracted.json and originals-2025.json are different.")

        print(comparison_result)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compare_originals.py <extracted_json_path> <originals_json_path>")
        sys.exit(1)

    extracted_json_path = sys.argv[1]
    originals_json_path = sys.argv[2]

    compare_originals(extracted_json_path, originals_json_path)
