#!/usr/bin/env python
import os
import web
import xml.etree.ElementTree as ET
import numbers

tree = ET.parse('user_data.xml')
root = tree.getroot()

urls = (
	'/users', 'list_users',
	'/(.*)', 'get_user'
)

app = web.application(urls, globals())

class list_users:        
	def GET(self):
		output = 'users:[';
		for child in root:
			print 'child', child.tag, child.attrib
			output += str(child.attrib) + ','
		output += ']';
		return output

class get_user:
	def GET(self, user):
		answer = ""
		if user.isdigit():
			answer = str(int(user)*3)

		else:
			answer = user + " potato"
		return answer

if __name__ == '__main__':
	_port = int(os.environ.get('PORT', 8080))
	app.run()