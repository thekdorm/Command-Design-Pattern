from __future__ import annotations

class Command:
    _receiver: function
    _cmd: str

    def __init__(self, cmd: str, receiver: function = print) -> None:
        """Generic Command constructor

        Args:
            cmd (str): Command to send.
            receiver (function): Function to call with cmd, exp. Defaults to print.
        """
        self._receiver = receiver
        self._cmd = str(cmd)

    def execute(self) -> None:
        """Pass self._cmd to self._receiver function
        """
        self._receiver(self._cmd)

    def __call__(self) -> None:
        self.execute()
