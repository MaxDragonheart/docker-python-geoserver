from flask import Flask

from conf import DOMAIN, WORKSPACE, SERVICE_VERSION, LAYER_NAME
from api import get_wms_data

app = Flask(__name__)

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

    return output


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
