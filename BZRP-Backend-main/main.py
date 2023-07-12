from fastapi import Depends, FastAPI
from database import get_db
from models import Session

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/sessions')
def get_sessions(db: Session = Depends(get_db)):
    sessions = db.query(Session).all() 
    return sessions


