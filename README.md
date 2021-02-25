# Velo'v scraping project

This projects aims to scrape and save realtime data from JC Decaux Velo'v service (Lyon’s self-service cycle scheme) for analysis purpose.
Data source: [Stations Vélo'v de la Métropole de Lyon](https://data.grandlyon.com/jeux-de-donnees/stations-velo-v-metropole-lyon/donnees)

## Requirements

Docker

## Run the container

To run the container with docker volumes for pesistent data:

```shell
docker run -it -v $(pwd)/logs:/usr/app/logs -v $(pwd)/data:/usr/app/data velov bash     
```