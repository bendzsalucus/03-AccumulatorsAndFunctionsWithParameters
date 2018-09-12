"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Mark Hays, Amanda Stouder,
         their colleagues and Lucus Bendzsa.
"""  # DOne: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()

def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # Done: 2. Implement this function, per its green doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.pdf  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------

    window = rg.RoseWindow(400, 400)


    center_point = rg.Point(100, 100)
    radius = 50
    circle = rg.Circle(center_point, radius)
    circle.fill_color = 'blue'
    circle.attach_to(window)

    center_point2 = rg.Point(200, 200)
    radius = 69
    circle2 = rg.Circle(center_point2, radius)
    circle2.attach_to(window)

    window.render()
    window.close_on_mouse_click()
def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """

    window = rg.RoseWindow(400, 400)
    f=100
    k=110
    p = 5
    y = 'blue'
    center_point = rg.Point(f, k)
    radius = 50
    circle = rg.Circle(center_point, radius)
    circle.fill_color = y
    circle.outline_color = 'black'
    circle.outline_thickness = p

    window = rg.RoseWindow()
    circle.attach_to(window)


    print(p)
    print(center_point)
    print(f)
    print(k)
    print(y)


    a = 200
    b = 200
    c =  300
    d = 50
    e = 5
    f = 'green'
    point1 = rg.Point(a, b)
    point2 = rg.Point(c, d)
    rectangle = rg.Rectangle(point1, point2)
    rectangle.attach_to(window)
    rectangle.outline_thickness = e
    rectangle.outline_color = f

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)


    window.render()
    window.close_on_mouse_click()
    # ------------------------------------------------------------------
    # DOne: 3. Implement this function, per its green doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------

def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # TODO: 4. Implement and test this function.

    window = rg.RoseWindow(800, 800)

    a = 100
    b = 200
    c = 90
    d = 400
    start = rg.Point(a, b)
    end = rg.Point(c, d)
    line = rg.Line(start, end)
    line.attach_to(window)
    line.thickness = 45

    midpoint1 = line.get_midpoint()

    print(midpoint1)
    print(midpoint1.x)
    print(midpoint1.y)
    a = 200
    b = 300
    c = 30
    d = 90
    start = rg.Point(a, b)
    end = rg.Point(c, d)
    line = rg.Line(start, end)
    line.attach_to(window)

    midpoint2 = line.get_midpoint()

    print(midpoint2)
    print(midpoint2.x)
    print(midpoint2.y)

    window.render()
    window.close_on_mouse_click()
# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
