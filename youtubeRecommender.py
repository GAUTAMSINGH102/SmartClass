import pandas as pd
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import joblib

def youtubeRecommender(keywordString):
    # model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    # joblib.dump(model, 'ST_model.pkl')
    model = joblib.load('sentenceTransformer/ST_model.pkl')
    sentence_embeddings = pickle.load(open('.\embeddings\sentence_embeddings.pkl', 'rb'))
    print(sentence_embeddings)
    ssdata = pd.read_csv('recommender/stratascratch.csv')

    source_embedding = model.encode(keywordString)

    similar_matrix = cosine_similarity(
        [source_embedding],
        sentence_embeddings[:]
    )
    # print(similar_matrix)

    # sorting
    similar_ix = np.argsort(similar_matrix[0])[::-1]
    # print(similar_ix)
    # print(similar_matrix[0][similar_ix])

    video_title_list = []
    video_id_list = []
    video_thumbnail_list = []

    for ix in similar_ix[:5]:
        title = ssdata.iloc[ix]['video_title']
        video_id = ssdata.iloc[ix]['video_id']
        thumbnail = ssdata.iloc[ix]['video_thumbnail']

        video_title_list.append(title)
        video_id_list.append(video_id)
        video_thumbnail_list.append(thumbnail)

    video_card = {video_title_list[i]: [video_id_list[i], video_thumbnail_list[i]] for i in range(len(similar_ix[:5]))}

    return video_card

# sourceText = 'naturallanguageprocess machinelearningcont machinelearn deeplearn datasci imbalancedlearn computervis opencv huggingfac'
# # sourceText = sourceText.encode()
# video_card = youtubeRecommender(sourceText)
# print(video_card)


