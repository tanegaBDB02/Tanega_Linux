def vowel_count():
    fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
    vowels="aeiou"

    fruits_with_only_two_vowels = [
        fruit for fruit in fruits
        if len([letter for letter in fruit if letter in vowels]) == 2
    ]

    print(fruits_with_only_two_vowels)

def main():
    vowel_count()

if __name__=="__main__":
    main()




