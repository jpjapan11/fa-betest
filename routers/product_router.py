from fastapi import APIRouter
from fastapi.responses import JSONResponse
from schemas.product_schema import ProductCreate, SellRequest, BulkPriceUpdateRequest
from services.product_service import product_service

# สร้าง Router และกำหนด Prefix
router = APIRouter(prefix="/api/products", tags=["Products"])

@router.post("", status_code=201)
def create_product(product: ProductCreate):
    try:
        return product_service.create_product(product)
    except ValueError as e:
        return JSONResponse(status_code=400, content={"errors": [str(e)]})

@router.get("")
def get_products(category: str = None):
    return product_service.get_products(category)

@router.post("/sell")
def sell_product(request: SellRequest):
    try:
        return product_service.sell_product(request)
    except ValueError as e:
        return JSONResponse(status_code=400, content={"errors": [str(e)]})
    except KeyError as e:
        # KeyError จาก Service หมายถึงไม่พบสินค้า (404)
        return JSONResponse(status_code=404, content={"errors": [str(e)]})

@router.get("/search")
def search_products(keyword: str):
    return product_service.search_products(keyword)

@router.put("/bulk-price-update")
def bulk_update_price(request: BulkPriceUpdateRequest):
    return product_service.bulk_update_price(request)