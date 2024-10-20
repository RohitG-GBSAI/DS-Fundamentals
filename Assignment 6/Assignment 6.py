import pymysql
from pymongo import MongoClient

# MySQL connection details
mysql_conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='ecommerce_db'
)

# MongoDB connection details
mongo_client = MongoClient('localhost', 27017)
mongo_db = mongo_client['ecommerce_db']
categories_collection = mongo_db['categories']

try:
    # Step 1: Retrieve data from MySQL
    with mysql_conn.cursor() as cursor:
        # Fetch all categories
        cursor.execute("SELECT id, name, description FROM categories")
        categories = cursor.fetchall()

        # Fetch all products
        cursor.execute("SELECT id, name, description, price, category_id FROM products")
        products = cursor.fetchall()

    # Step 2: Structure the data
    data = []
    for category in categories:
        category_id, category_name, category_description = category
        # Filter products belonging to this category
        category_products = [
            {
                "id": product[0],
                "name": product[1],
                "description": product[2],
                "price": float(product[3])
            }
            for product in products if product[4] == category_id
        ]

        # Structure the category with its products
        data.append({
            "id": category_id,
            "name": category_name,
            "description": category_description,
            "products": category_products
        })

    # Step 3: Insert data into MongoDB
    categories_collection.insert_many(data)
    print("Data inserted into MongoDB successfully!")

finally:
    # Close MySQL connection
    mysql_conn.close()
    mongo_client.close()
