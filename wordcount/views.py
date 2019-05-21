from django.shortcuts import render
import operator  # operator 사용

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def count(request):
    full_text = request.GET['fulltext']  # fulltext로부터 데이터 얻어옴
    word_list = full_text.split()  # 단어를 나누기 위해.
    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            # Increase
            word_dictionary[word] += 1
        else:
            # add to the dictionary
            word_dictionary[word] = 1

    #max_wordtotal = highest = max(word_dictionary.items(), key=lambda x: x[1])

    max_wordtotal_first_1 = max(word_dictionary.items(), key=lambda x: x[1])[0]  # 최대값(item으로 결정하는데 ..), 목록x중 첫번째를 x[1], 0은 key

    sortedArr = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)  # 내림차순(key가 아닌 value로 sorting)

    return render(request, 'count.html', {'fulltext': full_text, 'total': len(word_list), 'dictionary': word_dictionary.items(),
                                          'sortedArr': sortedArr, 'max_wordtotal_first_1': max_wordtotal_first_1})


#a = lambda x , y : x * y
# print a(3,4)
