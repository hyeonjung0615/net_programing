import socket
import struct
import binascii

class Udphdr:
    def __init__(self, Source_port, Destination_port, length, Checksum):
        self.Source_port = Source_port
        self.Destination_port = Destination_port
        self.length = length
        self.Checksum = Checksum
    
    def pack_Udphdr(self):
        packed = b''
        packed += struct.pack('!H', self.Source_port)
        packed += struct.pack('!H', self.Destination_port)
        packed += struct.pack('!H', self.length)
        packed += struct.pack('!H', self.Checksum)
        return packed

    
def unpack_Udphdr(buffer):
    unpacked = struct.unpack('!HHHH', buffer[:8])
    return unpacked

def getSrcPort(unpacked_Udphdr):
    return unpacked_Udphdr[0]

def getDstPort(unpacked_Udphdr):
    return unpacked_Udphdr[1]

def getLength(unpacked_Udphdr):
    return unpacked_Udphdr[2]

def getChecksum(unpacked_Udphdr):
    return unpacked_Udphdr[3]

## pack ##    
udp = Udphdr(5000, 80, 1000, 0xFFFF)
packed_Udphdr = udp.pack_Udphdr()
print(binascii.b2a_hex(packed_Udphdr))


unpacked_Udphdr = unpack_Udphdr(packed_Udphdr)
print(unpacked_Udphdr)
print("Source Port:{} Destination Port:{} Length:{} Checksum:{}" \
      .format(getSrcPort(unpacked_Udphdr), \
              getDstPort(unpacked_Udphdr), \
              getLength(unpacked_Udphdr), \
              getChecksum(unpacked_Udphdr) )) 