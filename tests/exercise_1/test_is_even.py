from exercise_1.is_even import IsEven

def test_is_even_number():
	is_even = IsEven()
	actual = is_even(2)
	expected = True

	assert actual == expected

def test_is_odd_number():
	is_even = IsEven()
	actual = is_even(1)
	expected = False

	assert actual == expected

def test_error_params():
	is_even = IsEven()
	actual = is_even("ss")
	expected = None

	assert actual == expected
