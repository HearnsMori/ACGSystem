from localStoragePy import localStoragePy
from datetime import date
import os

localStorage = localStoragePy('game', 'text')
automation = 0
connection = 0
gratification = 0
choices = 0
filename = date.today().strftime("%Y%B%d") + ".txt"

while True:
    print("Rule 1: Create/Execute Automation System with Flow State. Set aside beliefs and doubts; let the action flow with maximizing the results in mind.\n");
    print("Rule 2: Reflect the Rule 1 using the Connection System. Set aside beliefs and find the best action.\n");
    print("Rule 3: Rest using the Gratification System. Avoid Stimulation unrelated to ACG.\n");

    print("Choose:\n\t1. Update Skills\n\t2. Automation\n\t3. Upgrade Level\n\t4. Open App\n\t5. Exit");
    choices = int(input());
    if (localStorage.getItem('a')) is not None:
        automation = int(localStorage.getItem('a'));
    if (localStorage.getItem('c')) is not None:
        connection = int(localStorage.getItem('c'));
    if (localStorage.getItem('g')) is not None:
        gratification = int(localStorage.getItem('g'));
    if (choices == 1):
        ins = input("A/C/G which cloc to update: ");
        if ins == "A":
            os.system("scc ~/A");
            automation = int(input("cloc from A dir: "));
            localStorage.setItem('a', automation);
        elif ins == "C":
            os.system("scc ~/C");
            connection = int(input("cloc from C dir: "));
            localStorage.setItem('c', connection);
        elif ins == "G":
            os.system("scc ~/G");
            gratification = int(input("cloc from G dir: "));
            localStorage.setItem('g', gratification);
    elif (choices == 2):
        ins = input("C/A Create automation project or start executing automation project: ");
        if ins == "C":
            os.system("am start --user 0 -n com.quyetsama.tnotes/com.example.kanban.MainActivity");
        if ins == "A":
            break;
            os.system("cd ~/A");
    elif (choices == 3):
        ins = input("C/G which to upgrade: ");
        if ins == "C":
            os.system(("vim ~/C/"+ filename));
        elif ins == "G":
            os.system(("vim ~/G/"+ filename));
    elif (choices == 4):
        os.system("am start --user 0 -n com.transsion.XOSLauncher/com.android.launcher3.DynamicVirtualEntryActivity ");
    elif (choices == 5):
        break;
    print("Automation: " + str(automation));
    print("Connection: " + str(connection));
    print("Gratification: " + str(gratification));
    print("Level: " + str((int(automation*connection*gratification)**(1/7))*10));
