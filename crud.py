from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

import models
import schemas


def get_all_authors(db: Session) -> Sequence[models.DBAuthor]:
    return db.scalars(select(models.DBAuthor)).all()

def create_author(db: Session, author: schemas.AuthorCreate) -> models.DBAuthor:
    db_author = models.DBAuthor(
        name=author.name,
        bio=author.bio,
    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_all_books(db: Session) -> Sequence[models.DBBook]:
    return db.scalars(select(models.DBBook)).all()

def create_book(db: Session, book: schemas.BookCreate) -> models.DBBook:
    db_book = models.DBBook(
        title=book.title,
        summary=book.summary,
        publication_date=book.publication_date,
        author_id=book.author_id,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book