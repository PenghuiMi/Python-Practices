''' Personal contact information QR code generator '''

import urllib
import os

# QR code from google chart rest api documented at:
# https://developers.google.com/chart/infographics/docs/qr_codes
qr_root_url = 'https://chart.googleapis.com/chart?'

vcard_template = '''BEGIN:VCARD
VERSION:4.0
N:%s;%s;;;
FN:%s %s
ORG:%s
TITLE:%s
TEL;TYPE=work,voice;VALUE=uri:%s
TEL;TYPE=home,voice;VALUE=uri:%s
ADR;TYPE=work:;;%s
ADR;TYPE=home:;;%s
EMAIL:%s
REV:20080424T195243Z
END:VCARD
'''

# Personal information input
print 'Please specify your personal contact information:'
print '-------------------------------------------------'
# TODO
# 1. Add photo
# 2. Add formate check and confirmation

Fname = raw_input('First Name:')
Lname = raw_input('Last Name:')
Org = raw_input('Organization:')
Title = raw_input('Title:')
TelW = raw_input('Work Number:')
TelH = raw_input('Home Number:')
AddW = raw_input('Work Addr:')
AddH = raw_input('Home Addr:')
Email = raw_input('Eamil:')

# vcard string generator
vcard_str = vcard_template % (Fname, Lname, Lname, Fname,Org,
                              Title, TelW, TelH, AddW, AddH, Email)

# query rest api to get qr code
query = {'cht':'qr', 'chs':'300x300', 'chl':vcard_str}

url = qr_root_url + urllib.urlencode(query)
u = urllib.urlopen(url)
image = u.read()

TargetFile = '%s-qr.png' % Fname
with open(TargetFile, 'wb') as f:
    f.write(image)

print 'QR code has been generated, file saved as:%s' % os.path.abspath(TargetFile)

os.system('start %s' % TargetFile)
