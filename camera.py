import picamera
with picamera.PiCamera() as camera:
    camera.resolution = (320, 240)
    camera.capture('/home/pi/Desktop/Camera/newimage.jpg')
    print('picture taken')
