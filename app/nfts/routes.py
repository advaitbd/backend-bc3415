# app/nfts/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.nfts.controllers import (
    create_new_nft,
    read_nft,
    read_nfts_by_user,
    update_existing_nft,
    delete_existing_nft,
)
from app.nfts.schemas import NFTCreate, NFTUpdate, NFTResponse
from app.common.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/nft/", response_model=NFTResponse)
def create_nft(nft: NFTCreate, db: Session = Depends(get_db)):
    try:
        return create_new_nft(db, nft)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/nft/{nft_id}", response_model=NFTResponse)
def read_nft_route(nft_id: int, db: Session = Depends(get_db)):
    try:
        return read_nft(db, nft_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/nfts/user/{user_id}", response_model=list[NFTResponse])
def read_nfts_by_user_route(user_id: str, db: Session = Depends(get_db)):
    return read_nfts_by_user(db, user_id)

@router.put("/nft/{nft_id}", response_model=NFTResponse)
def update_nft(nft_id: int, nft: NFTUpdate, db: Session = Depends(get_db)):
    try:
        return update_existing_nft(db, nft_id, nft)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/nft/{nft_id}", response_model=NFTResponse)
def delete_nft(nft_id: int, db: Session = Depends(get_db)):
    try:
        return delete_existing_nft(db, nft_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
