from sqlalchemy.orm import Session
from blog import schemas, models
from blog.hashing import Hash
from fastapi import HTTPException, status

def create(request: schemas.User, db: Session):
    new_user = models.User(name=request.name, email=request.email, mobile=request.mobile, about=request.about, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id of {id} not found")
    
    return user

def edit(request: schemas.UpdateUser, db: Session, current_user_id: int):
    try:
        user = db.query(models.User).filter(models.User.id == current_user_id)
        if not user.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")
        
        if user.first().id != current_user_id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not authorized to update")

        user.update(dict(request))
        db.commit()
        return 'User details updated successfully'    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    