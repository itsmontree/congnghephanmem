from flask import render_template, request
import dao
from SaleApp import app


@app.route("/")

def index():
    q = request.args.get("q")
    cate_id = request.args.get("cate_id")
    print(cate_id)
    return render_template("index.html", cates = dao.load_categories(), prods = dao.load_products(q=q, cate_id=cate_id))

@app.route("/products/<int:id>")

def products(id):
    return render_template("products.html", prod=dao.get_product_by_id(id))

@app.context_processor
def common_attribute():
    return {
        "cates": dao.load_categories()
    }

if __name__ == "__main__":
    app.run(debug=True)