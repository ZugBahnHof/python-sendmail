Go to `/usr/bin/` and create a file called e.g. `mail`
It's content should be following:

```bash
#!/bin/bash
cd /path/to/this/sendmail/
python3 tui.py
```

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