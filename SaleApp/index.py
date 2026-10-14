from flask import Flask, render_template, request
import dao
app = Flask(__name__)

@app.route("/")

def index():
    q = request.args.get("q")
    cates_id = request.args.get("cates_id")
    print(cates_id)
    return render_template("index.html", cates = dao.load_categories(), prods = dao.load_products(q=q, cates_id=cates_id))

@app.route("/products/<int:id>")

def products(id):
    return render_template("products.html", id=id)

if __name__ == "__main__":
    app.run(debug=True)