from django.shortcuts import render
import os
import openai
from django.conf import settings

from django.middleware.csrf import get_token
import pytesseract
from PIL import Image

openai.api_key = settings.OPENAI_API_KEY

def index(request):

    extracted_text = ""
    formatted_text = ""
    summary_text = ""
    formatted_summary_text = ""

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


    if request.method == "POST":
        image_file = request.FILES.get('thefile')
        extracted_text = extract_text_from_image(image_file)
        print(extracted_text)
        extracted_text = extracted_text.replace('\n', '\n ')
        print(extracted_text)

        ask = 'Summarize this for a second-grade student: \n\n' + extracted_text

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=ask,
            temperature=1,
            max_tokens=64,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

        summary_text = response.choices[0].text.strip()

    context = {
        'extracted_text': extracted_text.replace('\n', '<br>'),
        'formatted_text': format_text(extracted_text),
        'formatted_summary_text': format_text(summary_text),
    }

    return render(request, 'able/index.html', context)


def format_text(input_text):
    words = input_text.split(" ")
    print(words)
    processed_words = []
    for word in words:
        first_half  = word[:len(word)//2]
        second_half = word[len(word)//2:]
        processed_words.append("<strong>"+first_half+"</strong>"+second_half)
    print(processed_words)
    processed_words = [x.replace('\n', '<br>') for x in processed_words]
    print(processed_words)

    return " ".join(processed_words)


def extract_text_from_image(image_path):
    # Open the image file
    with Image.open(image_path) as image:
        # Perform OCR using Tesseract
        text = pytesseract.image_to_string(image)
    return text

