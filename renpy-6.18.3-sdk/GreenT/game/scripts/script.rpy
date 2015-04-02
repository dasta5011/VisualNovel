# Declare characters used by this game.
#character n is for narrator, and represents the characters internal monologue and scene descriptions
define n = Character(' ', color="#c8ffc8")

##tests delete characters after this
define e = Character('Derek', color="#c8ffc8")
define robo = Character('Robot', color="#c8ffc8")

#define images
image blackscreen = "#000000"
image bg caveh = "images/backgrounds/cave_hallway.png"
image storageshed = "images/backgrounds/storage_shed.png"
#images below this are test
image bg cave = "images/backgrounds/cave.jpg"
image derek happy = "images/characters/lucy_happy.png"
image derek mad = "images/characters/lucy_mad.png"
image robo = "images/characters/robo_default_01.png"

#Transitions
define slowdissolve = Dissolve(1.0)
define fastdissolve = Dissolve(0.25)

# The game starts here.
label start:
    #keep this beginning section clean
    #used as a master jump sequences to control flow of the game
    call prologue
    call opening
    
    label prologue:
    #Dramatic Music - Opening - Goes over premise of the past/ancient times and explains in little detail how the families came to be
    #blackscreen keeps transitions between music tracks from overlapping
    scene blackscreen
    with slowdissolve
    play music "audio/bgm/Virtutes_Vocis.mp3" fadeout 1.0 fadein 1.0
    $ renpy.pause(0.70)
    scene bg caveh
    with slowdissolve
    
    n "{i}Several generations ago, when this land was barren, there came to be rumors of a great power lying within the land.{/i}"
    n "{i}It didn't take long for feuds to break out, and before long, it turned into war.{/i}"
    n "{i}What happened in this days has been lost to history, but the consequences remain.{/i}"
    n "{i}Five lineages who fought to discover the treasure still reside in that very land today.{/i}"
    n "{i}Only in their dark and cloudy pasts can the answers be found.{/i}"
    
    #more to add here obviously, and refine it
    return
    
    label opening:
    scene blackscreen
    with slowdissolve
    play music "audio/bgm/Schmetterling.mp3" fadeout 1.0 fadein 1.0
    $ renpy.pause(0.70)
    scene storageshed
    with fastdissolve   #Trio_for_Piano_Cello_and_Clarinet.mp3
    n "Birthdays are suppose to be fun, right?"
    n "That's what I was always told."
    n "{color=#f00}{b}*crack* !! *smack* *slam* !!{/b}{/color}"
    n "Especially your 21st, right?"
    n "Am I suppose to be enjoying this?  Is this fun?"
    n "{color=#f00}{b}*crack* *scream* !!!!!!!!!!!!!!!!!!!!!{/b}{/color}"
    n "Initiation.  Initiation is what they call it."
    n "{color=#f00}{b}*more screaming*{/b}{/color}"
    n "\"We're going to make a man of you today.  You get to help in the business today.  Congratulations!\""
    n "That's what they told me.  Then gave me this private shed and this snitch.  Something about leaking information to our enemies."
    n "{color=#f00}{b}*crack* !! *smack* *slam* !!{/b}{/color}"
    n "They brought all sorts of stuff.  Guns, bats, hammers, knives, and chains were just the basics.  They had more.  Gasoline, car batteries, pliers..shit, they even had a fish tank with piranhas. But that's my family, we never skimp on an expense."
    n "Speaking of birthdays, aren't your friends suppose to be there to celebrate with you?"
    n "I know I don't have many, but at least one of them made it.  In fact, he's why I'm here."    
    #cut to image showing man with the shit beat out of him
    show robo at center    
    #add name
    n "<friends name>.  The snitch.  And my best friend.  It's because of me that he was in this line of work.  If he hadn't been my best friend growing up, my family never would've recruited him.  He wouldn't have snitched, and I wouldn't be here doing this to him."
    n "{color=#f00}{b}*crack* !! *smack* *slam* !!{/b}{/color}" 
    n "This may look like I'm being a bad friend, but in reality, I'm helping him right now.  If it was anyone else taking care of this, they'd hurt him a lot worse and make sure he didn't survive.  I really hope he understands I'm doing this for him."
    n "..."
    n "He's crying.  How pitiful.  By my calculations, this will have to continue for another ten minutes before everyone is satisfied."
    n "{color=#f00}{b}*crack* !! *smack* *slam* !!{/b}{/color}"
    n "He's still crying.  I wonder if he'd laugh if I told him I envied him."
    n "I haven't been able to cry for eleven years as of today.  Not since that day."
    n "Anyway...I hope this is over soon.  It'd be a shame if this was the highlight of my birthday."    
    
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
    with slowdissolve
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
