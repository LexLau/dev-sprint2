# Enter your answrs for chapter 6 here
# Name: Alex Lau


# Ex. 6.6
def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

def is_palindrome(word):
	if len(word) <= 1:
		return True
	if first(word) != last(word):
		return False

print is_palindrome('tomot')
print is_palindrome('toot')
print is_palindrome('not')

# Ex 6.8
def gcd(a, b):
	if b == 0:
		return a
	else:
		r = a % b
		return gcd(b, r)

print gcd(12, 8)
