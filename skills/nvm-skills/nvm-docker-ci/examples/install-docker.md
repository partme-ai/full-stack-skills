## Instructions

Use `BASH_ENV` so non-interactive shells source nvm in Docker.

### Example

```Dockerfile
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
ENV BASH_ENV /home/user/.bash_env
RUN touch "${BASH_ENV}"
RUN echo '. "${BASH_ENV}"' >> ~/.bashrc
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | PROFILE="${BASH_ENV}" bash
RUN echo node > .nvmrc
RUN nvm install
```

Reference: https://github.com/nvm-sh/nvm/blob/master/README.md#installing-in-docker
