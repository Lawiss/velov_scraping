# Velo'v scraping project

This projects aims to scrape and save realtime data from JC Decaux Velo'v service (Lyon’s self-service cycle scheme) for analysis purpose.
Data source: [Stations Vélo'v de la Métropole de Lyon](https://data.grandlyon.com/jeux-de-donnees/stations-velo-v-metropole-lyon/donnees)

The project has been built in oder to be deployed on a Raspberry PI 3 B+ (armv7l) with docker.

## Requirements

- Python>=3.7
- pyyaml==5.4
- pandas==1.2.2
- requests==2.22.0

or Docker

## Run the container

To run the container in background with docker volumes for pesistent data:

```shell
docker build -t velov .
docker run -d -v $(pwd)/logs:/usr/app/logs -v $(pwd)/data:/usr/app/data velov    
```

## Settings

Currently the only setting available is the `SLEEP_TIME` parameter which is the time between each iteration of the scraping process.