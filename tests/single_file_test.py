import pytest

import single_file


@pytest.mark.parametrize(
    ("flag", "expected"),
    (
        (True, "Verbose flag activated"),
        (False, "Verbose flag deactivated")
    )
)
def test_get_messsage(flag: bool, expected: str) -> None:
    assert single_file.get_message(flag) == expected
