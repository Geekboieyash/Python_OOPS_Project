#ls will be the product list 
import pandas as pd
import numpy as np

food=pd.read_csv('food.csv')
book=pd.read_csv('books.csv')
furn=pd.read_csv('furn.csv')

def bill(product,price,quantity):
    amount=np.multiply(price,quantity)
    t_amount=np.sum(amount)
    df={'Product Name':product,'Price':price,'Quantity':quantity}
    x=pd.DataFrame(df)
    print("-------------------------------------------------Invoice-------------------------------------------------")
    print("--------------------------------------------------E-Shop-------------------------------------------------")
    print("-------------------------------------------Thankyou For shoping------------------------------------------")
    print("________________________________________________________________________________________________________ ")
    print("%60s %10s %10s %10s" %('Product Name', 'Price', 'Quantity', 'Amount'))
    for i in range(len(price)):
        print("%60s %10.2f %10d %10.2f " %(x.loc[i]['Product Name'],x.loc[i]['Price'],x.loc[i]['Quantity'],amount[i]))
    print("__________________________________________________________________________________________________________")
    print("Total                                                                                            ",t_amount)
    print("Your Product will be delivered within 3 days!!!!")
    print("-------------------------------------------Thankyou for shoping-------------------------------------------")
    print("-------------------------------------------Visit Again!!!!!!!!!-------------------------------------------")


def prod():
    a=1
    products=[]
    price=[]
    quantity=[]
    while(a):
        print("Enter category of product")
        ch = input("'F' for food, 'B' for books, 'T' for furniture & 'E' for exiting: ")
        if(ch=='F'):
            l=1
            while(l):
                print(food[['UID','Product Name','Price','Discount rates']])
                uid=int(input("Enter UID of products to buy: "))
                x=food.loc[food['UID']==uid]
                n=int(input("Enter quantity of this product you want: "))
                if(n<=x['Stock'].values[0]):
                    products.append(x['Product Name'].values[0])
                    price.append(x['Price'].values[0]) 
                    quantity.append(n)    
                    food.loc[food['UID']==uid,'Stock']=food.loc[food['UID']==uid,'Stock']-n
                else:
                    print("Sorry we don't have that much quantity!")
                    print("We are left with only this much quantity ",x['Stock'].values[0])
                    q=input("If you want to buy this much quantity, enter 'Y' for yes and 'N' for no: ")
                    if (q=='Y'):
                        products.append(x['Product Name'].values[0])
                        price.append(x['Price'].values[0]) 
                        quantity.append(x['Stock'].values[0])    
                        food.loc[food['UID']==uid,'Stock']=0
                print("Do you want any more food product?")
                l=int(input("Enter '1' for yes and '0' for no: "))
                food.to_csv('food.csv',index=False)

        elif(ch=='B'):
            print(book[['UID','Product Name','Price','Discount rates']])
            l=1
            while(l):
                print(book[['UID','Product Name','Price','Discount rates']])
                uid=int(input("Enter UID of products to buy: "))
                x=book.loc[book['UID']==uid]
                n=int(input("Enter quantity of this product you want: "))
                if(n<=x['Stock'].values[0]):
                    products.append(x['Product Name'].values[0])
                    price.append(x['Price'].values[0]) 
                    quantity.append(n)    
                    book.loc[food['UID']==uid,'Stock']-=n
                elif(n==0):
                    print('Sorry!! we are out of stock!!')
                else:
                    print("Sorry we don't have that much quantity!")
                    print("We are left with only this much quantity ",x['Stock'].values[0])
                    q=input("If you want to buy this much quantity, enter 'Y' for yes and 'N' for no: ")
                    if (q=='Y' and n!=0):
                        products.append(x['Product Name'].values[0])
                        price.append(x['Price'].values[0]) 
                        quantity.append(x['Stock'].values[0])    
                        book.loc[food['UID']==uid,'Stock']=0
                    
                print("Do you want any more book product?")
                l=int(input("Enter '1' for yes and '0' for no: "))
                book.to_csv('books.csv',index=False)

        elif(ch=='T'):
            print(furn[['Product Name','Price','Discount rates']])
            l=1
            while(l):
                print(furn[['UID','Product Name','Price','Discount rates']])
                uid=int(input("Enter UID of products to buy: "))
                x=furn.loc[furn['UID']==uid]
                n=int(input("Enter quantity of this product you want: "))
                if(n<=x['Stock'].values[0]):
                    products.append(x['Product Name'].values[0])
                    price.append(x['Price'].values[0]) 
                    quantity.append(n)    
                    furn.loc[furn['UID']==uid,'Stock']-=n
                elif(n==0):
                    print('Sorry!! we are out of stock!!')
                else:
                    print("Sorry we don't have that much quantity!")
                    print("We are left with only this much quantity ",x['Stock'].values[0])
                    q=input("If you want to buy this much quantity, enter 'Y' for yes and 'N' for no: ")
                    if (q=='Y'):
                        products.append(x['Product Name'].values[0])
                        price.append(x['Price'].values[0]) 
                        quantity.append(x['Stock'].values[0])    
                        furn.loc[furn['UID']==uid,'Stock']=0
                print("Do you want any more furn product?")
                l=int(input("Enter '1' for yes and '0' for no: "))
                furn.to_csv('furn.csv',index=False)     
        elif(ch=='E'):
            bill(products,price,quantity)
            return
        else:
            print("Enter a valid character!")

def adm():
    global food
    global book
    global furn
    print("What do you want to do?")
    wh=input('Enter "N" for adding new product and "O" for modifying old products details and "E" to return: ')
    a=1
    while(a):
        if (wh == 'N'):
            l=1
            while(l):
                print("In which category you want to add Product")
                ch=input("Enter 'F' for food,'B' for books & 'T' for furn: ")
                if (ch=='F'):
                    p=1
                    while(p):
                        uid=len(food.axes[0])+1
                        name=input("Enter Product Name: ")
                        pri=float(input("Enter Price: "))
                        o_pri=float(input("Enter Original Price: "))
                        dis=input("Enter discount rate: ")
                        st=int(input("Enter stock: "))
                        pro={'UID':[uid],'Product Name':[name],'Price':[pri],'Original Prices':[o_pri],'Discount rates':[(dis+'% off')],'Stock':[st]}
                        dg=pd.DataFrame(pro)
                        dg.to_csv("food.csv",mode='a',index=False,header=False)
                        print("Item added successfully!!!")
                        print("Do you want to add any more Food products?")
                        lp=1
                        while(lp):
                            try:
                                p=int(input("Enter '1' to add and '0' if not: "))
                            except ValueError:
                                print("Enter keys only in numbers")
                                lp=1
                            else:
                                lp-=1
                    print("Do you add products of any more category?")
                    lp=1
                    while(lp):
                        try:
                            l=int(input("Enter '1' for yes and '0' for no: "))
                        except ValueError:
                            print("Enter keys only in numbers")
                            lp=1
                        else:
                            lp-=1

                elif(ch=='B'):
                    p=1
                    while(p):
                        uid=len(book.axes[0])+1
                        name=input("Enter Product Name: ")
                        pri=float(input("Enter Price: "))
                        o_pri=float(input("Enter Original Price: "))
                        dis=input("Enter discount rate: ")
                        st=int(input("Enter stock: "))
                        pro={'UID':[uid],'Product Name':[name],'Price':[pri],'Original Prices':[o_pri],'Discount rates':[(dis+'% off')],'Stock':[st]}
                        dg=pd.DataFrame(pro)
                        dg.to_csv("books.csv",mode='a',index=False,header=False)
                        print("Item added successfully!!!")
                        print("Do you want to add any more Books?")
                        lp=1
                        while(lp):
                            try:
                                p=int(input("Enter '1' to add and '0' if not: "))
                            except ValueError:
                                print("Enter keys only in numbers")
                                lp=1
                            else:
                                lp-=1
                    print("Do you add products of any more category?")
                    lp=1
                    while(lp):
                        try:
                            l=int(input("Enter '1' for yes and '0' for no: "))
                        except ValueError:
                            print("Enter keys only in numbers")
                            lp=1
                        else:
                            lp-=1
                    
                    
                elif(ch=='T'):
                    p=1
                    while(p):
                        uid=len(furn.axes[0])+1
                        name=input("Enter Product Name: ")
                        pri=float(input("Enter Price: "))
                        o_pri=float(input("Enter Original Price: "))
                        dis=input("Enter discount rate: ")
                        st=int(input("Enter stock: "))
                        pro={'UID':[uid],'Product Name':[name],'Price':[pri],'Original Prices':[o_pri],'Discount rates':[(dis+'% off')],'Stock':[st]}
                        dg=pd.DataFrame(pro)
                        dg.to_csv("furn.csv",mode='a',index=False,header=False)
                        print("Item added successfully!!!")
                        print("Do you want to add any more Furniture products?")
                        lp=1
                        while(lp):
                            try:
                                p=int(input("Enter '1' to add and '0' if not: "))
                            except ValueError:
                                print("Enter keys only in numbers")
                                lp=1
                            else:
                                lp-=1   
                    print("Do you add products of any more category?")
                    lp=1
                    while(lp):
                        try:
                            l=int(input("Enter '1' for yes and '0' for no: "))
                        except ValueError:
                            print("Enter keys only in numbers")
                            lp=1
                        else:
                            lp-=1                 
                else:
                    l=1
                    print("Enter Correct Key!")
        
        elif(wh=='O'):
            l=1
            while(l):
                edit=input("Enter 'F' for food,'B' for books & 'T' for furn: ")
                if (edit=='F'):
                    l-=1
                    loop=1
                    while(loop):
                        print(food[['UID','Product Name','Price','Discount rates']])
                        uid=int(input("Enter UID of products to modify: "))
                        ch=input("Enter 'P' for changeing price,'D' for changind discount rate & 'S' for changing stock")
                        if(ch=='P'):
                            pri=float(input("Enter new Price: "))
                            food.loc[food['UID']==uid,'Price']=pri
                            food.to_csv('food.csv',index=False)
                            food = pd.read_csv('food.csv')
                            loop-=1
                        elif(ch=='D'):
                            dis=input("Enter discount rate: ")
                            food.loc[food['UID']==uid,'Discount rates']=dis
                            food.to_csv('food.csv',index=False)
                            food = pd.read_csv('food.csv')
                            loop-=1
                        elif(ch=='S'):
                            st=int(input("Enter new stock: "))
                            food.loc[food['UID']==uid,'Stock']=st
                            food.to_csv('food.csv',index=False)
                            food = pd.read_csv('food.csv')
                            loop-=1
                        else:
                            print('Enter correct key')
                            loop=1
                elif(edit=='B'):
                    l=l-1
                    loop=1
                    while(loop):
                        print(book[['UID','Product Name','Price','Discount rates']])
                        uid=int(input("Enter UID of products to modify: "))
                        ch=input("Enter 'P' for changeing price,'D' for changind discount rate & 'S' for changing stock")
                        if(ch=='P'):
                            pri=float(input("Enter new Price: "))
                            book.loc[book['UID']==uid,'Price']=pri
                            book.to_csv('books.csv',index=False)
                            book = pd.read_csv('books.csv')
                            loop-=1
                        elif(ch=='D'):
                            dis=input("Enter discount rate: ")
                            book.loc[book['UID']==uid,'Discount rates']=dis
                            book.to_csv('books.csv',index=False)
                            book = pd.read_csv('books.csv')
                            loop-=1
                        elif(ch=='S'):
                            st=int(input("Enter new stock: "))
                            book.loc[book['UID']==uid,'Stock']=st
                            book.to_csv('books.csv',index=False)
                            book = pd.read_csv('books.csv')
                            loop-=1
                        else:
                            print('Enter correct key')
                            loop=1
                elif(edit=='T'):
                    l-=1
                    loop=1
                    while(loop):
                        print(furn[['UID','Product Name','Price','Discount rates']])
                        uid=int(input("Enter UID of products to modify: "))
                        ch=input("Enter 'P' for changeing price,'D' for changind discount rate & 'S' for changing stock")
                        if(ch=='P'):
                            pri=float(input("Enter new Price: "))
                            furn.loc[furn['UID']==uid,'Price']=pri
                            furn.to_csv('furn.csv',index=False)
                            furn = pd.read_csv('furn.csv')
                            loop-=1
                        elif(ch=='D'):
                            dis=input("Enter discount rate: ")
                            furn.loc[furn['UID']==uid,'Discount rates']=dis
                            furn.to_csv('furn.csv',index=False)
                            furn = pd.read_csv('furn.csv')
                            loop-=1
                        elif(ch=='S'):
                            st=int(input("Enter new stock: "))
                            furn.loc[furn['UID']==uid,'Stock']=st
                            furn.to_csv('furn.csv',index=False)
                            furn = pd.read_csv('furn.csv')
                            loop-=1
                        else:
                            print('Enter correct key')
                            loop=1
                print("Modification done!!!")
        elif(wh=='E'):
            return
        else:
            print("Wrong key")
        wh=input('Enter "N" for adding new product and "O" for modifying old products details and "E" to return: ') 