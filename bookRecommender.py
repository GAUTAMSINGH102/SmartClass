import pandas as pd
import numpy as np
import pickle
import joblib
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer


def bookRecommender(keywordString):
    import joblib
    # model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    # joblib.dump(model, 'ST_model.pkl')
    model = joblib.load('sentenceTransformer/ST_model.pkl')
    book_sentence_embeddings = joblib.load('embeddings/sentence_embeddings_book_joblib.pkl')
    # print(book_sentence_embeddings)
    bookdata = pickle.load(open(r'recommender/bookdata.pkl', 'rb'))
    # bookdata = pd.read_csv('recommender/books_data.csv')
    # stemmer = pickle.load(open('preprocessing/snowballStemmer.pkl', 'rb'))
    # stop = pickle.load(open('preprocessing/stopwords.pkl', 'rb'))
    #
    # bookdata = bookdata.drop_duplicates().reset_index()
    #
    # bookdata['cleaned_desc'] = bookdata['desc'].astype('str').apply(lambda x: str(x.strip()))
    #
    # bookdata['cleaned_desc'] = bookdata['cleaned_desc'].astype('str').apply(lambda x: str(x.replace("nan", "")))
    #
    # bookdata['cleaned_desc'] = bookdata['cleaned_desc'].astype('str').apply(lambda x: str(x.replace("-", "")))
    # bookdata['cleaned_desc'] = bookdata['cleaned_desc'].astype('str').apply(lambda x: str(x.replace(",", "")))
    # bookdata['cleaned_desc'] = bookdata['cleaned_desc'].astype('str').apply(lambda x: str(x.replace(".", "")))
    # bookdata['cleaned_desc'] = bookdata['cleaned_desc'].astype('str').apply(lambda x: str(x.replace("'", "")))
    # bookdata['cleaned_desc'] = bookdata['cleaned_desc'].astype('str').apply(lambda x: str(x.replace('``', "")))
    # bookdata['cleaned_desc'] = bookdata['cleaned_desc'].astype('str').apply(lambda x: str(x.lower()))
    #
    # bookdata['cleaned_title'] = bookdata['title'].astype('str').apply(lambda x: str(x.replace("-", "")))
    # bookdata['cleaned_title'] = bookdata['cleaned_title'].astype('str').apply(lambda x: str(x.replace(",", "")))
    # bookdata['cleaned_title'] = bookdata['cleaned_title'].astype('str').apply(lambda x: str(x.replace(".", "")))
    # bookdata['cleaned_title'] = bookdata['cleaned_title'].astype('str').apply(lambda x: str(x.replace("'", "")))
    # bookdata['cleaned_title'] = bookdata['cleaned_title'].astype('str').apply(lambda x: str(x.lower()))
    #
    # bookdata['combine'] = bookdata['cleaned_title'] + " " + bookdata['cleaned_desc']
    #
    # ###**Removing Stopwords**
    #
    # bookdata['combine'] = bookdata['combine'].apply(
    #     lambda words: ' '.join(word.lower() for word in words.split() if word not in stop))
    #
    # ###**Stemming the String**
    #
    # bookdata['combine'] = bookdata['combine'].apply(
    #     lambda words: ' '.join(stemmer.stem(word) for word in words.split()))
    #
    # ###**Sentence Transformer**
    #
    # model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    #
    # book_sentence_embeddings = model.encode(bookdata['combine'])
    #
    # import joblib
    # joblib.dump(book_sentence_embeddings, 'sentence_embeddings_book_joblib.pkl')

    source_embedding = model.encode(keywordString)

    book_similar_matrix = cosine_similarity(
        [source_embedding],
        book_sentence_embeddings[:]
    )
    # print(similar_matrix)

    # sorting
    book_similar_ix = np.argsort(book_similar_matrix[0])[::-1]
    # print(similar_ix)
    # print(similar_matrix[0][similar_ix])

    book_title_list = []
    book_desc_list = []
    book_image_list = []

    for ix in book_similar_ix[:5]:
        title = bookdata.iloc[ix]['title']
        cleaned_desc = bookdata.iloc[ix]['cleaned_desc']
        thumbnail = bookdata.iloc[ix]['image']

        book_title_list.append(title)
        book_desc_list.append(cleaned_desc)
        book_image_list.append(thumbnail)

    # book_card = {book_title_list[i]: [book_desc_list[i], book_image_list[i]] for i in range(len(book_similar_ix[:5]))}
    book_card = [book_title_list[i] for i in range(len(book_similar_ix[:5]))]

    return book_card

sourceText = 'naturallanguageprocess machinelearningcont machinelearn deeplearn datasci imbalancedlearn computervis opencv huggingfac'
# sourceText = sourceText.encode()
book_card = bookRecommender(sourceText)
print(book_card)


