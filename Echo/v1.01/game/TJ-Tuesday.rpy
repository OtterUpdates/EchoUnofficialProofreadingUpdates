label tjtuesday:
window hide
stop music fadeout 3.0
scene bg TJTuesday0 with transition_fade
$ renpy.pause(1.0, hard=False)
scene bg TJTuesday with slow_dissolve
$ renpy.pause(2.0, hard=False)

scene bg trail1
with slow_dissolve
window show
play background "reststop.ogg" fadein 3.0
"The sun is bright, and I'm pretty sure I can smell the fur searing on the top of my head."
"It's the end of March, so it's not nearly as bad as it can be, but being right under the sun like this..."
"We've only been on the trail for about ten minutes at this point, but I'm already regretting it."
t "\"Chase?\""
"TJ, who's about five feet ahead of me, turns around."
"It's at that point that I realize he's said something and I have no idea what it is."
t "\"Everything okay?\""
m "\"Uh, yeah, sorry...what did you say?\""
"He looks concerned and walks back towards me."
show TJ Neutral at center with dissolve
t "\"Remember, if you have a headache, or feel sick to your stomach, or if you start feeling like you're not yourself—\""
m "\"Don't worry, I'm fine.\""
"I try to give him a smile to show it's true, but he's already in the process of unscrewing a bottle of water from his backpack."
m "\"No wait, you don't have—\""
play sound "pour.mp3"
"He dumps half of it over my head and I hurriedly unshoulder my camera bag."
m "\"Watch the equipment!\""
t "\"Sorry Chase, but you're not having a heat stroke on my watch.\""
t "\"You know I've studied otter physiology. You guys don't do well in dry, hot environments.\""
"He's pretty close to me, having to dump the bottle over my head."
"I keep holding the bag away from my body while I look down at him, water dripping from my whiskers."
m "\"Otter physiology?\""
t "\"Yeah, it's like your body, its parts, and what they do.\""
"It's a little awkward that TJ knows how my body works, for some reason."
m "\"Huh, so like, you've studied ALL our parts?\""
"The attempt at humor is weak in the first place, but I realize too late that I'm talking to TJ and that he probably wouldn't have laughed even if it was funny."
"He looks a little taken aback."
t "\"Oh, well, yeah. We all have different anatomy so it's important to...\""
"He trails off and I can tell that he's blushing."
"He frowns at me."
t "\"Are you making fun of me?\""
m "\"What? No, I was just trying—\""
"He turns away suddenly and starts back up the trail."
hide TJ with dissolve
t "\"We should keep going, it's an all-day hike.\""
"I follow him quietly."
"It's hard to judge the type of expression he just had on his face. It wasn't exactly angry. More...flustered?"
"I'm pretty sure it's because he knows I like guys."
"Even in college my straight, male friends get uncomfortable when I joke about sex, like they think I'm coming on to them."
"TJ's never told me how he feels about my sexuality."
"In fact, I know nothing about HIS sexuality."
"I think he dated one girl in high school, but that fell apart pretty quick."
"She had problems fitting in, so he befriended her. Obviously she took it as him liking her, so she asked him out."
"TJ, of course, couldn't say no. He's always on a quest to make other people happy."
"Anyway, he definitely isn't homophobic."
"He seemed really happy for me when he found out I was going out with Leo, and he seemed really sad when he found out that we broke up."
"He doesn't exactly follow any particular Christian denomination that I know of. He hasn't even weighed in on the whole Jesus species debate."
"From what I can gather, TJ just likes the spirituality of the whole thing."
"Once, Leo told me that TJ is the type of Christian that Christians always say they are, but definitely aren't."
"I have to agree."

scene bg trail2
with fade
play music "oldwinds.ogg"
"Two hours later and I'm pretty sure I'm going to die."
"I'm practically stumbling after TJ, the lynx fifteen feet ahead of me."
"He doesn't even notice either, cheerfully marching along up the steep trail and over rocks as if they aren't even there."
"I'm dying, literally dying."
play sound "bodyfall.ogg"
scene bg trail2 with vpunch
"My foot slips and I face-plant."
"I lay there, waiting for TJ's god to take me."
t "\"Chase!\""
"I hear some stumbling and TJ slides up next to my body, sending a cascade of gravel over my head."
show TJ Surprised at center with dissolve
t "\"Oh my gosh, are you okay!?\""
"I hear the telltale sound of an unscrewing bottle. I turn my head to the side."
m "\"N—no...\""
play sound "pour2.mp3"
"A gush of water hits me right in the face and I jerk up, sputtering and wiping at my eyes."
m "\"For the love of God, TJ, stop it!\""
t "\"Let's get you to some shade.\""
"He grabs me around the arms and starts dragging me towards a big boulder."
m "\"C—calm down, I can walk!\""
t "\"Are you sure?\""
m "\"Yes!\""
"TJ's looking incredibly worried right now, hovering over me as I make my way to sit against the boulder."
m "\"Dude, I'm fine, I'm just tired...I don't know how you do it.\""
"TJ keeps watching me, and once I sit down he kneels next to me, then runs his paw through the fur on my forehead, feeling it with his pawpads."
t "\"You're a little warm. We should rest here a bit.\""
"He takes out another bottle of water. It's like he brought fifty of the damn things."
t "\"We should probably get your clothes wet—\""
"I put a paw on his shoulder."
m "\"TJ, calm down. I'm fine.\""
t "\"You sure? Because—\""
m "\"TJ!\""
"He stops babbling and looks me in the eye, the water bottle in one paw, the cap in the other."
m "\"What's up?\""
show TJ Rejected with dis
"He looks at me for a second, then breaks eye contact, slowly screwing the cap back on the bottle."
t "\"Sorry, I just...I just want to make sure you're okay. I'm the one that asked you to come.\""
m "\"Relax! I'm just being a little dramatic.\""
t "\"Alright...if you're sure.\""
m "\"I am, but I could use a drink.\""
"He hands me the bottle."
t "\"Good idea. Have you been making sure to drink a lot? I have plenty.\""
m "\"Yup, my piss is crystal clear.\""
"TJ's muzzle quirks as I take a long draft of water from the bottle."
"I cap it and burp."
m "\"You know what, I think it's because I'm starving. When are we gonna eat?\""
show TJ Sheepish with dis
t "\"Not yet! We have to make it to the top first.\""
t "\"I have some granola bars, though!\""
m "\"Ew, dude, I'm hungry for REAL food.\""
t "\"It is real food! Anyway, it'll be so much better if we do it at the top.\""
t "\"Besides, this is the hardest part and it's almost over! It's all downhill after this.\""
t "\"Literally!\""
"I can tell he's getting anxious to start moving again, so I take one last gulp and get up."
m "\"I don't get how you're so damn unaffected by the heat.\""
t "\"Oh, I am. I'm just keeping wet.\""
"While he talks he starts pouring water on his shirt."
"It sticks slick to his torso, showing off his tight chest and flat stomach, his navel a dark indent through the fabric."
"I make sure I don't stare too long, not wanting to make him feel awkward again."
"Either way, I can feel my crotch area getting a little tight. Being in a motel room with two other people didn't exactly give me much time to...relieve stress."
"Maybe my straight friends did have reason to be wary..."
"I keep my eyes focused on TJ's."
m "\"I guess it's how you can keep moving like you do, here in the middle of the desert.\""
t "\"Well, I run a few miles on the track every day at school.\""
m "\"Jesu—Jeeze.\""
hide TJ with dissolve
"We start up the trail again, TJ sticking by my side now."
"I feel bad about holding him back, but at least now it's less likely I'm gonna eat shit again."
stop music fadeout 5.0

scene bg trail3
with fade
t "\"We did it!\""
show TJ at center with dissolve
"TJ looks over the view as I stagger up behind him."
"I'm not as beaten up as I was earlier, but my legs are really starting to kill me. I lean over with my paws on my knees, panting."
"Swimming is definitely a better way to work out."
"TJ turns on me abruptly and I straighten up, smiling."
"He holds up both his paws, grinning."
t "\"Hi-five!\""
play music "comeover.ogg" fadein 3.0
"I slap them with gusto and TJ laughs, pulling off his backpack and sitting down on a rocky bench."
"I look at it, a little confused."
m "\"What's this?\""
t "\"A rock bench! It's always been here.\""
t "\"I think some seniors from the old school made it, see?\""
show TJ at right with moveinleft
#!! not sure if this is too pause-y, but something should be done
"He scoots over, pointing at the back, and I look closer."
"Etched out in large letters and numbers, it says \"Echo High - Class of '59\"."
t "\"They used to paint the year on the canyon, too. You can still see some of them.\""
"Sure enough, I see some white lines on the canyon wall: a 52 here, a 72 there."
"The school closed after 1980, so I assume there's nothing after that."
"I sit next to him and lean my head back, closing my eyes."
"While the hike had been a massive bitch, I still don't regret coming."
"Not just for TJ's sake, but also because there's something nice about being isolated like this, like we're the only people on Earth."
stop music fadeout 2.0
"I feel a weight fall on my lap and look down, expecting to see a tasty sandwich."
"Instead, I find a big, fat, hairy tarantula."
"I freeze as my brain processes what's going on..."
play sound "stinger.ogg"
"!!!"
"Then I scream and take a swipe at it, at the same time doing a sort of spastic dance to the right."
"I slide off the bench and onto the ground, where I roll several times to get away."
m "\"HOLY FUCKING SHIT FUCKING SHIT SONUVABITCH!\""
"I roll to my feet and stumble back further away from the bench, eyes scanning the ground for the giant-ass spider that is sure to be after me."
show TJ Teasing2 with dis
"That's when I realize TJ's laughing."
show TJ Teasing2 at center with moveinright
t "\"Ahahahahaha! Ch—Chase, calm down it—it's ehehehehe!\""
"He holds up the giant spider, its frozen rigidness telling me what he couldn't finish."
m "\"...Fake!?\""
play music "banter.ogg" fadein 3.0
"TJ's still laughing, but I'm still hugging myself, shivering and flinching every time I see something spindly."
#! could use a stronger pause after "shocked" if desired
"I'm shocked, not because of what just happened, but because TJ did it to me...fucking TJ!"
"Feeling betrayed, I glare at him as he beckons me with a paw, wiping at his eyes with the other."
t "\"I'm—hehe, oh my gosh, I'm sorry.\""
show TJ with dis
t "\"But Jenna made me promise her that I'd do it.\""
"That figures."
"Jenna is the type to always play pranks and yeah, I hate to say it, but it's because she's a fox."
"I rub my arms up and down with my paws, shivering again."
m "\"I can't believe you! You know how much I hate spiders.\""
"One of my worst fears had always been that of a tarantula getting into my room."
"I used to regularly shake out the bedsheets when I found out that they lived around Echo."
t "\"I'm sorry. I thought you might not even fall for it. You know the ones around here are blonde, right?\""
m "\"Yeah, TJ, that's the first thing that comes to my mind when I find a fucking spider on my lap!\""
"His ears do lower at that point and he stops laughing, though I can tell he's trying not to smile."
t "\"Listen, Chase, I'm sorry...let's eat, I know you're hungry!\""
scene bg hike with slow_dissolve
stop music fadeout 3.0
play background "reststop.ogg" fadein 3.0
"My stomach IS painfully hollow right now, so I slowly walk back to the bench."
"I try hard not to be such a spoilsport as I reach out to take my plastic-wrapped sandwich from TJ."
"He squirts some hand sanitizer from a little bottle on my paws first before he lets me."
"We share a bag of chips and eat quietly for a few minutes, just taking in the nature. Still, even out here, I'm able to hear the train horns."
"I feel bad about the silence, though, since I'm worried TJ will think that I'm mad at him."
"I mean, I'm annoyed, but he's just too damn innocent to actually be angry with."
"The sun's beating straight down on us at this point, and it's uncomfortable feeling my semi-damp shirt rubbing up against my fur."
scene bg trail3
show TJ Neutral
with dissolve
"Setting aside my food for a moment, I strip off my shirt, the wetness giving me a bit of trouble."
"As I do this, TJ stiffens up next to me. I look over at him and right away it's pretty clear he's trying not to look at me."
"I wonder if TJ is just one of those guys that's embarrassed about showing any kind of fur."
"He only ever took off his shirt to swim, and even then he always seemed embarrassed about it."
"At that moment, both our paws slide into the chip bag at the same time and TJ jumps, pulling his paw away."
"I look over at him, quirking an eyebrow."
show TJ Sheepish with dis
t "\"S-sorry...\""
m "\"For what?\""
t "\"...Never mind.\""
"I watch him take out his phone and look over his messages. When he turns the screen off, he pauses."
"I realize he's looking at his reflection, adjusting the fur on his face, pawing at both sides until he seems satisfied."
"Again, this is something he did when he was much younger, back when he was obsessed with his cheek ruffs being perfectly even."
"I don't say anything, though, and just keep eating, bouncing one of my knees up and down."
"It's damn awkward and I can't figure out why; usually it's really easy to talk to TJ...mostly because he had a lot of things to talk about."
"I try to think of something to say."
m "\"Remember when I made fun of you for the way you used to say sorry?\""
"TJ gives a bright, high-pitched laugh and that makes me relax, feeling like I just broke the ice on a first date."
t "\"Yeah, it's one of the first things you said to me!\""
t "\"I was trying soooo hard to fit in and you just put me on the spot in front of everyone.\""
#!!! maybe?
"The scene plays out in my mind as TJ talks: the image of a seven-year-old lynx, looking way too small for his puffy winter fur."
"He'd just backed into me while trying to catch a ball thrown by Leo and had turned around, full of smiles—"
"\"{i}Sooow-rie!{/i}\""
"I pointed and laughed."
"\"{i}Don't you mean saw-rie?{/i}\""
"That mortified look followed by what would become TJ's trademark run-back-home-crying."
t "\"I must have practiced that word a hundred times when I got back home.\""
"There's a little pang in my heart at the image of kid TJ saying sorry over and over again, trying to get it \"right\"."
m "\"Well..I'm sorry for making fun of you for it.\""
t "\"Hehe, why? It was so long ago. Besides, you were just assimilating me into the culture...sort of.\""
m "\"If it makes you feel better, Leo did get mad at me after you ran away.\""
"TJ's having trouble keeping his lettuce-wrapped turkey together."
t "\"So...are you and him, um...doing alright?\""
m "\"I think so. We had a good talk a few days ago.\""
t "\"That's good.\""
"He gives up on holding the wrap together and instead just starts picking up the remnants from the plastic."
t "\"Were you...lonely after you left?\""
"I try not to act surprised that TJ's asking me these questions."
m "\"Uh, yeah, really lonely. Had a terrible first semester.\""
t "\"Ah...What about now?\""
m "\"Um, kind of? I guess I just haven't been able to find someone I connect with like I did Leo.\""
t "\"Hmm...\""
m "\"Then again, the GSA at the university is practically dead, so who knows? Maybe after I graduate.\""
"We eat in silence for a while longer and, though it's less awkward, I'm still trying to figure out what brought TJ to ask me those questions."
"I crumple up the plastic and toss it in my backpack before getting up."
m "\"Alright, now I gotta find a good view to get my shots. Shouldn't take too long.\""
show TJ with dis
t "\"Oh! There's a great view of the canyon just up the trail, there.\""
"He gestures in that direction with a half-eaten wrap."
"I wave to let him know I heard and make my way up the trail."
scene bg canyon
with dissolve
"The town's namesake isn't much of a canyon."
"You probably wouldn't even realize it IS one without being told."
"I sidle up as close to the edge as I'm willing, taking a look over the side."
play sound "drone.ogg"
"{cps=15}{font=Daubmark.ttf}Feet press pebbles over the side, they clatter down the edge of the cliff..."
stop sound fadeout 2.0
"It's dizzying, and I dig my toes into the rocks, feeling as if I'm going to tip over."
play sound "drone.ogg"
"{cps=15}{font=Daubmark.ttf}Tears and rain mingle, finally letting go, going limp, wind giving the final push..."
stop sound fadeout 2.0
"I back away."
play sound "drone.ogg"
"{cps=15}{font=Daubmark.ttf}Impact...instead of release...pain..."
stop sound fadeout 2.0
"I feel the buzzing starting up in my head again, and I sigh as I bend over and reach into my camera bag."
"I almost wish I could stay here until sunset since the canyon would be a great backdrop for it..."
"...but I definitely don't want to hike back in the middle of the night."
"It doesn't take long, and about five minutes later I've got all the footage I need."
#! probably?
"Hiking all this way definitely wasn't worth it, but of course that's not the reason why I did it."
show TJ at center with dissolve
t "\"You finished?\""
"TJ walks up behind me as I'm bending over to put my camera away."
m "\"Yup!\""
"He hands me a water bottle and I take it from him gratefully, pouring it over my head and chest, the fur flattening down over my body."
"TJ looks at my torso, his muzzle quirking at the corner a bit."
t "\"You know, you kind of look like Jared Grieze.\""
"I raise an eyebrow at him."
m "\"The survivalist, from the Wilderness Channel? What, just because I'm out in the wilderness and shirtless?\""
t "\"Well-\""
m "\"You saying all otters look the same?\""
show TJ Surprised with dis
t "\"No! I mean, not just because you're an otter, I mean your bodies are...\""
t "\"I mean-!\""
"Again, TJ's got me questioning certain things about him."
m "\"TJ, I'm kidding.\""
show TJ Sheepish with dis
t "\"Ahahaha! Yeah, right, of course...\""
"He rubs his shoulder sheepishly as he slowly walks up to the edge next to me."
show TJ with dis
t "\"Woooow...\""
"He gets closer to the cliff, though he does it in a manner in which he's spread out his legs and arms, bracing himself against the ground."
"He peers over the side, looking absolutely ridiculous."
t "\"We're so high up!\""
"I smirk, sneaking up behind him."
menu:
    "Grab him.":
        label grab:
        "I grin, then suddenly slap both of my paws on his shoulders."
        show TJ Surprised
        t "\"AAAAGGH!\""
        "He fluffs out to twice his size almost instantly and flails around like a cartoon."
        "Though I'm sure to keep my grip firmly on his shoulders, one of his windmilling paws catches me in the stomach."
        "My laughing is cut off in a grunt and I quickly pull him back before he can accidentally launch himself off the cliff."
        m "\"Jesus, TJ, calm down!\""
        "His waving paws finally latch on to my fur and before I know it, he's got his arms wrapped around my body."
        "I stumble back, clinging to him as well."
        "We stand like that for a few seconds, and I can't help but guiltily feel a little bit tight in the pants again."
        "It doesn't last long, though, and soon TJ lets go and swats me in the chest with the back of his paw."
        show TJ Annoyed
        t "\"Are you kidding me, Chase, how could you!?\""
        "I'd respond, but I'm busy trying to stop laughing."
        "TJ wipes his paws on his pants."
        t "\"You got all your sweat on me.\""
        m "\"Haha! Hey, you didn't think I'd get you back after that tarantula prank?\""
        t "\"It wasn't REAL! I could have DIED!\""
        m "\"Calm down, you're safe now.\""
        "I put a paw around his shoulders and pull him in close."
        "He tenses up, but does relax after a few seconds."
        t "\"You're all wet and sweaty...\""
        m "\"You'll air-dry.\""
    "Shove him.":
        play sound "drone.ogg"
        "{cps=15}{font=Daubmark.ttf}Lingering for days, white bone pokes through skin, maggots feeding off the living..."
        stop sound fadeout 2.0
        "What?"
        menu:
            "Grab him.":
                jump grab
            "Do nothing.":
                jump donothing
    "Do nothing.":
        label donothing:
        "It's tempting as hell, but I'm worried scaring the cat will make him jump right off the cliff."
        "Instead, I stand next to him and look out over the small canyon."
"We stand there a while, not really ready to head back yet."
show TJ Neutral with dis
"That's when TJ lets out a sudden, loud yell that almost makes me jump out of my fur."
t "\"YAAA!\""
"I put both paws over my ears."
m "\"TJ, what the fu-.. frick?\""
"He frowns."
t "\"Where's the echo?\""
m "\"Huh?\""
t "\"It's called Echo Canyon. Isn't it supposed to echo?\""
m "\"Oh...hmm. HEY!!!\""
"I yell too, TJ lowering his ears a bit as we wait for the response."
stop background fadeout 5.0
play music "canyon.ogg" fadein 10.0
"His ears perk."
t "\"I {i}think{/i} I heard it...\""
m "\"Maybe we're just in the wrong area.\""
t "\"But we're like, right in front of it.\""
"TJ leans forward, as if that will help, and cups his paws around his muzzle before yelling as loud as he can."
t "\"YEAAAAAAAAA!!!\""
"This time, I do hear a return."
"It's muffled, scratchy...ugly, but it's an echo alright."
"TJ makes a face."
t "\"Ugh, that sounded kinda creepy.\""
m "\"Heh, well, what did you expect? Everything's shi—crappy here.\""
m "\"Including Echo's echoes. BLAAAGH!\""
"Again, we're answered with a raspy, ugly response: my voice twisted and distorted."
t "\"Seems a bit silly to name the entire town after that.\""
m "\"I think it fits.\""
"I grunt as I sit down, spreading out my legs with a sigh."
"TJ does the same, except with his legs crossed."
t "\"You really hate this place, don't you.\""
"He looks sideways at me."
m "\"You don't?\""
t "\"Of course not! All of my best friends are from here. I mean, some of it is bad, but why let the bad taint the good?\""
"I make a noncommittal grunting sound."
t "\"I wish we all could have come up here.\""
"He really does look disappointed, and I feel bad about that."
m "\"What, I'm not good enough?\""
show TJ Teasing2 with dis
"TJ giggles."
t "\"I really am glad you came...it means a lot. It would have been pretty lonely otherwise.\""
"I look over at him, and he's looking me right in the eye. His powder blue gaze is really pretty with the sunlight hitting it like that."
stop music fadeout 5.0
play background "reststop.ogg" fadein 3.0
show TJ with dis
"He's smiling, and I smile back."
play sound "phonebuzz.ogg"
"Suddenly, his phone buzzes."
"He breaks eye contact to adjust his sitting position so he can get it out of his pocket."
t "\"Probably Jenna checking in on—\""
show TJ Neutral with dis
"I turn to look back at him when he goes quiet."
"He's furrowing his brow at the phone, as if trying to figure out what it says."
m "\"Everything alright?\""
"Slowly, his face relaxes, but now his expression is dull, his eyes glazed over."
m "\"TJ?\""
"I start to lean sideways to get a look at what the message might be, but TJ quickly shoves it back into his pocket."
t "\"Nothing....just a long message from my mom.\""
"I can tell right away he's lying, which is fucking crazy because I don't think TJ's ever lied to me, at least not so easily."
m "\"Is it bad?\""
t "\"No, just something about.. something about when I come home for the summer.\""
m "\"Oh, okay.\""
"It's weird because I know he's lying, and he probably knows I know he's lying, but still here we are, playing along."
"He stares quietly at the canyon for a few seconds, then stands up, brushing himself off."
show TJ with dis
t "\"Alright, let's go!\""
"The cheerfulness in his voice is forced. It just sounds like he's about to cry."
t "\"Like I said it's all—it's all downhill from here...literally!\""
hide TJ with dissolve
"He turns away quickly and starts back down the trail, wiping his face."
"I hang back, wanting to give him time to get over whatever it is that's bothering him."
"I wonder if it's something to do with family, like a grandparent passing away, or something."
"I'd feel too intrusive asking about it now, so I decide to put it off until tomorrow."

scene bg trail2
with fade
stop background fadeout 3.0
"The hike back is, like TJ said, literally downhill, so it's way easier than coming up."
"TJ's still a little overbearing, making sure I have water and dumping a few unsolicited bottles over my head."
"Even then, he's still acting a bit detached."
"I try to stay upbeat, though, and since TJ's never been one to sulk for long, I get him warmed back up pretty quick."
"By the time we get back to the car he's in a talkative mood again."

scene bg route93
with fade
play background "highway.ogg" fadein 3.0
m "\"So I'm thinking we get Jenna and go to the diner for dinner. Sound good?\""
t "\"Sure! I'll text her.\""
"I reach out to turn on the radio, then I remember where we are."
m "\"So now that we've got hiking out of the way, what are we gonna do for the rest of the trip? We've got like, three days left.\""
t "\"Hmmm...\""
"TJ rests his elbow against the door, tugging at the fur on his chin."
t "\"Well, there are more trails than just that one. We could hike those, too.\""
"I cringe inwardly at the thought of more hiking, but I don't say anything and I'm pretty sure TJ knows I'm not into it."
t "\"But you still need to do stuff for your project, too, right? I could help you with any research you might need to do.\""
m "\"Maybe. It's pretty boring stuff.\""
t "\"Well, the work, yeah, but hanging out together would make it fun!\""
"I grin at his eagerness."
#! probably?
m "\"Well, alright, but I'll warn you: it's a pain in the ass...I mean butt.\""
"TJ smirks at me."
t "\"Chase, you don't have to try so hard. Anyway, I just want to help.\""

scene bg diner
with fade
stop background fadeout 1.0
play music "neutraldiner.ogg"
"Turns out Jenna just walked from the motel to the diner, not really wanting to wait for us."
"Me and TJ step inside, greeted by the smell of what you'd expect in any diner: burgers and fries."
"I'm flooded with old memories."
"It's a place that I had gone to eat every weekend for over ten years of my life."
"I smile, despite myself."
"While I complained a lot about Echo, this place held incredibly happy memories, most of which involved my five friends."
"We see Jenna right away as she steps out from a booth next to the door."
show Jenna Smilinghips at center with dissolve
j "\"Hey, boys!\""
t "\"Hey!\""
m "\"'Sup?\""
show Jenna Smilinghips at left with moveinright
"We make our way over to the booth, TJ sitting on the opposite bench while Jenna steps back to let me pass and sit next to her."
"She wrinkles her nose as I do."
show Jenna at left with dissolve
j "\"Whew, maybe you should have showered before you got here.\""
m "\"Thanks, Jenna. TJ probably smells, too.\""
j "\"Naw, he smells fine.\""
"Of course he does."
show TJ at right with dissolve
t "\"Thanks Jenna! And don't blame Chase, otters are, um...naturally musky.\""
"I decide not to say anything and instead pull a menu out of the metal holder and flip through it."
"The table is greasy so I try not to lean anything on it."
j "\"So did you guys have fun?\""
t "\"Yeah! Made it all the way to the top. We did it faster than I thought we would, actually.\""
j "\"Did you.. you know?\""
t "\"Hehe, yeah...he really freaked out.\""
show Jenna Teasing with dis
j "\"Haha! I knew it! Did you film it?\""
t "\"Uh, no...\""
j "\"What!? That's the reason you pull pranks, why didn't you film it!?\""
t "\"I forgot!\""
"I glare at the menu."
m "\"Shouldn't let her corrupt you so easily, TJ.\""
"I try to think of some Satan metaphor that I can use, but that's when the giant plastic spider lands with a smack on top of the menu I'm looking at."
m "\"AGH!\""
"I can't help myself and shove the menu, and spider, away from myself to fall over onto TJ's bench."
"I look up and Jenna's filming me with her phone, grinning."
m "\"Stop it!\""
"I half-heartedly grab at the phone, but Jenna easily pulls it away."
unk "\"Oh my word! Is that Chase!?\""
"I look up to see the middle-aged coyote making her way from the back kitchen and around the counter."
show Janice Happy at center behind TJ, Jenna
show Jenna Smiling
with dissolve
t "\"Hi Janice!\""
#!!! Would Janice know that Jenna name-changed from Jasmynn?
#!!! It's probably too much of a pain in the ass to make everyone in Echo learn Jenna's name-change during the events of Echo
ja "\"And Jenna and Tobias, too!\""
"I smile politely, only now realizing how loud our bantering must be in the small diner."
ja "\"Now what in the world are y'all doin' back here? Thought we wouldn't see ya again after your graduation!\""
"I've known Janice as long as I can remember, her having always worked in this diner. In fact, she started here when she was about our age."
"Just like most of the town, though, once you're comfortable you don't move much."
j "\"Chase is filming the town for a school project. We decided to make a little reunion out of it.\""
ja "\"Well isn't that nice! I'll bet Leo's mighty happy. He's been talkin' non-stop 'bout you three since y'all left.\""
j "\"Yeah, he pretty much organized the whole thing.\""
show Janice with dis
"Janice suddenly makes a face."
ja "\"Phew-wee! It's ripe over here.\""
"My face burns and I sit harder on my tail, staring at the menu."
ja "\"You know, I think Duke sat here, forgot to spray the scent neutralizer. You know how weasels are.\""
show Jenna with dis
"I feel Jenna stiffen up next to me, but thank God, she doesn't say anything."
t "\"Yeaaah, anyway, how have you been, Janice?\""
"Janice leans her hip against TJ's bench, clasping her paws and leaning an elbow on the back of it."
ja "\"Oh, can't complain. You haven't missed anything, trust me. Actually I've been meanin' to do a little spring cleanin'.\""
ja "\"Not lookin' forward to it, my back doesn't bend like it always did.\""
"All the small-town, small talk niceties.. and speciesism, is starting to make me zone out when suddenly TJ pipes up."
t "\"We'll help!\""
show Janice Happy with dis
"Janice beams."
ja "\"Well, you know I could never ask that of you, especially while you're on vacation!\""
"TJ chuckles."
t "\"Actually, me and Chase were talking about how we had nothing to do. I think it's a good idea!\""
show Jenna Smiling with dis
"I can see from Jenna's tight smile that she's feeling exactly the way I am. TJ and his goddamn need to be a good Samaritan..."
ja "\"Oh Tobias, you're an incredible young man, you know that?\""
t "\"Heh, just wanting to be of help, ma'am. When can we come over?\""
ja "\"Oh, I don't know, how does sometime tomorrow evenin' sound when it's nice and cool?\""
t "\"Sure!\""
ja "\"Well thanks again, Toby, you're really one of a kind.\""
show TJ Neutral with dis
"TJ beams up at her, then at me, then frowns as he sees the look on my face."
hide Janice
show Janicenotepad Happy at center behind TJ, Jenna
with dis
ja "\"Now, what can I get for ya?\""
hide Janicenotepad
show Jenna Annoyed
with dissolve
"After Janice takes our orders she bustles off back to the back, leaving me and Jenna to glare at TJ."
"TJ, at first, pretends he doesn't notice and starts to adjust the salt and pepper shakers, trying to place them evenly between the menu holder."
t "\"That was nice seeing her again.\""
"We don't say anything. Finally, the tension becomes too much and he gives up on the salt and pepper shakers to look up at us."
t "\"What!?\""
j "\"You know exactly what. We didn't come here to clean up Echo's mess.\""
j "\"Speaking of which...\""
"Jenna reaches past me to grab a towelette and starts wiping our table, wrinkling her snout."
j "\"Disgusting.\""
t "\"There's no harm in helping someone. Chase, you told me you didn't know what else we could do.\""
"TJ starts to doodle on a napkin with one of the coloring pencils from the pack they leave on the tables."
m "\"Honestly, Teej, I'd rather hike another trail.\""
j "\"Please don't. I'm marinating in your otter musk right now.\""
show TJ Surprised with dis
m "\"Goddammit!\""
t "\"Chase!\""
"Glaring, I nudge Jenna to slide off the bench so I can get out. When she does, I stomp my way over to the single restroom."
scene bg drestroom
with dissolve
stop music fadeout 5.0
play sound "bathroomdoor.ogg"
play background "restroomamb.ogg" fadein 5.0
"I sigh as I let the heavy door ease shut behind me, pressing on the push-button style lock."
"The quiet coolness is a welcome relief, even if it is a restroom.."
"I put my palms to my eyes and rub them in circular motions, trying to ease the headache that has been building up since the afternoon."
play sound "faucet.ogg"
"I stand in front of the sink and run my paws under the faucet for a while before bringing some water up to my face."
"It feels good, but the headache continues to pound...in fact, it feels like it's getting worse."
"I squint at the mirror, the light suddenly becoming too bright for my eyes."
stop background fadeout 5.0
play loop "hysteria.ogg" fadein 15.0
"Is this a migraine?"
"I've never had one before...have I?"
"I continue staring at my face, feeling the pressure build."
"Pretty soon, there's a strange sound in my ears, like a tuning orchestra, and I feel my heart rate pick up."
"What the hell, is this a stroke?"
"Am I having a stroke!?"
scene mirror with slow_dissolve
"At that moment, looking at myself in the mirror, my eyes just...drop. They move in towards the center of my face."
"At the same time, the sides of my muzzle curve up unbelievably high, giving me a ghastly smile, one that goes up and up past the top of my head."
"Fleetingly, I remember playing with my laptop's camera once, putting on some effects so that my face would distort in ridiculous ways."
"It looks almost exactly like that."
"Then the earth gives way, falls out from under me and my paws slap the sink as I hold on to it to stop from falling sideways into the wall."
m "\"The fuck!?\""
"My voice squeaks as I try to find my footing."
stop loop fadeout 10.0
play background "restroomamb.ogg" fadein 5.0
"I shut my eyes to stop myself from throwing up and, slowly, the roaring dies down and I feel myself regain my balance."
scene bg drestroom with dissolve
"I crack my eyes open and I see my face is back to normal, the light at a tolerable level again."
"I open my eyes the rest of the way and stare at myself, my reflection staring wide-eyed back."
"I'm breathing hard, my chest heaving, pupils dilated."
"Looking down at my knuckles, I see the skin is white through the fur. I slowly let go of the sink and look at my shaking paws."
m "\"What the hell?\""
"My muzzle is dry and I swallow a few times. I'd take a drink, but I don't trust the dirty faucet."
"After a few moments, I'm able to calm down, realizing that I'm probably not dying. In fact, my head feels pretty clear at the moment."
"I'm pretty sure it was a migraine. Migraines can do that to people, right?"
"I draw in a shaky breath again before grabbing a few paper towels from the dispenser."
"I run them lightly under the water, adding a few pumps of foamy soap as well."
"Mom has migraines all the time. I'll call her about it tomorrow..."
"Able to keep my paws steady now, I run the soaped-up towel under my arms a few times."
"After a quick look to make sure the door is locked, I undo my belt and push down my pants and boxers to around my thighs."
"If I really want to take care of the musk smell, I'm gonna have to go down under."
"I run a few more paper towels under the faucet and soap dispenser."
"Just as I'm sliding the towel against my tail-base, I hear a knock and the lever-style handle rattle."
"I jump and look back, not really worried since I know it's locked."
"Because this place is a fucking piece of shit, I'm just in time to see the button lock pop out."
"The handle swings down and the door opens up enough for a lynx's head to poke through."
"There I am, pants down, a paper towel under my tail, looking like I'm wiping my ass while I moon my Christian best friend."
"I think we stay like that for at least ten seconds before TJ blinks first."
t "\"Ohmygosh, sorry!\""
play sound "bathroomdoor.ogg"
"He squeaks it out so fast I barely hear it before he yanks his head out and the door closes with a snap."
m "\"Fuck fucking fuck...FUCK!\""
#! maybe?
"I snarl between my teeth as I scrub myself, then throw away the towel."
"I feel like I'm gonna cry. It's like the entire universe is conspiring against me right now."
"I sigh and wash my hands, realizing that the longer I delay going out there, the stupider I'm gonna look."
stop background fadeout 3.0
scene bg diner
with dissolve
show TJ Surprised at center with dissolve
play music "neutral.ogg"
"When I come back out, I see TJ stand up immediately, eyes straight ahead as we walk past each other before he heads into the bathroom."
hide TJ with dissolve
"Jenna stands up to let me back in to the booth."
show Jenna at right with dissolve
j "\"Everything alright?\""
m "\"Yep!\""
"As we sit back down, Jenna sips from her glass of water, then starts sucking on an ice cube."
j "\"So I know TJ had fun, but did you?\""
"I drum my fingers on the table, still feeling a bit numb from embarrassment."
m "\"Yeah, it was fine. About as miserable as I thought I would be, so no surprises.\""
j "\"Honestly, I actually kind of wished I'd gone with you two.\""
m "\"Oh yeah?\""
j "\"Then I remembered that AC is a thing, so I didn't feel that way anymore.\""
m "\"At least you're built for that kind of weather.\""
j "\"True. Doesn't mean I have to like it.\""
m "\"So what'd you do, sit around all day?\""
j "\"I studied for a while, then Flynn and Leo came by, actually.\""
m "\"Oh, really?\""
j "\"Yeah, they wanted to have lunch with us. Leo was pretty disappointed when he found out you weren't there.\""
m "\"Hmm...\""
j "\"They brought a bunch of presents for Carl and had me choose which one I wanted to give him.\""
m "\"How thoughtful.\""
"Jenna shrugs."
j "\"Anyway, Flynn was pretty quiet.\""
"She doesn't say anything more, so I press her."
m "\"Oh?\""
j "\"Yeah, just kind of...subdued. I guess he might be feeling sorry? I don't know.\""
m "\"Well, here's hoping he comes around.\""
j "\"Anyway, they're planning a surprise birthday party for Carl.\""
m "\"Isn't that not for a few weeks?\""
j "\"Yeah, but we want to have it while we're all here.\""
"Jenna drags a drop of condensation around the outside of her glass for a moment."
j "\"Just between you and me, and don't tell TJ this because I told him I wouldn't tell you, but he said he was really glad to have you along.\""
j "\"He says you're what he misses most about this town.\""
m "\"Really?\""
"That kind of surprises me. We're really good friends, but to say I was what he missed most..."
"I look outside. Again, the sky is painted red, orange, and what almost looks like purple."
j "\"He drew this so I could see what happened when he pranked you, to make up for not recording it.\""
"I look back down at the table as Jenna slides over the napkin TJ had been doodling on."
"A stick figure with a thick tail (I assume me) is lying on the ground, his mouth bigger than his face as he screams. Next to him is a giant spider."
"Standing over them both is a stick-figure with big, tufted ears (I assume TJ) with its stick arms put up over its face, clearly feeling guilty."
m "\"Cute...\""
j "\"Isn't it, though?\""
"Despite my sarcasm, I really do think it's cute, especially the TJ figure."
show Jenna Annoyed with dis
j "\"Shit.\""
m "\"What?\""
j "\"Forgot my purse.\""
"She stands up."
j "\"I'll be right back.\""
m "\"Huh, why? I'll pay for you.\""
j "\"Don't worry about it. The motel's like, five minutes away.\""
m "\"You can pay me back—\""
hide Jenna with dissolve
"But she's already out the door."
"I sigh, watching her make her way down the road through the window."
show TJ Sheepish at center with dissolve
"That's when TJ slides back onto his bench. I quickly look down, feeling my cheeks burn all over again."
t "\"Sorry about that. Just wanted to wash up, too.\""
"I don't know why, considering TJ looks kempt no matter what he does. I force myself to look up."
m "\"Uh, funny drawing.\""
"He looks at the napkin and gives a little laugh."
t "\"Oh, haha, she showed that to you? Wait, where'd she go?\""
m "\"Forgot her purse.\""
t "\"Oh.\""
"We sit in unbearably awkward silence for a while before I finally sigh and lean my face against a paw as I stare hard out the window."
m "\"Okay, so I wasn't wiping my ass. You know otters have glands—\""
show TJ with dis
t "\"Chase.\""
"I look over at TJ and he's smiling."
t "\"I know. I shouldn't have opened the door. You were just taking a while and we were wondering if you were alright.\""
"I look up as I see Janice making her way over, our food on a giant tray."
m "\"I guess it's really the lock's fault.\""
show Janice Happy at farright behind TJ with dissolve
ja "\"Oh, having problems with the restroom door? Make sure it's jammed shut real tight, should lock then!\""
m "\"Thanks.\""
"As the plates are set down I'm faintly surprised at the portion sizes, not used to getting this much in the city."
hide Janice with dissolve
"Janice immediately bustles off to another customer."
t "\"And, you know...\""
stop music fadeout 3.0
"I look up from my giant sandwich and fries, grabbing the ketchup bottle."
play music "comeover.ogg" fadein 3.0
t "\"...it was kind of cute.\""
"TJ immediately looks down, pretending to read the menu even though we've already ordered our food."
"I feel like my brows are almost going to shoot off my forehead as I stare at him."
t "\"What does 'applewood-smoked' even mean?\""
m "\"Oh no, you're not getting off that easy. Did you just call my butt cute?\""
show TJ Surprised with dis
t "\"No!\""
show TJ Rejected with dis
"TJ's ears fall flat, and I'm kinda satisfied that he's the one feeling embarrassed right now."
t "\"I just, I just like.. otters have cute tails, that's all.\""
"I snort."
m "\"Yeah, I can see by the way you drew mine here.\""
show TJ Sheepish with dis
t "\"S—sorry...\""
m "\"Don't be.\""
"So yeah, I'm testing the waters here."
"It's been a while since I've played this game with a guy, and who the fuck thought the next one would be TJ, but here I am."
"I keep looking over at TJ, waiting for him to look up."
"Finally, he does look up at me for a moment and we lock eyes. I smirk and he smiles in return before looking back down."
"Well.. that's something."
stop music fadeout 3.0

scene bg creepylake
with opening_fade
play music "meeting1.mp3" fadein 10.0
"I sit on a big rock next to the shore, watching the tiny waves lap at the smaller rocks."
"Across the lake, maybe a half mile away I see my friends, all of them, floating on something."
"It's my car, they're all in my car. Leo's driving, he's got sunglasses on."
"Even from this distance I see him look across the lake at me."
"He waves, then makes a finger gun, shoots it at me, making a clicking sound with his tongue."
"Flynn sits next to him, head back, sleeping. Carl's drawing on his face. Jenna sits in the back and reads and TJ...Where's TJ?"
"There he is, he's swimming after the car—"
scene bg canyonneg
stop music
play music "unease.mp3"
"Colors fall flat, I feel sticky and sick...something isn't right."
"I'm at the canyon again, I'm looking over the edge, TJ's on the ground, he's staring at me, maggots in his eyes."
"Something moves in the bushes next to him, something...a paw, is that a paw? It reaches out towards TJ—"
scene bg lakeemma
with dissolve
#!!!! maybe? Hard to decipher how this is supposed to be paced
"The lake, I'm staring at the lake, but the day is clear, the sky is blue, and there are things in the water."
"Five...Six things float in the water. Bodies, bodies float in the water."
"I watch the bodies float, bobbing up and down and one looks really familiar."
"This isn't right, this isn't me, what is this?"
"Something across the lake, I see something across the lake."
"There's a toolshed, a toolshed is across the lake and I see the door open."
"There isn't a toolshed next to the lake."
"Something steps out."
stop music fadeout 5.0
jump tjwednesday