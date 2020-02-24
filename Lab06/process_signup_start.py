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
<title>Signup Feedback</title>
</head>
<body>
''')

def main():
	error = "AN ERROR OCCURRED!"
	try:
		firstName = str(form.getvalue("firstname"))
		lastName = str(form.getvalue("lastname"))
		gender = str(form.getvalue("gender"))
		email = str(form.getvalue("email"))
		password = str(form.getvalue("pass"))
		comments = str(form.getvalue("comments"))
	except:
		print(error)
		return False
	
	print("SUCCESS! Thank you for signing up for an outdoor membership! <br>")
	print("The email you signed up with is ",email)
	
main()

print ('''\
</body>
</html>
''')