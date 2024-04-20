# file_path = "xdd.txt"
# file = open(file_path, "a+")
# text = input("Enter text: ").split()
#
# for i in range(len(text)):
#     if len(text[i]) >= 7:
#         file.write(f'{text[i]}\n')
#     else:
#         print("Your text is shorter than 7")
#
# file.close()

file_path = "x.txt"
file_second_path = "xdd.txt"
file = open(file_path, "w+")
file2 = open(file_second_path, "r")

data = file2.read()
file2.close()

file.write(data)

