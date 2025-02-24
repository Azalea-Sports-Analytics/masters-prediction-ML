import re
from convert_near_json import extract_refs





def test_extra_refs():
    assert extract_refs("") == set()
    assert extract_refs("a") == set()
    assert extract_refs("a b") == set()
    assert extract_refs("$a") == set()
    assert extract_refs('"$a b" c d') == set()
    assert extract_refs('"$a " c d') == set()
    assert extract_refs('"$a" b" c d') == set(["a"])
    assert extract_refs('"$a" "$12b" c d') == set(["a", "12b"])
    assert extract_refs('"$a" "$12b" c d "$12b"') == set(["a", "12b"])
    assert extract_refs('"$a" "$12b" c d "$12b" "$1a"') == set(
        ["a", "12b", "1a"])
