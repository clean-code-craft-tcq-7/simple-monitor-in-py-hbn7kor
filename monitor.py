import sys
import time
import random
import deep_translator

LANGUAGE = "german"
VITALS = [
    {"name": "temperature", "minvalue": 95, "maxvalue": 102, "message": "Temperature critical!"},
    {"name": "pulserate", "minvalue": 60, "maxvalue": 100, "message": "Pulse Rate is out of range!"},
    {"name": "spo2", "minvalue": 90, "maxvalue": 100, "message": "Oxygen Saturation out of range!"},
    {"name": "blood-sugar", "minvalue": 70, "maxvalue": 110, "message": "Blood sugar levels out of range!"},
    {"name": "blood-pressure", "minvalue": 90, "maxvalue": 150, "message": "Blood pressure levels out of range!"},
    {"name": "respiratory-rate", "minvalue": 12, "maxvalue": 20, "message": "Blood sugar levels out of range!"},
]


def display(message):
    print(translate(message, LANGUAGE))
    for i in range(6):
        print("\r* ", end="")
        sys.stdout.flush()
        time.sleep(1)
        print("\r *", end="")
        sys.stdout.flush()
        time.sleep(1)
    return False


def sensorStub():
    return {"temperature": random.choice(range(95, 102)), "pulserate": random.choice(range(60, 100)), "spo2": random.choice(range(90, 100)), "blood-sugar": random.choice(range(70, 110)), "blood-pressure": random.choice(range(90, 150)), "respiratory-rate": random.choice(range(12, 20))}


def translate(text, target):
    return deep_translator.GoogleTranslator(target=target).translate(text)


def is_inrange(value, min_value, max_value):
    return min_value <= value <= max_value


def check_vitals(value, min_value, max_value, message):
    return True if is_inrange(value, min_value, max_value) else display(message)


def vitals_ok(sensorstub):
    for obj in VITALS:
        if not check_vitals(sensorstub[obj["name"]], obj["minvalue"], obj["maxvalue"], obj["message"]):
            return False
    return True
