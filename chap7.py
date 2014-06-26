# Enter your answrs for chapter 7 here
# Name: Alex


# Ex. 7.5
def estimate_pi():
	total = 0
	k = 0
	factor = 2 * math.sqrt(2) / 9801
	while True:
		num = factorial(4*k) * (1103 + 26390*k)
		den = factorial(k)**4 * 396**(4*k)
		term = factor * num /den
		total += term

		if abs(term) < 1e-15: break
		k += 1

	return 1 / total

print estimate_pi()


# How many iterations does it take to converge?
# I definitely could not figure this out on my own.