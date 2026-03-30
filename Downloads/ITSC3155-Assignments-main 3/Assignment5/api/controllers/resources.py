from sqlalchemy.orm import Session
from fastapi import Response, status
from ..models import models

def create(db: Session, resource):
    db_resource = models.Resource(**resource.model_dump())
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource

def read_all(db: Session):
    return db.query(models.Resource).all()

def read_one(db: Session, resource_id):
    return db.query(models.Resource).filter(models.Resource.id == resource_id).first()

def update(db: Session, resource_id, resource):
    db_resource = db.query(models.Resource).filter(models.Resource.id == resource_id)
    db_resource.update(resource.model_dump(exclude_unset=True))
    db.commit()
    return db_resource.first()

def delete(db: Session, resource_id):
    db_resource = db.query(models.Resource).filter(models.Resource.id == resource_id)
    db_resource.delete()
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)