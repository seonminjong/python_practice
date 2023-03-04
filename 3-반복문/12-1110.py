#int 방식으로 문제 해결
a = int(input())
count = 0
original = a  #초기 입력값 저장

while True:
  left = a // 10  #각자리의 숫자를 더하기 위한작업(10의자리)
  right = a % 10  #각자리의 숫자를 더하기 위한작업(1의자리)
  sum2 = left + right  #각 자리를 더해준다.

  new = right * 10 + sum2 % 10  #새로운수 만들기(주어진 수의 오른쪽 자리수(10의자리)와 앞에서 구한 합의 오른쪽자리(1의자리)의 합)
  count += 1  #연산횟수 1 증가(사이클 길이)
  if original == new:
    break  #만약 초기 값과 new의 값이 같다면 반복문을 빠져나온다.

  a = new  #새로운 수를 a에 대입하여 반복할 수 있게 해준다.

print(count)



#str(문자열)입력 방식으로 문제 해결
'''
num = input()  # 문자열 num을 입력받는다.

if int(num) < 10:  # 만약 num이 10보다 작다면
    num = "0" + num  # num의 값 앞에 0을 붙여 준다.

original = num  # num의 값의 초기 값을 저장한다.

sum = 0  # 합을 저장하기 위한 sum값 정의
count = 0  # 횟수를 세기 위한 count 값 정의

while True:  # 무한번 돈다.

    sum = int(num[0]) + int(num[1])  # 숫자의 앞자리와 뒷자리를 더한다.

    if len(str(sum)) == 1:  # 만약 길이가 1이라면
        new_num = num[1] + str(sum)[0]  # 기존의 숫자의 뒷자리와 합계의 한자리를 더한다.
    else:
        new_num = num[1] + str(sum)[1]  # 기존의 숫자의 뒷자리와 합계의 뒷자리를 더한다.

    num = new_num  # 새로 나온 수를 기존의 num에 대입해준다.(계속해서 값을 계산하기 위해)
    count += 1  # 횟수를 1 증가한다.

    if num == original:  # 만약 초기 값과 변화된 num 값이 다시 동일해 졌다면
        print(count)  # 횟수를 출력후
        break  # 반복문을 빠져 나온다.
'''
