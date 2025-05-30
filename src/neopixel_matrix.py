def xy_to_index(x: int, y: int, width: int=32, height: int=16, zigzag: bool=True, row_major: bool=True) -> int:
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
    
    # Accept negative y values for convenience
    y = abs(y)

    if x < 0 or x >= width or y >= height:
        raise ValueError("x or y is out of bounds")

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