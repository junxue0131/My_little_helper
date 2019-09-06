import webbrowser 
import time

print("The reminder started!")
flag = 0
while True: 
    print("\nThis program started on: " + time.ctime())
    time.sleep(25 * 60)
    print("\nBreak Time!\t" + time.ctime())
    webbrowser.open("http://106.14.139.144/articles/2019/09/05/1567664492948.html")
    flag = input('continue to remind you?')
    if flag == 'yes':
        continue
    else:
        print('The reminder stopped!')
        break