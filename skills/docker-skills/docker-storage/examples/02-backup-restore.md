# Backup and restore a Docker volume

```bash
# === BACKUP ===
# Create a temporary alpine container that mounts:
# - the source volume at /source
# - the current directory at /backup
docker run --rm \
  -v mysql-data:/source:ro \
  -v $(pwd):/backup \
  alpine tar czf /backup/mysql-data-$(date +%Y%m%d).tar.gz -C /source .

# === RESTORE ===
# 1. Create a new (or ensure existing) volume
docker volume create mysql-data-restored

# 2. Restore from backup
docker run --rm \
  -v mysql-data-restored:/target \
  -v $(pwd):/backup \
  alpine tar xzf /backup/mysql-data-20250101.tar.gz -C /target

# 3. Verify: start a container using the restored volume
docker run --rm -v mysql-data-restored:/var/lib/mysql alpine ls /var/lib/mysql
```

### Automate with a backup script

```bash
#!/bin/bash
# backup-volume.sh — Backup a Docker volume to a timestamped tar.gz
VOLUME=${1:?Usage: $0 <volume-name>}
BACKUP_DIR=${2:-./backups}
mkdir -p "$BACKUP_DIR"
docker run --rm \
  -v "$VOLUME":/source:ro \
  -v "$(cd "$BACKUP_DIR" && pwd)":/backup \
  alpine tar czf "/backup/${VOLUME}-$(date +%Y%m%d-%H%M%S).tar.gz" -C /source .
echo "Backed up $VOLUME to $BACKUP_DIR"
```
