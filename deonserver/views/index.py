"""
Deonserver index (main) view.

"""
import hashlib
import pathlib
import os
import flask
import deonserver


@deonserver.app.route('/')
def show_index():
    """Display / route."""
    checklists = os.listdir("deonserver/checklists")
    inserter = {"files": []}
    for num, checklist in enumerate(checklists):
        inserter["files"].append({
            "title": checklist.replace(".html", ""),
            "file_num": num + 1,
            "link": "/checklist/" + str(num + 1)
        })
    return flask.render_template("index.html", **inserter)


@deonserver.app.route('/checklist/<num>')
def uploads(num):
    checklists = os.listdir("deonserver/checklists")
    name = checklists[int(num)-1]
    # do language and job ask if file is specified instead
    if not name.lower().endswith(('.txt', '.html', '.ipynb', '.md', '.rmd', '.rst', '.tex')):
        lan = flask.request.args.get("l", default="eng", type=str)
        job = flask.request.args.get("j", default="worker", type=str)
        name += "/" + os.path.basename(os.path.normpath(name))
        if lan:
            name += "_" + lan
        if job:
            name += "_" + job
        name += ".html"
    htmlloader = open("deonserver/checklists/" + name)
    htmltext = htmlloader.read()
    return htmltext