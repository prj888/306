#!/usr/bin/env python3
import cgi
import cgitb; cgitb.enable()
import os
import html

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
	usersFile = open("USERS.txt", "r+")  #Opens USERS file
	error = "AN ERROR OCCURRED!"
	try: #Ensures the proper boxes are filled in
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
	test = True  #Sets default
	append = False #sets default
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
	else: #checks to see if a digit is present in the password
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
	if test == True: #If the form passes all tests
		first = usersFile.read(1)
		if not first:
			append = True
		else:
			usersFile.seek(0, os.SEEK_SET) #moves seek to beginning of file to read lines
			for line in usersFile:
				userInfo = line.split()
				if userInfo[3] == email:
					print("A registration already exists for the email that was entered, if this is an issue please return to the previous page.")
					append = False
					return False
				else:
					append = True
				
	elif test == False: #If form data was not valid for some reason
		append = False
		return False
	if append == True:
		#escape non-valid symbols "<>&"
		firstName = html.escape(firstName)
		lastName = html.escape(lastName)
		gender = html.escape(gender)
		email = html.escape(email)
		comments = html.escape(comments)
		password = html.escape(password)
		print(firtName)
#Display success message
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
		usersFile.seek(0,os.SEEK_END) #Places seek at end of file to append Data
		string = firstName+'\t'+lastName+'\t'+gender+'\t'+email+'\t'+password+'\t'+comments+'\n'
		usersFile.write(string) #Append new user data
	elif append == False:
		return False


	#ALWAYS EXECUTE
	usersFile.close()


main()

print ('''\
</body>
</html>
''')
