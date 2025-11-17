
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.apirouter import router

app = FastAPI(title="Sales Analytics Chatbot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Sales Analytics Chatbot API is running"}
