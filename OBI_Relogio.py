from datetime import datetime, timedelta


H = int(input())
M = int(input())
S = int(input())
T = int(input())

hora_real = datetime(2024, 6, 13, H, M, S)

adiou = timedelta(seconds=T)

H_novo = hora_real + adiou

print(H_novo.hour)
print(H_novo.minute)
print(H_novo.second)


