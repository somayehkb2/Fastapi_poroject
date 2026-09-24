import requests

def get_all_item():
    url = 'http://127.0.0.1:8000/getitems/'
    response = requests.get(url)

    if response.status_code != 200:
        return 'ERROR'
    else:
        return response.json()
    

def add_item(new_item):
    url =f'http://127.0.0.1:8000/add/{new_item}'
    response = requests.post(url)

    if response.status_code != 200:
        return 'ERROR'
    else:
        return response.json()

    
def delete_item(item):
    url = f"http://127.0.0.1:8000/deleteitem?item={item}"

    response = requests.delete(url)
    
    if response.status_code != 200:
        return 'ERROR'
    else:
        return response.json()
    

def update_index(index, new_item):
    url =f"http://127.0.0.1:8000/updateIndex?index={index}&new_item={new_item}"

    response = requests.put(url)
        
    if response.status_code != 200:
        return 'ERROR'
    else:
        return response.json()


    

if __name__ == '__main__':
    #print(get_all_item())
    #print(add_item(1000))
    #print(delete_item(30))
    print(update_index(0, 678))

