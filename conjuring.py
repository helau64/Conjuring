import string
import random
import time

words = [line.strip() for line in open('dictionary.txt')]

random_value = random.random()

while True == True:

	time.sleep(0.5)
	random_value = random.random()

	if random_value <= 0.25:

		random_string = '_'.join(random.sample(words, 2))
		random_variable = random.choice(words)

		print "def %s (%s, %s):" % (random_string, random.choice(words), random.choice(words))
		print "	%s = %s [%s : %s]" % (random_variable, random.choice(words), random_string, random.choice(words))
		print "	%s = %s" % (random.choice(words), random.choice(words))
		print "return %s" % (random_variable)
		print ""

	elif random_value > 0.25 and random_value <= 0.5:

		random_string = str('_'.join(random.sample(words, 2)))

		print "for (%s, %s) in %s():" % (random_string, random.choice(words), random.choice(words))
		print "	setattr(%s, %s)" % (random.choice(words), random.choice(words))
		print ""

	elif random_value > 0.5 and random_value <= 0.75:

		print "from %s import %s" % (random.choice(words), random.choice(words))
		print ""

	else:

		random_string = '_'.join(random.sample(words, 2))

		if random_value <= 0.5:

			print "if %s != %s" % (random.choice(words), random.choice(words))
			print "	%s = %s %s.%s(%s)" % (random.choice(words), random_string, random.choice(words), random_string, random.choice(words))
			print ""

		else:

			print "if %s == %s" % (random.choice(words), random.choice(words))
			print "	%s = %s [%s : %s]" % (random.choice(words), random.choice(words), random_string, random.choice(words))
			print ""

	