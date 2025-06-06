from sqlalchemy import select,insert
from app.config.session import Session
from app.models.link_model import LinkModel
from app.schemas.link_schemas import LinkCreate


class LinkRepositories:

    @staticmethod
    def create(payload: LinkCreate, short_code: str, db: Session):
        stmt = insert(LinkModel).values(
            original_url=payload.original_url,
            short_code=short_code
        ).returning(LinkModel)
        result =db.execute(stmt)
        db.commit()
        return result.scalar_one()

    @staticmethod
    def get_by_code(code: str, db: Session):
        stmt = select(LinkModel).where(LinkModel.short_code == code)
        result = db.execute(stmt)
        return result.scalar_one_or_none()

    @staticmethod
    def exists_code(code: str, db: Session):
        stmt = select(LinkModel).where(LinkModel.short_code == code)
        result =db.execute(stmt)
        return result.scalar_one_or_none() is not None

    @staticmethod
    def get_all(db: Session):
        stmt = select(LinkModel)
        result = db.execute(stmt)
        return result.scalars().all()