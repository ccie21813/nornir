from builtins import super


class CommandError(Exception):
    """
    Raised when there is a command error.

    Attributes:
        status_code (int): status code returned by the command
        stdout (str): stdout
        stderr (str): stderr
        command (str): command that triggered the error
    """

    def __init__(self, command, status_code, stdout, stderr):
        self.status_code = status_code
        self.stdout = stdout
        self.stderr = stderr
        self.command = command
        super().__init__(command, status_code, stdout, stderr)


class BrigadeExecutionError(Exception):
    """
    Raised by brigade when any of the tasks managed by :meth:`brigade.core.Brigade.run`
    when any of the tasks fail.

    Arguments:
        result (:obj:`brigade.core.task.AggregatedResult`):
    Attributes:
        result (:obj:`brigade.core.task.AggregatedResult`):
    """
    def __init__(self, result):
        self.result = result
        self.failed_hosts = result.failed_hosts
        self.tracebacks = result.tracebacks

    def __str__(self):
        text = "\n"
        for k, r in self.result.tracebacks.items():
            text += "{}\n".format("#" * 40)
            text += "# {} (succeeded) \n".format(k)
            text += "{}\n".format("#" * 40)
            text += "{}\n".format(r)
        for k, r in self.result.tracebacks.items():
            text += "{}\n".format("#" * 40)
            text += "# {} (failed) \n".format(k)
            text += "{}\n".format("#" * 40)
            text += "{}\n".format(r)
        return text
