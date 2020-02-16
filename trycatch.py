try:
    # a = 5/0
    # print(a)
    # name = input('enter your name:')
    # for i in name:
    #     print(i)
    f = open('C:\\Senthil\\testdirs\\MyFolderfilename0.txt', 'w')


except ZeroDivisionError:
    print('error as division by zero')
except KeyboardInterrupt:
    print('Keyboard got interrupted')
except FileNotFoundError:
    print('file not found')
except Exception as e:
    print(e)
else:
    f.write('testing try catch block')
    print('writing file succeeded')
    f.close()
finally:
    print('finally block is here')