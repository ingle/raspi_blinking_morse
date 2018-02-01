#!/usr/bin/python

import time
import RPi.GPIO as gpio
import sys

# https://morsecode.scphillips.com/morse2.html
DOT_DURATION = 0.10
DASH_DURATION = 4.0*DOT_DURATION
SILENCE_BTWN_COMPONENTS = DOT_DURATION # space btwn components of same character
SILENCE_BTWN_CHARACTERS = 5.0*DOT_DURATION 
WHITE_SPACE_DURATION = 7.0*DOT_DURATION # space btwn words

CODE_DICT = {
'A': '.-',     'B': '-...',   'C': '-.-.', 
'D': '-..',    'E': '.',      'F': '..-.',
'G': '--.',    'H': '....',   'I': '..',
'J': '.---',   'K': '-.-',    'L': '.-..',
'M': '--',     'N': '-.',     'O': '---',
'P': '.--.',   'Q': '--.-',   'R': '.-.',
'S': '...',    'T': '-',      'U': '..-',
'V': '...-',   'W': '.--',    'X': '-..-',
'Y': '-.--',   'Z': '--..',
'a': '.-',     'b': '-...',   'c': '-.-.', 
'd': '-..',    'e': '.',      'f': '..-.',
'g': '--.',    'h': '....',   'i': '..',
'j': '.---',   'k': '-.-',    'l': '.-..',
'm': '--',     'n': '-.',     'o': '---',
'p': '.--.',   'q': '--.-',   'r': '.-.',
's': '...',    't': '-',      'u': '..-',
'v': '...-',   'w': '.--',    'x': '-..-',
'y': '-.--',   'z': '--..',
'0': '-----',  '1': '.----',  '2': '..---',
'3': '...--',  '4': '....-',  '5': '.....',
'6': '-....',  '7': '--...',  '8': '---..',
'9': '----.',
} 

def init(ledpin):
  gpio.setwarnings(False)
  gpio.setmode(gpio.BCM)
  gpio.setup(ledpin, gpio.OUT)
  gpio.output(ledpin, gpio.LOW)
  print 'Get ready!'
  time.sleep(2*DASH_DURATION)

def cleanup(ledpin):
  time.sleep(2*DASH_DURATION)
  gpio.output(ledpin, gpio.HIGH)
  #gpio.cleanup()
  print 'Done!'

def dot(ledpin):
  gpio.output(ledpin, gpio.HIGH)
  time.sleep(DOT_DURATION)
  gpio.output(ledpin, gpio.LOW)
  time.sleep(SILENCE_BTWN_COMPONENTS)

def dash(ledpin):
  gpio.output(ledpin, gpio.HIGH)
  time.sleep(DASH_DURATION)
  gpio.output(ledpin, gpio.LOW)
  time.sleep(SILENCE_BTWN_COMPONENTS)

def whitespace(ledpin):
  time.sleep(WHITE_SPACE_DURATION)

def emit_character(char, ledpin=23):
  if char not in CODE_DICT.keys():
    print char,'not found, skipped.'
  else:
    for dd in CODE_DICT[char]:
      if dd=='-':
        sys.stdout.write('-')
        sys.stdout.flush()
        dash(ledpin)
      elif dd=='.':
        sys.stdout.write('.')
        sys.stdout.flush()
        dot(ledpin)
	time.sleep(SILENCE_BTWN_CHARACTERS)

def emit_whitespace(ledpin=23):
  print "[I've got a blank space baby!]"
  whitespace(ledpin)

def emit_word(word, ledpin=23):
  print(word)
  for char in word:
    sys.stdout.write(char)
    sys.stdout.flush()
    sys.stdout.write(' ')
    sys.stdout.flush()
    emit_character(char)
    sys.stdout.write('\r\n')

if __name__=='__main__':
  if len(sys.argv)>=2:
    ledpin = 23
    init(ledpin)

    for word in sys.argv[1:-1]:
      emit_word(word)
      emit_whitespace()
    emit_word(sys.argv[-1])

    cleanup(ledpin)
  else:
    print 'Missing message! Try this:'
    print 'blink.py your message here'
