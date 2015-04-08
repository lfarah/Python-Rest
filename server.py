from flask import Flask,request,jsonify
import json

app = Flask(__name__)

@app.route('/hello')
def api_hello():
	if 'name' in request.args:
		list = [
		{'name': request.args['name'], 'age': request.args['age']},
		]
	# jsonify will do for us all the work, returning the
	# previous data structure in JSON
		return jsonify(results=list)

	else:
		return 'Hello John Doe'

@app.route("/")
def welcome():
	return "Welcome to the website. Possible method: http://127.0.0.1:5000/hello?name=Lucas&age=30"

@app.route("/save")
def wc():
	my_dict = {                   
  'Name':      'KAIRA',
  'Location':  u'Kilpisj\u00E4rvi',
  'Longitude': 20.76,
  'Latitude':  69.07
	}
	my_dict2 = {                   
  'Name':      'KAIRA',
  'Location':  u'Kilpisj\u00E4rvi',
  'Longitude': 20.76,
  'Latitude':  69.07
	}
	myArray = [my_dict,my_dict2]
	out_file = open("test.json","w")
	json.dump(myArray,out_file, indent=4)                                    
	out_file.close()
	return "saved"

@app.route("/open")
def opn():
	# Open the file for reading
	in_file = open("test.json","r")

# Load the contents from the file, which creates a new dictionary
	array = json.load(in_file)

# Close the file... we don't need it anymore  
	in_file.close()

# Print the contents of our freshly loaded dictionary
	return jsonify(results=array)

@app.route("/add")
def addNew():
	# Open the file for reading
	inFiled = open("test.json","r")
	arr = json.load(inFiled)
	inFiled.close()

	my_dict2 = {                   
  'Name':      'KURIO',
  'Location':  u'Kilpisj\u00E4rvi',
  'Longitude': 20.76,
  'Latitude':  69.07
	}

	arr.append(my_dict2)
# Load the contents from the file, which creates a new array

	
	out_file = open("test.json","w")
	json.dump(arr,out_file, indent=4)                                    
	out_file.close()
	return "added"

@app.route("/remove")
def remov():
	in_file = open("test.json","r")
	array = json.load(in_file)
	in_file.close()
	array.pop()
	
	out_file = open("test.json","w")
	json.dump(array,out_file, indent=4)                                    
	out_file.close()
	return "Last item removed"


if __name__ == "__main__":
	app.run()





   #return 'Hello ' + request.args['name'] + ', ' + request.args['age']
