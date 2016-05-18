#!/usr/bin/python

import random
import time

badmStudents = ["x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x"]

random.shuffle(badmStudents, random.random);

print "DM Creative HackLab Groups : " + time.strftime("%Y-%m-%d %H:%M")
print "++++++++++++++++++++++++++"
for i in range(0,len(badmStudents),1):
    if i == 4 or i == 8 or i == 12 or i == 16 :
        print "------------------------------"
    print badmStudents[i]
print "++++++++++++++++++++++++++"
