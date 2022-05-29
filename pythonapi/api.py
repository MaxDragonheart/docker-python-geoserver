from owslib.wms import WebMapService


def get_wms_data(
        wms_url: str,
        service_version: str,
        layer_name: str,
        srs: str = 'EPSG:4326',
        width: int = 300,
        high: int = 300,
):
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
        pathlib.PosixPath
    """
    # Read WMS
    wms = WebMapService(url=wms_url, version=service_version)

    # Get bounding box from selected layer
    layer = wms[layer_name]
    title = layer.title
    bbox = layer.boundingBoxWGS84

    # Create thumbnail
    img = wms.getmap(
        layers=[layer_name],
        #styles=[styles],
        srs=srs,
        bbox=bbox,
        size=(width, high),
        format='image/jpeg',
        transparent=True
    )

    data = {
        "wms-title": title,
        "wms-bbox": bbox,
        "wms-img": img
    }
    print(data)