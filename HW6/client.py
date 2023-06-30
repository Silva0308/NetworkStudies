# Импорт модуля socket для работы с сетевыми соединениями
import socket
# Импорт модуля threading для многопоточной работы программы
import threading

# Запрос никнейма пользователя
nickname = input("Choose your nickname: ")

# Создание объекта сокета для клиента и установление соединения с сервером по адресу и порту
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('158.160.12.125', 55555)) # тут важно, что IP внешний

# Функция для прослушивания сообщений от сервера и отправки никнейма клиента
def receive():
    while True:
        try:
            # получение сообщения с сервера
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break

# Функция для отправки сообщений от клиента
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))

#  Создание двух потоков для прослушивания сообщений от сервера и отправки сообщений на сервер
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
