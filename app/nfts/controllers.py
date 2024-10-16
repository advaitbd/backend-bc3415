# app/nfts/controllers.py
from sqlalchemy.orm import Session
from app.nfts.crud import (
    get_nft,
    get_nfts_by_user_id,
    create_nft,
    update_nft,
    delete_nft,
)
from app.nfts.schemas import NFTCreate, NFTUpdate

def create_new_nft(db: Session, nft: NFTCreate):
    return create_nft(db=db, nft=nft)

def read_nft(db: Session, nft_id: int):
    db_nft = get_nft(db, nft_id=nft_id)
    if db_nft is None:
        raise ValueError("NFT not found")
    return db_nft

def read_nfts_by_user(db: Session, user_id: str):
    return get_nfts_by_user_id(db, user_id=user_id)

def update_existing_nft(db: Session, nft_id: int, nft: NFTUpdate):
    db_nft = update_nft(db=db, nft_id=nft_id, nft=nft)
    if db_nft is None:
        raise ValueError("NFT not found")
    return db_nft

def delete_existing_nft(db: Session, nft_id: int):
    db_nft = delete_nft(db=db, nft_id=nft_id)
    if db_nft is None:
        raise ValueError("NFT not found")
    return db_nft
