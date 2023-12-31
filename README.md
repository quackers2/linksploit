# LinkSploit
---

`LinkSploit` is a command line application that demonstrates proof-of-concept for exploitation of the **Linksys E1000** router. Using it, the user can access privelaged shell commands that take advantage of existing exploits in the router framework.


## Installation
---

A version of python 3.X.X is required as well as pip

### Installation on Windows

```
git clone https://github.com/quackers2/linksploit.git
cd linksploit
pip install -r requirements.txt
py linksploit.py
```

### Installation on MacOS

```
git clone https://github.com/quackers2/linksploit.git
cd linksploit
python3 -m pip install -r requirements.txt
python3 linksploit.py
```

## Usage
---

### Settings
There are eight settings that Routersploit uses:
1. Target: the target IP address (defaults to 192.168.1.1) 
2. Port: the target port (defaults to 80)
3. Username: If using the 'ping' exploit described below, username of the router must be known (defaults to 'admin')
4. Password: If using the 'ping' exploit described below, password of the router must be known (defaults to 'admin')
5. Timeout: seconds to wait for a response from the HTTP Request sent (defaults to 10.0 seconds)
6. Verify: Indicates whether or not to Validate the TLS certificate provided by the server (defaults to False)
7. Allow_Redirects: Indicates whether or not to allow request to be redirected (defaults to False)
8. Exploit: Either 'moon' or 'ping' for the exploit found in the Moon Worm or the 'ping_size' exploit (defaults to 'moon')

You can view these settings at any time using the command:
`>> settings`
You can also change any of these settings using the command:
`>> set [setting] [value]`


### Commands
To run a privelaged shell command on your router, simply type the command into the command line. For example, try running:

`>> reboot`

and see what happens :smile: