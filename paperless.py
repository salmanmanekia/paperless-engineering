# The Challenge:

# A trained cat and dog run a race, one hundred feet straight 
# away and return. The dog leaps three feet at each bound and 
# the cat but two, but then she makes three leaps to his two.
# Now, under those circumstances, who wins the race?

# Input

# The race distance eg 100, 200

# Output

# {Animal} wins by {distance}

# Cat wins by 50 feet
# Dog wins by 10 feet
# or Draw 

#!/usr/bin/python
import math

distance = 0
def validDistance(d):
    if d < 0:
		print "%s is not positive. Try again." % d
		print 
		return 0
    else:
        return 1

def getInput():
	global distance
	while 1:
		distance = int(raw_input("The race distance "))
		if validDistance(distance):
			break
	return

def raceFunc(): 
	global distance
	total_cat_leaps = int(math.ceil(distance/2.0) * 2)
	total_dog_leaps = int(math.ceil(distance/3.0) * 2)

	total_cat_distance = total_cat_leaps * 2
	total_dog_distance = total_dog_leaps * 3

	if total_cat_distance == total_dog_distance:
		print 'Draw'
	elif total_cat_distance < total_dog_distance:
		print 'Cat wins by', total_dog_distance-total_cat_distance, 'feet'
	elif total_cat_distance > total_dog_distance:
		print 'Dog wins by', total_cat_distance-total_dog_distance, 'feet'

if __name__ == '__main__':
	print
	getInput()
	raceFunc()
