run=10
prybavlRun=0
runSum=10
day=0
dayNumber=int(input('Введите количество дней:'))
for i in range (9):
    prybavlRun=run*0.1
    run+=prybavlRun
    print('Пробег лыжника за',i+2,'день:',round(run,1))
run=10
prybavlRun=0
for i in range (6):
    prybavlRun=run*0.1
    run+=prybavlRun
    runSum+=run
print('Суммарный пробег лыжника за 7 дней:',round(runSum,1))
run=10
prybavlRun=0
runSum=10
if dayNumber == 0:
    runSum = 0
else:
    for i in range (dayNumber-1):
            prybavlRun=run*0.1
            run+=prybavlRun
            runSum+=run
print('Суммарный пробег лыжника за количество введенных дней:',round(runSum,1))
runSum=10
run=10
prybavlRun=0
while runSum<80:
    prybavlRun = run * 0.1
    run += prybavlRun
    runSum += run
    day+=1
print('Лыжнику не стоит увеличивать пробег на',day,'день')




