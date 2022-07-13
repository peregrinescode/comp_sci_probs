def calculate_pi(n_terms: int) -> float:
	numerator: float = 4.0
	denominator: float = 1.0	# to begin
	operation: float = -1.0	# subtract to begin
	pi: float = 0.0	# to begin
	for _ in range(1, n_terms):	# use underscore here because do not require the variable in the loop.
		pi += operation * (numerator / denominator)
		operation *= -1.0
		denominator += 2.0
	return pi

if __name__ == "__main__":
	print(calculate_pi(999999))