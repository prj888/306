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
	# print("First Name =",firstName)
	# print("Last Name=",lastName)
	# print("Gender= ",gender)
	# print("Email= ",email)
	# print("Password =",password)
	# print("Comments = ",comments)
	# Validate Text Portion
	test = True
	
	oldSubmit = '''<form name="membershipForm" action="process_signup_validate.py" method="GET" id="membershipForm" onsubmit="return submitCheck()">
		First Name:
		<input type="text" name="firstname" required value='firstName'>
		<span id="firstName">
		</span><br>

		Last Name:
		<input type="text" name="lastname" value = lastName>
		<br>
		Gender:<br>
		<input type="radio" name="gender" value="male">Male<br>
		<input type="radio" name="gender" value="female">Female<br>
		Email:
		<input type="email" name="email" value=email>
		<span id="email">
		</span>
		<br>
		Create Password:
		<input type="password" name="pass" value='password'>
		<span id="password">
		</span><br>
		<input type="hidden" id="reason" name="reason" value="Membership">
		<input type="reset" value="Reset">
		<input type="submit" value="Submit" onclick="submitCheck()"><br>
		</form>
		Comments:<br>
		<textarea rows="5" cols="55" name="comments" form="membershipForm" value=comments
			Enter Comments Here...</textarea>
		<span id="textarea">
		</span>'''
		
	if (firstName == "") or firstName == 'None':
		print(oldSubmit)
		#print("The first name box was unfilled, membership not complete please return to previous page!")
		test = False
	else:
		pass
	
	# Validate textarea
	if (comments == "") or comments == 'None':
		print("The comments box was unfilled, membership not complete please return to previous page!")
		test = False
	else:
		pass
	
	# Validate radio buttons
	if (gender == "") or gender == 'None':
		print("The gender selection was unfilled, membership not complete please return to previous page!")
		test = False
	else:
		pass
	
	# Validate password
	if (password == "") or password == 'None':
		print("The password box was unfilled, membership not complete please return to previous page!")
		test = False
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
			test = False	
	
	if test == True:
			print("SUCCESS! Thank you for signing up for an outdoor membership! <br>")
			print("The email you signed up with is ",email)
	elif test == False:
		return False

	
main()

print ('''\
</body>
</html>
''')