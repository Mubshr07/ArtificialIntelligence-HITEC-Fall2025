import numpy as np
import pandas as pd

#for plotting
import matplotlib.pyplot as plt
import seaborn as sns

#to work on text data
import re
import string

#for memory management
import gc 

#for ignoring warnings
import warnings
warnings.filterwarnings('ignore')
data = pd.read_csv('F:\DSA\AI Project\SentimentAnalysis_RomanUrdu_data-master\Roman Urdu DataSet.csv',  usecols = [0,1], names = ['review','sentiment'])
data.head(3)
print("The size of the training data is: " + str(data.shape))
print(data.dtypes)
data.isna().sum()
data.dropna(inplace= True)
def clean_df(input_df):
    input_df['review'] = input_df['review'].apply(lambda x: ' '.join(x.split())) #removing blanks
    input_df['review'].replace('', np.nan, inplace = True) #replacing blanks with nan
    input_df.dropna(subset = ['review'], inplace = True) #dropping blank values
    return input_df 
data.isna().sum()
data = clean_df(data)
data['sentiment'].value_counts()
data[data['sentiment'] == 'Neative']
data['sentiment'] = data['sentiment'].replace('Neative','Negative')
print(data['sentiment'].value_counts())
print()
sns.countplot(data['sentiment'])
stopwordslist = [
    "ai","ayi","hy","hai","main","ki","tha","koi","ko","sy","woh","bhi","aur","wo","yeh",
    "rha","hota","ho","ga","ka","le","lye","kr","kar","liye","hotay","waisay","gya","gaya",
    "kch","ab","thy","thay","houn","hain","han","to","is","hi","jo","kya","thi","se","pe",
    "phr","wala","us","na","ny","hun","raha","ja","rahay","abi","uski","ne","haan","acha",
    "nai","sent","photo","you","kafi","gai","rhy","kuch","jata","aye","ya","dono","hoa",
    "aese","de","wohi","jati","jb","krta","lg","rahi","hui","karna","krna","gi","hova",
    "yehi","jana","jye","chal","mil","tu","hum","par","hay","kis","sb","gy","dain","krny","tou"
]
def review_preprocessing(input_review):
    input_review = input_review.astype(str).str.lower()  # lowercase
    input_review = input_review.astype(str).str.replace('[{}]'.format(string.punctuation), '', regex=True)  # remove punctuation
    input_review = input_review.astype(str).str.replace("[^a-zA-Z#]", ' ', regex=True)  # remove special chars
    input_review = input_review.apply(
        lambda x: ' '.join([word for word in str(x).split() if not word.isdigit() and word not in stopwordslist])
    )  # remove numbers + stopwords
    input_review = input_review.astype(str).str.strip()  # strip spaces
    return input_review
data['review'] = review_preprocessing(data['review'])
data. duplicated().sum()
data = data.drop_duplicates(keep='first').reset_index(drop = True)
data.describe().transpose()
sns.distplot (data.review.str.len()[data['sentiment']=='Positive'], bins=10, label='Positive')
sns.distplot (data.review.str.len()[data['sentiment']=='Neutral'], bins=10, label='Neutral')
sns.distplot (data.review.str.len()[data['sentiment']=='Negative'], bins=10, label='Negative')
plt.legend()
plt.show()
print(data['sentiment'].value_counts())
print()
sns.countplot(data['sentiment'])
from wordcloud import WordCloud
all_words = ' '.join([word for word in data[data['sentiment'] == 'Positive']['review']])
wordcloud_gen = WordCloud(width=800, height=500, random_state=1, max_font_size=110).generate(all_words)
plt.imshow(wordcloud_gen, interpolation="bilinear")
plt.show()
from wordcloud import WordCloud
all_words = ' '.join([word for word in data[data['sentiment'] == 'Negative']['review']])
wordcloud_gen = WordCloud(width=800, height=500, random_state=1, max_font_size=110).generate(all_words)
plt.imshow(wordcloud_gen, interpolation="bilinear")
plt.show()
from wordcloud import WordCloud
all_words = ' '.join([word for word in data[data['sentiment'] == 'Neutral']['review']])
wordcloud_gen = WordCloud(width=800, height=500, random_state=1, max_font_size=110).generate(all_words)
plt.imshow(wordcloud_gen, interpolation="bilinear")
plt.show()
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

# Limit vocabulary size and remove very rare/common words
cv = CountVectorizer(max_df=0.95, min_df=2, max_features=2000)
cv_data = cv.fit_transform(data['review'])

# Use n_components instead of n_topics
lda_model = LatentDirichletAllocation(
    n_components=3,
    random_state=1,
    learning_method='online',   # faster than 'batch'
    max_iter=5                  # fewer iterations
)

topics = lda_model.fit_transform(cv_data)

n_top_words = 10
topic_word = lda_model.components_
vocab = cv.get_feature_names_out()

for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
    print(f'Topic {i}: {" | ".join(topic_words)}')
#Change sentiment to numerical value for modeling:
data['target'] = data['sentiment'].factorize()[0]
data.head()
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import gensim
from sklearn.model_selection import train_test_split

train_features,test_features, train_target, test_target = train_test_split(data['review'], data['target'],  
                                                          random_state=42, 
                                                          test_size=0.3)
cv = CountVectorizer(lowercase=False, stop_words=None, ngram_range=(1,2))
bow = cv.fit_transform(train_features)
bow.shape
tfidf =TfidfVectorizer(stop_words=None, ngram_range=(1,2))
tfidf_features = tfidf.fit_transform(train_features)
tfidf_features.shape
from gensim.models import Word2Vec
train_features_w2v = train_features.reset_index()['review']
test_features_w2v = test_features.reset_index()['review']
tokenized_train_features_w2v = train_features_w2v.apply(lambda x:x.split())
tokenized_test_features_w2v = test_features_w2v.apply(lambda x:x.split())
from gensim.models import Word2Vec

# Train Word2Vec model
word2vec_model = Word2Vec(
    sentences=tokenized_train_features_w2v,
    vector_size=200,   # instead of size
    window=5,
    min_count=2,
    sg=1,              # skip-gram
    hs=0,
    negative=10,
    workers=2,
    seed=34,
    epochs=10          # training epochs
)

# If you want to train further:
word2vec_model.train(tokenized_train_features_w2v, total_examples=len(tokenized_train_features_w2v), epochs=10)
# Check most similar words to "wah"
print(word2vec_model.wv.most_similar("wah"))
# Correct usage in gensim 4.x
print(word2vec_model.wv.most_similar("khushi"))
word2vec_model.wv.similarity(w1 = 'sari',w2 = 'hamesha')
vec = word2vec_model.wv['khushi']   # get the vector
print(len(vec))                     # length of the vector
def word_vector(tokens, size):
    vec,count = np.zeros(size).reshape((1, size)),0
    for word in tokens:
        try:
            vec += word2vec_model[word].reshape((1, size))
            count += 1
        except KeyError: # handling the case where the token is not in the vocabulary             
            continue
            
    if count != 0:
        vec /= count
    return vec
import numpy as np
import pandas as pd

# Function to average word vectors for a review
def word_vector(tokens, size=200):
    vec, count = np.zeros(size).reshape((1, size)), 0
    for word in tokens:
        if word in word2vec_model.wv:   # gensim 4.x requires .wv
            vec += word2vec_model.wv[word].reshape((1, size))
            count += 1
    return vec / count if count else vec

# Build train feature matrix
train_array_w2v = np.zeros((len(tokenized_train_features_w2v), 200))
for i, tokens in enumerate(tokenized_train_features_w2v):
    train_array_w2v[i, :] = word_vector(tokens, 200)

train_features_w2v = pd.DataFrame(train_array_w2v)

# Build test feature matrix (same process)
test_array_w2v = np.zeros((len(tokenized_test_features_w2v), 200))
for i, tokens in enumerate(tokenized_test_features_w2v):
    test_array_w2v[i, :] = word_vector(tokens, 200)

test_features_w2v = pd.DataFrame(test_array_w2v)
test_array_w2v = np.zeros((len(tokenized_test_features_w2v), 200))

for i in range(len(tokenized_test_features_w2v)):
    test_array_w2v[i,:] = word_vector(tokenized_test_features_w2v[i], 200)
    
test_features_w2v =    pd.DataFrame(test_array_w2v) 
test_array_w2v = np.zeros((len(tokenized_test_features_w2v), 200))

for i in range(len(tokenized_test_features_w2v)):
    test_array_w2v[i,:] = word_vector(tokenized_test_features_w2v[i], 200)
    
test_features_w2v =    pd.DataFrame(test_array_w2v) 
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer

from sklearn.linear_model import LogisticRegression

from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import GridSearchCV

from sklearn.metrics import accuracy_score

from sklearn.pipeline import Pipeline
pipe_logreg_cv = Pipeline ([('cv' , CountVectorizer()),('logreg', LogisticRegression (class_weight = 'balanced', random_state=42))])
pipe_logreg_tfidf = Pipeline ([('tfidf' , TfidfVectorizer()),('logreg', LogisticRegression(class_weight = 'balanced',random_state=42))])
pipe_logreg_w2v = Pipeline ([('logreg', LogisticRegression (class_weight = 'balanced',random_state=42))])

pipe_rf_cv = Pipeline ([('cv' , CountVectorizer()),('rf', RandomForestClassifier (random_state=42))])
pipe_rf_tfidf = Pipeline ([('tfidf' , TfidfVectorizer()),('rf', RandomForestClassifier (random_state=42))])
pipe_rf_w2v = Pipeline ([('rf', RandomForestClassifier (random_state=42))])

pipeline_list = [pipe_logreg_cv,pipe_logreg_tfidf,pipe_logreg_w2v,pipe_rf_cv,pipe_rf_tfidf,pipe_rf_w2v]

pipeline_dict = {0: 'Logistic Regression with CountVectorizer', 1: 'Logistic Regression with Tfidf', 
             2: 'Logistic Regression with w2v', 3: 'Random Forest with CountVectorizer', 
             4: 'Random Forest with Tfidf' , 5: 'Random Forest with w2v'}
for idx, gs in enumerate(pipeline_list):
    print('\nEstimator: %s' % pipeline_dict[idx])
    train_features1 = train_features_w2v if pipeline_dict[idx] == 'Logistic Regression with w2v' or  pipeline_dict[idx] == 'Random Forest with w2v'  else train_features
    test_features1 = test_features_w2v if pipeline_dict[idx] == 'Logistic Regression with w2v'  or  pipeline_dict[idx] == 'Random Forest with w2v'  else test_features
    # Fit grid search
    gs.fit(train_features1, train_target)
    # Predict on test data with best params
    y_pred = gs.predict(test_features1)
    # Test data accuracy of model with best params
    print('Test set accuracy score: %.3f ' % accuracy_score(test_target, y_pred))
param_range = [1,  3, 5, 10]
param_range_fl = [1.0, 0.5, 0.1]
param_ngram_range = [(1,2),(1,3)]
param_max_df = [0.8, 1.0]
param_cv_tfidf_max_features =  [100,200]
param_min_samples =  [1, 2]
param_rf_max_features = ["auto",  "sqrt"]
param_penalty= ['l1', 'l2']


gridparams_logreg_cv = [{'logreg__C': param_range_fl,'logreg__penalty':param_penalty, 'cv__max_df': param_max_df,
                         #'cv__max_features': param_cv_tfidf_max_features,
                         'cv__ngram_range':param_ngram_range}]

gridparams_rf_tfidf = [{ 'rf__max_features': param_rf_max_features,
                    #    'rf__min_samples_leaf' : param_range,
'tfidf__max_df': param_max_df,#'tfidf__max_features': param_cv_tfidf_max_features
                       #, 'tfidf__ngram_range':param_ngram_range
                       }]
gs_logreg_cv = GridSearchCV(estimator=pipe_logreg_cv,param_grid=gridparams_logreg_cv,scoring='accuracy',cv=10)
gs_rf_tfidfcv = GridSearchCV(estimator=pipe_rf_tfidf,param_grid=gridparams_rf_tfidf,scoring='accuracy',cv=10)
gridlist = [gs_logreg_cv, gs_rf_tfidfcv]

grid_dict = {0: 'Logistic Regression with CountVectorizer', 
             1: 'Random Forest with Tfidf'}
best_acc = 0.0
best_clf = 0
best_gs = ''

for idx, gs in enumerate(gridlist):
    print('\nEstimator: %s' % grid_dict[idx])
    # Fit grid search
    gs.fit(train_features, train_target)
    #gs.fit(train_features_w2v, train_target) if gs == gs_logreg_w2v else gs.fit(train_features, train_target)
    # Best params
    print('Best params: %s' % gs.best_params_)
    y_pred = gs.predict(test_features)
    # Test data accuracy of model with best params
    print('Test set accuracy score for best params: %.3f ' % accuracy_score(test_target, y_pred))
    #Track best (highest test accuracy) model
    if accuracy_score(test_target, y_pred) > best_acc:
        best_acc = accuracy_score(test_target, y_pred)
        best_gs = gs
        best_clf = idx
print('\nClassifier with best test set accuracy: %s' % grid_dict[best_clf])
import joblib

# Save the best model
joblib.dump(best_gs.best_estimator_, "best_model.pkl")

# Save the vectorizer used inside the pipeline
if 'cv' in best_gs.best_estimator_.named_steps:
    joblib.dump(best_gs.best_estimator_.named_steps['cv'], "vectorizer.pkl")
elif 'tfidf' in best_gs.best_estimator_.named_steps:
    joblib.dump(best_gs.best_estimator_.named_steps['tfidf'], "vectorizer.pkl")
import joblib
import pandas as pd

# Load saved pipeline
best_model = joblib.load("best_model.pkl")

# Load dataset to recover label mapping
data = pd.read_csv("Roman Urdu DataSet.csv", usecols=[0,1], names=["review", "sentiment"])
_, uniques = pd.factorize(data["sentiment"])

# Predict new review
new_review = "Mannan yera project ki report to bana"
prediction = best_model.predict([new_review])
print("Predicted sentiment:", uniques[prediction[0]])