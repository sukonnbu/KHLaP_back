from typing import Optional

from pydantic import BaseModel, Field


class FreeBoardSchema(BaseModel):
    title: str = Field(...)
    username: str = Field(...)
    content: str = Field(...)
    image: str = Field(...)
    updated_at: str = Field(...)
    comments: Optional[list]

    class Config:
        json_schema_extra = {
            "example": {
                "title": "오늘부로 아즈사에 대한 지지를 철회한다",
                "username": "아즈사날개의파닥임",
                "content": "오늘부터 지지관계에서 벗어나 아즈사와 나는 한몸으로 일체가 된다. 아즈사에 대한 공격은 나에 대한 공격으로 간주한다.",
                "image": "",
                "updated_at": "12/23 08:16",
                "comments": [
                    {
                        "username": "작성자1",
                        "content": "히히 오줌발싸",
                        "updated_at": "12/23 11:30",
                    },
                ],
            }
        }


class UpdateFreeBoardModel(BaseModel):
    title: Optional[str]
    content: Optional[str]
    img: Optional[str]
    updated_at: Optional[str]
    comments: Optional[list]

    class Config:
        json_schema_extra = {
            "example": {
                "title": "오늘부로 아즈사에 대한 지지를 철회한다",
                "username": "아즈사날개의파닥임",
                "content": "오늘부터 지지관계에서 벗어나 아즈사와 나는 한몸으로 일체가 된다. 아즈사에 대한 공격은 나에 대한 공격으로 간주한다.",
                "image": "",
                "updated_at": "12/23 08:16",
                "comments": [
                    {
                        "username": "작성자1",
                        "content": "히히 오줌발싸",
                        "updated_at": "12/23 11:30",
                    },
                ],
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
