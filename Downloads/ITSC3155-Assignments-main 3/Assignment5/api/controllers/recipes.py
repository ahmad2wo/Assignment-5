from sqlalchemy.orm import Session
from fastapi import Response, status
from ..models import models

def create(db: Session, recipe):
    db_recipe = models.Recipe(**recipe.model_dump())
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def read_all(db: Session):
    return db.query(models.Recipe).all()

def read_one(db: Session, recipe_id):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()

def update(db: Session, recipe_id, recipe):
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)
    db_recipe.update(recipe.model_dump(exclude_unset=True))
    db.commit()
    return db_recipe.first()

def delete(db: Session, recipe_id):
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)
    db_recipe.delete()
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)