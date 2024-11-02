FROM alpine:3.20.3 AS base
LABEL AUTHOR="Frédéric Loulergue"

ARG USERNAME=default_user
ARG USERID=1000

RUN echo "==============================="
RUN echo "$USERNAME ($USERID)"
RUN echo "==============================="

RUN apk update && \
    apk add --no-cache \
        python3 \
        py3-pip \
        bash \
        shadow \
        libffi-dev \
        musl-dev \
        gcc

RUN echo "UID_MAX 9223372036854775807" > /etc/login.defs && \
    /usr/sbin/useradd -m -d /home/user -s /bin/bash -u ${USERID} ${USERNAME}

USER ${USERNAME}

# Créer un environnement virtuel
RUN python3 -m venv /home/user/venv

# Activer l'environnement virtuel et installer les paquets
RUN /home/user/venv/bin/pip install --upgrade pip && \
    /home/user/venv/bin/pip install django==5.1.1 django-bootstrap5 tzdata

RUN echo 'export PS1="[ $(whoami) | \w ] "' >> /home/user/.bashrc && \
    echo 'source /home/user/venv/bin/activate' >> /home/user/.bashrc && \
    mkdir /home/user/workspace

WORKDIR /home/user/workspace

CMD ["/bin/bash"]

