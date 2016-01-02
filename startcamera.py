import picamera

camera = picamera.PiCamera()

camera.hflip = True
camera.vflip = True

camera.start_preview()


