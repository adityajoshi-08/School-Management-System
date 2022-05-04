# Structure of Table just in case there is a need to create in other system
# +--------------+--------------+------+-----+---------+-------+
# | Field        | Type         | Null | Key | Default | Extra |
# +--------------+--------------+------+-----+---------+-------+
# | Name         | varchar(50)  | YES  |     | NULL    |       |
# | Class        | varchar(20)  | YES  |     | NULL    |       |
# | Section      | varchar(10)  | YES  |     | NULL    |       |
# | Scholar_No   | int          | YES  |     | NULL    |       |
# | Fees_Paid    | int          | YES  |     | NULL    |       |
# | Fees_Due     | int          | YES  |     | NULL    |       |
# | Caution_Fee  | int          | YES  |     | NULL    |       |
# | Items_Broken | varchar(100) | YES  |     | NULL    |       |
# +--------------+--------------+------+-----+---------+-------+
# MySQL query to create table -->
#  create table school(Name VARCHAR(50),
#  Class VARCHAR(20), Section VARCHAR(10), Scholar_No INT, Fees_Paid INT,
#  Fees_Due INT, Caution_Fee INT, Items_Broken
#  VARCHAR(100));

# To start mysql in Linux -->
# source .bash_profile
# mysql -u root -p

import mysql.connector

mydb1 = mysql.connector.connect(host="localhost", user="root",
                                passwd="Home@253144", database="school")
mycursor = mydb1.cursor()
list_sno = []
list_sno_int = []
final_choice = 1

print('\t*************\n'
      '\t* Main Menu *\n'
      '\t*************')
while final_choice == 1:
    print("1. Insert a new record")
    print("2. Update some records")
    print("3. Delete some records")
    print("4. View full table")

    choice = input("Enter your choice:\n")
    while True:
        if choice.isdigit():
            choice = int(choice)
            break
        else:
            print('Wrong input! Enter only the number')
            print('Do you want to use the service again?')
            choice = input("Enter your choice:\n")
    while True:
        if choice > 4:
            print('Wrong input! Please enter a valid choice!')
            print("1. Insert a new record")
            print("2. Update some records")
            print("3. Delete some records")
            print("4. View full table")
            choice = int(input("Enter your choice:\n"))
            while True:
                if choice.isdigit():
                    choice = int(choice)
                    break
                else:
                    print('Wrong input! Enter only the number')
                    print('Do you want to use the service again?')
                    choice = input("Enter your choice:\n")
        else:
            break

    if choice == 1:
        seetable = int(input('Do you want to see full table \n'
                             '1. Yes \n'
                             '2. No : \n'))
        if seetable == 1:
            mycursor.execute("select * from school")
            for i in mycursor:
                print(i)
        else:
            pass
        no_of_names = int(input('How many records do you want'
                                ' to Enter? :'))
        for i in range(no_of_names):
            if no_of_names == 1:
                print('Enter the details of student')
            else:
                print('Enter the details of student', i + 1)

            name = input('Enter the Name: \n')
            standard = input('Enter the class: \n')
            section = input('Enter the Section: \n')

            while True:
                scholar_no = int(input('Enter the Scholar Number: \n'))

                mycursor.execute("SELECT Scholar_No from school")
                for i in mycursor:
                    list_sno.append(i)
                for j in range(len(list_sno)):
                    a_string = str(list_sno[j])
                    numbers = []
                    for i in range(len(a_string)):

                        if a_string[i].isdigit():
                            numbers.append(a_string[i])

                    result = int("".join([str(i) for i in numbers]))

                    list_sno_int.append(result)
                if scholar_no in list_sno_int:
                    print('Wrong scholar number input. Please'
                          ' enter again!')
                else:
                    break

            fees_paid = int(input('Enter the fees paid: \n'))
            fees_due = 100000 - fees_paid
            print('Fees due is taken as ', fees_due)
            while True:
                caution_query = int(input('Is there any caution fee to be'
                                    ' deducted? \n1. Yes \n2. No:\n'))
                if caution_query == 1:
                    caution_fee = int(input('Enter the caution fee to be'
                                            ' deducted: \n'))
                    items_broken = input('Enter the items broken'
                                         ' by student: \n')
                    break

                elif caution_query == 2:
                    caution_fee = 0
                    items_broken = 'NULL'
                    break

            mycursor.execute("INSERT INTO school  VALUES(%s, %s, %s,"
                             " %s, %s, %s,%s,%s)",
                             (name, standard, section, scholar_no, fees_paid,
                              fees_due, caution_fee, items_broken))
            mydb1.commit()
            print('Record added successfully!!')
            print(" _______________________________________________"
                  "__________________")
        seetable = int(input('Do you want to see full table \n'
                             '1. Yes \n'
                             '2. No : \n'))
        if seetable == 1:
            mycursor.execute("select * from school")
            for i in mycursor:
                print(i)
        else:
            pass
    if choice == 2:
        update_again = 1
        while update_again == 1:
            print("You can update on the basis of Scholar Number!!!")
            seetable = int(input('Do you want to see full table \n'
                                 '1. Yes \n'
                                 '2. No : \n'))
            if seetable == 1:
                mycursor.execute("select * from school")
                for i in mycursor:
                    print(i)
            else:
                pass
            while True:
                update_query = int(input('What do you want to update? \n'
                                         '1. Name \n'
                                         '2. Standard \n'
                                         '3. Section \n'
                                         '4. Scholar Number \n'
                                         '5. Fees Paid \n'
                                         '6. Fees Due : \n'
                                         '7. Caution Fee Deduction : \n'
                                         '8. Items broken : \n'))
                if update_query > 8:
                    print('Please enter a valid option!')
                else:
                    break
            if update_query != 4:
                while True:
                    scholar_no = int(input('Enter the Scholar Number: \n'))

                    mycursor.execute("SELECT Scholar_No from school")
                    for i in mycursor:
                        list_sno.append(i)
                    for j in range(len(list_sno)):
                        a_string = str(list_sno[j])
                        numbers = []
                        for i in range(len(a_string)):

                            if a_string[i].isdigit():
                                numbers.append(a_string[i])

                        result = int("".join([str(i) for i in numbers]))

                        list_sno_int.append(result)
                    if scholar_no not in list_sno_int:
                        print('Scholar number does not exist'
                              ' Please enter a valid number!')
                    else:
                        break

            if update_query == 1:
                new_name = input('Enter new Name :\n')
                mycursor.execute(" UPDATE school SET Name = %s where"
                                 " Scholar_No = %s", (new_name, scholar_no))
                mydb1.commit()
                print('Record updated successfully')
                seetable = int(input('Do you want to see full table \n'
                                     '1. Yes \n'
                                     '2. No : \n'))
                if seetable == 1:
                    mycursor.execute("select * from school")
                    for i in mycursor:
                        print(i)
                else:
                    pass

            if update_query == 2:
                new_class = input("Enter the new Standard :\n")
                mycursor.execute("Update school set Class = %s"
                                 " where Scholar_no = %s", (new_class, scholar_no))

                mydb1.commit()
                print('Record updated successfully')
                seetable = int(input('Do you want to see full table \n'
                                     '1. Yes \n'
                                     '2. No : \n'))
                if seetable == 1:
                    mycursor.execute("select * from school")
                    for i in mycursor:
                        print(i)
                else:
                    pass

            if update_query == 3:
                new_section = input("Enter the new Section :\n")
                mycursor.execute("Update school set Section = %s"
                                 " where Scholar_no = %s", (new_section, scholar_no))
                mydb1.commit()
                print('Record updated successfully')
                seetable = int(input('Do you want to see full table \n'
                                     '1. Yes \n'
                                     '2. No : \n'))
                if seetable == 1:
                    mycursor.execute("select * from school")
                    for i in mycursor:
                        print(i)
                else:
                    pass

            if update_query == 4:
                scholar_no = int(input('Enter the Old Scholar Number'
                                       ' of desired student:\n'))
                scholar_no_new = int(input('Enter the new Scholar'
                                           ' number of the desired student:\n'))
                mycursor.execute("Update school set Scholar_No = %s"
                                 " where Scholar_no = %s", (scholar_no_new,
                                                            scholar_no))
                mydb1.commit()
                print('Record updated successfully')

                seetable = int(input('Do you want to see full table\n'
                                     '1. Yes \n'
                                     '2. No : \n'))
                if seetable == 1:
                    mycursor.execute("select * from school")
                    for i in mycursor:
                        print(i)
                else:
                    pass

            if update_query == 5:
                fees_paid = int(input('Enter the total fees paid :\n'))
                fees_due = 100000 - fees_paid
                print('Fees due is taken as :', fees_due)
                mycursor.execute("Update school set Fees_Paid = %s where"
                                 " Scholar_no = %s", (fees_paid,
                                                      scholar_no))
                mycursor.execute("update school set Fees_Due = %s where"
                                 " Scholar_No = %s", (fees_due,
                                                      scholar_no))
                mydb1.commit()
                print('Record updated successfully')

                seetable = int(input('Do you want to see full table \n'
                                     '1. Yes \n'
                                     '2. No : \n'))
                if seetable == 1:
                    mycursor.execute("select * from school")
                    for i in mycursor:
                        print(i)
                else:
                    pass

            if update_query == 6:
                fees_due = int(input('Enter the total fees due : \n'))
                fees_paid = 100000 - fees_due
                print('Fees paid is taken as :', fees_paid)
                mycursor.execute("Update school set Fees_Paid = %s"
                                 " where Scholar_no = %s", (fees_paid,
                                                            scholar_no))
                mycursor.execute("update school set Fees_Due = %s"
                                 " where Scholar_No = %s", (fees_due,
                                                            scholar_no))
                mydb1.commit()
                print('Record updated successfully')

                seetable = int(input('Do you want to see full table \n'
                                     '1. Yes \n'
                                     '2. No : \n'))
                if seetable == 1:
                    mycursor.execute("select * from school")
                    for i in mycursor:
                        print(i)
                else:
                    pass

            if update_query == 7:
                caution_fee = int(input('Enter the total caution'
                                        ' fee to be deducted : \n'))
                mycursor.execute("Update school set Caution_Fee = %s"
                                 " where Scholar_no = %s", (caution_fee,
                                                            scholar_no))
                mydb1.commit()
                print('Record updated successfully')

                seetable = int(input('Do you want to see full table \n'
                                     '1. Yes \n'
                                     '2. No : \n'))
                if seetable == 1:
                    mycursor.execute("select * from school")
                    for i in mycursor:
                        print(i)
                else:
                    pass

            if update_query == 8:
                items_broken = input('Enter the items broken by the'
                                     ' student : \n')
                mycursor.execute("Update school set Items_Broken = %s"
                                 " where Scholar_no = %s", (items_broken,
                                                            scholar_no))
                mydb1.commit()
                print('Record updated successfully')
                fees_query = int(input('Do you want to change caution'
                                       ' fees deducted? \n'
                                       '1. Yes \n'
                                       '2. No:'))
                if fees_query == 1:
                    caution_fee = int(input('Enter the total caution fee'
                                            ' to be deducted:\n'))
                    mycursor.execute("Update school set "
                                     "Caution_Fee = %s where Scholar_no = %s",
                                     (caution_fee, scholar_no))
                seetable = int(input('Do you want to see full table \n'
                                     '1. Yes \n'
                                     '2. No : \n'))
                if seetable == 1:
                    mycursor.execute("select * from school")
                    for i in mycursor:
                        print(i)
                else:
                    pass

            update_again = int(input('Do you want to update any'
                                     ' other record? \n'
                                     '1. Yes \n'
                                     '2. No : \n'))

    if choice == 3:
        delete_no = int(input('How many records do you want to '
                              'delete?:\n'))
        seetable = int(input('Do you want to see the table? \n'
                             '1. Yes \n'
                             '2. No : \n'))
        for i in range(delete_no):

            if seetable == 1:
                mycursor.execute("select * from school")
            for i in mycursor:
                print(i)
            else:
                pass

            while True:
                scholar_no = int(input('Enter the Scholar Number: \n'))

                mycursor.execute("SELECT Scholar_No from school")
                for i in mycursor:
                    list_sno.append(i)
                for j in range(len(list_sno)):
                    a_string = str(list_sno[j])
                    numbers = []
                    for i in range(len(a_string)):

                        if a_string[i].isdigit():
                            numbers.append(a_string[i])

                    result = int("".join([str(i) for i in numbers]))

                    list_sno_int.append(result)
                if scholar_no not in list_sno_int:
                    print('Scholar number does not exist'
                          ' Please enter a valid number!')
                else:
                    break
            mycursor.execute("select Name from school where"
                             " Scholar_No = %s", (scholar_no,))
            for i in mycursor:
                s = str(i)
                s1 = s.replace(",", "")
                name = str(s1)
            print('Record of', name, 'Scholar No:', scholar_no,
                  'removed successfully')

            mycursor.execute("delete from school WHERE Scholar_No = %s",
                             (scholar_no,))

            mydb1.commit()
            seetable = int(input('Do you want to see full table \n'
                                 '1. Yes \n'
                                 '2. No : \n'))
            if seetable == 1:
                mycursor.execute("select * from school")
                for i in mycursor:
                    print(i)
            else:
                pass

    if choice == 4:
        mycursor.execute("select * from school")
        for i in mycursor:
            print(i)
    print('Do you want to use the service again?')
    final_choice = input('1.Yes\n2.No:\n')
    while True:
        if final_choice.isdigit():
            final_choice = int(final_choice)
            break
        else:
            print('Wrong input! Enter only the number')
            print('Do you want to use the service again?')
            final_choice = input('1.Yes\n2.No:\n')


print('Thank you for using the service.')
print("Have a Good Day :)")
