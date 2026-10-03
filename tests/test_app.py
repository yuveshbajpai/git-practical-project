from app import add, subtract, login


def test_add():
    assert add(10, 5) == 15


def test_subtract():
    assert subtract(10, 5) == 5


def test_subtract_when_b_is_greater():
    assert subtract(5, 10) == 0


def test_login_success():
    assert login("admin", "admin123") == "Login successful"


def test_login_failure():
    assert login("admin", "wrongpassword") == "Invalid credentials"