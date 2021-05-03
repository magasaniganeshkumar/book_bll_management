import math
from  datetime import datetime
print("\tWelcome To Ganesh Book Store ")
name = input("Enter Customer name : ")
phone_number = int(input("enter Customer phone number : "))
def bill():
    loop = True
    Total_price = 0
    list_iteams_price = []
    while loop:
        print('''
                1.list of Books 
                2.Order Books
                3. exit for bill
                ''')
        cholice = int(input(" enter your choice : "))
        cholices = [1,2,3]
        if cholice in cholices:
            d = {'python':200,'html5':100,'css3':100,'java':300,'javascript':150,'django':300,'datascience':400,'machinelearning':300,}
            if cholice == 1:
                Book_number = 1
                for key,value in d.items():
                    print('\t',Book_number,'.',key,'₹',value)
                    Book_number+=1
            if cholice == 2:
                quite = True
                while quite:
                    print("press 'q' to to see main menu.")
                    book = input('enter book name:')
                    if book in d.keys():
                        book_quan = input('enter book Quantity number you want:')
                        if book_quan.isdigit():

                            book_quan = int(book_quan)
                            price = float(d[book] * book_quan)
                            list_iteams_price.append((book, book_quan, price))
                            Total_price += price
                        else:
                            print('Invalid input quantity plese enter number of books you need to buy...')
                    elif book == 'q':
                        quite = False

                    else:
                        print(book,'book is not avalable in Ganesh_book_store.')
            if cholice == 3:
                loop = False
        else:
            print(name , " your enter invalid input ... please enter valid input ..")
    return Total_price,'thank you please visit again',list_iteams_price

total,msg,price=bill()
print('\t',name, "You are Books Order bill is  ....")
if total != 0:
    print('\n')
    print('''
                Ganesh Book Stores
            JANGAMVARIPALLE,CHITTOOR,517280
                 PHONE:6302984048
    ''')
    print('Customer Name:', name,'\t','Phone:',phone_number ,'\t', 'Date:', datetime.now())
    print(39 * '==')

    for item in price:
        print('Book_Name:', item[0], '\tQuntity:', item[1], ' Price:', item[2])

    discount = total * 0.05
    discount = math.ceil(discount)
    print(26 * '==')
    print('Save_Amount: Rs.', float(discount))
    gst = total * 0.1
    gst = math.ceil(gst)
    print('GST: Rs.', float(gst))
    print('Total payble amount: Rs.', float(total-discount+gst))
    print(18* '==')
    print('🙏🙏🙏 ', msg, ' 🙏🙏🙏')

else:
    print("hey,",name," you waren't brought anything.....Please Buy something you")
    bill()
