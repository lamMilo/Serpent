SSH Connection Tool
This tool allows you to establish SSH connections to remote devices, execute commands, and interact securely with a remote system.

Requirements
Python 3.7 or higher
PyQt5: pip install PyQt5
Paramiko library (used for SSH connection):
Install Paramiko via: pip install paramiko
Note: This project uses Paramiko, a Python library for SSHv2. While alternatives like Netmiko exist (which is specifically tailored for network devices), Paramiko was chosen for this implementation.

Features
Connect to remote devices using SSHv2.
Enter the IP address of the host, username for authentication, and password (password is masked with asterisks for privacy).
The interface allows sending one command at a time to the remote system.
Any command entered is forwarded directly to the target system.
Password input is masked with * in the password field for privacy.
Important Notes
SSHv2 Only: Only SSHv2 connections are supported.
Password Display: Passwords are only shown as asterisks (*) in the password field. If the system prompts for a password, it will not be displayed as asterisks in the terminal for security reasons.
Command Limit: Only one command can be sent at a time; multiple commands cannot be queued for sequential execution.
Usage
Enter Host IP: Provide the IP address of the remote system.
Username & Password: Enter your username and password. Note that the password will be displayed as asterisks for privacy.
Connect: Press "Connect" to initiate the SSH connection.
Command Input: Enter a single command to be executed on the remote system. It will be forwarded for execution.
Documentation & References
This tool uses Paramiko for SSH functionality. For further details, check out the Paramiko Documentation.
