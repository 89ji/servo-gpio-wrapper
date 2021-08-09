import pigpio

class Servo():
	def __init__(self, pin, verboseMode = True):
		self.pin = pin
		self.loud = verboseMode
		self.angle = None
		self.pwmWidth = None
		self.pi = pigpio.pi()

	def setAngle(self, angle):
		angle = int(angle)
		if angle < 0:
			if self.loud == True:
				print('Clamped angle from', angle, 'deg to 0 deg')
			angle = 0
		if angle > 180:
			if self.loud == True:
				print('Clamped angle from', angle, 'deg to 180 deg')
			angle = 180

		pwmWidth = int(angle * 100 / 9 + 500)
		self.angle = angle

		if self.loud == True:
			print('Angle set to', angle, 'degrees')

		self.setPWM(pwmWidth)
	
	def setPWM(self, pwmWidth):
		self.pi.set_servo_pulsewidth(self.pin, pwmWidth)
		if self.loud == True:
			print('PWM width set to', pwmWidth)
		self.pwmWidth = pwmWidth

	def getPWM(self):
		return self.pwmWidth

	def getAngle(self):
		return self.angle

	def detach(self):
		self.pi.set_servo_pulsewidth(self.pin, 0)
		self.pi.stop()