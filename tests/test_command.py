import pytest

@pytest.mark.usefixtures("command")
def test_basic(command: str):
    assert command == "TEST"
