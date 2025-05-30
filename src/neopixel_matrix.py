def xy_to_index(
        x: int,
        y: int,
        width: int      = 32,
        height: int     = 16,
        zigzag: bool    = True,
        row_major: bool = True,
        flip_x: bool    = False,
        flip_y: bool    = False
    ) -> int:
    """
    Convert (x, y) coordinate to NeoPixel index for a 32x16 matrix with zigzag wiring.

    Args:
        x (int): X coordinate (0 to width-1).
        y (int): Y coordinate (0 to height-1).
        width (int): Matrix width. Default is 32.
        height (int): Matrix height. Default is 16.
        zigzag (bool): True if wired in zigzag, False if wired in progressive. Defaults to True.
        row_major(bool): True if wired row by row, False if wired column by column. Defaults to True.

    Returns:
        int: The NeoPixel index (0-based).
    """
    
    if x < 0 or x >= width or y < 0 or y >= height:
        raise ValueError("x or y is out of bounds")

    if flip_x:
        x = width - 1 - x
    if flip_y:
        y = height - 1 - y

    if row_major:
        if zigzag:
            if y % 2 == 0:
                # Even rows go left to right
                return y * width + x
            else:
                # Odd rows go right to left
                return y * width + (width - 1 - x)
        else:
            return y * width + x
    else:
        if zigzag:
            if x % 2 == 0:
                return x * height + y
            else:
                return x * height + (height - 1 - y)
        else:
            return x * height + y

def xy_to_lonlat(x, y, width=32, height=16):
    """
    Converts x, y coordinates in an arbitrary range (0 to x_max, 0 to y_max)
    to longitude and latitude using the Plate Carrée projection.

    Parameters:
        x (float or array-like): x-coordinate(s) in the range [0, x_max]
        y (float or array-like): y-coordinate(s) in the range [0, y_max]
        x_max (float): maximum value of x (corresponds to longitude 180°)
        y_max (float): maximum value of y (corresponds to latitude 90°)

    Returns:
        tuple: (longitude, latitude)
    """
    # Normalize x and y to [0, 1]
    x_norm = x / width
    y_norm = y / height

    # Map to longitude [-180, 180] and latitude [-90, 90]
    lon = x_norm * 360.0 - 180.0
    lat = y_norm * 180.0 - 90.0

    return lon, lat