import hashlib
#from werkzeug.security import generate_password_hash, check_password_hash
import corefunc as core

def create_password(pw, app, size):
	"""
	Function used to generate a password for an application, given the global password and application's name and desired size of the output
	input is the global password, application name, and desired password size
	returns a single string to serve as a new password.
	"""
	pwhash = int(hashlib.sha224(pw.encode()).hexdigest(), 16)
	apphash = int(hashlib.sha224(app.encode()).hexdigest(), 16)
	sizeint = int(size)
	scrambled = core.scrambler(str(pwhash), str(apphash))
	resized = core.resizer(sizeint, scrambled)
	return resized

def create_password_old(pw, app, size):
	"""
	Function used to generate a password for an application, given the global password and application's name and desired size of the output
	input is the global password, application name, and desired password size
	returns a single string to serve as a new password.
	"""
	pwhash = hash(pw)
	apphash = hash(app)
	sizeint = int(size)
	scrambled = core.scrambler(str(abs(pwhash)), str(abs(apphash)))
	resized = core.resizer(sizeint, scrambled)
	return resized

"""
#code for use with testing/debugging. Not enabled in pushed version.
size = input("requested size: ")
password = input("global password: ")
site = input("application name: ")
endpass = create_password(password, site, size)
print(endpass)
input()
"""