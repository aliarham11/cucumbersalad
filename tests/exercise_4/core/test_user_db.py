from exercise_4.core.user import UserDB


def test_valid_add_n_delete_user():
	user_db = UserDB()
	bid = user_db.add_user({
		"name": "Jez Humble & David Farley"
	})

	assert len(user_db.users.keys()) == 1

	user_db.delete_user(user_id=bid)

	assert len(user_db.users.keys()) == 0

def test_invalid_delete_user():
	user_db = UserDB()
	
	msg = user_db.delete_user("dummy_id")

	assert msg == "user not found"

def test_valid_add_n_get_user():
	user_db = UserDB()
	expected = {
		"name": "Jez Humble & David Farley"
	}
	bid = user_db.add_user(user=expected)

	assert len(user_db.users.keys()) == 1

	actual = user_db.get_user(user_id=bid)

	assert expected == actual

def test_invalid_get_user():
	user_db = UserDB()
	
	msg = user_db.get_user("dummy_id")

	assert msg == "user not found"

def test_valid_add_n_update_user():
	user_db = UserDB()
	user = {
		"name": "Jez Humble & David Farley"
	}

	expected = {
		"name": "Kurozumi Kanjuro"
	}

	bid = user_db.add_user(user=user)

	assert len(user_db.users.keys()) == 1

	msg = user_db.update_user(user_id=bid, user=expected)
	actual = user_db.get_user(user_id=bid)

	assert msg == "user updated"
	assert expected == actual

def test_invalid_update_user():
	user_db = UserDB()
	
	msg = user_db.update_user(user_id="dummy_id", user={})

	assert msg == "user not found"