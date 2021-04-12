from output.pwm import PCA9685

def test(address):
    pwm = PCA9685(address)
    pwm.begin()
    for i in range(8, 16):
        pwm.setPin(i, 1)
