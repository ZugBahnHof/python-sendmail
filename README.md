## SETUP

### Requirements

Install following global, if you want to use your executable.
Otherwise you can install it in an virtual environment.

```bash
pip3 install prompt_toolkit
pip3 install pyaescrypt
```

### Executable

Go to `/usr/bin/` and create a file called e.g. `mail`
It's content should be following:

```bash
#!/bin/bash
cd /path/to/this/sendmail/
python3 tui.py
```

### USERNAME and PASSWORD
To add your username and password for your email account, as well as the server data,
run the file `setup.py`. For example:
```bash
cd /path/to/this/sendmail/
python3 setup.py
```

If you don't give some of the parameters, it'll use default values.

| PARAMETER | DEFAULT VALUE     |
|-----------|-------------------|
| SERVER    | example.com       |
| PORT      | 0                 |
| USER      | admin@example.com |
| PASSWORD  | admin             |

If you have forgotten your password for this mail-client, you have to do the setup again.