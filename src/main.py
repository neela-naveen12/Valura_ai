from fastapi import FastAPI
from src.routes.query import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Valura AI Microservice")

app.include_router(router)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)