import time
import ctypes
import threading
from ctypes.util import find_library

currentX = 0
currentY = 0

CFArrayRef = ctypes.c_void_p
CFMutableArrayRef = ctypes.c_void_p
CFIndex = ctypes.c_long

MultitouchSupport = ctypes.CDLL("/System/Library/PrivateFrameworks/MultitouchSupport.framework/MultitouchSupport")

CFArrayGetCount = MultitouchSupport.CFArrayGetCount
CFArrayGetCount.argtypes = [CFArrayRef]
CFArrayGetCount.restype = CFIndex

CFArrayGetValueAtIndex = MultitouchSupport.CFArrayGetValueAtIndex
CFArrayGetValueAtIndex.argtypes = [CFArrayRef, CFIndex]
CFArrayGetValueAtIndex.restype = ctypes.c_void_p

MTDeviceCreateList = MultitouchSupport.MTDeviceCreateList
MTDeviceCreateList.argtypes = []
MTDeviceCreateList.restype = CFMutableArrayRef

class MTPoint(ctypes.Structure):
    _fields_ = [("x", ctypes.c_float),
                ("y", ctypes.c_float)]

class MTVector(ctypes.Structure):
    _fields_ = [("position", MTPoint),
                ("velocity", MTPoint)]

class MTData(ctypes.Structure):
    _fields_ = [
      ("frame", ctypes.c_int),
      ("timestamp", ctypes.c_double),
      ("identifier", ctypes.c_int),
      ("state", ctypes.c_int),  # Current state (of unknown meaning).
      ("unknown1", ctypes.c_int),
      ("unknown2", ctypes.c_int),
      ("normalized", MTVector),  # Normalized position and vector of
                                 # the touch (0 to 1).
      ("size", ctypes.c_float),  # The area of the touch.
      ("unknown3", ctypes.c_int),
      # The following three define the ellipsoid of a finger.
      ("angle", ctypes.c_float),
      ("major_axis", ctypes.c_float),
      ("minor_axis", ctypes.c_float),
      ("unknown4", MTVector),
      ("unknown5_1", ctypes.c_int),
      ("unknown5_2", ctypes.c_int),
      ("unknown6", ctypes.c_float),
    ]

MTDataRef = ctypes.POINTER(MTData)

MTContactCallbackFunction = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, MTDataRef,
    ctypes.c_int, ctypes.c_double, ctypes.c_int)

MTDeviceRef = ctypes.c_void_p

MTRegisterContactFrameCallback = MultitouchSupport.MTRegisterContactFrameCallback
MTRegisterContactFrameCallback.argtypes = [MTDeviceRef, MTContactCallbackFunction]
MTRegisterContactFrameCallback.restype = None

MTDeviceStart = MultitouchSupport.MTDeviceStart
MTDeviceStart.argtypes = [MTDeviceRef, ctypes.c_int]
MTDeviceStart.restype = None

###

@MTContactCallbackFunction
def my_callback(device, data_ptr, n_fingers, timestamp, frame):
    #print threading.current_thread(), device, data_ptr, n_fingers, timestamp, frame
    for i in xrange(n_fingers):
        data = data_ptr[i]
        d = "x=%.2f, y=%.2f" % (data.normalized.position.x * 100,
                                data.normalized.position.y * 100)
        currentX = data.normalized.position.x * 100
        currentY = data.normalized.position.y * 100
    return 0

def listen():
	devices = MultitouchSupport.MTDeviceCreateList()
	num_devices = CFArrayGetCount(devices)
	# print "num_devices =", num_devices
	for i in xrange(num_devices):
	    device = CFArrayGetValueAtIndex(devices, i)
	#     print "device #%d: %016x" % (i, device)
	    MTRegisterContactFrameCallback(device, my_callback)
	    MTDeviceStart(device, 0)
	
	while threading.active_count():
	    # Why sleep instead of join? Ask David Beazley.
	    time.sleep(0.125)
