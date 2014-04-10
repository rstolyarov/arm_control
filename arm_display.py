from Tkinter import *
from definitions import *
import socket
import time

def tick(canvas, conn, sigs, motors):
    print "tick tock"
    values = getValues(conn)
    sigs, motors = renderNewValues(canvas, values, sigs, motors)
    canvas.after(1, tick, canvas, conn, sigs, motors)

def createSocket():
	HOST = ''                 # Symbolic name meaning the local host
	PORT = 50001              # Arbitrary non-privileged port
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	s.listen(1)
	conn, addr = s.accept()
	return conn

def getValues(conn):
	values = [0]*11
	data = conn.recv(1024)
	data = data.split(',')
	for i in range(11):
		values[i] = data[i]
	return values

def renderNewValues(canvas,values, sigs,motors):
	k = 120
	for i in sigs:
		canvas.delete(i)
	for i in motors:
		canvas.delete(i)
	for i in range(8):
		sigs[i] = canvas.create_text(k, 10, text=values[i])
	for i in range(3):
		motors[i] = canvas.create_text(k, 10, text=values[i+8])

	return sigs, motors

def renderHeadings(canvas):
	for i in range(13):
		canvas.create_text(100,VERTICALPOSITIONS[i],text=HEADINGS[i])
	return canvas

root = Tk()
canvas = Canvas(root, width=200, height=400)
canvas.pack()

sigs = [None]*8
motors = [None]*3

print "creating Socket"
conn = createSocket()
print "rendering headings"
canvas = renderHeadings(canvas)
print "hello"
time.sleep(10)
canvas.after(1, tick, canvas, conn, sigs, motors)
root.mainloop()