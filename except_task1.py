#Перепишите функцию ask_user() из задания про while, чтобы она перехватывала KeyboardInterrupt, 
#писала пользователю "Пока!" и завершала работу при помощи оператора break

ask_answer_dict = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую"} 

def ask_user(ask_answer_dict):
    while True:
        try:
            answer = input('Задайте вопрос:\n')
            print(ask_answer_dict.get(answer, 'Не понимаю'))
        except KeyboardInterrupt:
            print('Пока!')
            break

ask_user(ask_answer_dict)


