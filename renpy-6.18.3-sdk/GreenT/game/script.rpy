# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Derek', color="#c8ffc8")
image bg cave = "cave.jpg"
image derek happy = "lucy_happy.png"
image derek mad = "lucy_mad.png"
define slowdissolve = Dissolve(1.0)

# The game starts here.
label start:
    scene bg cave
    with slowdissolve
    show derek happy

    e "I'll show you my new Dotes lair, man, but so fucking help me, if you tell anyone..."
    show derek mad at right

    e "Bitch, what the fuck did I say?  I said, don't fucking tell anyone and your bitchass busts out your iphone and you start tweetin' that shit?  Damn."
    
    scene bg cave
    with slowdissolve
    show derek happy at left
    
    e "Well, I'll forgive you this time..Since you're a scrub and all."

    return
