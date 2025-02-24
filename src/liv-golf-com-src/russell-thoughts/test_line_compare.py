# import re
import pytest
from convert_near_jason import good_line, bad_line


# GOOD_RE = re.compile(
#     r'^[0-9a-z]+:\"'
#     # r'^(?:[0-9a-z]+):(?:\[|\{)"'
# )


# def test_one():
#     line = 'a:{"'
#     # answer = GOOD_RE.match(line)  # type: ignore
#     answer = re.match(r'^[0-9a-z]+:[{[]"', line)
#     print(f"{answer=}")
#     assert (answer)


# @pytest.mark.skip(reason="Skipping this test")
@pytest.mark.parametrize("good_example", [
    'a:{"',
    'b:{"bbb',
    'c:["ccc',
    'd1:{"111',
    '10e:{"',
    '20:["',]

)
def test_good_line(good_example: str) -> None:
    assert good_line(good_example) == True


# @pytest.mark.skip(reason="Skipping this test")
@pytest.mark.parametrize("bad_example", ["", "hello"])
def test_bad_line(bad_example: str) -> None:
    assert bad_line(bad_example) == True
