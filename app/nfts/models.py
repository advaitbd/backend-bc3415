# app/nfts/models.py
from sqlalchemy import Column, Integer, String, ForeignKey, JSON, DateTime
from sqlalchemy.orm import relationship
from app.common.database import Base
from datetime import datetime

class NFT(Base):
    __tablename__ = "nfts"

    nft_id = Column(Integer, primary_key=True, index=True)
    token_id = Column(String, unique=True, index=True)
    owner_user_id = Column(String, ForeignKey("users.user_id"), index=True)
    nft_metadata = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    transferred_at = Column(DateTime, nullable=True)

    owner = relationship("User", back_populates="nfts")
    transactions = relationship("Transaction", back_populates="nft")
    reward = relationship("Reward", back_populates="nft", uselist=False)
