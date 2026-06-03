# Automated ETL Pipeline for Weather Data

##  Overview

Built an automated ETL pipeline to extract, process, and store job data in a PostgreSQL database using Python and GitHub Actions.

---

## Tech Stack

* Python
* Pandas
* PostgreSQL (Neon)
* GitHub Actions
* SQL

---

## Workflow

* Extract data using Python
* Transform and clean using Pandas
* Load into PostgreSQL database
* Automate pipeline using GitHub Actions

---

## Structure

```bash
src/            # ETL script
logs/           # Pipeline logs
.github/        # Automation workflow
requirements.txt
README.md
```

---

## Run Locally

```bash
pip install -r requirements.txt
python src/main.py
```

---

## Output

Structured weather data stored in PostgreSQL, ready for analysis.

Below is a snapshot of processed weather data stored in PostgreSQL:


<img width="935" height="382" alt="image" src="https://github.com/user-attachments/assets/c0414fa9-1e67-4ae5-bf32-e2ede8e0eb12" />


| City      | Avg Temperature | Avg Humidity |
|----------|---------------|-------------|
| Bangalore | 28.82 | 44.52 |
| Chennai   | 29.72 | 75.52 |
| Delhi     | 27.13 | 33.50 |
| Mumbai    | 29.20 | 63.76 |

---

## Author

Sidharth Nair
Aspiring Data Engineer

