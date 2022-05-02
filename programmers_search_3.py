def solution(brown, yellow):
    ab = brown + yellow

    for b in range(1, (ab + 1)//2 ):
        if ab % b == 0:
            a = int(ab / b)
            if a >= b:
                if 2 * a + 2 * b == brown + 4:
                    answer = [a, b]

                    return answer


print(solution(10, 2))
