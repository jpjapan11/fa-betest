from pydantic import BaseModel, Field
from typing import Literal

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1)
    sku: str = Field(..., min_length=3)
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)
    category: Literal["อาหาร", "เครื่องดื่ม", "ของใช้", "เสื้อผ้า"]

class SellRequest(BaseModel):
    productId: int
    quantity: int

class PriceUpdateRequest(BaseModel):
    productId: int
    newPrice: float = Field(..., gt=0)

class BulkPriceUpdateRequest(BaseModel):
    updates: list[PriceUpdateRequest]