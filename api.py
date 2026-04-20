import requests

BASE_URL = "https://ditch-exes-tribesman.ngrok-free.dev/customers"


def get_customers():
    return requests.get(BASE_URL).json()


def create_customer(data):
    return requests.post(BASE_URL, json=data).json()


def update_customer(cid, data):
    return requests.put(f"{BASE_URL}/{cid}", json=data).json()


def delete_customer(cid):
    return requests.delete(f"{BASE_URL}/{cid}").json()
