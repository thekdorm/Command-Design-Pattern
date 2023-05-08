import pytest

@pytest.fixture
def command():
    cmd = "TEST"

    yield cmd
