#!/usr/bin/env python3

import cgi, cgitb
cgitb.enable()

input_data = cgi.FieldStorage()

firstName = form.getvalue("firstname")
lastName = form.getvalue("lastname")

#generate output as feedback for the user
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

if firstName == None or lastName == None:
  print ('<p>Please fill out both food AND color</p>')
else:
  # Save result in file.  Use colon as separator
  outfile = open ("names.txt","a")
  outfile.write(first + " : " + last + "\n")
  outfile.close()

  print ('<h1>Thank you for filling out our survey</h1>')
  print ('<p>Your responses have been recorded as follows:</p>')
  print ('<ul>')
  print ('<li>First Name: ' + firstName + '</li>')
  print ('<li>Last Name: ' + lastName + '</li>')
  print ('</ul>')

print ('</body></html>')
