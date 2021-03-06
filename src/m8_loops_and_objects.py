"""
This module demonstrates simple LOOPS of the form:
   for k in range(blah):
      ... k ...

and also USING OBJECTS.

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Mark Hays, Amanda Stouder,
         their colleagues and Lucus Bendzsa.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    print_sequence1(21)
    draw_circles1(20)
    print_sequence2(18)
    draw_circles2(20)
    print_sequence3(100)
    draw_circles3(100)
    print_cosines(100)
    draw_cosines_and_sines(100)

def print_sequence1(x):
    """
    Prints:
       0
       10
       20
       30
       40
       ...
       200
    """
    for k in range(x):
        x = (x+10)
        print(x-31)
    # ------------------------------------------------------------------
    # Done: 2. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running print_sequence1:')
    print('--------------------------------------------------')


def draw_circles1(x):
    """
    -- Constructs an rg.RoseWindow whose width and height are both 400.
    -- Constructs and draws 21 rg.Circle objects such that:
         -- Each is centered at (200, 200)
    #          -- They have radii:  0  10  20  30  40 ... 200, respectively.
    #     -- Waits for the user to press the mouse, then closes the window.
    #     """
    #     # ------------------------------------------------------------------
    #     # Done: 3. Implement this function, per its doc-string above.
    #     # Put a statement in  main  to test this function.
    #     # REQUIREMENT: You must use a   RANGE statement to solve this problem.

    window = rg.RoseWindow(1000, 1000)

    for k in range(x):
        center_point = rg.Point(200, 100)
        radius = 200-(k*10)
        circle = rg.Circle(center_point, radius)
        circle.attach_to(window)
    window.render()

    window.close_on_mouse_click()


    print()
    print('--------------------------------------------------')
    print('Running draw_circles1:  See graphics window')
    print('--------------------------------------------------')


def print_sequence2(x):
    """
    Prints:
      50
      70
      90
      110
      130
      ...
      390.
    """
    # ------------------------------------------------------------------
    # Done: 4. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running print_sequence2:')
    print('--------------------------------------------------')

    for k in range(x):
        x = (x+20)
        print(x +12)



def draw_circles2(x):
    """
    -- Constructs an rg.RoseWindow whose width and height are both 400.
    -- Constructs and draws rg.Circle objects such that:
         -- Each has radius 10.
         -- Each has fill_color 'blue'.
         -- They are centered at, respectively:
               (50, 100)   (70, 100)   (90, 100)  (110, 100) ... (390, 100)
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # Done: 5. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running draw_circles2:  See graphics window')
    print('--------------------------------------------------')

    window = rg.RoseWindow(400, 400)

    for k in range(x):
        p = 50 + (20*k)
        center_point = rg.Point(p, 100)
        radius = 10
        circle = rg.Circle(center_point, radius)
        circle.fill_color = 'blue'
        circle.attach_to(window)
    window.render()

    window.close_on_mouse_click()

def print_sequence3(x):
    """
    Prints:
      1
      2
      3 
      4
      ...
      100.
    """
    # ------------------------------------------------------------------
    # Done: 6. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running print_sequence3:')
    print('--------------------------------------------------')
    for k in range(x):
        print(k + 1)


def draw_circles3(x):
    """
    -- Constructs an rg.RoseWindow whose width and height are both 300.
    -- Constructs and draws 100 rg.Circle objects such that:
         -- Each is centered at (200, 150)
         -- They have radii:  1  2  3  4  ... 100, respectively.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # Done: 7. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running draw_circles3:  See graphics window')
    print('--------------------------------------------------')

    window = rg.RoseWindow(300, 300)

    for k in range(x):
        center_point = rg.Point(200, 150)
        radius = (k+1)
        circle = rg.Circle(center_point, radius)
        circle.attach_to(window)
    window.render()

    window.close_on_mouse_click()

def print_cosines(x):
    """
    For each of the integers 0  1  2  ... 100,
    prints 80 times the cosine of that integer.
    Thus, the numbers printed should be about:
       80.0
       43.224184469451174
       -33.29174692377139
       -79.19939972803563
       -52.29148966908895
       22.6929748370581
       76.81362293202928
       60.31218034746437
         ...
       -65.54305962331674
       3.185670431451112
       68.9855097830147
    """
    # ------------------------------------------------------------------
    # Done: 8. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    #
    # HINT: You need to   import math   at the top of this file
    #       to use math functions like the ones for cosine and sine.
    #       Once you have that import in place, typing
    #            math.
    #       (note the DOT) and pausing will display options that make
    #       it plain what the notation for the cosine function is.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running print_cosines:')
    print('--------------------------------------------------')
    import math
    for k in range(x):
        a= math.cos(k+1)
        b=(a*80)
        print(b)


def draw_cosines_and_sines(x):
    """
    -- Constructs a window whose width and height are both 400.
    -- Constructs and draws rg.Circle objects such that:
         -- Each has radius 10.
         -- They are centered at, respectively:
               ( 200 + (80 * cos(0)), 200 + (80 * sin(0) )
               ( 200 + (80 * cos(1)), 200 + (80 * sin(1) )
               ( 200 + (80 * cos(2)), 200 + (80 * sin(2) )
               ( 200 + (80 * cos(3)), 200 + (80 * sin(3) )
                   ...
               ( 200 + (80 * cos(100)), 200 + (80 * sin(100) )
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # TODO: 9. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running draw_cosines_and_sines:  See graphics window')
    print('--------------------------------------------------')


    window = rg.RoseWindow(400, 400)
    import math
    for k in range(x):
        p = 200 + (80 * math.cos(k+1))
        l = 200 + (80 * math.sin(k+1))
        center_point = rg.Point(p, l)
        radius = 10
        circle = rg.Circle(center_point, radius)
        circle.fill_color = 'blue'
        circle.attach_to(window)

    window.render()

    window.close_on_mouse_click()
# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
