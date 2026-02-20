from flask import Flask, render_template, request, redirect, flash
from database import db
from models import Vendor, Product, PurchaseOrder

app = Flask(__name__)
app.secret_key = "erpsecret123"

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///erp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# connect database to app
db.init_app(app)

@app.route("/")
def home():
    total_vendors = Vendor.query.count()
    total_products = Product.query.count()
    pending_orders = PurchaseOrder.query.filter_by(status="Pending").count()
    approved_orders = PurchaseOrder.query.filter_by(status="Approved").count()

    recent_orders = PurchaseOrder.query.order_by(PurchaseOrder.id.desc()).limit(5).all()

    return render_template(
        "home.html",
        total_vendors=total_vendors,
        total_products=total_products,
        pending_orders=pending_orders,
        approved_orders=approved_orders,
        recent_orders=recent_orders
    )

@app.route("/add-vendor", methods=["GET", "POST"])
def add_vendor():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        address = request.form.get("address")

        new_vendor = Vendor(
            name=name,
            email=email,
            phone=phone,
            address=address
        )

        db.session.add(new_vendor)
        db.session.commit()
        flash("Vendor added successfully!")
        return redirect("/")

    return render_template("add_vendor.html")

@app.route("/vendors")
def view_vendors():
    search = request.args.get("search")

    if search:
        vendors = Vendor.query.filter(Vendor.name.ilike(f"%{search}%")).all()
    else:
        vendors = Vendor.query.all()

    return render_template("vendors.html", vendors=vendors)

@app.route("/add-product", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        price = request.form.get("price")

        new_product = Product(
            name=name,
            description=description,
            price=float(price)
        )

        db.session.add(new_product)
        db.session.commit()

        return redirect("/")
    
    return render_template("add_product.html")
    
@app.route("/products")
def view_products():
    products = Product.query.all()
    return render_template("products.html", products=products)

@app.route("/create-po", methods=["GET", "POST"])
def create_po():
    vendors = Vendor.query.all()
    products = Product.query.all()

    if request.method == "POST":
        vendor_id = request.form.get("vendor")
        product_id = request.form.get("product")
        quantity = request.form.get("quantity")

        new_po = PurchaseOrder(
            vendor_id=vendor_id,
            product_id=product_id,
            quantity=int(quantity)
        )

        db.session.add(new_po)
        db.session.commit()

        return redirect("/")

    return render_template("create_po.html", vendors=vendors, products=products)

@app.route("/purchase-orders")
def view_purchase_orders():
    status = request.args.get("status")

    if status:
        orders = PurchaseOrder.query.filter_by(status=status).all()
    else:
        orders = PurchaseOrder.query.all()

    return render_template("purchase_orders.html", orders=orders)

@app.route("/approve-po/<int:po_id>")
def approve_po(po_id):
    order = PurchaseOrder.query.get_or_404(po_id)
    order.status = "Approved"
    db.session.commit()
    return redirect("/purchase-orders")

@app.route("/reports")
def reports():
    total_vendors = Vendor.query.count()
    total_products = Product.query.count()
    total_orders = PurchaseOrder.query.count()
    approved_orders = PurchaseOrder.query.filter_by(status="Approved").count()
    pending_orders = PurchaseOrder.query.filter_by(status="Pending").count()

    return render_template(
        "reports.html",
        total_vendors=total_vendors,
        total_products=total_products,
        total_orders=total_orders,
        approved_orders=approved_orders,
        pending_orders=pending_orders
    )

@app.route("/edit-vendor/<int:vendor_id>", methods=["GET", "POST"])
def edit_vendor(vendor_id):
    vendor = Vendor.query.get_or_404(vendor_id)

    if request.method == "POST":
        vendor.name = request.form.get("name")
        vendor.email = request.form.get("email")
        vendor.phone = request.form.get("phone")
        vendor.address = request.form.get("address")

        db.session.commit()
        return redirect("/vendors")

    return render_template("edit_vendor.html", vendor=vendor)

@app.route("/delete-vendor/<int:vendor_id>")
def delete_vendor(vendor_id):
    vendor = Vendor.query.get_or_404(vendor_id)

    # Check if vendor has purchase orders
    if vendor.purchase_orders:
        return "Cannot delete vendor. Purchase Orders exist for this vendor."

    db.session.delete(vendor)
    db.session.commit()

    return redirect("/vendors")

@app.route("/edit-product/<int:product_id>", methods=["GET", "POST"])
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)

    if request.method == "POST":
        product.name = request.form.get("name")
        product.description = request.form.get("description")
        product.price = float(request.form.get("price"))

        db.session.commit()
        return redirect("/products")

    return render_template("edit_product.html", product=product)

@app.route("/delete-product/<int:product_id>")
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)

    # Prevent deletion if product is used in orders
    if product.purchase_orders:
        return "Cannot delete product. Purchase Orders exist for this product."

    db.session.delete(product)
    db.session.commit()

    return redirect("/products")

@app.route("/cancel-po/<int:po_id>")
def cancel_po(po_id):
    order = PurchaseOrder.query.get_or_404(po_id)

    if order.status == "Approved":
        return "Approved orders cannot be cancelled."

    order.status = "Cancelled"
    db.session.commit()

    return redirect("/purchase-orders")

if __name__ == "__main__":
    app.run(debug=True)