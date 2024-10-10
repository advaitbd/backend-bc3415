from fastapi import HTTPException
from rewards.services import RewardsService

class RewardsController:
    @staticmethod
    def get_rewards():
        try:
            return RewardsService.get_rewards()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))