label prologue:
    #Dramatic Music - Opening - Goes over premise of the past/ancient times and explains in little detail how the families came to be
    
    #blackscreen keeps transitions between music tracks from overlapping
    play music "audio/bgm/Virtutes_Vocis.mp3" fadeout 1.0 fadein 1.0
    scene blackscreen with slowdissolve
    $renpy.pause(0.70)
    scene caveh with slowdissolve
    
    #maybe make this a scene with Koji as a child hearing a story from his parent or grandparent
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
    show hiro beat at center
    
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
    n "I haven't even had breakfast yet, but maybe that's a good thing for now."
    n "That was Hiroshi. And I nearly killed him."
    n "I know I broke at least a bone or two. The sound of it cracking still rings in my ears."
    n "Betrayal, huh? My older sister always did tell me to be careful who I'm friends with. I wonder if she's had to do the same?"
    n "Knowing the old man, I wouldn't put it past him. Seriously, on my birthday of all things."
    n "But still...was it right? Does that matter? I'm sure he was taught a lesson and won't ever come around my family or myself again, so that should keep him out of harms way."
    n "I'm sweating. I feel cold. My breathing is off."
    n "I can't think about this anymore. I need a distraction."
    mayu "I told you that was Koji. Hey! Hey, Koji!"
    n "The blood washed off well enough, but there was so much...it felt like too much."
    n "No, I need to stop this. I just need to focus on the positive. Hiroshi is alive. Hiroshi is alive because of me."
    n "His face...that look he had. I couldn't tell if it was fear or anger or even disgust. I've never seen him look at me like that before."
    n "I guess you really can't escape this life."
    n "It's a shame really."
    
    show mayu def at center
    
    mayu "Kooooooo-Jiiiiiiii."
    n "Lost in my own head, I nearly crashed right into someone who had just run in front of me."
    koji "Mayu! Where did you come from?"
    mayu "Are you ok, Koji? You look like your dog died. And you totally ignored me while we were trying to get your attention!  Your dog didn't really die did it?!  You never even told me you had a dog!"
    koji "Uh, no, I don't. \"We?\""
    
    show mayu smile at center with moveinbottom
    show kaori def at mymoveinleft(0.45, 0.2, 1.0)
    show toshi def at mymoveinright(0.45, 0.8, 1.0)
    
    mayu "That's right, ignore us again and it'll be painful when we have to get your attention."
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
    n "If only you knew Toshi, if only you knew."
    koji "Hmm, well he's not here anymore, so just enjoy it."
    koji "Hey, Mayu?"
    
    show mayu surprised
    
    mayu "Hmm?"
    koji "Did something happen to put you in such a generous mood today?"
    
    show mayu smile
    
    mayu "My father arranged to get special present today. That's where we're going shopping."
    koji "That's right, you've said he's usually out on business?"
    mayu "Yep, but whenever he gets the chance he usually arranges something like this for me. He said the shopkeeper should have already been paid and to pick out whatever. Although, I wonder how well you three will fit in."
    toshi "Must be nice being that rich."    
    
    return
    
label day1_cafe:
    play music "audio/bgm/bright_wish.ogg" fadein 1.0
    scene cafe with wipeleft
    show kaori def at center with Dissolve(1.0)
    
    kaori "Thanks so much for taking us here, Mayu! I've been wanting to try this place out for so long, but the...erm...the prices.."
    n "Kaori stumbled open her words when she opened the menu. She knew they were high, but I guess she didn't know just how high."
    
    show mayu def at left with Dissolve(1.0)
    
    mayu "Don't start with the glum faces. Let's get extra today. Kaori, get your fill today. I mean it, no holding back like you always do."
    
    show toshi def at right with Dissolve(1.0)
    
    toshi "Can do! Though I'd love it if you made treating us like this a habbit, I still feel kind of bad."
    
    show mayu dis at left with Dissolve(1.0)
    
    toshi "Oh, I'm definitely getting three of these."
    koji "Well, don't worry, Mayu. You can take me out to eat all the time and I'll never have a hint of guilt."
    mayu "That's because you're a trouble maker."
    koji "What?! Since when?"
    mayu "Since the first time I met you. What was it again? Oh yes..You were running to the restroom in between classes and hit me like a truck when you turned the corner."
    koji "Eh, well..Yeah, that's right. That's when I found out how unforgiving you are."
    mayu "Then I made you pick up all my stuff, bring it to my classroom, and buy my lunch before you made it to the restroom. I was waiting for you to run off yelling about not being able to hold it anymore, but you kept doing everything I said while apologizing. I thought you were going to wet yourself."
    
    show mayu def with fastdissolve
    
    koji "I was at fault, I had to make amends."
    n "The truth is that I was terrified she was going to have me killed. I was taught who to watch out for by my family, and the Jagura's were near the top. You can imagine how they might be over protective of their family heir and eldest daughter."
    
    waiter "Is everyone all set to order?"
    n "Mayu, Kaori, and Toshi all seem set and look at me for approval."
    n "Damnit, I'm the only one who hasn't decided yet. That's what I get for not paying attention and making too much conversation."
    
    show cafe with fade
    
    kaori "Please...please...no...more..."
    
    show mayu cry with fastdissolve
    
    mayu "Ugh...maybe thirds was a bad idea.."
    toshi "Never again am I listening to you."
    n "Sitting here with a smile on my face, I take another bite from my plate. They really did get their fill and make in count just like they said. Fortunately, I didn't feel to try and keep up with them."
    
    return
    

label day1_gunshop:
    play music "audio/bgm/marty_plant.ogg"
    scene blackscreen with slowdissolve
    
    n "Damn it...why here of all places? This isn't good. What if someone here knows my secret already? This is basically a Jagura stronghold."
    
    scene gunshop with slowdissolve
    
    n "There's a few employees in the store, they all give us the once over visually, but return to their work. Maybe I worry too much."
    
    show shopkeep def at left with Dissolve(1.0)
    
    shop "Well, what about this one here? It's got great aim, a double stack magazine, night sights, 9mm, and thing is damn near indestructible."
    
    show mayu def at right with Dissolve(0.55)
    
    n "She takes the gun and holds it in her hand, getting a feel for it. Then, after looking down and sights and racking the slide, she hands it back dissatisfied."
    mayu "Ugh, no. It's too bulky and unwieldy. And do you have anything in a bigger caliber?"
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
    scene gunrange with wipeleft
    
    n "For being such a normal looking and average shop out front, the range here was extravagant. There was at least a dozen lanes, a dedicated break room attached, and enough ammo boxes to fill a van. I guess this really is a Jagura business."
    n "Most impressive yet was the fact this whole section was underground and well hidden. We had to get buzzed in behind a locked door then take a narrow staircase down."
    
    #add gun range practice scene
    
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
    n "I'm some Kaori, Toshi. I guess you got inadvertently dragged into this too."
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
    
    scene alley with fastdissolve
    show mayu dis at right with moveinbottom
    $renpy.pause(0.25)
    hide mayu with moveoutright
    
    n "I just barely catch a glimpse of her from behind as she takes a turn behind a building. I'm not too late!"
    n "I turn and follow the way she went. Where did she go?"
    n "Then I hear it. The footsteps from behind me."
    
    show mayu sad at center with fastdissolve
    
    n "I turn around and there she is. Gun drawn."
    n "This is my end. And I was just trying to make this better."
    mayu "Is it true, Koji?"
    n "She looks serious."
    koji "Mayu, I can explai--"
    mayu "Is it true?! Are you Koji Ikida?"
    koji "Yes, yes it's true. After my parents died, they said I had died in the hospital and tried to make it seem like I didn't exist anymore."
    mayu "So you've just been keeping tabs on me for your family? Thought we'd just be friends until it was convenient for you to try something?"
    n "Her hand was shaking with something that was probably filled with anger and fear."
    koji "Hey, do you remember when we first met? I didn't even know your last name was Jagura until the second week. And I haven't told anyone anything regarding you. Do you think my grandfather would approve me spending time alone with anyone from another family?"
    n "Her breathing is getting heavier. She's getting emotional and angrier. This is bad. I'm going to die here."
    mayu "You've been lying to me since we met, and you want me to believe all that?"
    n "She falters her stance as she makes hand motions when speaking, she's really mad. But her aim wavers off of me for a moment...it's an opening! I..."
        
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
    koji "..."
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
    mayu "Oh, and Koji...Don't make me have to kill you. Avoid getting dragged in if you can, but if you can't, stay out of Jagura business."
    n "After her stern warning she disappeared. I guess I can't expect her to go against her family. Could I go against my own family, even if I wanted to?"
    $jagura += 1
    
    return
        
label day1_home:
    scene blackscreen with slowdissolve
    play music "audio/bgm/Trio_for_Piano_Cello_and_Clarinet.mp3" fadein 0.5
    $renpy.pause(0.70)
    scene ikidahome with slowdissolve
    
    n "I took the same roundabout way home and entered secretly through the back door as I always have, even though the secret is out now. It's just a habit I guess. I prefer it this way."
    n "Thankfully it's a big house, but I feel it'll still be too small tonight."
    n "I'm not much for dealing with my grandfather. He's driven, focused, and I don't even want to know what he's done in his past. He's exactly what the Ikida family needed to pull it through the hard times we had."
    n "But that has it's cost. I think Yukino gets along with him a bit better, but I don't think she understands him either. It'd be selfish of me to say I hate him, after all he's done for me, but I can't approve of him either."
    n "Maybe I just don't know my place yet, or maybe I'm just scared. Do I want to become like him?"
    
    show ikidahome with fade
    play music "audio/bgm/mourning_song.ogg" fadeout 1.0 fadein 1.0
    
    n "Dinner came earlier than I wanted that night."
    
    show aido def at center
    
    aido "I heard you did an incomplete job of dealing with your gift, Koji."
    koji "I thought I was able to treat my {i}presents{/i} however I wanted?"
    
    show aido dis
    
    aido "That boy may have just well ruined the peaceful life I've built you, and after all these years of keeping you off the radar."
    koji "That may be, grandfather.  But, what's done is done, and killing him would have only caused more trouble for you, the family, and myself."
    aido "Hmmf."
    koji "And besides, I'd like to keep him as a friend...if he ever comes back to school that is."
    
    show aido def with fastdissolve
    
    aido "Koji, you're free to have your own friends, but do keep them away from the house, will you? I'd hate having to talk to the police about missing persons."
    aido "The right you had to live in the dark was abandoned when you picked your friends poorly. The family needs to make big changes starting tomorrow. Be prepared, tomorrow we take a look at how you can do your part. Don't go to school tomorrow."
    n "This conversation wasn't going to go anywhere. I'm a grown man, but even here I have no power."
    
    show yukino def at setloc(0.15,1.0) with fastdissolve
    
    n "I catch my sister off to the side quietly eating while the tension between my grandfather and I builds. She must have something to say about all this."
    n "--Eh, it's not right. If she wanted to say anything, she would have. No need to drag her into this battle. I should find some time to talk to her later."
    
    hide yukino with fastdissolve
    
    n "With a few words of goodbye I left to my room. Today has been too much."
    
    #add scene of self reflection dicking around in bedroom
    play music "audio/bgm/Trio_for_Piano_Cello_and_Clarinet.mp3" fadein 0.5
    scene bedroom with wipeleft
    
    n "What a ridiculous day."
    n "But maybe it's just compounded interest from everything I've avoided up until now."
    n "When my parents died ten years ago, I was with them but survived. I don't know how much money it took, but when the paperwork was all done, I had died along with them and no longer existed."
    n "I think my grandfather was distraught during that time too, having just lost his son and probably felt bad for me or it was just an inconvenient excuse to get one of his grandchildren off the radar."
    n "There isn't any doubt about it, it was an attack from a rival family that killed them."
    koji "Yukino.."
    n "My older sister, Yukino, has had to play the part as the next family successor since that day."
    n "I don't know if she hated me for that or if she was happy. It's hard talking to her about it, she was older when the accident happened and always stayed strong. I don't think I ever once saw her cry since it happened. Maybe she thought it was her responsibility as the oldest to keep her composure."
    n "Not even when Saku, my younger sister died three years ago."
    n "I can't think about this right now, my stomach gets in a knot and my chest hurts whenever I do."
    n "Is it guilt? Regret?"
    #have the butler come in and offer words of wisdom
    n "*Knock* *Knock*"
    n "With a few knocks against the door I finally pull my head back into the present. Guess I got carried away."
    
    play music "audio/bgm/marty_plant.ogg" fadein 0.5
    
    n "Yes?"
    denji "It's Denji, may I come in?"
    
    show denji def at mymoveinleft(0.35, 0.5, 1.0)
    
    n "Denji Yamazaki, one of the most dangerous, well, I guess you can call them henchmen, employed by my family."
    n "He was my fathers best friend and now he's my grandfathers right hand man. But, he's also been kind to me ever since I've known him."
    n "I don't know why he bounces between housework and taking care of family business, but I do appreciate having him around."
    koji "Come on in, what can I help you with?"
    denji "Actually, I wanted to talk to you earlier today but it you were out. How are doing after this morning?"
    koji "Oh, you mean that. I'm honestly not sure..um, feel free to have a seat if you'd like."
    
    return
    
label day1_nightdream:
    play music "audio/bgm/Trio_for_Piano_Cello_and_Clarinet.mp3"
    scene blackscreen with slowdissolve
    
    n "It's like this every time."
    n "Dark. {w=1.5} Lonely. {w=1.5} A place where I've kept all those tears."
    
    show saku smile at alphacon(0.5, 0.5, 1.0)
    
    n "I see her face. {w=1.5} Smiling. {w=1.5} Then she leaves."
    
    hide saku with slowdissolve
    show bedroom dream at alphacon(0.1, 0.5, 1.0) with slowdissolve
    
    n "When she does, the walls of the room fade to a pale gray color. {w=1.5} My chests clamps up. {w=1.5} My eyes burn."
    n "I'm hunched over on the ground, I can't think. {w=1.5} I can't feel."
    n "That's when I realize all over again."
    n "She's gone."
    
    return