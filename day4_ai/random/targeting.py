import random as r
import math
from time import time

def test_random(name, func, count = 1000):
	sum = 0

	begin = time()
	for i in range(count):
		sum += func()
	elapsed = (time() - begin) * 1000
	prop = sum / count * 100

	print("%s(%dms): %.2f%%" % (name, elapsed, prop))

state = []
for i in range(16):
	state.append(r.randint(0, 65536))
def well512():
	index = 0
	val = 0.0

	a = state[index]
	c = state[(index + 3) & 15]
	b = a ^ c ^ (a << 16) ^ (c << 5)
	c = state[(index + 9) & 15]
	c ^= c >> 11
	a = state[index] = b ^ c
	d = a ^ ((a << 5) & 0xDA442D20)

	index = (index + 15) & 15
	a = state[index]
	state[index] = a ^ b ^ d ^ (a << 2) ^ \
			(b << 18) ^ (c << 28)

	val = state[index] % 1000 / 1000.0
	return val

def rand_increase():
	return well512() + 0.1
def rand_square():
	return well512() ** 2
def rand_sqrt():
	return math.sqrt(well512())
def rand_sin():
	return math.sin(well512() * 3.141592 / 2)
def rand_tan():
	return math.tan(well512() * 3.141592 / 4)
def rand_gaussian():
	return math.exp(-2 * well512() ** 2)

test_random('random()', r.random)
test_random('well512()', well512)
test_random('rand_increase()', rand_increase)
test_random('rand_square()', rand_square)
test_random('rand_sqrt()', rand_sqrt)
test_random('rand_sin()', rand_sin)
test_random('rand_tan()', rand_tan)
test_random('rand_gaussian()', rand_gaussian)
