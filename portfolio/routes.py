from fastapi import APIRouter, HTTPException
from .controller import PortfolioController

router = APIRouter()

@router.post("/create-portfolio")
def create_portfolio():
    return {"message": "We are in create-portfolio [portfolio home (Post --> Create)]"}

@router.get("/fetch-portfolio")
def fetch_portfolio():
    return {"message": "We are in fetch-portfolio [portfolio home (Get --> Read)]"}

@router.put("/update-portfolio")
def update_portfolio():
    return {"message": "We are in update-portfolio [portfolio home (Put --> Update)]"}

@router.delete("/delete-portfolio")
def delete_portfolio():
    return {"message": "We are in delete-portfolio [portfolio home (Delete)]"}