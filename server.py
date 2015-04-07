#!/usr/bin/env python
import os
import web
import xml.etree.ElementTree as ET
import numbers

tree = ET.parse('user_data.xml')
root = tree.getroot()

urls = (
	'/users', 'list_users',
	'/potato/(.*)', 'get_user',
	'/write', 'write_users',
	'/getXml', 'get_xml',
	'/', 'greetings'


)

app = web.application(urls, globals())

class greetings:
	def GET(self):
		return "Welcome!"

class get_xml:
	def GET(self):
		answer = ""
		for node in root:
			answer += str(node)
		return answer


class write_users:
	def GET(self):
		doc = ET.SubElement(root, "user")
		co  = ET.SubElement(doc, 'age', name='15')
	 	ppl = ET.SubElement(co, 'name', name='Luis Lopez')
	 	idd  = ET.SubElement(doc, 'id', name='30')

		tree = ET.ElementTree(root)
		doc.append(co)
		doc.append(ppl)
		doc.append(idd)

		root.append(doc)
		tree.write("user_data.xml")
		return "wrote new line"

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