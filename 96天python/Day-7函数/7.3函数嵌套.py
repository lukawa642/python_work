def stu_form():
    form={
        "name":input("Name:").strip(),
        "age": input("Ags:").strip(),
        "job": input("Job:").strip(),
        "phone": input("Phone:").strip()
    }
    print(form)
    #下面的函数是为了修改form dict值的功能
    def change_form(form_date):
        print(form_date.keys())
        print(form_date.values())
        print("修改信息".center(20,"-"))
        while True:
            key=input("输入要修改的key:").strip()
            if not key:continue
            if key in form_date.keys():
                print(f"({key})的当前值为：{form_date[key]}")
                key_new_val=input("输入要改的新制值：").strip()
                form_date[key]=key_new_val
                break
            else:
                print("不合法的key..........")
    change_form(form)
    print("new form:",form)
    return form
stu_form()


