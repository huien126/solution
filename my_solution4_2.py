# n 이하의 자연수들중 m의 배수
    ''' Tip for developer: 
        input (6, 2)

        6 이하의 자연수
        1, 2, 3, 4, 5, 6

        2의 배수 
        2, 4, 6, 8, 10 ...

        후! 그러면 저걸 리스트로 만든다음 교집합 구하면 깔끔히 나오네?
        다만 2의 배수를 다 적기에는 불가능 하기에.. 이런 방법으로 접근해보자

        n 이하의 자연수에 m을 나눈 나머지가 0이라면 그 뜻은 m의 배수라는거겠지?
        그것만 리스트로 만드는거야, 딱 한줄이면 돼!
    '''

def solution(n, m):
    return [i for i in range(1, n+1) if i % m == 0]

if __name__ == "__main__":
    print("[Solution Example 4-2] Bienvenue!")
    print("Question 4-2: ")

    print("모든 입력값은 자연수여야 합니다.")

    n = input("자연수 n을 입력하세요")
    m = input("자연수 m을 입력하세요")

    Result = solution(int(n), int(m))

    print("total = %d" % sum(Result))
    print("count = %d" & len(Result))