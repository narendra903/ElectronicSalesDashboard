from faker import Faker
import random
import pandas as pd

# Initialize Faker
fake = Faker()
Faker.seed(0)

# Define some product categories and brands
categories = [
    "Mobile Phones", "Laptops", "Tablets", "Headphones", 
    "Smartwatches", "Televisions", "Cameras", "Speakers"
]

brands = [
    "Apple", "Samsung", "Sony", "LG", "Dell", 
    "HP", "Lenovo", "Asus", "Xiaomi", "OnePlus"
]

# Function to generate products
def generate_products(num):
    products = []
    for i in range(1, num + 1):
        product_id = f"PROD{i:03d}"
        product_name = f"{random.choice(brands)} {fake.word().capitalize()}"
        category = random.choice(categories)
        brand = random.choice(brands)
        price = round(random.uniform(100, 2000), 2)  # Price range between $100 and $2000
        stock_quantity = random.randint(10, 100)     # Stock range between 10 and 100
        
        products.append([product_id, product_name, category, brand, price, stock_quantity])
    
    return products

# Generate 80 products
products = generate_products(80)

# Create a DataFrame
columns = ["ProductID", "ProductName", "Category", "Brand", "Price", "StockQuantity"]
df_products = pd.DataFrame(products, columns=columns)

# Save to CSV
df_products.to_csv("products.csv", index=False)

# Display the first 5 rows
print(df_products.head())
