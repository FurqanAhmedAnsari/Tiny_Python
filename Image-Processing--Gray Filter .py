import struct
import turtle

with open(r"C:\Users\khush\OneDrive\Desktop\Furqan Python\Image Processing Sample.BMP","rb") as f:

    # First two Signature Bytes.
    b=f.read(1)
    m=f.read(1)
    print ("SignatureB =",b)
    print ("SignatureM =",m)

    # File Size in next four Bytes, then converted into integers. 
    fSize=f.read(4)
    fileSizeInInt=struct.unpack("i",fSize)[0]
    print ("Size of the File =",fileSizeInInt)

    # Next four unUsed Bytes.
    f.read(4)

    # Bytes from where pixels start.
    po = f.read(4)
    pixelOffset = struct.unpack("i",po)[0]

    # Four another unUsed Bytes.
    f.read(4)

    # if you want to skip all above lines. 
    f.seek(18,0)
    # image Width and Height.
    w = f.read(4)
    width = struct.unpack("i",w)[0]
    print ("Width of image=",width)
    h = f.read(4)
    height = struct.unpack("i",h)[0]
    print ("Height of image=",height)

    # Turtle Srtup.
    tr=turtle.Turtle()
    sc=turtle.Screen()
    sc.setup(width*4, height*4)
    sc.colormode(255)
    turtle.title ("Gray Filter")
    turtle.tracer(0, 0)

    # Start reading pixels.
    f.seek(pixelOffset,0)
    for rr in range(0,height,1):
        for cc in range(0,width,1):
            b=f.read(1)[0]
            g=f.read(1)[0]
            r=f.read(1)[0]
            # b =b[0]
            # g = g[0]
            # r = r[0]
            tr.setpos(rr, cc)
            # Low level Module (Gray Scale)
            gr = ( b + g + r) // 3
            tr.color(gr,gr,gr)
            tr.dot()

    turtle.update()
    turtle.done()