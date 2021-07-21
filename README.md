# Tuya Zigbee Doorlock using API

Install Python and the [pip requeriments are here](https://github.com/Sthopeless/74757961/blob/main/requirements.txt)  
  
  
Think this are all the necessary options to be configured in [env.py](https://github.com/Sthopeless/74757961/blob/main/env.py) file.  
  
| Env.py    |              |
| :-------- | :----------- |
ACCESS_ID   | iot.tuya.cloud Access ID
ACCESS_KEY  | iot.tuya.cloud Access Secret
USERNAME    | Tuya/Smartlife MobileAPP Username
PASSWORD    | Tuya/Smartlife MobileAPP Password
COUNTRY_CODE | Tuya/Smartlife MobileAPP Country Code
SCHEMA | Which MobileAPP are you using Tuya or Smartlife
ASSET_ID | shouldn't be necessary
ENDPOINT | Tuya url of your region (default Europe)
TUYA_UID | Tuya user UID
ZIGBEE_LOCK | Tuya Zigbee Doorlock UUID
LOCKPINCODE | Tuya Zigbee Doorlock Pincode
MQTT_BROKER | MQTT IP
MQTT_PORT | MQTT Port
MQTT_USERNAME | MQTT Username
MQTT_PASSWORD | MQTT Password
  
  
| Endpoint Region |  Url                            |
| :-------------- | :------------------------------ |
| America         | https://openapi.tuyaus.com      |
| China           | https://openapi.tuyacn.com      |
| Europe          | https://openapi.tuyaeu.com      |
| India           | https://openapi.tuyain.com      |
| Eastern America | https://openapi-ueaz.tuyaus.com |
| Western Europe  | https://openapi-weaz.tuyaeu.com |

## Using Docker 

1. Run the docker container with:
```
docker run -d --name tuya_doorlock ghcr.io/sthopeless/tuya_doorlock:latest
```

2. Exec into the container:
```
docker run -it --name tuya_doorlock ghcr.io/sthopeless/tuya_doorlock:latest
```

3. Edit the env.py file with your details
```
nano /home/tuyactl/env.py
```

4. Run python file and test
```
python3 /home/tuyactl/Zigbee_Doorlock.py
```

5. Send MQTT message:
```
  topic: TuyaLock/Doorlock
  payload: unlock_door
```