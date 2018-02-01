#!/usr/bin/python

import time
import RPi.GPIO as gpio
import sys

if __name__=='__main__':
  ledpin = 23
  gpio.setwarnings(False)
  gpio.setmode(gpio.BCM)
  gpio.setup(ledpin, gpio.OUT)
  gpio.output(ledpin, gpio.HIGH)
  print 'Lights are on!'

