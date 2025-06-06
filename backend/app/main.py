from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.logger.log_config import configure_logging
from app.middleware.log_middleware import LogMiddleware

configure_logging()

app = FastAPI(
    title='FastAPI Template',
    description='Just use in your project'
)

app.add_middleware(LogMiddleware)

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/ping')
async def ping():
    return 'Server is running'