import json
filename = 'data.json'


def add():

    code = input("Enter the course code:")
    title = input("Enter the course title:")
    credit = input("Enter the Course credit:")
    precode = input("Enter the Prerequisites Course code, Enter 'null' if there is no prerequisites:")

    keyword = precode

    with open(filename, 'r') as file:
        info = json.load(file)

        flag = 0

        data = {}

        data["code"] = code
        data["title"] = title
        data["credit"] = credit
        data["pre_code"] = precode

        for row in info:
            code = row["code"]
            if keyword == code or keyword=="null":

                with open(filename, 'r') as file:
                    info = json.load(file)

                    info.append(data)


                with open(filename, 'w') as file:
                    json.dump(info, file, indent=2)

                file.close()

                print("Success! The course successfully added")
                flag = 1
                break
        if flag == 0:
            print(
                "\nSorry!The Prerequisites Course is not exists. Please add the course first.\n")


def update():
    keyword = input("\nEnter a course code for Update:")

    with open(filename, 'r') as file:
        info = json.load(file)

        flag = 0

        for idx, row in enumerate(info):
            code = row["code"]
            title = row["title"]
            credit = row["credit"]
            pre_code = row["pre_code"]

            if keyword == row["code"]:
                print("\nSelected Course Information below:\n")
                print("Course Code:"+code)
                print("Course Title:"+title)
                print("Course Credit:"+credit)
                print("Prerequisite Course Code:"+pre_code)
                print("\n")

                print("Enter the course information for update:\n")

                info[idx]['code'] = input("Enter Course Code:")
                info[idx]['title'] = input("Enter Course Title:")
                info[idx]['credit'] = input("Enter Course Credit:")
                info[idx]['pre_code'] = input(
                    "Enter Prerequisite Course Code:")

                with open(filename, 'w') as file:
                    json.dump(info, file, indent=2)

                file.close()
                flag = 1
                break
        if flag == 0:
            print("\nSorry!No match found. Please add the course.\n")


def delete():

    keyword = input("\nEnter the course code for delete:")

    with open(filename, 'r') as file:
        info = json.load(file)

        flag = 0

        for idx, row in enumerate(info):

            if keyword == row['code']:
                info.pop(idx)
                with open(filename, 'w') as file:
                    json.dump(info, file, indent=2)

                file.close()
                flag = 1
                break
        if flag == 0:
            print("\nSorry!No match found.\n")


def display():

    with open(filename, 'r') as file:
        info = json.load(file)

        for row in info:
            code = row["code"]
            title = row["title"]
            credit = row["credit"]
            pre_code = row["pre_code"]

            print("\nCourse Code:"+code)
            print("Course Title:"+title)
            print("Course Credit:"+credit)
            print("Prerequisite Course Code:"+pre_code)
            print("\n")
    file.close()


def search():
    keyword = input("\nEnter a course code for search:")

    with open(filename, 'r') as file:
        info = json.load(file)

        flag = 0

        for row in info:
            code = row["code"]
            title = row["title"]
            credit = row["credit"]
            pre_code = row["pre_code"]

            if keyword == code:
                print("\nCourse Code:"+code)
                print("Course Title:"+title)
                print("Course Credit:"+credit)
                print("Prerequisite Course Code:"+pre_code)
                print("\n")
                flag = 1
                break
        if flag == 0:
            print("\nSorry!No match found. Please add the course.\n")
    file.close()


while True:
    print("Welcome to course management application")

    print("Press 1 to add a new course")
    print("Press 2 to update an existing course")
    print("Press 3 to delete an existing course")
    print("Press 4 to display information about all the courses")
    print("Press 5 to search for a particular course and display all the information of a course")
    print("Press 6 to quit")

    button = input("Press Button:")

    if button == "1":
        add()

    elif button == "2":
        update()

    elif button == "3":
        delete()

    elif button == "4":
        display()

    elif button == "5":
        search()

    elif button == "6":
        break
    else:
        print("\nSorry!You have press the wrong button.")
