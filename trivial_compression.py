class CompressedGene():
	"""docstring for Compressed Gene"""
	def __init__(self, gene:str) -> None:
		self._compress(gene)

	def _compress(self, gene: str) -> None:
		self.bit_string: int = 1	# start with sentinel
		for nucleotide in gene.upper():
			print(nucleotide)
			self.bit_string <<=2	# shift left two bits
			if nucleotide == "A":	# change last two bits to 00
				self.bit_string |= 0b00
			if nucleotide == "C":	# change last two bits to 01
				self.bit_string |= 0b01
			if nucleotide == "G":	# change last two bits to 10
				self.bit_string |= 0b10
			if nucleotide == "T":	# change last two bits to 11
				self.bit_string |= 0b11
			else:
				raise ValueError(f"Invalid nucleotide:{nucleotide}")

	def decompress(self) -> str:
		gene: str=""
		for i in range(0, self.bit_string.bit_length() - 1, 2):	# -1 to exclude sentinel
			bits: int=self.bit_string >> i & 0b11	# get just 2 relevant bits
			if bits == 0b00:	# A
				gene +="A"
			if bits == 0b01:	# C
				gene +="C"
			if bits == 0b10:	# G
				gene +="G"
			if bits == 0b11:	# T
				gene +="T"
			else:
				raise ValueError(f"Invalid bits: {bits}")
		return gene[::-1]	# reverses string by slicing backward

	def __str__(self) -> str:	# str representation for pretty printing
		return self.decompress()


if __name__ == "__main__":
	from sys import getsizeof
	original: str = "T" * 100
	print(f"original is {getsizeof(original)} bytes")
	compressed: CompressedGene = CompressedGene(original)	# compress
	print(f"compressed is {getsizeof(compressed.bit_string)} bytes")
	print(compressed)
	print(f"original and decompressed are the same: {original == compressed.decompress()}")