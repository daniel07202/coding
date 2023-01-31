import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

date_string = "ko"


def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko')
        print('[다니엘]' + text)
        answer(text)
    except sr.UnknownValueError:
        print('죄송하지만 무슨 뜻인지 잘 모르겠어요')
    except sr.RequestError as e:
        print('요청 실패 : {0}'.format(e))

def answer(input_text):
    answer_text=''
    if '안녕' in input_text:
        answer_text = '안녕하세요 저도 반가워요'
    elif '날씨' in input_text:
        answer_text = '오늘의 서울 기온은 20도입니다. 맑은 하능이 예상되는 날씨에요'
    elif '환율' in input_text:
        answer_text = '현재 1000원을 달러로 환율하면 0.81 달러에요'
    elif '고마워' in input_text:
        answer_text = '별 말씀을요~'
    elif '종료' in input_text:
        answer_text = '다음에 또 만나요!'
        stop_listening(wait_for_stop=False)
    else:
        answer_text = '죄송한데 무슨 말씀이신지 잘 모르겠어요'
    speak(answer_text)

def speak(text):
    print('[인공지능]' + text)
    file_name = 'voice.mp3'
    tts = gTTS(text=text, lang='ko')
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name):
        os.remove(file_name)

r = sr.Recognizer()
m = sr.Microphone()

speak('무엇을 도와드릴까요?')
stop_listening = r.listen_in_background(m, listen)
#stop_listening(wait_for_stop=False)

while True:
    time.sleep(0.1) 