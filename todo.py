"""
3. To-Do List App
Concepts: list, file handling, functions

Features:

task add
task remove
completed mark
save/load from file

"""
def save_file():
    with open('saved.txt', 'w') as f:
        for i in completed_list:
            f.write(f'{i} [DONE]\n')
        for i in main_list:
            f.write(f'{i} []\n')

def update_list():
    y = input('1.Save\n2.Print only\n')
    if y == '1':
        save_file()
    else:
        print(f'{completed_list}\n{main_list}')

def load_list():
    with open('saved.txt', 'r') as f:
        for i in f:
            in_complete = '[]'
            complete = '[DONE]'
            if in_complete in i:
                i = i.replace(' []', '').replace('\n', '')
                main_list.append(i)
            if complete in i:
                i = i.replace(' [DONE]', '').replace('\n', '')
                completed_list.append(i)


main_list = []
completed_list = []
user_input = input('1.task add\n2.task remove\n3.Mark as completed\n4.Remove Completed Mark\n5.Check Completed & In Completed Task\nWhat do you want\n')

#add task to list
if user_input == '1':
    new_item = input('Task Name\n')
    load_list()
    main_list.append(new_item)
    update_list()

#remove task
if user_input == '2':
    remove_item = input('Task Name\n')
    load_list()
    if remove_item in main_list:
        main_list.remove(remove_item)
        update_list()
    else:
        update_list()

#Mark as completed
if user_input == '3':
    mark = input('Task Name\n')
    load_list()
    if mark in main_list:
        main_list.remove(mark)
        completed_list.append(mark)
        update_list()
    elif mark in completed_list:
        print('Already Marked')
    else:
        print('Not in To-Do List')

#Completed mark remove
if user_input == '4':
    unmark = input('Task Name\n')
    load_list()
    if unmark in completed_list:
        completed_list.remove(unmark)
        main_list.append(unmark)
        update_list()
    elif unmark in main_list:
        print('You didn\'t mark it')
    else:
        print('Not in To-Do List')

#Check Completed & In Completed Task
if user_input == '5':
    load_list()
    print(f'Completed List = {completed_list}\nIn Completed List = {main_list}')