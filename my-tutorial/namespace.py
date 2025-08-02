x = "global"  # Global namespace

def outer():
    x = "enclosing"  # Enclosing namespace
    def inner():
        x = "local"  # Local namespace
        print(x)     # Output: "local" (Local scope first)
    inner()

outer()

print(globals())
print(f"\n{locals()}")