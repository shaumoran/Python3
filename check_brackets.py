#This checks for matching brackets in a string.

def check_brackets(line):
	is_bracket = ["(", ")", "{", "}", "[", "]"]
	is_opened = ["(", "[", "{"]
	is_closed = [")", "}", "]"]

	matching = {
		")" = "(",
		"}" = "{",
		"]" = "["
	}

	letterless = [bracket for bracket in line if bracket in is_bracket]
	fakestack = []

	for bracket in letterless:
		if bracket in is_opened:
			fakestack.append(bracket)
		elif bracket in is_closed and matching[bracket] in fakestack:
			fakestack.pop()

		else:
			return False 

	if len(fakestack) > 0:
		return False

	else:
		return True
