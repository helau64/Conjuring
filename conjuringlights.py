import unicornhat as unicorn
from time import sleep

try:
	while True:
		for i in range(0,4):
			for j in range(0,8):
				unicorn.brightness(0.5)
				unicorn.set_pixel(i, j, 255, 255, 255)
				unicorn.show()
				sleep(0.01)
		sleep(0.5)

		for i in range(0,4):
			for j in range(0,8):
				unicorn.brightness(0.5)
				unicorn.set_pixel(i, j, 0, 0, 0)
				unicorn.show()
				sleep(0.01)
		sleep(0.5)

		for i in range(4,8):
			for j in range(0,8):
				unicorn.brightness(0.5)
				unicorn.set_pixel(i, j, 255, 255, 255)
				unicorn.show()
				sleep(0.01)
		sleep(0.5)

		for i in range(4,8):
			for j in range(0,8):
				unicorn.brightness(0.5)
				unicorn.set_pixel(i, j, 0, 0, 0)
				unicorn.show()
				sleep(0.01)
		sleep(0.5)

except KeyboardInterrupt:
	unicorn.clean_shutdown()