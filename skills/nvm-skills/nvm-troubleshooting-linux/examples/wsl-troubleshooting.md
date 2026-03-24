## Instructions

WSL troubleshooting for DNS resolution errors during install.

### Example

```sh
sudo rm /etc/resolv.conf
sudo bash -c 'echo "nameserver 8.8.8.8" > /etc/resolv.conf'
sudo bash -c 'echo "[network]" > /etc/wsl.conf'
sudo bash -c 'echo "generateResolvConf = false" >> /etc/wsl.conf'
sudo chattr +i /etc/resolv.conf
```

Reference: https://github.com/nvm-sh/nvm/blob/master/README.md#wsl-troubleshooting
