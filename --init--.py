from mycroft import MycroftSkill, intent_handler
from gpiozero import LED, OutputDevice

class LightFanControlSkill(MycroftSkill):
    def __init__(self):
        super().__init__()
        self.light = LED(27)  # Chân GPIO mà đèn được kết nối
        self.fan = OutputDevice(22)  # Chân GPIO mà quạt được kết nối

    def initialize(self):
        # Đăng ký skill với Mycroft
        self.register_intent_file('turn.light.on.intent', self.handle_turn_light_on)
        self.register_intent_file('turn.light.off.intent', self.handle_turn_light_off)
        self.register_intent_file('turn.fan.on.intent', self.handle_turn_fan_on)
        self.register_intent_file('turn.fan.off.intent', self.handle_turn_fan_off)

    @intent_handler('turn.light.on.intent')
    def handle_turn_light_on(self, message):
        self.light.on()
        self.speak_dialog('light.on')

    @intent_handler('turn.light.off.intent')
    def handle_turn_light_off(self, message):
        self.light.off()
        self.speak_dialog('light.off')

    @intent_handler('turn.fan.on.intent')
    def handle_turn_fan_on(self, message):
        self.fan.on()
        self.speak_dialog('fan.on')

    @intent_handler('turn.fan.off.intent')
    def handle_turn_fan_off(self, message):
        self.fan.off()
        self.speak_dialog('fan.off')

def create_skill():
    return LightFanControlSkill()