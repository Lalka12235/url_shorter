from fastapi import APIRouter, Depends, HTTPException
from app.utils.make_link import generate_code
from app.config.session import Session, get_db
from app.schemas.link_schemas import LinkCreate, LinkOut
from app.repositories.link_repo import LinkRepositories

link = APIRouter()


@link.post(
    "/shorten",
    summary="Сократить ссылку",
    description="Создаёт короткий код для длинной ссылки",
    response_model=LinkOut
)
async def shorten(payload: LinkCreate, db: Session = Depends(get_db)):
    while True:
        code = generate_code()
        if not  LinkRepositories.exists_code(code, db):
            break

    link_obj = LinkRepositories.create(payload, code, db)
    return link_obj


@link.get(
    "/{code}",
    summary="Редирект по короткой ссылке",
    description="Перенаправляет пользователя на оригинальный URL по коду"
)
async def redirect(code: str, db: Session = Depends(get_db)):
    link_obj = LinkRepositories.get_by_code(code, db)
    if not link_obj:
        raise HTTPException(status_code=404, detail="Ссылка не найдена")
    
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url=link_obj.original_url)


@link.get(
    "/all",
    summary="Список всех ссылок",
    description="Возвращает список всех сохранённых ссылок",
    response_model=list[LinkOut]
)
async def get_all_links(db: Session = Depends(get_db)):
    return LinkRepositories.get_all(db)
