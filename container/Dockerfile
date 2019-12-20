# gnuradio/pelican:latest
FROM alpine:3.8
MAINTAINER Andrej Rode <mail@andrejro.de>

ENV security_updates_as_of 2018-12-26
RUN apk update && apk add python3 && apk add git && apk add bash && apk add openssh-client && rm -rf /var/cache/apk/*
RUN python3 -m pip install pelican bs4 markdown
RUN mkdir -p /plugins && cd /plugins && git clone --recursive https://github.com/getpelican/pelican-plugins
