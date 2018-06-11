from repository import Repository
from api.products.product_model import Product

class ProductRepository(Repository):

    model = Product
