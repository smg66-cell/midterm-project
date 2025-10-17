Code Documentation
The Python script processes restaurant order data from a JSON file and extracts information, storing it in:

customers.json - Creates a mapping of phone numbers to customer names
items.json - Tracks each menu item with its price and how many times it was ordered

Output: Two JSON files: customers.json and items.json

How It Is Designed
Architecture
Read Orders → Process Data → Write Output Files
Function: extract_customers()
Arguments:

input_filename - File to process data from
output_filename_customers - Where customer names and phone numbers will be saved
output_filename_items - Where item data will be saved

Data Structures
1. Customer Dictionary:
json{
    "phone_number": "customer_name"
}
2. Items Dictionary:
json{
    "item_name": {
        "price": 13.95,
        "orders": 127
    }
}

Logic
1. Read Input

Opens and parses the JSON file
Loads the data into a Python list

2. Extract Customers

Loops through each order
Extracts phone and name fields
Adds to customers dictionary only if:

Both phone and name exist
Phone number not already recorded (prevents duplicates)



3. Analyze Items

For each order, loops through the items array
For each item:

If first time seeing this item: Creates a new entry with price and order count of 1
If item already exists: Increments the order count


Assumes price is consistent

4. Write Output

Saves customers dictionary to JSON file
Saves items dictionary to JSON file

5. Error Handling

Catches file not found errors
Handles JSON parsing errors


How to Use It
Basic Usage
bashpython dataFetch.py <input_json_file>
Example
bashpython dataFetch.py example_orders.json
Expected Output
Successfully created customers.json
Successfully created items.json
Total unique customers: 30
Total unique items: 45

   

  
