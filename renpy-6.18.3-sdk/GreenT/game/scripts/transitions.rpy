#Transitions
define slowdissolve = Dissolve(2.0)
define fastdissolve = Dissolve(0.25)
##BECAUSE I KEEP TYPING IT
define quickdissolve = Dissolve(0.25)
define meddissolve = Dissolve(1.0)

#timing = seconds for transition, x and y are 0-1 coordinates on screen to be placed
transform mymoveinleft(timing, x, y):
    parallel:
        xanchor 0.5 yanchor 1.0 ypos 1.0 xpos -0.5
        linear timing xpos x ypos y
    parallel:
        alpha 0.0
        linear timing alpha 1.0
    
transform mymoveinright(timing, x, y):
    parallel:
        xanchor 0.5 yanchor 1.0 ypos 1.0 xpos 1.5
        linear timing xpos x ypos y
    parallel:
        alpha 0.0
        linear timing alpha 1.0
        
#fade to black and back
define fade = Fade(0.75, 0.25, 0.75)

##important, make sure to use floats. 1.0, 0.0, etc. Not 1 or 0.
transform setloc(x,y):
    xanchor 0.5 yanchor 1.0 ypos y xpos x
    
transform alphacon(alphac, x, y):
    xanchor 0.5 yanchor 1.0 alpha alphac xpos x ypos y