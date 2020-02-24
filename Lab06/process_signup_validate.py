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
	# Validate Text Portion
	if firstName == "":
		print("The first name box was unfilled, membership not complete please return to previous page!")
	else:
		pass
	
	# Validate textarea
	if comments == "":
		print("The comments box was unfilled, membership not complete please return to previous page!")
	else:
		pass
	
	# Validate radio buttons
	if gender == "":
		print("The gender selection was unfilled, membership not complete please return to previous page!")
	else:
		pass
	
	# Validate password
	if password == "":
		print("The password box was unfilled, membership not complete please return to previous page!")
	else if:
		digit = False
		for i in password:
			if i.isdigit():
				digit = True
				break
			else:
				digit = False
		if digit == True:
			pass
		else if digit == False:
			print("The password entered did not contain a number, membership not complete please return to previous page!")
				
	
	
	print("SUCCESS! Thank you for signing up for an outdoor membership! <br>")
	print("The email you signed up with is ",email)
	
main()

print ('''\
</body>
</html>
''')