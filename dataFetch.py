import json


def extract_customers_items(input_filename,output_filename_customers, output_filename_items):
    try:
        with open(input_filename,'r') as f:
            orders = json.load(f)

        customers = {}
        items = {}

        for order in orders:
            phone = order.get('phone')
            name = order.get('name')


            for item in order["items"]:
                item_name = item["name"]
                item_price = item["price"]

                if item_name not in items:
                    items[item_name] = {
                        "price": item_price,
                        "orders": 1
                    }
                else:
                    items[item_name]["orders"] = items[item_name]["orders"] + 1
    

            #only add if both exists
            if phone and name:
                if phone not in customers:
                     customers[phone] = name

        with open(output_filename_customers, 'w' ) as f:
            json.dump(customers,f,indent=4)
        
        with open(output_filename_items, 'w') as f:
             json.dump(items,f, indent=4)
            
        print(f"Successfully created {output_filename_customers}")
        print(f"Successfully created {output_filename_items}")
        print(f"Total unique customers: {len(customers)}")
        print(f"Total unique items: {len(items)}")

    except FileNotFoundError:
         print(f"Error: {input_filename} not found")
    except Exception as e:
         print(f"An error occurred: {e}")


     

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Make sure command: python script_name.py")
        sys.exit(1)



    input_filename = sys.argv[1]
    output_filename_customers = 'customers.json'
    output_filename_items = 'items.json'
    extract_customers_items(input_filename,output_filename_customers,output_filename_items)
    
   

    