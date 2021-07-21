FROM alpine:3.14

LABEL Maintainer="Sthope" \
      Description="Unlock Zigbee Tuya Doorlocks with API" \
      version="0.1"

RUN mkdir -p /home/tuya_doorlock

ADD tuya_doorlock/ /home/tuya_doorlock/

RUN apk --no-cache add \
 bash \
 nano \
 mosquitto \
 mosquitto-clients \
 python3-dev \
 build-base \
 py3-pip

RUN pip3 install \
 tuya-iot-py-sdk \
 paho-mqtt \
 pycryptodome

WORKDIR /home/tuya_doorlock

ENTRYPOINT ["/bin/bash"]