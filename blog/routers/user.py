from fastapi import APIRouter, Depends, HTTPException, status
from blog.database import get_db
from blog import schemas, oauth2
from sqlalchemy.orm import Session
from blog.repository import user

router = APIRouter(
    prefix='/user',
    tags=['Users']
)


@router.post('/', response_model=schemas.ShowUser)
def create(request: schemas.User, db: Session = Depends(get_db)):
    try:
        return user.create(request, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    try:
        return user.show(id, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    

@router.put('/', response_model=schemas.ShowUser, status_code=status.HTTP_202_ACCEPTED)
def edit_profile(request: schemas.UpdateUser,db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    try:
        return user.edit(request, db, current_user.id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED, detail=str(e))