from pydantic import BaseModel, field_validator


MAX_BCRYPT_PASSWORD_BYTES = 72


class UserCreate(BaseModel):

    username: str

    password: str

    @field_validator("password")
    @classmethod
    def password_must_fit_bcrypt(cls, value: str) -> str:
        if len(value.encode("utf-8")) > MAX_BCRYPT_PASSWORD_BYTES:
            raise ValueError("password must be 72 bytes or fewer")

        return value


class UserResponse(BaseModel):

    id: int

    username: str

    class Config:

        from_attributes = True
