1️⃣ Generator Expression क्या है?

Generator बनाने का short तरीका Generator Expression कहलाता है।
पहले हम function लिखते थे:

def numbers():
    for i in range(1, 6):
        yield i


अब इसी काम को छोटा करके:
numbers = (i for i in range(1, 6))

बस इतना। ✅
🧠 Difference

Generator Function:
def numbers():
    for i in range(1, 6):
        yield i

Generator Expression:
numbers = (i for i in range(1, 6))

यहाँ ध्यान दो:
[ ] → List
( ) → Generator Expression

याद रखने की Trick
Generator Function → yield वाला function
Generator Expression → (expression for item in iterable)


numbers = (i for i in range(1, 6))

print(next(numbers))
print(next(numbers))
print(next(numbers))

