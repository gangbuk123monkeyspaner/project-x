import random
class DummySensor:
    def __init__(self):
        self.env_values = {        
        'mars_base_internal_temperature' : 0,
        'mars_base_internal_humidity' : 0,
        'mars_base_external_illuminance' : 0,
        'mars_base_internal_co2' : 0,
        'mars_base_internal_oxygen' : 0
        }
    def set_env(self):               
        self.env_values['mars_base_internal_temperature'] = random.randrange(18,30)
        self.env_values['mars_base_internal_humidity'] = random.randrange(50,60)
        self.env_values['mars_base_external_illuminance'] = random.randrange(500,715)
        self.env_values['mars_base_internal_co2'] = random.uniform(0.02,0.1)
        self.env_values['mars_base_internal_oxygen'] = random.randrange(4,7)
    
    def get_env(self):
        return self.env_values
    
ds = DummySensor()
ds.set_env()
result = ds.get_env()
print(result)

