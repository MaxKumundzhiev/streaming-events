# Spin up EdgeDB 
```bash
docker run --name edgedb -d \
  -e EDGEDB_SERVER_SECURITY=insecure_dev_mode \
  edgedb/edgedb \
  -p 5656:5656
```