from time import sleep
from picamera import PiCamera

camera = PiCamera()
startRecording = 5
endRecording = 10
i = 0


while i < 7:
    a = "space"+i
    sleep(startRecording)
    camera.start_preview()
    camera.start_recording('/home/pi/Desktop/SPACE' + a)
    sleep(endRecording)
    camera.stop_recording()
    camera.stop_preview()
    i += 1
