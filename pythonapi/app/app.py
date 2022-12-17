from pathlib import Path

from flask import Flask, render_template

from conf import DOMAIN, WORKSPACE, SERVICE_VERSION, LAYER_NAME, PYTHON_API_PORT
from api import get_wms_data

app = Flask(__name__, template_folder=Path('./templates'))

WMS_URL = f"{DOMAIN}/geoserver/{WORKSPACE}/wms"


@app.route('/')
def start_api():
    output = get_wms_data(
        wms_url=WMS_URL,
        service_version=SERVICE_VERSION,
        layer_name=LAYER_NAME,
    )
    output['wms-url'] = WMS_URL
    output['wms-layer'] = LAYER_NAME

    return render_template('index.html', title=LAYER_NAME, context=output)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PYTHON_API_PORT, debug=True)
