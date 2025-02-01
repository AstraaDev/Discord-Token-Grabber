Skip to content
Navigation Menu
AstraaDev
Discord-Token-Grabber

Type / to search

Code
Issues
2
Pull requests
2
Actions
Projects
Wiki
Security
Insights
Settings
Discord-Token-Grabber
/
README.md
in
main

Edit

Preview
Indent mode

Spaces
Indent size

2
Line wrap mode

Soft wrap
Editing README.md file contents
Selection deleted
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79

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

---

### Requirements
- Python 3.x
- Required libraries:
  - `requests`
  - `win32crypt`
  - `pycryptodome` (for AES decryption)
  - `json`
  - `re`
  - `base64`
  
Install the required libraries using `pip`:

```bash
pip install requests pycryptodome
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

### Example Output

<img src="https://cdn.discordapp.com/attachments/1033450243481677874/1064212640332775565/614B4832-BC76-4C2F-95DD-6175E6D22BAB.png?ex=679eee01&is=679d9c81&hm=c313cfa1eb935b232e02a3c8e1e33af1bafdfe757149a498556bf79e740cb97b&" width="500">

---

## Additional Information
- Need help? Join the [Discord Server](https://discord.gg/PKR7nM9j9U).
- Contributions are welcome! Open an issue or create a pull request.

Use Control + Shift + m to toggle the tab key moving focus. Alternatively, use esc then tab to move to the next interactive element on the page.
Aucun fichier choisi
Attach files by dragging & dropping, selecting or pasting them.
Editing Discord-Token-Grabber/README.md at main · AstraaDev/Discord-Token-Grabber
