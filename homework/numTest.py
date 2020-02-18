#!/usr/bin/env python3

import cgi, cgitb
cgitb.enable()

input_data = cgi.FieldStorage()

print ("Content-Type: text/html")
print ()
print ('''\
<!DOCTYPE html>
<html>
<head>
<meta charset = "utf-8">
<title>Survey Feedback</title>
</head>
<body>
''')

def main():
	numOne = form.getvalue("numOne")
	numTwo = form.getvalue("numTwo")

	try:
		outOne = int(numOne)
		outTwo = int(numTwo)
	except:
		print("One of the variables is not a number!")

	if (numOne or numTwo) == 0:
		print("One of the variables is 0!")

	if (numOne or numTwo) == "":
		print("One of the variables is blank!")
