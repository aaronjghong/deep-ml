def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	ret = []
	if len(a) == 0 or len(b) == 0:
		return -1
	if len(a[0]) != len(b):
		return -1
	for vec in a:
		ret.append(sum([e_a * e_b for e_a, e_b in zip(vec,b)]))
	return ret