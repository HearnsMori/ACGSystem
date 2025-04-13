from localStoragePy import localStoragePy
from datetime import date
import os
import time
import math
from ASystem import asystem
from CSystem import csystem
from GSystem import gsystem

#Checks percentage when at level
leveltest = 0;

#Level Up@
level = 0;

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
    def gaussianDistribution(self, level):
        # Parameters
        mu = (((7*60*2*37)**.7)*((.1*60*5*37)**.3)*((5*60*2*37)**.1))**(1/3.7); #Mean skill level of the population
        sigma = (((7*60*2*0.137)**.7)*((.1*60*5*0.137)**.3)*((5*60*2*0.137)**.1))**(1/3.7); #Standard deviation of skill levels in the population
        return (level-mu)/sigma;
    def rightSkewedDistribution(self, Z):
        global level;
        #Estimated skewed z-score from a converted z-score from assumed normal distributed but a right-skewed distribution
        #Piecewise function
        if Z < -2.47:
            print("E");
            return Z+2**(1.2/abs(Z));
        elif Z < 0:
            print("D to C");
            return Z+1.4;
        elif Z <= 2.5:
            print("B to A");
            skew_factor = 0.6; #Lower for lower
            return (Z+2.2)**skew_factor;
        else:
            print("A++ to S");
            skew_factor = 2.5; #Higher for lower
            return math.exp(Z / skew_factor);
    def z_to_percentile(self, Z):
        # Z-Score to Percentile mapping (Standard Normal Distribution)
        z_percentile_map = {
            -5.0: 0.0000003,
            -4.9: 0.0000005,
            -4.8: 0.000001,
            -4.7: 0.0000013,
            -4.6: 0.0000021,
            -4.5: 0.0000034,
            -4.4: 0.0000055,
            -4.3: 0.0000085,
            -4.2: 0.0000137,
            -4.1: 0.0000216,
            -4.0: 0.000032,
            -3.9: 0.000048,
            -3.8: 0.000071,
            -3.7: 0.000108,
            -3.6: 0.000154,
            -3.5: 0.000232,
            -3.4: 0.000336,
            -3.3: 0.000483,
            -3.2: 0.000686,
            -3.1: 0.000968,
            -3.0: 0.00135,
            -2.9: 0.00187,
            -2.8: 0.00256,
            -2.7: 0.00347,
            -2.6: 0.00466,
            -2.5: 0.00621,
            -2.4: 0.0082,
            -2.3: 0.01072,
            -2.2: 0.0139,
            -2.1: 0.01786,
            -2.0: 0.02275,
            -1.9: 0.02872,
            -1.8: 0.03593,
            -1.7: 0.04457,
            -1.6: 0.0548,
            -1.5: 0.06681,
            -1.4: 0.08076,
            -1.3: 0.0968,
            -1.2: 0.11507,
            -1.1: 0.13567,
            -1.0: 0.15866,
            -0.9: 0.18406,
            -0.8: 0.21186,
            -0.7: 0.24196,
            -0.6: 0.27425,
            -0.5: 0.30854,
            -0.4: 0.34458,
            -0.3: 0.38209,
            -0.2: 0.42074,
            -0.1: 0.46017,
             0.0: 0.5,
             0.1: 0.53983,
             0.2: 0.57926,
             0.3: 0.61791,
             0.4: 0.65542,
             0.5: 0.69146,
             0.6: 0.72575,
             0.7: 0.75804,
             0.8: 0.78814,
             0.9: 0.81594,
             1.0: 0.84134,
             1.1: 0.86433,
             1.2: 0.88493,
             1.3: 0.9032,
             1.4: 0.91924,
             1.5: 0.93319,
             1.6: 0.9452,
             1.7: 0.95543,
             1.8: 0.96407,
             1.9: 0.97128,
             2.0: 0.97725,
             2.1: 0.98214,
             2.2: 0.9861,
             2.3: 0.98928,
             2.4: 0.9918,
             2.5: 0.99379,
             2.6: 0.99534,
             2.7: 0.99653,
             2.8: 0.99744,
             2.9: 0.99813,
             3.0: 0.99865,
             3.1: 0.99903,
             3.2: 0.99931,
             3.3: 0.99952,
             3.4: 0.99966,
             3.5: 0.99977,
             3.6: 0.99985,
             3.7: 0.99989,
             3.8: 0.99993,
             3.9: 0.99995,
             4.0: 0.999968,
             4.1: 0.999982,
             4.2: 0.999988,
             4.3: 0.999991,
             4.4: 0.999995,
             4.5: 0.999997,
             4.6: 0.999998,
             4.7: 0.999999,
             4.8: 0.9999993,
             4.9: 0.9999995,
             5.0: 0.9999997,
             5.1: 0.9999998,
             5.2: 0.9999998,
             5.3: 0.9999999,
             5.4: 0.9999999,
             5.5: 0.99999993,
             5.6: 0.99999995,
             5.7: 0.99999996,
             5.8: 0.99999997,
             5.9: 0.999999975,
             6.0: 0.99999998,
             6.1: 0.999999984,
             6.2: 0.999999986,
             6.3: 0.999999988,
             6.4: 0.999999989,
             6.5: 0.999999991
        }
        # If the Z-score is outside the provided range, approximate further
        if Z <= -5.0:
            return 0.0;
        elif Z >= 6.5:
            return 1.0;
        
        # Find the closest lower and upper Z-scores for interpolation
        lower_z = max(k for k in z_percentile_map.keys() if k <= Z);
        upper_z = min(k for k in z_percentile_map.keys() if k >= Z);

        if lower_z == upper_z:
            return z_percentile_map[lower_z];

        # Linear interpolation between the two closest Z-scores
        lower_percentile = z_percentile_map[lower_z];
        upper_percentile = z_percentile_map[upper_z];
    
        # Interpolate
        percentile = lower_percentile + (upper_percentile - lower_percentile) * ((Z - lower_z) / (upper_z - lower_z));
    
        return percentile;
    
    def startProgram(self):
        global localStorage, automation, connection, gratification, choices, filename, level;
        self.defVar();
        self.initVar();
        print("Show to everything the ACG System!");
        while True:
            print("\nAutomation: " + str(automation));
            print("Connection: " + str(connection));
            print("Gratification: " + str(gratification));
            # exponential growth function: y = a * (1 + r)^x
            level = (automation**.7)*(gratification**.3)*(connection**.1);
            level = leveltest or level;
            
            level = level**(1/3.7);
            levelOfHistoryBest = (((11*60*7*73)**.7)*((.11*60*5*73)**.3)*((11*60*3*73)**.1))**(1/3.7);
            print(f"My Level: {str(int(731*(1+.37)**(level)))}");
            print(f"History Best Level: {str(int(731*(1+.37)**(levelOfHistoryBest)))}");
            
            # Calculate the Z-score
            Z = self.gaussianDistribution(level);
            Z = self.rightSkewedDistribution(Z);
            percentile = self.z_to_percentile(Z)
            print(f"Your skills are better than {percentile*100:.9f}% to all top 1% and ACG System User.")
            
            print("\n\tRule 0: The ACG Haki, imagining an event one desire. The closer to the time point the better.\n");
            print("\tRule 1: Create Automation System with Flow State. Let the action flow, maximizing the results.\n");
            print("\tRule 2: Reflect the Rule 1 using Connection System. Explain as much visualization and key words as possible.\n");
            print("\tRule 3: Rest using Gratification System. Always be in ACG-Gratitude State; A state in which being grateful that ACG System exist.\n");

            print("Choose:\n\t0. ACG Haki\n\t1. Update Skills\n\t2. Automation System\n\t3. Connection System\n\t4. Gratification System\n\t5. Open App\n\t6. Open Trevo\n\t7. Exit");
            choices = input();
            if not choices:
                choices = 'none';
            if (choices[-1] == '0'):
                while True:
                    ins = input("A task that is closest to your time point that will lead you to Automation of Everything: ");
                    ins2 = input(f'{ins} Task Done (y/n)?');
                    if (ins2 and ins2[-1] == "y"):
                        path = os.path.join('/data/data/com.termux/files/home/C', filename);
                        with open(path, 'a+') as file:
                            file.seek(0);  # Go to start to read contents
                            lines = file.readlines();
                            file.write(f'\nACG Haki: {ins}');

                        path = os.path.join('/data/data/com.termux/files/home/G', filename);
                        with open(path, 'a+') as file:
                            file.seek(0);  # Go to start to read contents
                            lines = file.readlines();
                            file.write(f'\nACG Haki: {ins}');
                    else:
                        break;
            elif (choices[-1] == '1'): 
                os.system("mkdir /data/data/com.termux/files/home/A");
                os.system("scc /data/data/com.termux/files/home/A");
                automation = int(input("cloc from A dir: "));
                localStorage.setItem('a', automation);
                os.system("mkdir /data/data/com.termux/files/home/C");
                os.system("scc /data/data/com.termux/files/home/C");
                connection = int(input("cloc from C dir: "));
                localStorage.setItem('c', connection);
                os.system("mkdir /data/data/com.termux/files/home/G");
                os.system("scc /data/data/com.termux/files/home/G");
                gratification = int(input("cloc from G dir: "));
                localStorage.setItem('g', gratification);
            elif (choices[-1] == '2'):
                asystem.A();
            elif (choices[-1] == '3'):
                csystem.C(filename);
            elif (choices[-1] == '4'):
                gsystem.G(filename);
            elif (choices[-1] == '5'):
                os.system("am start --user 0 -n com.transsion.XOSLauncher/com.android.launcher3.DynamicVirtualEntryActivity ");
            elif (choices[-1] == '6'):
                os.system("am start --user 0 -n com.quyetsama.tnotes/com.example.kanban.MainActivity ");
            elif (choices[-1] == '7'):
                break;

thread = MainProgram();
thread.startProgram();
