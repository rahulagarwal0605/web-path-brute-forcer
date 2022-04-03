import validators
import os
import requests
import multiprocessing


def validate_url(url_list):
    validated_url_list = []
    for url in url_list:
        if validators.url(url) == True:
            validated_url_list.append(url)
        else:
            print(url + " is not a valid URL. Skipping it...")
    return validated_url_list


def get_url_list():
    url_list = input(
        "Enter list of URLs seperated by space (https://www.github.com): ")
    url_list = url_list.split(" ")
    validated_url_list = validate_url(url_list)
    return validated_url_list


def get_wordlist():
    wordlist_path = input("Enter Wordlist path (wordlist.txt): ")
    if os.path.isfile(wordlist_path):
        wordlist = []
        with open(wordlist_path) as f:
            wordlist = f.readlines()
            for i in range(len(wordlist)):
                wordlist[i] = wordlist[i].strip()
        return wordlist
    else:
        print(wordlist_path + " is not a valid file. Try Again...")
        return get_wordlist()


def validate_status_code(status_code_list):
    validated_status_code_list = []
    for status_code in status_code_list:
        try:
            status = int(status_code.strip())
            if status >= 100 and status < 600:
                validated_status_code_list.append(int(status_code))
            else:
                print(status_code + " is not a valid status code. Skipping it...")
        except:
            print(status_code + " is not a valid status code. Skipping it...")
    return validated_status_code_list


def get_status_codes():
    status_code_list = input(
        "Enter list of status codes ([200, 301, 302]): ")[1:-1]
    status_code_list = status_code_list.split(",")
    validated_status_code_list = validate_status_code(status_code_list)
    return validated_status_code_list


def get_status(url, word):
    url = url + '/' + word
    try:
        return (url, requests.head(url).status_code)
    except:
        return (url, None)


def get_output(url_list, wordlist):
    pool = multiprocessing.Pool()
    result_async = [
        pool.apply_async(get_status, args=(url, word, ))
        for url in url_list for word in wordlist
    ]
    results = [r.get() for r in result_async]
    return results


if __name__ == '__main__':
    url_list = get_url_list()
    wordlist = get_wordlist()
    status_codes = get_status_codes()
    print('\nGenerating results...')
    results = get_output(url_list, wordlist)
    for url, status_code in results:
        if status_code in status_codes or status_code == 200:
            print(url + ' [Status code ' + str(status_code) + ']')
