while True:

   inp =input('화씨온도:')
   try:
       fahr = float(inp)
       섭씨온도 = (fahr - 32.0)*5.0/9.0
       print(섭씨온도)
   except:
       print('숫자를 넣으시오')
