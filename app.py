def add(a, b):
    return a + b


def subtract(a, b):
    return a - b

def login(username, password):
    if username == "admin" and password == "admin123":
        return "Login successful"
    return "Invalid credentials"


if __name__ == "__main__":
    print("Addition:", add(10, 5))
    print("Subtraction:", subtract(10, 5))