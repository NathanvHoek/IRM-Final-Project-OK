import gzip
import json
import os
import csv


def main():
    header = ['name', 'screenname', 'text', 'category', 'gender', 'file', 'date']
    test_words = input('What words do you want to check? Split by space. (e.g. \'ok oke okay oké\')').split()
    file_name = input('What should the filename be? ')
    annotated_tweets_male = 0
    annotated_tweets_female = 0
    with open(f'{file_name}.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        file_count = 0
        for filename in os.listdir('dataset'):
            with gzip.open(f'dataset/{filename}', 'rt') as file:
                input_file = file.readlines()
                file_count += 1

                print(file_count, '-', filename)

                for i in input_file:
                    i = i.strip()
                    metadata = json.loads(i)

                    username = metadata['user']['name']
                    screen_name = metadata['user']['screen_name']
                    text = metadata['text']
                    description = metadata['user']['description']
                    date = metadata['created_at']

                    for test_word in test_words:
                        if f' {test_word.upper()} ' in text.upper() and text[:2] != 'RT':
                            print(f"Name:        {username}\n"
                                  f"Screenname:  {screen_name}\n"
                                  f"Description: {description}\n"
                                  f"Text:        {text}")

                            annotation = input('Male, female or not cannot be known? (f/m/n) ')

                            if annotation == 'f':
                                writer.writerow([username, screen_name, f'\"{text}\"', test_word, 'female', filename, date])
                                annotated_tweets_female += 1
                            elif annotation == 'm':
                                writer.writerow([username, screen_name, f'\"{text}\"', test_word, 'male', filename, date])
                                annotated_tweets_male += 1
                            else:
                                pass

                            print(f"\n female:{annotated_tweets_female}, male: {annotated_tweets_male}\n")


main()

