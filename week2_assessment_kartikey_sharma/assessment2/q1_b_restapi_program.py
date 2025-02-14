import requests

API_URL = "http://127.0.0.1:8000/q1_app/list/"

def get_products():
    try:
        response = requests.get(API_URL)
        
        if response.status_code == 200:
            data = response.json() 
            products_list = []

            for product in data:
                product_info = {
                    "p_id": product.get("p_id"),
                    "p_name": product.get("p_name"),
                    "price": product.get("price"),
                    "quantity": product.get("quantity"),
                    "dop": product.get("dop")
                }
                products_list.append(product_info)

            return products_list
        else:
            print(f"Error: Unable to fetch data, Status Code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

products = get_products()
if products:
    print("Product Data List:")
    for product in products:
        print(product)
