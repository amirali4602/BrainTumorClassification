from PySide6.QtWidgets import QTextEdit


class LogConsole(QTextEdit):

    def __init__(self):
        super().__init__()

        self.setReadOnly(True)

    def log(self, message):

        self.append(message)

    def clear_logs(self):

        self.clear()