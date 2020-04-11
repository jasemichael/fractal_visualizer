from tkinter import Tk, Canvas, PhotoImage, mainloop

def draw(configs, fractalType, gradient, filename):
    """Paint a Fractal image into the TKinter PhotoImage canvas."""
    # Correlate the boundaries of the PhotoImage object to the complex
    # coordinates of the imaginary plane
    fractal = configs
    min = ((float(fractal['centerx']) - (float(fractal['axislength']) / 2.0)),
           (float(fractal['centery']) - (float(fractal['axislength']) / 2.0)))

    max = ((float(fractal['centerx']) + (float(fractal['axislength']) / 2.0)),
           (float(fractal['centery']) + (float(fractal['axislength']) / 2.0)))
    pixels = int(fractal['pixels'])
    win = Tk()
    image = PhotoImage(width=pixels, height=pixels)
    # Display the image on the screen
    canvas = Canvas(win, width=pixels, height=pixels, bg='#ffffff')
    canvas.pack()
    canvas.create_image((pixels/2, pixels/2), image=image, state="normal")
    canvas.pack()


    size = abs(max[0] - min[0]) / float(pixels)#512.0
    for r in range(pixels, 0, -1):
        for c in range(pixels):
            x = min[0] + c * size
            y = min[1] + r * size
            n = fractalType.count(fractalType, complex(x, y))
            color = gradient.getColor(gradient, n)
            image.put(color, (c, pixels - r))
        win.update()  # display a row of pixels

    # Output the Fractal into a .png image
    image.write(filename + ".png")
    print("Wrote picture " + filename + ".png")

    # Call tkinter.mainloop so the GUI remains open
    mainloop()