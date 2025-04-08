from localStoragePy import localStoragePy
from datetime import date
import os
import time
import math

class MainProgram:
    def __init__(self):
        pass;
    def defVar(self):
        global localStorage, automation, connection, gratification, choices, filename;
        localStorage = localStoragePy('game', 'text')
        automation = 0
        connection = 0
        gratification = 0
        choices = 0
        filename = date.today().strftime("%Y%B%d") + ".txt"
    def initVar(self): 
        global localStorage, automation, connection, gratification, choices, filename;
        if (localStorage.getItem('a')) is not None:
            automation = int(localStorage.getItem('a'));
        if (localStorage.getItem('c')) is not None:
            connection = int(localStorage.getItem('c'));
        if (localStorage.getItem('g')) is not None:
            gratification = int(localStorage.getItem('g'));
    def startProgram(self):
        global localStorage, automation, connection, gratification, choices, filename;
        self.defVar();
        self.initVar();
        while True:
            print("\nAutomation: " + str(automation));
            print("Connection: " + str(connection));
            print("Gratification: " + str(gratification));
            base = (automation*1)+(connection*3)+(gratification*7);
            level = float(format( (base**(1/3.7))*137, '.2f'));
            level += 137;
            levelOfHistoryBest = 130000000;
            log = abs(math.log(137/levelOfHistoryBest)/math.log(137)) - abs(math.log(level/levelOfHistoryBest)/math.log(137));
            log = log/abs(math.log(137/levelOfHistoryBest)/math.log(137));
            log = 1 - log**(.000137/137000);
            topPercentageInHistory = format(log, '.10%');
            topPercentageInHistoryFloat = log;
            topPercentageInHistoryString = str(float(topPercentageInHistory.replace('%', 'e-2')));
            print("Level: " + str(level));
            if (topPercentageInHistoryFloat >= 10/100):
                print("Your skills belong to top " + topPercentageInHistory[0] + " in 10 Humanity ever Existed.");
            elif (topPercentageInHistoryFloat >= 1/100):
                print("Your skills belong to top " + topPercentageInHistory[0] + " in 100 Humanity ever Existed."); 
            elif (topPercentageInHistoryFloat >= 0.1/100):
                print("Your skills belong to top " + topPercentageInHistory[2] + " in 1K Humanity ever Existed.");
            elif (topPercentageInHistoryFloat >= 0.01/100):
                print("Your skills belong to top " + topPercentageInHistory[3] + " in 10K Humanity ever Existed.");
            elif (topPercentageInHistoryFloat >= 0.001/100):
                print("Your skills belong to top " + topPercentageInHistory[4] + " in 100K Humanity ever Existed.");
            elif (topPercentageInHistoryFloat >= 0.0001/100):
                print("Your skills belong to top " + topPercentageInHistory[5] + " in 1M Humanity ever Existed.");
            elif (topPercentageInHistoryFloat >= 0.00001/100):
                print("Your skills belong to top " + topPercentageInHistory[6] + " in 10M Humanity ever Existed.");
            elif (topPercentageInHistoryFloat >= 0.000001/100):
                print("Your skills belong to top " + topPercentageInHistory[7] + " in 100M Humanity ever Existed.");
            elif (topPercentageInHistoryFloat >= 0.0000001/100):
                print("Your skills belong to top " + topPercentageInHistory[8] + " in 1B Humanity ever Existed.");
            elif (topPercentageInHistoryFloat >= 0.00000001/100):
                print("Your skills belong to top " + topPercentageInHistory[9] + " in 10B Humanity ever Existed.");
            elif (topPercentageInHistoryFloat >= 0.000000001/100):
                print("Your skills belong to top " + topPercentageInHistory[10] + " in 100B Humanity ever Existed.");
            else:
                print("Your skills belong to top 0." + topPercentageInHistory[11] + " in All Humanity Ever Existed. You broke the limit.");
            print("\n\tRule 1: Create/Execute Automation System with Flow State. Set aside beliefs and doubts; let the action flow with maximizing the results in mind.\n");
            print("\tRule 2: Reflect the Rule 1 using the Connection System. Set aside beliefs and find the best action.\n");
            print("\tRule 3: Rest using the Gratification System. Avoid Stimulation unrelated to ACG.\n");

            print("Choose:\n\t1. Update Skills\n\t2. Automation\n\t3. Upgrade Level\n\t4. Open App\n\t5. Exit");
            choices = int(input());
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
                ins = input("P/D Plan an automation project or develop automation project: ");
                if ins == "P":
                    os.system("am start --user 0 -n com.quyetsama.tnotes/com.example.kanban.MainActivity");
                if ins == "D":
                    ins2 = input("Project Programming File Extention (Web/Ios/Android if specific OS): ");
                    try:
                        print(os.listdir(os.path.expanduser("~/A/"+ins2)));
                    except:
                        print("New Skills Unlocked");
                    finally:
                        ins = input("Project Name: ");
                        os.system("mkdir "+os.path.expanduser("~/A/"+ins2+"/"+ins));
                        ins3 = "~/A/"+ins2.capitalize()+"/"+ins+"/"+"README.md";
                        os.system("vim "+ins3);
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

thread = MainProgram();
thread.startProgram();
