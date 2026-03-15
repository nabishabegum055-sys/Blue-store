from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Login credentials
admin_username = "admin"
admin_password = "admin123"

user_username = "user"
user_password = "user123"

# Products with correct images
products = [

{"name":"Laptop","price":55000,
"image":"https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=500"},

{"name":"Smart Watch","price":3000,
"image":"https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=500"},

{"name":"Headphones","price":2000,
"image":"https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500"},

{"name":"Keyboard","price":1500,
"image":"https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=500"},

{"name":"Bluetooth Speaker","price":2500,
"image":"https://images.unsplash.com/photo-1589003077984-894e133dabab?w=400"},

{"name":"Camera","price":45000,
"image":"https://images.unsplash.com/photo-1516724562728-afc824a36e84?w=500"},

]

cart = []
orders = []


# Login page
@app.route("/", methods=["GET","POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == admin_username and password == admin_password:
            return redirect("/admin")

        elif username == user_username and password == user_password:
            return redirect("/store")

    return render_template("login.html")


# Store page
@app.route("/store")
def store():
    return render_template("index.html", products=products)


# Add to cart
@app.route("/add", methods=["POST"])
def add():

    product = request.form["product"]
    price = request.form["price"]

    cart.append({
        "product": product,
        "price": price
    })

    return redirect("/cart")


# Cart page
@app.route("/cart")
def cart_page():
    return render_template("cart.html", cart=cart)


# Place order
@app.route("/place", methods=["POST"])
def place():

    for item in cart:
        orders.append(item)

    cart.clear()

    return render_template("status.html")


@app.route("/admin")
def admin():

    total = 0

    for o in orders:
        total += int(o["price"])

    return render_template("admin.html", orders=orders, total=total)
if __name__ == "__main__":
    app.run(debug=True)