def fib1(n: int) -> int:
	# fails because recursion error
	return fib1(n - 1) + fib1(n - 2)


def fib2(n: int) -> int:
	# catches base cases, stopping infinite recurssion.
	# print(n)
	if n < 2:	# base case
		return n
	return fib2(n - 2) + fib2(n - 1)


from typing import Dict
memo: Dict[int,int] = {0 :0, 1:1} #base cases stored as an annotation

def fib3(n: int) -> int:
	if n not in memo:
		memo[n] = fib3(n - 1) + fib3(n - 2) #memoristation
	return memo[n]


from functools import lru_cache

@lru_cache(maxsize=None) # python automagically memorises all previous calls to the function
def fib4(n: int) -> int:
	if n < 2:	# base case
		return n
	return fib4(n - 2) + fib4(n - 1)


def fib5(n: int) -> int:
	if n==0: return n # special case
	last: int = 0 	# initially set to fib(0)
	next: int = 1 	# initially set to fib(1)
	for _ in range(1,n):
		last, next = next, last + next
	return next

from typing import Generator

def fib6(n: int) -> Generator[int, None, None]:
	yield 0
	if n > 0: yield 1 # special case
	last: int = 0 	# initially set to fib(0)
	next: int = 1 	# initially set to fib(1)
	for _ in range(1,n):
		last, next = next, last + next
		yield next
	return next


if __name__ == '__main__':
	print(fib2(10))
	# print(fib6(50))
	# for i in fib6(50):
	# 	print(i)