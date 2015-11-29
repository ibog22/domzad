s = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%3D%22USDBYR%2CEURBYR%2CRUBBYR%22&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'
import urllib2
u = urllib2.urlopen(s)
data = u.read()

import json


parsed_data = json.loads(data)
x = 0

while x < 3:
      print parsed_data["query"]['results']['rate'][x]['Name'], parsed_data["query"]['results']['rate'][x]['Rate']
      x = x + 1

