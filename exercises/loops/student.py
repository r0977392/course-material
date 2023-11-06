def print_numbers(a, b, step):
    current = a
    while current < b:
        print(current)
        current += step

def thanos(queue_size, target_size):
    snap_count = 0
    while queue_size > target_size:
        queue_size //= 2
        snap_count += 1
    return snap_count

def sum_input():
    result = 0
    while (value := int(input())) != 0:
        result += value
    print(f'The sum equals {result}')
    
def factorial(n):
    result = 1
    for k in range(2, n+1):
        result *= k
    return result

