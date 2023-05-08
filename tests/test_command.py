import pytest

from Command import Command

cmds = (
    "TEST",
    "",
    "81233456",
    81233456,
    True
)

@pytest.mark.usefixtures("command")
class TestCommandFixture:
    receiver = print

    @staticmethod
    def test_execute_using_fixture(command: Command, capsys):
        command = Command(cmd="TEST", receiver=TestCommandFixture.receiver)
        command.execute()

        captured = capsys.readouterr()
        assert captured.out.strip() == command._cmd
        assert captured.err in ("", None)


@pytest.mark.parametrize(argnames="cmd", argvalues=cmds)
class TestCommandParams:
    receiver = print

    @staticmethod
    def test_execute_parametrized(cmd: str | int | bool, capsys):
        command = Command(cmd=cmd, receiver=TestCommandParams.receiver)
        command.execute()

        captured = capsys.readouterr()
        assert captured.out.strip() == command._cmd
        assert captured.err in ("", None)

    @staticmethod
    def test_call_parametrized(cmd: str | int | bool, capsys):
        command = Command(cmd=cmd, receiver=TestCommandParams.receiver)
        command()

        captured = capsys.readouterr()
        assert captured.out.strip() == command._cmd
        assert captured.err in ("", None)
