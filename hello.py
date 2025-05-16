# Basic python lines to print "Hello "

def say_hello(input):
	if input == "Hi":
		return f'Hello my friend {input}'
	else:
	    	return f'Hey Hii'
	    	
if "__name__" == "__main__":
	user = input("Enter your name hear : ")
	
	reply = say_hello(user)
	print(reply)
	
	
