def solution(number):
    answer = sum(list(dict.fromkeys(list(filter(lambda x: x % 3 == 0 or x % 5 == 0, [i for i in range(1, number)])))))
    return answer

print(solution(10))