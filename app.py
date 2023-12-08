from flask import Flask, render_template, request
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

app = Flask(__name__)
@app.route('/')

def index():
 return render_template('index.html')
@app.route('/login')
def login():
    return render_template('login/log.html')

@app.route('/signup')
def signup():
    return render_template('Signup/signup.html')

@app.route('/test')
def test():
    return render_template('Faq/test.html')

def summaryGenerator(text):

    # Tokenizing the text
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)

    # Creating a frequency table to keep the score of each word

    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    # Creating a dictionary to keep the score of each sentence
    sentences = sent_tokenize(text)
    sentenceValue = dict()

    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq

    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]

    # Average value of a sentence from the original text
    average = int(sumValues / len(sentenceValue))

    # Storing sentences into our summary.
    summary = ''
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
            summary += " " + sentence

    print(summary)
    return summary

# render index.html page


@app.route('/indText', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("indtext.html")


# get input text from client then summarise and render respective .html page for solution


@app.route("/summariser", methods=['GET', 'POST'])
def summariser():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        initial_corpus = request.form.get("initial-corpus")
        # text = summaryGenerator(initial_corpus)
        return """
        <h1>Welcome</h1>
        <label>Summary</label>
        <Textarea>{initial_corpus}</Textarea>
        <button><a href="./summariser">Go Back</a></button>
        """.format(initial_corpus=initial_corpus)
    return render_template('webApp.html')


if __name__ =="__main__":
 app.run(host="0.0.0.0")