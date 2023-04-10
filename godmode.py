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
    print("Launching Godmode...")
    time.sleep(3)
    os.system("cls")
elif process_checkup("ac_client.exe") == False:
    print()
    print("AC not runnning!")
    print("Please run Assault Box in order to use Godmode!")
    print("Press any key to exit...")
    exit()
    
rwm = ReadWriteMemory()
process = rwm.get_process_by_name("ac_client.exe")
process.open()

baseadress = 0x00400000+0x00083134

healthpointer = process.get_pointer(baseadress, offsets=[0x8, 0xE0, 0x88, 0xEC])

print()
print("Running Godmode. Do not close this window as long as you want to use godmode!")
print("If a new match begins please restart godmode!")

while True:
    process.write(healthpointer, 9999)
    time.sleep(.2)
