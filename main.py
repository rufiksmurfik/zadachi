def how_many_called(n: int, k: int) -> int:
    num_of_called = 0
    max_num = 0
    i = 1
    while num_of_called < k:
        num_of_called += i
        max_num = i
        i += 1
    return max_num


if __name__ == "__main__":
    n = int(input())
    k = int(input())
    result = how_many_called(n, k)
    print(result)
xxx