# from flask import Flask, jsonify
# import requests
# import time

# app = Flask(__name__)

# # Configuration
# API_BASE_URL = "http://20.244.56.144/test"
# HEADERS = {
#     "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzE4MzU3MzA4LCJpYXQiOjE3MTgzNTcwMDgsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6IjY2M2ZkZDIyLTQ4ODctNGRiZi04MWZkLWEyOTZhN2U2MjM3MiIsInN1YiI6IjIwZXBjaTAwOEBza2NldC5hYy5pbiJ9LCJjb21wYW55TmFtZSI6ImdvTWFydCIsImNsaWVudElEIjoiNjYzZmRkMjItNDg4Ny00ZGJmLTgxZmQtYTI5NmE3ZTYyMzcyIiwiY2xpZW50U2VjcmV0IjoiWG9MY1VDcGlnT2pLSWxheCIsIm93bmVyTmFtZSI6IkJhbGFtaXRocmFuIFMiLCJvd25lckVtYWlsIjoiMjBlcGNpMDA4QHNrY2V0LmFjLmluIiwicm9sbE5vIjoiMjBlcGNpMDA4In0.u221WAWEGRJiMClEo78hI8GYgSKLgUpcwXlnWyX3fmg"
# }
# WINDOW_SIZE = 10
# ENDPOINTS = {
#     'p': 'primes',
#     'f': 'fibo',
#     'e': 'even',
#     'r': 'rand'
# }

# # Store the current state of numbers
# window_state = {
#     'p': [],
#     'f': [],
#     'e': [],
#     'r': []
# }

# def fetch_numbers(endpoint):
#     url = f"{API_BASE_URL}/{endpoint}"
#     response = requests.get(url, headers=HEADERS, timeout=0.5)
#     if response.status_code == 200:
#         numbers = response.json().get('numbers', [])
#         print(response.json())
#         return numbers

#     return []

# @app.route('/numbers/<id>', methods=['GET'])
# def get_numbers(id):
#     if id not in ENDPOINTS:
#         return jsonify({"error": "Invalid ID"}), 400

#     endpoint = ENDPOINTS[id]
#     new_numbers = fetch_numbers(endpoint)


#     previous_state = window_state[id][:]
#     current_state = list(set(previous_state + new_numbers))[:WINDOW_SIZE]
#     window_state[id] = current_state
#     print(previous_state,current_state,new_numbers)
#     if len(current_state) > WINDOW_SIZE:
#         current_state = current_state[-WINDOW_SIZE:]

#     avg = sum(current_state) / len(current_state) if current_state else 0.0

#     return jsonify({
#         "numbers": new_numbers,
#         "windowPrevState": previous_state,
#         "windowCurrState": current_state,
#         "avg": round(avg, 2)
#     }), 200

# if __name__ == '__main__':
#     app.run(port=9876)
from flask import Flask, jsonify
import requests
import time
import jwt

app = Flask(__name__)

# Configuration
API_BASE_URL = "http://20.244.56.144/test"
BEARER_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzE4MzU3NjY1LCJpYXQiOjE3MTgzNTczNjUsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6IjY2M2ZkZDIyLTQ4ODctNGRiZi04MWZkLWEyOTZhN2U2MjM3MiIsInN1YiI6IjIwZXBjaTAwOEBza2NldC5hYy5pbiJ9LCJjb21wYW55TmFtZSI6ImdvTWFydCIsImNsaWVudElEIjoiNjYzZmRkMjItNDg4Ny00ZGJmLTgxZmQtYTI5NmE3ZTYyMzcyIiwiY2xpZW50U2VjcmV0IjoiWG9MY1VDcGlnT2pLSWxheCIsIm93bmVyTmFtZSI6IkJhbGFtaXRocmFuIFMiLCJvd25lckVtYWlsIjoiMjBlcGNpMDA4QHNrY2V0LmFjLmluIiwicm9sbE5vIjoiMjBlcGNpMDA4In0.I9RF5iv6Ys1tTOYAO_RqSFQapXVfEIiUCHL1HKw8Ld0"
HEADERS = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}
WINDOW_SIZE = 10
ENDPOINTS = {
    'p': 'primes',
    'f': 'fibo',
    'e': 'even',
    'r': 'rand'
}

# Store the current state of numbers
window_state = {
    'p': [],
    'f': [],
    'e': [],
    'r': []
}



def fetch_numbers(endpoint):


    url = f"{API_BASE_URL}/{endpoint}"
    start_time = time.time()
    response = requests.get(url, headers=HEADERS, timeout=0.5)
    if response.status_code == 200:
        numbers = response.json().get('numbers', [])
        return numbers

    return []

@app.route('/numbers/<id>', methods=['GET'])
def get_numbers(id):

    endpoint = ENDPOINTS[id]
    new_numbers = fetch_numbers(endpoint)

    previous_state = window_state[id][:]
    current_state = list(set(previous_state + new_numbers))[:WINDOW_SIZE]
    window_state[id] = current_state

    if len(current_state) > WINDOW_SIZE:
        current_state = current_state[-WINDOW_SIZE:]

    avg = sum(current_state) / len(current_state) if current_state else 0.0

    return jsonify({
        "numbers": new_numbers,
        "windowPrevState": previous_state,
        "windowCurrState": current_state,
        "avg": round(avg, 2)
    }), 200

if __name__ == '__main__':
    app.run(port=9876)
