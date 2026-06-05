# Port Mapping Reference

```
-p HOST_PORT:CONTAINER_PORT[/PROTOCOL]

# Map container port 80 to host port 8080
docker run -p 8080:80 nginx

# Map to random host port
docker run -p 80 nginx
docker port <container>      # See which host port was assigned

# Protocol-specific
docker run -p 8080:80/tcp -p 8080:80/udp nginx

# Bind to specific interface
docker run -p 127.0.0.1:8080:80 nginx   # localhost only
docker run -p 0.0.0.0:8080:80 nginx     # all interfaces

# Publish all EXPOSE'd ports to random host ports
docker run -P nginx
```

### In compose.yml
```yaml
ports:
  - "8080:80"              # host:container
  - "127.0.0.1:8443:443"   # bind to localhost
  - "8080:8080/udp"        # UDP
```
