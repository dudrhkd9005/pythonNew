성인 =('감사합니다')
청소년 =('반갑습니다')
어린이 =('안녕하세요')
a = int(input('나이:'))
if a>19:
        print(성인)
elif 13<a<20:
        print(청소년)
elif a<14:
        print(어린이)
