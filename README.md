# SSH Connection Tool

A simple Python tool to establish an SSH connection using Paramiko.

---

## Requirements

### Dependencies

To run this tool, ensure you have the following installed:

- **PyQt5**
- **Python 3.7 or higher**
- **Paramiko** (for SSHv2 connections)

You can install the required dependencies with:

```bash
pip install PyQt5 paramiko
Description
This tool leverages Paramiko, a Python library for SSHv2, to establish SSH connections. While Netmiko is also available for network devices, Paramiko is used here for a more general SSH connection.

How to Use
Host IP Address: Enter the IP address of the system you want to connect to.
Username: Enter the username for SSH login.
Password: Enter the password (it will be replaced with asterisks for privacy).
Connect: Press the Connect button to establish the SSH connection.
Important Notes
This tool only supports SSHv2 connections.
Passwords are displayed as asterisks in the password field.
If the system prompts for a password, it will not be shown as asterisks.
Once connected, any input in the terminal will be sent to the target system. Note that only one command can be sent at a time. Multiple commands cannot be executed in a single input.
License
No license specified. Please add a license if applicable.

vbnet
Code kopieren

Feel free to copy and paste it! Let me know if you need further adjustments.
