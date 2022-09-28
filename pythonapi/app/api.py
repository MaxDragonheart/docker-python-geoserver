from pathlib import Path

from owslib.wms import WebMapService
from fsspec import get_fs_token_paths


def get_wms_data(
        wms_url: str,
        service_version: str,
        layer_name: str,
        srs: str = 'EPSG:4326',
        width: int = 300,
        high: int = 300,
) -> dict:
    """Get thumbnail from WMS layer, it's saved into selected folder and also return
    the saved path.
    Args:
        wms_url: String.
        service_version: String.
        layer_name: String.
        srs: String.
        width: Integer.
        high: Integer.
    Returns:
        dict
    """
    # Read WMS
    wms = WebMapService(url=wms_url, version=service_version)

    # Get bounding box from selected layer
    layer = wms[layer_name]
    bbox = layer.boundingBoxWGS84

    # Create thumbnail
    img = wms.getmap(
        layers=[layer_name],
        srs=srs,
        bbox=bbox,
        size=(width, high),
        format='image/jpeg',
        transparent=True
    )

    # Make destination folder
    destination_folder = Path().cwd().parent.joinpath('media')
    fs, fs_token, paths = get_fs_token_paths(destination_folder)
    fs.mkdirs(path=destination_folder, exist_ok=True)

    # Put thumbnail into destinantion folder
    img_path = Path(f'{destination_folder}/{layer.title}.jpg')
    out = open(img_path, 'wb')
    out.write(img.read())
    out.close()

    data = {
        "wms-title": layer.title,
        "wms-bbox": bbox,
        "wms-img": img_path
    }
    return data

# TEST
# if __name__ == '__main__':
#     domain = "https://geoserver.massimilianomoraca.me"
#     workspace = "MassimilianoMoraca"
#     service_version = "1.3.0"
#     layer_name = "edificicasalnuovo"
#
#     get_wms_data(
#         wms_url=f"{domain}/geoserver/{workspace}/wms",
#         service_version=service_version,
#         layer_name=layer_name,
#     )
