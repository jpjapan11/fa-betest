from datetime import datetime
from schemas.product_schema import ProductCreate, SellRequest, BulkPriceUpdateRequest
from repositories.product_repo import product_repo

class ProductService:
    def create_product(self, product: ProductCreate):
        # 1. เช็ค SKU ซ้ำ
        if product_repo.get_by_sku(product.sku):
            raise ValueError("รหัสสินค้าต้องไม่ซ้ำกับสินค้าที่มีอยู่แล้ว")
        
        # 2. บันทึกข้อมูล
        new_product = product.model_dump()
        new_product["createdAt"] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        return product_repo.save(new_product)

    def get_products(self, category: str = None):
        products = product_repo.get_all()
        if category:
            return [p for p in products if p["category"] == category]
        return products

    def sell_product(self, request: SellRequest):
        # Logic 1
        if request.quantity <= 0:
            raise ValueError("จำนวนที่ต้องการขายต้องมากกว่า 0")
        
        # Logic 2
        target_product = product_repo.get_by_id(request.productId)
        if not target_product:
            raise KeyError("ไม่พบสินค้าในระบบ") # ใช้ KeyError เพื่อสื่อถึง HTTP 404
        
        # Logic 3
        if target_product["stock"] < request.quantity:
            raise ValueError("สต็อกสินค้าไม่เพียงพอ")
            
        # Logic 4: ตัดสต็อก
        target_product["stock"] -= request.quantity
        return {"message": "ขายสินค้าสำเร็จ", "product": target_product}

    def search_products(self, keyword: str):
        if not keyword:
            return [] # ถ้าไม่ได้ส่ง keyword มา ให้คืนค่าลิสต์ว่าง
        return product_repo.search(keyword)

    def bulk_update_price(self, request: BulkPriceUpdateRequest):
        success_count = 0
        
        for update_item in request.updates:
            # โยนให้ Repo จัดการอัปเดตทีละตัว
            if product_repo.update_price(update_item.productId, update_item.newPrice):
                success_count += 1
                
        # ส่ง summary กลับไป
        return {
            "message": "Bulk price update completed",
            "successCount": success_count,
            "totalRequested": len(request.updates)
        }

product_service = ProductService()