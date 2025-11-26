import os
print(f"\033[1;32;40mCPU Information\033[00m\n")
print("\033[96m")
os.system("lscpu|grep -i 'model name'")
os.system("lscpu|grep -i 'CPU max MHz'")
os.system("lscpu|grep -i 'On-line CPU(s) list'")
print("\033[00m")

print("**********************************************\n");	
print("\033[36m ccminer CPU High Hashrate \033[00m  : " 4.0 "\n");
print("Verushash v2.2 based on ccminer\n");
print("**********************************************\n");	
   
