from dotenv import load_dotenv
import os
import requests

load_dotenv()
if os.getenv('BACKEND_URI'):
    backend_uri = os.getenv('BACKEND_URI')
else:
    backend_uri = "https://backend-chahineba-dev.apps.rm1.0a51.p1.openshiftapps.com/"

def login(username: str, password: str):
    try:
        print(backend_uri)
        # Send a POST request to the backend login endpoint
        response = requests.post(
            f"{backend_uri}/login",
            json={"username": username, "password": password}
        )
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response JSON
            response_data = response.json()
            
            # Extract the message and color from the response
            message = response_data[0]  # "Login successful!"
            color = response_data[1]
            return message, color
        else:
            # Handle non-200 status codes (e.g., 400 Bad Request, 500 Internal Server Error)
            error_message = "Invalid username or password!"
            return error_message, "red"
    except requests.exceptions.RequestException as e:
        # Handle connection errors, timeouts, etc.
        print(f"Error connecting to the backend: {e}")
        return "Unable to connect to the server. Please try again later.", "red"
    except Exception as e:
        # Handle any other unexpected errors
        print(f"Unexpected error: {e}")
        return "An unexpected error occurred. Please try again.", "red"


def register(username: str, email: str, password: str):
    try:
        # Send a POST request to the backend registration endpoint
        response = requests.post(
            f"{backend_uri}/register",
            json={"username": username, "email": email, "password": password}
        )
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response JSON
            response_data = response.json()
            
            # Extract the message and color from the response
            message = response_data[0]  # "Registration successful!"
            color = response_data[1]    # "green"
            return message, color
        else:
            # Handle non-200 status codes (e.g., 400 Bad Request, 500 Internal Server Error)
            error_message = response.json().get("message", "Registration failed.")
            return error_message, "red"
    except requests.exceptions.RequestException as e:
        # Handle connection errors, timeouts, etc.
        print(f"Error connecting to the backend: {e}")
        return "Unable to connect to the server. Please try again later.", "red"
    except Exception as e:
        # Handle any other unexpected errors
        print(f"Unexpected error: {e}")
        return "An unexpected error occurred. Please try again.", "red"