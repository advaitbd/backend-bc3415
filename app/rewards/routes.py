# app/rewards/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.rewards.controllers import (
    create_new_reward,
    read_reward,
    read_reward_by_nft,
    update_existing_reward,
    delete_existing_reward,
)
from app.rewards.schemas import RewardCreate, RewardUpdate, RewardResponse
from app.common.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/reward/", response_model=RewardResponse)
def create_reward(reward: RewardCreate, db: Session = Depends(get_db)):
    try:
        return create_new_reward(db, reward)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/reward/{reward_id}", response_model=RewardResponse)
def read_reward(reward_id: int, db: Session = Depends(get_db)):
    try:
        return read_reward(db, reward_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/reward/nft/{nft_id}", response_model=RewardResponse)
def read_reward_by_nft(nft_id: int, db: Session = Depends(get_db)):
    return read_reward_by_nft(db, nft_id)

@router.put("/reward/{reward_id}", response_model=RewardResponse)
def update_reward(reward_id: int, reward: RewardUpdate, db: Session = Depends(get_db)):
    try:
        return update_existing_reward(db, reward_id, reward)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/reward/{reward_id}", response_model=RewardResponse)
def delete_reward(reward_id: int, db: Session = Depends(get_db)):
    try:
        return delete_existing_reward(db, reward_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
