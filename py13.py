# page 85 (1)
'''10  99 사이의 정수를 입력하세요 >>> 45
십의자리 : 4
일의자리 : 5
'''

print()
문제 = int(input('10 ~ 99 사이의 정수를 입력하세요 >>> '))
십의자리 = int(문제/10)
일의자리 = 문제%10

print('십의자리: {}'.format(십의자리))
print('일의자리: {}'.format(일의자리))
# 힌트 : 10으로 나누면 십의자리, 10의 나머지는 일의자리
