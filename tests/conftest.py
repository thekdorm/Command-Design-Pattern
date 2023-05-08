import pytest

from Command import Command


@pytest.fixture(scope="class")
def command():
    cmd = Command(cmd="TEST")

    yield cmd
