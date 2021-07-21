#!/usr/bin/env python3
 
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import json

from env import *

from tuya_iot import *
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES

pad_pkcs7 = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad_pkcs7 = lambda s: s[:-ord(s[len(s) - 1:])]

class AESCipher:
    """
    Usage:
        c = AESCipher('secret_key').encrypt('message')
        m = AESCipher('secret_key').decrypt(c)
    """

    def __init__(self, hex_key):
        self.key = hex_key.encode('utf-8')

    def __pad(self, s):
        return s + (self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE) \
               * chr(self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE)

    def __unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]

    def encrypt(self, raw):
        raw = self.__pad(raw)
        cipher = AES.new(self.key, AES.MODE_ECB)
        return cipher.encrypt(raw).hex().upper()

    def decrypt(self, enc):
        cipher = AES.new(self.key, AES.MODE_ECB)
        return self.__unpad(cipher.decrypt(enc)).decode('utf8')

def on_connect(client, userdata, flags, rc):
    client.subscribe(DOORLOCK_TOPIC + "/#")

def on_message(client, userdata, msg):

  if msg.topic == DOORLOCK_TOPIC_CMD and msg.payload.decode() == "unlock_door":
      afd = openapi.post('/v1.0/devices/' + ZIGBEE_LOCK + '/door-lock/password-ticket')
      x = json.dumps(afd)
      check_token = json.loads(x)
      PasswordTicket = check_token["result"]["ticket_key"]
      TICKETID = check_token["result"]["ticket_id"]
      encrypted_ticket = bytes.fromhex(PasswordTicket)
      decrypted_ticket = AESCipher(ACCESS_KEY).decrypt(encrypted_ticket)
      decrypted_msg = decrypted_ticket # result from Erol
      lock_pincode = pad(LOCKPINCODE.encode('UTF-8'), BLOCK_SIZE)
      cipher = AES.new(decrypted_msg.encode('utf8'), AES.MODE_ECB)
      ready_password = cipher.encrypt(lock_pincode)
      opendoor_password = ready_password.hex()
      openapi.post('/v1.0/devices/' + ZIGBEE_LOCK + '/door-lock/open-door', {
          'password_type': 'ticket',
          'password': opendoor_password,
          'ticket_id': TICKETID,
          })

openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY, ProjectType.SMART_HOME)
openapi.login(USERNAME, PASSWORD, COUNTRY_CODE, SCHEMA)

client = mqtt.Client(MQTT_CLIENT_ID)
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(MQTT_BROKER, MQTT_PORT)

client.loop_forever()