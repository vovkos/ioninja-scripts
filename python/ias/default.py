#...............................................................................
#
#  Use this script to define logic for packet transmission in Python language.
#
#...............................................................................

# TODO: write the main action sequence here

# prints will go both to session log and system log
print("Hello from Python in-app scripting!\n");

# we have event handlers below, so the script won't terminate here
# stop it manually by clicking the "Stop" button

def on_log_record(timestamp, record_code, data):
	# TODO: write the new log record handling logic here

def pretransmit(data) {
	# TODO: write the outbound packet preprocessing logic here
	transmit(data);
