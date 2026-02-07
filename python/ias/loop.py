#...............................................................................
#
#  The example below defines an infinite loop which sends packets with
#  ever-incrementing index. Don't let the *infinite* part scare you -- you can
#  always abort the execution of a script with the 'Stop' button.
#
#...............................................................................

import time

connect();

i = 0
while True:
	packet = f"packet {i}\r\n";
	transmit(packet);
	time.sleep(1); # wait one second and repeat
	i += 1
