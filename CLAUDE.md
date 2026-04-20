# CLAUDE.md

## #ProjectOverview

Spendly is a lightweight personal expense tracker built with Flask and SQLite.

## #Architecture

```
spendly/
├── app.py              # All routes — single file, no blueprints
├── database/
│   └── db.py           # SQLite helpers: get_db(), init_db(), seed_db()
├── templates/
│   ├── base.html       # Shared layout — all templates must extend this
│   └── *.html          # One template per page
├── static/
│   ├── css/
│   │   ├── style.css       # Global styles
│   │   └── landing.css     # Landing-page-only styles
│   └── js/
│       └── main.js         # Vanilla JS only
└── requirements.txt
```

## #WhereThingsBelong

* #NewRoutes → app.py only, no blueprints
* #DBLogic → database/db.py only, never inline in routes
* #NewPages → new .html file extending base.html
* #PageStyles → new .css file, not inline <style> tags

## #CodeStyle

### #Python

* Follow #PEP8
* Use #snake_case

### #Templates

* Use #Jinja2
* Always use #url_for
* #NoHardcodedURLs

### #RouteFunctions

* #SingleResponsibility
* #FetchData
* #RenderTemplate

### #Database

* Use #ParameterizedQueries
* #NoFStringsSQL

### #ErrorHandling

* Use #abort
* #NoRawErrorStrings

## #TechConstraints

* #FlaskOnly
* #SQLiteOnly
* #VanillaJSOnly
* #NoNewPackages
* #Python310Plus

## #Commands

### #Setup

```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### #RunServer

```bash
python app.py
```

### #Testing

```bash
# Run all tests
pytest

# Run specific file
pytest tests/test_foo.py

# Run specific test
pytest -k "test_name"

# Show output
pytest -s
```

## #RoutesStatus

* #GET_/ → #Implemented
* #GET_/register → #Implemented
* #GET_/login → #Implemented
* #GET_/logout → #Stub_Step3
* #GET_/profile → #Stub_Step4
* #GET_/expenses_add → #Stub_Step7
* #GET_/expenses_edit → #Stub_Step8
* #GET_/expenses_delete → #Stub_Step9

## #Rules

* #DoNotImplementStubsUnlessAsked

## #Warnings

* #NoRawReturns
* #UseUrlFor
* #NoDBInRoutes
* #KeepRequirementsUpdated
* #NoJSFrameworks
* #DBFileInitiallyEmpty
* #EnableForeignKeys
* #Port5001Only

Warnings and things to avoid
Never use raw string returns for stub routes once a step is implemented — always render a template
Never hardcode URLs in templates — always use url_for()
Never put DB logic in route functions — it belongs in database/db.py
Never install new packages mid-feature without flagging it — keep requirements.txt in sync
Never use JS frameworks — the frontend is intentionally vanilla
database/db.py is currently empty — do not assume helpers exist until the step that implements them
FK enforcement is manual — SQLite foreign keys are off by default; get_db() must run PRAGMA foreign_keys = ON on every connection
The app runs on port 5001, not the Flask default 5000 — don't change this
