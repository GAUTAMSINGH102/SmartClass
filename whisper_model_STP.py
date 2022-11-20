import pickle
import whisper
import numpy as np


def speechToText(audioFile):
    model = pickle.load(open('.\SpeechToText\whisper_model.pkl', 'rb'))
    result = model.transcribe(audioFile)
    transcribeText = result['text']
    return transcribeText