uname = 'Admin'
pwd = 'admin123'

while True:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if username != uname:
        print('Invalid username')
    if password != pwd:
        print('Invalid password')
    if username == uname and password == pwd:
        print('Login successful')
        break