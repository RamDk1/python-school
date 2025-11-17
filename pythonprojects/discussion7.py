# A Smartphone has two parts: its brand and its battery level. It also has one job, use an app that lowers the battery level depending on how long you use the app.

class Smartphone:
    def __init__(self, brand, battery_level):
        self.brand = brand
        self.battery_level = battery_level # Battery level 0-100

    def use_app(self, app_name, duration):
        
        battery_consumption = duration * 0.4
        if self.battery_level >= battery_consumption:
            self.battery_level -= battery_consumption
            return f"Used {app_name} for {duration} minutes. Battery level now is {self.battery_level:.1f}%"
        else:
            return f"Not enough battery to use {app_name} for {duration} minutes. Please recharge!"
        
phone = Smartphone("IPhone 15",50)
print(phone.use_app("Youtube",30))
print(phone.use_app("Instagram",50))