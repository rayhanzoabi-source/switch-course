def extract_str(s):
   str_with_number = s[14:]
   try:
       return int(str_with_number)
   except ValueError:
       return 0

def add(a, b):
   return a + b

def multiply(a, b):
   return a * b

def divide(a, b):
   try:
       return a / b
   except ZeroDivisionError:
       return 0

def average(numbers):
   if not numbers:
       return 0
   return sum(numbers) / len(numbers)

def power(base, exponent):
   try:
       return base ** exponent
   except Exception:
       return 0

def get_max(numbers):
   if not numbers:
       return 0
   return max(numbers)

def get_min(numbers):
   if not numbers:
       return 0
   return min(numbers)

def calculate_range(numbers):
   if not numbers:
       return 0
   return get_max(numbers) - get_min(numbers)

def calculate_factorial(n):
   if n < 0:
       return 0
   if n == 0:
       return 1
   return n * calculate_factorial(n - 1)

def process_string_operations():
   strings = {
       'str1': "my number is 26",
       'str2': "my number is ll",
       'str3': "my number is 10",
       'str4': "my number is 0",
       'str5': "my number is -5",
       'str6': "my number is",
       'str7': "wrong format 20"
   }
   
   numbers = {key: extract_str(value) for key, value in strings.items()}
   return numbers

def perform_basic_operations(numbers):
   results = {}
   
   results['sum1'] = add(numbers['str1'], 4)
   results['sum2'] = add(numbers['str2'], 9)
   results['result1'] = add(results['sum1'], results['sum2'])
   
   results['mult1'] = multiply(numbers['str1'], numbers['str3'])
   results['div1'] = divide(results['mult1'], numbers['str4'])
   
   return results

def perform_list_operations(numbers):
   results = {}
   
   number_list = [value for value in numbers.values()]
   
   results['average'] = average(number_list)
   results['max'] = get_max(number_list)
   results['min'] = get_min(number_list)
   results['range'] = calculate_range(number_list)
   
   return results

def perform_complex_operations(numbers, basic_results, list_results):
   results = {}
   
   results['power1'] = power(numbers['str3'], 2)
   results['factorial1'] = calculate_factorial(numbers['str3'])
   
   results['complex_sum'] = add(
       multiply(basic_results['mult1'], list_results['average']),
       power(list_results['range'], 2)
   )
   
   results['mega_operation'] = divide(
       add(
           power(list_results['max'], 2),
           multiply(list_results['min'], basic_results['sum1'])
       ),
       list_results['average'] if list_results['average'] != 0 else 1
   )
   
   return results

def calculate_advanced_metrics(numbers_dict):
   numbers = list(numbers_dict.values())
   results = {}
   
   positive_numbers = [n for n in numbers if n > 0]
   results['positive_average'] = average(positive_numbers)
   
   negative_numbers = [n for n in numbers if n < 0]
   results['negative_average'] = average(negative_numbers)
   
   results['squares_sum'] = sum([power(n, 2) for n in numbers])
   
   valid_factorials = {k: calculate_factorial(v) for k, v in numbers_dict.items() 
                      if v >= 0 and v <= 10}
   results['factorials'] = valid_factorials
   
   return results

def main():
   try:
       numbers = process_string_operations()
       basic_results = perform_basic_operations(numbers)
       assert list(basic_results.values()) == [30,20,50,260,0], "wrong results"
       
       print("\nPerforming list operations...")
       list_results = perform_list_operations(numbers)
       print("List operation results:", list_results)
       
       print("\nPerforming complex operations...")
       complex_results = perform_complex_operations(numbers, basic_results, list_results)
       print("Complex operation results:", complex_results)
       
       print("\nCalculating advanced metrics...")
       advanced_results = calculate_advanced_metrics(numbers)
       print("Advanced metrics results:", advanced_results)
       
   except Exception as e:
       print(f"An error occurred: {str(e)}")
       
if __name__ == "__main__":
   main()