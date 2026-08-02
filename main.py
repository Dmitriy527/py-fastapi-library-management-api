from typing import Annotated, Generator

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from database import SessionLocal

app = FastAPI()


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/authors/", response_model=list[schemas.Author])
def read_authors(db: Annotated[Session, Depends(get_db)]):
    return crud.get_all_authors(db=db)


@app.post("/author/", response_model=schemas.Author)
def create_author(
    author: schemas.AuthorCreate,
    db: Annotated[Session, Depends(get_db)]
):


    return crud.create_author(
        db=db,
        author=author
    )

@app.get("/books/", response_model=list[schemas.Book])
def read_books(db: Annotated[Session, Depends(get_db)]):
    return crud.get_all_books(db=db)

@app.post("/book/", response_model=schemas.Book)
def create_book(
        book: schemas.BookCreate,
        db: Annotated[Session, Depends(get_db)]
):
    return crud.create_book(
        db=db,
        book=book
    )


