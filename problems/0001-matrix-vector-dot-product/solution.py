def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	ret = []
	for vec in a:
		if len(vec) != len(b):
			return -1
		ret.append(sum([e_a * e_b for e_a, e_b in zip(vec,b)]))
	return ret