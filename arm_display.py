from Tkinter import *
from definitions import *
import socket
import time

def tick(canvas, sigs, motors):
    print "tick tock"
    values = [0]*11
    sigs, motors = renderNewValues(canvas, values, sigs, motors)
    canvas.after(1, tick, canvas, sigs, motors)

# def createSocket():
# 	HOST = ''                 # Symbolic name meaning the local host
# 	PORT = 50001              # Arbitrary non-privileged port
# 	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 	s.bind((HOST, PORT))
# 	s.listen(1)
# 	conn, addr = s.accept()
# 	return conn

# def getValues(conn):
# 	values = [0]*11
# 	data = conn.recv(1024)
# 	data = data.split(',')
# 	for i in range(11):
# 		values[i] = data[i]
# 	return values

def renderNewValues(canvas,values, sigs,motors):
	k = 130
	for i in sigs:
		if i != None:
			canvas.delete(i)
			print "cleared i"
	for j in motors:
		if j != None:
			canvas.delete(j)
			print "cleared j"
	for i in range(6):
		sigs[i] = canvas.create_text(k, VERTICAL_POSITIONS[i+1], text=values[i])
	for i in range(6,8):
		sigs[i] = canvas.create_text(k, VERTICAL_POSITIONS[i+2], text=values[i])
	for i in range(3):
		motors[i] = canvas.create_text(k, VERTICAL_POSITIONS[i+11], text=values[i+8])

	return sigs, motors

def renderHeadings(canvas):
	for i in range(14):
		canvas.create_text(100,VERTICAL_POSITIONS[i],text=HEADINGS[i])
	return canvas

def initializeGUI():
	root = Tk()
	canvas = Canvas(root, width=300, height=500)
	canvas.pack()

	sigs = [None]*8
	motors = [None]*3

	#print "creating Socket"
	#conn = createSocket()
	print "rendering headings"
	canvas = renderHeadings(canvas)
	canvas.after(1, tick, canvas, sigs, motors)
	root.mainloop()

initializeGUI()