def solution(clothes):
    # headgear, eyewear, face 등 옷 종류별로 구분하기
    clothesTypeMap = {}

    for c, t in clothes:
        if t not in clothesTypeMap:
            clothesTypeMap[t]=2
        else:
            clothesTypeMap[t]+=1

    cnt = 1
    for num in clothesTypeMap.values():
        cnt *= num

    return cnt - 1

if __name__ == '__main__':
    ot = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

    print(solution(ot))