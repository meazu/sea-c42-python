# Program: Mailroom Madness

# Datastructure that holds the list of donations and their history
donation_list = [
    ['dad', [100, 200]],
    ['bil gates', [3000, 4000]],
    ['suresh nadella' [400, 3000]]]

# Function definition is_name_found returns
# True if the entered name is alread in the list.


def is_name_found(list, iname):
    for sub_list in list:
        for name in sub_list:
            if iname == name:
                return True

# Function definition get_list_of_donars takes
# donation list as argument and retuns the donars list


def get_list_of_donars(list):
    list_of_names = []
    for sub_list in list:
            list_of_names = list_of_names + (sub_list[0:1])
    return list_of_names

# Function definition add_donar takes donation list and
# name of the new donar, adds and returns the donation list


def add_donar(list, name):
    list.append([name, []])
    return list

# Function add_amount takes donation list, name of the donar
# and amont he is donating. It includes the value and returns true.


def add_amount(list, name, amount):
    for sub_list in list:
        if name == sub_list[0]:
            sub_list[1].append(amount)
            return True

# Function print_report takes donation_list as an argument and returns the list
# of computed values as a string per donar.


def print_report(list):
    final_list = []
    str = 'Name'.ljust(20) + '|Total  |#  |Average'
    final_list.append(str)
    for sub_list in list:
        sum = 0
        avg = 0
        cnt = 0
        name = sub_list[0]
        amount_str = sub_list[1]
        for amt in amount_str:
            cnt = cnt + 1
            sum = sum + amt
        avg = sum / cnt
        str = ("%s|%r    |%r  |%r") % (name.ljust(20), sum, cnt, avg)
        final_list.append(str)
    return final_list

# This function returns true if the value is number or returns flase.


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
        prompt = input(
            '\nWelcome to mailroom madness!!! \n\n'
            'Select the options below.\nT - '
            'Send a (T)hank You \nR - Create a (R)eport\n '
            'quit - Quit the program \n>')
        if prompt.upper() == 'T':
            prompt_t = input(
                'Please enter a name, or choose from the following'
                ':\nlist - Print a list of previous donors\nquit -'
                'Return to main menu  \n>')
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
                    print((
                        'Hi %s \nThank you so much for your kind donation '
                        'of $%r for Homeless people.\n'
                        'Thanks again,\n-Manasa\n\n') % (prompt_t, prompt_amt))
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
                    print((
                        'Hi %s \nThank you so much for your kind donation of'
                        '$%r for Homeless people.\nThanks again,\n-'
                        'Manasa\n') % (prompt_t, prompt_amt))
                    input('Press enter to continue...')
                    var_quit = True

        elif prompt.upper() == 'R':
            for list in print_report(donation_list):
                print(list)
            input('\nPress enter to continue...')
        elif prompt == 'quit':
            var_quit = False
