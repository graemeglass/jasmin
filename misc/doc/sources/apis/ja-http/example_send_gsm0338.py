# Python example
# http://jasminsms.com
import urllib2
import urllib

baseParams = {'username':'nathalie', 'password':'secret', 'to':'+24206155423', 'content':'Hello'}

# Send an SMS-MT with minimal parameters
urllib2.urlopen("http://127.0.0.1:1401/send?%s" % urllib.urlencode(baseParams)).read()

# Send an SMS-MT with defined originating address
baseParams['from'] = 'Jasmin GW'
urllib2.urlopen("http://127.0.0.1:1401/send?%s" % urllib.urlencode(baseParams)).read()