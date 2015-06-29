from pyo import *
from time import sleep

# 100 loops sound recording experiment
# 29/06/15 dotmancando
# This experiment used alsamixer config as follow:
# Speaker Front 59
# Line 100

s = Server().boot() 
s.start()

lineVolume = 1 # 100% line volume
firstRound = 0 
lastRound = 100

readFile = "" # file name to read from 
writeFile = "" # file name to write to


if len(sys.argv) == 3: # give arguments to specify first round and last round
	firstRound = int(sys.argv[1])
	lastRound = int(sys.argv[2])
	
print "start from round ", firstRound, " to ", lastRound

# get the writeFile of the "last round", as if it has just been written
if(firstRound < 10): #  I just like file name to have 2 digits.......
	writeFile = "wav/pyo_record0" + str(firstRound) + ".wav" 
else:
	writeFile = "wav/pyo_record" + str(firstRound) + ".wav"		


for round in range(firstRound, lastRound): #looping from firstRound to lastRound
	
	
	readFile = writeFile # readFile of this round is the writeFile from the previous round	
	
	round += 1 
	
	if(round < 10):
		writeFile = "wav/pyo_record0" + str(round) + ".wav"
	else:
		writeFile = "wav/pyo_record" + str(round) + ".wav"	
	
	print "reading from ", readFile
	print "saving to ",  writeFile

	sf = SfPlayer(readFile, speed=1, loop=False).out(chnl = 0) # play a sound file through channel Front Left channel (0)
	
	# the audio cable connects Front to Line-in

	lineL = Input(chnl = 0, mul = lineVolume) # use left Line-in as input
	sleep(0.05) # it takes a bit of time to actually play the sound file, so we have to delay it a bit here

	rec = Record(lineL, writeFile, fileformat=0, sampletype=0) #record the lineL object, to that file, this will keep recording until we stop it
	
	
	sleep(7) # sleep for 7 seconds
	clean = Clean_objects(0, rec) # then we schedule to clean (stop) the recording in 0 second
	clean.start() # start now
	print "--------"
	sleep(2) # then it takes sometimes to actually finish saving the file, so we delay a bit here

	#then we keep looping until we hit the lastRound
	
	
	

