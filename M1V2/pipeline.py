services:
    postgres:
    image: postgres:13
    environment:
        POSTGRES_USER: airflow
        POSTGRES_PASSWORD: airflow
        POSTGRES_DB: airflow
    volumes:
        - postagres-db-voolume:/var/lib/postgresql/data
    healthcheck:
        test:["CMD","pg_isready","-U","airflow"]
        interval: 5s
        retries: 5
    restart: always

docker run-it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi"
  -v /workspaces/DDLZoomcamp25-DE
  -p 5432:5432 \

  postgres:13

docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v c:/Users/alexe/git/data-engineering-zoomcamp/week_1_basics_n_setup/2_docker_sql/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:13