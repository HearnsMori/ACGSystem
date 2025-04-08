import os;

def A():
    ins = input("Project Programming File Extention (Web/Ios/Android if specific OS): ");
    try:
        print(os.listdir(os.path.expanduser("~/A/"+ins2)));
    except:
        os.system("mkdir "+os.path.expanduser("~/A/"+ins2+"/"+ins));
        print("New Skills Unlocked");
    finally:
        ins2 = input("Project Name: ");
        ins3 = "~/A/"+ins.capitalize()+"/"+ins2+"/"+"README.md";
        os.system("vim "+ins3);
