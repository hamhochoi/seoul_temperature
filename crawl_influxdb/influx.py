from influxdb import InfluxDBClient
from datetime import datetime
from datetime import timezone
import os

#INFLUXDB_HOST = os.environ['INFLUXDB_HOST']
INFLUXDB_HOST = 'localhost'
INFLUXDB_ADMIN_USER_PASSWORD = 'root' #os.environ['INFLUXDB_ADMIN_USER_PASSWORD']
INFLUXDB_PORT = 8086 #os.environ['INFLUXDB_PORT']
INFLUXDB_DB = "temperature" #os.environ['INFLUXDB_DB']

is_connected = False
while (is_connected==False):
	try:
		client = InfluxDBClient(host=INFLUXDB_HOST, port=INFLUXDB_PORT, username=INFLUXDB_ADMIN_USER_PASSWORD, password=INFLUXDB_ADMIN_USER_PASSWORD)
		#client.create_database('temperature')
		client.switch_database('temperature')
		is_connected = True
	except:
		pass

def select():
	results = client.query(" SELECT temperature FROM temperature where station='Seoul' limit 5")
	print (results.raw)


def insert(infos):
	station, weather, visibility, \
	cloud, temp, wind_dir, wind_speed, \
	hum, _, air_pressure 						= infos
	station = str(station)[4:-5]
	weather = str(weather)[4:-5]
	visibility = str(visibility)[4:-5]
	cloud = str(cloud)[4:-5]
	temp = str(temp)[4:-5]
	wind_dir = str(wind_dir)[4:-5]
	wind_speed = str(wind_speed)[4:-5]
	hum = str(hum)[4:-5]
	air_pressure = str(air_pressure)[4:-5]
	curr_time = datetime.now()
	curr_time = str(curr_time.replace(tzinfo=timezone.utc))


	json_body = [
		{
		    "measurement": "temperature",
		    "time": curr_time,
		    "fields": {
				"station": station,
				"weather": weather,
				"visibility": visibility,
				"cloud": cloud,
				"temperature": temp,
				"wind_dir": wind_dir,
				"wind_speed": wind_speed,
				"humidity": hum,
				"air_pressure": air_pressure
		    }
		}
	]


	result = client.write_points(json_body)
	#print (result)


if __name__ == "__main__":
	#insert(1)
	select()


