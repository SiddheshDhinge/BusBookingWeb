import random

own = ['Chintan', 'Siddhesh', 'Manas', 'Sahil', 'Shubham', 'jack123', 'emmam', 'brianb', 'katherineg', 'chrisd', 'samuelm', 'laurar', 'davids', 'jennifert', 'michaelw', 'susanb', 'jamesm', 'lisaq', 'matthewr', 'nicolej']
oper = ['Manish', 'Guarav', 'Ketan', 'Akshay', 'Lokesh', 'timothyb', 'rachelc', 'michaelg', 'jenniferl', 'davidm', 'sarahp', 'matthewr', 'lisaq', 'katherinet', 'johnd']
number = ['MH 12 AB 1234', 'MH 13 AB 1235', 'MH 14 AB 1236', 'MH 15 AB 1237', 'MH 18 AB 1238', 'MH 20 AB 1239', 'MH 16 AB 1240', 'MH 17 AB 1241', 'MH 10 AB 1242', 'MH 12 AB 1243', 'MH 19 AB 5211', 'MH 11 AB 6292', 'MH 17 AB 5074', 'MH 15 AB 5005', 'MH 12 AB 6645', 'MH 7 AB 7697', 'MH 6 AB 7826', 'MH 7 AB 5772', 'MH 11 AB 5572', 'MH 5 AB 5165', 'MH 18 AB 8838', 'MH 20 AB 8011', 'MH 5 AB 6923', 'MH 20 AB 8273', 'MH 9 AB 9063', 'MH 7 AB 7471', 'MH 14 AB 9620', 'MH 6 AB 6360', 'MH 7 AB 7453', 'MH 7 AB 6836', 'MH 20 AB 6562', 'MH 6 AB 6058', 'MH 14 AB 8810', 'MH 7 AB 8906', 'MH 16 AB 9804', 'MH 16 AB 9511', 'MH 11 AB 9845', 'MH 20 AB 7639', 'MH 20 AB 5514', 'MH 11 AB 7412']
typ = ['SLEEP', 'SEAT']

def pad(num):
    if(num < 10):
        return f'0{num}'
    return num
    
def randomPad(a, b):
    return pad(random.randint(a, b))

for _ in range(1, 75):
    # Bus
    # data = (f'MH {random.randint(5, 20)} AB {random.randint(5000, 9999)}' , random.randint(30, 50), pos[random.randint(0, 1)], own[random.randint(0, len(own) -1)])

    # Schedule
    frmM = random.randint(1, 11)
    frmD = random.randint(1, 29)
    toD = frmD+ 1
    data = (
        f'2022-{pad(frmM)}-{pad(frmD)}',
        f'2022-{pad(frmM)}-{pad(toD)}',
        f'{randomPad(0, 23)}:{randomPad(0, 59)}:{randomPad(0, 59)}', 
        f'{randomPad(0, 23)}:{randomPad(0, 59)}:{randomPad(0, 59)}', 
        random.randint(1000, 10000), 
        random.randint(1, 3),
        random.randint(1, 3),
        f'{number[random.randint(0, len(number) -1)]}',
        oper[random.randint(0, len(oper) -1)]
    )

    # At
    # for __ in random.sample(range(1, 30), 10):
    #     print(f'{_}, {__}')

    # Booking
    # for seat in range(1, random.randint(1, 30)):
    #     data = (seat, _, random.randint(1, 35))

    print(data)



# Schedule(fromDate: str, toDate: str, departureTime: str, dropTime: str, fairFees: int, fromCity: int, toCity: int, numberPlate: str, username: str)
# assert Schedule('2019-12-01', '2019-12-31', '08:00:00', '11:00:00', 5000, 1, 6, 'MH 12 AB 1234', 'Manish').createObject() == True