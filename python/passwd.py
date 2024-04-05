#! /usr/bin/env python3
import random, string, secrets

### README ###
# A simple script to generate a string of random characters 
# to be used as a password. This was created back when I was
# first learning python.
##############

def passwd(stringLength=15):
    characters = string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation
    return ''.join(random.choice(characters) for i in range(stringLength))
print ("Random Key is", passwd() )
