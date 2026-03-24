## Instructions

A more robust Docker setup for CI/CD jobs.

### Example

```Dockerfile
FROM ubuntu:latest
ARG NODE_VERSION=20
RUN apt update && apt install curl -y
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
ENV NVM_DIR=/root/.nvm
RUN bash -c "source $NVM_DIR/nvm.sh && nvm install $NODE_VERSION"
ENTRYPOINT ["bash", "-c", "source $NVM_DIR/nvm.sh && exec \"$@\"", "--"]
CMD ["/bin/bash"]
```

Reference: https://github.com/nvm-sh/nvm/blob/master/README.md#installing-in-docker-for-cicd-jobs
