# Notes

Notes is a FASTAPI app for users ro write notes.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requiremets.

```bash
pip install -r requirements.txt
```
### Database

You must create a PostgreSQL database named firstapi.

Download [PostgreSQL](https://www.postgresql.org/download/).


In linux you can install it using apt.

```bash
sudo apt install postgresql
```


Now create a database named firstapi.

```bash
sudo -u postgres psql -c 'firstapi;
```

create the first revision to commit.

```bash
python migration.py make_revision "added models"
```

then migrate the revision.
```bash
python migration.py migrate
```


## Usage



run this command to start the app.

```bash
uvicorn main:app --reload
```


to see the swagger documentation of your running app head to this url.

```
http://127.0.0.1:8000/docs
```


Thanks and enjoy!!