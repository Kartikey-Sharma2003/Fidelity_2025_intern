try:
    x=int(input("enter the number:"))
    y=int(input("enter the number:"))
    print(x/y)
except ZeroDivisionError:
    print('Error')
except ValueError:
    print("Value Error")    
#except Exception as msg:
    #print(msg.with_traceback)        