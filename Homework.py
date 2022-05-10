import random

users_name = input("Здравствуйте, пожалуйста введите ваше имя")


def shuffle_word(i):
    i_list = list(i)
    shuffled_word = ''.join(random.sample(i_list, len(i_list)))
    return shuffled_word


def get_word():
    score = 0
    with open('words.txt', 'r') as file:
        for i in file:
            i = i.rstrip('\n')
            print(f"слово: {shuffle_word(i)}")
            user_answer = input()
            if user_answer == i:
                print("Всё верно! Вы заработали 10 очков!")
                score += 10
                print("")
            else:
                print(f'Неверно, это слово {i}')
                print("")
    return score


def write_history():
    with open('history_of_games.txt', 'a', encoding="utf-8") as file:
        file.write(f"{users_name}:{total_score}\n")


def print_history():
    scores_list = []
    names_list = []
    lines_count = 0
    with open("history_of_games.txt") as file:
        for data in file:
            names, scores = data.strip().split(":")
            scores_list.append(scores)
            names_list.append(names)
            lines_count += 1
    return f"Всего было попыток: {lines_count}\nМаксимальный счёт: {max(scores_list)}"


print("вам будут предложены слова с изменённым порядком букв\nваша задача отгадать слово")
print('')
total_score = 0
total_score += get_word()
history = write_history()
print(f"Спасибо за игру, {users_name}\n{print_history()}")
