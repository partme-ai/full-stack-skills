# Using volumes to persist MySQL data

```bash
# 1. Create a named volume
docker volume create mysql-data

# 2. Run MySQL with the volume mounted
docker run -d --name mysql \
  -e MYSQL_ROOT_PASSWORD=secret123 \
  -v mysql-data:/var/lib/mysql \
  -p 3306:3306 \
  mysql:8.4

# 3. Verify data persists
docker exec mysql mysql -uroot -psecret123 -e "CREATE DATABASE testdb;"
docker stop mysql
docker rm mysql
docker run -d --name mysql-new -v mysql-data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=secret123 -p 3306:3306 mysql:8.4
docker exec mysql-new mysql -uroot -psecret123 -e "SHOW DATABASES;"
# testdb still exists! ✅
```
