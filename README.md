<p align="center"><img src="https://fadedhd.xyz/IMG/Github/LamMilo/Serpentv2.png"...></p>

---

## 🐍 Overview

**Serpent SSH Client** is a simple yet functional SSHv2 GUI client written in Python using **PyQt5** and **Paramiko**.
It provides an easy way to connect to remote systems, execute commands, and save connection profiles — all within a clean, theme-switchable interface.

---

## ✨ Features

* ✔️ **SSHv2 Support** using Paramiko
* ✔️ **Command Execution** via interactive shell
* ✔️ **Custom Themes** (Light, Dark, Blue, Green)
* ✔️ **Local Profile Saving** to JSON
* ✔️ **Password Field Masking** (asterisks)
* ✔️ **Real-Time Output Display**
* ✔️ **Hotkey Support** (Enter to execute command)

---

## 📦 Requirements

### Python Version

* **Python 3.7 or higher**

### Required pip Packages

| Package  | Link                                                     |
| -------- | -------------------------------------------------------- |
| Paramiko | [**Download**](https://www.paramiko.org/installing.html) |
| PyQt5    | [**Download**](https://pypi.org/project/PyQt5/)          |

Install dependencies via:

```bash
pip install paramiko PyQt5
```

---

## 🚀 Installation & Usage

Clone the repository:

```bash
git clone https://github.com/yourusername/SerpentSSH.git
cd SerpentSSH
```

Run the SSH client:

```bash
python serpent.py
```

---

## 🖥️ How It Works

* Enter **Host**, **Username**, and **Password**
* Connect to the server
* Type commands into the input field
* View responses in the live output window
* Save or load connection profiles for quick access
* Switch themes anytime using **Toggle Theme**

---

## 📁 Project Structure

```
SerpentSSH/
│── serpent.py          # Main application
│── profiles.json       # Saved profiles (created automatically)
│── README.md
└── assets/             # (Optional) images/icons
```

---

## ⚠️ Important Notes

| Note              | Description                                                                                  |
| ----------------- | -------------------------------------------------------------------------------------------- |
| SSHv2 Only        | The client supports **SSHv2** connections exclusively.                                       |
| Password Masking  | Passwords typed into the field appear as asterisks.                                          |
| Password Prompts  | If a remote system prompts for a password, it may display unmasked in the output.            |
| Command Input     | Only **one command per input** is supported. Chaining commands in one line is not supported. |
| Profiles          | Profiles are saved **locally** on your PC in **clear-text JSON**.                            |
| Security Reminder | Do **not** save profiles if you do not want your credentials stored unencrypted.             |

---

## 🛡️ Security Considerations

This tool is intended for **personal / trusted environments**.
Because profile data is stored in plain text, do **not** use it for sensitive systems without modifying the storage method.



---

## 🤝 Contributing

1. Fork the project
2. Create a new feature branch
3. Commit your changes
4. Submit a pull request

Suggestions and improvements are always welcome!

---

## 📜 License

This project is licensed under your preferred license (MIT recommended).
Update this section accordingly.

---

## 👤 Author

**Milo (lamMilo)**
📧 [admin@ffcld.cloud](mailto:admin@ffcld.cloud)
2024 © lamMilo

---

