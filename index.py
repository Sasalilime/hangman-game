import random

words = "automatique contractuel langue ballon papa cage graine broyage courbe parachute charme"
words_list = words.split()

secret = random.randint(0, len(words_list)-1)
secret_word = words_list[secret]

game = {
    "secret_word": words_list,
    "guess_word": "_" * len(secret_word),
    "life": len(secret_word)+5
}

print(f"{game['guess_word']} | vie(s): {game['life']}")


while True:
    letter = input('Entrez une lettre :')
    if letter in game["secret_word"] and letter not in game["guess_word"]:
        guess_word_list = list(game["guess_word"])
        for index, current_letter in game['secret_word']:
            if current_letter == letter:

    elif letter not in game["secret_word"]:
        game["life"] -= 1
    print(f"{game['guess_word']} | vies : {game['life']}")
    if '_' not in game['guess_word']:
        print('Gagné !')
        break
    elif game['life'] < 1:
        print('Perdu !')
        break
