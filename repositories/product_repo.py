class ProductRepository:
    def __init__(self):
        self.products_db = []
        self.next_id = 1

    def get_all(self):
        return self.products_db

    def get_by_sku(self, sku: str):
        for p in self.products_db:
            if p["sku"] == sku:
                return p
        return None

    def get_by_id(self, product_id: int):
        for p in self.products_db:
            if p["id"] == product_id:
                return p
        return None

    def save(self, product_data: dict):
        product_data["id"] = self.next_id
        self.products_db.append(product_data)
        self.next_id += 1
        return product_data

    def search(self, keyword: str):
        keyword_lower = keyword.lower()
        result = []
        for p in self.products_db:
            # ค้นหาใน name หรือ sku (case-insensitive)
            if keyword_lower in p["name"].lower() or keyword_lower in p["sku"].lower():
                result.append(p)
        return result

    def update_price(self, product_id: int, new_price: float):
        for p in self.products_db:
            if p["id"] == product_id:
                p["price"] = new_price
                return True # อัปเดตสำเร็จ
        return False # ไม่พบสินค้า

# สร้าง Instance ไว้ใช้งาน
product_repo = ProductRepository()