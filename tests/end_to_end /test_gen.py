import random

tests_number = 10
operations_number = 1000000

for test_number in range(0, tests_number):
    name_of_file = "test_" + f'{test_number + 1:02}' + ".in"
    file = open(name_of_file, 'w')
    test_text = ""
    for operation_number in range (0, operations_number):
        type_of_oper = random.randint(0, 1)
        if type_of_oper == 0:
            test_text += "k "
            test_text += str(random.randint(-100000, 100000)) + "\n"
        if type_of_oper == 1:
            test_text += "q "
            test_text += str(random.randint(-100000, 100000)) + " "
            test_text += str(random.randint(-10000000, 1000000)) + "\n"
        if operation_number % 100 == 0:
            file.write(test_text)
            test_text = ""
    file.write(test_text)
    file.close()
