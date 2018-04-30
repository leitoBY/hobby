from backend.api.products.product_repository import ProductRepository


class ProductService:

    @classmethod
    def get_all_products(cls) -> list:
        products = ProductRepository.get_all()
        return [product for product in products]
