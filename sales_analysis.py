import pandas as pd

file_path='Learning/sales_data.csv'
df = pd.read_csv(file_path)

# 2. EXPLORING DATA TYPES (Shape, Columns, Types)
print('------------------')
print("--- DATA TYPES ---")
print(f"Shape: {df.shape}") 
print(f"\nColumns: {df.columns}")
print("\nData Types:")
print(df.dtypes)

# 3. CLEAN DATA
# Checking for missing values and duplicates
missing_count = df.isnull().sum().sum()
duplicate_count = df.duplicated().sum()

# Cleaning
df = df.fillna(0) 
df = df.drop_duplicates()
print('-----------------------------')
print('-------CLEANING DETAILS------')
print(f"Missing values: {missing_count}")
print(f"Duplicates removed: {duplicate_count}")

# 4. CALCULATE TOTAL REVENUE
total_revenue = df['Total_Sales'].sum()

# 5. FIND BEST-SELLING PRODUCT

product_stats = df.groupby('Product')['Total_Sales'].sum()
best_product = product_stats.idxmax()
best_product_val = product_stats.max()

# 6. FINAL REPORT
print("\n========================================")
print("          SALES REPORT         ")
print("===========================================")
print(f"Total Revenue:         ${total_revenue:,}")
print(f"Best-Selling Product:  {best_product}")
print(f"Product Revenue:       ${best_product_val:,}")
print("----------------------------------------")


