import pickle
from multi_rake import Rake

def keywordsUsingRake(transcribeText):
    rake_model = pickle.load(open(r'.\keywords\rake_model.pkl', 'rb'))
    stemmer = pickle.load(open(r'.\preprocessing\snowballStemmer.pkl', 'rb'))

    keywords = rake_model.apply(transcribeText)

    listKeywords = []
    cleanKeywords = []

    for i in keywords[:30]:
        if(i[1]>=4.0):
            listKeywords.append(i[0])

    #we are cleaning the keywords so that we can use it in the recommender system
    for i in listKeywords:
        clean = i.replace(" ", "")
        cleanKeywords.append(clean)

    keywordString = ','.join(cleanKeywords)

    keywordString = keywordString.replace(",", " ")

    sourceText = keywordString

    li = []
    for word in sourceText.split():
        stemmedword = stemmer.stem(word)
        li.append(stemmedword)
        sourceText = ' '.join(li)
    
    keywordsText = sourceText
    return keywordsText


# transcribe = ' 15 Python libraries you need for machine learning, deep learning and data science in 30 seconds. Let\'s go. The base is built by NumPy, Pandas, Matplotlib and PsychitLearn. Optionally, for machine learning, you can have a look at Seaborn, Xtibust and Imbalanced Learn. For deep learning, you should choose one of the following. Tens of flow, PyTorch, or Chex. For computer vision, those two libraries are essential. Open CV and Pillow. And for natural language processing, these are the most important ones. Hugging Face, NLTK, and Spacey. Follow our channel for more machine learning content.'
# keywordsText = keywordsUsingRake(transcribe)
# print(keywordsText)