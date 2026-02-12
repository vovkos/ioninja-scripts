#...............................................................................
#
#  The example below works as a simple echo-server. Whatever is received, is
#  sent back immediately.
#
#...............................................................................

while True:
	data = receive()
	transmit(data)
