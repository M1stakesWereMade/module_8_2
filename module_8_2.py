import re

def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    
    if isinstance(numbers, str):
        numbers = re.findall(r'-?\d+\.?\d*', numbers)
    
    for num in numbers:
        try:
            result += float(num)
        except ValueError:
            incorrect_data += 1
    
    return result, incorrect_data

def calculate_average(numbers):
    try:
        if not hasattr(numbers, '__iter__'):
            raise TypeError("В numbers записан некорректный тип данных")
        
        total_sum, incorrect_count = personal_sum(numbers)
        if incorrect_count > 0:
            print(f"В коллекции содержатся некорректные данные: {incorrect_count} элементов.")
        return total_sum / len(numbers)
    except TypeError as e:
        print(f"Произошла ошибка: {str(e)}")
        return None
    except ZeroDivisionError:
        return 0

print(calculate_average("1, 2, 3"))
print(calculate_average([1, "Строка", 3, "Ещё Строка"]))
print(calculate_average(567))
print(calculate_average([42, 15, 36, 13]))