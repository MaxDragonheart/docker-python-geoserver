import json

from api import get_wms_data


# Opening JSON file
file = open('geoserver_json.json')

# returns JSON object as
# a dictionary
data = json.load(file)


if __name__ == '__main__':
    get_wms_data(
        wms_url=f"{data['url']}/geoserver/{data['workspace']}/wms",
        service_version=data['service_version'],
        layer_name=data['layer_name'],
    )
