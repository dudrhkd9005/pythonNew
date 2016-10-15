while True:
    num = input('점수:')

    try:
        num = float(num)
        
        if num>=0.9:
            print('A')
        elif num>=0.8 and num<0.9:
            print('B')
        elif num>=0.7 and num<0.8:
            print('C')
        elif num>=0.6 and num<0.7:
            print('D')
        else:
            print('F')
    except:
        print('잘못된 값')
    
