from steady_calculations.math_operations import add, div, mult, sub

def test_code():
    assert (add(1,2) == 3)
    
x = 13.4
y = 23.4

print("Hello, World!")
print(add(x,y))
print(div(x,y))
print(mult(x,y))
print(sub(x,y))
print("Goodbye, World!")
