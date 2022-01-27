from PIL import Image


WIDTH = 1000
HEIGHT = 1000
SIZE = (WIDTH, HEIGHT)
MODE = "RGB"


def mandelbrot_iterations(c: complex, z=None, depth: int=None) -> int:
    """Returns the number of iterations until the absolute value of the complex number z
    is higher than two. If this doesn't happen it will automatically stop at 100 iterations.
    
    To calculate the new z's the function uses the logic of the mangelbrot set."""

    if z is None:
        z = 0+0j
    if depth is None:
        depth = 0

    if abs(z) > 2:  # complex number isn't part of the mandelbrot set
        return depth
    
    if depth >= 100:  # complex number is part of the mandelbrot set
        return 100

    new_z = z**2 + c
    return mandelbrot_iterations(c, new_z, depth+1)
    
def mandelbrot_set(img: Image, width: int, height: int) -> None:
    """Makes the given img an image of the mandelbrot set."""

    for x in range(width):
        for y in range(height):
            a = 4*(x/width) - 2
            b = (4*(y/height) - 2)*(-1j)
            
            n = mandelbrot_iterations(a+b)
            
            if n > 50:
                color = (255-2*n, 255-2*n, 255)
            else:
                color = (255-5*n, 255-5*n, 255)

            if n == 100:
                color = (0, 0, 0)

            img.putpixel((x, y), color)



if __name__ == "__main__":
    img = Image.new(MODE, SIZE, (50, 50, 50))

    mandelbrot_set(img, WIDTH, HEIGHT)

    img.save("mandelbrot.png")