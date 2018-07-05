#!/bin/sh

pulseaudio --kill
jack_control start
pulseaudio --start

