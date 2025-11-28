# Exchange Rate Monitor

A simple Python script that fetches exchange rates using the **Date Fixer API** and **kavenegar API**, archives results, and triggers notifications based on custom rules.

## Features

* Fetch exchange rates from Date Fixer API
* Archive rate snapshots as JSON
* Email preparation (optional)
* SMS notifications when rates hit min/max thresholds

## Project Structure

```
main.py
config.py          # contains API URL + rules (DO NOT commit)
notification.py
archive/
```

## Requirements

```
pip install requests
```

## Run

```
python main.py
```

## Note

`config.py` contains sensitive data and must stay in `.gitignore`. Create a safe example file like `config.example.py` for public repositories.
