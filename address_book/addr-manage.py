#通讯录
persons = []

#添加联系人
def create_person():
    name = input("请输入姓名：")
    address = input("请输入地址:")
    phone = input("请输入手机号：")

    if name and address and phone:
        person = {
                "name":name,
                "address":address,
                "phone":phone
        }
        persons.append(person)
    
#列出联系人
def list_person():
    for person in persons:
        print(person)


#查找联系人
def query_person():
    name = input("请输入要查找的联系人的名字：")
    for person in persons:
        if name == person["name"]:
            print(person)

#删除联系人
def delete_person():
    name = input("请输入要删除的联系人的名字：")
    for person in persons:
        if name == person[name]:
            persons.remove(person)

#主函数
def main():
    while True:
        #获取用户输入
        input_str=input("1.create person\n"
                        "2.list all persons\n"
                        "3.query person\n"
                        "4.delete person\n"
                        "5.quit\n"
                        "Enter a number(1-5):"
                        )
        if input_str == "1":
            create_person()
        elif input_str == "2":
            list_person()
        elif input_str == "3":
            query_person()
        elif input_str == "4":
            delete_person()    
        elif input_str == "5":
            break
        else:
            print("无效输入")


main()
