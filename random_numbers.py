import random

def append_random_numbers(arry, quantity = 1):
    while quantity >= 0:
        arry.append(random.randint(-100, 100))
        quantity -= 1
    return arry

def append_random_words(arry, quantity = 1):
    words = ["Dog","Cat","Rat","Bird"]
    while quantity >= 0:
        arry.append(random.choice(words))
        quantity -= 1
    return arry

def main():
    numbers = [10,18,22,36,42,78,99]
    print(numbers)
    numbers = append_random_numbers(numbers)
    print(numbers)
    numbers = append_random_numbers(numbers,5)
    print(numbers)

    words = ["List","starts"]
    print(words)
    numbers = append_random_words(words)
    print(words)
    numbers = append_random_words(words,2)
    print(words)
    
