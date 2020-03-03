# flask 는 웹앱을 만들기 위한 마이크로 웹 프라임워크 
# render_template = 
from flask import Flask, render_template, request
from vsearch import search_for_letters
app = Flask(__name__)

def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
         print(req,res, file=log)

@app.route('/search4', methods=['GET', 'POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here you are results:'
    results = str(search_for_letters(phrase,letters))
    log_request(request, results)
    return render_template('results.html',
                            the_title=title,
                            the_phrase=phrase,
                            the_letters=letters,
                            the_results=results)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                            the_title='Welcome to search4letters on the web!')
@app.route('/viewlog')
def view_log_data() -> str:
    with open('vsearch.log') as log:
        contents = log.read()
    return contents

if __name__ == '__main__':
    app.run(debug=True)