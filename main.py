from fastapi import FastAPI
from pydantic import BaseModel
from pricing_engine import calculate_price, days_between

app = FastAPI(title="Price-Drop API")


class PriceRequest(BaseModel):
    item_name: str
    original_price: float
    expiry_date: str
    total_shelf_life_days: float
    demand_score: float = 0.5


@app.get("/")
def root():
    return {"message": "Price-Drop API running - go to /docs to test it"}


@app.post("/price")
def get_price(req: PriceRequest):
    days_left = days_between(req.expiry_date)
    result = calculate_price(
        req.original_price,
        days_left,
        req.total_shelf_life_days,
        req.demand_score
    )
    result["item_name"] = req.item_name
    return result