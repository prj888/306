#!/usr/bin/env python3

import cgi
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

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
	error = "ERROR: Invalid entry - entry should be in the format numTest.py?numOne=10&numTwo=20"
	try:
		One = int(form.getvalue("numOne"))
		Two = int(form.getvalue("numTwo"))
	except:
		print(error)
		return False

	if (One == 0) or (Two == 0):
		print(error)

	if (One or Two) == "":
		print(error)
		return False

	result = One/Two
	out = "{0:d}/{1:d} = {2:.1f}"
	print(out.format(One,Two,result))



main()

print ('''\
</body>
</html>
''')
