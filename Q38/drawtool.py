# drawtool.py:

# drawtool.py
#
# Simplified tools for drawing via Matplotlib and Tkinter
# Also has image features: reading, conversions, pixels
# Needs: matplotlib, tkinter, PIL, numpy
#
# Author: Marcus G. Young and Rahul Simha (June 2020)
# Edited: Samuel Gassman (July 2020)

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.patches import Rectangle
import numpy as np
import tkinter as tk
import time
import os
from PIL import Image, ImageTk


class DrawTool:
    xMin = 0
    xMax = 10
    yMin = 0
    yMax = 10
    a = 0
    p_size = 35
    draw_color = 'b'
    angle = 0
    axis_str = 'on'

    def __init__(self):
        self.a = plt.subplot(111, aspect='auto')
        plt.xlim(0, 10)
        plt.ylim(0, 10)

    def set_aspect(self, aspect='auto'):
        self.a.set_aspect(aspect)

    def display(self):
        plt.xlim(self.xMin, self.xMax)
        plt.ylim(self.yMin, self.yMax)
        plt.axis(self.axis_str)
        plt.show()

    def set_XY_range(self, xMin, xMax, yMin, yMax):
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax

        # Availabile Colors:
        #       'b' : blue.
        #       'g' : green.
        #       'r' : red.
        #       'c' : cyan.
        #       'm' : magenta.
        #       'y' : yellow.
        #       'k' : black.
        #       'w' : white.

    def set_color(self, color):
        self.draw_color = color

    def set_color_rgb(self, r, g, b):
        self.draw_color = (r, g, b)

    def draw_point(self, x, y, size=1.0):
        dot_size = int(self.p_size * size)
        plt.scatter(x, y, s=dot_size, c=self.draw_color)

    def draw_line(self, x1, y1, x2, y2):
        plt.plot((x1, x2), (y1, y2), self.draw_color)

    def draw_arrow(self, x1, y1, x2, y2):
        hw = (.025 * self.xMax)
        hl = (.025 * self.yMax)
        plt.arrow(x1, y1, x2, y2, head_width=hw,
                  head_length=hl, color=self.draw_color)

    def draw_ellipse(self, x, y, width, height):
        e = Ellipse((x, y), width, height, self.angle,
                    color=self.draw_color, fill=False)
        e.set_clip_box(self.a.bbox)
        self.a.add_artist(e)

    def draw_filled_ellipse(self, x, y, width, height):
        e = Ellipse((x, y), width, height, self.angle,
                    color=self.draw_color, fill=True)
        e.set_clip_box(self.a.bbox)
        self.a.add_artist(e)

    def draw_circle(self, x, y, radius):
        self.draw_ellipse(x, y, 2*radius, 2*radius)

    def draw_filled_circle(self, x, y, radius):
        self.draw_filled_ellipse(x, y, 2*radius, 2*radius)

    def draw_rectangle(self, x, y, width, height):
        r = Rectangle((x, y), width, height, self.angle,
                      color=self.draw_color, fill=False)
        r.set_clip_box(self.a.bbox)
        self.a.add_artist(r)

    def draw_filled_rectangle(self, x, y, width, height):
        r = Rectangle((x, y), width, height, self.angle,
                      color=self.draw_color, fill=True)
        r.set_clip_box(self.a.bbox)
        self.a.add_artist(r)

    def draw_curve_as_points(self, x, y):
        if len(x) == len(y):
            plt.scatter(x, y, s=self.p_size, c=self.draw_color)
        else:
            print(
                'draw_curve_as_points error: List length of X and Y values must be equal')

    def draw_curve_as_lines(self, x, y):
        if len(x) == len(y):
            for i in range(0, len(x)):
                plt.plot(x[i:i+2], y[i:i+2], self.draw_color)
        else:
            print('draw_curve_as_lines: List length of X and Y values must be equal')

    def draw_curve(self, x, y):
        if len(x) == len(y):
            for i in range(0, len(x)):
                plt.scatter(x[i], y[i], s=self.p_size, c=self.draw_color)
                plt.plot(x[i:i+2], y[i:i+2], self.draw_color)
        else:
            print('draw_curve_as_lines: List length of X and Y values must be equal')

    def draw_text(self, x, y, text_str, fontsizeint=12):
        plt.text(x, y, text_str, fontsize=fontsizeint, color=self.draw_color)

    def set_axes_on(self):
        self.axis_str = 'on'

    def set_axes_off(self):
        self.axis_str = 'off'

    ###############################################################

    def to_int_pixels(self, pixels_u):
        # Default is 'uint8' so convert to int.
        return pixels_u.astype('int')

    def to_uint8_pixels(self, pixels):
        # Default is 'uint8' so convert to int.
        return pixels.astype('uint8')

    def read_imagefile(self, filename):
        pixels_u = np.array(Image.open(filename))
        return self.to_int_pixels(pixels_u)

    def read_greyimagefile(self, filename):
        pixels = self.read_imagefile(filename)
        return self.to_greypixels(pixels)

    def draw_fitted_image(self, pixels, x, y, width, height):
        pixels_u = self.to_uint8_pixels(pixels)
        img = Image.fromarray(pixels_u)
        plt.imshow(img, origin='upper', extent=(x, x+width, y, y+height))

    def draw_image(self, pixels):
        # Fit to whichever is less.
        pixels_u = self.to_uint8_pixels(pixels)
        img = Image.fromarray(pixels_u)
        num_rows = pixels_u.shape[0]
        num_cols = pixels_u.shape[1]
        xscale = num_cols / (self.xMax - self.xMin)
        yscale = num_rows / (self.yMax - self.yMin)
        scale = max(xscale, yscale)
        w = num_cols / scale
        h = num_rows / scale
        plt.axis(self.axis_str)
        plt.imshow(img, origin='upper', extent=(
            self.xMin, self.xMin + w, self.yMin, self.yMin + h))

    def draw_fitted_greyimage(self, pixels, x, y, width, height):
        self.draw_image(self.to_colorpixels(pixels, x, y, width, height))

    def draw_greyimage(self, pixels):
        self.draw_image(self.to_colorpixels(pixels))

    def show_image_separate(self, pixels):
        # Separate window
        pixels_u = self.to_uint8_pixels(pixels)
        img = Image.fromarray(pixels_u)
        img.show()

    def show_greyimage_separate(self, pixels):
        # Separate window
        self.show_image_separate(self.to_colorpixels(pixels))

    def save_image(self, pixels, filename):
        pixels_u = self.to_uint8_pixels(pixels)
        img = Image.fromarray(pixels_u)
        img.save(filename)

    def save_greyimage(self, greypixels, filename):
        self.save_image(self.to_colorpixels(greypixels), filename)

    def to_greypixels(self, pixels):
        greypixels = np.zeros((pixels.shape[0], pixels.shape[1]), dtype='int')
        for i in range(pixels.shape[0]):
            for j in range(pixels.shape[1]):
                #greyval = int( ( np.int(pixels[i,j,0]) + np.int(pixels[i,j,1]) + np.int(pixels[i,j,2]) ) / 3 )
                greyval = int(
                    (pixels[i, j, 0] + pixels[i, j, 1] + pixels[i, j, 2]) / 3)
                greypixels[i, j] = greyval
        return greypixels

    def to_colorpixels(self, greypixels):
        pixels = np.zeros(
            (greypixels.shape[0], greypixels.shape[1], 3), dtype='int')
        for i in range(pixels.shape[0]):
            for j in range(pixels.shape[1]):
                pixels[i, j, 0] = greypixels[i, j]
                pixels[i, j, 1] = greypixels[i, j]
                pixels[i, j, 2] = greypixels[i, j]
        return pixels

    def make_greypixel_array(self, nrows, ncols):
        greypixels = np.zeros((nrows, ncols), dtype='int')
        return greypixels

    def make_pixel_array(self, nrows, ncols):
        pixels = np.zeros((nrows, ncols, 3), dtype='int')
        return pixels
