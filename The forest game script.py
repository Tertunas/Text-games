
def forest():
	print " Welcome to the forest you have just woken up, you see many dead people around you that have been cut open and eaten up "
	print " You walk about 1km ahead and you see a cave will you enter remember you only have an axe "
	answer = raw_input(" Type left if you want to enter the cave or right if you want to leave the area and hit 'Enter'. ")
	if answer == "left":
		print " You have enterd the cave and you were killed by an army of man eaters "
		die()
	elif answer == "right":
		print " You got lucky and you escaped certain death and you lived "
	else:
		print " You cant just stand still!"
	print " Well now whats next"
	forest()

def die():
	print "You died"

forest()