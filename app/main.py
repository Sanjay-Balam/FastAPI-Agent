from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import csv_router

app = FastAPI()

# Allow requests from your frontend if hosted elsewhere
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend's URL if it's hosted separately
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register CSV upload router
app.include_router(csv_router.router)

# Root route
@app.get("/")
async def root():
    return {"message": "CSV to JSON converter API"}
