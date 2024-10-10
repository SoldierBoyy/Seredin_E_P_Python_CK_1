numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

numbers_without_none = numbers[:4] + numbers[5:]
number_for_change = sum(numbers_without_none) / len(numbers)
numbers[4] = number_for_change

print(f"Измененный список: {numbers}")
