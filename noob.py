#!/usr/bin/env python

import time
import sys
sys.path.insert(0, '../GrovePi/Software/Python')
import grovepi
sys.path.insert(0, '../GrovePi/Software/Python/grove_rgb_lcd')
import grove_rgb_lcd


# === Led ===
class Led:

  def setName(self, name):
    self.name = name
    return self

  def initialize(self, options):
    self.name = options['name']
    print("Initializing["+self.name+"]\n")
    self.digitalPort = options['digitalPort']
    self.pinMode = options['pinMode']
    grovepi.pinMode(self.digitalPort, self.pinMode)
    return self

  def setDigitalPort(self, digitalPort):
    self.digitalPort = digitalPort
    return self

  def setPinMode(self, mode):
    self.pinMode = mode
    grovepi.pinMode(self.digitalPort, self.pinMode)
    return self

  def digitalWrite(self, value):
    grovepi.digitalWrite(self.digitalPort, value)
    return self

  def analogWrite(self, value):
    grovepi.analogWrite(self.digitalPort, value)
    return self

  def switchOn(self):
    # Send HIGH to switch on LED
    grovepi.digitalWrite(self.digitalPort, 1)
    return self

  def switchOff(self):
    # Send LOW to switch off LED
    grovepi.digitalWrite(self.digitalPort, 0)
    return self

  def blink(self, delay):
    self.switchOn()
    time.sleep(delay)
    self.switchOff()
    time.sleep(delay)
    return self

# === LightSensor ===
class LightSensor:

  def setName(self, name):
    self.name = name
    return self

  def initialize(self, options):
    self.value = 0
    self.name = options['name']
    print("Initializing["+self.name+"]\n")
    self.analogPort = options['analogPort']
    grovepi.pinMode(self.analogPort,"INPUT")
    return self

  def setAnalogPort(self, analogPort):
    self.analogPort = analogPort
    return self

  def analogRead(self):
    self.value = grovepi.analogRead(self.analogPort)
    return self.value

  def lightValue(self):
    self.value = grovepi.analogRead(self.analogPort)
    return self.value

  def lightResistance(self):
    self.resistance = (float)(1023 - self.lightValue()) * 10 / self.lightValue()
    #self.value = grovepi.analogRead(self.analogPort)
    return self.resistance

# === SoundSensor ===
class SoundSensor:

  def setName(self, name):
    self.name = name
    return self

  def initialize(self, options):
    self.value = 0
    self.name = options['name']
    print("Initializing["+self.name+"]\n")
    self.analogPort = options['analogPort']
    grovepi.pinMode(self.analogPort,"INPUT")
    return self

  def setAnalogPort(self, analogPort):
    self.analogPort = analogPort
    return self

  def analogRead(self):
    self.value = grovepi.analogRead(self.analogPort)
    return self.value

  def soundValue(self):
    self.value = grovepi.analogRead(self.analogPort)
    return self.value

# === Potentiometer ===
class Potentiometer:

  def setName(self, name):
    self.name = name
    return self

  def initialize(self, options):
    self.value = 0
    self.name = options['name']
    print("Initializing["+self.name+"]\n")
    self.analogPort = options['analogPort']
    return self

  def setAnalogPort(self, analogPort):
    self.analogPort = analogPort
    return self

  def analogRead(self):
    self.value = grovepi.analogRead(self.analogPort)
    return self.value

# === LCDDisplay ===
class LCDDisplay:

  def setText(self, message):
    #grove_rgb_lcd.setRGB(0,128,64)
    #grove_rgb_lcd.setRGB(0,255,0)
    grove_rgb_lcd.setText(message)
    self.message = message
    return self

  def setRGB(self, r, g, b):
    grove_rgb_lcd.setRGB(r, g, b)
    return self

  def console(self):
    print(self.message)

  def initialize(self, options):
    self.name = options['name']
    print("Initializing["+self.name+"]\n")
    self.message = options['message']
    self.setText(self.message)
    return self


# === DHTSensor ===
class DHTSensor:

  def setName(self, name):
    self.name = name
    return self

  def initialize(self, options):
    self.name = options['name']
    print("Initializing["+self.name+"]\n")
    self.digitalPort = options['digitalPort']
    return self

  def setDigitalPort(self, digitalPort):
    self.digitalPort = digitalPort
    return self

  # Get the temperature and Humidity from the DHT sensor
  # [temp, hum] = inst.humidityTemperature()
  def temperatureHumidity(self):
    return grovepi.dht(self.digitalPort,1)

# === UltrasonicRanger ===
class UltrasonicRanger:

  def setName(self, name):
    self.name = name
    return self

  def initialize(self, options):
    self.name = options['name']
    print("Initializing["+self.name+"]\n")
    self.digitalPort = options['digitalPort']
    return self

  def setDigitalPort(self, digitalPort):
    self.digitalPort = digitalPort
    return self

  def distance(self):
    return grovepi.ultrasonicRead(self.digitalPort)

# === Buzzer ===
class Buzzer:

  def setName(self, name):
    self.name = name
    return self

  def initialize(self, options):
    self.name = options['name']
    print("Initializing["+self.name+"]\n")
    self.digitalPort = options['digitalPort']
    grovepi.pinMode(self.digitalPort,"OUTPUT")
    return self

  def setDigitalPort(self, digitalPort):
    self.digitalPort = digitalPort
    return self

  def sound(self):
    grovepi.digitalWrite(self.digitalPort, 1)

  def buzz(self, delay):
    grovepi.digitalWrite(self.digitalPort, 1)
    time.sleep(delay)
    grovepi.digitalWrite(self.digitalPort, 0)
