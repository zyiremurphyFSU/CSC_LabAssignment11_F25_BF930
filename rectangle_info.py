def rectangle_info(width, height):
    """
    Calculate area, perimeter, and diagonal of a rectangle.

    @param width (float): Width of the rectangle.
    @param height (float): Height of the rectangle.

    @return
        area (float) - The area of the rectangle.
        perimeter (float) - The perimeter of the rectangle.
        diagonal (float) - The length of the diagonal.
    """
    area = width * height
    perimeter = 2 * (width + height)
    diagonal = (width**2 + height**2) ** 0.5

    return area, perimeter, diagonal


if __name__ == "__main__":
    w = float(input("Enter width: "))
    h = float(input("Enter height: "))

    rect_a, rect_p, rect_d = rectangle_info (w, h)
    print(f"Area: {rect_a}, Perimeter: {rect_p}, Diagonal: {rect_d}")
