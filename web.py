import json
import os

from flask import request, url_for, send_from_directory
from flask_accept import accept
from flask_api import FlaskAPI
from flask_cors import CORS
from flask_jwt_simple import (
    JWTManager, jwt_required, get_jwt_identity
)

from src.gid.service import GidService
from src.list.service import ListService
from src.services.directory import ServicesDirectoryFactory

# get your Fidj Secret Ids and
ENV_PORT = int(os.environ.get("PORT", 7654))
ENV_JWT_AUDIENCE = str(os.environ.get("FIDJ_APP_ID", ''))
ENV_JWT_SECRET_KEY = str(os.environ.get("FIDJ_SECRET_KEY", ''))
print('APP 0.0.0.0:' + str(ENV_PORT))

# webapp
app = FlaskAPI(__name__, template_folder='templates', static_folder='static')
app.debug = True
app.config['JWT_SECRET_KEY'] = ENV_JWT_SECRET_KEY
app.config['JWT_DECODE_AUDIENCE'] = ENV_JWT_AUDIENCE
app.config['JWT_IDENTITY_CLAIM'] = 'roles'
jwt = JWTManager(app)
CORS(app)

# launch your bots
bot1 = ListService()
bot2 = GidService()
ServicesDirectoryFactory.get().launchAllServices()


@app.route('/api/', methods=['GET'])
def get_all_apis():
    """
    Seed for a Futur Revolubot : services oriented (POST /api/services/:title with params)
    """
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        # methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        # line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        line = "" + request.host_url.rstrip('/') + url

        if ("flask" not in line) and ("filename" not in line):
            output.append(line)

    return {'apis': output}, 200


@app.route('/api/status', methods=['GET', 'POST', 'OPTIONS', 'PUT', 'DELETE', 'PATCH', 'POO'])
def get_status():
    """
    Get status & version
    """
    output = {'ok': 'true', 'version': '0.0.1', 'jwt.roles': get_jwt_identity()}
    return output, 200


@app.route('/api/protected', methods=['GET'])
@jwt_required
def test_jwt_bearer_protection():
    """
    Test with curl -H "Authorization: Bearer YOUR_JWT_ID_TOKEN" http://localhost:7654/api/protected
    """
    roles = get_jwt_identity()
    return {'roles': roles}, 200


@app.route('/api/services', methods=['GET'])
def get_all_services():
    """
    Get all services
    """
    output = {'services': json.dumps(ServicesDirectoryFactory.get().getAllServices())}
    return output, 200


@app.route('/api/services/<title>', methods=['POST'])
@accept('application/json', 'text/json')
@jwt_required
def post_service(title):
    """
    Get one service for the role needed;

    Test with curl -H "Authorization: Bearer YOUR_JWT_ID_TOKEN" -X POST http://localhost:7654/api/services/:title
    """
    roles = get_jwt_identity()
    if 'Nuxeo' not in roles:
        return {'result': ''}, 403

    formData = request.data
    output, outputStatus = ServicesDirectoryFactory.get().launchService(title, formData)

    return {'result': output}, outputStatus


@app.route('/downloads/<path:filename>', methods=['GET', 'POST'])
def get_downloads(filename):
    downloads = os.path.join(app.root_path, 'downloads')
    return send_from_directory(directory=downloads, filename=filename)


# Usefull but need protection ;
# @app.route('/api/pull', methods=['POST'])
# def admin_pull():
#     """
#     Pull git
#     """
#     g = git.cmd.Git('./')
#     g.pull()
#     return response_format({'ok': 'true'})


# No root but /api ;
# @app.route('/')
# def main():
#    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=ENV_PORT, debug=True)
