import re
import time
import sys


sys.setrecursionlimit(200000)

def calculate_time_execute(func):
    def decorator(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()

        return end - start

    return decorator


def get_input():
    with open("num_1M.inp", "r") as f:
        n = int(f.readline())

        input_list = re.sub(' +', ' ',f.read().replace('\n', '').strip()).split(" ")
        input_list = [int(x) for x in input_list]

    return n, input_list


@calculate_time_execute
def call_quick_sort(input_list, n, left, right):
    quick_sort(input_list, n, left, right)


def partition(input_list, n, left, right):
    pivot = input_list[left]
    low = left + 1
    high = right

    while True:
        while low <= high and input_list[high] >= pivot:
            high = high - 1

        while low <= high and input_list[low] <= pivot:
            low = low + 1

        if low <= high:
            input_list[low], input_list[high] = input_list[high], input_list[low]
        else:
            break

    input_list[left], input_list[high] = input_list[high], input_list[left]
    
    return high

def quick_sort(input_list, n, left, right):
    if left >= right:
        return

    stable = partition(input_list, n, left, right)
    quick_sort(input_list, n, left, stable-1)
    quick_sort(input_list, n, stable+1, right)


def write_output(input_list):
    output = [str(x) for x in input_list]
    with open("sorted.out", "w") as f:
        f.write(" ".join(output))


if __name__ == "__main__":
    n, input_list = get_input()
    time_exec = call_quick_sort(input_list, n, 0, n-1)
    print(time_exec)
    write_output(input_list)

