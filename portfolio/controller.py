# Temp placeholder file (Check how it should work)
# Business logic goes here

from fastapi import HTTPException
from portfolio.tests import PortfolioService

class PortfolioController:
    @staticmethod
    def get_portfolio():
        try:
            return PortfolioService.get_portfolio()
        except Exception as e:
            raise HTTPException(status_code = 500, detail = str(e))