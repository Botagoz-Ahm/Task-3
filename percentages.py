P = int(input())
X = int(input())
Y = int(input())
now = 100 * X + Y
after_year = int(now * (100 + P) / 100)
print(after_year // 100, after_year % 100) 
