import logging
from pathlib import Path

from owslib.wms import WebMapService
from fsspec import get_fs_token_paths

from conf import DOMAIN, WORKSPACE, SERVICE_VERSION, LAYER_NAME, MAIN_PATH


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
    logging.info("Read WMS")
    wms = WebMapService(url=wms_url, version=service_version)

    # Get bounding box from selected layer
    logging.info("Get bounding box from selected layer")
    layer = wms[layer_name]
    bbox = layer.boundingBoxWGS84

    # Create thumbnail
    logging.info("Create thumbnail")
    img = wms.getmap(
        layers=[layer_name],
        srs=srs,
        bbox=bbox,
        size=(width, high),
        format='image/jpeg',
        transparent=True
    )

    # Make destination folder
    logging.info("Make thumbnail's destination folder")
    destination_folder = MAIN_PATH.parent.joinpath('media')
    fs, fs_token, paths = get_fs_token_paths(destination_folder)
    fs.mkdirs(path=destination_folder, exist_ok=True)

    # Put thumbnail into destinantion folder
    logging.info("Put thumbnail into destinantion folder")
    img_path = Path(f'{destination_folder}/{layer.title}.jpg')
    out = open(img_path, 'wb')
    out.write(img.read())
    out.close()

    data = {
        "wms-title": layer.title,
        "wms-bbox": bbox,
        "wms-img": img_path
    }
    logging.info(f"Output: {data}")
    return data


# # TEST
# if __name__ == '__main__':
#
#     get_wms_data(
#         wms_url=f"{DOMAIN}/geoserver/{WORKSPACE}/wms",
#         service_version=SERVICE_VERSION,
#         layer_name=LAYER_NAME,
#     )
