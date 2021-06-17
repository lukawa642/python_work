def xueshengbaomingxitong():
    form={
        "name":input("name:").strip(),
        # strip()就是把字符串首尾的多余字符给去掉
        "Age": input("Age:").strip(),
        "Phone": input("Phone:").strip(),
    }
    xueshengbaomingxitong_all=True
    for i,k in form.items():
        if len(k)==0:
            xueshengbaomingxitong_all=False
            break
    return form,xueshengbaomingxitong_all
student_xinxi,xueshengbaomingxitong_all=xueshengbaomingxitong()
print(student_xinxi)
print(xueshengbaomingxitong_all)
