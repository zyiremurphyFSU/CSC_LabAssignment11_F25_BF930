# TODO: complete the function definition in the next line
def rectangle_info():
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

    # TODO: return three calculated variables


if __name__ == "__main__":
    w = float(input("Enter width: "))
    h = float(input("Enter height: "))

    # TODO: call function rectangle_info() and pass two arguments: w and h.
    print(f"Area: {rect_a}, Perimeter: {rect_p}, Diagonal: {rect_d}")
