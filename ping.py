import platform    # For getting the operating system name
import subprocess  # For executing a shell command

def ping1(host):
	param = '-n' if platform.system().lower()=='windows' else '-c'
	command = ['ping', param, '1', host]
	output = ''
	if subprocess.call(command) == 0 :
		output = subprocess.check_output(command)

	return str(output)