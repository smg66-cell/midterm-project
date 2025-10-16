import json


def extract_customers(input_filename,output_filename):
    try:
        with open(input_filename,'r') as f:
            orders = json.load(f)

        customers = {}

        for order in orders:
            phone = order.get('phone')
            name = order.get('name')

            #only add if both exists
            if phone and name:
                if phone not in customers:
                     customers[phone] = name

        with open(output_filename, 'w' ) as f:
                json.dump(customers,f,indent=4)
            
        print(f"Successfully created {output_filename}")
        print(f"Total unique customers: {len(customers)}")

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
    output_filename = 'customers1.json'

    customers = extract_customers(input_filename,output_filename)
   

    