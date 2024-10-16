# app/rewards/controllers.py
from sqlalchemy.orm import Session
from app.rewards.crud import (
    get_reward,
    get_reward_by_nft_id,
    create_reward,
    update_reward,
    delete_reward,
)
from app.rewards.schemas import RewardCreate, RewardUpdate

def create_new_reward(db: Session, reward: RewardCreate):
    return create_reward(db=db, reward=reward)

def read_reward(db: Session, reward_id: int):
    db_reward = get_reward(db, reward_id=reward_id)
    if db_reward is None:
        raise ValueError("Reward not found")
    return db_reward

def read_reward_by_nft(db: Session, nft_id: int):
    return get_reward_by_nft_id(db, nft_id=nft_id)

def update_existing_reward(db: Session, reward_id: int, reward: RewardUpdate):
    db_reward = update_reward(db=db, reward_id=reward_id, reward=reward)
    if db_reward is None:
        raise ValueError("Reward not found")
    return db_reward

def delete_existing_reward(db: Session, reward_id: int):
    db_reward = delete_reward(db=db, reward_id=reward_id)
    if db_reward is None:
        raise ValueError("Reward not found")
    return db_reward
