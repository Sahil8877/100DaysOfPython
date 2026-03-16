import requests
import datetime
now_date = datetime.datetime.now().date()
print(now_date.strftime('%Y%m%d'))

header = { #header with token data
    'X-USER-TOKEN' : 'ashkdhikdhajdbakduq8877', 
}

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "sahil8877"
GRAPH_ID = "sahilgraph1"
GRAPH_NAME = "sahilsgraph8877"

def create_user():
    params = {
        'token' : 'ashkdhikdhajdbakduq8877',
        'username' : 'sahil8877',
        'agreeTermsOfService' : 'yes',
        'notMinor' : 'yes',
    }
    create_request = requests.post(url=PIXELA_ENDPOINT,json=params)
    print(create_request.json())

def add_pixel():
    params = {
        'X-USER-TOKEN' : 'ashkdhikdhajdbakduq8877',
        'date' : now_date.strftime('%Y%m%d'),
        'quantity' : '50',
    }
    pixel_add_request = requests.post(url="https://pixe.la/v1/users/sahil8877/graphs/sahilgraph1",headers=header,json=params)
    print(pixel_add_request.json())

def create_graph():
    params={
        'id' : 'sahilgraph1',
        'name' : 'sahilsgraph8877',
        'unit' : 'commit',
        'type' : 'int',
        'color' : 'ajisai',
    }
    graph_create_request = requests.post(url="https://pixe.la/v1/users/sahil8877/graphs",headers=header,json=params)
    print(graph_create_request.json())

def update_pixel():
    params = {
        'name' : GRAPH_NAME,
        'unit' : 'commit',
        'color' : 'kuro',
    }
    update_pixel_request = requests.put(url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}",headers=header,json=params)
    print(update_pixel_request.json())

def delete_pixel():
    delete_pixel_request = requests.delete(url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}",headers=header)
    print(delete_pixel_request.json())
