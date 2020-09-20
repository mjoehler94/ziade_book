from flask import Blueprint, jsonify

teams = Blueprint('teams', __name__)

_DEVS = ['Tarek', 'Bob']
_OPS = ['Bill','Ted', 'Matt']
_ANALYSTS = ['Justin', 'Conner', 'Casey']
_TEAMS = {1: _DEVS, 2: _OPS, 3: _ANALYSTS}

@teams.route('/teams')
def get_all():
    return jsonify(_TEAMS)

@teams.route('/teams/<int:team_id>')
def get_team(team_id):
    return jsonify(_TEAMS[team_id])
