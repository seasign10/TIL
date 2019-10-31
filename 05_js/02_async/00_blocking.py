from time import sleep # 잠시 시스템을 멈추게 하는 것

def sleep_3s():
    sleep(3)
    print('Wake up!')

print('Start sleeping')
sleep_3s() # 해당식이 동작되기 전까지는
print('End of program') # 동작하지 않게 된다. => 그때까지 코드의 실행을 blocking => 동기식 처리