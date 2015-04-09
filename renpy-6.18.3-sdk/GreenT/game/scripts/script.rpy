﻿# The game starts here.
label start:
    #variables for game tracking
    #family reputation
    $ikida = 0
    $jagura = 0
    $kenshido = 0
    $maclynn = 0
    $akosnov = 0
    $gameover = False
    #keep this beginning section clean ## used as a master jump sequences to control flow of the game
    window show #keeps text window from hiding during transitions
    call prologue
    call opening
    call day1_meetup
    
    call day1_gunshop
    #returns to main menu if gameover condition variable is set
    if gameover:
        return
    call day1_reflection
    
    call test
    
label prologue:
    #Dramatic Music - Opening - Goes over premise of the past/ancient times and explains in little detail how the families came to be
    #blackscreen keeps transitions between music tracks from overlapping
    play music "audio/bgm/Virtutes_Vocis.mp3" fadeout 1.0 fadein 1.0
    scene blackscreen with slowdissolve
    $renpy.pause(0.70)
    scene caveh with slowdissolve
    n "{i}Several generations ago, when this land was barren, there came to be rumors of a great power lying within the land.{/i}"
    n "{i}\"Great power requires great sacrifice.\"{/i}"
    n "{i}Upon hearing that, several powerful and wealthy families scoured their countries and the globe for a suitable sacrifice.{/i}"
    n "{i}Following the call of the promise of untold power, they came to the rumored place of power.{/i}"
    n "{i}In the covers of secrecy and deception, the peoples greatest treasures vanished.{/i}"
    n "{i}It didn't take long for blame to spread, feuds to break out, and before long, it turned into war.{/i}"
    n "{i}What happened in this days has been lost to history, but the consequences remain.{/i}"
    n "{i}Five lineages who fought to recover their greatest loss and to discover the unknown treasure still reside in that very land today.{/i}"
    n "{i}Only in their bloody and violent pasts can the answers be found.{/i}"
    #more to add here obviously, and refine it
    return
    
label opening:
    play music "audio/bgm/Schmetterling.mp3" fadeout 1.0 fadein 1.0
    scene blackscreen with slowdissolve
    $renpy.pause(0.70)
    scene storageshed with fastdissolve
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
    n "My fists hurt."
    n "Everyone is watching. I don't even know if I'm doing this right."
    n "I hate this."
    show blood_splat_01 at truecenter with Dissolve(0.1):
        alpha 0.9
    $renpy.pause(0.25)
    play sound "audio/sfx/heartbeat_01.ogg"
    hide blood_splat_01 at truecenter with slowdissolve
    show blood_splat_01 at truecenter with Dissolve(0.1):
        alpha 1.0
    $renpy.pause(0.25)
    hide blood_splat_01 at truecenter with slowdissolve
    n "Fucking old man, of course he'd put me up to this. I guess I had to too. Cat's out of the bag and my quiet life is over."
    n "{color=#f00}{b}*crack* !! *smack* *slam* !!{/b}{/color}"
    n "He's still crying.  I wonder if he'd laugh if I told him I envied him."
    n "I haven't been able to cry for six years as of today.  Not since that day."
    n "What would she tell me at a time like this?"
    stop sound fadeout 0.2
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
    show mayu smile at center with moveinbottom
    show kaori def at mymoveinleft(0.45, 0.2, 1.0)
    show toshi def at mymoveinright(0.45, 0.8, 1.0)
    mayu "Kaori and Toshi wanted to come get food over here, then we saw you on our way."
    show mayu def at center
    mayu "So, will you join us or will we have to drag you by force?"
    koji "Actually, I was just thinking about how to spend my afternoon, so this sounds great!"
    show mayu smile at center
    mayu "Awesome, we'll start with lunch at the cafe over here then shopping!"
    hide mayu with Dissolve(0.7)
    hide kaori with Dissolve(0.7)
    hide toshi with Dissolve(0.7)
    n "This should be exactly what I need. But..."
    n "I don't know if I should be around Mayu anytime soon. Mayu Jagura is the daughter of the infamous Jagura family, one of my families direct rivals."
    n "The Jagura's run most of the arms dealing in Kahira city, legal and illegal. And we still don't know who Hiroshi was working for, but with the way sensitive information like this travels, it'll be well known within the week by four other families."
    n "Which means I'll have to give up my friendship with Mayu. If I stay around too long, she may very well be the one who kills me when we're alone."
    n "But today should be fine. Anything to get Hiroshi's screams out of my head."
    show kaori def at mymoveinleft(0.5, 0.2, 1.0)
    kaori "Mayu sure is in high spirits today, huh? She called us up and told us to get ready in ten minutes before she'd be there to pick us up and take us shopping."
    show toshi def at mymoveinright(0.5, 0.8, 1.0)
    toshi "She even insisted she'd pay for everything. The only thing I don't like is her driver. He always looks like he's ready for trouble."
    koji "Hmm, well he's not here anymore, so just enjoy it."
    koji "Hey, Mayu?"
    show mayu surprised
    mayu "Hmm?"
    koji "Did something happen to put you in such a generous mood today?"
    show mayu smile
    mayu "My father arranged to get special present today. That's where we're going shopping."
    koji "That's right, you've said he's usually out on business?"
    mayu "Yep, but whenever he gets the chance he usually arranges something like this for me. He said the shopkeeper should have already been paid and to pick out whatever."
    toshi "Must be nice being that rich."
    
    return
    
#most likely want Mayu to get a phone call before the evening is over telling her the truth about Koji. She doesn't let him know she knows yet, but makes an awkward goodbye.
label day1_gunshop:
    play music "audio/bgm/marty_plant.ogg"
    scene gunshop with slowdissolve
    show shopkeep def at left with Dissolve(1.0)
    shop "Well, what about this one here? It's got great aim, a double stack magazine, night sights, 9mm, and thing is damn near indestructible."
    show mayu def at right with Dissolve(0.55)
    n "She takes the gun and holds it in her hand, getting a feel for it. Then, after looking down and sights and racking the slide, she hands it back dissatisfied."
    mayu "Ugh, no. It's too bulky and unwieldly. And do you have anything in a bigger calibur?"
    shop "Come on, you're really limiting our options here. You want smaller, but bigger. Alright, let me see what I got."
    n "Meanwhile, on the other end of the store."
    hide shopkeep with moveoutleft 
    hide mayu with moveoutleft
    $renpy.pause(0.1)
    show kaori def at center with Dissolve(1)
    kaori "Hey, they got some great stuff here, huh? Look at this, it has so many pockets!"
    show toshi def at right with Dissolve(1)
    toshi "For what would you need tactical underwear for?"
    n "Kaori looks at him like the answer would be obvious."
    kaori "Carry all my makeup without a purse."
    hide toshi with moveoutright
    hide kaori with moveoutright
    
    show mayu def at center with Dissolve(0.25)
    mayu "Here."
    koji "What's this?"
    mayu "Since I can't be the only one getting something here, you might as well get this pocketknife or something. Here."
    koji "Alright, well thanks! It'll be the best birthday present I've gotten in a while."
    show mayu surprised with Dissolve(0.2)
    n "Uh oh. She looks shocked."
    mayu "It's your birthday?!"
    koji "Yeah, but don't be so loud about it."
    show mayu dis with Dissolve(0.2)
    mayu "Shut up. We're picking you out something better."
    show mayu def with Dissolve(0.2)
    mayu "See these handguns? Pick one out."
    koji "Oh, I can't do that. Really. These are all way more expensive that that knife was."
    mayu "Do it or I'll pick one out for you. And just maybe it'll be pink."
    
    #add a choice in here somewhere, about letting her pick or choosing your own with a few options maybe.
    show shopkeep def at left with fastdissolve
    shop "No worries, Mayu. Your father said whatever you want is fine. You sure you trust this other guy with a firearm though?"
    mayu "It's fine. It's his birthday, and if he can't figure it out I can bring him back to use the range."
    shop "More business is always better I say. Take care on your way back now, and if you get stopped by the police-"
    hide shopkeep with moveoutleft
    mayu "I know, I know, you didn't sell us anything."
    
    mayu "Actually, Koji, would you like to use the range real quick just to see how you do?"
    koji "I don't know, and we have Kaori and Toshi here who--"
    show kaori def at left with moveinright
    kaori "It's alright, we're actually going to go across the street and get some ice cream."
    show toshi def at right with moveinright
    toshi "Yeah, you two have fun. I don't think this environment is really for me anyways. But Kaori, onward to ice cream."
    hide toshi with moveoutright
    hide kaori with moveoutright
    
    #add range scene where Mayu shows Koji how to shoot
    #end it with her sticking the loaded gun into his waste line
    scene gunrange with wipeleft
    n "For being such a normal looking and average shop out front, the range here was extravagant. There was at least a dozen lanes, a dedicated break room attached, and enough ammo boxes to fill a van. I guess this really is a Jagura business."
    mayu "Alright, for now just leave it unchambered since you're still new to this. Don't want it giving you a heart attack if it suddenly goes off."
    
    scene gunshop with slowdissolve
    toshi "Ah, perfect timing. We just got back. All set?"
    
    n "We were just about to leave, then.."
    n "*ring* *buzz* *ring* *buzz*"
    mayu "Oh sorry, phone call. I'll be right back."
    play music "audio/bgm/the_complex.ogg" fadeout 1.0 fadein 1.0
    n "Mayu stepped away to the other end of the store. I have a bad feeling about this."
    n "If news got around already. If she finds out I'm not really Koji Tasura, but really Koji Ikida, the Ikida successor thought to be deceased, I'll really be dead."
    n "She takes a look back at me while listening on the phone."
    n "Our eyes meet."
    n "Fuck. This is it, isn't it?"
    n "It's already loaded with bullets in the magazine. I just have to chamber it. That would let me be able to react to her attack in just a few seconds."
    n "Wait. What am I thinking? It's probably just a normal phone call. She was just looking over here to see if I'm ok waiting for her."
    n "Her expression changed. Not fully, just her eyes. It's hard to tell. It was so fast. Does she know?"
    n "Does she know I'm really Koji Ikida, one of her families blood rivals? Worse yet, that I've been deceiving her all this time? What if she thinks our entire friendship was just be manipulating her?!"
    n "Fucking shit. She's hanging up the call. I need to be ready. Or do I deserve whatever happens? Even though I spared Hiroshi...people have died protecting my identity. And here I am, about to be executed for it. She'll probably have to kill Kaori and Toshi too."
    n "I'm some Kaori, Toshi. I guess you got inadvertantly dragged into this too."
    n "This shop is run by associates of her family. They'll cover it all up. I'm in their hunting grounds right now."
    n "Damnit, she's already right in front of me."
    koji "Eh, ummm...ready to go?"
    n "She looks at me with a complexed expression before speaking."
    play music "audio/bgm/marty_plant.ogg"
    mayu "It turns out I need to go. Um, I'm sorry everyone that I won't be able to give you rides back to your houses even though I drove you out here. Excuse me!"
    n "She turned back to me just before leaving the store."
    mayu "Happy birthday, Koji. I hope you like your present."
    koji "..Whew."
    n "And with that she quickly disappeared, as should I. I quickly say my goodbyes and..."
    
    menu:
        "Quickly head the opposite way from her.":
            jump day1_c1_away
        "If she knows, I have to explain to her!":
            jump day1_c1_follow
    
    label day1_c1_away:
        n "It's best if I just avoid her for now, no telling what she'll do if she knew the truth."
        return
        
    label day1_c1_follow:
        n "I can't have her get the wrong idea. I can only hope she'll listen to me. And if she doesn't know, I can explain it to her before hand."
        n "I just barely catch a glimpse of her from behind as she takes a turn behind a building. I'm not too late!"
        n "I turn and follow the way she went. Where did she go?"
        n "Then I hear it. The footsteps from behind me."
        n "I turn around and there she is. Gun drawn."
        n "This is my end. And I was just trying to make this better."
        mayu "Is it true, Koji?"
        n "She looks serious."
        koji "Mayu, I can explai--"
        mayu "Is it true? Are you Koji Ikida?"
        koji "Yes, yes it's true. After my parents died, they said I had died in the hospital and tried to make it seem like I didn't exist anymore."
        mayu "So you've just been keeping tabs on me for your family? Thought we'd just be friends until it was convenient for you to try something?"
        n "Her hand was shaking with something that was probably filled with anger and fear."
        koji "Hey, do you remember when we first met? I didn't even know your last name was Jagura until the second week. And I haven't told anyone anything regarding you. Do you think my grandfather would approve me spending time alone with anyone from another family?"
        n "Her breathing is getting heavier. She's getting emotional and angrier. This is bad. I'm going to die here."
        mayu "You've been lying to me since we met, and you want me to believe all that?"
        n "She faulters her stance as she makes hand motions when speaking, she's really mad. But it's an opening! I..."
        
        menu:
            "Take my gun out quickly.":
                jump day1_c1_follow_c1_attack
            "She her that I mean no harm, no matter what it takes.":
                jump day1_c1_follow_c1_surrender
            
        label day1_c1_follow_c1_attack:
            n "In her quick falter and distraction, I pull out the gun she just bought me and aim it at her center."
            n "I'm sorry, Mayu. But you won't listen to reason and I don't want to die. I'm so sorry."
            n "*click* ... *click*"
            koji "Fuck."
            mayu "You never chambered a round after we left the range, Koji. I'm sorry for this, I really am. I liked having you as a friend."
            koji "No, Mayu you don--"
            mayu "Please forgive me."
            n "With that, I felt nothing but pain and darkness afterwards."
            #maybe have him get paralyzed and him and mayu become friends as he is hospitalized and cant move on his own anymore. still, bad end..
            jump badend1
            return
        label day1_c1_follow_c1_surrender:
            n "I can't hurt her. I'm not that type of person, yet anyways. It almost gave me a panic attack thinking back to what I did to Hiroshi, how could I go on if I killed Mayu?"
            n "I do the only thing I can do. It's childish, but I'm scared for my life right now. Anything to fix this situation."
            n "She gasps as I touch her, she must have just realized how off guard she was. It could have been a deadly mistake."
            n "I embrace her. What else could I do? I'm not ready for this life yet. Since I've been hiding my identity, I haven't made many good friends. I can't lose one over family rivalries."
            mayu "What do you think you're doing?"
            koji "Please just listen. You're my friend, Mayu. Yes, I lied about who I was. No, I've never betrayed your trust other than that. I followed you here, because I want to tell you the truth before you found out. I don't want to lose you as one of my few friends. If you must still kill me, fine..I won't blame you."
            n "A strange silence lingers in the air as we stand there frozen."
            mayu "What are you saying? Of course I'm not going to kill you. I just had a hunch you might follow me and thought you were going to kill me."
            koji "That's stupid, I wouldn't do that."
            mayu "Hey, don't take my lines."
            mayu "You can let go now.."
            n "Realizing I was still hugging her, I let go. My entire body was sweating, but the fear I felt was finally dying down."
            koji "Eh, um, sorry."
            mayu "I do have to go though, my driver will be here shortly. I'm sure everyone knows about you by now and they'll expect me to be extra cautious. We may need to keep some distance for a while. I'll call you later and you can fill me in about some details I'm curious about."
            n "With that, we said our goodbyes. It wouldn't be good for her driver to see me."
            $jagura += 1
            return
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

    
label endgame: