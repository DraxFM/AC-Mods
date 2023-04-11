from ReadWriteMemory import ReadWriteMemory
import subprocess
import time
import os

def process_checkup(process_name):
    progs = str(subprocess.check_output('tasklist'))
    if process_name in progs:
        return True
    else:
        return False


if process_checkup("ac_client.exe") == True:
    print()
    print("Assault Cube running")
    print("Launching Health Changer...")
    time.sleep(3)
    os.system("cls")
elif process_checkup("ac_client.exe") == False:
    print()
    print("Error: AC not runnning!")
    print("Please run Assault Box in order to use the health changer!")
    print("Press any key to exit...")
    exit()
    
def main():
    rwm = ReadWriteMemory()
    process = rwm.get_process_by_name("ac_client.exe")
    process.open()

    baseadress = 0x00400000+0x00083134

    healthpointer = process.get_pointer(baseadress, offsets=[0x8, 0xE0, 0x88, 0xEC])

    print()
    print("Enter the health you want to set the adress to: ")
    healthinput = int(input())

    if healthinput >= 1:
        process.write(healthpointer, healthinput)

while True:
    main()
    os.system("cls")
