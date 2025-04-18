# server_test.py (run this on the Raspberry Pi)
import bluetooth

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(("", bluetooth.PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]
bluetooth.advertise_service(
    server_sock,
    "New RAAVC Device",
    service_classes=[bluetooth.SERIAL_PORT_CLASS],
    profiles=[bluetooth.SERIAL_PORT_PROFILE]
)

print(f"[SERVER] Waiting for connection on RFCOMM channel {port}...")

client_sock, client_info = server_sock.accept()
print(f"[SERVER] Accepted connection from {client_info}")

try:
    data = client_sock.recv(1024)
    print(f"[SERVER] Received: {data.decode()}")
except Exception as e:
    print(f"[SERVER] Error: {e}")

client_sock.close()
server_sock.close()