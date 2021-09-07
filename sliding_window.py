'''
Find out the maximum sum of a list with O(n) complexity.
'''


def maxSum(arr, k):
    n = len(arr)
    if n < k:
        print("Invalid!!")
        return -1

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)

    return max_sum


if __name__ == '__main__':
    arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    k = 4
    print(maxSum(arr, k))
