# Program: Mailroom Madness

# Datastructure that holds the list of donations and their history
donation_list = {'dad': [100.00, 200.00, 350.00], 'bil gates': [3000.00, 4000.00], 'suresh nadella' : [400.00, 3000.00]}

# Function definition is_name_found returns
# True if the entered name is alread in the list.


def is_name_found(list, name):
    for sub_list in list.keys():
        if sub_list == name:
            return True

# Function definition get_list_of_donars takes
# donation list as argument and retuns the donars list


def get_list_of_donars(list):
    list_of_names = []
    for sub_list in list.keys():
        list_of_names.append(sub_list)
    return list_of_names

# Function definition add_donar takes donation list and
# name of the new donar, adds and returns the donation list


def add_donar(list, name):
    list[name] = []
    return list

# Function add_amount takes donation list, name of the donar
# and amont he is donating. It includes the value and returns true.


def add_amount(list, name, amount):
    for (lname, list_amount) in list.items():
        if lname == name:
            list_amount.append(amount)
    return True

# Function print_report takes donation_list as an argument and returns the list
# of computed values as a string per donar.


def print_report(list):
    final_list = []
    str = 'Name'.ljust(20) + '|Total  |#  |Average'
    final_list.append(str)
    for (dname, amount_list) in list.items():
        sum = 0
        avg = 0
        cnt = 0
        name = dname
        for amt in amount_list:
            cnt = cnt + 1
            sum = sum + amt
        avg = sum / cnt
        str = ("%s|%r    |%r  |%r") % (name.ljust(20), sum, cnt, avg)
        final_list.append(str)
    return final_list

# This function returns true if the value is number or returns flase.


def thank_file(list):
    for (name, amount_list) in list.items():
        file_name = name + '.txt'
        outfile = open(file_name, 'w')
        for amount in amount_list:
            outfile.write('Hi {0}, Thanks for donating ${1} to our organization'.format(name, amount) + '\n')            
        outfile.close()


def is_number(value):
    length = len(value)
    cnt = 0
    for char in value:
        if char in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'):
            cnt = cnt + 1
    if length == cnt:
        return True
    else:
        return False


#  Main Function
if __name__ == '__main__':
    var_quit = True
    while var_quit is True:
        prompt = input('\nWelcome to mailroom madness!!! \n\nSelect the options below.\nT - Send a (T)hank You \nR - Create a (R)eport\nquit - Quit the program \n>')    
        if prompt.upper() == 'T':
            prompt_t = input('Please enter a name, or choose from the following:\nlist - Print a list of previous donors\nquit - Return to main menu  \n>')
            if prompt_t.lower() == 'list':
                print('List of the donars\n.................')
                for list in get_list_of_donars(donation_list):
                    print(list)
                input('\nPress enter to continue...')
            elif prompt_t.lower() == 'quit':
                var_quit = True
            else:
                if is_name_found(donation_list, prompt_t) is True:
                    amount = input('Please enter the amount:\n>')
                    flag = is_number(amount)
                    while flag is False:
                        amount = input('Please enter the valid number')
                        flag = is_number(amount)

                    prompt_amt = float(amount)
                    add_amount(donation_list, prompt_t, prompt_amt)
                    thank_file(donation_list)
                    print(("Thank you note added for file %s for $%r amount") %(:prompt_t, prompt_amt))
                    input('Press enter to continue....')
                else:
                    add_donar(donation_list, prompt_t)
                    amount = input('Please enter the amount:\n>')
                    flag = is_number(amount)
                    while flag is False:
                        amount = input('Please enter the valid number')
                        flag = is_number(amount)

                    prompt_amt = float(amount)
                    add_amount(donation_list, prompt_t, prompt_amt)
                    thank_file(donation_list)
                    print(("File has beed created for %s and thank you note added for $%r amount") %(prompt_t, prompt_amt))        
                    input('Press enter to continue...')
                    var_quit = True

        elif prompt.upper() == 'R':
            for list in print_report(donation_list):
                print(list)
            input('\nPress enter to continue...')
        elif prompt == 'quit':
            var_quit = False
