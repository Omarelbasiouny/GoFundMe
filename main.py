import csv
import re
import os
import datetime
import random
import fileinput
import pathlib
dirpath = pathlib.Path().resolve()
# regEX Values
regex_EML = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"    # E-mail Confirmation
regex_PWRD = "(?=.*\d)(?=.*[A-Z])\w{8,}"       # At least 1Num, 1Uppercase, 8 or more characters
regex_MN = "^[0][1][0125]\d{8,8}$"
regex_target = "\d+$"
PWRD = ""
# Title
print("GoFundMe App!")

# # STEP 1 App Authentication
def loginQ():
    global Auth
    Auth = (input(" 1-Signup\n 2-Login\n"))
loginQ()
if  Auth != "1" and Auth != "2":
     loginQ()
def signup(Auth):
    i = 0
    if Auth == "1" :
        global PWRD
        print("Please Enter the required information to Signup")
        FN = input("First Name:")
        LN = input("Last Name:")
        EML = input("E-mail:")
        while not re.search(regex_EML, EML):
            EML = input("Please Enter Your E-mail Correctly\n")
        PWRD = input("Password:")
        while not re.search(regex_PWRD, PWRD):
            print("Your Password is Weak \n It should have at least \n 8 characters \n One Uppercase letter \n One digit")
            PWRD = input("Try Stronger Password:")
        CFPWRD = input("Confirm Password:")
        while not CFPWRD == PWRD:
            print("This don't match your assigned Password")
            CFPWRD = input("Reconfirm your Password:\n")
            i+=1
            if i == 3:
                print(" Too many attempts!")
                signup("1")

        MN = input("Mobile Number:\n")
        while not re.search(regex_MN, MN):
            MN = input("Please enter your number correctly\n")
        New_User = [EML, PWRD, FN, LN, MN]
        with(open('Auth.csv', 'a')) as Authfile:
            csv_writer = csv.writer(Authfile)
            csv_writer.writerow(New_User)
    Applogin("2")

def Applogin(Auth):
    if Auth == "2":
        global PWRD
        print("login")
        with(open('Auth.csv', 'r')) as Authfile:
            reader = csv.reader(Authfile)
            EML = input("E-mail: ")
            PWRD = input("Password: ")

            for row in reader:
                if row[0]==EML and row[1]==PWRD:
                    login = True
                    break
                else:
                    login = False
        if login == True:
            print("Welcome", row[2])

        elif login == False:
            print("Wrong E-mail or Password")
            wrong_credentials = input("Do you want to signup a new account y/n")
            if wrong_credentials == "y":
                signup("1")
            elif wrong_credentials == "n":
                Applogin("2")
            else:
                exit()

if Auth == "1":
    signup(Auth)
elif Auth == "2":
    Applogin(Auth)
else:
    exit()

def Pathq():
    global Path
    Path = input("Do you want to \n 1-Donate\n 2-Start a new fundraising\n 3-Setting")
Pathq()
while Path != "1" and Path != "2" and Path != "3":
    print("Write the number of your choice")
    Pathq()
# STEP 2 Fundraising
def new_case():
    if Path == "2":
        title = input("Your fundraising title:")
        details = input("Specify why you need this fundraising in details:")
        target = input("Your Target:")
        while not re.search(regex_target, target):
            target = input("Write your target in numbers:")
        def set_s_date():
            global s_date
            s_date = input("Start Date dd-mm-yyyy")
            try:
                datetime.datetime.strptime(s_date, "%d-%m-%Y")
            except ValueError:
                print("Write date in the shown format dd-mm-yyyy")
                set_s_date()

        set_s_date()


        def set_e_date():
            global e_date
            e_date = input("End Date dd-mm-yyyy")
            try:
                datetime.datetime.strptime(e_date, "%d-%m-%Y")
            except ValueError:
                print("Write date in the shown format dd-mm-yyyy")
                set_e_date()


        set_e_date()
        def Urgencyf():
            global Urgency
            Urgency = input("How Urgent this case is? scale from 1 to 3")
            while Urgency != "1" and Urgency != "2" and Urgency != "3":
                print("Please enter number from 1 to 3\n 1/not Urgent 2/ Urgent 3/very Urgent")
                Urgencyf()

        Urgencyf()
        filecom = [title, details,"I still need", target, s_date, e_date, PWRD]
        filecom1 = "\n".join(filecom)
        x = str(random.randint(1, 9999))
        save_path = str(dirpath)+"/Cases/"
        file_name = Urgency+str(title)+x
        print("Your case id is", file_name)

        completeName = os.path.join(save_path, file_name)

        with open(completeName, "w") as writecase:
              writecase.write(filecom1)

new_case()

# Step 3 Donating
def donate(Path):
    if Path == "1":
        find_case = input(" 1-Enter Case ID\n 2-List 'PeopleInNeed' Cases\n 3-Charity Organizations\n 4- Search by date")
        def findcase(find_case):
            searchresult = ""
            if find_case == "1":
                case_id = input("please enter the case ID")
                casepass = str(dirpath)+"/Cases/"+case_id
                with open(casepass, "r") as case_fileR:
                        print("\n".join(case_fileR.readlines()[1:6]))
                with open(casepass, "r") as case_fileR:
                     NM = case_fileR.readlines()[3]
                needed_money = int(NM)
                donate_money = int(input("please enter the amount of money you will donate to this case"))
                left_to_case = needed_money - donate_money
                leftstr = str(left_to_case)
                NMstr = str(needed_money)
                for line in fileinput.FileInput(casepass, inplace=1):
                    line = line.replace(NMstr, leftstr)
                    print(line, end="")
            elif find_case == "2":
                print("Cases are listed from the highest to least Urgent")
                print(sorted(os.listdir(str(dirpath)+"/Cases"), reverse=True))
                findcase("1")
            elif find_case == "3":
                print(os.listdir(str(dirpath)+"/organizations"))
                about = input("Enter Organization Name")
                Organpass = str(dirpath)+"/organizations/"+about
                with open (Organpass, "r") as readorgan:
                    print(readorgan.read())
            elif find_case == "4":
                search_date = input("Enter Start Date dd-mm-yyyy")+"\n"
                listoffilenames = []
                for x in os.listdir(str(dirpath)+"/Cases/"):
                    lpass = str(dirpath)+"/Cases/" + x
                    listoffilenames.append(lpass)
                for item in listoffilenames:
                        with open(item, "r") as searchfile:
                            h = searchfile.readlines()[4]
                            #print(repr(h))
                            #print(repr(search_date))
                            if search_date == h:
                                print("found match")
                                searchresult = item
                                print(os.path.basename(searchresult))
                if searchresult == "":
                        print("No match found")


            else:
                donate("1")
        findcase(find_case)

donate(Path)

def setting(Path):
    SettQ = ""
    if Path == "3":
        SettQ = input("SETTING\n 1- Edit\n 2- Delete\n 3-list your Cases")
        if  SettQ == "2":
            rm_case_id= input("Enter the id of the case you want to delete")
            #PWRD = input("Password:")
            rmd_case = str(dirpath)+"/Cases/"+rm_case_id
            with open(rmd_case, "r") as rmd_case_file:
                   if rmd_case_file.readlines()[6] == PWRD:
                       os.remove(rmd_case)
                       print("Your case has been Removed")
                   else:
                       print("Wrong Password!")

        elif SettQ == "1":
            def replace_line(file_name, line_num, text):
                lines = open(file_name, 'r').readlines()
                text = text + "\n"
                lines[line_num] = text
                out = open(file_name, 'w')
                out.writelines(lines)
                out.close()

            def set_e_date():
                global e_date
                e_date = input("End Date dd/mm/yyyy")
                try:
                    datetime.datetime.strptime(e_date, "%d-%m-%Y")
                except ValueError:
                    print("Write date in the shown format dd-mm-yyyy")
                    set_e_date()

            rm_case_id = input("Enter the id of the case you want to Edit")
            #PWRD = input("Password:")
            rmd_case = str(dirpath)+"/Cases/" + rm_case_id
            with open(rmd_case, "r") as rmd_case_file:
                if rmd_case_file.readlines()[6] == PWRD:
                    editcase = input("What do you want to Edit\n 1- Details \n 2- Donations needed\n 3- End Date")
                    if editcase == "1":
                        dtls_edit_var = input("Type your new details")
                        replace_line(rmd_case, 1, dtls_edit_var)
                    elif editcase == "2":
                        dtls_edit_var = input("Type your new donations needed")
                        replace_line(rmd_case, 3, dtls_edit_var)
                    elif editcase == "3":
                        set_e_date()
                        dtls_edit_var = e_date
                        replace_line(rmd_case, 5, dtls_edit_var)
                else:
                    print("Wrong Password")
        elif SettQ == "3":
            searchresult = ""
            #PWRD = input("Enter your Password:")
            listoffilenames = []
            for x in os.listdir(str(dirpath)+"/Cases"):
                lpass = str(dirpath)+"/Cases/"+x
                listoffilenames.append(lpass)
            for item in listoffilenames:
                    with open (item, "r") as searchfile:
                        h = searchfile.readlines()[6]
                        if h == PWRD:

                            searchresult = item
                            print(os.path.basename(searchresult))
            if searchresult == "":
                print("You have no cases")


        else:
             setting(3)

setting(Path)


backtomenu=input("1- Back to Main menu 2-Exit")
while backtomenu == "1":
    Pathq()
    if Path == "2":
            new_case()
    elif Path == "1":
            donate("1")
    elif Path == "3":
            setting("3")


print("Thank You for using our app\n Always remember that the happiest people are not those getting more, but those giving more.")