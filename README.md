# Signal Flair
---------

"Generate a Pandas-style profiling report from a Flask web app."

## Environment Set-up
Pre-requisite: Python 3

```
$ python3 -m venv env
$ source env/bin/activate
$ python -m pip install --upgrade pip
$ python -m pip install -r requirements.txt
```

## Run the App

1. For local environments - use `flask run`:
```bash
./start.sh <enter port number, or leave blank to use 5000>
```

1. For production - use `gunicorn`:
```bash
cd signal_flair/
gunicorn production:app
```

Credit to Nathan Lauga, for building the initial version of this repo [here on GitHub](https://github.com/Nathanlauga/pandas-profiling-flask).
