import json
from pathlib import Path

from flask import Flask

from api import get_wms_data, MAIN_PATH

app = Flask(__name__)


@app.route('/')
# def hello_world():
#     return 'hello world'
def start_api():
    # Opening JSON file
    file = open(MAIN_PATH.parent.joinpath('geoserver_json.json'))

    # returns JSON object as
    # a dictionary
    data = json.load(file)

    output = get_wms_data(
        wms_url=f"{data['url']}/geoserver/{data['workspace']}/wms",
        service_version=data['service_version'],
        layer_name=data['layer_name'],
    )

    return f"<h1>Layer Title: {output['wms-title']}</h1><br>" \
           f"<p>BBOX: {output['wms-bbox']}</p><br>" \
           f"<p>THUMBNAIL PATH: {output['wms-img']}</p><br>"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
