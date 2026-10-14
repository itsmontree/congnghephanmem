import json
def load_categories():
    with open("data/cate.json", encoding="utf-8") as f:
        cates = json.load(f)

        return cates

def load_products(q=None, cates_id=None):
    with open("data/prods.json", encoding="utf-8") as f:

        prods = json.load(f)
        if q:
            prods = [p for p in prods if q in p["name"]]
        if cates_id:
            print(cates_id)
            prods = [p for p in prods if int(cates_id) == p["cates_id"]]
        return prods
if __name__ == "__main__":
    print(load_products())