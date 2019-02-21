#!C:/Python27/python.exe
print("Content-Type: text/html; chartset=utf-8\n\n")
import pymysql
import cgi, cgitb
form = cgi.FieldStorage()
in_prod_name =""
in_prod_category =""
in_prod_radio =""
productName = form.getvalue("productName")
productCategory = form.getvalue("productCategory")
productMade = form.getvalue("productMade")
if productName != None: 
 in_prod_name =productName
 in_prod_category =productCategory
 in_prod_radio =productMade
 conn = pymysql.connect (host="localhost", user= "root", passwd="",db="python")
 myCursor = conn.cursor()
 sql = "insert INTO  form (prod_name,prod_cate,prod_radio) VALUES ( %s, %s, %s);"
 val =(in_prod_name,in_prod_category,in_prod_radio)
 myCursor.execute(sql,val )
 conn.commit()
 conn.close()
 print ("> Your Product has been Inserted, Please check your Input:")
 print("<p>Product Name: "+ in_prod_name +"</p>")
 print("<p>Product category: "+in_prod_category+"</p>")
 print("<p>Product Made:"+ in_prod_radio + "</p>")
 
 
 

else:
 print ("<html>")
 print ("<head>")
 print('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />')
 print ("<title>Self Form post</title>")
 print ("</head>")
 print ("<body>")
 print("<h1>Self Form post</h1>")
 print("<form id='form1' name='form1' method='post' action='form.py'>")
 print(" <p>Product Name:")
 print("<input type='text' name='productName' id='productName' /> </p>")
 print("<p>product Category:")
 print(" <input type='text' name='productCategory' id='productCategory' /></p>")
 print(" <p>product Made:  <input type='text' name='productMade' id='productMade' /></p> ")
 print(" <p> <input type='submit' name='button' id='button' value='Submit' /> ")
 print(" <input type='reset' name='button2' id='button2' value='Reset' />")
 print("</p>")
 print("</form>")
 print "</body>"
 print "</html>"

