from conf import domain, workspace, service_version, layer_name

from flask import Flask

from api import get_wms_data

app = Flask(__name__)


@app.route('/')
# def hello_world():
#     return 'hello world'
def start_api():
    output = get_wms_data(
        wms_url=f"{domain}/geoserver/{workspace}/wms",
        service_version=service_version,
        layer_name=layer_name,
    )

    return f"<h1>Layer Title: {output['wms-title']}</h1><br>" \
           f"<p>BBOX: {output['wms-bbox']}</p><br>" \
           f"<p>THUMBNAIL PATH: {output['wms-img']}</p><br>"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
