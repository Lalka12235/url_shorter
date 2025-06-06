from sqlalchemy.orm import Mapped,mapped_column

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class LinkModel(Base):
    __tablename__ = 'links'

    id: Mapped[int] = mapped_column(primary_key=True)
    original_url: Mapped[str] = mapped_column(nullable=False)
    short_code: Mapped[str] = mapped_column(unique=True,nullable=False)