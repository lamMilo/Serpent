SSH Connection Tool
A simple Python tool to establish an SSH connection using Paramiko.

Requirements
PyQt5
Python 3.7 or higher
Paramiko library for SSHv2 connections
To install the required dependencies, run:

bash
Code kopieren
pip install PyQt5 paramiko
Description
This tool uses Paramiko, a Python library for SSHv2, to establish SSH connections. Netmiko is another library for network devices, but Paramiko is used here.

How to use the tool:

Host IP Address: Enter the host IP address of the system you want to connect to.
Username: Enter the username for SSH login.
Password: Enter the password. The password will be replaced by asterisks (*) for added privacy.
Connect: Press the Connect button to establish the SSH connection.
Important Notes:

Only SSHv2 connections will work.
Passwords are shown as asterisks (*) in the password field.
If prompted for a password by the system, it will not be displayed as asterisks.
Once connected, any input in the bottom line will be sent to the target system. Only one command can be sent at a time. You cannot send multiple commands in sequence in one input.

License
No license specified. Please add a license if applicable.
