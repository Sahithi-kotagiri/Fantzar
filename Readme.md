Code Explanation

mobile_factory.py:

Class MobileFactory: This class encapsulates the logic for creating orders for configurable mobiles.

Static Constants: It defines two dictionaries, PRICES and PARTS, which store the prices and names of different mobile components, respectively.

validate_order Method: This static method validates whether an order contains one and only one component of each type. It checks the uniqueness of component types in the order.

calculate_total Method: This static method calculates the total price of an order by summing up the prices of individual components.

create_order Method: This static method creates an order for configurable mobiles. It first validates the order, calculates the total price, retrieves the component names, and constructs the order response containing the order ID, total price, and component names.


test_mobile_factory.py:

Unit Tests: This file contains unit tests for the MobileFactory class methods.

test_validate_order: Tests the validate_order method to ensure it correctly validates orders.

test_calculate_total: Tests the calculate_total method to ensure it correctly calculates the total price of orders.

test_create_order: Tests the create_order method to ensure it correctly creates orders and constructs the order response.


main.py:

Flask API: This file implements a Flask API to expose endpoints for creating orders.

create_order Endpoint: Defines a POST endpoint /orders to accept JSON payloads containing lists of component codes.

Request Processing: Processes incoming requests, validates the components, and returns JSON responses with order details.


send_request.py:

HTTP Request Sender: This script sends a POST request to the Flask API to create an order for a configurable mobile.

requests Library: It utilizes the requests library to make HTTP requests.

Request Payload: Constructs a JSON payload with a list of component codes.

Response Handling: Prints the response received from the server, including order details.


How to Run:

Requirements:

Python 

Flask

Requests library


Steps:

Start the Flask server by running python main.py in a terminal window.

Open another terminal window and navigate to the project directory.

Run python send_request.py to send a POST request and create an order.

View the response received in the terminal window.

OR 

For powershell:

Invoke-WebRequest -Method POST -Uri "http://127.0.0.1:5000/orders" -ContentType "application/json" -Body '{"components":["I","A","D","F","K"]}'

For Unix based systems(Linux/MacOS)

curl -X POST -H "Content-Type: application/json" -d '{"components":["I","A","D","F","K"]}' http://127.0.0.1:5000/orders

