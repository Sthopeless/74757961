FROM alpine:3.14
LABEL Maintainer="Sthope" \
      Description="Unlock Zigbee Tuya Doorlocks with API " \
      version="0.1"

RUN apk --no-cache add mosquitto mosquitto-clients && \
    apk add python3-dev build-base py3-pip --update-cache && \
    pip3 install tuya-iot-py-sdk paho-mqtt pycryptodome
