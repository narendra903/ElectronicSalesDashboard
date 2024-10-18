from faker import Faker
import random
import pandas as pd

# Initialize Faker
fake = Faker()
Faker.seed(0)

# Sample ProductIDs, StoreIDs, and CustomerIDs based on previous tables
product_ids = [f"PROD{i:03d}" for i in range(1, 81)]  # Assuming 80 products
store_ids = [f"STORE{i:03d}" for i in range(1, 9)]    # Assuming 8 stores
customer_ids = [f"CUST{i:03d}" for i in range(1, 120)] # Assuming 80 customers

# Function to generate sales
def generate_sales(num):
    sales = []
    for i in range(1, num + 1):
        sale_id = f"SALE{i:03d}"
        product_id = random.choice(product_ids)
        store_id = random.choice(store_ids)
        customer_id = random.choice(customer_ids)
        quantity_sold = random.randint(1, 10)  # Selling between 1 and 10 units
        sale_date = fake.date_this_year()
        price = round(random.uniform(100, 2000), 2)  # Assuming a random price range
        total_amount = round(price * quantity_sold, 2)
        
        sales.append([sale_id, product_id, store_id, customer_id, quantity_sold, sale_date, total_amount])
    
    return sales

# Generate 80 sales
sales = generate_sales(180)

# Create a DataFrame
columns = ["SaleID", "ProductID", "StoreID", "CustomerID", "QuantitySold", "SaleDate", "TotalAmount"]
df_sales = pd.DataFrame(sales, columns=columns)

# Save to CSV
df_sales.to_csv("sales.csv", index=False)

# Display the first 5 rows
print(df_sales.head())
