# Coding Club Person Screensaver

## Ben Raz | 2022

### Instructions

To configure the animation go to `Scene.py` and change the `presenter` variable to the name of the presenter whose presentation screensaver you want to render.

Additionally, you can change the `font` variable to any font installed on your computer and it *should* work. (I didn't make ManimPango)

#### Rendering the Animation

To render the animation, open up the command line and install ManimCE (instructions on docs.manim.community). After that, write `manim -pqk Scene.py` into the directory containing the file. After that, the animation will automatically open. 

If you want to open the file yourself, just write `manim -qk Scene.py`. Additionally, you do not have to render the file at 4K resolution. You can use `manim -(p)q[l,m,h,k] Scene.py` (low, medium, high, and 4K respectively), to render at differnet qualities. 
