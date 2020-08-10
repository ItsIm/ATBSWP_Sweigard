import ipinfo, sys, pprint, requests
access_token = ''


if sys.argv[1] == 'ip':
	handler = ipinfo.getHandler(access_token)
	ip_address = sys.argv[2]
	details = handler.getDetails(ip_address)
	pprint.pprint(details.all)
elif sys.argv[1] == 'asn':
	asn = sys.argv[2]
	response = requests.get(f'http://ipinfo.io/{asn}/json?token={access_token}')
	print(response.text)
else:
	print('Неправильный запрос.')
