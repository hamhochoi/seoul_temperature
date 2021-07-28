# READ ME

## Introduction
- This project contains 2 different modules.
- The first service crawl data from website https://web.kma.go.kr/eng/weather/forecast/current_korea.jsp and save the data to Mysql database. A web server run by php will read the data from the database and an Android app will retrieve 24 hours temperature through that web server to display on a line chart.

- The second service crawl data from above website and save to influxdb database. A grafana dashboard is created to monitor real-time data of Seoul.

- All services are built and run by docker-compose.

### Run MySQL crawler
- cd crawl_sql
- docker-compose up -d
- To turn down service: docker-compose down

### Run Influx crawler
- cd crawl_influxb
- docker-compose up -d
- To turn down service: docker-compose down

### Setup Grafana to connect to InfluxDB
- In Grafana, create data source with host = http://influxdb:8086 (dockername:8086)
- Create dashboard connect from the above data source. With query inspector: 
```
SELECT "temperature" FROM "temperature" WHERE ("station" = 'Seoul')
```

### Setup PHP web server
- go to localhost:800 to see 10 most recent Seoul's temperature data.

### To debug services
- Go to each container by the command:
```
docker exec -it <container name> /bin/bash
```

### Run Android app
- Download seoul_temperature.apk to an android phone and install it.
- Open the app and use.



Thanks for watching this repo!
