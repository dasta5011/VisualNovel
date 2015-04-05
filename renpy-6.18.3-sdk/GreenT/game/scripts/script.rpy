﻿# The game starts here.
label start:
    #variables for game tracking
    #family reputation
    $ikida = 0
    $jagura = 0
    $kenshido = 0
    $maclynn = 0
    $akosnov = 0
    #keep this beginning section clean
    #used as a master jump sequences to control flow of the game
    call prologue
    call opening
    call day1_meetup
    call day1_reflection
    
    call test
    
label prologue:
    #Dramatic Music - Opening - Goes over premise of the past/ancient times and explains in little detail how the families came to be
    #blackscreen keeps transitions between music tracks from overlapping
    scene blackscreen
    with slowdissolve
    play music "audio/bgm/Virtutes_Vocis.mp3" fadeout 1.0 fadein 1.0
    $renpy.pause(0.70)
    scene caveh
    with slowdissolve    
    n "{i}Several generations ago, when this land was barren, there came to be rumors of a great power lying within the land.{/i}"
    n "{i}Following the call of the promise of untold power, it drew in people from all corners of the world.{/i}"
    n "{i}In the covers of secrecy, the peoples greatest treasures vanished.{/i}"
    n "{i}It didn't take long for feuds to break out, and before long, it turned into war.{/i}"
    n "{i}What happened in this days has been lost to history, but the consequences remain.{/i}"
    n "{i}Five lineages who fought to recover their greatest loss and to discover the unknown treasure still reside in that very land today.{/i}"
    n "{i}Only in their bloody and violent pasts can the answers be found.{/i}"
    #more to add here obviously, and refine it
    return
    
label opening:
    scene blackscreen
    with slowdissolve
    play music "audio/bgm/Schmetterling.mp3" fadeout 1.0 fadein 1.0
    $renpy.pause(0.70)
    scene storageshed
    with fastdissolve   #Trio_for_Piano_Cello_and_Clarinet.mp3
    n "Birthdays are suppose to be fun, right?"
    n "That's what I was always told."
    show blood_splat_01 at truecenter with Dissolve(0.5):
        alpha 0.1
    $renpy.pause(0.2)
    play sound "audio/sfx/heartbeat_01.ogg"
    hide blood_splat_01 at truecenter with slowdissolve
    show blood_splat_01 at truecenter with Dissolve(0.5):
        alpha 0.2 
    $renpy.pause(0.2)
    hide blood_splat_01 at truecenter with slowdissolve
    n "{color=#f00}{b}*crack* !! *smack* *slam* !!{/b}{/color}"
    n "Especially your 21st, right?"
    stop sound fadeout 0.25
    n "Am I suppose to be enjoying this?  Is this fun?"
    show blood_splat_01 at truecenter with Dissolve(0.4):
        alpha 0.3
    $renpy.pause(0.25)
    play sound "audio/sfx/heartbeat_01.ogg"
    hide blood_splat_01 at truecenter with slowdissolve
    show blood_splat_01 at truecenter with Dissolve(0.4):
        alpha 0.4
    $renpy.pause(0.25)
    hide blood_splat_01 at truecenter with slowdissolve
    n "{color=#f00}{b}*crack* *scream* !!!!!!!!!!!!!!!!!!!!!{/b}{/color}"
    n "Initiation.  Initiation is what they call it."
    stop sound fadeout 0.25
    n "{color=#f00}{b}*more screaming*{/b}{/color}"
    n "\"We're going to make a man of you today.  You get to help in the business today.  Congratulations!\""
    n "That's what they told me.  Then gave me this private shed and this snitch.  Something about leaking information to our enemies."
    show blood_splat_01 at truecenter with Dissolve(0.3):
        alpha 0.5
    $renpy.pause(0.25)
    play sound "audio/sfx/heartbeat_01.ogg"
    hide blood_splat_01 at truecenter with slowdissolve
    show blood_splat_01 at truecenter with Dissolve(0.3):
        alpha 0.6
    $renpy.pause(0.25)
    hide blood_splat_01 at truecenter with slowdissolve
    n "{color=#f00}{b}*crack* !! *smack* *slam* !!{/b}{/color}"
    n "They brought all sorts of stuff.  Guns, bats, hammers, knives, and chains were just the basics.  They had more.  Gasoline, car batteries, pliers..shit, they even had a fish tank with piranhas. But that's my family, we never skimp on an expense."
    stop sound fadeout 0.25
    n "Speaking of birthdays, aren't your friends suppose to be there to celebrate with you?"
    n "I know I don't have many, but at least one of them made it.  In fact, he's why I'm here."    
    #cut to image showing man with the shit beat out of him
    show hiro def at center
    n "Hiroshi Omura.  The snitch.  And my best friend.  It's because of me that he was in this line of work.  If he hadn't been my best friend growing up, my family never would've recruited him.  He wouldn't have snitched, and I wouldn't be here doing this to him."
    show blood_splat_01 at truecenter with Dissolve(0.2):
        alpha 0.7
    $renpy.pause(0.25)
    play sound "audio/sfx/heartbeat_01.ogg"
    hide blood_splat_01 at truecenter with slowdissolve
    show blood_splat_01 at truecenter with Dissolve(0.2):
        alpha 0.8
    $renpy.pause(0.25)
    hide blood_splat_01 at truecenter with slowdissolve
    n "{color=#f00}{b}*crack* !! *smack* *slam* !!{/b}{/color}" 
    n "This may look like I'm being a bad friend, but in reality, I'm helping him right now.  If it was anyone else taking care of this, they'd hurt him a lot worse and make sure he didn't survive.  I really hope he understands I'm doing this for him."
    stop sound fadeout 0.25
    n "..."
    n "He's crying.  How pitiful.  By my calculations, this will have to continue for another ten minutes before everyone is satisfied."
    show blood_splat_01 at truecenter with Dissolve(0.1):
        alpha 0.9
    $renpy.pause(0.25)
    play sound "audio/sfx/heartbeat_01.ogg"
    hide blood_splat_01 at truecenter with slowdissolve
    show blood_splat_01 at truecenter with Dissolve(0.1):
        alpha 1.0
    $renpy.pause(0.25)
    hide blood_splat_01 at truecenter with slowdissolve
    n "{color=#f00}{b}*crack* !! *smack* *slam* !!{/b}{/color}"
    n "He's still crying.  I wonder if he'd laugh if I told him I envied him."
    n "I haven't been able to cry for eleven years as of today.  Not since that day."
    stop sound fadeout 0.25
    n "Anyway...I hope this is over soon.  It'd be a shame if this was the highlight of my birthday."    
    return
    
label day1_meetup:
    scene blackscreen with slowdissolve
    play music "audio/bgm/easy_lemon.ogg" fadeout 1.0 fadein 1.0
    $renpy.pause(0.70)
    scene sidewalk1 with slowdissolve    
    n "That incident was over three hours ago, but I still feel sick."
    n "At the time I was so focused on doing what I had to do that I didn't notice, but I've thrown up three times after it has sunk in."
    n "That was Hiroshi. And I nearly killed him."
    n "I know I broke at least a bone or two. The sound of it cracking still rings in my ears."
    n "I'm sweating. I feel cold. My breathing is off."
    n "I can't think about this anymore. I need a distraction."
    mayu "I told you that was Koji. Hey! Hey, Koji!"
    n "The blood washed off well enough, but there was so much...it felt like too much."
    n "No, I need to stop this. I just need to focus on the positive. Hiroshi is alive. Hiroshi is alive because of me."
    show mayu def at center
    mayu "Kooooooo-Jiiiiiiii."
    n "Lost in my own head, I nearly crashed right into someone who had just run in front of me."
    koji "Mayu! Where did you come from?"
    mayu "Are you ok, Koji? You look pale. And you totally ignored me while we were trying to get your attention!"
    koji "\"We?\""
    show mayu smile1 at center with moveinbottom
    $renpy.pause(0.15)
    show kaori def at left with moveinleft
    $renpy.pause(0.25)
    show toshi def at right with moveinright
    mayu "Kaori and Toshi wanted to come get food over here, then we saw you on our way."
    show mayu def at center
    mayu "So, will you join us or will we have to drag you by force?"
    
    return

label day1_reflection:
    scene blackscreen with slowdissolve
    play music "audio/bgm/mourning_song.ogg" fadeout 1.0 fadein 1.0
    $renpy.pause(0.70)
    scene ikidahome with slowdissolve
    show aido def at center
    aido "I heard you did an incomplete job of dealing with your gift, Koji."
    koji "I thought I was able to treat my {i}presents{/i} however I wanted?"
    show aido dis
    aido "That boy may have just well ruined the peaceful life I've built you, and after all these years of keeping you off the radar."
    koji "That may be, grandfather.  But, what's done is done, and killing him would have only caused more trouble for you, the family, and myself."
    aido "Hmmf."
    koji "And besides, I'd like to keep him as a friend...if he ever comes back to school that is."
    aido "Koji, you're free to have your own friends, but do keep them away from the house, will you? I'd hate having to talk to the police about missing persons."
    return
    
    #all test after this    
label test:
    show derek happy
    e "I'll show you my new Dotes lair, man, but so fucking help me, if you tell anyone..."
    n "you have [ikida] ikida point. test."
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
    show hiro def at right
    
    e "I bet it's that fucker, Greg."
    show hiro def at offscreenright
    with move
    e "Get back here!  Gnnh..!"
    show derek mad at offscreenright
    with move
    n "And with that, Derek took off down the tunnel with a murderous look in his eyes."
    n "I wonder if there'll be cake..."

    return
