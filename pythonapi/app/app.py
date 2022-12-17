from flask import Flask, render_template

from conf import DOMAIN, WORKSPACE, SERVICE_VERSION, LAYER_NAME, MAIN_PATH, PYTHON_API_PORT
from api import get_wms_data

app = Flask(__name__)

WMS_URL = f"{DOMAIN}/geoserver/{WORKSPACE}/wms"


@app.route('/')
def start_api():
    # output = get_wms_data(
    #     wms_url=WMS_URL,
    #     service_version=SERVICE_VERSION,
    #     layer_name=LAYER_NAME,
    # )
    # output['wms-url'] = WMS_URL
    # output['wms-layer'] = LAYER_NAME

    template_path = MAIN_PATH.joinpath('./templates/index.html')
    if not template_path.exists():
        raise Exception(f"Template path doesn't exists.\n Path: {template_path}")

    #return output
    return render_template(str(template_path), title=LAYER_NAME)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PYTHON_API_PORT, debug=True)
