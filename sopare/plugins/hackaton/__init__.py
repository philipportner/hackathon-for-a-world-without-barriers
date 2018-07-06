#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (C) 2015 - 2017 Martin Kauss (yo@bishoph.org)

Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain
a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations
under the License.
"""

# Default plugin for output of analysis
import os

# Global defaults...
import pyaudio
import wave

off = "aus"
on = "ein"
state = "status"
current_state = off

raspberry = False
raspberry_uname = 'raspberrypi'

if os.uname()[1] == raspberry_uname:
    raspberry = True

    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)
    relais = 12
    GPIO.setup(relais, GPIO.OUT)
    GPIO.output(relais, GPIO.HIGH)
    current_state = on


def run(readable_results, data, rawbuf):
    global current_state
    readable_results.append(on)

    if len(readable_results) > 0:

        if readable_results[0] == off and current_state != off:
            current_state = off
            print current_state
            if raspberry:
                GPIO.output(relais, GPIO.LOW)
                play_audio(off)

        elif readable_results[0] == on and current_state != on:
            current_state = on
            print current_state
            if raspberry:
                GPIO.output(relais, GPIO.HIGH)
                play_audio(on)

        elif readable_results[0] == state:
            if raspberry and current_state == on:
                play_audio(on)
            elif raspberry and current_state == off:
                play_audio(off)
            print "state: " + current_state

    else:
        print "not known"


def play_audio(cmd):
    import pygame
    pygame.mixer.init()

    wavefile = ''
    if cmd == on:
        wavefile = "./audio/on.wav"
    elif cmd == off:
        wavefile = "./audio/off.wav"

    if not os.path.isfile(wavefile):
        return

    pygame.mixer.music.load(wavefile)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
