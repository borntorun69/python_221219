# import webbrowser
# webbrowser.open('hrrtps://www.google.com/')
# webbrowser.open_new('hrrtps://www.google.com/')
import time, threading, requests, sys

def long_task():
  for i in range(5):
    time.sleep(0.5)
    print(f"working: {i}\n")

print("start")

threads = []
for i in range(3):
  #순차적으로 진행
  #long_task()

  # thread를 이용한 프로그래밍
  t = threading.Thread(target=long_task)
  threads.append(t)
  t.start()
  t.join() #비동기적인 흐름을 순차적으로 동기화가능

print("end")


def getHtml(url):
  result = requests.get(url)
  time.sleep(1)
  print(url, result.text, '  chars')
t1 = threading.Thread(
  target=getHtml, args=('https://www.google.com/',)).start()

