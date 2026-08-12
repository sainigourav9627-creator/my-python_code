def add(a: int, b: int) -> int:
    """This function adds two numbers."""
    return a + b


print(add.__name__)
print(add.__doc__)
print(add.__annotations__)

__name__        → Function ka NAME
__doc__         → Function ki DOCUMENTATION
: type          → Parameter TYPE information
-> type         → RETURN TYPE information
__annotations__ → Saari ANNOTATIONS dekhna
