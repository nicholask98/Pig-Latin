def translate_to_english(pig_latin_sentence):
    translated_sentence = []
    sentence_to_translate = pig_latin_sentence.split()
    for word in sentence_to_translate:
        first_letter = word[-3]
        word = word[0:-3]
        word = first_letter + word
        translated_sentence.append(word)
    translated_sentence = ' '.join(translated_sentence)
    return translated_sentence

def translate_to_pig_latin(sentence_to_translate):
    translated_sentence = []
    for word in sentence_to_translate:
        first_letter = word[0]
        word = word[1:] + first_letter + 'ay'
        translated_sentence.append(word)
    translated_sentence = ' '.join(translated_sentence)
    translated_sentence = translated_sentence[0] + translated_sentence[1:]
    return translated_sentence

def main():
    sentence_to_translate = input('Enter a sentence to translate to Pig Latin and back:\n').lower().split()
    pig_latin_sentence = translate_to_pig_latin(sentence_to_translate)
    print(pig_latin_sentence)
    english_sentence = translate_to_english(pig_latin_sentence)
    print(english_sentence)

if __name__ == '__main__':
    main()