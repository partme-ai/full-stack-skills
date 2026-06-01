# Web + Database on custom network

```bash
# 1. Create custom network
docker network create app-net

# 2. Start database
docker run -d --name db --network app-net   -e POSTGRES_PASSWORD=secret   -v pgdata:/var/lib/postgresql/data   postgres:16-alpine

# 3. Start web app (connects to db by name!)
docker run -d --name web --network app-net   -e DATABASE_URL=postgres://postgres:secret@db:5432/mydb   -p 8080:8080   myapp:latest

# 4. Verify: web can reach db via DNS
docker exec web ping -c 2 db     # ✅
docker exec web nslookup db      # ✅ resolves to 172.x.x.x
```
