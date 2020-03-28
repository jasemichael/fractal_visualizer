from tkinter import Tk, Canvas, PhotoImage, mainloop
import Julia, Mandelbrot

def draw(configs, config, fractalType, gradient):
    """Paint a Fractal image into the TKinter PhotoImage canvas.
    Assumes the image is 512x512 pixels."""
    # Correlate the boundaries of the PhotoImage object to the complex
    # coordinates of the imaginary plane
    fractal = configs[config]
    min = ((fractal['centerX'] - (fractal['axisLength'] / 2.0)),
           (fractal['centerY'] - (fractal['axisLength'] / 2.0)))

    max = ((fractal['centerX'] + (fractal['axisLength'] / 2.0)),
           (fractal['centerY'] + (fractal['axisLength'] / 2.0)))

    win = Tk()
    image = PhotoImage(width=512, height=512)
    # Display the image on the screen
    canvas = Canvas(win, width=512, height=512, bg='#ffffff')
    canvas.pack()
    canvas.create_image((256, 256), image=image, state="normal")
    canvas.pack()


    size = abs(max[0] - min[0]) / 512.0

    for r in range(512, 0, -1):
        for c in range(512):
            x = min[0] + c * size
            y = min[1] + r * size
            if fractalType == 'julia':
                color = Julia.getJuliaPixelColor(complex(x, y), gradient)
            elif fractalType == 'mandelbrot':
                color = Mandelbrot.getMandelbrotPixelColor(complex(x, y), gradient)
            image.put(color, (c, 512 - r))
        win.update()  # display a row of pixels

    # Output the Fractal into a .png image
    image.write(config + ".png")
    print("Wrote picture " + config + ".png")

    # Call tkinter.mainloop so the GUI remains open
    mainloop()