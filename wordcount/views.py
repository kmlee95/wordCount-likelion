from django.shortcuts import render

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

    return render(request, 'count.html', {'fulltext': full_text, 'total': len(word_list), 'dictionary': word_dictionary.items()})
