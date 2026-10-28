import json
from models import Category, Product

def load_categories():
    # with open("data/cate.json", encoding="utf-8") as f:
    #     cates = json.load(f)
    #
        return Category.query

def load_products(q=None, cate_id=None):
    # with open("data/prods.json", encoding="utf-8") as f:
    #
    #     prods = json.load(f)
    query = Product.query
    if q:
        query = query.filter(Product.name.contains(q))
    if cate_id:
        query = query.filter(Product.cate_id == int(cate_id))
    return query.all()
    # return Product.query.filter(or_(Product.name.ilike(f"%{q}%"), Product.cate_id == cate_id)).all()

def get_product_by_id(id):
    # with open("data/prods.json", encoding="utf-8") as f:
    #     prods = json.load(f)
    #     for p in prods:
    #         if p["id"]==id:
    #             return p
    return Product.query.get(id)

if __name__ == "__main__":
    print(load_products())