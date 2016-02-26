import time

def pauseTime(seconds):
	'''
	Function to tell python to wait a given period of time before going to next function
	Args:
		seconds(integer): less than 60
	Returns:
		string text telling the user how long the program is waiting
	'''
	s = seconds
	print "waiting %s seconds" % s
	time.sleep(seconds)
