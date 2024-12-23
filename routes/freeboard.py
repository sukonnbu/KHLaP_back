from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from database import (
    add_freeboard,
    delete_freeboard,
    retrieve_freeboard,
    retrieve_freeboards,
    update_freeboard,
)
from models.freeboard import (
    ErrorResponseModel,
    ResponseModel,
    FreeBoardSchema,
    UpdateFreeBoardModel,
)

router = APIRouter()


@router.get("/", response_description="Get Freeboard Threads from the database")
async def get_freeboard_data():
    freeboards = jsonable_encoder(await retrieve_freeboards())
    return ResponseModel(freeboards, "Freeboards retrieved successfully.")


@router.post("/", response_description="Freeboard added into the database")
async def add_freeboard_data(freeboard: FreeBoardSchema = Body(...)):
    freeboard = jsonable_encoder(freeboard)
    new_freeboard = await add_freeboard(freeboard)
    return ResponseModel(new_freeboard, "Freeboard added successfully.")


@router.get("/{id}", response_description="Freeboard retrieved from the database")
async def get_freeboard_by_id(id: str):
    freeboard = await retrieve_freeboard(id)
    return ResponseModel(freeboard, "Freeboard retrieved successfully.")


@router.put("/{id}", response_description="Freeboard updated into the database")
async def update_freeboard_by_id(id: str, freeboard: UpdateFreeBoardModel = Body(...)):
    updated_freeboard = await update_freeboard(id, freeboard)
    return ResponseModel(updated_freeboard, "Freeboard updated successfully.")
