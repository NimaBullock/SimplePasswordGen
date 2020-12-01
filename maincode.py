#from werkzeug.security import generate_password_hash, check_password_hash

def create_password(pw, app, size):
	"""
	Function used to generate a password for an application, given the global password and application's name and desired size of the output
	input is the global password, application name, and desired password size
	returns a single string to serve as a new password.
	"""
	pwhash = hash(pw)
	apphash = hash(app)
	sizeint = int(size)
	scrambled = scrambler(str(abs(pwhash)), str(abs(apphash)))
	resized = resizer(sizeint, scrambled)
	return resized

def scrambler(hash1, hash2):
	"""
	Function used to scramble characters in two strings to increase complexity of the resultant.
	input is two strings of arbitrary size
	returns a single scrambled string of arbitrary size
	"""
	finalString = ""
	index = 0
	for character in hash1:
		finalString += hash1[index]
		finalString += hash2[index]
		if index+1 == len(hash1):
			finalString += hash2[index:]
			break
		elif index+1 == len(hash2):
			finalString += hash1[index:]
			break
		index += 1
	return finalString


def resizer(size, string):
	"""
	Function used to resize a string, characters of the string are constantly reformed into new characters in the range of 33-126 on the ascii table
	Input is an int and a string
	returns a single string of length size
	"""
	index = 0
	finalString, badstring1, badstring2 = "", "", ""
	while len(finalString) != size:
		if(len(string[index:]) <= 1):
			break

		if int(string[index:index+2]) >= 33 and int(string[index:index+2]) <= 126:
			finalString += chr(int(string[index:index+2]))
			index += 2
			continue
		elif int(string[index:index+3]) >= 33 and int(string[index:index+3]) <= 126:
			finalString += chr(int(string[index:index+3]))
			index += 3
			continue
		else:
			#print("Error catcher: Recieved unhandled number of", string[index:index+3])
			if not badstring1:
				badstring1 += string[index:index+3]
			if not badstring2:
				badstring2 += string[index:index+3]
				string += scrambler(badstring1, badstring2)
			index += 1
			continue
	return finalString[:size]

"""
#code for use with testing/debugging. Not enabled in pushed version.
size = input("requested size: ")
password = input("global password: ")
site = input("application name: ")
endpass = create_password(password, site, size)
print(endpass)
input()
"""