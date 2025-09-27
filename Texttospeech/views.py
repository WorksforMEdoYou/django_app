from django.shortcuts import render
import pyttsx3
# Create your views here.
def Texttospeech(request):
    if request.method == 'POST':
        speaking = pyttsx3.init()
        speaking.setProperty('rate', 200)
        text = request.POST.get('content')
        speaking.say(text)
        speaking.runAndWait()
        return render(request, r'Textspeech/Textspeech.html')
    return render(request, r'Textspeech/Textspeech.html')
