from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from routers import product_router

app = FastAPI()

# ---------------------------------------------
# Custom Error Handler สำหรับ Pydantic (HTTP 422 -> 400)
# ---------------------------------------------
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for err in exc.errors():
        field = err.get("loc")[-1]
        if field == "name":
            errors.append("ชื่อสินค้าต้องไม่ว่าง")
        elif field == "sku":
            errors.append("รหัสสินค้าต้องมีอย่างน้อย 3 ตัวอักษร")
        elif field == "price":
            errors.append("ราคาต้องมากกว่า 0")
        elif field == "stock":
            errors.append("จำนวนคงเหลือ (Stock) ต้องไม่ติดลบ")
        elif field == "category":
            errors.append('หมวดหมู่ต้องเป็น "อาหาร", "เครื่องดื่ม", "ของใช้" หรือ "เสื้อผ้า"')
            
    return JSONResponse(status_code=400, content={"errors": errors})

# ---------------------------------------------
# นำ Router เข้ามาเชื่อมต่อ
# ---------------------------------------------
app.include_router(product_router.router)