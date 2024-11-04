import pickle
def patientrecord():
    passw=input('Enter password:')
    while passw=='Joshi Hospital':
        name=input("Enter the patient's name:")
        age=int(input("Enter the patient's age:"))
        num=int(input("Enter the patient's contact number:"))
        gender=input("Enter the patient's gender:")
        bg=input("Enter the patient's blood group:")
        dis=input("Enter the patient's disease:")
        content={'name':name,'age':age,'num':num,'gender':gender,'bg':bg,'dis':dis}
        f=open('test.dat','ab')
        pickle.dump(content,f)
        f.close()
        opt=input('Do you want to enter more records Y/N:')
        if opt.upper()!='Y':
            break
    else:
        print('Sorry, the password is incorrect.')

def readp():
    f=open('test.dat','rb')
    while True:
        try:
            record=pickle.load(f)
            print(record['name'],record['age'],record['num'],record['gender'],record['bg'],record['dis'])
        except EOFError:
            break
    f.close()

def searchp():
    f=open('test.dat','rb')
    test=False
    ser=input('Enter the patient name to be searched:')
    while True:
        try:
            record=pickle.load(f)
            if record['name']==ser:
                test=True
                print(record)
                break
        except EOFError:
            break
    if test==False:
        print('No record Found')
    f.close()

def updatedis(n,m):
    f=open('test.dat','rb')
    list1=[]
    while True:
        try:
            rec=pickle.load(f)
            list1.append(rec)
        except EOFError:
            break
    f.close()
    for i in range(len(list1)):
        if list1[i]['name']==n:
            list1[i]['dis']=m
    f=open('test.dat','wb')
    for x in list1:
        pickle.dump(x,f)
    f.close()

def deletep(r):
    f=open('test.dat','rb')
    list1=[]
    while True:
        try:
            rec=pickle.load(f)
            list1.append(rec)
        except EOFError:
            break
    f.close()
    test = False
    f=open('test.dat','wb')
    for x in list1:
        if x['name']==r:
            print(x['name'])
            test = True
            continue
    if test==False:
        print('No record Found')
        pickle.dump(x,f)
    f.close()
def message():
    print('*'*100)
    print('Type 1 to insert record')
    print('Type 2 to display record')
    print('Type 3 to search record')
    print('Type 4 to update record')
    print('Type 5 to delete record')
    print('Enter 0 to exit')
    print('*'*100)
while True:
    message()
    choice = int (input ("Enter your choice:"))
    if choice == 0:
        break
    elif choice == 1:
        patientrecord()
    elif choice == 2:
        readp ()
    elif choice == 3:
        searchp()
    elif choice == 4:
        n = (input("Enter name:"))
        m = (input ("Enter new diesease: "))
        updatedis(n,m)
    elif choice == 5:
        r = (input ("Enter name:"))
        deletep(r)