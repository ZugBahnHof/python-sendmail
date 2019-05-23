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
Either, you do this via the `Update function` (just run the program and press `u`)
or you can do this manually. For this, look at following manual.

Create file `secret_credentials.json` and fill it with following:

```json
{ 
  "SERVER": "postoffice.katharineum.de",
  "PORT": "",
  "USER": "",
  "PASSWORD": ""
}
```

If you don't give some of the parameters, it'll use default values.

| PARAMETER | DEFAULT VALUE     |
|-----------|-------------------|
| SERVER    | example.com       |
| PORT      | 0                 |
| USER      | admin@example.com |
| PASSWORD  | admin             |