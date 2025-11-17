
from faker import Faker
import mysql.connector
import random
from tqdm import tqdm
import os

fake = Faker()

# ================================
# KONEKSI MYSQL
# ================================
conn = mysql.connector.connect(
    host=os.environ.get("MYSQL_HOST", "localhost"),
    user=os.environ.get("MYSQL_USER", "root"),
    password=os.environ.get("MYSQL_PASSWORD", ""),
    database=os.environ.get("MYSQL_DATABASE", "sales_db")
)
cur = conn.cursor()

# ================================
# 1. Generate Customers
# ================================
def seed_customers(n=500):
    print("Inserting customers...")
    fake.unique.clear()

    batch_size = 100
    for i in tqdm(range(n)):
        name = fake.name()
        email = fake.unique.email()
        phone = fake.phone_number()
        address = fake.address().replace("\n", ", ")

        try:
            cur.execute("""
                INSERT INTO customers (name, email, phone, address)
                VALUES (%s, %s, %s, %s)
            """, (name, email, phone, address))
        except mysql.connector.errors.IntegrityError as e:
            if e.errno == 1062:
                continue
            else:
                raise e

        if (i + 1) % batch_size == 0:
            conn.commit()
    conn.commit()

# ================================
# 2. Generate Products
# ================================
def seed_products(n=200):
    print("Inserting products...")
    fake.unique.clear()
    categories = ["Elektronik", "Fashion", "Makanan", "Minuman", "Aksesoris", "Gaming"]

    batch_size = 100
    for i in tqdm(range(n)):
        product_name = fake.word().capitalize() + " " + fake.word().capitalize()
        category = random.choice(categories)
        price = round(random.uniform(20000, 3000000), 2)
        stock = random.randint(10, 500)

        cur.execute("""
            INSERT INTO products (product_name, category, price, stock)
            VALUES (%s, %s, %s, %s)
        """, (product_name, category, price, stock))

        if (i + 1) % batch_size == 0:
            conn.commit()
    conn.commit()

# ================================
# 3. Generate Sales + Items
# ================================
def seed_sales(n=2000):
    print("Inserting sales...")

    cur.execute("SELECT customer_id FROM customers")
    customers = [row[0] for row in cur.fetchall()]

    cur.execute("SELECT product_id, price FROM products")
    products = cur.fetchall()

    for _ in tqdm(range(n)):
        customer_id = random.choice(customers)
        sale_date = fake.date_between(start_date="-1y", end_date="today")
        payment_method = random.choice(["Cash", "Transfer", "QRIS", "Debit"])

        cur.execute("""
            INSERT INTO sales (customer_id, sale_date, payment_method, total_amount)
            VALUES (%s, %s, %s, %s)
        """, (customer_id, sale_date, payment_method, 0))

        sale_id = cur.lastrowid
        total_amount = 0

        num_items = random.randint(1, 5)
        for _ in range(num_items):
            product_id, price = random.choice(products)
            quantity = random.randint(1, 3)
            line_total = price * quantity
            total_amount += line_total

            cur.execute("""
                INSERT INTO sale_items (sale_id, product_id, quantity, price_each)
                VALUES (%s, %s, %s, %s)
            """, (sale_id, product_id, quantity, price))

        cur.execute("""
            UPDATE sales SET total_amount = %s WHERE sale_id = %s
        """, (total_amount, sale_id))

    conn.commit()

# ================================
# RUN ALL
# ================================
if __name__ == "__main__":
    print("Starting database seeding...")
    seed_customers(500)
    seed_products(200)
    seed_sales(2000)

    cur.close()
    conn.close()

    print("\nDONE! Database MySQL sudah terisi dengan data Faker.")
    print("Total: 500 customers, 200 products, 2000 sales")
