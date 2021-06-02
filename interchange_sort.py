import re
import time


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
def interchange_sort(input_list, n):
    for i in range(n-1):
        for j in range(i+1, n):
            if input_list[i] > input_list[j]:
                input_list[i], input_list[j] = input_list[j], input_list[i]


def write_output(input_list):
    output = [str(x) for x in input_list]
    with open("sorted.out", "w") as f:
        f.write(" ".join(output))


if __name__ == "__main__":
    n, input_list = get_input()
    time_exec = interchange_sort(input_list, n)
    print(time_exec)
    write_output(input_list)

