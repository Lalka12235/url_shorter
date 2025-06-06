from pydantic import BaseModel, AnyHttpUrl

class LinkCreate(BaseModel):
    original_url: AnyHttpUrl

class LinkOut(BaseModel):
    short_code: str
    original_url: AnyHttpUrl