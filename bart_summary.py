import pickle

def summaryfromtranscribe(transcribeText):
    # transcribeText = " 15 Python libraries you need for machine learning, deep learning and data science in 30 seconds. Let's go. The base is built by NumPy, Pandas, Matplotlib and PsychitLearn. Optionally, for machine learning, you can have a look at Seaborn, Xtibust and Imbalanced Learn. For deep learning, you should choose one of the following. Tens of flow, PyTorch, or Chex. For computer vision, those two libraries are essential. Open CV and Pillow. And for natural language processing, these are the most important ones. Hugging Face, NLTK, and Spacey. Follow our channel for more machine learning content."
    model = pickle.load(open(r'.\bart\bart_model_large_cnn.pkl', 'rb'))
    tokenizer = pickle.load(open(r'.\bart\bart_tokenizer_large_cnn.pkl', 'rb'))
    transcribeText = transcribeText
    #Divinding Text
    dividedText = transcribeText.replace(".", ".<eos>")
    dividedText = transcribeText.replace("?", "?<eos>")
    dividedText = transcribeText.replace("!", "!<eos>")

    transcribeSentences = dividedText.split("<eos>")

    max_chunk = 500
    current_chunk = 0
    chunks = []

    for sentence in transcribeSentences:
        if(len(chunks) == current_chunk + 1):
            if (len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk):
                chunks[current_chunk].extend(sentence.split(' '))
            else:
                current_chunk += 1
                chunks.append(sentence.split(' '))
        else:
            chunks.append(sentence.split(' '))
            # print(len(chunks))
            # print(chunks)

    for id in range(len(chunks)):
        chunks[id] = ' '.join(chunks[id])

    summary = []

    for i in chunks:
        inputs = tokenizer([i], return_tensors='pt')
        summary_ids = model.generate(inputs['input_ids'], max_length=500, early_stopping=False)
        output = [tokenizer.decode(g, skip_special_tokens=True) for g in summary_ids]
        summary.append(output[0])

    summaryText = ' '.join(summary)
    
    return summaryText

# summary = summaryfromtranscribe()
# print(summary)