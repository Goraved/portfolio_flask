from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('./index.html')


@app.route('/work/<work_name>')
def work(work_name):
    return render_template('./work.html', work_name=work_name)


@app.route('/<page_name>')
def contact(page_name):
    return render_template(f'./{page_name}.html')


if __name__ == "__main__":
    app.run()
