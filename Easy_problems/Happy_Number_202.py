number = int(input())

def is_happy(n: int) -> bool:

    was_sum = dict()

    cur_sum = 0
    for i in str(n):
        cur_sum += int(i) ** 2

    while True:

        if cur_sum == 1:
            return True
        elif not cur_sum in was_sum:
            was_sum[cur_sum] = 1
            cur_sum = sum([int(i) ** 2 for i in str(cur_sum)])
        elif cur_sum in was_sum:
            return False




#damn , i solved it with O(1)

