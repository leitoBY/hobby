from backend.repository import Repository
from backend.api.products.product_model import Product

class ProductRepository(Repository):

    model = Product
