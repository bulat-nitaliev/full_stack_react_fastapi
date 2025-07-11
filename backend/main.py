from fastapi import FastAPI
from routes import router

from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


origins = [
    "http://localhost:3000/",
    "http://10.64.0.86:3000/",
    "http://10.64.0.86:8000/",
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
]


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)
# app.include_router(auth_router)


app.mount("/static", StaticFiles(directory="static"), name="static")
