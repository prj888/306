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
	usersFile = open("USERS.txt", "a+")
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
	append = False
	print("CHECK POINT 1")
	if (firstName == "") or firstName == 'None':
		print("The first name box was unfilled, membership not complete please return to previous page!")
		test = False
		print("IF")
	else:
		print("ELSE")
		pass
	print("CHECK POINT 2")
	# Validate textarea
	if (comments == "") or comments == 'None':
		print("The comments box was unfilled, membership not complete please return to previous page!")
		test = False
		print("IF)")

	# Validate radio buttons
	elif (gender == "") or gender == 'None':
		print("The gender selection was unfilled, membership not complete please return to previous page!")
		test = False
		print("ELIF")
		# Validate password
	elif (password == "") or password == 'None':
		print("The password box was unfilled, membership not complete please return to previous page!")
		test = False
	else:
		print("ELSE")
		digit = False
		for i in password:
			print("for")
			if i.isdigit():
				print("if")
				digit = True
				break
			else:
				print("else")
				digit = False
		print("CHECK POINT 3")
		if digit == False:
			print("The password entered did not contain a number, membership not complete please return to previous page!")
			test = False
		elif digit == True:
			print("elif")
			test = True
			print("TEST: ",test)
	print("CHECK POINT 4")
	if test == True:
		for line in usersFile:
			userInfo = line.split()
			if userInfo[3] == email:
				print("A registration already exists for the email that was entered, if this is an issue please return to the previous page.")
				append = False
			else:
				print("else")
				append = True
				
	elif test == False:
		append = False
		return False
	print("CHECK POINT 5")
	if append == True:
		print('<img src="Mountain_Range.jpg" style="width:100%;" alt="Mountain Range">')
		print("<h1 style=text-align:center;> Paul's Outdoor Recreation</h1>")
		print("<nav style=text-align:center;>")
		print('<a href="index.html">Home</a> &nbsp;&nbsp;&nbsp;&nbsp;')
		print('<a href="products.html">Products</a>')
		print("</nav>")
		print("<br>SUCCESS! Thank you for signing up for an outdoor membership! <br><br>")
		print("You signed up with the following information:")
		print("<ul>")
		print("<li>")
		print("First Name:", firstName)
		print("</li>")
		print("<li>")
		print("Last Name:", lastName)
		print("</li>")
		print("<li>")
		print("Gender:", gender)
		print("</li>")
		print("<li>")
		print("Email:", email)
		print("</li>")
		print("<li>")
		print("Interests:", comments)
		print("</li>")
		print("</ul>")

		#USERS File Append Data
		string = firstName+'\t'+lastName+'\t'+gender+'\t'+email+'\t'+password+'\t'+comments+'\n'
		usersFile.write(string)
	elif append == False:
		print("elif)")
		return False


	print("CHECK POINT 5")
	#ALWAYS EXECUTE
	usersFile.close()


main()

print ('''\
</body>
</html>
''')
