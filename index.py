from itertools import islice

from flask import Flask, render_template

from data import PROJECTS, PROJECT_LINKS

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('./index.html')


@app.route('/project/<project_name>')
def project(project_name):
    info = PROJECTS[project_name]
    if 'site_link' in info:
        return render_template('./project.html', work_name=project_name, title=info['title'], desc=info['desc'],
                               git_link=info['git_link'], site_link=info['site_link'], images=info['images'],
                               projects=PROJECT_LINKS)
    else:
        return render_template('./project.html', work_name=project_name, title=info['title'], desc=info['desc'],
                               git_link=info['git_link'], images=info['images'], projects=PROJECT_LINKS)


def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


@app.route('/projects')
def projects():
    info = list(chunk([PROJECTS[project] for project in PROJECTS], 3))
    return render_template(f'./projects.html', info=info, len_projects=len(PROJECTS))


@app.route('/<page_name>')
def contact(page_name):
    return render_template(f'./{page_name}.html')


if __name__ == "__main__":
    app.run()
