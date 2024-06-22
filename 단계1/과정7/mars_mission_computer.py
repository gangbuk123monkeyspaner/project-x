    import time #5초 주기를 위한 모듈 불러오기
    from 'C:/Users/USER/Desktop/파이썬 프로그래밍 모음집/project-x-1-1/단계1/과정7/1-6 모듈 불러오기용.py' import DummySensor

    class MissionComputer:
        def __init__(self):
            self.env_values = {        
            'mars_base_internal_temperature' : 0,
            'mars_base_internal_humidity' : 0,
            'mars_base_external_illuminance' : 0,
            'mars_base_internal_co2' : 0,
            'mars_base_internal_oxygen' : 0
            }
        def get_sensor_data(self):
            for i in range(5):
                ds = DummySensor()
                ds.set_env()           
                self.env_values = ds.get_env() 
                print(self.env_values)
                time.sleep(5)
    RunComputer = MissionComputer()
    RunComputer.get_sensor_data()