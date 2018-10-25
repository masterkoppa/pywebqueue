# Setup
## Install Dependencies

```bash
python -m virtualenv venv/
source venv/bin/activate
pip install -r requirements.txt
```

## Running the App

### Initialize DB

```bash
python scripts/init_db.py
```

### Run Web App

```bash
FLASK_APP=pywebqueue/routes.py python -m flask run
```