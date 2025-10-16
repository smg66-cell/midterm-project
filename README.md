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
   

  
