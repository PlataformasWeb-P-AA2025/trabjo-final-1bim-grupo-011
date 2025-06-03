docker run --name postgres-db \
  -e POSTGRES_PASSWORD=oabenitez \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_DB=midb \
  -p 5433:5432 \
  -v /home/omer/postgres-init/:/docker-entrypoint-initdb.d/ \
  -d postgres