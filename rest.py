import webbrowser 
import time

print("The reminder started!")
flag = 0
while True: 
    start = time.time()
    min = 25

    print("\nThis program started on: " + time.ctime())
    while time.time() < start + min * 60:
        last_time = time.time() - start
        print(str(round(last_time*100 / (min * 60), 4))+'%', end='\r')
    print("\nBreak Time!\t" + time.ctime())
    webbrowser.open("http://106.14.139.144/articles/2019/09/05/1567664492948.html")
    flag = input('continue to remind you?\n')
    if flag == 'yes':
        continue
    else:
        print('The reminder stopped!')
        break