import math

def numberCheck(num):
    # 0, 1은 소수가 아니다
    if num == 0 or num == 1:
        return False
    else:
        # 2부터 입력 받은 숫자의 제곱근 값까지 반복
        for i in range(2, int(math.sqrt(num)) + 1):
            print(i)
            if num % i == 0:
                return False
    return True

print(numberCheck(7))