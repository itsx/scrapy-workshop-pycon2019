FROM ubuntu:16.04

COPY ./entrypoint.sh /tmp/entrypoint.sh
#COPY ./create_proxy_list.py /usr/local/bin/create_proxy_list.py
COPY ./requirements.txt /tmp/requirements.txt

RUN apt-get update -q \
 && apt-get install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    curl \
    git \
    libffi-dev \
    libjpeg-turbo8 \
    liblcms2-2 \
    libssl-dev \
    libtiff5 \
    libtool \
    libwebp5 \
    python \
    python-dev \
    zlib1g \
 && curl -sSL https://bootstrap.pypa.io/get-pip.py | python \
 && pip install --no-cache-dir \
    -r /tmp/requirements.txt \
    scrapyd \
 && apt-get purge -y --auto-remove \
    build-essential \
    curl \
    git \
    libffi-dev \
    libssl-dev \
    libtool \
    python-dev \
 && rm -rf /var/lib/apt/lists/*

COPY ./scrapyd.conf /etc/scrapyd/

VOLUME /etc/scrapyd /var/lib/scrapyd
EXPOSE 6800
EXPOSE 6080

ENTRYPOINT ["/tmp/entrypoint.sh"]

CMD ["scrapyd", "--logfile=/var/log/scrapyd.log", "--pidfile="]
