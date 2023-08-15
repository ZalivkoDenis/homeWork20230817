# ШАГ. Д/з по сроку 17/08/2023, часть 1
"""
Д/з по сроку 17/08/2023:
1. Дано предложение. Удалить все повторяющиеся слова.
"""


def clear_items_litter(in_list: list[str]) -> list[str]:
    """
    Обход списка и "очистка" от мусора: удаление знаков препинания и перевод строк в нижний регистр
    :param in_list: Список слов для очистки
    :return: Очищенный список
    """
    lst = list[str]()
    for word in in_list:
        lst.append(''.join([ch for ch in word if ch.isalpha()]).lower())
    return lst


def to_word_list(in_text: str) -> str:
    """
    Собственно функция обработки предложения с возвратом очищенного предложения в соответствии с условием задачи
    :param in_text: Входящий текст
    :return: "Очищенный" текст
    """
    res = list[str]()
    l_txt = clear_items_litter(in_text.split())
    counter = [l_txt.count(w) for w in l_txt]
    lst = in_text.split()
    for _ in range(len(lst)):
        if counter[_] == 1:
            res.append(lst[_])
        else:
            print(f'\t\t "{lst[_]}" deleted...')
    return ' '.join(res)


sentence = "Hello, world! It's a beautiful world. It is a beautiful and wonderful world!!!"
print(f'Original sentence:\n\t{sentence}')
clear_sentence = to_word_list(sentence)
print(f'Clear sentence:\n\t{clear_sentence}')

# Original sentence:
# 	Hello, world! It's a beautiful world. It is a beautiful and wonderful world!!!
# 		 "world!" deleted...
# 		 "a" deleted...
# 		 "beautiful" deleted...
# 		 "world." deleted...
# 		 "a" deleted...
# 		 "beautiful" deleted...
# 		 "world!!!" deleted...
# Clear sentence:
# 	Hello, It's It is and wonderful
