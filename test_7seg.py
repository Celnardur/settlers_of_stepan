from output.pwm import PCA9685

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please specify the i2c address")
        print("Example:")
        print("    ./test_7seg.py 0x48")

    addr = int(sys.argv[1], 0)
    pwm = PCA9685(addr)
    pwm.begin()
    for i in range(8, 16):
        pwm.setPin(i, 1)

