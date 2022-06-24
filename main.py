import pickle


def main():
    create_one_file()
    create_two_file()

    file_one = open("one_sheet.data", "rb")
    file_two = open("two_sheet.data", "rb")

    one = pickle.load(file_one)
    two = pickle.load(file_two)

    unic_full = one & two
    one_unic = one - two
    two_unic = two - one
    full = one | two
    only_one_file = one ^ two

    print(f"Разницы: {one_unic}; {two_unic}")
    print(f"Все: {full}")
    print(f"В обоих: {unic_full}")
    print(f"Только в одном файле: {only_one_file}")

    file_one.close()
    file_two.close()




def create_one_file():
    my_file = open("one_sheet.data", "wb")

    one_data = set(["Pavel", "Ivan", "Stesha", "Alina", "Alisa"])

    pickle.dump(one_data, my_file)

    my_file.close()

def create_two_file():
    my_file = open("two_sheet.data", "wb")

    two = set(["Ereman", "Ivan", "Alex", "Valera", "Alisa"])

    pickle.dump(two, my_file)

    my_file.close()

main()