# Simple FastAPI + MongoDB

A minimal FastAPI app using Motor (async MongoDB driver) with `GET` and `PUT` endpoints for users.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # edit if your Mongo isn't on localhost:27017
```

Make sure MongoDB is running, e.g. with Docker:

```bash
docker run -d -p 27017:27017 --name mongo mongo:7
```

## Run

```bash
uvicorn app.main:app --reload
```

Interactive docs: http://127.0.0.1:8000/docs

## Endpoints

| Method | Path               | Description                                      |
|--------|--------------------|--------------------------------------------------|
| PUT    | `/users/{user_id}` | Create the user (201) or replace it (200)        |
| GET    | `/users/{user_id}` | Fetch a user (404 if it doesn't exist)           |
| GET    | `/health`          | Health check                                     |

```bash
curl -X PUT http://127.0.0.1:8000/users/noa \
  -H "Content-Type: application/json" \
  -d '{"name": "Noa", "email": "noa@example.com", "age": 30}'

curl http://127.0.0.1:8000/users/noa
```

## Layout

```
app/
  main.py        # app + startup/shutdown (Mongo connect/close)
  config.py      # settings from env / .env
  database.py    # Motor client + get_db dependency
  models.py      # Pydantic models
  routers/
    users.py     # GET / PUT user
```
