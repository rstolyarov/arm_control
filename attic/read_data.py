import spidev
import time

class MCP3208:
  def __init__(self, spi_channel=0):
    self.spi_channel = spi_channel
    self.conn = spidev.SpiDev(0, spi_channel)
    self.conn.max_speed_hz = 1000000

  def __del__(self):
    self.close
  
  def close(self):
    if self.conn != None:
      self.conn.close
      self.conn = None

  def bitstring(self,n):
    s = bin(n)[2:]
    return '0'*(8-len(s))+s

  def read(self,adc_channel=0):
    cmd = 128
    cmd += 64
    if adc_channel % 2 == 1:
      cmd += 8
    if (adc_channel/2) % 2 == 1:
      cmd += 16
    if (adc_channel/4) % 2 == 1:
      cmd += 32
    reply_bytes = self.conn.xfer2([cmd,0,0,0])
    reply_bitstring = ''.join(self.bitstring(n) for n in reply_bytes)
    reply = reply_bitstring[5:19]
    return int(reply,2)


def convertVolts(data):
  return data * 3.3/4095

def convertTemp(data):
  return (data - 25)/12.4

def convertPressure(data):
  return data * 25/4095

def readChannel(channel):
  spi = MCP3208(0)
  read = 0
  for i in range(100):
   read += spi.read(channel)

  read = read/100
  return read
