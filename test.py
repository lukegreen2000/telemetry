import can

# Set up the CAN bus interface with the correct bitrate and interface
bus = can.interface.Bus(channel='can0', bustype='socketcan', bitrate=50000)

# Set up a message listener to print any received messages to the console
#def print_message(msg):
    #print(msg)

notifier = can.Notifier(bus, [can.Printer()])
# Wait for incoming messages indefinitely
while True:
    message = bus.recv()
    print("1")
    pass