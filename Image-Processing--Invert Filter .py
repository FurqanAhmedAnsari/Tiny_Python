import struct
import turtle

with open(r"C:\Users\khush\OneDrive\Desktop\Furqan Python\Image Processing Sample.BMP", "rb") as f:
    f.seek(10)
    
    # bytes where Pixel start.
    pixelOffsetInBytes = f.read(4)
    pixelOffsetInInt = struct.unpack("i", pixelOffsetInBytes)[0]
    print(f"Pixel Offset is ={pixelOffsetInInt}")
    
    f.seek(18)
    # Width and Height.
    w = f.read(4)
    h = f.read(4)
    width = struct.unpack("i", w)[0]
    height = struct.unpack("i", h)[0]
    print(f"Image width ={width}")
    print(f"Image height ={height}")
    
    # Turtle Steup.
    tr = turtle.Turtle()
    sc = turtle.Screen()
    sc.setup(width*4, height*4)
    turtle.colormode(255)
    turtle.title("Invert Filter")
    turtle.tracer(0, 0)
    
    # Start reading pixels.
    f.seek(pixelOffsetInInt, 0)
    for rr in range(0, width):
        for cc in range(0, height):
            r = f.read(1)[0]
            g = f.read(1)[0]
            b = f.read(1)[0]
            tr.setpos(rr, cc)
            # invert Filter.
            r = 255 - r
            g = 255 - g
            b = 255 - b
            tr.color(r, g, b)
            tr.dot()
    turtle.update()    
    turtle.done()    