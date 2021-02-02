def solution(l, d, x):
    # a + (n - 1)d : 안녕 나는 등차수열 공식이라고 해~
    sequenceList = []

    a = 1 # 첫째항 1

    for n in range(a, l + 1):
        # 여기서 등차수열공식을 이용하여 계산!
        sequenceList.append(a + (n - 1) * d)
    
    # 필터를 이용하여 x보다 낮은 등차수열 값을 구해보자.
    countLessThan = len(list(filter(lambda t: t < x, sequenceList)))

    return [sequenceList, countLessThan]


if __name__ == "__main__":
    print("[Solution Example 4-3] Bienvenue!")
    print("Question 4-3: ")

    print("모든 입력값은 정수여야 합니다.")

    n = input("정수 n을 입력하세요:")
    m = input("정수 m을 입력하세요:")
    x = input("정수 x을 입력하세요:")

    Result = solution(int(n), int(m), int(x))

    print(str(Result[0]))
    
    if Result[1] == 0:
        print("None")
    else: print("count = %d" % Result[1])