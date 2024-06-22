import random
import time
import platform
import psutil
import json

class DummySensor:
    def __init__(self):
        self.env_values = {        
            'mars_base_internal_temperature': 0,
            'mars_base_internal_humidity': 0,
            'mars_base_external_illuminance': 0,
            'mars_base_internal_co2': 0,    
            'mars_base_internal_oxygen': 0
        }
    
    def set_env(self):               
        self.env_values['mars_base_internal_temperature'] = random.randrange(18, 30)
        self.env_values['mars_base_internal_humidity'] = random.randrange(50, 60)
        self.env_values['mars_base_external_illuminance'] = random.randrange(500, 715)
        self.env_values['mars_base_internal_co2'] = random.uniform(0.02, 0.1)
        self.env_values['mars_base_internal_oxygen'] = random.randrange(4, 7)
    
    def get_env(self):
        return self.env_values

class MissionComputer:
    def __init__(self):
        self.env_values = {        
            'mars_base_internal_temperature': 0,
            'mars_base_internal_humidity': 0,
            'mars_base_external_illuminance': 0,
            'mars_base_internal_co2': 0,
            'mars_base_internal_oxygen': 0
        }
    
    def get_sensor_data(self):
        for i in range(5):
            ds = DummySensor()
            ds.set_env()           
            self.env_values = ds.get_env() 
            print(self.env_values)
            time.sleep(5)
    
    def get_mission_computer_info(self):
        info = {
            'Operating System': platform.system(),
            'OS Version': platform.version(),
            'CPU Type': platform.processor(),
            'CPU Cores': psutil.cpu_count(logical=False),
            'Memory Size': psutil.virtual_memory().total
        }
        print(json.dumps(info, indent=4))
    
    def get_mission_computer_load(self):
        load = {
            'CPU Usage': psutil.cpu_percent(interval=1),
            'Memory Usage': psutil.virtual_memory().percent
        }
        print(json.dumps(load, indent=4))

# Run the code
runComputer = MissionComputer()
runComputer.get_sensor_data()
runComputer.get_mission_computer_info()
runComputer.get_mission_computer_load()




