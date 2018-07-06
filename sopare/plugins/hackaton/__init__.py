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
aus = "aus"
ein = "ein"
raspberry = False

if os.uname()[1] == 'raspberrypi':
    import RPi.GPIO as GPIO

    raspberry = True
    GPIO.setmode(GPIO.BOARD)
    relais = 12
    GPIO.setup(relais, GPIO.OUT)
    GPIO.output(relais, GPIO.HIGH)

def run(readable_results, data, rawbuf):
    if len(readable_results) > 0:
        if raspberry and readable_results[0] == aus:
            GPIO.output(relais, GPIO.LOW)
            print "juhu ausschalten"

        elif raspberry and readable_results[0] == ein:
            GPIO.output(relais, GPIO.HIGH)
            print "juhu einschalten"
    else:
        print "not known"
