#!/usr/bin/python3.4
import sys, os
from time import sleep
def main():
    print("What do  you want to do?")
    print("1: Add")
    print("2: Change state")
    print("3: Show the lists")
    print("4: Quit")
    ques = input("...")
    if ques == "1":
        add()
    elif ques == "2":
        pick_done()
    elif ques == "3":
        show_lists()
    elif ques == "4":
        print("Quitting...")
        sleep(2)
        sys.exit()
    else:
        print("That is not a valid choice!")
        main()
def add():
    add_item = input("Please type what you want to add to the list: ")
    add_file = open('todo.txt', 'a')
    add_file.write(str(add_item) + '\n')
    add_file.close()
    input("Press any key to continue.")
    main()

def pick_done():

    f = open('todo.txt', 'r')
    linenum = 1
    for line in f:
        print(str(linenum) +  " " + line),
        linenum += 1

    f.close()

    choice = input("What item do you want to make 'done'? ")
    try:
        line_num = int(choice)
        if int(choice) > linenum:
            print("That is not a valid choice! ")
            input("Press any key to continue...")
            main()
        else:
            done(choice)
    except ValueError:
        print('That is not a number!')
        input()
        main()

def done(choice):
    f = open('todo.txt', 'r')
    linenum = 1
    for line in f:
        print(str(linenum) +  " " + line),
        linenum += 1

    f.close()

    num = open('todo.txt', 'r+')
    done_file = open('done.txt', 'a')
    lines = num.readlines()

    ch = lines[int(choice) - 1]

    done_file.write(ch)
        
        
    num.close()
    done_file.close()


    # add all items to a list

    rmd = open('todo.txt', 'r+')
    
    check = rmd.readlines()
    already_in = []
    for i in check:
        if i not in already_in and i != ch:
            already_in.append(i)
    rmd.close()
# Remove duuplicate items
    replace(already_in)

def replace(already_in):
    new_file = open('temp_todo.txt', 'a')
    for item in already_in:
        new_file.write(item)

    os.remove('todo.txt')
    os.rename("temp_todo.txt", "todo.txt")

    new_file.close()
    main()

def show_lists():
    
    done_file = open('done.txt', 'r')
    todo_file = open('todo.txt', 'r')

    a = todo_file.readlines()

    b = done_file.readlines()
    
    print("To-do: ")
    for i in a:
        print(i.rstrip('\n'))

    print()
    print("Done: ")
    for x in b:
        print(x.rstrip('\n'))
        
    print()


    main()

main()

