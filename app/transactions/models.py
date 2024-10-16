# app/transactions/models.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.common.database import Base
from datetime import datetime

class Transaction(Base):
    __tablename__ = "transactions"

    transaction_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.user_id"), index=True)
    points = Column(Integer)
    transaction_type = Column(String)
    related_nft_id = Column(Integer, ForeignKey("nfts.nft_id"), nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="transactions")
    nft = relationship("NFT", back_populates="transactions", uselist=False)
