# Basic python lines to print "Hello "

def say_hello(input):
	if input in ["Ravi","Roman","Brock"]:
		return f'Hello my friend {input}'
	else:
	    return f'Hey Hii'
	    	
if __name__ == "__main__":
	user = "Brock"
	
	reply = say_hello(user)
	print(reply)
	
	
