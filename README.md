Code Documentation:

The python script processes the data of restaurant order from JSON file and extracts information and stores in:
1. customers.json - Creates a mapping of phone numbers to customer names
2. items.json - Tracks each menu item with its price and how many times it was ordered

Output: Two json files: customers.json and items.json

How it is Designed:
Read orders -> Process Data -> write output files

Function: extract_customers_items()
  arguments:
    1) input_filename (to process data)
    2) output_filename_customers (Where the customer's name and phone number will be saved)
    3) output_filename_items (Where the item data will be saved)

Data Structures:
1) Customer Dictionary:
   {
     "phone_number":"customer_name"
   }

2) Items dictionary
   {
     "item_name":{
         "price": float,
         "orders": int
     }
   }
   
Logic:
1) Read input
   Open a json file and parse it.
   Load the data into python list.

2) Extract Customers
   Loop through each order
   extract phone and name fields
   Adds to customers dictionary only if:
       Both phone and name exist
       To prevent duplicates: Check phone number not already recorded

3) Analyze Items
   For each order, loops through the items array
   For each item:
     If first time seeing this item: Creates a new entry with price and order count of 1
     If item already exists: Increments the order count
   Assuming price is consistent

4) Write Output
   Save customers dictionary to JSON file
   Save items dictionary to JSON file

4) Error Handling
   Catches file not found errors

How to Use it:
Basic Usage:
command:
python dataFetch.py <input_json_file>

Example:
python dataFetch.py example_orders.json
```

# Expected Output
```
Successfully created customers.json
Successfully created items.json
Total unique customers: 30
Total unique items: 45
   

  
