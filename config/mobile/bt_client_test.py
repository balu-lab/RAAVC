# client_test.py
import bluetooth

TARGET_NAME = "New RAAVC Device"
print("[CLIENT] Scanning for devices...")
nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True)

addr = None
for bdaddr, name in nearby_devices:
    print(f"Found: {name} - {bdaddr}")
    if name == TARGET_NAME:
        addr = bdaddr
        break

if addr is None:
    print("[CLIENT] Target device not found.")
    exit()

print(f"[CLIENT] Connecting to {addr} on RFCOMM channel 1...")
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((addr, 1))

message = "Hello from client!"
sock.send(message)
print(f"[CLIENT] Sent: {message}")

sock.close()