from gpiozero import MotionSensor
from picamera import PiCamera
from time import time
from time import sleep
import datetime
 
pir=MotionSensor(4)
camera=PiCamera()

def getFileName():
    return datetime.datetime.now().strftime("$Y-$m-$d.$H.$M.$S.h264")

while True:
    filename = getFileName()
    pir.wait_for_motion
    camera.start_preview()
    camera.start_recording(filename)
    camera.wait_recording(50)
    camera.stop_preview()
    camera.stop_recording()
    time.sleep(1)
    