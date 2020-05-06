import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import convs

# nltk.download('punkt', quiet=True)
# nltk.download('wordnet', quiet=True)

RANDOM_RESPONSES = ['ExTeRmiNaTe', 'I love cheese!', 'I don\'t understand. And what? Gonna bully me?',
                    'It\'s time to stop!', 'WHAT?', 'You know...', 'Ask google', 'I\'m not interested']

sent_tokens = nltk.sent_tokenize(convs.text)
remove_punctuation_dict = dict((ord(pun), None) for pun in string.punctuation)


def LemNormalize(text):
    return nltk.word_tokenize(text.lower().translate(remove_punctuation_dict))


def response(user_response):
    user_response = user_response.lower()
    bot_response = ''
    sent_tokens.append(user_response)  # добавим ответ пользователя в список предложений

    # create TfidfVectorizer Object
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]  # индекс самого похожего на ответ пользователя предложения
    flat = vals.flatten()
    flat.sort()
    score = flat[-2]
    if score <= 0.20:
        bot_response += random.choice(RANDOM_RESPONSES)
    else:
        try:
            metka = convs.inv_lines[sent_tokens[idx] + '\n']
            next_m = convs.line_after_line[metka]
            resp = convs.lines[next_m]
            bot_response += resp
        except Exception:
            try:
                bot_response += sent_tokens[idx]
            except Exception:
                bot_response += random.choice(RANDOM_RESPONSES)
    sent_tokens.remove(user_response)
    return bot_response
