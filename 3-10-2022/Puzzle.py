# def can_construct(message, magazine_letters):
#     flag = True
#     for letter in message:
#         for letter_mag in magazine_letters:
#             if letter == letter_mag:
#                 magazine_letters = magazine_letters.replace(letter_mag, '')
#                 print(magazine_letters)
#                 flag = True
#             # else:
#             #     flag = False
#             #     break
#     return flag

def can_construct(message, magazine_letters):
    message_letters = [message_letter for message_letter in message]
    magazine_letters = [magazine_letter for magazine_letter in magazine_letters]

    for message_letter in message_letters:
        if message_letter in magazine_letters:
            magazine_letters.remove(message_letter)
            flag = True
        else:
            flag = False
            break
    print(flag)


# def can_construct(message, magazine_letters):
#     di = {}
#     count = 0
#     for letter in message:
#         if letter in di:
#             count += 1
#             di[letter] = count
#         else:
#             di[letter] = 1
#
#         if count < di[letter]:
#             return True
#         else:
#             return False
#


can_construct('aab', 'abbcca')
can_construct('aabccc', 'abbcca')
