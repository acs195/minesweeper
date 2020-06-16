# Backend

## DB migrations
Initialize for first time:
```
alembic init alembic
```

Create a new revision:
```
alembic revision --autogenerate
```

Upgrade DB:
```
alembic upgrade head or tag
```

Downgrade DB:
```
alembic downgrade base or tag
```

## Run app
With Uvicorn:
```
uvicorn app/main:app --reload
```

Straigth with Python
```
python app/main.py
```

---

## Run tests
```
pytest -v
```

---

## Deploy to Google Cloud Run
```
gcloud builds submit
```

It is hosted on: https://aleapi-bot26wz5ma-ue.a.run.app

### API Documentation
https://aleapi-bot26wz5ma-ue.a.run.app/docs
