#!C:/Python27/python.exe
print("Content-Type: text/html; chartset=utf-8\n\n")
print("")
import cgi
print("<h1>Welcome to Python Programming </h1>")
print("<hr/>")
print("<h2>Form Handler Result Page \- Code Example</h2>")
form = cgi.FieldStorage()
firstName = form.getvalue("firstName")
lastName = form.getvalue("lastName")
school = form.getvalue("school")

print("<p>First Name: "+ firstName +"</p>")
print("<p>Last Name: "+lastName+"</p>")
print("<p>School:"+ school + "</p>")