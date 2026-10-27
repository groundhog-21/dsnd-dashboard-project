# Employee and Team Performance Dashboard

Analyze employee-level and team-level positive and negative events from the
`employee_events.db` SQLite database and their relationship to predicted
recruitment risk. This Udacity Data Science Nanodegree project uses Python,
FastHTML, and Matplotlib to present cumulative events, risk predictions,
and dated notes.

## Set up

These instructions use Windows PowerShell and Python 3.11. Install Python
3.11 and Git, then run:

```powershell
git clone https://github.com/groundhog-21/dsnd-dashboard-project.git
cd dsnd-dashboard-project
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

The requirements also install the local `employee_events` package in editable
mode. In VS Code, select `.venv` as the Python interpreter.

## Run the dashboard

From the project root, with `.venv` active:

```powershell
python report/dashboard.py
```

Open [the dashboard](http://127.0.0.1:5001). Select **Employee** or **Team**,
choose a name, and click **Submit**. Stop the server with **Ctrl+C**.

- **Events:** cumulative positive and negative event counts over time.
- **Risk:** the supplied model's predicted probability; team views show the
  mean of individual employee predictions. The axis runs from 0 to 1.
  Color intensity increases from 0% to 20% risk and is capped above 20%.
- **Notes:** dated notes for the selected employee or team.

## Check the project

Run from the project root:

```powershell
python -m pytest -v
python -m flake8 --config .flake8 .
```

The four tests check that the database file and the `employee`, `team`, and
`employee_events` tables exist. GitHub Actions runs tests and Flake8 on pushes
and pull requests to `main`.

## Project layout

| Location | Contents |
| --- | --- |
| `report/` | Dashboard, reusable interface components, and model loader |
| `python-package/` | Installable `employee_events` package and SQLite database |
| `python-package/dist/` | Built source distribution |
| `assets/` | Trained model, stylesheet, and Inter fonts |
| `tests/` | Database tests |
| `.github/workflows/` | Automated test and lint workflows |
| `src/` | Supporting data and model generation scripts |
| `requirements.txt` | Project installation dependencies |

## Acknowledgments

Based on Udacity's Software Engineering for Data Scientists starter project.
Typography uses Inter; its license is included with the font files in
`assets/fonts/`.
