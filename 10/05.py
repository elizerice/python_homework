soldiers = []
for i in range(int(input())):
    soldiers.append(input())
verdict = int(input())
sum_verdict = int(input())
for i in range(sum_verdict):
    count = 1
    for j in range(1, len(soldiers) + 1):
        if j % verdict == 0:
            soldiers.remove(soldiers[j - count])
            count += 1
for i in soldiers:
    print(i)
