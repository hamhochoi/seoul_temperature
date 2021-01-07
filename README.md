# READ ME

## Introduction
- This project contains 2 different modules.
- The first service crawl data from website https://web.kma.go.kr/eng/weather/forecast/current_korea.jsp and save the data to Mysql database. A web server run by php will read the data from the database and an Android app will retrieve 24 hours temperature through that web server to display on a line chart.

- The second service crawl data from above website and save to influxdb database. A grafana dashboard is created to monitor real-time data of Seoul.

- All services are built and run by docker-compose.

### Run MySQL crawler
cd crawl_sql
docker-compose up -d

### Run Influx crawler
cd crawl_influxsb
docker-compose up -d

### Run Android app
- Download seoul_temperature.apk to an android phone and install it.
- Open the app and use.

Thanks for watching this repo!
