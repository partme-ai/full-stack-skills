# Your first Docker container

```bash
# 1. Verify Docker is installed
docker --version

# 2. Run hello-world (one-off container)
docker run hello-world

# 3. Run an interactive Ubuntu container
docker run -it ubuntu:22.04 bash
# Inside: whoami / cat /etc/os-release / exit

# 4. Run a background web server
docker run -d --name my-nginx -p 8080:80 nginx:alpine
curl localhost:8080
docker stop my-nginx
docker rm my-nginx
```
