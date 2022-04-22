import pandas as pd
import product

df = pd.read_csv('customer.csv') # reading customer dataset containing it all details like name, email, etc.


#customer class
class customer():
    def __init__(self):
        pass
     
    # login method 
    def login(self):
        ''' This method helps us to login and  after that we can shop, see profile, delete account'''
        self.username = input("Enter Username: ")
        if(self.username in df.Username.values): # USERNAME VALIDATION    
            self.password = input("Enter Password: ")
            if (df.loc[df['Username']==self.username,'Password'].values[0]==self.password): #PASSWORD VALIDATION
                print("Welcome to E-Shop!!!")
                print("What do you want to do?")
                print()
                # redirect to shopping list
                l=1
                while(l):
                    try:
                        wish = int(input("Enter '1' to shop,'2' to see profile,'3' to delete account and '0' to exit: "))
                        print()
                    except ValueError:
                        print("Enter keys only in number")
                        l=1
                    else:
                        l-=1

                while(wish):
                    if (wish == 1):
                        product.prod()
                    elif (wish == 2):
                        ob.profile() # to see profile
                    elif (wish == 3):
                        ob.delete_account() # to delete account
                    elif (wish == 0):
                        exit() # to logout
                    l=1
                    while(l):
                        try:
                            wish = int(input("Enter '1' to shop,'2' to see profile,'3' to delete account and '0' to exit: "))
                            print()
                        except ValueError:
                            print("Enter keys only in number")
                            l=1
                        else:
                            l-=1
            else:
                print("Wrong Password!!!")
        else:
            print('Wrong Username!!!')
    
    def signup(self):
        ''' This method create account for new user and then redirect to login'''
        self.fname = input("Enter First Name: ")
        self.lname = input("Enter Last name: ")
        self.username = input("Enter username: ")
        self.gender = input("Enter 'F' for female and 'M' for male and 'O' for others: ")
        l=1
        while(l):
            try:
                self.age = int(input("Enter age: "))
            except ValueError:
                print("Enter Age only in numbers")
                l=1
            else:
                l-=1
        l=1
        while(l):
            try:
                self.education = int(input("Enter Education level: "))
            except ValueError:
                print("Enter Level only in numbers")
                l=1
            else:
                l-=1                
        self.relationship = input("Enter Relationship Status: ")
        self.state = input("Enter your state: ")
        self.password = input("Create Password: ")
        l=1
        while(l):
            try:
                self.phone_no = (input("Enter 10-digit Phone Number: "))
            except ValueError:
                print("Enter Phone Number only in numbers")
                l=1
            else:
                if(len(self.phone_no)==10):
                    l-=1
                else:
                    print("Enter 10 digit Phone number")
                    l=l
        self.email = input('Enter email: ')
        loop=1 
        while(loop):
            global df
            user = {'Fname':[self.fname],'Lname':[self.lname],'Username':[self.username],'Gender':[self.gender],'Age':[self.age],'Education_Level':[self.education],'Relationship_Status':[self.relationship],'state':[self.state],'Password':[self.password],'Phone_NO':self.phone_no,'Email':self.email}
            dg=pd.DataFrame(user)
            if(user['Username'] not in df.Username.values):
                dg.to_csv("customer.csv",mode='a',index=False,header=False)
                loop-=1
                print("Your account created successfully!!")
                df=pd.read_csv('customer.csv')
                l=1
                while(l):
                    try:
                        n=int(input("Enter '1' if you want to login and '0' if you want to exit: "))
                    except ValueError:
                        print("Enter keys only in numbers")
                        l=1
                    else:
                        l-=1
                if (n):
                    ob.login()
                else:
                    exit()

            else:
                print("Username already taken! Take some other username")
                self.username = input("Enter username: ")
                loop=1

    def delete_account(self):
        '''This function helps us to delete ou account'''
        global df
        self.username = input("Enter Username: ")
        if(self.username in df.Username.values): # USERNAME VALIDATION    
            self.password = input("Enter Password: ")
            if (df.loc[df['Username']==self.username,'Password'].values[0]==self.password): #PASSWORD VALIDATION
                df.drop([(df.loc[df['Username']==self.username,'Username'].index[0])],axis=0,inplace=True)
                df.to_csv('customer.csv',index=False) # index=False helps not to replicate the index
                print("Your account is deleted successfully!!!")
                print("Feeling bad to see you go!!")
                df=pd.read_csv('customer.csv')
                l=1
                while(l):
                    try:
                        x=int(input("Enter '1' for exit and '0' for creating account again!!!"))
                    except ValueError:
                        print("Enter integer '1' or '0' only")
                        l=1
                    else:
                        l-=1
                if(x):
                    exit()
                else:
                    ob.signup()
            else:
                print('Wrong Password!!!')
        else:
            print('Wrong Username!!!')

    def profile(self):
        '''This function helps us to view our profile and editing option'''
        global df
        x=df.loc[df['Username']==self.username]
        print("################### Your Profile #####################")
        print('Name: ',x['Fname'].values[0]+' '+x['Lname'].values[0])
        print('Username: ',x['Username'].values[0])
        print('Gender: ',x['Gender'].values[0])
        print('Age: ',x['Age'].values[0])
        print('Education Level: ',x['Education_Level'].values[0])
        print('Relationship: ',x['Relationship_Status'].values[0])
        print('state: ',x['state'].values[0])
        print("Phone Number: ",x['Phone_NO'].values[0])
        print("Email: ",x['Email'].values[0])
        print('Do you want to edit something?')
        l=1
        while(l):
            edit=input('Enter "E" for editing profile, "P" for changing password and "R" if want to go to home page: ')
            loop=1
            if (edit == 'E'):
                l-=1
                while (loop):
                    ch=input("Enter 'U' to change username, 'R' to change Relationship, 'H' to change state, 'P' for phone number and 'E' to change Education level: ")
                    if(ch=='U'):
                        lp=1
                        user=input("Enter New Username: ")
                        while(lp):
                            if(user not in df.Username.values):
                                df.loc[df['Username']==self.username,'Username']=user
                                df.to_csv('customer.csv',index=False)
                                self.username=user
                                df=pd.read_csv('customer.csv')
                                lp-=1
                            else:
                                print("Username already taken! Take some other username")
                                user=input("Enter New username: ")
                                lp=1
                        loop-=1
                    elif (ch=='R'):
                        rel=input("Enter Relationship Status: ")
                        df.loc[df['Username']==self.username,'Relationship_Status']=rel
                        df.to_csv('customer.csv',index=False)
                        self.relationship=rel
                        df=pd.read_csv('customer.csv')
                        loop-=1
                    elif (ch=='H'):
                        hmt=input("Enter new state: ")
                        df.loc[df['Username']==self.username,'state']=hmt
                        df.to_csv('customer.csv',index=False)
                        self.state=hmt
                        df=pd.read_csv('customer.csv')
                        loop-=1
                    elif (ch=='P'):
                        l=1
                        while(l):
                            try:
                                phn=int(input('Enter new 10 digit Phone number: '))
                                df.loc[df['Username']==self.username,'Phone_NO']=phn
                            except ValueError:
                                print("Enter Phone number only in numbers")
                                l=1
                            else:
                                if(len(self.phone_no)==10):
                                    l-=1
                                else:
                                    print("Enter 10 digit Phone number")
                                    l=l
                        df.to_csv('customer.csv',index=False)
                        self.phone_no=phn
                        df=pd.read_csv('customer.csv')
                        loop-=1
                    elif (ch=='E'):
                        l=1
                        while(l):
                            try:
                                edu=int(input("Enter new Education Level: "))
                                df.loc[df['Username']==self.username,'Education_Level']=edu
                            except ValueError:
                                print("Enter Level only in numbers")
                                l=1
                            else:
                                l-=1  
                        df.to_csv('customer.csv',index=False)
                        df=pd.read_csv('customer.csv')
                        self.education=edu
                        loop-=1
                    else:
                        print("Enter correct key")
                        loop=1
            elif (edit == 'P'):
                pwd=input("Enter New Password")
                df.loc[df['Username']==self.username,'Password']=pwd
                df.to_csv('customer.csv',index=False)
                print('Your Password is changed successfully!!!')
                self.password=pwd
                df=pd.read_csv('customer.csv')
                l-=1
                ob.login()
            elif (edit == 'R'):
                return
            else:
                print("Enter correct key")
                l=1



#################################################################################################################################
# Main function
if __name__ == '__main__':
    a=1
    ob=customer()
    while(a):
        who = input("Enter 'A' for Administration, Enter 'C' for shop and 'E' for exit: ")
        if (who == 'C'): 
            old_new = input("Enter 'O' for existing customer and 'N' for New: ")
            if(old_new == 'O'):
                ob.login()
            elif(old_new == 'N'):
                ob.signup()
            else:
                print("Enter a valid characters:")
                a=1
        elif( who == 'A'):
            product.adm()
        elif (who == 'E'):
            exit()
        else:
            print("Does not recognize you? Re-enter")