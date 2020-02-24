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
	print("First Name =",firstName)
	print("Last Name=",lastName)
	print("Gender= ",gender)
	print("Email= ",email)
	print("Password =",password)
	print("Comments = ",comments)
	# Validate Text Portion
	if (firstName == "") or firstName == 'None':
		print("The first name box was unfilled, membership not complete please return to previous page!")
	else:
		pass
	
	# Validate textarea
	if (comments == "") or comments == 'None':
		print("The comments box was unfilled, membership not complete please return to previous page!")
	else:
		pass
	
	# Validate radio buttons
	if (gender == "") or gender == 'None':
		print("The gender selection was unfilled, membership not complete please return to previous page!")
	else:
		pass
	
	# Validate password
	if (password == "") or password == 'None':
		print("The password box was unfilled, membership not complete please return to previous page!")
	else:
		digit = False
		for i in password:
			if i.isdigit():
				digit = True
				break
			else:
				digit = False
		if digit == True:
			pass
		elif digit == False:
			print("The password entered did not contain a number, membership not complete please return to previous page!")
				
	
	
	print("SUCCESS! Thank you for signing up for an outdoor membership! <br>")
	print("The email you signed up with is ",email)
	
main()

print ('''\
</body>
</html>
''')