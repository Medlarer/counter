
# def func(num,cou):
#     sum = 0
#     if  num == 0:
#         return None
#     if num == 1:
#         return True
#     if cou < 0 or cou > 10 * num:
#         return None
#     for i in range(10):
#         digit = cou - i
#         if digit >= 0:
#             sum += func(num,digit)
#     return sum
#
# def foo():
#     while True:

# store = {}
# def output():
#     print(1)
#
# def f1(sco,num):
#     if sco < 0 or sco > (num+1)*10:
#         return
#     if num == 0:
#         store[num] = sco
#         output()
#         return
#     for i in range(10):
#         store[num] = i
#         f1(sco - i ,num -1)
#
# def f2():
#     f1(90,9)
#     print("总数:",)


seq = []
MAX_SCORE = 10


def butt(n, score):
    global seq, MAX_SCORE
    assert (n >= 1 and score >= 0)
    if n == 1:
        if score <= MAX_SCORE:
            seq.append(score)
            print(seq)
            seq.pop()
            return 1
        else:  # 一次得不了这么多分
            return 0
    else:
        cnt = 0
        for s in range(min(MAX_SCORE, score) + 1):
            # 本靶中s环（s in [0, 1, 2, ...]），计算剩下 n-1 个靶中 score - s 环的情况
            remain_score = score - s

            # 剩下 n-1 个靶全得满分也打不了 score-s 环，就算了
            if (n - 1) * MAX_SCORE < remain_score:
                continue

            seq.append(s)
            cnt += butt(n - 1, remain_score)
            seq.pop()
        return cnt


if __name__ == '__main__':
    all = butt(10, 90)
    print("Total cases:", all)