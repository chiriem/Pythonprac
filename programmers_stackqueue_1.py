from collections import deque

def solution(priority, location):

    myDeque = deque([(v,i) for i,v in enumerate(priority)])

    answer = 0

    while myDeque:
        firstData = myDeque.popleft()

        if myDeque and max(myDeque)[0] > firstData[0]:
            myDeque.append(firstData)

        else:
            answer += 1
            if location == firstData[1]:
                break

    return answer

if __name__ == '__main__':
    array = [2,1,3,2]
    location = 2

    print(solution(array, location))