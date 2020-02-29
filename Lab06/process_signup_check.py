#!/usr/bin/env python3
import cgi
import cgitb; cgitb.enable()
import os

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
	usersFile = open("USERS.txt", "r+")
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
	if (firstName == "") or firstName == 'None':
		print("The first name box was unfilled, membership not complete please return to previous page!")
		test = False
	else:
		pass
	# Validate textarea
	if (comments == "") or comments == 'None':
		print("The comments box was unfilled, membership not complete please return to previous page!")
		test = False

	# Validate radio buttons
	elif (gender == "") or gender == 'None':
		print("The gender selection was unfilled, membership not complete please return to previous page!")
		test = False
		# Validate password
	elif (password == "") or password == 'None':
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
		if digit == False:
			print("The password entered did not contain a number, membership not complete please return to previous page!")
			test = False
		elif digit == True:
			test = True
	if test == True:
		first = usersFile.read(1)
		if not first:
			append = True
			print("if not")
		else:
			usersFile.seek(0, os.SEEK_SET)
			print("else")
			for line in usersFile:
				print("for")
				userInfo = line.split()
				print(userInfo[3])
				if userInfo[3] == email:
					print("A registration already exists for the email that was entered, if this is an issue please return to the previous page.")
					append = False
					return False
				else:
					append = True
				
	elif test == False:
		append = False
		return False
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
		usersFile.seek(0,os.SEEK_END)
		string = firstName+'\t'+lastName+'\t'+gender+'\t'+email+'\t'+password+'\t'+comments+'\n'
		usersFile.write(string)
	elif append == False:
		return False


	#ALWAYS EXECUTE
	usersFile.close()


main()

print ('''\
</body>
</html>
''')
