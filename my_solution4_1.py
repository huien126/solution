def solution(priceTotal):
    ratio = 0

    if priceTotal >= 100000:
        ratio = 10
    elif priceTotal >= 50000:
        ratio = 5

    return int(priceTotal - (priceTotal * (ratio/100)))


if __name__ == "__main__":
    print("모든 입력값은 0이상의 정수여야합니다.")

    priceTotal = 0

    for ProductIdx in range(11):
        priceInput = input("%d번째 제품의 금액을 입력해주세요:" % (ProductIdx+1))
        priceInt = int(priceInput)

        if priceInt == 0:
            break
        else:
            priceTotal = priceTotal + priceInt
    
    print("total =  %d" % solution(priceTotal))