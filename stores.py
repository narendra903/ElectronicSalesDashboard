from faker import Faker
import random
import pandas as pd

# Initialize Faker
fake = Faker()
Faker.seed(0)

# Define sample cities, states, and zip codes
locations = [
    ("Mumbai", "Maharashtra", "400001"),
    ("Bengaluru", "Karnataka", "560001"),
    ("Delhi", "Delhi", "110001"),
    ("Chennai", "Tamil Nadu", "600001"),
    ("Hyderabad", "Telangana", "500001"),
    ("Pune", "Maharashtra", "411001"),
    ("Ahmedabad", "Gujarat", "380001"),
    ("Kolkata", "West Bengal", "700001")
]

# Function to generate stores
def generate_stores(num):
    stores = []
    for i in range(1, num + 1):
        store_id = f"STORE{i:03d}"
        store_name = fake.company()
        city, state, zipcode = random.choice(locations)
        
        
        stores.append([store_id, store_name, city, state, zipcode])
    
    return stores

# Generate 8 stores
stores = generate_stores(8)

# Create a DataFrame
columns = ["StoreID", "StoreName", "City", "State", "ZipCode"]
df_stores = pd.DataFrame(stores, columns=columns)

# Save to CSV
df_stores.to_csv("stores.csv", index=False)

# Display the first 5 rows
print(df_stores.head())
