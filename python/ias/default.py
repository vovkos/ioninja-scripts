#...............................................................................
#
#  Use this script to define logic for packet transmission in Python language.
#
#...............................................................................

# TODO: write the main action sequence here

# prints will go both to session log and system log
print("Hello from Python in-app scripting!")

# we have event handlers below, so the script won't terminate here
# stop it manually by clicking the "Stop" button

def on_log_record(timestamp, record_code, data):
	# TODO: write the new log record handling logic here
	trace(f"on_log_record 0x{record_code: 016x}, {data}")

def pretransmit(data):
	# TODO: write the outbound packet preprocessing logic here
	transmit(data)
