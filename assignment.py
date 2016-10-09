import msvcrt
import time
import sys

finish=7
count=0
count1=-1
finish1=5
count2=0
finish2=7

print "press enter key"
start_time = time.time()

while(1):
	key= msvcrt.getch()
	if key =='\xe0':
		key=msvcrt.getch()
		if key == 'M':
			count=count+1
			print "-->",
			if count == finish:
				print "\tdown key to continue"
				break
		else:
			print "wrong key.....You lost!!!!"	
			sys.exit()	
while(1):
	key1= msvcrt.getch()
	if key1 =='\xe0':
		key1=msvcrt.getch()
		if key1 == 'P':
			count1=count1+1
			if count1==0:
				print"\t\t\t\t/\n"
			if count1==1:
				print"\t\t\t/\n"
			if count1==2:
				print"\t\t/\n"	
			if count1==3:
				print"\t/\n"
			if count1==4:
				print"/\n",					
			if count1 == finish1:
				print "\tright key to continue"	
				break
		else:
			print"wrong key....you lost!!!!"
			sys.exit()	

					
while(1):
	key2= msvcrt.getch()
	if key2 =='\xe0':
		key2=msvcrt.getch()
		if key2 =="M":
			count2=count2+1

			print "-->",
			if count2 == finish2:
				print "finished"
				break
		else:
			print"wrong key.....You lost!!!!"
			sys.exit()				

time_elapsed = time.time()-start_time
print "congo you won"
print"time taken is=",str(round(time_elapsed))


'''
1. Mention controls for the game.
'''
