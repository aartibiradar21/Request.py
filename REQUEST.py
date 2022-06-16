
# import requests
# import json
# link="https://api.merakilearn.org/courses"
# saral_url=requests.get(link)
# print(saral_url)
# data=saral_url.json()

# f=open("course_data.json","w")
# json.dump(data,f,indent=4)


# print(" ")
# print(" welcome to navgurukul and learn basic programming language")
# print(" ")

# serial_no=0
# for i in data:
#     print(serial_no+1 , i["name"],i["id"])
#     serial_no=serial_no+1

# course_no_1=int(input("enter your  course number do you want in id :- "))
# print(data[course_no_1-1]["name"])

# # link1="https://api.merakilearn.org/courses/"+str(data[course_no_1-1]["id"])+"/exercises"

# # get_data=requests.get(link1)
# # data=get_data.json()
# # file =open("coursesexercise.json","w")
# # json.dump(data,file,indent=4)
# # print(saral_url[course_no_1-1]["name"],'-',saral_url[course_no_1-1]["id"])
