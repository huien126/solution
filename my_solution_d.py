# 순서대로 작성해보자

def getJurorInfo(): # 함수 이름은 마음대로 정할 수 있음.. :ㅇ
    gradeCard = [] # 빈 성적표 ;b

    # 유저로부터 심사위원 수를 입력 받기
    numberOfPeople = input("심사위원 수를 입력하세요:")

    # 유저로부터 입력 받은 것은 type이 string이기 때문에 int(정수)로 재 정의
    numberOfPeople = int(numberOfPeople)

    if numberOfPeople < 3: # 문제 조건에 심사위원은 3명 이상
        print('심사위원 수는 최소 3명 이상이어야 합니다.')
        return False
    
    for jurorIdx in range(numberOfPeople): # 심사위원마다 점수를 물어보자
        score = input("%d번째 심사위원의 점수는 (1~100):" % (jurorIdx + 1))
        score = int(score)

        if 1 <= score and score <= 100: # 점수가 1~100점이 맞다면 
            gradeCard.append(score) # 성적표에 점수를 기입한다.
        else:
            print('점수는 1~100이내의 범위에 있어야 합니다.')
            return False
    
    # 이제 심사위원들의 성적표가 완성됐어, 정보를 반환해보자

    return gradeCard

if __name__ == "__main__": # 이건 굳이 필요 없음.. 이것은 모듈이 아니기 때문에
    print("모든 입력값은 양의 정수입니다.")
    
    gradeCard = getJurorInfo() # 유저에게 정보를 입력받기!

    if gradeCard != False: # 조건에 맞게 입력을 받았다면
        i_max = max(gradeCard) # 최대
        i_min = min(gradeCard) # 최소
        print(str(gradeCard)) # 성적표 배열 문자열로서 출력하기!
        print('Max: %d, Min: %d' % (i_max, i_min))
        print('Total score: %d' % (sum(gradeCard) - (i_max + i_min)))
        
    else: # 조건에 맞지 않는 입력값을 받았다면
        print('작업을 종료합니다.')