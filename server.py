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
	'/write', 'write_users',

)

app = web.application(urls, globals())

class write_users:
	def WRITE(self):
		tree = xml.parse("user_data.xml")
		xmlRoot = tree.getroot()
		child = xml.Element("NewNode")
		xmlRoot.append(child)
		tree.write("user_data.xml")

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