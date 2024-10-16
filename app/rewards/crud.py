# app/rewards/crud.py
from sqlalchemy.orm import Session
from app.rewards.models import Reward
from app.rewards.schemas import RewardCreate, RewardUpdate

def get_reward(db: Session, reward_id: int):
    return db.query(Reward).filter(Reward.reward_id == reward_id).first()

def get_reward_by_nft_id(db: Session, nft_id: int):
    return db.query(Reward).filter(Reward.nft_id == nft_id).first()

def create_reward(db: Session, reward: RewardCreate):
    db_reward = Reward(**reward.dict())
    db.add(db_reward)
    db.commit()
    db.refresh(db_reward)
    return db_reward

def update_reward(db: Session, reward_id: int, reward: RewardUpdate):
    db_reward = get_reward(db, reward_id)
    if db_reward:
        for key, value in reward.dict().items():
            setattr(db_reward, key, value)
        db.commit()
        db.refresh(db_reward)
    return db_reward

def delete_reward(db: Session, reward_id: int):
    db_reward = get_reward(db, reward_id)
    if db_reward:
        db.delete(db_reward)
        db.commit()
    return db_reward
