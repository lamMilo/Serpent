__author__ = "Milo"
__copyright__ = "Copyright 2024, lamMilo"
__email__ = "admin@fflcd.cloud"

from PyQt5 import QtWidgets, QtGui, QtCore
import paramiko
import threading
import sys


class SSHClientApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

        self.ssh = None
        self.channel = None

        # Themes
        self.light_theme = {
            "bg_color": "#ffffff",
            "fg_color": "#000000",
            "entry_bg": "#ffffff",
            "entry_fg": "#000000",
            "button_bg": "#f0f0f0",
            "button_fg": "#000000",
        }
        self.dark_theme = {
            "bg_color": "#2e2e2e",
            "fg_color": "#ffffff",
            "entry_bg": "#3c3c3c",
            "entry_fg": "#ffffff",
            "button_bg": "#5a5a5a",
            "button_fg": "#ffffff",
        }
        self.current_theme = self.light_theme
        self.apply_theme()

    def init_ui(self):
        self.setWindowTitle("Serpent-V01.01")
        self.setGeometry(200, 200, 800, 600)

        # Layouts
        main_layout = QtWidgets.QVBoxLayout()

        # Host Input
        host_layout = QtWidgets.QHBoxLayout()
        self.host_label = QtWidgets.QLabel("Host:")
        self.host_entry = QtWidgets.QLineEdit()
        host_layout.addWidget(self.host_label)
        host_layout.addWidget(self.host_entry)

        # Username Input
        username_layout = QtWidgets.QHBoxLayout()
        self.username_label = QtWidgets.QLabel("Username:")
        self.username_entry = QtWidgets.QLineEdit()
        username_layout.addWidget(self.username_label)
        username_layout.addWidget(self.username_entry)

        # Password Input
        password_layout = QtWidgets.QHBoxLayout()
        self.password_label = QtWidgets.QLabel("Password:")
        self.password_entry = QtWidgets.QLineEdit()
        self.password_entry.setEchoMode(QtWidgets.QLineEdit.Password)
        password_layout.addWidget(self.password_label)
        password_layout.addWidget(self.password_entry)

        # Connect Button
        self.connect_button = QtWidgets.QPushButton("Connect")
        self.connect_button.clicked.connect(self.connect)

        # Theme Toggle Button
        self.theme_button = QtWidgets.QPushButton("Toggle Theme")
        self.theme_button.clicked.connect(self.toggle_theme)

        # Output Area
        self.output_area = QtWidgets.QTextEdit()
        self.output_area.setReadOnly(True)

        # Command Input
        command_layout = QtWidgets.QHBoxLayout()
        self.command_entry = QtWidgets.QLineEdit()
        self.command_entry.setPlaceholderText("Enter your command here...")
        self.command_button = QtWidgets.QPushButton("Send")
        self.command_button.clicked.connect(self.send_command)
        self.command_entry.returnPressed.connect(self.send_command)
        command_layout.addWidget(self.command_entry)
        command_layout.addWidget(self.command_button)

        # Add Widgets to Layout
        main_layout.addLayout(host_layout)
        main_layout.addLayout(username_layout)
        main_layout.addLayout(password_layout)
        main_layout.addWidget(self.connect_button)
        main_layout.addWidget(self.theme_button)
        main_layout.addWidget(self.output_area)
        main_layout.addLayout(command_layout)

        self.setLayout(main_layout)

    def apply_theme(self):
        theme = self.current_theme

        self.setStyleSheet(f"background-color: {theme['bg_color']}; color: {theme['fg_color']};")
        self.output_area.setStyleSheet(f"background-color: {theme['entry_bg']}; color: {theme['entry_fg']};")
        self.host_entry.setStyleSheet(f"background-color: {theme['entry_bg']}; color: {theme['entry_fg']};")
        self.username_entry.setStyleSheet(f"background-color: {theme['entry_bg']}; color: {theme['entry_fg']};")
        self.password_entry.setStyleSheet(f"background-color: {theme['entry_bg']}; color: {theme['entry_fg']};")
        self.command_entry.setStyleSheet(f"background-color: {theme['entry_bg']}; color: {theme['entry_fg']};")
        self.connect_button.setStyleSheet(f"background-color: {theme['button_bg']}; color: {theme['button_fg']};")
        self.theme_button.setStyleSheet(f"background-color: {theme['button_bg']}; color: {theme['button_fg']};")
        self.command_button.setStyleSheet(f"background-color: {theme['button_bg']}; color: {theme['button_fg']};")

    def toggle_theme(self):
        if self.current_theme == self.light_theme:
            self.current_theme = self.dark_theme
        else:
            self.current_theme = self.light_theme
        self.apply_theme()

    def connect(self):
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            host = self.host_entry.text()
            username = self.username_entry.text()
            password = self.password_entry.text()
            self.ssh.connect(host, username=username, password=password)

            self.channel = self.ssh.invoke_shell()
            self.channel.send("\n")

            self.receive_thread = threading.Thread(target=self.receive_output)
            self.receive_thread.daemon = True
            self.receive_thread.start()

            self.output_area.append("Connected to the server.")
        except paramiko.AuthenticationException:
            self.output_area.append("Authentication failed. Please check your credentials.")
        except paramiko.SSHException as e:
            self.output_area.append(f"SSH error: {e}")
        except Exception as e:
            self.output_area.append(f"An error occurred: {e}")

    def send_command(self):
        if not self.channel or not self.channel.active:
            self.output_area.append("Connection lost. Please reconnect.")
            return

        command = self.command_entry.text() + "\n"
        self.channel.send(command)
        self.command_entry.clear()
        self.output_area.append(f"Command sent: {command.strip()}")

    def receive_output(self):
        while True:
            if self.channel.recv_ready():
                output = self.channel.recv(1024).decode('utf-8')
                QtCore.QMetaObject.invokeMethod(
                    self.output_area,
                    "append",
                    QtCore.Qt.QueuedConnection,
                    QtCore.Q_ARG(str, output)
                )

    def closeEvent(self, event):
        if self.ssh:
            self.ssh.close()
        event.accept()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SSHClientApp()
    window.show()
    sys.exit(app.exec_())
