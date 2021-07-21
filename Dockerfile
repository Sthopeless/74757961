FROM alpine:3.14

LABEL Maintainer="Sthope" \
      Description="Unlock Zigbee Tuya Doorlocks with API" \
      version="0.1"

RUN apk --no-cache add \
 bash \
 mosquitto \
 mosquitto-clients \
 python3-dev \
 build-base \
 py3-pip \
 patch

RUN pip3 install \
 tuya-iot-py-sdk \
 paho-mqtt \
 pycryptodome

RUN mkdir -p /home/tuyactl

ADD tuyactl/ /home/tuyactl/

ENTRYPOINT ["tail", "-f", "/dev/null"]
