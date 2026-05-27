from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import SessionLocal

from app.schemas.user_schema import (
    UserCreate,
    UserResponse
)

from app.crud.user_crud import create_user


router = APIRouter()


def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()


@router.post(
    "/register",
    response_model=UserResponse
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    return create_user(db, user)


from fastapi import HTTPException

from app.schemas.user_schema import (
    UserCreate,
    UserResponse,
    UserLogin,
    Token
)

from app.crud.user_crud import (
    create_user,
    get_user_by_username
)

from app.core.security import (
    verify_password,
    create_access_token
)

@router.post(
    "/login",
    response_model=Token
)
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    db_user = get_user_by_username(
        db,
        user.username
    )

    if not db_user:

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    if not verify_password(
        user.password,
        db_user.hashed_password # type: ignore
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    access_token = create_access_token(
        data={
            "sub": db_user.username
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }