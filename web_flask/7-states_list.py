#!/usr/bin/python3
"""
    List of state
"""

from flask import Flask, render_template
from models.state import State
from models import storage
app = Flask(__name__)


@app.route('/states_list')
def states_list():
    """Render template with states
    """
    path = '7-states_list.html'
    states = storage.all(State)
    # sort State object alphabetically by name
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template(path, sorted_states=sorted_states)


@app.teardown_appcontext
def app_teardown(arg=None):
    """Clean-up session
    """
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
