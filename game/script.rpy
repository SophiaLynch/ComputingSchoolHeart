# Script for CSH Major Project - Computing School of the Heart

# Characters declared that are used in the game.
# name of the character.
define j = Character("Jimmy")
define m = Character("Maddie")
define so = Character("Sophia")
define s = Character("Sam")
define n = Character("Nick")
define jp = Character("Jacob")
define r = Character("Ram")
define st1 = Character("Student 1")
define st2 = Character("Student 2")
define r2 = Character("Dark Haired Boy")
define n1 = Character("Fierce Eyebrowed Boy")
define m1 = Character("Red Haired Girl")
define so1 = Character("Apostrophe Girl")
define s1 = Character("Bearded Boy")
define jp1 = Character("Technical Boy")
define who = Character("?")

#Locations used in the game
image bg gate = "generic_school_gate"
image bg bike = "bbike"
image bg cafe = "cafe"
image bg classrm = "classroom"
image bg classrm2 = "Classroom_02_day"
image bg park = "park"
image bg corridor = "school_corridor"
image bg gate2 = "school_gate_2"
image bg outside = "school_outside"
image bg house = "someplace_usa"
image bg clouds = "sunset_clouds"

# Character portraits
image jimmy smile = "jimmy"
image ram frown = "ramfrown"
image ram frown blush = "ramfrownblush"
image ram smile = "ramsmile"
image ram smile blush = "ramsmileblush"
image sophia char = "sophia"
image jp frown = "jpfrown"
image jp frown blush = "jpfrownblush"
image jp frown open = "jpfrownopen"
image jp frown open blush = "jpfrownopenblush"
image jp smile = "jpsmile"
image jp smile blush = "jpsmileblush"
image maddie char = "maddie"
image nick frown = "nickfrown"
image nick smile = "nicksmile"
image nick nick smile blush = "nicksmileblush"
image nick uwa = "nickuwa"
image nick uwa less = "nickuwaless"
image sam frown = "samfrown"
image sam frown blush = "samfrownblush"
image sam smile = "samsmile"
image sam smile blush = "samsmileblush"



# The game starts here.

label start:
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg gate

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    # music stuff
    
    
    play music "background.wav" fadein 1 fadeout 2

    show jimmy smile

    # These display lines of dialogue.

    j "Well..."

    j "I guess this is it."
    
    "Today is my first day at my new, pretigious school: The Computing School of the Heart."
    
    "I'm a transfer student, and I've been anxiously looking forward to my time here ever since I got my acceptance letter."
    
    "The Computing School of the Heart, or CSH for short, is one of the most elite computing focused schools in New York."
    
    "To finally have been able to get in after numerous attempts...well, I couldn't be happier."
    
    "Normally, I wouldn't have even been able to afford going here, but thanks to the GDD scholarship, my dream can finally come true!"
    
    "For those of us who are a little bit behind financially and don't have as much experience, the school offers the GDD scholarship."
    
    "The General Discipline Deposit. If you show you're passionate enough about learning, then the school may offer it to you."
    
    "And it's finally my chance! I can learn all I've ever wanted to know about computers!"
    
    "I may be nervous, but I also couldn't be more excited."
    
    "I look around at the students entering the school gates and gulp."
    
    "This is it..."
    
    "I take a deep breath, close my eyes and take my first step into-"
    
    stop music
    
    hide jimmy smile
    
    play music "silly1.wav" fadein 1 fadeout 2
    
    who "HEY!"
    
    who "Watch where you're going!"
    
    j "Oh gosh, sorry!"
    
    "Great..."
    
    "My first day here and I already walk right into someone. I look up to see..."
    
    menu:
        #Ram's route
        "A boy with luscious, dark locks.":
            
            stop music
            
            show ram frown
            "His dark hair waves slightly in the wind, and I can’t help but marvel at how glamorous he looks."
            
            r2 "Why are you staring at me?"
            
            r2 "Nevermind, it doesn't matter. Just get out of my way."
            
            hide ram frown
            
            "The mysterious boy pushes past me into the building."
            
            "Wow...something about him felt..."
            
            "...kind of sad."
            
            "Anyways, it's time to continue on to class!"
            
            play music "background.wav" fadein 1 fadeout 2

            scene bg corridor
            
            with Dissolve(.5)
            
            pause .5
            
            "I head on into the school's entryway and begin to marvel at all of the technical wonders."
            
            "They look pretty radical, but I have pretty much no idea what anything is."
            
            "I've always enjoyed working with computers, but never had the resources to learn as much as others have."
            
            "I keep walking and finally get to my classroom."
            
            "Because of my status as a GDD, I first need to take a preliminary class to teach me a little bit about the basics of everything."
            
            "Everyone else in the class also is a fellow GDD student, so it's nice to know that I don't need to feel too initmidated off the bat."
            
            "I walk into the room, and sit down at one of the empty seats."
            
            scene bg classrm
            
            with Dissolve(.5)
            
            pause .5
            
            "To my right, there's a girl with bright pink hair."
            
            show sophia char
            
            j "Are those...apostrophes on her face??"
            
            "Upon closer examination, I realize that her eyebrows are trimmed down significantly and resemble little triangles."
            
            "That's definitely an...interesting aesthetic choice."
            
            "I look over to my left to see a boy who also has pretty strong eyebrows."
            
            show sophia char at right
            
            show nick smile at left
            
            "His aren't as unique, but they're still quite memorable."
            
            "As I keep looking at the two of them, the girl turns to the boy on my left and starts to speak."
            
            so1 "Nick, did you do the discrete homework?"
            
            n "Uhh...yep! Why? Need help with a question?"
            
            stop music
            
            play music "silly2.wav" fadein 1 fadeout 2
            
            so1 "Yeahhh I kind of haven't started yet. Whoops!"
            
            hide nick smile
            
            show nick uwa at left
            
            n "WHAT? The quiz is tomorrow, Sophia!! Geeze, you really need to start the homework sooner."
            
            so "Pshaw, it's fine. Let's work on it now quickly. We totally have time, right?"
            
            n "Sophia..."
            
            stop music
            
            "I feel kind of uncomfortable caught up literally in the middle of their conversation."
            
            "They must have noticed my embarrassment because Sophia seems to suddenly notice that I'm there."
            
            play music "background.wav" fadein 1 fadeout 2
            
            so "Hey, are you new or something?"
            
            j "Uh, yeah. I'm a transfer student. I'm Jimmy."
            
            so "Eyy, rad! Welcome to CSH, Jimmy! I'm Sophia. That's Nicholas."
            
            hide nick uwa
            
            show nick smile at left
            
            n "Hi, I'm Nick! It's nice to meet a new GDD, Jimmy!"
            
            "I smile up at them."
            
            "They seem friendly enough!"
            
            j "Yeah! It's good to meet you guys!"
            
            j "I don't really know anyone here yet, so it's nice to just not be alone."
            
            n "Hey, would you want to eat with us at lunch today?"
            
            so "Nick...are you sure that's a good idea? You know how the Gossip Gang can be."
            
            n "Psh, I'm sure it'll be fine! Look at him."
            
            n "He needs people to hang out with. They'll understand."
            
            so "Whatever you say..."
            
            so "But don't blame me when Ram loses his shit."
            
            n "It's fine."
            
            j "Hey, I don't want to be a bother. I can just do my own thing. It's alright."
            
            n "No way! You gotta meet the gang, Jimmy! It'll be great!"
            
            j "Okay, if you say so...Thanks, Nick!"
            
            "Nick smiles at me, and I can't help but feel my heart warm up a little bit."
            
            "Who knew I could meet two fun new friends so quickly?"
            
            "My first day might not be so bad!"
            
            "Class passes by quickly, and I leap out of my seat in anticipation once the bell rings."
            
            "Nick chuckles at that, and seems to share my excitement."
            
            so "C'mon, Jimbo. Let's go to the cafeteria."
            
            "Sophia pushes me out of the door of the classroom, barely giving me any time to pick up my things."
            
            hide sophia char
            
            hide nick smile
            
            stop music
            
            scene bg corridor
            
            with Dissolve(.5)
            
            pause .5
            
            "The three of us walk to the cafeteria and pleasantly chat about various games we like."
            
            "Despite the pleasant company, I can't help but be a little nervous about what's in store."
            
            scene cafe
            
            with Dissolve(.5)
            
            pause .5
            
            play music "generic.wav" fadein 1 fadeout 2
            
            "We enter the cafeteria, and Nick and Sophia wave excitedly at a group of people."
            
            "All sitting down at a round table, I see the cast of colorful characters I can only assume to be the Gossip Gang."
            
            show nick smile
            
            n "Hey guys, this is Jimmy!"
            
            n "He's a new GDD student. I figured we could help show him the ropes."
            
            hide nick smile
            
            show sam frown
            
            s1 "Great, Nick! Just great."
            
            "I can't tell if he's being sarcastic or not..."
            
            hide sam frown
            
            show nick smile
            
            n "That's Sam. He's sort of like the big brother of the group."
            
            n "He can seem sort of intimidating at first, but he's a real softy."
            
            hide nick smile
            
            show jp smile
            
            jp1 "Haha, a softy. Hear that, Sam? Nick just called you out."
            
            "I turn to look at the boy who just spoke. He's holding a server in one hand, and a router in the other."
            
            "So...technical..."
            
            hide jp smile
            
            show nick smile
            
            n "That's Jacob, but we sometimes call him JP. He loves working on projects."
            
            hide nick smile
            
            show maddie
            
            m1 "Hi, Jimmy. I'm Maddie. It's nice to meet you!"
            
            "The other girl in the group introduces herself to me without any of Nick's help."
            
            "She smiles at me genuinely, and I already feel like we'll get along pretty well."
            
            hide maddie
            
            "That leaves one more person..."
            
            stop music
            
            show ram frown
            
            "Wait...is that the same guy from before? The one I ran into?"
            
            "Oh God, no way. It can't be."
            
            r2 "Wow, look who it is. The kid who ran into me."
            
            r2 "Nick, did you have to bring him along? He's not some lost little puppy."
            
            j "I'm so sorry about earlier!!"
            
            j "Could you at least tell me your name, though? I want to apologize properly."
            
            r2 "Ugh, fine."
            
            r "It's Ram."
            
            j "Ram..."
            
            j "Ram, I'm so sorry!!"
            
            "I keep bowing my head to Ram to show the sincerity of my apology."
            
            "I really want to be friends with him!"
            
            r "Whatever."
            
            "Ram scoffs at me and turns away."
            
            hide ram frown
            
            show sam smile at left
            
            show ram frown at right
            
            s "Ram, just because you already have a job lined up doesn't mean you're better than us!"
            
            s "Not to mention the fact that you suck at bowling and constantly lose to JC."
            
            play music "background.wav" fadein 1 fadeout 2
            
            "Ram already has a co-op?"
            
            "But...he's still a first year!"
            
            "Gosh, he must be incredibly smart!!"
            
            r "Shut up, Sam."
            
            "Ram turns away, clearly annoyed at Sam's comment."
            
            hide sam smile
            
            hide ram frown
            
            show ram frown
            
            j "Ram, that's so amazing! You're amazing!"
            
            hide ram frown 
            
            show ram frown blush
            
            "I blurt out before I realize what I'm saying."
            
            j "To be a first year and already have a co-op? That's just...wow."
            
            j "You must be so smart!"
            
            "I marvel at how impressive and inspiring Ram already is to me."
            
            r "Jeeze, chill. It's not really a big deal."
            
            r "You're being kind of weird about it."
            
            "My face heats up his comment."
            
            j "A-ahhh!! I'm so sorry!!"
            
            "I once again bow my head to him in a panic."
            
            "The others just chuckle at our exchange, and then the bell rings."
            
            hide ram frown blush
            
            show nick smile
            
            n "Well, looks like it's time to go back to class!"
            
            n "You ready, Sophia? Jimmy?"
            
            "Nick smiles at the two of us."
            
            hide nick smile
            
            show nick smile at left
            
            show sophia at right
            
            so "Yeah, boi. Let's do it."
            
            "I stand up with them, and we head on to our next GDD class."
            
            hide nick smile
            
            hide sophia
            
            stop music
            
            play music "romantic.wav" fadein 1 fadeout 2
            
            "Throughout class, I can't stop thinking about Ram."
            
            scene bg classrm
            
            with Dissolve(.5)
            
            pause .5
            
            j "Guhhh, I messed up real bad with him!!"
            
            "He probably hates me by now!"
            
            "All I ever do is screw up my chances with the coolest people..."
            
            "I decide that I should stop worrying and go back to focusing on class."
            
            "Class seems to last forever as I can't help but keep Ram on my mind..."
            
            scene bg clouds
            
            with Dissolve(.5)
            
            pause .5
            
            stop music
            
            "Over the next few weeks, I keep sitting with the Gossip Gang, and they have seem to have accepted me as one of their own."
            
            "I joke around with them every day, and become especially close with Nick and Sophia."
            
            "And yet...I feel a hole in my heart."
            
            "During that same time, Ram seems to be consistently becoming more and more distant."
            
            "It seems as though the only interactions between us two involve him criticizing me for my lack of knowledge."
            
            "And yet... that criticism just drives me harder and harder to do my best in my classes."
            
            "If Ram sees that I'm trying really hard, he'll like me, right?"
            
            scene bg park
            
            with Dissolve(.5)
            
            pause .5
            
            play music "background.wav" fadein 1 fadeout 2
            
            "One warm Saturday, I decide to take a simple walk around campus."
            
            "I haven't explored much outside of the dorms or classrooms, so it'll be nice to see what the rest of the school looks like."
            
            "There seems to be a small section of forest surrounding one of the school roads, so I decide I might as well explore them."
            
            "As I start to walk closer to the entrance of the woods, I hear something peculiar."
            
            "Someone is...laughing?"
            
            "And barking??"
            
            "I snap my head, trying to find the source of the noises."
            
            "And that's when I see him."
            
            show ram smile blush
            
            stop music
            
            play music "romantic.wav" fadein 1 fadeout 2
            
            "Ram is on the gorund, smiling as a dog licks his face."
            
            "No, it can't be..."
            
            j "That cheerful guy is Ram??"
            
            "I've never seen him look so happy before..."
            
            "His smile is so serene and blissful..."
            
            "My heart skips a beat, and my cheeks flush up."
            
            j "I didn't know Ram could look like this..."
            
            hide ram smile blush
            
            show ram frown
            
            "Ram must have heard my initial statement, because his head pops up in surprise after a second."
            
            r "Jimmy?"
            
            r "W-what are you doing here?"
            
            hide ram frown
            
            show ram frown blush
            
            "His face turns beet red, and he stands up."
            
            r "W-were you there this whole time...?"
            
            j "Uh um, I don't think for the entire time!!"
            
            j "But I saw you playing with that dog."
            
            j "You seemed so happy, Ram..."
            
            j "I've never seen you smile like that..."
            
            "Ram's face become even redder."
            
            r "You can't tell anyone about this, okay?"
            
            r "Promise me you won't?"
            
            j "Of course!"
            
            "I get kind of excited at the idea of sharing a secret with Ram."
            
            "My heart just won't stand still."
             
            "I smile at him."
            
            j "I promise, Ram."
            
            "He seems a little taken back by my enthisiasm."
            
            r "Alright."
            
            "I start to turn around to give him more time alone, but he stops me."
            
            r "Jimmy..."
            
            hide ram frown blush
            
            show ram smile blush
            
            r "Thanks."
            
            "Ram smiles at me slightly, not looking me in the eye."
            
            "That smile made it official."
            
            "There's no way I can't become close to Ram now."
            
            "I need to give it everything I've got!"
            
            "I nod at him and skip away, beaming."
            
            hide ram smile blush
            
            scene bg clouds
            
            with Dissolve(.5)
            
            pause .5
            
            stop music
            
            "The next few weeks seem to go by in a blur."
            
            "I consistently spend more time with Ram."
            
            "At first, he was extremely reluctant to be with me and would push me away."
            
            "But I learned that if I didn't leave, he eventually just gave in."
            
            "And now...Ram smiles at me sometimes when we're alone together."
            
            "I'm always so happy when I'm with him."
            
            "I've never felt anything like this before."
            
            "Do I realy just want to be friends with him?"
            
            "I'm not sure if I can claim that anymore..."
            
            "I want him to smile at me forever."
            
            "I want him to become an even more special part of my life."
            
            "I think..."
            
            "I think I love Ram."
            
            scene bg classrm
            
            with Dissolve(.5)
            
            pause .5
            
            "One day, I head over to our typical, private hangout spot: the software room."
            
            "It's just an empty classroom, but it does the job."
            
            "Ram is usually already there by the time I arrive, but today he doesn't seem to be..."
            
            "I sit around and wait for him for a few hours, doing my homework all the meanwhile, but he never shows up."
            
            "I'm pretty disappointed to say the least."
            
            "Once it starts getting late, I decide it's probably about time to head out and go back to my dorm room."
            
            scene bg corridor
            
            with Dissolve(.5)
            
            pause .5
            
            "On the way there, however, I hear people whispering about something that catches my attention."
            
            play music "sad.wav" fadein 1 fadeout 2
            
            st1 "Did you hear?"
            
            st1 "Ram brought some illegal drugs with him from California."
            
            st2 "What?? No way!!"
            
            st2 "He's going to get in so much trouble!"
            
            st1" Oh, definitely."
            
            st1 "He might even lose his co-op!"
            
            "My heart stops."
            
            "Ram losing his co-op?"
            
            "Ram bringing illegal drugs to the dorms??"
            
            "I can't hold myself back anymore."
            
            j "Ram would never do something like that!"
            
            j "Don't spread false rumors around about someone so kind!"
            
            "I run off, my vision getting slightly blurrier."
            
            "I can't believe that people would accuse Ram of something like this."
            
            "As I'm walking, trying not to let the tears fall, I bump into someone."
            
            j "I'm so-"
            
            show ram frown
            
            j "Ram!"
            
            "I look up to see the person I most wanted to see."
            
            hide ram frown
            
            show ram smile
            
            r "Jimmy, hey."
            
            hide ram smile
            
            show ram frown
            
            r "Hey, are you crying??"
            
            "Ram's voice suddenly grows more concerned."
            
            r "Are you doing alright, Jimmy?"
            
            j "No, I'm not."
            
            "I stop trying to restrain my tears, and I let out everything that I've been holding in for so long."
            
            j "People are spreading rumors around about you, Ram!"
            
            j "They're saying that you brought in illegal drugs from California and that you might lose your co-op because of it!"
            
            r "Jimmy, I di-"
            
            j "I know you didn't do it!"
            
            j "I know that you'd never do something like that."
            
            j "Your heart is too pure, Ram."
            
            hide ram frown
            
            show ram frown blush
            
            j "I know you like to put on a face that you're cold and uncaring, but I've seen the other parts of you too."
            
            j "I know that you have the sweetest smile and the kindest heart."
            
            j "And I can't hold it in anymore."
            
            j "I love you, Ram."
            
            stop music
            
            j "I think I've loved you all along, but I only realized once we started spending more time together."
            
            "I said my final piece, and waited."
            
            "Ram was silent for a few minutes, and then finally spoke."
            
            "He turned his face towards mine, and he had the most blissful smile."
            
            play music "romantic.wav" fadein 1 fadeout 2
            
            hide ram frown blush
            
            show ram smile blush
            
            r "I feel the same way, Jimmy."
            
            r "I love you too."
            
            "My heart leaps out of my chest, and I jump into his now open arms."
            
            "Ram takes my chin in his hands, tilts my face up closer to his, and kisses me passionately."
            
            "Who knew?"
            
            "I came here to learn about computers, but then I also ended up learning a thing or two about love."
            
            stop music
            
            hide ram smile blush
            
            "(Thanks to Andrew Glaude for composing the music!)"
            
            return
                             
                             
        
        #Sam's route
        "A boy with a warm beard.":
            stop music
            
            show sam frown
            
            "I look up at the boy I ran into and can't help but feel my heart grow fuzzy."
            
            "He seems so warm..."
            
            s1 "Eh, nevermind. Don't worry about it! These things happen."
            
            "He smiles at me and starts to walk away."
            
            hide sam frown
            
            show sam smile
            
            j "Uh, w-wait!"
            
            "I try to get his attention before he can disappear entirely."
            
            j "I didn't even get..."
            
            hide sam smile
            
            j "...your name."
            
            "His head disappears into the crowd of students."
             
            "Hopefully I'll be able to see him again..."
            
            "Anyways, it's time to continue on to class!"
            
            play music "background.wav" fadein 1 fadeout 2

            scene bg corridor
            
            with Dissolve(.5)
            
            pause .5
            
            "I head on into the school's entryway and begin to marvel at all of the technical wonders."
            
            "They look pretty radical, but I have pretty much no idea what anything is."
            
            "I've always enjoyed working with computers, but never had the resources to learn as much as others have."
            
            "I keep walking and finally get to my classroom."
            
            "Because of my status as a GDD, I first need to take a preliminary class to teach me a little bit about the basics of everything."
            
            "Everyone else in the class also is a fellow GDD student, so it's nice to know that I don't need to feel too initmidated off the bat."
            
            "I walk into the room, and sit down at one of the empty seats."
            
            scene bg classrm
            
            with Dissolve(.5)
            
            pause .5
            
            "To my right, there's a girl with bright pink hair."
            
            show sophia char
            
            j "Are those...apostrophes on her face??"
            
            "Upon closer examination, I realize that her eyebrows are trimmed down significantly and resemble little triangles."
            
            "That's definitely an...interesting aesthetic choice."
            
            "I look over to my left to see a boy who also has pretty strong eyebrows."
            
            show sophia char at right
            
            show nick smile at left
            
            "His aren't as unique, but they're still quite memorable."
            
            "As I keep looking at the two of them, the girl turns to the boy on my left and starts to speak."
            
            so1 "Nick, did you do the discrete homework?"
            
            n "Uhh...yep! Why? Need help with a question?"
            
            stop music
            
            play music "silly2.wav" fadein 1 fadeout 2
            
            so1 "Yeahhh I kind of haven't started yet. Whoops!"
            
            hide nick smile
            
            show nick uwa at left
            
            n "WHAT? The quiz is tomorrow, Sophia!! Geeze, you really need to start the homework sooner."
            
            so "Pshaw, it's fine. Let's work on it now quickly. We totally have time, right?"
            
            n "Sophia..."
            
            stop music
            
            "I feel kind of uncomfortable caught up literally in the middle of their conversation."
            
            "They must have noticed my embarrassment because Sophia seems to suddenly notice that I'm there."
            
            play music "background.wav" fadein 1 fadeout 2
            
            so "Hey, are you new or something?"
            
            j "Uh, yeah. I'm a transfer student. I'm Jimmy."
            
            so "Eyy, rad! Welcome to CSH, Jimmy! I'm Sophia. That's Nicholas."
            
            hide nick uwa
            
            show nick smile at left
            
            n "Hi, I'm Nick! It's nice to meet a new GDD, Jimmy!"
            
            "I smile up at them."
            
            "They seem friendly enough!"
            
            j "Yeah! It's good to meet you guys!"
            
            j "I don't really know anyone here yet, so it's nice to just not be alone."
            
            n "Hey, would you want to eat with us at lunch today?"
            
            so "Nick...are you sure that's a good idea? You know how the Gossip Gang can be."
            
            n "Psh, I'm sure it'll be fine! Look at him."
            
            n "He needs people to hang out with. They'll understand."
            
            so "Whatever you say..."
            
            so "But don't blame me when Ram loses his shit."
            
            n "It's fine."
            
            j "Hey, I don't want to be a bother. I can just do my own thing. It's alright."
            
            n "No way! You gotta meet the gang, Jimmy! It'll be great!"
            
            j "Okay, if you say so...Thanks, Nick!"
            
            "Nick smiles at me, and I can't help but feel my heart warm up a little bit."
            
            "Who knew I could meet two fun new friends so quickly?"
            
            "My first day might not be so bad!"
            
            "Class passes by quickly, and I leap out of my seat in anticipation once the bell rings."
            
            "Nick chuckles at that, and seems to share my excitement."
            
            so "C'mon, Jimbo. Let's go to the cafeteria."
            
            "Sophia pushes me out of the door of the classroom, barely giving me any time to pick up my things."
            
            stop music
            
            hide sophia char
            
            hide nick smile
            
            scene bg corridor
            
            with Dissolve(.5)
            
            pause .5
            
            "The three of us walk to the cafeteria and pleasantly chat about various games we like."
            
            "Despite the pleasant company, I can't help but be a little nervous about what's in store."
            
            scene cafe
            
            with Dissolve(.5)
            
            pause .5
            
            "We enter the cafeteria, and Nick and Sophia wave excitedly at a group of people."
            
            play music "generic.wav" fadein 1 fadeout 2
            
            "All sitting down at a round table, I see the cast of colorful characters I can only assume to be the Gossip Gang."
            
            show nick smile
            
            n "Hey guys, this is Jimmy!"
            
            n "He's a new GDD student. I figured we could help show him the ropes."
            
            hide nick smile
            
            show ram frown
            
            r2 "Wow, great. Another GDD."
            
            "I can't tell if he's being sarcastic or not..."
            
            hide ram frown
            
            show nick smile
            
            n "That's Ram."
            
            n "He can seem sort of intimidating at first, but he's actually a really nice guy!"
            
            hide nick smile
            
            show jp smile
            
            jp1 "Haha, nice guy. Hear that, Ram? You're a nice guy!"
            
            "I turn to look at the boy who just spoke. He's holding a server in one hand, and a router in the other."
            
            "So...technical..."
            
            hide jp smile
            
            show nick smile
            
            n "That's Jacob, but we sometimes call him JP. He loves working on projects."
            
            hide nick smile
            
            show maddie
            
            m1 "Hi, Jimmy. I'm Maddie. It's nice to meet you!"
            
            "The other girl in the group introduces herself to me without any of Nick's help."
            
            "She smiles at me genuinely, and I already feel like we'll get along pretty well."
            
            hide maddie
            
            stop music
            
            "That leaves one more person..."
            
            "Wait... is that the same guy from before? The one I ran into?"
            
            "Oh God, no way....it can't be..."
            
            show sam smile
            
            play music "background.wav" fadein 1 fadeout 2
            
            s1 "Oh, you're the kid I ran into earlier today! Nice to see you again."
                         
            "My heart skips a beat."
            
            "I can't believe that our paths crossed again."
            
            j "Uh, y-yeah!! Nice to see you again too!"
            
            s "The name's Sam."
            
            j "Sam, I'm so sorry about running into you earlier!!"
            
            "I bow my head in shame, hoping he can find it in him to forgive me."
            
            "Sam just chuckles."
            
            s "Don't worry about it, kid."
            
            s "It's not a big deal."
            
            hide sam smile
            
            show sam smile at left
            
            show nick smile at right
            
            n "Sam isn't the type of person to take something like that to heart if he knows you didn't mean to do it."
            
            n "He's a cool dude."
            
            "I smile and feel a weight lift off of my chest a little bit."
            
            "Thank goodness..."
            
            j "Thanks, Sam."
            
            j "I'm glad that you're not too upset with me because of what happened."
            
            s "Not at all, man."
            
            s "You're good. Don't worry about it."
            
            "He smiles warmly at me, and I feel my face flushing."
            
            "What a comforting guy..."
            
            "And with that, lunch ends and we all go back to our appropriate classrooms."
            
            stop music
            
            hide sam smile
            
            hide nick smile
            
            scene bg clouds
            
            with Dissolve(.5)
            
            pause .5
            
            "Over the next few weeks, I see Sam every day at the lunch table."
            
            "We chat, joke around, and I feel myself growing closer to him with each passing meal."
            
            "Eventually, we even get to the point of hanging out together and doing things on our own."
            
            "Occasionally, we drive to the local mall together and buy things. Or we just browse around and goof off."
            
            "I can't help but really admire him after all the time we've spent together."
            
            scene bg bike
            
            with Dissolve(.5)
            
            pause .5
            
            "One day however, my constant joy is interrupted, and I start to notice a pain in my foot while I'm out with Sam."
            
            show sam smile
            
            s "So yeah, Maddie, Sophia and I do this thing every week where we just talk about their relationship issues."
            
            s "Girls, am I right?"
            
            s "They're both so thirsty, Jesus Christ."
            
            "Sam laughs at that."
            
            play music "sad.wav" fadein 1 fadeout 2
            
            "I start to laugh too, but the sharp pain in my foot becomes too awful to bear."
            
            j "Ow! Oh my God."
            
            "I grimace and tense up my leg."
            
            hide sam smile
            
            show sam frown
            
            "Sam stops walking and turns to me quickly, concerned."
            
            s "Jimmy, are you alright?!"
            
            s "What's the matter??"
            
            "He puts his hand on my shoulder, and I'm momentarily distracted from the pain by his warmth."
            
            "How is a human being this kind and wonderful..."
            
            "But my thoughts are interrupted by another intense pain in my foot."
            
            j "It's my foot. It's-"
            
            "I sigh out in pain again."
            
            j "I'm not sure. It just suddenly started really hurting."
            
            "I can't bear it any longer, and I just start to fall to the ground, holding my foot."
            
            s "Jimmy!"
            
            s "It's okay. It's going to be okay."
            
            "He crouches down next to me and rubs my back, worry all over his face."
            
            s "We have to get you to a doctor right away."
            
            s "Lean on my shoulder if you can't walk."
            
            j "It's alright. It's not too bad. I can still- AHH!"
            
            "I cry out in pain."
            
            s "That's it. We're going to the doctor's right now."
            
            "He lifts me up in his arms and carries me bridal style to his car."
            
            "Everyone in the shopping center is staring at us, and I even see a few faces of classmates from school."
            
            "Oh God...I'm so embarrassed right now."
            
            stop music
            
            play music "romantic.wav" fadein 1 fadeout 2
            
            "...but I can't help but feel like a princess in Sam's arms right now."
            
            "Wait, does that make him my prince??"
            
            "My cheeks flush deeply."
            
            "The idea of Sam as my prince somehow makes me feel a little happy."
            
            "People who see us right now probably think that we're a couple."
            
            "Uwaa, that's so embarrassing!!"
            
            "I don't think I'd mind if that were true though..."
            
            "Yeah."
            
            "I love Sam."
            
            "I think I can safely admit that to myself now."
            
            "How can I not by proud of loving someone so kind?"
            
            "Sam carries me the rest of the way, and gently places me down in the seat of the car once we reach it."
            
            "He gives my hair one final ruffle, and smiles softly."
            
            hide sam frown
            
            show sam smile
            
            s "Let's get you to a doctor now."
            
            stop music
            
            scene bg clouds
            
            with Dissolve(.5)
            
            pause .5
            
            "At the appointment, I'm perscribed a medication for the pain."
            
            "The entire time, Sam sits in the waiting room, anxiously awaiting my return."
            
            "Once I leave the patient's area, he jumps out of his seat, hoping for some good news."
            
            show sam frown
            
            j "My foot will be alright. I just need to take this medication daily."
            
            "I smile at him, letting him know that I'll be safe and healthy."
            
            play music "romantic.wav" fadein 1 fadeout 2
            
            "Sam rushes up to me and hugs me tightly."
            
            hide sam frown
            
            show sam frown blush
            
            s "Thank God..."
            
            s "I was so worried about you, Jimmy..."
            
            "I'm initially taken aback by his sudden hug, but soon enough I wrap my arms around him as well."
            
            j "Thank you, Sam..."
            
            j "Thanks for everything."
            
            "I feel his arms tighten even more, and the two of us eventually break the hug after a minute."
            
            hide sam frown blush
            
            stop music
            
            scene bg classrm
            
            with Dissolve(.5)
            
            pause .5
            
            "The next day, we're both back at school for our classes and our regular schedule."
            
            "My foot isn't feeling as in pain as it was earlier, and I know that I have Sam to thank for his earnestness in getting me some medical help ASAP."
            
            "My first class breezes by, and I'm about to head to lunch when I'm stopped in the hallway."
        
            scene bg corridor
            
            with Dissolve(.5)
            
            pause .5
            
            st1 "Hey..."
            
            st1 "You're Jimmy, right?"
            
            j "Yeah, that's me. Why?"
            
            st2 "You're the one who's been hanging out with Sam-senpai lately!"
            
            play music "sad.wav" fadein 1 fadeout 2
            
            st2 "Who do you think you are?!"
            
            j "What? What do you mean?"
            
            "I back up into the wall behind me as the two strangers keep coming towards me."
            
            st1 "You're not allowed to get so close to senpai like that!"
            
            st1 "You aren't even a member of the official Sam-senpai fan club!"
            
            st2 "Yeah! If someone gets close to senpai, it's gonna be one of us."
            
            st2 "Stay away from him!"
            
            "One of them grabs my collar and pulls up their closed fist."
            
            "Oh God! They're going to hit me!"
            
            "I instinctively close my eyes to prepare for the pain I'm about to feel."
            
            who "DON'T YOU DARE HURT HIM!"
            
            "BAM!"
            
            "I no longer feel the two students holding on to me, and I decide to open my eyes."
            
            show sam frown
            
            "I see Sam standing over the two students, both cowering on the ground."
            
            s "Don't you ever lay a finger on him again."
            
            s "You hear me?"
            
            st1 "S-sorry, senpai!!"
            
            st2 "It w-won't happen again, senpai!"
            
            "They both run away, and Sam comes up to me and holds me against his chest."
            
            hide sam frown
            
            show sam frown blush
            
            s "I was so worried, Jimmy..."
            
            s "I would never be able to forgive myself if the boy I loved got hurt because of me."
            
            "My heart started to beat harder."
            
            stop music
            
            j "L-love??"
            
            j "I'm not sure you understand what you said, Sam."
            
            "He pulled away and tilted my face up to be more in line with his."
            
            hide sam frown blush
            
            show sam smile blush
            
            s "No, I understand it very well."
            
            play music "romantic.wav" fadein 1 fadeout 2
            
            s "I'm in love with you, Jimmy."
            
            s "I want to keep taking care of you, like I have been."
            
            s "You're so important to me."
            
            j "I want that too, Sam!"
            
            j "I love you!"
            
            "I close the gap between our lips, and stand up on my toes to kiss him."
            
            "He holds me tightly, and I've never been happier."
            
            stop music
            
            hide sam smile blush
            
            "(Thanks to Andrew Glaude for composing the music!)"
            
            return
            
        #Nick's route
        "A boy with fierce eyebrows.":
            
            stop music
            
            show nick frown
            
            n1 "Sorry for running into you!"
            
            n1 "Hey...wait..."
            
            n1 "Are you the new GDD I heard about?"
            
            hide nick frown
            
            show nick smile
            
            j "Uh, probably. I am A new GDD student. You might have heard about someone else though."
            
            j "My name's Jimmy."
            
            "I can't help but shyly look away from his eager face."
            
            n "Aw, great! I'm Nick! I'm also a GDD!"
            
            "He grabs my hand and violently shakes it."
            
            n "We should probably be heading to class now, right?"
            
            n "We're headed to the same place, so we might as well go together!"
            
            j "Y-yeah. That sounds really nice!"
            
            "I feel instantly more comfortable at the new school with Nick's welcoming personality."
            
            "We head on into the school's entryway, and I begin to marvel at all of the technical wonders."
            
            play music "background.wav" fadein 1 fadeout 2
            
            scene bg corridor
            
            with Dissolve(.5)
            
            pause .5
            
            "They look pretty radical, but I have pretty much no idea what anything is."
            
            "I've always enjoyed working with computers, but never had the resources to learn as much as others have."
            
            "Nick and I keep walking, aimlessly chatting about various topics, and finally get to our classroom."
            
            scene bg classrm
            
            with Dissolve(.5)
            
            pause .5
            
            "Because of my status as a GDD, I first need to take a preliminary class to teach me a little bit about the basics of everything."
            
            "Everyone else in the class is also a fellow GDD student, so it's nice to know that I don't need to feel too intimidated off the bat."
            
            n "C'mon, Jimmy! Sit next to me!"
            
            "I take a seat to Nick's right, which seems to be an empty seat."
            
            hide nick smile
            
            show nick smile at left
            
            show sophia at right
            
            "To my right, there's a girl with bright pink hair"
            
            j "Are those...apostrophes on her face??"
            
            "Upon closer examination, I realize that her eyebrows are timmed down significantly and resemble little triangles."
            
            "That's definitely an...interesting aesthetic choice."
            
            "As I keep looking at her unique fashion choices, the girl turns to Nick and starts to speak."
            
            so1 "Nick, did you do the discrete homework?"
            
            n "Uhh...yep! Why? Need help with a problem?"
            
            stop music
            
            play music "silly2.wav" fadein 1 fadeout 2
            
            so1 "Yeahhh, I kind of haven't started yet. Whoops!"
            
            hide nick smlie
            
            show nick uwa at left
            
            n "WHAT? The quiz is tomorrow, Sophia!! Geeze, you really need to start the homework sooner."
            
            so "Pshaw, it's fine. Let's work on it now quickly. We totally have time, right?"
            
            hide nick uwa
            
            show nick frown at left
            
            n "Sophia..."
            
            stop music
            
            "I feel kind of uncomfortable caught up literally in the middle of their conversation, and they must have noticed because Sophia seems to suddenly realize I'm here."
            
            play music "background.wav" fadein 1 fadeout 2
            
            so "Hey, are you new or something?"
            
            j "Uh, yeah. I'm a transfer student. I'm Jimmy."
            
            so "Eyy, rad! Welcome to CSH, Jimmy! I'm Sophia. That's Nicholas."
            
            hide nick frown
            
            show nick smile at left
            
            n "I met Jimmy earlier! We came to class together."
            
            "I smile up at them."
            
            j "It's nice to meet you!"
            
            j "I don't really know anyone here yet, I only just met Nick, so it's nice to just not be so alone."
            
            n "Hey, would you want to eat with us at lunch today?"
            
            so "Nick...are you sure that's a good idea? You know how the Gossip Gang can be."
            
            n "Psh, I'm sure it'll be fine! Look at him! He needs people to hang out with. They'll understand."
            
            so "Whatever you say..."
            
            so "But don't blame me when Ram loses his shit."
            
            n "It's fine."
            
            j "Hey, I don't want to be a bother. I can just do my own thing. It's alright."
            
            n "No way! You gotta meet the gang, Jimmy! It'll be great."
            
            j "Okay, if you say so... Thanks, Nick!"
            
            "Nick smiles at me, and I can't help but feel my heart warm up a little bit."
            
            "Who knew I could meet two fun new friends so quickly?"
            
            "My first day might not be so bad!"
            
            "Class passes by quickly, and I leap out of my seat in anticipation once the bell rings."
            
            "Nick chuckles at that and seems to share my excitement."
            
            so "C'mon, Jimbo. Let's go to the cafeteria."
            
            scene bg corridor
            
            with Dissolve(.5)
            
            pause .5
            
            "Sophia pushes me out the door of the classroom, barely giving me any time to pick up my things."
            
            stop music
            
            "The three of us walk to the cafeteria and pleasantly chat about various games we like."
            
            "Despite the pleasant company, I can't help but be a little nervous about what's in store."
            
            scene bg cafe
            
            with Dissolve(.5)
            
            pause .5
            
            "We enter the cafeteria, and Nick and Sophia wave excitedly to a group of people."
            
            play music "generic.wav" fadein 1 fadeout 2
            
            "All sitting down at a round table, I see the cast of colorful characters I can only assume to be the Gossip Gang."
            
            hide sophia
            
            show nick smile at left
            
            show sam frown at right
            
            n "Hey guys, this is Jimmy! He's a new GDD student."
            
            n "I figured we could help show him the ropes."
            
            s1 "Great, Nick! Just great."
            
            "I can't tell if he's being sarcastic or not..."
            
            n "That's Sam. He's sort of like the big brother of the group."
            
            n "He can seem sort of intimidating the first time you meet him, but he's a real softy."
            
            hide sam frown
            
            show jp smile at right
            
            jp1 "Haha, a softy. Hear that, Sam? Nick just called you out."
            
            "I turn to look at the boy who just spoke."
            
            "He's holding a server in one hand, and a router in the other."
            
            "So...technical."
            
            n "That's Jacob, but we'll sometimes call him JP. He loves working on projects."
            
            hide jp smile
            
            hide nick smile
            
            show ram frown at left
            
            show maddie at right
            
            m1 "Hi, Jimmy. I'm Maddie. It's nice to meet you!"
            
            "The other girl in the group introduces herself to me without any of Nick's help."
            
            "She smiles at me genuinely, and I already feel like we'll get along pretty well."
            
            "I turn to the last person there."
            
            "He seems like he doesn't want anything to do with me."
            
            hide maddie
            
            show nick smile at right
            
            n "That's Ram. He's kind of cold at first, but he's a fun guy."
            
            r "Nick, is this really necessary?"
            
            hide nick smile
            
            show nick frown at right
            
            n "Ram, be nice to the poor guy!"
            
            "Nick sighs slightly at Ram's behavior and then turns to me."
            
            hide ram frown
            
            hide nick frown
            
            show nick smile
            
            n "Jimmy, do you want to go over some of the materials you missed from earlier on in the year?"
            
            "He smiles endearingly at me."
            
            j "S-sure!"
            
            "It seems a little unnecessary to be going over these things so soon, but I appreciate Nick's help nevertheless."
            
            "What a sweet guy!"
            
            hide nick smile
            
            stop music
            
            "The lunch bell then rings, and I head back to the GDD classroom with Nick and Sophia."
            
            scene bg classrm
            
            with Dissolve(.5)
            
            pause .5
            
            "The three of us occasionally goof around in class, but we mostly pay attention to the lectures given."
            
            scene bg clouds
            
            with Dissolve(.5)
            
            pause .5
            
            "And it continues that way for the next few weeks."
            
            "After about a month, I start to realize that I've been seeing Nick a little less often than I'd like."
            
            scene bg classrm
            
            with Dissolve(.5)
            
            pause .5
            
            show nick frown at left
            
            show sophia at right
            
            "Our GDD class is about to end, and I look to Nick, hoping we can walk to lunch together."
            
            "But to my dismay, he walks out the classroom without either me or Sophia."
            
            hide nick frown
            
            "I look at her in confusion, and slight heartbreak."
            
            scene bg corridor
            
            with Dissolve(.5)
            
            pause .5
             
            "So, the two of us just start walking to lunch on our own."
            
            show maddie at left
            
            show sophia at right
            
            "On the way to the cafeteria, we run into Maddie and we strike up conversation."
            
            j "I feel like..."
            
            j "I feel like Nick has been avoiding me lately. I'm not sure why."
            
            "Maddie and Sophia give each other a look."
            
            m "Well...I think that Nick is just feeling some things, and he doesn't really know how to deal with them right now."
            
            play music "silly1.wav" fadein 1 fadeout 2
            
            so "Jimmy, he digs you."
            
            j "WHAT?!"
            
            "I scream out in surprise, startling a few people around us."
            
            j "No. No way. Nick...likes me??"
            
            "I'm not sure how to feel right now."
            
            stop music
            
            "He's a close friend, but I guess...I just never thought of him that way."
            
            "But the idea of being with him doesn't seem so bad, actually."
            
            "He's sweet and always fun to be with, and we just have a lot in common."
            
            m "Don't be surprised if he approaches you at some point about it."
            
            "I nod at Maddie, still a little in shock by what I just learned."
            
            scene bg cafe
            
            with Dissolve(.5)
            
            pause .5
            
            "The three of us finally make it to the cafeteria, and we all have a relatively average lunch, except for the fact that Nick isn't there."
            
            "I feel lonely without him but understand that he's probably just preoccupied with something."
            
            "Lunch comes and goes, and it's once again time for class."
            
            scene bg classrm
            
            with Dissolve(.5)
            
            pause .5
            
            "As usual, class isn't esepecially significant, but it's concerning that Nick still hasn't shown up."
            
            "Once class is over, I start heading to my dorm room."
            
            scene bg gate
            
            with Dissolve(.5)
            
            pause .5
            
            "I'm about halfway there, when someone stops me in my tracks."
            
            who "JIMMY!"
            
            "I turn around to see the person who called my name."
            
            show nick frown blush
            
            n "Jimmy, I need to talk to you."
            
            "I smile fondly at Nick, happy that I finally get to see him alone today."
            
            j "Are you going to tell me that you have feelings for me?"
            
            hide nick frown blush
            
            show nick uwa
            
            play music "romantic.wav" fadein 1 fadeout 2
            
            n "W-what?! How did you know??"
            
            "His expression turns to exasperation, and he seems genuinely bewildered by my knowledge."
            
            j "Maddie and Sophia sort of told me."
            
            "I admit sheepishly."
            
            hide nick uwa
            
            show nick frown blush
            
            "Nick sighs."
            
            n "Guh. Those two gossip about everything."
            
            j "Yeah, they're not exactly the best at keeping to themselves."
            
            n "I'm sorry about this, Jimmy. This is such a weird way to confess to you."
            
            n "I'd understand if you never wanted to talk to me again."
            
            "He looks down at his feet, ready to give up."
            
            j "What? That's ridiculous, Nick!"
            
            j "In fact...if it's okay with you, I wouldnt really mind giving this relationship a shot."
            
            hide nick frown blush
            
            show nick uwa less
            
            j "I never really thought about romantic feelings for you until I realized you liked me."
            
            j "It just never occurred to me, but now nothing seems more natural."
            
            j "So, what do you say?"
            
            hide nick uwa less
            
            show nick smile blush
            
            "Nicks eyes widen in surprise for a moment, and then he grabs my face to give me a passionate, yet slightly awkward, kiss."
            
            j "I take that as a yes."
            
            stop music
            
            hide nick smile blush
            
            "(Thanks to Andrew Glaude for composing the music!)"
            
            return
            
        #Jacob's route
        "A boy with a server in one hand and a router in the other.":
            stop music
            
            show jp frown
            
            jp1 "Not cool."
            
            hide jp frown
            
            "That's the only thing I hear the boy say before he walks away, ignoring my attempts at an apology."
            
            "I feel awful..."
            
            "Anyways, it's time to continue on to class!"
            
            play music "background.wav" fadein 1 fadeout 2

            scene bg corridor
            
            with Dissolve(.5)
            
            pause .5
            
            "I head on into the school's entryway and begin to marvel at all of the technical wonders."
            
            "They look pretty radical, but I have pretty much no idea what anything is."
            
            "I've always enjoyed working with computers, but never had the resources to learn as much as others have."
            
            "I keep walking and finally get to my classroom."
            
            "Because of my status as a GDD, I first need to take a preliminary class to teach me a little bit about the basics of everything."
            
            "Everyone else in the class also is a fellow GDD student, so it's nice to know that I don't need to feel too initmidated off the bat."
            
            "I walk into the room, and sit down at one of the empty seats."
            
            scene bg classrm
            
            with Dissolve(.5)
            
            pause .5
            
            "To my right, there's a girl with bright pink hair."
            
            show sophia char
            
            j "Are those...apostrophes on her face??"
            
            "Upon closer examination, I realize that her eyebrows are trimmed down significantly and resemble little triangles."
            
            "That's definitely an...interesting aesthetic choice."
            
            "I look over to my left to see a boy who also has pretty strong eyebrows."
            
            show sophia char at right
            
            show nick smile at left
            
            "His aren't as unique, but they're still quite memorable."
            
            "As I keep looking at the two of them, the girl turns to the boy on my left and starts to speak."
            
            so1 "Nick, did you do the discrete homework?"
            
            stop music
            
            n "Uhh...yep! Why? Need help with a question?"
            
            play music "silly2.wav" fadein 1 fadeout 2
            
            so1 "Yeahhh I kind of haven't started yet. Whoops!"
            
            hide nick smile
            
            show nick uwa at left
            
            n "WHAT? The quiz is tomorrow, Sophia!! Geeze, you really need to start the homework sooner."
            
            so "Pshaw, it's fine. Let's work on it now quickly. We totally have time, right?"
            
            n "Sophia..."
            
            stop music
            
            "I feel kind of uncomfortable caught up literally in the middle of their conversation."
            
            "They must have noticed my embarrassment because Sophia seems to suddenly notice that I'm there."
            
            play music "background.wav" fadein 1 fadeout 2
            
            so "Hey, are you new or something?"
            
            j "Uh, yeah. I'm a transfer student. I'm Jimmy."
            
            so "Eyy, rad! Welcome to CSH, Jimmy! I'm Sophia. That's Nicholas."
            
            hide nick uwa
            
            show nick smile at left
            
            n "Hi, I'm Nick! It's nice to meet a new GDD, Jimmy!"
            
            "I smile up at them."
            
            "They seem friendly enough!"
            
            j "Yeah! It's good to meet you guys!"
            
            j "I don't really know anyone here yet, so it's nice to just not be alone."
            
            n "Hey, would you want to eat with us at lunch today?"
            
            so "Nick...are you sure that's a good idea? You know how the Gossip Gang can be."
            
            n "Psh, I'm sure it'll be fine! Look at him."
            
            n "He needs people to hang out with. They'll understand."
            
            so "Whatever you say..."
            
            so "But don't blame me when Ram loses his shit."
            
            n "It's fine."
            
            j "Hey, I don't want to be a bother. I can just do my own thing. It's alright."
            
            n "No way! You gotta meet the gang, Jimmy! It'll be great!"
            
            j "Okay, if you say so...Thanks, Nick!"
            
            "Nick smiles at me, and I can't help but feel my heart warm up a little bit."
            
            "Who knew I could meet two fun new friends so quickly?"
            
            "My first day might not be so bad!"
            
            "Class passes by quickly, and I leap out of my seat in anticipation once the bell rings."
            
            "Nick chuckles at that, and seems to share my excitement."
            
            so "C'mon, Jimbo. Let's go to the cafeteria."
            
            "Sophia pushes me out of the door of the classroom, barely giving me any time to pick up my things."
            
            stop music
            
            hide sophia char
            
            hide nick smile
            
            scene bg corridor
            
            with Dissolve(.5)
            
            pause .5
            
            "The three of us walk to the cafeteria and pleasantly chat about various games we like."
            
            "Despite the pleasant company, I can't help but be a little nervous about what's in store."
            
            scene cafe
            
            with Dissolve(.5)
            
            pause .5
            
            "We enter the cafeteria, and Nick and Sophia wave excitedly at a group of people."
            
            play music "generic.wav" fadein 1 fadeout 2
            
            "All sitting down at a round table, I see the cast of colorful characters I can only assume to be the Gossip Gang."
            
            show nick smile
            
            n "Hey guys, this is Jimmy!"
            
            n "He's a new GDD student. I figured we could help show him the ropes."
            
            hide nick smile
            
            show ram frown
            
            r2 "Wow, great."
            
            "I can't tell if he's being sarcastic or not..."
            
            hide ram frown
            
            show nick smile
            
            n "That's Ram."
            
            n "He can seem sort of intimidating the first time you meet him, but he's a pretty fun guy!"
            
            hide nick smile
            
            show sam smile
            
            s1 "Haha, a fun guy. Hear that, Ram? You're a fun guy!"
            
            "I turn to look at the boy who just spoke. He has sandy blonde hair, and a full beard."
            
            hide sam smile
            
            show nick smile
            
            n "That's Sam. He's sort of like the big brother of the group."
            
            hide nick smile
            
            show maddie
            
            m1 "Hi, Jimmy. I'm Maddie. It's nice to meet you!"
            
            "The other girl in the group introduces herself to me without any of Nick's help."
            
            "She smiles at me genuinely, and I already feel like we'll get along pretty well."
            
            hide maddie
            
            "That leaves one more person..."
            
            stop music
            
            "No way..."
            
            "It can't be..."
            
            show jp frown
            
            "I see that the final boy is the one I ran into earlier."
            
            "He still has a server in one hand, and a router in the other."
            
            jp1 "Hi."
            
            j "U-Uh, hello!! I'm sorry for running into you earlier!"
            
            play music "silly1.wav" fadein 1 fadeout 2
            
            jp1 "What are you talking about?"
            
            j "Oh, um...I accidentally bumped into you outside of the school."
            
            j "I feel awful that I didn't get to apologize properly!"
            
            jp1 "I don't even remember that happening."
            
            jp1 "Oh well."
            
            stop music
            
            hide jp frown
            
            show jp smile
            
            jp1 "I'm Jacob."
            
            j "I'm so sorry, Jacob! It won't happen again!"
            
            jp "It's okay. Don't worry about it."
            
            jp "Hey, Jimmy, you're new here right?"
            
            j "Uh...yeah. Nick did just explain that to the group."
            
            jp "Are you into Linux?"
            
            jp "No, I'm sure I don't even need to ask that."
            
            jp "How could you not be all about that Linux life?"
            
            "...what?"
            
            j "Linux?"
            
            j "What's that?"
            
            "..."
            
            "......"
            
            "........."
            
            "....?"
            
            hide jp smile
            
            show jp frown open
            
            play music "silly2.wav" fadein 1 fadeout 2
            
            jp "WHAT?!"
            
            jp "YOU DON'T KNOW WHAT LINUX IS?!"
            
            jp "Nick, why did you bring him here?!"
            
            jp "I can't believe I'm talking to someone who doesn't even know what Linux is."
            
            hide jp frown open
            
            show jp frown
            
            "Jacob brings his palm to his face and sighs loudly."
            
            "I can't help but feel shame at not knowing about something that seems to be so essential to a person's well being."
            
            hide jp frown
            
            show nick smile
            
            n "It's alright, Jimmy."
            
            n "You don't have to feel bad about that!"
            
            n "JP is just sort of an elitest about these things."
            
            "Regardless of Nick's reassurance, I look down at my feet in embarrssment."
            
            stop music
            
            hide nick smile
            
            scene bg classrm
            
            with Dissolve(.5)
            
            pause .5
            
            "The lunch period then ends, and I head on with Sophia and Nick to my next class."
            
            "The rest of the day passes by quickly, and I keep reflecting on what had happened."
            
            scene bg clouds
            
            with Dissolve(.5)
            
            pause .5
            
            "The following days go by nearly the same as the day before."
            
            "I go to class, chat with my fellow GDD students, eat lunch, and finish my next class."
            
            "The only difference is that I've started to chat a little more with Jacob."
            
            "He's even let me call him by his nickname, JP, but I still feel a little nervous about that."
            
            "Initially, Jacob wouldn't let me talk to him much..."
            
            "...but once I told him that I wanted him to teach me all about Linux, he was more open to the idea of hanging out."
            
            "We'll often spend time in the software room after classes, just studying together or joking around."
            
            "He's a pretty intelligent guy. Why wouldn't I want to hang with him?"
            
            scene bg classrm
            
            with Dissolve(.5)
            
            pause .5
            
            play music "background.wav" fadein 1 fadeout 2
            
            "Today, Jacob is teaching me the basics of Linux."
            
            show jp smile
            
            jp "So, what do you already know about Linux?"
            
            j "U-um..."
            
            j "I..."
            
            j "It has to do with computers?"
            
            hide jp smile
            
            show jp frown open
            
            jp "Seriously?"
            
            jp "That's it??"
            
            hide jp frown open
            
            show jp frown
            
            jp "Alright then. I guess I'm starting at the beginning."
            
            jp "Linux is an operating system, which is what manages the communication between your hardware and software."
            
            j "Ok, I think I understand."
            
            j "But like...what's the appeal of Linux?"
            
            j "Why is it so great?"
            
            hide jp frown
            
            show jp frown open
            
            jp "WHY IS IT SO GREAT?!?"
            
            jp "Jimmy, Linux is free...It's also a really safe and reliable operating system to use!"
            
            jp "And you don't really have to worry about malware and stuff if you use it."
            
            hide jp frown open
            
            show jp smile blush
            
            jp "Linux is incredible..."
            
            j "Seriously??"
            
            j "That actually sounds pretty great!"
            
            jp "I know, right??"
            
            jp "Linux is amazing!"
            
            "Jacob keeps teaching me more about Linux, and I can't help but be constantly amazed by what he's telling me."
            
            "The two of us occasionally get off topic and start talking about shared interests, friends, our classes and so on, but I still learn a lot about Linux all the meanwhile."
            
            jp "Jimmy, you're fun. I like you."
            
            hide jp smile blush
            
            show jp smile
            
            jp "And I like you more now that you like Linux."
            
            "Jacob smiles at me."
            
            jp "We should do more of-"
            
            stop music
            
            hide jp smile
            
            show jp frown open blush
            
            "Jacob's eyes widen in what only could be surprise and slight delight, and he stops speaking to me immediately."
            
            hide jp frown open blush
            
            show jp smile blush
            
            jp "Paul-senpai!"
            
            "He runs off to an upperclassman who just walked through the software room door."
            
            "Paul(?)" "Oh, sorry. I didn't realize there were already people here."
        
            "The upperclassman looks bewildered, and a little bit uncomfortable by Jacob's excitement."
            
            "Jacob grabs his schoolbag, and exits the software room, dragging Paul out with him."
            
            hide jp smile blush
            
            play music "sad.wav" fadein 1 fadeout 2
            
            "I'm suddenly alone."
            
            "I sit there for a few minutes, lonely and confused as to why Jacob would just leave like that."
            
            "After a few minutes, other members of the Gossip Gang start piling into the software room."
            
            show nick frown
            
            n "Where's JP?"
            
            j "He just..."
            
            j "...left."
            
            hide nick frown
            
            show nick smile
            
            n "Alright!"
            
            "Nick seems unconcerned."
            
            hide nick smile
            
            j "Hey, do you guys know what's between Jacob and Paul?"
            
            "I decide to ask them the question that's been burning in my mind."
            
            show sam frown
            
            s "Oh..."
            
            s "You didn't know?"
            
            s "Jacob has been pretty infatuated with Paul for a while now."
            
            s "They're not even dating, but Jacob is super clingy."
            
            hide sam frown
            
            show ram frown
            
            r "Yeah, Paul doesn't feel the same way at all."
            
            r "I think he just feels bad for the kid."
            
            "I feel empty inside after hearing this."
            
            "Why am I so sad...?"
            
            "Am I sad for Jacob?"
            
            "That must be it."
            
            hide ram frown
            
            show maddie
            
            m "Jacob could probably tone it down, though."
            
            hide maddie
            
            "The rest of the group nods in agreement, and soon enough start discussing different topics amongst themselves."
            
            "I still can't stop thinking about what I learned."
            
            "My heart feels so broken..."
            
            "But I'm sure it's just me feeling bad for Jacob."
            
            stop music
            
            scene bg clouds
            
            with Dissolve(.5)
            
            pause .5
            
            "The next week or so goes by in a blur, and I start to notice all of the times Jacob trails after Paul-senpai or talks about Paul's charm and intelligence."
            
            "How can I compete with that..."
            
            "Maybe I don't really belong with the Gossip Gang."
            
            "Maybe I don't belong here at all."
            
            "I'm starting to think that I should just go back to New Jersey so I can stay out of everyone's way."
            
            "I end up buying my train tickets for the ride home, and gather the Gossip Gang to tell them the news."
            
            scene bg park
            
            with Dissolve(.5)
            
            pause .5
            
            j "Hey, guys."
            
            j "So, I've decided to go back home."
            
            play music "sad.wav" fadein 1 fadeout 2
            
            show nick uwa
            
            n "What?! C'mon, man! You gotta be joking!"
            
            "Everyone's faces fall."
            
            hide nick uwa
            
            show ram frown
            
            r "Jimmy, there's literally no reason to go back."
            
            r "That's so dumb."
            
            hide ram frown
            
            show jp frown
            
            jp "Jimmy...but we're buddies."
            
            "My heart breaks when I hear the term JP uses to describe our relationship."
            
            "Ah...so that's why his feelings for Paul made me sad."
            
            "It's because I love him."
            
            "I don't want to just be his buddy."
            
            "I want to be with him."
            
            "I love him teaching me Linux all the time, and us getting so off topic we just start goofing around instead."
            
            "I just...love him."
            
            "And that's when I know I really have to leave."
            
            "I need to move on."
            
            stop music
            
            hide jp frown
            
            scene bg house
            
            with Dissolve(.5)
            
            pause .5
            
            "And despite their protests, I end up leaving the following morning."
            
            "I get home safely and spend the next few days just lounging around at home."
            
            "I miss everyone terribly...but there's nothing I can do about it anymore."
            
            "One day, the doorbell rings."
            
            "Mom" "Jimmy! There's someone at the door for you!"
            
            "Who could be visiting me?"
            
            "I get up and walk to the front door, unsure of what to expect."
            
            "Once I get there, I can't believe who I'm seeing."
            
            show jp frown
            
            jp "Hey, Jimmy."
            
            j "J-Jacob?!"
            
            j "What are you doing?"
            
            jp "I really missed you..."
            
            play music "romantic.wav" fadein 1 fadeout 2
            
            "His face turns red."
            
            hide jp frown
            
            show jp frown blush
            
            j "Jacob, you don't understand."
            
            j "I need to stay away from you for a little while."
            
            j "Being around you will only hurt me."
            
            jp "Jimmy, please come back!"
            
            jp "I've been so lost without you."
            
            jp "Even being around Paul doesn't make my heart flutter anymore..."
            
            jp "...but thinking about you does."
            
            j "What?"
            
            j "What are you saying, Jacob?"
            
            jp "I'm saying that I'm in love with you, Jimmy!"
            
            jp "I realized it the second you left, but the rest of the group said I should probably take it easy and wait before I come after you."
            
            jp "But...how do you feel about me?"
            
            "He fidgets anxiously."
            
            "Instead of answering him with words, I decide to be bold."
            
            "I lean up and kiss his lips."
            
            hide jp frown blush
            
            show jp frown open blush
            
            j "Does that answer your question?"
            
            "I grin up at him, and I can feel myself growing flustered too."
            
            hide jp frown open blush
            
            show jp smile blush
            
            jp "Hmm, maybe."
            
            jp "You might need to try that one more time."
            
            "The two of use keep kissing over and over again, and I've never felt so happy."
            
            stop music
            
            hide jp smile blush
            
            "Thanks to Andrew Glaude for composing the music"
            
            return
            
            "(Thanks to Andrew Glaude for composing the music!)"
            

    # This ends the game.

    return
