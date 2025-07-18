import sys
from time import sleep


def display(message):
    print(message)
    for i in range(6):
        print("\r* ", end="")
        sys.stdout.flush()
        sleep(1)
        print("\r *", end="")
        sys.stdout.flush()
        sleep(1)
    return False


def is_inrange(value, min_value, max_value):
    return min_value < value < max_value


def check_vitals(value, min_value, max_value, message):
    return True if is_inrange(value, min_value, max_value) else display(message)


def check_temp(temperature):
    return check_vitals(temperature, 95, 102, "Temperature critical!")


def check_pulse(pulseRate):
    return check_vitals(pulseRate, 60, 100, "Pulse Rate is out of range!")


def check_spo2(spo2):
    return check_vitals(spo2, 90, 100, "Oxygen Saturation out of range!")


def vitals_ok(temperature, pulse, spo2):
    return check_temp(temperature) and check_pulse(pulse) and check_spo2(spo2)
