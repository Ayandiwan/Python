def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True
# Test the prime number checker
print("For 17", prime(17))
print("For 20", prime(20))
print("For 2", prime(2))




def cel_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_cel(fahrenheit):
        return (fahrenheit - 32) * 5/9
    
print("25°C to Fahrenheit:", cel_to_fahrenheit(25))
print("77°F to Celsius:", fahrenheit_to_cel(77))



def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))
print("Factorial of 7:", factorial(7))