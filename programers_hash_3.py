def solution(clothes):
    # headgear, eyewear, face 등 옷 종류별로 구분하기
    clothesTypeMap = {}

    for clothe, clothesType in clothes:
        print(clothe)
        print("clotheType : ", clothesType)

        # 옷 종류마다 값을 1 더하기
        clothesTypeMap[clothesType] = clothesTypeMap.get(clothesType, 0) + 1

        print(clothesTypeMap)

    # 옷 안입은 경우 계산
    answer = 1
    for clothesType in clothesTypeMap:
        answer *= (clothesTypeMap[clothesType] + 1)

    # 아무것도 안입은 경우 계산
    return answer - 1

if __name__ == '__main__':
    ot = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]

    print(solution(ot))