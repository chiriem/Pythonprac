from itertools import permutations
import math

def numberCheck(num):
    # 0, 1은 소수가 아니다
    if num == 0 or num == 1:
        return False
    else:
        # 2부터 입력 받은 숫자의 제곱근 값까지 반복
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
    return True

def solution(numbers):
    answer = []

    for i in range(1, len(numbers)+1):

        # 숫자들의 경우의 수를 모두 순열로 배열
        arr = list(permutations(numbers, i))

        for j in range(len(arr)):

            # 문자를 숫자로 변환
            num = int(''.join(map(str, arr[j])))

            # 소수 확인
            if numberCheck(num):
                answer.append(num)

    # 중복 제거
    answer = set(answer)

    return len(answer)

numbers = "17"
print(solution(numbers))