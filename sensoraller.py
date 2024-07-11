import random
import json
import asyncio
import telegram
from variables import api_token,grp_chat_id
from telegram_module import Telegram_Module

telegram = Telegram_Module(api_token,grp_chat_id)
# this function checks for any parameter breach, returns true when breached else false
def check(parameter,sensor_data, alert_zones): #takes parameter, data from sensor and the dictionary alert_zones
    for key, value in alert_zones[parameter].items(): 
            if (key == 'Upper_Limit' and sensor_data > value) or (key == 'Lower_Limit' and sensor_data < value):
                print(f'{parameter}={sensor_data}',end=" ")
                return True
    return False

#function that reads the json file and deserializes it to a dicrtionary and returns the  dictionary
def read_json():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)   
    except FileNotFoundError as e:
        print("file not found")     #if file not found
    except json.JSONDecodeError:
        print("file not formated")  # if error in json file
    finally:
        return data


data=read_json()
co2=random.uniform(0,3000) # returns a random  floating point number between the given values
humidity =random.uniform(0,100)
temp =random.uniform(0,80)


#the parameters are passed to the check function, and then 
check_data_co2=check('co2',co2,data['alert_zones'])  
if check_data_co2==True:
    msg='warning!! co2 level seems alerting'
    print('warning!! co2 level seems alerting')
    print(f'Violation detected: ${msg}')
    asyncio.run(telegram.send_test_message(msg))
else:
    pass

check_data_humidity=check('humidity',humidity,data['alert_zones'])
if check_data_humidity==True:
    msg='warning!! humidity level seems alerting'
    print('warning!! humidity level seems alerting')
    print(f'Violation detected: ${msg}')
    asyncio.run(telegram.send_test_message(msg))
else:
    pass

check_data_temp=check('temp',temp,data['alert_zones'])
if check_data_temp==True:
    msg='warning!! temp level seems alerting'
    print('warning!! temp level seems alerting')
    print(f'Violation detected: ${msg}')
    asyncio.run(telegram.send_test_message(msg))
else:
    pass

