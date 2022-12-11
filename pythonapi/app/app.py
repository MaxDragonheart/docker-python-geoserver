from flask import Flask

from conf import DOMAIN, WORKSPACE, SERVICE_VERSION, LAYER_NAME
from api import get_wms_data

app = Flask(__name__)


@app.route('/')
# def hello_world():
#     return 'hello world'
def start_api():
    output = get_wms_data(
        wms_url=f"{DOMAIN}/geoserver/{WORKSPACE}/wms",
        service_version=SERVICE_VERSION,
        layer_name=LAYER_NAME,
    )

    return f"<h1>Layer Title: {output['wms-title']}</h1><br>" \
           f"<p>BBOX: {output['wms-bbox']}</p><br>" \
           f"<p>THUMBNAIL PATH: {output['wms-img']}</p><br>"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8301)
