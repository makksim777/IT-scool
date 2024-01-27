# try:
#     file = open("test.txt","W")
#     try:
#          if file:
#              print("File is opened successfull")
#              file.close("Hello World to you")
#     finally:
#             file.close()
#             print("File Is closed" )
# except:
#      print("Someting went wrong while opening the file")
# list = ['1','1','2','3','4','5','6','7',]
# with open("test.txt", "a+") as file, open("text.txt", "w") as files2:
#     file.write("Hello World to you")
#     file.write("\nHello from Rivne")
#     file.writelines(list1)
#     print("File is closed")
#     file2.write("Hello World to all of us")
#     print("File2 is closed")

with open("test.txt", "r+") as file, open("text.txt", "w") as file2:
    stingNew = file.read().split(" ")
    for i in stingNew:
        if len(i) < 7:
            file.write(i)
with open("text.txt" , "r") as file2:
    print(file2.read())               
