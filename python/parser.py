#!/usr/bin/python3
# IMPORTS
import sys # sys.argv

# Utility-functions
def getHexString(data,at,length):
    hex = ""
    for offset in range(0,length):
        hex = hex + ("%x" % data[at + offset])
    return hex

def hexStringToAscii(hex):
    return bytearray.fromhex(hex).decode()

# DIRS
CAP_FILE = sys.argv[1]

# Open the .cap file.
with open(CAP_FILE, "rb") as FILE:
    # Read the whole file at once
    data = FILE.read()

# Get the location of the first frame in the captured data.
FIRST_FRAME_OFFSET      = 39                    
FRAME_OFFSET            = FIRST_FRAME_OFFSET 

# Number of the frame in the recording.
FRAME_NUMBER = 1

# Run as long as there is data left.
# Currently while-true
while True:

    # Locations of tags in the current frame thats specified by the FRAME_OFFSET.
    DEST_ADDR                       = FRAME_OFFSET + 31
    SRC_ADDR                        = FRAME_OFFSET + DEST_ADDR + 6
    SSID                            = FRAME_OFFSET + 53
    SSID_LENGTH                     = FRAME_OFFSET + 52

    # Get location of the next request.
    # We need to calculate the length of the current request,
    # to know where the next request begins.
    # To get the total length, whe have to add all the 'length' bytes
    # of which the location may vary because of the length of the previous
    # data such as the SSID.
    SUPPORTED_TAG_LENGTH            = SSID                          + data[SSID_LENGTH]                    + 1
    SUPPORTED_TAG_EXTENDED_LENGTH   = SUPPORTED_TAG_LENGTH          + data[SUPPORTED_TAG_LENGTH]           + 2
    DS_TAG_LENGTH                   = SUPPORTED_TAG_EXTENDED_LENGTH + data[SUPPORTED_TAG_EXTENDED_LENGTH]  + 2
    HT_TAG_LENGTH                   = DS_TAG_LENGTH                 + data[DS_TAG_LENGTH]                  + 2
    VENDOR_SPECIFIC_TAG             = HT_TAG_LENGTH                 + data[HT_TAG_LENGTH]                  + 2
    VENDOR_SPECIFIC_TAG2            = VENDOR_SPECIFIC_TAG           + data[VENDOR_SPECIFIC_TAG]            + 2 
    NEXT_FRAME_OFFSET               = VENDOR_SPECIFIC_TAG2          + data[VENDOR_SPECIFIC_TAG2]           + 20 # skip 20 bytes of tail that I dont know the purpose of. (yet)
    
    # Print debug data.
    print("FRAME_NUMBER: " + str(FRAME_NUMBER))
    print("DEST_ADDR: " + str(data[DEST_ADDR]))
    print("SRC_ADDR: " + str(data[SRC_ADDR]))
    print("SSID HEX: " + getHexString(data,SSID,data[SSID_LENGTH]))
    print("SSID ASCII: " + hexStringToAscii(getHexString(data,SSID,data[SSID_LENGTH])))
    print("SSID_LENGTH: " + str(data[SSID_LENGTH]))
    print("SUPPORTED_TAG_LENGTH: " + str(data[SUPPORTED_TAG_LENGTH]))
    print("SUPPORTED_TAG_EXTENDED_LENGTH: " + str(data[ SUPPORTED_TAG_EXTENDED_LENGTH]))
    print("DS_TAG_LENGTH: " + str(data[DS_TAG_LENGTH]))
    print("HT_TAG_LENGTH: " + str(data[HT_TAG_LENGTH]))
    print("VENDOR_SPECIFIC_TAG: " + str(data[VENDOR_SPECIFIC_TAG]))
    print("VENDOR_SPECIFIC_TAG2: " + str(data[VENDOR_SPECIFIC_TAG2]))
    print("NEXT_FRAME_OFFSET: " + str(NEXT_FRAME_OFFSET) + " (" + str(NEXT_FRAME_OFFSET - FRAME_OFFSET) + ")")
    
    # Set the offset to the start of the next frame.
    FRAME_OFFSET = NEXT_FRAME_OFFSET
    FRAME_NUMBER = FRAME_NUMBER + 1
    
    # Add data to database here somewhere
    # ...
    # ...

    # For debugging purposes.
    input("############################################")