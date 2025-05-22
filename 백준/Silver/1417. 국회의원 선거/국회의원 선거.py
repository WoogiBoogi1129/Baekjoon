'''
선거 조작
누구를 찍을 지 미리 읽기 가능
어떤 사람이 누굴 찍을 지 선택 --> 반드시 선거 때 그 사람 찍음
국회의원 후보 N명
주민 M 명의 마음 읽음
다솜이는 기호 1번
자신을 찍지 않으려는 사람 돈으로 매수
다른 모든 사람의 득표수 보다 많은 득표수 -> 국회의원 당선
'''

vote = []
answer = 0
n = int(input())
dasom = int(input())
if n == 1:
    print(answer)

else:
    for _ in range(n-1):
        vote.append(int(input()))
        
    vote.sort(reverse = True)

    while vote[0] >= dasom:
        vote[0] -= 1
        answer += 1
        dasom += 1
        vote.sort(reverse = True)
        
    print(answer)