from pydantic import BaseModel, AnyUrl

class Link(BaseModel):
    url: AnyUrl