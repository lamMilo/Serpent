<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SSH Connection Tool</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }

        h1 {
            color: #4CAF50;
            font-size: 2em;
        }

        h2 {
            color: #333;
            font-size: 1.5em;
        }

        p,
        li {
            font-size: 1.1em;
            margin-bottom: 10px;
        }

        ul {
            margin: 10px 0;
            padding-left: 20px;
        }

        code {
            background-color: #f4f4f4;
            padding: 5px 10px;
            border-radius: 5px;
            font-family: 'Courier New', monospace;
        }

        blockquote {
            background-color: #e9ecef;
            border-left: 5px solid #4CAF50;
            padding: 10px;
            margin: 20px 0;
            font-style: italic;
        }

        .important {
            font-weight: bold;
            color: #d9534f;
        }

        pre {
            background-color: #282c34;
            color: white;
            padding: 20px;
            border-radius: 10px;
            overflow-x: auto;
        }
    </style>
</head>

<body>
    <h1>SSH Connection Tool</h1>

    <p>This tool allows you to establish SSH connections to remote devices, execute commands, and interact securely with a remote system.</p>

    <h2>Requirements</h2>
    <ul>
        <li><strong>Python 3.7</strong> or higher</li>
        <li>PyQt5: <code>pip install PyQt5</code></li>
        <li>Paramiko library (used for SSH connection):
            <pre>pip install paramiko</pre>
        </li>
    </ul>

    <blockquote>
        <p><strong>Note:</strong> This project uses Paramiko, a Python library for SSHv2. While alternatives like Netmiko exist (which is specifically tailored for network devices), Paramiko was chosen for this implementation.</p>
    </blockquote>

    <h2>Features</h2>
    <ul>
        <li>Connect to remote devices using <strong>SSHv2</strong>.</li>
        <li>Enter the IP address of the host, username for authentication, and password (password is masked with asterisks for privacy).</li>
        <li>The interface allows sending <strong>one command at a time</strong> to the remote system.</li>
        <li>Any command entered is forwarded directly to the target system.</li>
        <li>Password input is masked with <strong>*</strong> in the password field for privacy.</li>
    </ul>

    <h2>Important Notes</h2>
    <ul>
        <li class="important">Only <strong>SSHv2</strong> connections are supported.</li>
        <li>Password fields are shown as <strong>*</strong> for privacy. If the system prompts for a password, it will not be displayed as asterisks in the terminal for security reasons.</li>
        <li>Only <strong>one command</strong> can be sent at a time. Multiple commands cannot be queued for sequential execution.</li>
    </ul>

    <h2>Usage</h2>
    <ol>
        <li><strong>Enter Host IP:</strong> Provide the IP address of the remote system.</li>
        <li><strong>Username & Password:</strong> Enter your username and password. Note that the password will be displayed as asterisks for privacy.</li>
        <li><strong>Connect:</strong> Press "Connect" to initiate the SSH connection.</li>
        <li><strong>Command Input:</strong> Enter a single command to be executed on the remote system. It will be forwarded for execution.</li>
    </ol>

    <h2>Documentation & References</h2>
    <p>This tool uses Paramiko for SSH functionality. For further details, check out the <a href="https://www.paramiko.org/" target="_blank">Paramiko Documentation</a>.</p>

</body>

</html>
