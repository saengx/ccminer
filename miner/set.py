import os, time, json
from config import banneredit
from multiprocessing import cpu_count


cpu_thread = cpu_count()


def setminer():

   banneredit()
   try:
       print("0-5 \033[93mปกติ 3\033[00m")
       cpu-priority = int(input("[cpu-priority]: ")
       print("\033[35m-----------------------------------------\033[0m")

       print(f"ค่า full-acess ip \033[93mเช่น 192.168.1.0/24\033[00m")
       api-allow = int(input("[api-allow]: "))
       print("\033[35m-----------------------------------------\033[0m")

       print(f"ค่า bind ip:port \033[93mเช่น 0.0.0.0:4068\033[00m")
       api-bind = int(input("[api-bind]: "))
       print("\033[35m-----------------------------------------\033[0m")
   except:
            os.system("@cls||clear")
            print("เกิดข้อผิดพลาดโปรดตั้งค่าใหม่!")
            time.sleep(3)
            os.system("set")
   push = {
          'cpu-priority': cpu-priority,
          'api-allow': api-allow,
          'api-bind' : api-bind
          }
   with open("setip/set-cpu.json", "w") as set:
     json.dump(push, set, indent=4)

while True:
  banneredit()
  setminer()
  os.system("run-miner")     
  break
