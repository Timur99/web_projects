from flask import Flask, render_template, request, redirect, url_for, make_response
from story import story_data # тут хранится история формата [{},{}]

app = Flask(__name__, template_folder='templates')
player_state = {
    'current_scene': 1,
    'answers': {}
}
user_answer = ''

@app.route('/')
def index():
    current_scene = get_current_scene()
    print(current_scene)
    if current_scene['id'] == 2:
        return render_template('index.html', scene=current_scene, user_answer=story_data[0]['options'].get(user_answer,''))
    return render_template('index.html', scene=current_scene, user_answer='')


@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    answer = request.form.get('answer')
    global user_answer
    user_answer = request.form.get('answer')
    save_answer(answer)
    print(answer)
    return redirect(url_for('index'))

@app.route('/exit', methods=['POST'])
def exit():
    player_state['current_scene'] = 1
    return redirect(url_for('index'))
    #return render_template('index.html', scene=1)
def get_current_scene():
    for scene in story_data:
        if scene['id'] == player_state['current_scene']:
            return scene

def save_answer(answer):
    player_state['answers'][player_state['current_scene']] = answer
    next_scene = get_current_scene()['next_scene']
    print(player_state)
    if next_scene is not None:
        player_state['current_scene'] = next_scene

if __name__ == '__main__':
    app.run(debug=True)