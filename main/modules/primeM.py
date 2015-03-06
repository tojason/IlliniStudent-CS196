class Prime(object):
	def is_Prime(self,a):
		for num in range(2, (int)(a**(1/2)+1)):
			if a % num == 0:
				return "%d +not prime" % a
		return "%d is prime" % a

if __name__ == '__main__':
	primetest = Prime()
	print primetest.is_Prime(379)