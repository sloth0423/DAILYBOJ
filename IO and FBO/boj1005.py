def function1 (aToB, midSet, lastB, allList, bSequen):
    midSet.add(int(aToB[1]))
    midSet.add(int(aToB[0]))
    newMidSet = midSet.copy()
    allList.append(newMidSet)
    # print(allList)
    lastB = int(aToB[0])
    for seq in bSequen:
        if int(seq[1]) == lastB:
            function1(seq, newMidSet, lastB, allList,bSequen)
            break
# testcase 입력 받기
testCase = int(input())
# for문 testcase {
for i in range(testCase):
    # 건물 개수랑 건설 순서 개수 입력받기
    bNumAndBSequenNum = input()
    bNum, bSequenNum = bNumAndBSequenNum.split()
    bNum = int(bNum)
    bSequenNum = int(bSequenNum)
    # 건설 시간 입력받기
    bTime = input()
    bTime = bTime.split()
    # print(bTime)
    # 리스트 요소 출력
    # for j in range (len(bTime)):
    #     print(bTime[j])
    # 건설 순서 입력받기
    bSequen = list()
    for k in range(bSequenNum):
        aToB = input()
        aToB = aToB.split()
        bSequen.append(aToB)
        # print(bSequen)
    # 마지막에 지어야할 건물 입력받기
    lastB = input()
    lastB = int(lastB)
    found = False
    for aToB in bSequen:
        if int(aToB[1]) == lastB:
            found = True
    if found:
        allList = list()
        for aToB in bSequen:
            if int(aToB[1]) == lastB:
                midSet = set()
                function1(aToB, midSet, lastB, allList, bSequen)
        max_length = max(len(s) for s in allList)
        largest_sets = [s for s in allList if len(s) == max_length]
        # print(largest_sets)
        maxNumbers = list()
        for s in largest_sets:
            count = 0
            for t in s:
                count += int(bTime[t-1])
            maxNumbers.append(count)
        maxNumber = max(maxNumbers)
        print(maxNumber)
    if not found:
        print(int(bTime[lastB - 1]))
    # print(maxNumbers)


            # midSet.add(int(aToB[1]))
            # midSet.add(int(aToB[0]))
            # newMidSet = midSet.copy()
            # allList.append(newMidSet)
            # print(allList)

# def function1 (aToB, midset, lastB, allList):
#     midSet.add(int(aToB[1]))
#     midSet.add(int(aToB[0]))
#     newMidSet = midSet.copy()
#     allList.append(newMidSet)
#     print(allList)
#     lastB = aToB[0]
#     function1(aToB, newMidSet, lastB, allList)



# 프로그램 내용 ???
# 대강 설명
# 각 건물 숫자에 맞는 시간 리스트?를 만듦
# 건설 순서를 담는 튜플을 만듦(건설 순서 개수 이용)
# 마지막에 지어야 하는 건물을 두번째 요소로 하는(index로는 1)건물 순서를 찾고 set에? 넣음
# 그 건물 순서의  첫번째 요소를 다시 두번째 요소로 하는 건물 순서를 찾고 다시 set에 넣음
# 없으면 set반환하고 빠져나오도록 만듦
# set들 중에서 노드 개수가 가장 많은 것을 찾음
# 만약 같은 것이 나온다면 값을 계산해서 가장 큰 값이 나오는 set?을 찾음
# 그 값을 출력함
# }
# 이게 되려나...
# 결국 틀렸어
# 난이도 순으로 풀다가 다시 와서 푼다
