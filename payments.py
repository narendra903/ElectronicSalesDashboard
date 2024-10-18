from faker import Faker
import random
import pandas as pd

# Initialize Faker
fake = Faker()
Faker.seed(0)

# Sample SaleIDs and Payment Methods
sale_ids = [f"SALE{i:03d}" for i in range(1, 181)]  # Assuming 80 sales
payment_methods = ["Credit Card", "Cash", "Digital Wallet", "Bank Transfer"]

# Function to generate payments
def generate_payments(num):
    payments = []
    for i in range(1, num + 1):
        payment_id = f"PAY{i:03d}"
        sale_id = random.choice(sale_ids)
        payment_method = random.choice(payment_methods)
        amount = round(random.uniform(100, 2000), 2)
        payment_date = fake.date_this_year()
        
        payments.append([payment_id, sale_id, payment_method, amount, payment_date])
    
    return payments

# Generate 80 payments
payments = generate_payments(180)

# Create a DataFrame
columns = ["PaymentID", "SaleID", "PaymentMethod", "Amount", "PaymentDate"]
df_payments = pd.DataFrame(payments, columns=columns)

# Save to CSV
df_payments.to_csv("payment_methods.csv", index=False)

# Display the first 5 rows
print(df_payments.head())
