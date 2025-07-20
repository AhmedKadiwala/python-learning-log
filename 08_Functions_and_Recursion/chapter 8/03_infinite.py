def greet(name = "stranger"):
    greet() # this will create an infinite recursion so IDE will fail.
greet()
greet("Ahmed")