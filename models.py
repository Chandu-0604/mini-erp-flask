from database import db
from datetime import datetime

class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    address = db.Column(db.Text)

    def __repr__(self):
        return f"<Vendor {self.name}>"
    
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Product {self.name}>"

class PurchaseOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

    quantity = db.Column(db.Integer, nullable=False)

    order_date = db.Column(db.DateTime, default=datetime.utcnow)

    status = db.Column(db.String(20), default="Pending")

    vendor = db.relationship('Vendor', backref='purchase_orders')
    product = db.relationship('Product', backref='purchase_orders')

    def __repr__(self):
        return f"<PO {self.id}>"