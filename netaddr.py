import sys

def print_usage():
	print('Usage: %s [ipaddr] [netmask]' % sys.argv[0])

def calculate(ipaddr, netmask):
	ipaddr_list, netmask_list = ipaddr.split('.'), netmask.split('.')
	if len(ipaddr_list) != 4 or len(netmask_list) != 4:
		return "Error: Invalid IP address or Netmask"
	result = ''
	for i in range(4):
		if int(ipaddr_list[i]) not in range(256) or int(netmask_list[i]) not in range(256):
			return "Error: Invalid IP address or Netmask"
		tmp = int(ipaddr_list[i]) & int(netmask_list[i])
		result = result + str(tmp) + '.'
	result = result[:-1]
	return result

def main():
	if len(sys.argv) != 3:
		print_usage()
	else:
		ipaddr = sys.argv[1]
		netmask = sys.argv[2]
		print("Network address:", calculate(ipaddr, netmask))

if __name__ == '__main__':
	main()