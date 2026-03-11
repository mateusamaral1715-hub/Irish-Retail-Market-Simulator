import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta


fake = Faker('en_IE')


NUM_TRANSACTIONS = 50000 
NUM_CUSTOMERS = 1000      
NUM_PRODUCTS = 100        

print(f"Generating data for {NUM_TRANSACTIONS} transactions...")



customers = []
for i in range(1, NUM_CUSTOMERS + 1):
    customers.append({
        'Customer_ID': f"CUST-{i:04d}",
        'Customer_Name': fake.name(),
        'County': fake.county(),
        'Eircode': fake.postcode() 
    })
df_customers = pd.DataFrame(customers)


categories = ['Beverages', 'Electronics', 'Home Decor', 'Clothing', 'Groceries', 'Health & Beauty']
products = []
for i in range(1, NUM_PRODUCTS + 1):
    products.append({
        'Product_ID': f"PROD-{i:04d}",
        'Product_Category': random.choice(categories),
        'Unit_Price_EUR': round(random.uniform(5.0, 500.0), 2)
    })
df_products = pd.DataFrame(products)


transactions = []
payment_methods = ['Revolut', 'Revolut', 'Visa', 'Mastercard', 'Apple Pay', 'Google Pay']

start_date = datetime(2023, 1, 1)
end_date = datetime(2025, 12, 31)
date_range = (end_date - start_date).days

for i in range(1, NUM_TRANSACTIONS + 1):
    customer = random.choice(customers)
    product = random.choice(products)
    
    random_days = random.randint(0, date_range)
    txn_date = start_date + timedelta(days=random_days)
    
    quantity = random.randint(1, 10)
    vat_rate = 0.23 
    
    base_amount = product['Unit_Price_EUR'] * quantity
    total_amount = base_amount * (1 + vat_rate)
    
    transactions.append({
        'Transaction_ID': f"IE-TXN-{i:06d}",
        'Date': txn_date.strftime('%d/%m/%Y'),
        'Customer_ID': customer['Customer_ID'],
        'Customer_Name': customer['Customer_Name'],
        'County': customer['County'],
        'Eircode': customer['Eircode'],
        'Product_ID': product['Product_ID'],
        'Product_Category': product['Product_Category'],
        'Unit_Price_EUR': product['Unit_Price_EUR'],
        'Quantity': quantity,
        'VAT_Rate': '23%',
        'Total_Amount_EUR': round(total_amount, 2),
        'Payment_Method': random.choice(payment_methods)
    })

df_transactions = pd.DataFrame(transactions)
file_name = "irish_sales_data.csv"
df_transactions.to_csv(file_name, index=False, encoding='utf-8')

print(f"Success! File '{file_name}' created with {NUM_TRANSACTIONS} rows.")