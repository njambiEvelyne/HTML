# try:
#     #value = 10/0
#     number = int(input("Enter a number: "))
#     print(number)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError as e:
#     print(e)

#Reading from external files
employee_file = open("employees.txt", "r")
print(employee_file.readlines())
employee_file.close()
 
 