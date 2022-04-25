def solution(answers):
    answer = []

    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    results = {1: 0, 2: 0, 3: 0}

    for i in range(len(answers)):

        if student1[i % 5] == answers[i]:
            results[1] += 1

        if student2[i % 8] == answers[i]:
            results[2] += 1

        if student3[i % 10] == answers[i]:
            results[3] += 1

    for i in range(1, 4):
        if results[i] == max(results.values()):
            answer.append(i)


    print(results)

    return answer

if __name__ == '__main__':
    ot = [2,3,4,2,2,4,5,3,4,4,5,1,2,3,2,4,3,3,1,4,2]

    print(solution(ot))