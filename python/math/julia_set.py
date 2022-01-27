from PIL import Image


WIDTH = 1000
HEIGHT = 1000
SIZE = (WIDTH, HEIGHT)
MODE = "RGB"


def julia_iterations(z: complex, c: complex | int, depth=None) -> int:
    
    if depth is None:
        depth = 0

    if abs(z) > 2:
        return depth
    if depth >= 100:
        return 100

    new_z = z**2 + c
    return julia_iterations(new_z, c, depth+1)

def julia_set(img: Image, width: int, height: int, c: complex | int):
    
    for x in range(width):
        for y in range(height):
            a = 4*(x/width) - 2
            b = (4*(y/height)-2)*(-1j)

            n = julia_iterations(a+b, c)

            if n > 50:
                color = (255-2*n, 255-2*n, 255)
            else:
                color = (255-5*n, 255-5*n, 255)

            if n == 100:
                color = (0, 0, 0)

            img.putpixel((x, y), color)


if __name__ == "__main__":
    img = Image.new(MODE, SIZE, (50, 50, 50))
    
    julia_set(img, WIDTH, HEIGHT, -1+0.25j)

    img.save("julia_set.png")