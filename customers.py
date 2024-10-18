from faker import Faker
import random
import pandas as pd

# Initialize Faker
fake = Faker()
Faker.seed(0)

# Define Indian cities and states
cities_states = [
    ("Mumbai", "Maharashtra"),
    ("Delhi", "Delhi"),
    ("Bengaluru", "Karnataka"),
    ("Hyderabad", "Telangana"),
    ("Chennai", "Tamil Nadu"),
    ("Kolkata", "West Bengal"),
    ("Ahmedabad", "Gujarat"),
    ("Pune", "Maharashtra"),
    ("Jaipur", "Rajasthan"),
    ("Lucknow", "Uttar Pradesh")
]

# Function to generate customers
def generate_customers(num):
    customers = []
    for i in range(1, num + 1):
        customer_id = f"CUST{i:03d}"
        first_name = fake.first_name()
        last_name = fake.last_name()
        city, state = random.choice(cities_states)
        zipcode = fake.zipcode_in_state(state_abbr="MH")  # Just for variety, using Maharashtra pattern
        country = "India"
        gender = random.choice(["Male", "Female"])
        dob = fake.date_of_birth(minimum_age=18, maximum_age=65).strftime("%Y-%m-%d")
        
        customers.append([customer_id, first_name, last_name, city, state, zipcode, gender, dob])
    
    return customers

# Generate 80 customers
customers = generate_customers(120)

# Create a DataFrame
columns = ["CustomerID", "FirstName", "LastName", "City", "State", "ZipCode", "Gender", "DateOfBirth"]
df_customers = pd.DataFrame(customers, columns=columns)

# Save to CSV
df_customers.to_csv("customers.csv", index=False)

# Display the first 5 rows
print(df_customers.head())
