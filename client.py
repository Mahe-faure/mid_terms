import socket
import time
import openpyxl

# Function to generate sample sensor data
def generate_sensor_data():
    # Simulate sensor data using a simple loop for demonstration
    sensor_data = []
    current_time = time.mktime(time.gmtime())
    for i in range(10):
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(current_time))
        rotation_count = 100 + i
        sensor_data.append(f"{timestamp}, {rotation_count}")
        current_time += 60  # Add 1 minute for each data point
    return sensor_data

# Load sensor data from an Excel file
wb = openpyxl.load_workbook('sensor_data.xlsx')  # Replace with your Excel file path
sheet = wb.active

# Create a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 12345)  # Use the server's IP and port
client_socket.connect(server_address)

for data_row in sheet.iter_rows(values_only=True):
    timestamp, rotation_count = data_row
    ping_message = f"Ping: {timestamp}, Count: {rotation_count}"
    start_time = time.time()
    client_socket.send(ping_message.encode())

    # Wait for a response or timeout
    client_socket.settimeout(5)  # Adjust the timeout as needed
    try:
        response = client_socket.recv(1024)
        end_time = time.time()
        rtt = end_time - start_time
        print(f"Received: {response.decode()}. RTT: {rtt} seconds")
    except socket.timeout:
        print("No response received. Packet lost.")

client_socket.close()
