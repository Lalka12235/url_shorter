from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.logger.log_config import configure_logging
from app.middleware.log_middleware import LogMiddleware

from app.api.v1.link_router import link

configure_logging()

app = FastAPI(
    title='Url shorter',
    description='',
    version='1.0'
)

app.add_middleware(LogMiddleware)
app.include_router(link)


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