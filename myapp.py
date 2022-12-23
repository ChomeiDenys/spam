from fastapi import FastAPI, Query
import uvicorn
import joblib, os

PACKAGE_DIR = os.path.dirname(__file__)

spam_vectorizer = open("models/spam_vectorizer.pkl", 'rb')
spam_cv = joblib.load(spam_vectorizer)

spam_nb_model = open("models/spam_detector_nb_model.pkl", 'rb')
spam_clf = joblib.load(spam_nb_model)

app = FastAPI()


@app.get('/')
def index():
    return {"Text": "THIS IS MY FIRST API TUTORIAL"}


@app.get('/items/')
async def get_item(name: str = Query(None, min_length=2, max_length=25)):
    return {"name": name}


@app.get('/predict/{text}')
async def predict(text=None):
    # super(CommentClassifier, self).__init__()
    # self.text = text
    # predict(self.text)
    """Predict If It is Spam or Not
	By Default It uses the Naive Bayes Algorithm
	
	s = CommentClassifier()
	s.text = " "
	s.predict()

	"""
    text = [text]
    # self.text=text
    # load Vectorizer For Spam Prediction
    spam_vectorizer = open(os.path.join(PACKAGE_DIR, "models/spam_vectorizer.pkl"), "rb")
    spam_cv = joblib.load(spam_vectorizer)

    # load Model For Spam Prediction
    spam_detector_nb_model = open(os.path.join(PACKAGE_DIR, "models/spam_detector_nb_model.pkl"), "rb")
    spam_detector_clf = joblib.load(spam_detector_nb_model)
    vectorized_data = spam_cv.transform(text).toarray()
    prediction = spam_detector_clf.predict(vectorized_data)
    if prediction[0] == 0:
        result = 'Non-Spam'
    elif prediction[0] == 1:
        result = 'Spam'
    return result


@app.post('/predict/{text}')
async def predict(text=None):
    # super(CommentClassifier, self).__init__()
    # self.text = text
    # predict(self.text)
    """Predict If It is Spam or Not
	By Default It uses the Naive Bayes Algorithm
	
	s = CommentClassifier()
	s.text = " "
	s.predict()

	"""
    text = [text]
    # self.text=text
    # load Vectorizer For Spam Prediction
    spam_vectorizer = open(os.path.join(PACKAGE_DIR, "models/spam_vectorizer.pkl"), "rb")
    spam_cv = joblib.load(spam_vectorizer)

    # load Model For Spam Prediction
    spam_detector_nb_model = open(os.path.join(PACKAGE_DIR, "models/spam_detector_nb_model.pkl"), "rb")
    spam_detector_clf = joblib.load(spam_detector_nb_model)
    vectorized_data = spam_cv.transform(text).toarray()
    prediction = spam_detector_clf.predict(vectorized_data)
    if prediction[0] == 0:
        result = 'Non-Spam'
    elif prediction[0] == 1:
        result = 'Spam'
    return result


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
