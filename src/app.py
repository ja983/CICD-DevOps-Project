def greet(name):
    if not name or not name.strip():
        raise ValueError("Name cannot be empty")
    return f"Welcome, {name}!"

def farewell(name):
    return f"Goodbye, {name}!"

print(greet("DevOps Engineer"))
print(farewell("DevOps Engineer"))
