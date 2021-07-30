from datetime import datetime
from datetime import timezone
import mysql.connector
import time
import os

MYSQL_HOST = "localhost" #os.environ['MYSQL_HOST']
MYSQL_USER = "root" #os.environ['MYSQL_USER']
MYSQL_PASSWORD = "secret" #os.environ['MYSQL_PASSWORD']
MYSQL_DB = "Temperature" #os.environ['MYSQL_DB']

is_connected = False
while (is_connected == False):
	try:
		mydb = mysql.connector.connect(
		  host=MYSQL_HOST,
		  user=MYSQL_USER,
		  password=MYSQL_PASSWORD
		)
		is_connected = True
	except:
		time.sleep(5)
	
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE if not exists Temperature")
mycursor.execute("use Temperature")

mycursor.execute("create table if not exists temperature(\
		  Time varchar(50), Station varchar(50), \
		  Weather varchar(50), Visibility float, \
		  Cloud int(8), Temp float, WindDir varchar(10), \
		  WindSpeed float, Humidity int(8), AirPressure float)")


def select():
	mycursor = mydb.cursor()
	mycursor.execute("SELECT Time, Temp FROM temperature where Station='Seoul' order by Time desc limit 5")

	myresult = mycursor.fetchall()

	for x in myresult:
	  print(x)


def insert(infos):
	station, weather, visibility, \
	cloud, temp, wind_dir, wind_speed, \
	hum, _, air_pressure 			= infos

	station = str(station)[4:-5] 
	weather = str(weather)[4:-5]
	visibility = str(visibility)[4:-5]
	if (visibility == ''):
		visibility = -1

	cloud = str(cloud)[4:-5]
	if (cloud == ''):
		cloud = -1

	temp = str(temp)[4:-5]
	if (temp == ''):
		temp = -1

	wind_dir = str(wind_dir)[4:-5]
	wind_speed = str(wind_speed)[4:-5]
	if (wind_speed == ''):
		wind_speed = -1

	hum = str(hum)[4:-5]
	if (hum == ''):
		hum = -1

	air_pressure = str(air_pressure)[4:-5]
	if (air_pressure == ''):
		air_pressure = -1

	curr_time = datetime.now()
	curr_time = str(curr_time.replace(tzinfo=timezone.utc))

	mycursor = mydb.cursor()

	sql = "INSERT INTO temperature (Time, Station, Weather, \
					Visibility, Cloud, \
					Temp, WindDir, WindSpeed, \
					Humidity, AirPressure ) \
		VALUES ('%s', '%s', '%s', %f, %d, %f, '%s', %f, %d, %f)" %     (curr_time, station, weather, \
								 	float(visibility), int(cloud), float(temp), \
									wind_dir, float(wind_speed), \
									int(hum), float(air_pressure))

	#print (sql)
	mycursor.execute(sql)

	mydb.commit()

	#print(mycursor.rowcount, "record inserted.")


if __name__ == "__main__":
	#insert(1)
	select()


