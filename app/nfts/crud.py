# app/nfts/crud.py
from sqlalchemy.orm import Session
from app.nfts.models import NFT
from app.nfts.schemas import NFTCreate, NFTUpdate

def get_nft(db: Session, nft_id: int):
    return db.query(NFT).filter(NFT.nft_id == nft_id).first()

def get_nfts_by_user_id(db: Session, user_id: str):
    return db.query(NFT).filter(NFT.owner_user_id == user_id).all()

def create_nft(db: Session, nft: NFTCreate):
    db_nft = NFT(**nft.dict())
    db.add(db_nft)
    db.commit()
    db.refresh(db_nft)
    return db_nft

def update_nft(db: Session, nft_id: int, nft: NFTUpdate):
    db_nft = get_nft(db, nft_id)
    if db_nft:
        for key, value in nft.dict().items():
            setattr(db_nft, key, value)
        db.commit()
        db.refresh(db_nft)
    return db_nft

def delete_nft(db: Session, nft_id: int):
    db_nft = get_nft(db, nft_id)
    if db_nft:
        db.delete(db_nft)
        db.commit()
    return db_nft
