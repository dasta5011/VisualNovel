##Use this for dicking around and testing

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