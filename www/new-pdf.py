import PyPDF2
#import gensim
#import nltk
#import sys
import string
from flask import Flask, redirect, url_for, request, render_template
import os
#import cgi
import jinja2
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


app = Flask(__name__)


#upload = sys.argv[1]
corpus_raw = u""
with open("driver/test.pdf", 'rb') as pdf_file:
    pdfReader = PyPDF2.PdfFileReader(pdf_file)
    no_of_page = pdfReader.numPages
    print("Number of Pages in PDF = ",no_of_page)
    i = 0

    while i < no_of_page:
        pageObj = pdfReader.getPage(i)
        text = pageObj.extractText().replace('\n', ' ')
        i += 1

        corpus_raw = corpus_raw + text
        corpus_raw = corpus_raw.translate(string.punctuation)
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(corpus_raw)
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        filtered_sentence = []
        for w in word_tokens:
            if w not in stop_words:
                filtered_sentence.append(w)
        #print(word_tokens)
        #print(filtered_sentence)


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)




@app.route('/')

def index():
    template = jinja_env.get_template('verify.html')
    return template.render(filtered_sentence=filtered_sentence)


@app.route('/submit')

def result():
    exec('Synchronous.py')



if __name__ == '__main__':
    app.run(port=5000)
