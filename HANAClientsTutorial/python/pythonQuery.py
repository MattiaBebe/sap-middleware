import platform 
import time
from hdbcli import dbapi

#verify the architecture of python 
def attesa(time):{
   time.sleep(time)
}

print("Platform architecture: "+ platform.architecture()[0])
time = 5
attesa
for contatore in range(100):{
#print("connection testing refresh every 5 seconds")
}

#initialize connection 
conn = dbapi.connect(
	#OPTION1, retrive the connection parameters from the hdbuserstore
	#key = 'USER1UserKey' , #address, port user and password are retrive from the hdbuserstore
	
	#OPTION 2, specify the connection parameter
	address = '192.168.0.2',
	port = '30213',
	user = 'ODBC_USER',
	password = 'CyPAG2021',
	
	#ADDITIONAL PARAMETERS 
	#encript =True, #must set on true when connection to HANA as a service 
	#encription is default set when connecting on port 443 with hana 
	#SslValidateCertificate = False #Must be set to false when connecting 
	#to an SAP HANA, express edition instance that uses a self-signed certificate

    #questa è la prima modifica al programma che faccio 

	#questa è la seconda modifica al programma che voglio mettere su git con una pull request
	
)
#if no errors print connected 
print('connected') 

cursor = conn.cursor()
sql_command = "SELECT TITLE, FIRSTNAME,  NAME from HOTEL.CUSTOMER;" #this is a test for a query hotel.customer doesn't exist
cursor.execute (sql_command)
rows = cursor.fetchall()
for row in rows:
	for col in row:
		print ("%s" %col, end="")
	print (" ")
cursor.close()
print ("\n")

#prepared statement example 
sql_command2 = "call HOTEL.SHOW_RESERVATIONS (?,?);"
parameters = [11, "2021-09-02"]
cursor.execute(sql_command2)
rows = cursor.fetchall()
for row in rows:
	for col in row:
		print("%s" %col, end="")
	print ("")
cursor.close()
conn.close() 
