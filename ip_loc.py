'''Get self ip address, and find the loc of a given ip address'''

import urllib

url_self_ip = 'http://www.telize.com/ip'
url_ip_loc = 'http://api.hostip.info/get_html.php?ip=%s&position=true'

ip_addr = urllib.urlopen(url_self_ip).read()
self_ip = ip_addr.rstrip('\n')

print '-----------------------------------------------------------'
print '---------  Python Tool for IP location look up  -----------'
print '-----------------------------------------------------------'
print
print 'Your ip address is:%s' % self_ip

loc_str = url_ip_loc % self_ip
loc = urllib.urlopen(loc_str).read()

print 'Your location is:'
print loc

ip_lookup = raw_input('Please specify the ip address that you want to lookup:')

# TODO - ip address validation

loc_str = url_ip_loc % ip_lookup
loc = urllib.urlopen(loc_str).read()

print 'Location of %s is:' % ip_lookup
print loc
