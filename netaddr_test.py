from netaddr import calculate

def test_netaddr():
	ipaddr_test = ['192.168.5.154', '129.0.0.1', '20.20.197.2', '145.52.22.4']
	netmask_test = ['255.255.255.192', '255.128.0.0', '255.0.0.0', '255.255.192.0']
	expected = ['192.168.5.128', '129.0.0.0', '20.0.0.0', '145.52.0.0']
	for i in range(len(ipaddr_test)):
		print('Test %d: ' % (i+1), end='')
		reality = calculate(ipaddr_test[i], netmask_test[i])
		if reality == expected[i]:
			print("passed")
		else:
			print("got %s, expected %s" % (reality, expected[i]))

test_netaddr()