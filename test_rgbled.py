from lib import mBot

if __name__ == '__main__':
	bot = mBot.mBot()
	bot.startWithSerial("/dev/ttyUSB0")
	# bot.startWithHID()
	while(1):
		print "loop"
		bot.doRGBLedOnBoard(0,100,0,0)
		bot.doRGBLedOnBoard(1,100,0,0)
		sleep(0.5)
		bot.doRGBLedOnBoard(0,0,100,0)
		bot.doRGBLedOnBoard(1,0,100,0)
		sleep(0.5)
