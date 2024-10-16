# app/rewards/models.py
from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.common.database import Base

class Reward(Base):
    __tablename__ = "rewards"

    reward_id = Column(Integer, primary_key=True, index=True)
    nft_id = Column(Integer, ForeignKey("nfts.nft_id"), unique=True, index=True)
    reward_type = Column(String)
    details = Column(JSON)

    nft = relationship("NFT", back_populates="reward")
