import random


def read_file(path1):
    with open(path1, 'r') as f:
        txt = f.read()
    return txt


def phone_numbers():
    phone_number = ['+' + str(random.randint(79000000000, 80000000000)) for _ in
                    range(5)]
    numbers = random.choices(phone_number, k=random.randint(1, 2))
    return ' '.join(numbers)


def row_creation():
    row = [random.choice(name), random.choice(surname),
           random.choice(birthday), random.choice(work_place), phone_numbers()]
    return row


name = read_file('base_files//name.csv').split()
surname = read_file('base_files//surname.csv').split()
birthday = read_file('base_files//birthday.csv').split()
work_place = read_file('base_files//work_place.csv').split()
