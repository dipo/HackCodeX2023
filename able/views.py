from django.shortcuts import render
import os
import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def index(request):

    res = ""
    txt = ""

    ocr = """
        Acknowledgements:

        The results presented in this thesis originate from the kind cooperation of many people
        that shared their time, enthusiasm, knowledge, abilities and friendship. Everyone was so
        essential and unique, and every one was so kind and helpful. For all these reasons and
        more I kindly acknowledge you, with the hope that this thesis could be somehow useful
        for the environmentally friendly development of the rural producers in Nicaragua.

        In particular I would like to thank for their time, patience, and hospitality all the
        rural producers, the meaning and the objective of this study: I learnt so much from
        you. A big thanks go to Pierre Casal that suggested me to contact Johan Bastiaensen
        and ask for an internship in Nitlapan. A great acknowledgment to my supervisor Johan
        Bastiaensen that made all this possible and showed me the path for my first steps in
        the realm of rural development and he illuminated it with wise advises and discussions.
        I would like to thank René Mendoza first of all for his friendship, hospitality and the
        time spent discussing together that gave so much, moreover to trust in my investigation
        and give me the possibility to present my final results in Nitlapan. Frédéric Huybrechs
        for sharing his expertise, passion, advises and sources of information. Carlos Sosa that
        shared with me the time spent in the field, his vehicle and so many discussions. Omar
        Davila, Marcelo Rodriguez, Elias Ramirez, Fatima Fonseca, Manuel Bermudez for all
        the information they shared with me, for the time spent in discussions and for all the
        advises. Yuri Marin to allow me to present to Nitlapan in a seminar the topic and the
        objectives of my internship when I arrived in Nicaragua, and my preliminary results in
        the middle of my permanence in Nicaragua. Julio Flores for the knowledge he shared with
        me, the trust he gave me and the possibility to present the final result in the meeting of
        all the managers of FDL. Julio Barrio, Walter, Cesar Sampson, Inocente Cerda Madriz,
        Jairo Gonzales, Eva Garcia, Gilmer Gutiérrez, Arlin Jarquin, Alvaro for their kindness in
        sharing with me their very precious experience in the field and the nice moments spent
        together. Rene Gomez Flores, Oscar Manzanarez, Mercedes Martinez, Maria Engracia
        De Trinidad Prado, Claudia Ruiz, Francisco Perez for their help that allowed me to better
        understand the program. Silvia Martinez and Milagros Romero to have introduced me
    """

    ask = 'Summarize this for a second-grade student: \n\n' + ocr

    if request.method == "POST":
        print(request.POST)

    # response = openai.Completion.create(
    #     model="text-davinci-003",
    #     prompt=ask,
    #     temperature=1,
    #     max_tokens=64,
    #     top_p=1.0,
    #     frequency_penalty=0.0,
    #     presence_penalty=0.0
    # )

    # res = response.choices[0].text.strip()

    # words = res.split(" ")
    # print(words)
    # processed_words = []
    # for word in words:
    #     first_half  = word[:len(word)//2]
    #     second_half = word[len(word)//2:]
    #     processed_words.append("<strong>"+first_half+"</strong>"+second_half)
    # print(processed_words)

    # res = " ".join(processed_words)

    context = {
        'res': res,
        'txt': txt,
    }

    return render(request, 'able/index.html', context)

def index2(request):

    res = ""
    txt = ""

    if request.method == "POST":
        txt = request.POST['txt']

        ask = 'Please correct this text written by a person with dyslexia: "' + txt + '"'

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=ask,
            temperature=1,
            max_tokens=64,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

        res = response.choices[0].text


    context = {
        'res': res,
        'txt': txt,
    }

    return render(request, 'able/index.html', context)
