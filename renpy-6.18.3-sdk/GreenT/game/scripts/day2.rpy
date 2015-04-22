label day2_open:
    ##Day 1 Recap - Birthday
    ##Same Day/Day After Hiroshi revealed his identity to the other families
    ##Take care of Hiroshi -- Meet up with Mayu
    ##Mayu Finds out one way or another -- Terms can vary
    ##Grandfather wants him to stay home from college today
    ##Could switch focus to Mayu for a bit.
    ##Maybe have Koji brought to secluded area where he can talk with his grandfather and other family thugs about what he can do or his future roll.  Maybe have Yukino with since she has been involved in this herself.
    ##Could be his first mission to show his competence. Something based on his families specialty? Or something basic.
    ##Right now his families specialty is blackmail and gambling. The kind of people who will put you in an unsuspecting trap then wring you dry with you powerless to fight back.
    ##kind of want the days to detail Koji's descendance into the darker underworld of his families lifestyle and see him transform from a college student into someone who has been forced to sacrifice friends and himself to become whats needed to make his family secure
    
    scene whitescreen with slowdissolve
    play sound "audio/sfx/alarm.ogg" loop
    #scene bedroom morn with slowdissolve
    
    n "Oh god. What is that awful sound? Oh yeah...that's right."
    n "..."
    
    stop sound
    
    n "My alarm clock.  I hate whoever invented it."
    
    scene bedroom with slowdissolve
    play music "audio/bgm/easy_lemon.ogg"
    
    n "Normally I'd be getting up for school, but not today. So that means..."
    n "Zzzz...Zzz..."
    n "Zzzz...Zzz..."
    n "Zzzz...Zzz..."
    n "{size=+5}{b}*Knock!* *Knock!*{/b}{/size}"
    n "...why..."
    n "{size=+10}{b}*Knock!* *Knock!*{/b}{/size}"
    n "WHY?!?!?!"
    n "{color=#f00}{size=+15}{b}*Knock!* *Knock!*{/b}{/size}{/color}"
    koji "Who is it? You can come in."
    
    show denji def at mymoveinleft(0.7, 0.5, 1.0)
    
    denji "Your grandfather sent me to you let you know you're expected in the backyard in ten minutes."
    koji "..so..early."
    
    show denji alt with fastdissolve
    
    denji "I figured you'd might head back to sleep after your alarm went off, so here's a quick breakfast before you head downstairs."
    koji "Unghh...Thanks."
    
    hide denji with moveoutleft
    
    n "I'm not ready to get up yet. I must have been up too late thinking about everything last night."
    n "Ugh. I guess it's time to get up."    
    
    return
    
label day2_yard:
    play music "audio/bgm/the_complex.ogg" fadein 1.5
    scene ikidayard with slowdissolve
    
    n "The backyard here is nice, large, and safe from prying eyes thanks to the high walls. It's a perfect spot for doing any sort of activity you can imagine. Thanks to the distance we are from any of our neighbors, it's often used as a makeshift gun range for some of our employees and family members."
    
    show aido def at center with quickdissolve
    show yuki def at left with quickdissolve
    
    n "Both my grandfather and Yukino were waiting for me as well as a few of our employees that I'm somewhat familiar with. Sometimes I don't realize just how many people enter and leave our grounds, but they're all paid by Ikida money one way or the other."
    n "Aido Ikida, the man who is my grandfather, just stares at me as I enter the courtyard. His presence fills the atmosphere with a commanding tone. With a simple hand motion one of the larger, bulkier men behind him comes forward. I don't have a good feeling about this."
    n "There's a brief pause of silence before Yukino speaks up."
    yuki "Are you sure about this, grandfather?"
    aido "If you don't care to watch, you are free to head inside."
    n "Next he turns back to me."
    aido "Koji, today we will keep this basic. This will be your first training lesson. Since we can't have you out doing business with no way to handle a situation should it occur, your job is to beat Leon before the day is over."
    n "The man I can only assume is Leon takes a bow. I can't beat him! He's huge!"
    koji "What?! I can't possibly do that, look how muscular he is! How tall he is!"
    aido "That's why you have all day to try. I don't want to have to tell you what happens if you fail."
    n "With that he starts walking off like what he did was simply just a mundane task."
    koji "How do I know if I succeed? What counts as beating him?"
    aido "Hmm, break his nose. Sound good, Leon?"
    n "He simply gives a nod and a grunt even though his nose is now on the line. What did I just get into?"
        
    return