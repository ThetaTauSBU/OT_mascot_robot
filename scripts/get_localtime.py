#!/usr/bin/python3
import time

t = time.localtime()
current_time = time.strftime("%I:%M %p", t)
print("It is", current_time)
