from django.shortcuts import render
import os
import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def index(request):

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
