from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from config.config import settings
from routes import auth, user

app = FastAPI()

origins = [
    settings.CLIENT_ORIGIN,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router, tags=['Auth'], prefix='/api/auth')
app.include_router(user.router, tags=['Users'], prefix='/api/users')


@app.get("/api/healthchecker")
def root():
    return {"message": "Welcome to FastAPI with MongoDB"}



if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)

