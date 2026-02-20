# 🧾 Mini ERP — Purchase Order Management System (Flask)

A web-based Enterprise Resource Planning (ERP) module developed using **Flask, SQLAlchemy, SQLite, and Bootstrap** that simulates a real business purchase workflow.

This system allows an organization to manage suppliers, products, and purchase orders with an approval lifecycle and dashboard analytics.

---

## 🔹 Project Purpose

This project was built to demonstrate backend development skills, database modeling, and real-world workflow implementation — not just CRUD operations.

It models how small and medium businesses actually handle procurement:

Vendor ➜ Product ➜ Purchase Order ➜ Approval ➜ Reporting

---

## 🚀 Key Features

### 1. Vendor Management

* Add, edit, and delete vendors
* Search vendors by name
* Prevent deletion if vendor is used in a purchase order
* Data validation with confirmation prompts

### 2. Product Management

* Add, edit, and delete products
* Unit price handling
* Referential integrity protection (cannot delete used product)

### 3. Purchase Order Workflow

* Create purchase orders
* Select vendor and product dynamically
* Order status lifecycle:

  * Pending
  * Approved
  * Cancelled
* Approval action
* Cancel order functionality
* Filter orders by status

### 4. Dashboard & Reporting

* KPI summary cards
* Recent purchase orders activity
* Reports page analytics:

  * Total vendors
  * Total products
  * Pending orders
  * Approved orders

### 5. User Experience Features

* Bootstrap admin interface
* Flash success messages
* Delete confirmation dialogs
* Search and filtering
* Structured form layouts

---

## 🧠 Business Logic Implemented

The application enforces real ERP rules:

* Vendors cannot be deleted if linked to orders
* Products cannot be removed if used in transactions
* Approved orders cannot be cancelled
* Purchase orders maintain referential integrity

---

## 🛠 Technology Stack

**Backend**

* Python
* Flask
* Flask-SQLAlchemy
* SQLite

**Frontend**

* HTML
* Bootstrap 5
* Jinja2 Templates

**Database**

* Relational database modeling
* Foreign key relationships
* Transaction handling

---

## 📂 Project Structure

```
ERP_Project/
│
├── app.py
├── models.py
├── database.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── vendors.html
│   ├── products.html
│   ├── purchase_orders.html
│   ├── add_vendor.html
│   ├── add_product.html
│   └── create_po.html
│
└── static/
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/Chandu-0604/mini-erp-flask.git
```

### 2. Navigate to the project

```
cd mini-erp-flask
```

### 3. Create virtual environment

```
python -m venv venv
```

### 4. Activate environment

Windows:

```
venv\Scripts\activate
```

### 5. Install dependencies

```
pip install -r requirements.txt
```

### 6. Run the application

```
python app.py
```

### 7. Open in browser

```
http://127.0.0.1:5000
```

---

## 📸 Screenshots (Add Later)

Add screenshots here after running the app:

* Dashboard
  <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c530383c-4c67-4653-81cb-be300c03fa92" />
* Vendor List
 <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/cc8b90b8-c765-4104-9db6-fcd642fe6dac" />
* Product List
  <img width="1755" height="987" alt="image" src="https://github.com/user-attachments/assets/00aa7769-b0eb-4cdf-b294-e4a686d15a29" />
* Create Purchase Order
 <img width="1755" height="987" alt="image" src="https://github.com/user-attachments/assets/0acb8f02-ad12-40f4-ac7e-435635c86459" />
* Reports Page
 <img width="1755" height="987" alt="image" src="https://github.com/user-attachments/assets/d9d0b9e5-376f-464b-a480-bbf97b0f5add" />

---

## 📈 What This Project Demonstrates

This project demonstrates:

* Flask web application development
* MVC architecture
* Relational database modeling
* Foreign key relationships
* Workflow/state management
* Backend validation logic
* UI integration with backend
* Real-world business process simulation

---

## 🔮 Future Improvements

* User authentication (Admin / Manager roles)
* Export reports to Excel
* REST API endpoints
* Deployment to cloud (Render / Railway)
* Email notification on order approval

---

## 👨‍💻 Author

**Chandan B**
Computer Science Engineering Student

GitHub: https://github.com/Chandu-0604

---

## ⭐ Why This Project Matters

This is not a tutorial CRUD project.

It is a workflow-based backend application that replicates an actual business procurement process, focusing on database integrity, transaction handling, and system usability.
