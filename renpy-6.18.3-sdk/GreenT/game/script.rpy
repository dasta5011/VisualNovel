# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Derek', color="#c8ffc8")
define robo = Character('Robot', color="#c8ffc8")
#character n is for narrator, and represents the characters internal monologue and scene descriptions
define n = Character(' ', color="#c8ffc8")
image bg cave = "cave.jpg"
image derek happy = "lucy_happy.png"
image derek mad = "lucy_mad.png"
image robo = "robo_default_01.png"
define slowdissolve = Dissolve(1.0)

# The game starts here.
label start:
    scene bg cave
    with slowdissolve
    play music "iron_man_01.mp3" fadeout 1
    show derek happy

    e "I'll show you my new Dotes lair, man, but so fucking help me, if you tell anyone..."
    n "Well, this should be interesting. D-Man never lets anyone see his Dotes lair."
    
    menu:
        "Yes, oh lord and master.":
            jump choice1_yes
            
        "Tweet that shit.":
            jump choice1_no
            
    label choice1_yes:
        $ menu_flag = True
        e "As long as you keep your mouth shut, you can see it."
        jump choice1_done
        
    label choice1_no:
        $ menu_flag = False    
        show derek mad at center
    e "Bitch, what the fuck did I say?  I said, don't fucking tell anyone and your bitchass busts out your iphone and you start tweetin' that shit?  Damn."
    jump choice1_done
    
    label choice1_done:
        show derek mad at center
        e "Oh shit, someone triggered PURPLE ALERT!  Let's go."
    
    scene bg cave
    show derek mad at left
    with move
    show robo at right
    
    e "I bet it's that fucker, Greg."
    show robo at offscreenright
    with move
    e "Get back here!  Gnnh..!"
    show derek mad at offscreenright
    with move
    n "And with that, Derek took off down the tunnel with a murderous look in his eyes."
    n "I wonder if there'll be cake..."
    
    jump start2

    return
