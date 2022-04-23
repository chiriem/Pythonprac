def solution(participant, completion):
    tmp = 0

    dic = {}

    for p in participant:
        dic[hash(p)] = p

        tmp += int(hash(p))

    for com in completion:
        tmp -= hash(com)

    print(dic)
    return dic[tmp]

a = {"a", "b", "c"}
b = {"a", "c"}
print(solution(a, b))