﻿label wideshot:
stop music fadeout 3.0
window hide
scene bg sunday
with transition_fade
$ renpy.pause(3.0, hard=True)
scene bg route93
with slow_dissolve
window show
play music "highway.ogg" fadein 2.5
#!! "about a bit of a distance" is way too jarring
"Payton is a bit of a distance away."
"To get there, you have to get on Route 93 - which Flynn tells me isn't even called that anymore."
"That would make sense considering how it was impossible to find on the GPS."
"Anyway, to get to the city you have to merge from the.. remnants of 93 onto I-40, which runs straight through the city of Payton."
stop music fadeout 2.5
"About fifteen minutes from Payton we pull over at a rest stop which sits at a higher elevation than Echo."
"If you're looking in the right direction it gives you a great view of the town."
scene bg reststop
with dissolve
play background "reststop.ogg" fadein 2.5
"I stand outside the old, run-down restroom, a paw over my eyes as I stare out over the desert."
"A distant, hazy view of a group of small buildings huddled together signals where the town is."
"From this vicarious distance, it looks small and harmless, hard to imagine all of the things that happened there."
show Leo at center
with dissolve
l "\"Alright, how do I use this thing?\""
"I look over and see Leo fumbling with the camera, obviously worried that he's going to break it."
"I walk over and show him how to use it, checking the white balance and exposure myself."
"I wasn't too good with cameras, but the equipment manager at the university had given me a quick lesson on how to do things."
m "\"Alright, so I want you to zoom out from Echo, slowly, and while you do that I'm going to walk in frame, okay?\""
l "\"Yeah, okay.\""
"Leo hoists the camera up and looks through the viewfinder, ears perked up and smiling."
m "\"Alright, signal me when you're ready.\""
stop background fadeout 2.5
"I adjust the clip-on mic while Leo focuses the camera, then raises his paw, signaling that I should start."
"I walk into the frame, keeping one paw in my pocket, and using the other to gesture."
"I hope I don't look too awkward, I always feel like I do."
#Another image + music
scene bg echowide
with dissolve
play sound "mitt.ogg" fadein 3.0
m "\"Echo first began as a settlement in 1852 after James Hendricks discovered gold in a quartz deposit.\""
m "\"The town grew quickly in size and, once it began to serve as a junction along Prescott Railway, it reached a peak population of 6500 in 1877.\""
m "\"It was at this point in time that a peculiar phenomenon of mass hysteria took over.\""
m "\"Many say the reason this occurred was due to the discovery of a body within the gold mine and the circumstances surrounding that discovery.\""
m "\"While not much is known about this event, what {i}is{/i} known is that once it ended a large portion of the population left Echo.\""
m "\"Most of those who left settled in the nearby town of Payton.\""
m "\"However, the town still managed to prosper well enough until the '40s.\""
m "\"That's when the government stepped in to shut down the mine, as it became a federal law to divert all mining resources to the war effort.\""
m "\"The town's population sharply declined shortly thereafter and, by the 1950s, it had dwindled to approximately 2,000 people.\""
m "\"A shutdown of the Prescott railway in the 1960s, followed by the bypassing of Route 93 by I-40 in 1986 was the final nail in the coffin for the town.\""
m "\"By the '90s the population had dwindled to just 150 people.\""
m "\"My goal, however, is to investigate the first event which led to this town's decline, and possible demise.\""
m "\"What happened in that mine almost 150 years ago?\""
m "\"I've come to Echo to try and find out what information, if any, can be gleaned from the events of the past.\""
stop sound fadeout 7.0
"I wait for a few seconds, then look at Leo."
scene bg reststop
show Leo at center
with dissolve
play music "reststop.ogg" fadein 2.5
m "\"That good?\""
l "\"Uh, yeah, don't know how to stop this, though.\""
m "\"Here.\""
"I walk over to take the heavy camera off Leo's paws."
l "\"That was pretty good, you wanna be a reporter?\""
m "\"Mmh, maybe. I'd rather just write than be on camera, though.\""
c "\"YO, CHASE!\""
#Leone image
hide Leo
with dissolve
"Leo and I look up towards the car, greeted by the sight of a bright white ram's ass hanging out the back window of Leo's van."
"I don't really react. I mean, despite being self-conscious about his weight, Carl was pretty shameless about stuff like this."
"I'd probably seen his naked butt more often than I'd seen Leo's...and that was saying something."
c "\"Make sure you get a shot of m- HEY!\""
"At that moment, Flynn, who is sitting next to Carl in the back, reaches around and yanks the ram's pants down so that they hang around his knees."
"Even though Carl's pretty quick to pull them back up, I still get a pretty good view of his equally big white balls dangling between his legs."
"Leo snorts and I can see Flynn laughing his ass off while Carl punches him in the shoulder."
"Unfortunately for TJ, who is sitting in the middle row with Jenna, he was looking back at the time and probably got a much better view than I did."
"Now he's facing forward, covering his face while Jenna sits next to him, reading a book, looking uninterested."
m "\"Nearly 21 and he's still doing that, huh?\""
l "\"Yeah. It's a little more awkward without you three around, though.\""
"We head back to the car, and I grab the camera bag from the passenger seat to put the camera away."
c "\"Hey, did you see my ass!?\""
m "\"Saw more than that.\""
f "\"Your thing's about the horrors of Echo, right? It'll be a perfect fit, well, if you could even fit it on the camera.\""
"I stash the camera bag in the footwell before hopping in."

scene bg swadventures1
with fade
play background "parksounds.ogg" fadein 3.0
"Southwest Adventures is an amusement park right in the middle of Payton."
"It's decent enough that people come not just from Payton, but cities up to 100 miles away to vacation here."
"Because of this, it's usually crowded, and today is no exception; families and their kids are everywhere."
"It's a generally nice day, sunny, in the 80s, and it being on a Sunday added to the crowd."
"I didn't mind, though. The point of this is to hang out with my friends."
show Carl at right
with dissolve
c "\"I don't know about you guys, but I'm starving. Let's get some funnel cakes.\""
show Flynn at center
with dissolve
f "\"Jesus, Carl, we just got here.\""
c "\"Hey, I didn't have any breakfast.\""
f "\"You had breakfast alright; a blunt with a side of the munchies.\""
show Leo at left
with dissolve
l "\"It's no problem, you can do that while I plan out what we're doing.\""
"Carl ambles off, on his way to the funnel cake stand."
hide Carl with moveoutright
show Flynn at right with easeinright
"I snagged one of the park maps from the entrance and I hand that to Leo."
l "\"Alright, so usually when my family comes here we go clockwise to hit all the rides.\""
j "\"That sounds like a plan.\""
l "\"It's pretty crowded today, so we probably won't be able to do everything, but in this order we'll at least be able to ride Event Horizon.\""
show TJ Sheepish at farright
with dissolve
t "\"Y-you sure...the line is always so long for that ride...\""
"TJ's looking up towards a tall, spiraling, electric red steel roller coaster."
"It's definitely the most recognizable landmark in the park, you could see it from almost anywhere in Payton."
l "\"Yep! Fastest and tallest roller coaster in the West! I think it'll be worth it.\""
t "\"Oh...\""
"TJ rubs his arm with one paw, the corner of his muzzle twitching a little bit."
"I had forgotten about that."
"He used to have a pretty pronounced motor tic where the corner of his mouth would twitch up over and over again."
"It used to be a constant thing, but it stopped once we entered middle school. Guess it hadn't completely gone away."
l "\"You alright, TJ? We could skip the big rides if you-\""
show Flynn Annoyed with dis
f "\"Oh, hell, TJ, you're a fucking adult now!\""
t "\"No! It's fine.. I'm fine. I just haven't been on a roller coaster in a while.\""
"TJ snaps his head back towards us. He's all tensed up and the movement looks like a rubber band being snapped."
t "\"I'm riding all the rides with you guys.\""
"TJ walks off, his paws shoved deep in his pockets."
hide TJ with moveoutright
"I feel bad for him, and I wanna give him an out somehow, but that's when Carl comes back with his funnel cake."
"It's topped with ice cream, powdered sugar, and strawberries."
show Carl at farright with easeinright
show Flynn Annoyed at center
show Leo at farleft
with easeinleft
c "\"Anyone wanna share?\""
l "\"Yeah! That looks really good-\""
show Leo Neutral with dis
c "\"No? Alright, guess I'll have to eat the whooole thing.\""
f "\"Great, now we gotta wait for fatass to finish eating.\""
"Carl pulls his face out of the cake. Even with his white fur I can see the powdered sugar clinging to his chin."
c "\"Naw, I can eat in the line. We goin' on Event Horizon first? The wait'll be an hour long, at LEAST.\""
scene bg coasterline
with fade
stop music fadeout 5.0
"The line ends up being two hours long and by the time we get to the actual ride, I'm dying to get into a pool of any kind."
"To put it bluntly, an otter needs water."
#! readability?
"Part of the problem with living in Echo was that we didn't have any kind of indoor pool system in our house, being as cheap as it was."
"We ended up having to get an outdoor swimming pool, which was a pain."
show Leo at center with dissolve
l "\"Heh, nervous, Chase?\""
"I smirk at him."
m "\"I've ridden it before, Leo.\""
m "\"Though.. your tail's kinda down, sure you're not nervous?\""
show Leo Rejected with dis
l "\"Eh?\""
show Jenna Smilinghips at left with dissolve
j "\"Come on, Leo, let's ride the front!\""
l "\"Oh! Er...I don't know-\""
"I watch as Jenna pulls Leo towards the line for the front, which is twice as long as all the others."
hide Jenna
hide Leo
with moveoutleft
"I opt for the middle, and it just so happens that TJ comes with me."
show TJ Rejected at center
with dissolve
"His tufted ears had been poking straight up the entire time, muzzle giving an occasional twitch. I lean over to him."
m "\"You know, there's an exit over there for people who, uh, change their mind.\""
m "\"I'll bet you could slip out without anyone knowing, looks like not all of us are even gonna be riding the same train.\""
"TJ stares straight ahead, clutching onto the railing. I can see his sharp claws unsheathed, pressing into the metal and chipping away some of the red paint."
t "\"No, I'm fine.\""
m "\"You sure?\""
t "\"Yep! Perfectly fine, hahaha..hehe...\""
m "\"Well, we're in the middle, which is the best place to be, if you don't like roller coasters.\""
t "\"Uh-huh, yeah.\""
"I REALLY wanted to be able to get TJ to skip the ride, but it seems like he's pretty determined to do it, for some reason."
"Finally, our train comes along and I step in as two laughing and panting hyenas step out."
"Hyena 1" "\"Oh my god, that was the most intense-!\""
"Hyena 2" "\"Holy shit, dude, I know! I never get scared on rides and I almost fucking pissed myself!\""
"I do a quick check of the seat to make sure there isn't any actual piss before sitting down."
show TJ Depressed1 with dis
"I look up and see TJ standing on the edge of the platform, his eyes wide, one foot stuck out to get on."
m "\"TJ?\""
t "\"I...I uh...\""
"A bored-looking teenage fox comes by to check my lap bar and I stick out my paw."
m "\"Hey wait. TJ, you getting on?\""
"The fox goes from looking bored to mildly annoyed."
"Ride Attendant" "\"If you're getting on, you need to get on now. We can't hold up the entire ride for you, sir. The exit's that way where other adventures await.\""
"People around us are starting to notice."
"Unfortunately, Flynn, who is lined up with Carl towards the back, is paying very close attention, grinning like he knew this was going to happen."
show Flynn Teasing1 at farleft behind TJ with dissolve
f "\"Aww, TJ, too scared? Guess you're a pussy, after all!\""
show Carl at farright behind TJ
with dissolve
c "\"Shut up, Flynn. Hey TJ, when it gets real bad just say to yourself 'at least I'm not gonna die'.\""
f "\"Actually, a few people HAVE-\""
m "\"TJ!\""
"I yell up at him and that seems to jar TJ out of his trance."
hide Flynn
hide Carl
hide TJ
with dissolve
play sound "impact.mp3"
with vpunch
"He almost falls into the car as he stumbles into it, fumbling with his shoulder restraints before the fox attendant sighs and leans down to do it for him."
"I can see the red on the insides of TJ's ears as he blushes and I feel my own ears burn a little from second-hand embarrassment."
"Now that it's too late, I realize that we shouldn't have started with this ride. We should have started with something smaller to build up his confidence."
stop background fadeout 5.0
"I'm jolted back as the train moves forward."
t "\"Oh, gosh!\""
"TJ's paw lashes out and latches onto my arm."
t "\"Oh no, oh no, why am I doing this?\""
"I reach over to try and move his paw from my arm and back onto the handle on his shoulder restraints."
m "\"TJ, hold onto that. My arm....you're gonna-\""
t "\"Chase, quiet!\""
"I pause, staring at the lynx. I'm really not used to hearing TJ yell. He's almost puffed out to twice his size."
t "\"I just need some quiet right now, and-AH!\""
play sound "lifthill.mp3"
scene bg lifthill
with dissolve
"Our train begins its ascent up the first hill and I can feel TJ's claws pricking through my fur into the skin."
"He starts mumbling quietly to himself, his eyes closed."
m "\"TJ...are you praying?\""
"He doesn't say anything and soon, we've reached the apex of the climb."
"I give up on trying to move his paw and sit back, a little nervous myself. I really, really hope TJ doesn't completely lose it..."

stop sound fadeout 2.0
scene bg restroom
with fade
"I rinse the blood off my arm in a dirty theme park bathroom."
"It wasn't as bad as I thought it could have been, though TJ did start crying when we hit the first inversion."
"He had scratched the shit out of my forearm, grabbing it with BOTH paws once we started the descent."
"Unfortunately, Flynn and Carl were still on the platform when we rolled back into the boarding station."
"Flynn looked ready to lay into TJ again, but when he saw the tears he had the decency to hold back."
"I helped the shaking lynx out of the car and somehow we managed to stumble into the bathroom where he quickly hid in a stall."
"I should have forced him out the exit. He'd always had anxiety problems, though I think we all believed it was a childhood thing that he'd gotten over."
play music "intimate.ogg" fadein 20.0
"I don't know if he still takes medication..."
m "\"Hey, TJ?\""
t "\"Y-yeah?\""
#chat history
m "\"We should probably get back. Leo texted me that they're all waiting by the ride.\""
t "\"Yeah, I'll be out in a second!\""
"The cheerfulness in his voice is forced."
"I ignore the weird looks I'm getting from the other people in the bathroom and instead inspect my arm."
"The scratches are pretty superficial, so the bleeding has stopped."
"No one would notice it under the thick fur, even if it's tender as hell."
play sound "stalldoor.ogg"
show TJ Rejected at center
with dissolve
"I hear the stall door open behind me and, through the mirror, I see TJ come out."
"He sees me looking over my arm and his face crumples up again."
t "\"Chase, I'm sorry. Is it bad?\""
"I really don't want him to start crying again."
#!! maybe emdashes around "almost every day"?
"TJ cried a lot when he was a kid, almost every day, and even at 19, it seems like he's still pretty susceptible."
m "\"It's fine, it's fine! Doesn't even hurt.\""
t "\"Ah...well, th-that's good.\""
"We stand there awkwardly for a few seconds, then I air out my shirt, which was starting to stick to my sweaty body."
m "\"Listen, it's honestly getting way too hot for me to wait in lines all day. I think I'd rather just sit down and watch some shows, or something.\""
t "\"Oh yeah?\""
m "\"Yeah, uh, you wanna do that with me?\""
"TJ's ears come up a little, and he clutches his paws together, the fidgeting subsiding a bit."
t "\"Yeah, Chase, I think that'll be fun...\""
"I can tell he's at least a little relieved."
stop music fadeout 5.0
scene bg swadventures1
with fade
"We both head out back towards the ride and I spot the four of them waiting by the exit."
#work on positioning
show Carl Depressed at left
show Jenna Depressed at farleft behind Carl
with dissolve
"I furrow my brow as I spot Carl crouched on the ground, Jenna kneeling next to him and rubbing his back."
m "\"Hey, everything alright?\""
play music "neutral.ogg" fadein 5.0
show Jenna with dis
"Jenna looks up, a sympathetic smile on her face."
j "\"Carl's not feeling too good.\""
m "\"Uh, you wanna sit on a bench, or something?\""
c "\"If I move, I'm gonna...\""
show Flynn at farright
with dissolve
f "\"That's what you get for stuffing your face right before the ride.\""
j "\"You think they sell ginger pills here, or ginger ale, at least?\""
c "\"Ergh...A joint would be nice.\""
t "\"There are some vendors over there, I'll go check.\""
"I'm actually kinda glad everyone's preoccupied with Carl right now; takes some of the heat off of TJ."
show Leo Neutral at center behind Carl
with dissolve
l "\"Let's move you to a bench, it'll be better if you're sitting down.\""
"Slowly, Jenna and Leo lift Carl up, and now I can see from his face that he really is ill."
"To the average person our little outing might already seem like a disaster, but this is perfectly typical for us."
"Nothing ever went according to plan."
scene bg bench
with dissolve
"We sit Carl down at a bench and he bends over, his face in his hands as he moans softly."
show Carl Depressed at center
with dissolve
c "\"Urrgghh...\""
show TJ Neutral at right
with dissolve
"TJ comes back with a medium-sized cup in his paws. He sits next to Carl."
t "\"No ginger ale, but they did have some lime soda.\""
#! reduces repetition of "it" (especially with "bit" in the line)
"Carl takes it and sips a bit before sitting back and belching."
c "\"Ugh...fuck it, I'm done, guys.\""
f "\"What!? What're you gonna do all day, sit there?\""
t "\"Actually, me and Chase are going to go see some shows. You can come with us.\""
scene bg hedge
show Flynn Annoyed at right
show Leo Neutral at left
with dissolve
f "\"Ugh.\""
l "\"Guys, we were doing this to hang out with each other, remember?\""
f "\"Aw, leave 'em. We're wasting time.\""
hide Flynn
with moveoutright
"Flynn turns and walks off, his hands shoved in his pockets, hunched like a stone gargoyle."
"He definitely looked the part, being a lizard."
"...Damn, that was probably a bit speciesist."
show Jenna at right
with dissolve
j "\"Well, we all have our phones. Text us, alright?\""
m "\"Sure!\""
hide Jenna with moveoutright
"Jenna turns and follows Flynn, but Leo hesitates a moment."
"He looks at me, before eventually turning to follow Flynn and Jenna."
hide Leo with dissolve
stop music fadeout 10.0
"Five minutes later, Carl's stomach settles to the point where he's able to get up and walk."
"At this point, I'm completely wiped out and I just want to sit down."
scene bg stage
with fade
play background "amphitheater.ogg" fadein 3.0
"I point out the first stage we see and they agree."
"I sigh gratefully when I sit down."
show Carl at right
with dissolve
c "\"You look tired as shit.\""
"I crack an eye open to see Carl giving me a sidelong glance."
m "\"I don't sleep very well in motel beds.\""
show TJ at left
with dissolve
t "\"I actually woke up around...two? You were gone.\""
"Now TJ's looking at me, too, and I feel my gut clench for a second."
m "\"Yeah, I tried to go for a walk down the street, hoped it would help me get tired.\""
t "\"Hmm...\""
c "\"Well, if that happens again, you can just walk over to my house. I'm up until like, three every night.\""
m "\"Wow, why?\""
"Carl shrugs, leaning back and sticking his hooves up against the chair in front of him, earning him a dirty glance from its occupier."
c "\"Games, mostly. Sometimes I read...\""
"Carl rubs his chin, opening his muzzle, closing it, then opening it again."
c "\"You know, it WOULD be pretty cool if you spent the night one of these days. That house can be creepy as hell when you're the only one in it.\""
m "\"You're alone?\""
c "\"Yeah, parents are vacationing in the 'Regal Paradise' having a bloody good time, they tell me.\""
"Carl tries to put on an accent, but doesn't do a very good job of it."
m "\"Oh...did you want to go with them?\""
"Carl blows a raspberry, laughing."
c "\"Heh, not really. Mom told me right away that weed isn't legal there either, so I took that as them not wanting me to come along.\""
m "\"Oh...\""
c "\"They did say that the chocolate there is real, whatever that means, and that they'd bring me some.\""
c "\"Guess I'm not enough of a fatass yet.\""
m "\"Come on, Carl.\""
c "\"But dude, I'm getting there. Soon, all I'll have to do is stand in front of the mirror, block out my face, and jerk it to my moobs.\""
show TJ Neutral with dis
"I make a dumb snorting, croaking sound and I can feel TJ looking at the two of us disapprovingly."
c "\"Not the hardest thing to do when you're high.\""
m "\"Wait, so you've actually done it?\""
"Carl shrugs, smirking at me."
"I reach out and grab his chest. From what I can tell, there's a pretty firm set of pecs under there."
"Carl puts a mock horrified look on his face."
c "\"Sexual assault! He touched my breast!\""
m "\"Oh, whatever, Carl, they're harder than mine!\""
c "\"So now we're teenage girls in the locker room comparing racks?\""
m "\"Hey, you're the one that brought up tits.\""
c "\"You know what, I can see it...Yeah.\""
c "\"You're the hot preppy one everyone likes, I'm the big fat chick you're all nice to, but call Big Thunder Mountain behind her back, and TJ—!\""
"TJ hadn't been paying attention, distracted with watching some dancers come on stage. He looks innocently at us."
t "\"Huh?\""
#!! maybe? This is an oddly-phrased line originally
c "\"You're the cute, naive Christian chick that only takes it up the butt so she can stay a virgin.\""
#Malcolm line
show TJ Surprised with dis
t "\"Whaaa!?\""
show Carl Teasing with dis
c "\"Let me feel your boobies, I wanna compare!\""
t "\"What in the world are you ta—NO!!!\""
c "\"Small, but perky!\""
"After a few seconds of tussling and Carl getting smacked in the nose by TJ, somebody shushes us from behind and we're forced into silence."
"The show starts off with a bunch of mice having a weird sort of hoe-down. TJ's really into it and actually starts clapping along."
"I smile; TJ could definitely be kinda cute sometimes. Carl just rubs his nose and leans back, watching with a smirk, as if the whole thing is a joke to him."
"At this point, my eyelids were feeling really heavy. At most, I'd gotten maybe four hours of sleep last night."
"I think about leaning my head back, but the backs of the seats are pretty low and I'd just end up with my head hanging over the back."
"Leaning forward would just be impossible...I {i}could{/i} lean on one of my friends, I don't think they'd mind..."

menu:
    "Lean on Carl":
        show Carl at center
        with moveinright
        hide TJ
        with dissolve
        "Carl is definitely the better choice."
        "Bigger and probably softer, he'd make a nice pillow."
        m "\"Carl, I'm gonna use you as my bed.\""
        c "\"Huh?\""
        "I put my head on his shoulder and close my eyes, feeling the soft, puffy, sleeveless hoodie and his bulk under my cheek."
        "Weirdly enough, he was pretty damn sturdy. I had expected him to feel like a pillow puff."
        c "\"Damn, Chase. You that tired?\""
        m "\"Mmh.\""
        c "\"Well, alright then.\""
        "I feel him shift, and suddenly he's putting an arm across the back of the bench, giving me more support."
        "The gesture makes me feel a little warm. I can feel TJ's eyes on us, but I ignore him, enjoying the position of intimacy."
    "Lean on TJ":
        show TJ at center
        with moveinleft
        hide Carl
        with dissolve
        "TJ might be smaller, but he's definitely an easy guy to convince, especially if he thinks he's helping someone out."
        m "\"TJ, can I lean on you for a bit?\""
        t "\"What, why?\""
        "He looks a little uncomfortable."
        m "\"I'm soooo tired, man.\""
        t "\"A-alright...\""
        "I lay my head in the crook of his neck and I feel him tense up a little, but after a while he relaxes."
        "There's some heat coming off his neck, and I'm pretty sure he's blushing. It's not too bad, though. He may be slender, but his fur is pretty damn soft."

"The sounds of the clapping and fiddles starts to drift away as the lack of sleep takes its toll..."

scene bg black
with slow_dissolve
stop background fadeout 3.0
play music "creep.ogg"
"I feel along the rough edges of rock and dirt. The only thing I can hear is the shower of debris I'm knocking to the ground."
"The air is stale and I have the vague feeling that I'm suffocating."
"I keep going, I'm gonna reach the end eventually, just have to keep moving. I can tell that I'm going down, deeper and deeper."
"The space around me is growing smaller and smaller and soon, I'm hunching so that my head doesn't scrape the ceiling."
"I can hear footsteps, not quite in synchrony with my own."
"They aren't any kind of footsteps that I've heard before though."
"I stop and listen."
"There's definitely the sound of feet, but not like they're walking, it's like they're stamping down on the ground, making as much noise as possible."
"This is accompanied by a slapping sound, as if someone is smacking their paws on the ground as well."
"I imagine a canine toddler, still insisting on walking on all fours while throwing a tantrum. It's heavier, though, like an adult is doing it."
"That image makes the nape of my neck prickle, but I'm not scared..."
"It's not long after I've stopped that the noise stops as well, just ten feet behind me. I turn, watching the darkness."
m "\"I knew you'd come back, they always do.\""
"My voice sounds clogged, muted, like the rocky walls are just sucking up the sound instead of bouncing them down the tunnel."
"The stamping starts up again, loudly, coming towards me at full speed. Now, I can hear sobbing, sniffling, and a strange, guttural grunting."
"It's just feet away."
m "\"You're only moving in circles.\""
"It veers away just as the words leave my mouth, going back the way it came. I stand there a while, listening until I can't hear it anymore."
"I turn and continue on, feeling the walls again as I make my way lower and lower."
"The smell hits me right as my paws hit it; slick and slippery, blood coats the walls my paws run along like thick oil."
"It's warm and fresh, and now I know I'm getting close. A voice abruptly echoes down the tunnel, it's not far away at all."
"\"{cps=15}{font=Daubmark.ttf}I knew you'd come back, they always do.\""
"I make my way closer and closer and now, fear pricks my heart."
"\"{cps=15}{font=Daubmark.ttf}They always do...\""
"I hear muffled screams now, as if someone is yelling with their mouth closed."
"Now the fur is standing up all over my body, but my feet won't stop, I keep going, I'm getting closer and closer."
"\"{cps=15}{font=Daubmark.ttf}You're only moving in circles.\""
"I'm here, it's right here in front of me, and now I'm reaching out to it, reaching out to touch it. I can't stop, I can't stop-"

stop music
play background "amphitheater.ogg"
scene bg stage
show Carl at right
show TJ at left
m "\"*Gasp!*\""
#variable
"I jump, my head jerks up and my eyes snap open, looking around wildly. It's like I just came up from being underwater too long."
show Carl Surprised
show TJ Surprised
with dis
c "\"Shit!\""
t "\"Whoa!\""
"TJ and Carl both jump shortly after I do. I look back and forth, as they stare wide-eyed back at me."
"It takes me a second to realize I'm still at Southwest Adventures, at the stage, watching shows."
c "\"Jesus fuck, dude, you alright?\""
t "\"Carl!\""
"I lean forward and rub my face in my paws, trying to stop shaking."
m "\"I'm fine, I'm fine....just a really bad dream.\""
"I feel a small paw on my back as TJ rubs it."
t "\"What about?\""
m "\"I uh...\""
#Tell Truth or not?
m "\"I'm...not really sure. Just in a really dark place...and some things were in there.\""
c "\"Huh, that does sound pretty creepy. What kinds of things?\""
"I think for a minute."
"The weird, crawling thing, the screaming thing...I pull my head up, looking towards the stage, which is empty right now."
m "\"It...it doesn't matter, it was just a dream. Hey, what happened to the show?\""
"Carl chuckles next to me, leaning back again."
c "\"Ya missed 'em, dude. We've seen like, three shows.\""
t "\"Yeah, they even had a segment with otters doing water tricks! We thought about waking you up for it, but you were in a really deep sleep.\""
"That's too bad, I always loved seeing my people laughed at for the swimming clowns that we are."
m "\"How long's it been?\""
"Carl checks his phone, which he already has out."
c "\"Been about three hours, could probably get some lunch now.\""
"Damn, I'd been out for a while. I'm surprised I hadn't at least woken up a few times, considering the uncomfortable position I'd been in."
t "\"I guess you feel better, then?\""
c "\"Yeah, been feelin' better for the past two hours. Now I'm hungry.\""
#"I've composed myself for the most part and take out my phone to text Leo. It's already 2 PM, so I tell him we're hungry, and that we should meet up."
#"He gets back to me pretty quick, saying that they are mostly done with the big rides."
#"He also says that we should meet at the center of the park in the food court."
"It's already 2 PM and I've composed myself for the most part, so I take out my phone to text Leo."
call text_chase("leo") from _call_text_chase_5
$ renpy.pause(0.5, hard=False)
play sound "texting2.ogg"
$ renpy.pause(1, hard=False)
call text_0("m", "We're kinda hungry. We should meet back up.") from _call_text_0_5
""
"He gets back to me pretty quick."
play sound "phonebuzz.ogg"
$ renpy.pause(1, hard=False)
call text("", "k. mostly done wit rids anwya") from _call_text_6
""
call text("", "meet @ food crt") from _call_text_7
""
call text_end from _call_text_end_5
stop background fadeout 3.0
scene bg foodcourt
with fade
"We meet Flynn at a table in the food court where he's already bought some pizza."
play background "parksounds.ogg" fadein 3.0
"Carl immediately sits down and pries open the box, taking out a few slices."
show Flynn at center
with dissolve
f "\"Ugh, of course. You guys have fun?\""
c "\"It was alright, watched a few shows about our state's speciesist history...Chase took a nap.\""
"Flynn eyes TJ, who doesn't say anything as he sits to take out his own slice of pizza, a bit more daintily than Carl had."
f "\"Feelin' better, Teej?\""
t "\"Yeah, I'm fine.\""
"TJ nibbles on his slice of cheese pizza."
f "\"Yeah, well, the pizza here is a hell of a lot scarier than any of the rides, so you're braver than I am.\""
#More
m "\"Where're Leo and Jenna?\""
"Flynn rolls his eyes and nods towards a row of carnival games to the right of the court."
f "\"Fightin'.\""
f "\"They've been playin' those games for a fuckin' half hour already.\""
"I'm not surprised."
"I grab my own slice of pizza in a napkin and make my way over there."
scene bg carnival
with dissolve
"Keeping with the theme of the Old West, the carnival section of the park is decked out with fake saloons and brothels."
"I spot them pretty quick: Leo's holding a pink unicorn, and Jenna's carrying a green dragon."
"They seem to be in pretty good spirits, though Leo's grin is a little tight."
m "\"Looks like a pretty successful haul, you guys!\""
show Jenna Smilinghips at left
with dissolve
j "\"Hey, Chase!\""
"Jenna's grinning, looking a little smug as well."
m "\"You guys finished? We're eating now.\""
"Leo shifts the giant unicorn around."
show Leo at right
with dissolve
l "\"Yeah, we're pretty much done, I think.\""
m "\"Daaamn, Leo, you must have won something pretty hard to get that!\""
show Leo Embarassed with dis
l "\"Um...\""
show Jenna Smiling with dis
j "\"Yeah, that was me.\""
"I look over at the green dragon Jenna's holding."
m "\"But what about that—\""
j "\"Yeah, I won this, too.\""
m "\"Oh, uh, well, I'm sure you've won a couple?\""
l "\"Um, actually...\""
j "\"Yeah, I've beaten him at every game.\""
l "\"Hahaha! Yeah, well, you're visiting, I want your memories of this vacation to be good!\""
l "\"Obviously it's getting to your head, though...\""
j "\"Oh please.\""
j "\"Chase, you should have seen his face; sour grapes the whole time.\""
m "\"Oh really?\""
"I would usually stay out of stuff like this."
"Leo always got a little carried away when it came to competition, especially when I was around, but it was kinda funny seeing him act like this."
show Leo Rejected with dis
l "\"Let's just go eat.\""
j "\"Wait, there's a high striker! Why don't we show Chase who's stronger, huh?\""
"Leo contemplates that for a second, but seems pretty confident about this one."
"He's literally almost twice the size of Jenna."
l "\"I don't know if that's very fair to you, Jenna, I mean...\""
"He lets that sit, and honestly, I have to agree."
"Jenna, though, gets a little fox gleam in her eyes that I knew meant she thought she knew something we didn't."
stop background fadeout 3.0
j "\"Afraid I'm gonna woo your ex?\""
play loop "carefree.ogg" fadein 3.0
"Wow, Jenna's going all out."
"My muzzle flushes under the fur, but that only seems to decide things for Leo."
"A confident smile replaces the sheepish one from before."
l "\"Oh yeah?\""
show Leo Wry with dis
"He flexes his shoulders and sticks out the stuffed unicorn to me."
"I stuff the last of the crust into my mouth and reach out to take it."
"Jenna does the same and now I'm hugging two massive stuffed animals to my sides, tripling my girth."
l "\"Alright, let's do this.\""
#Scene Change
show Leo Wry at farright
show Jenna Smiling at center
with easeoutright
show Carny at farleft with dissolve
car "\"Step right up, test your strength! Three dollars, three tries. Ring the bell and win a prize!\""
hide Jenna
with easeoutright
show Leo Wry at right with easeinleft
l "\"I'd like a try.\""
car "\"Ah, we have a taker! Big strong wolf like you would have no problem at all! Three dollars, please!\""
"Leo hands over the money and the carny hands him a mallet."
"Leo points it at me with a grin."
l "\"This one's for you, {i}chula{/i}.\""
#the moment that started it all#
"My heart skips a beat; he hasn't called me that in a while."
"But I decide to play along."
m "\"Don't disappoint me, Leo. I really want that stuffed gryphon!\""
"I point to the gryphon on the carny's long shelf of toys."
l "\"Sure thing.\""
"Leo spreads his legs and squares his shoulders before raising the hammer, and bringing it down hard onto the rubber-looking pad."
play sound "mallet.mp3"
with vpunch
"It's a pretty hard hit, but the chaser only raises up to the 40 mark."
car "\"Oooh, almost, sir wolf, try again!\""
show Leo Questioning with dis
"Leo's brow furrows, and now I'm not so sure this was a good idea."
"He raises the mallet again and grunts as he brings it down even harder, causing the contraption to shake a little."
play sound "mallet.mp3"
with vpunch
"This time, the chaser shoots up to the 70 mark."
car "\"Even better! This time, put your back into it!\""
"I can hear Leo growling a little as he raises the mallet a final time and brings it down with a snarl, all the muscles in his arms standing out."
play sound "mallet.mp3"
with vpunch
"I'm pretty sure I feel the ground shake this time as the impact causes more than a few heads to turn."
"This time, the chaser only goes up to the 60 mark."
show Leo Rejected with dis
"Leo gapes at the game."
car "\"So close! Three more dollars will get you three more tries! Would you like to try again?\""
show Jenna Teasinghips at right
with dissolve
j "\"Nope, my turn!\""
"Jenna already has her money ready and hands it to the carny."
car "\"Oh-ho! A little battle between the sexes, eh?\""
car "\"Well step right up my fair fox maiden, how will you fare against the big bad wolf?\""
"Leo reluctantly hands the mallet to Jenna."
l "\"Alright, beat 70.\""
"Jenna points the mallet at me, winking."
j "\"Don't worry, Chase, I'll get that gryphon for you.\""
"Leo snorts loudly, folding his arms and looking pretty annoyed."
show Leo Neutral with dis
l "\"Good luck, I was hitting that thing as—\""
show Jenna Teasinghips at center with easeinleft
show Leo Neutral at farright with easeoutright
"Before he can finish, Jenna raises the mallet into the air and puts it into a graceful swing."
"It's as if she were chopping wood as she brings it down hard into the rubber pad."
"It lands precisely and cleanly, in sharp contrast with Leo's sloppy hits."
play sound "mallet.mp3"
with vpunch
play sound "ding.ogg"
show Leo Surprised
show Jenna Smilinghips
with dis
"I stare, Leo stares, the carny stares."
"Jenna simply raises her paws in the air."
j "\"Yay!\""
"A few onlookers around us laugh and cheer."
car "\"O-Oh my! The fair fox has won! Come over and pick your prize!\""
hide Jenna
with moveoutright
"He glances at Leo."
car "\"Sorry buddy.\""
"The feline shoots a sympathetic, but also amused smile Leo's way before turning to the onlookers."
car "\"See that? A female fox, half the size of this male wolf has rung the bell. Could one of you be next!?\""
hide Carny
show Leo
with dissolve
"Leo looks mortified, but quickly changes his expression to a sheepish grin."
"He doesn't seem to want to look at me."
l "\"Uh, good job, Jenna.\""
show Jenna Smiling
with moveinright
"Jenna bounds back to us, carrying the big stuffed gryphon."
j "\"Give those ones to Leo, so I can give you this.\""
"I hand off the stuffed toys to Leo, who grumbles a bit as he takes them."
l "\"Damn thing's rigged.\""
"Jenna hands me the gryphon."
m "\"Thanks, Jenna, that was really-\""
"She leans over and pecks me on the cheek."
show Leo Surprised with dis
"I see Leo's eyes widen as she does it, his ears standing straight up."
j "\"Aww, it was nothing.\""
"Leo stands there for a few more seconds, working his jaw."
l "\"Awesome.\""
hide Leo
with easeoutleft
"He turns away and leaves, his arms still wrapped around the giant, stuffed toys."
"Jenna starts laughing."
m "\"Jenna!\""
j "\"Oh hush, he'll get over it. He's just so damn fun to tease!\""
"I have to agree, but not when I'm being used to do the teasing."
m "\"He's still really sensitive about the whole thing.\""
j "\"You guys talked it over, didn't you? Anyway, aren't you gay?\""
"I take a deep breath."
menu:
    "Yes, I'm gay.":
        $ Jenna_Route = "Gay"
        m "\"Yeah...\""
        j "\"See? He's got nothing to worry about!\""
        "I'm not in the mood to go in-depth about my sexuality."
        "Saying anything else confuses people."
    "No, I'm bi.":
        $ Jenna_Route = "Bi"
        m "\"Not really.\""
        j "\"Hm?\""
        m "\"I mean, yeah, obviously I liked Leo, but I've liked girls, too.\""
        j "\"Oh, interesting...\""
        j "\"Hmmmm...\""

"I sigh and rub my eyes with a paw, still a little tired."
j "\"Hey, don't tell Leo that I work at the state fair every year.\""
m "\"Wasn't planning on it.\""
stop loop fadeout 15.0

scene bg swadventures3
with fade
#intimate music
"The rest of the day is pretty relaxing. We ride a few of the more mellow rides."
"Leo seemed to cheer up when I volunteered to sit next to him on the Ferris wheel."
"TJ even built up his courage to the point where he rode the swinging ship."
#! check intended commas here, could be structured differently if desired
"Flynn and Carl rode the slingshot ride together and, with the video feed from the ground, I think it's the first time I've ever seen Flynn scared."
"Carl did end up barfing after that one."
"By about 6 PM, everyone's tired enough that we agree to head back."
play background "reststop.ogg" fadein 7.0
"I'm still exhausted, so I sleep for the half hour it takes to get back to the motel."

scene bg parkingloteve
with dissolve
"When we do get back I notice how good the sun looks right now."
"With a sigh I remind myself that I'm here to actually get a project done, not just play around."
"So as everyone sits in the motel I let them know I'm about to shoot some B-roll, gathering up my equipment and heading out into the heat."
"Dragging it outside, I set it up, sweating even under the evening light."
"Even this late in the day the heat was pissing me off. For some reason it's a lot cooler in Pueblo."
"My mind drifts back to the many days of summer under the blazing sun, the temperature rarely dipping below a hundred."
"I'm amazed poor TJ never had a heat stroke."
"When I put my eye to the viewfinder, I'm a bit disappointed at how broken down the town looks even with the amazing backdrop."
m "\"What a dump...\""
j "\"I'll say.\""
"It's then that I hear footsteps and talking behind me. I pause my recording and turn around."
show Leo at left
show Jenna Smilinghips at right
with dissolve
l "\"How's the filming?\""
m "\"It's alright. Kinda ran out of sun, but it's okay; Echo looks like crap no matter what kind of light you shoot it in.\""
j "\"Do you need us to keep quiet?\""
m "\"Naw, I'm just shooting B-roll. Was about to come back in.\""
l "\"Let's stay out here a minute. Carl and Flynn are...getting a little loud.\""
l "\"Besides, I want to talk to you two!\""
show Leo at center with moveinright
"He wraps an arm around Jenna, and reaches out the other one to pull me in so that we're both flanking him."
"I feel my shoulder press into the warm bulk of his side and chest."
"He'd always been taller than me (my eyes barely came up to his chin) but now it seemed like he was almost twice as wide."
"He'd definitely put on more muscle since I last saw him."
"While he was always pretty muscular, he'd been more on the lean side. Now his chest and biceps pulled his shirt tight."
"It felt...nice, though, like something very sturdy wrapped in velvet. I suppose it was a mixture of adding on both muscle and fat."
"I'm at least happy to see he's gotten over his little defeat to Jenna."
l "\"Look at us, the OG crew!\""
"Leo's strong voice vibrates from his body into mine. The effect is tranquilizing, and I feel myself relax."
j "\"Together again.\""
m "\"The only thing I miss about this town.\""
"Leo is referring to the fact that he, Jenna, and I were the original three in our group of six to become friends."
"Later we would add TJ, then Carl, and finally Flynn and Sydney. Leo had really been the one to unite us all."
j "\"I remember when you first got here everyone was afraid of you, haha.\""
l "\"I remember when I first got here I found a bunch of {i}gringos{/i} who wouldn't even talk to each other.\""
"We all went to the same schools in Payton and had had our different friends there."
"When Leo moved in he thought it was strange that the kids in Echo didn't hang out together."
"As I entered middle school and high school I cycled through a ton of different friends, but the ones in Echo always stayed the same."
l "\"Remember when we'd always have sleepovers at Chase's place?\""
j "\"Of course, I'd kick your ass at Claws of Fury all the time.\""
m "\"I remember. I used to think you guys were only friends with me for my video games.\""
"Many times I'd fallen asleep to the flickering of the old CRT television set, watching the outlines of Jenna and Leo twist side to side as they played."
"I would wake up hours later only to find them still playing."
"It was weird; Jenna and Leo get along really well, but there is a bit of a competitive streak between the two."
"Actually, it's one of the few things that gets Leo genuinely angry."
"I think he even broke one of my controllers once..."
l "\"How long has it been since we first met?\""
j "\"Well, when did you move in?\""
l "\"Uh, I think it was in 2000?\""
m "\"So take 2015 and subtract 2000. What does that leave you with, Leo?\""
"Leo looks sideways at me, and smirks. There's a flash of a white canine as it appears from under his lip for a moment."
l "\"You think yourself a real hotshot now that you're in college, eh?\""
"I smirk back, though I know my canines aren't as impressive."
m "\"Pretty much, yeah.\""
l "\"Well, you'll always be those little brats to me.\""
"I feel Leo's wagging tail swat me in the butt."
"I'm not really sure how I feel about that."
l "\"Speaking of which, are you two getting along over there?\""
"Jenna looks at me around Leo's broad chest."
j "\"Yeah, sort of.\""
m "\"Yeah, we haven't had many chances to hang out.\""
#Leo surprised.
l "\"Eh? Why not?\""
j "\"Well, it's college. It's also a pretty large university.\""
j "\"I don't even think we've ever seen each other in passing.\""
m "\"Yeah, things are different. But Jenna, we should do something together soon, before you graduate.\""
j "\"Definitely.\""
"Leo still looks a little disappointed that me and Jenna aren't keeping up at the university, but I don't know why."
"She had her friends, I had mine, and we did talk sometimes..."
"Jenna nudges into Leo, causing us all to sway."
j "\"And speaking of that, when are you going back to Mesa?\""
"Mesa is the community college in Payton. Leo went there for a few semesters before taking a break..."
"And by break, I mean he quit."
show Leo Depressed with dis
l "\"We'll see, I'll have to talk to my parents.\""
l "\"It's just.. starting to get really busy.\""
j "\"Why don't they hire more people? You know, you would have graduated by now...you would have had your MASTERS by now.\""
"Leo sighs."
l "\"It's about committing to the family business, not the help he needs.\""
show Jenna with dis
"Jenna rolls her eyes, blowing out some air and ruffling the tuft of fur on her head."
j "\"Wolves and their families. You should try thinking and speaking for yourself sometime.\""
j "\"If I hadn't done that I'd still be stuck in that crank house.\""
"Jenna flicks her head vaguely in the direction of where she used to live."
"Jenna is the only one, aside from Carl, who has family still living in Echo."
"I wonder if she's going to visit them, even though I'm pretty sure I already know the answer to that."
"I see Leo tighten his arm around her shoulder, but she goes on without missing a beat."
j "\"And you can start with our otter, here.\""
stop music fadeout 3.0
show Leo Neutral with dis
"I look up, caught unawares."
m "\"Huh, what?\""
l "\"Jenna...\""
j "\"I'm serious.\""
"Jenna puts her paw up in Leo's face, cutting him off."
j "\"I am NOT going to spend this entire week with you asking me when or how you should do it. Let's rip off the band-aid now. Chase—\""
l "\"Jenna.\""
show Leo Depressed with dis
"There's a warning tone in Leo's voice as he pins back his ears and drops his arms from our shoulders."
"I already know what's happening. It's been a long time coming...I take a step back and fold my arms, looking to the side."
j "\"Chase, Leo has some things to say to you, and yes, it's about THAT. Now I'm going to head back in and make sure Carl didn't light up in the bathroom.\""
show Leo Annoyed with dis
l "\"Jenna!\""
hide Jenna with dissolve
"His tone changes to exasperation as Jenna turns on her heel and leaves."
"Judging by the curl in her tail, I can tell that she's pretty satisfied with what she's just done."
show Leo Depressed with dis
"I return my attention to the road; I couldn't really bring myself to look at him right now."
"We both stand there for a minute, three feet apart. I hear Leo scuff the ground with his foot, then sniff as dust rises up from the ground."
"I hear him draw in a breath a few times, as if he's going to say something, but ends up blowing it out with a sigh."
"We were never good at this, probably why it ended up failing like it did."
m "\"Leo...\""
l "\"I'm sorry, Chase.\""
play music "intimate.ogg" fadein 10.0
m "\"F—for what?\""
l "\"Not talking to you about this when I should have. Talking to Jenna about it when I should have been talking to you...\""
"He reaches out and sets a paw on my shoulder, the silver anchor on his wrist glinting just a bit in the fading light."
"He's smiling at me, but I grit my teeth."
m "\"Why are you still wearing that?\""
l "\"I...\""
#! his eyes are not originally on the bracelet, so they can't flick "from" it
"His eyes flick to the bracelet and then back to my face, expression turning defensive."
l "\"Why aren't you still wearing yours? Don't you remember what we said?\""
"I sigh, looking at the scattering of clouds behind Leo's head. They're tinged a soft pink from the fading sun."
"The sunset is almost the same color as Leo's fur..."
m "\"Leo, we were teenagers...\""
l "\"That's not an answer.\""
"He cuts me off and I look back at him."
l "\"I told you, they weren't...love bracelets.\""
l "\"They weren't just about our relationship, they were about everything: our friends, family, memories-\""
m "\"Echo.\""
"I raise my voice above his, cutting him off this time."
m "\"They were about Echo, Leo...\""
"We stand there a while, and Leo's looking closely at me, expectantly, his ears tipped forward."
"His eyes pierce me like amber shards. It was always hard to look him in the eye during our...arguments."
scene apology
with slow_dissolve
m "\"What, do I have to say it?\""
l "\"...\""
m "\"Alright, fine...\""
m "\"I fucking hate this place, everything about it. It's the most miserable goddamn place I've ever been.\""
l "\"How many places have you even been?\""
m "\"Enough to know that it's miserable. Most everyone here's old, obese, on welfare...half of them are probably on meth.\""
"Leo pulls in a deep breath and blows it over my head. I can smell the bell peppers on his breath."
l "\"No one likes it here, Chase.\""
m "\"I mean, it was an anchor.\""
"I'm half laughing."
m "\"Just looking at it made me feel like I was still tied to this town. I didn't need it reminding me of all that awful stuff.\""
m "\"I know it was supposed to symbolize our being each other's...rocks, or whatever, but it stands for a lot more than that.\""
l "\"But a lot of good things happened here, too! No one should forget where they come from.\""
m "\"Sometimes I wish I could.\""
"At this point Leo's deflated a bit, going into a slouch, his ears lowered."
l "\"Wait, you said 'was'. You didn't...you didn't get rid-\""
m "\"No.. no I still have it. It's just in a drawer in my dorm room.\""
m "\"Honestly, if it was anything else, like one of those infinity bracelets we saw, I wouldn't have trouble wearing it...\""
l "\"Well fuck, why didn't you say anything when we were buying them?\""
m "\"I didn't know it was gonna be a problem!\""
"Leo takes in a deep breath again before blowing it out, puffing out his cheeks this time."
l "\"{i}Puchica{/i}, otter.\""
"He puts a paw to his eyes and holds it there for a few seconds. It's a pose I'm pretty familiar with."
"Even though I haven't seen it in a few years, I'm hit with a wave of memories, mostly of me frustrating, or embarrassing Leo somehow."
"We'd decided on the anchors mostly because they looked pretty."
"Leo had referenced some wolf metaphor about roots and how we're always drawn back to them."
"Also some bullshit about how otters were great sailors, but really, it was just the aesthetic."
"For some reason over the years I'd begun to associate the anchor with being stuck in Echo."
"It was when I started connecting the anchor to Sydney that I'd taken it off."
"It was too much."
l "\"{i}Anyway{/i}—\""
"Leo brings me back to the present, and I focus back on him."
l "\"What I was trying to say was that I'm still not okay with how you left.\""
m "\"Leo, I said I was sorry, and I still am—\""
l "\"Or how you stopped talking to me for a while.\""
m "\"I—okay, I was a {i}kid{/i}.\""
m "\"I thought I had a good tactic. Like Jenna said; rip off the band-aid, you know? We did start talking again...\""
l "\"It was more like you punching me in the gut, then kicking me in the balls.\""
l "\"The problem was that you didn't even give me a chance to say anything, or at least tell me why before you broke it off...\""
"I stay silent for a while, then finally look up, setting my jaw."
m "\"Like I said, I was young and dumb, I didn't know how to handle it.\""
m "\"I can keep apologizing, or...we can move on and make the most of this.\""
m "\"We only have one week, and I wanna have fun.\""
scene bg parkingloteve
show Leo Neutral at center
with slow_dissolve
"Leo looks to the side, paws on hips, as if contemplating, then looks back at me with a smile."
l "\"Alright, fine...but don't think you're off the hook! I still want to talk soon.\""
m "\"Soon, just not right now.\""
"I stand there awkwardly for a few moments, then, because it feels appropriate, I step in to give him a hug."
"He takes it willingly and he's warm and strong. For a moment I wonder why the hell I dumped this guy."
stop music
play sound "horn.wav"
queue sound "driveby.mp3"
show Leo Surprised with dis
"Just then, someone lays on the horn as they drive past us, pulling me out of my reverie."
"???" "\"FAAAAAAAGS!!!\""
"I lean back so I can watch the car speed down the empty road. Leo keeps holding me, though, and he just chuckles."
show Leo with dis
l "\"Hehe, Echo hasn't changed much, has it?\""
m "\"No, it hasn't.\""

stop background fadeout 3.0
play loop "AC.ogg" fadein 3.0
scene bg motelfull
with fade
"As we're saying our goodbyes, I remind Leo about the shots I need of the lake."
"He says he'll talk to the other two about it after they leave."
"We all say our goodbyes before Leo, Carl, and Flynn take off."
"TJ takes his usual hour getting ready for bed while Jenna does some schoolwork."
"By the time I'm finished brushing my teeth, I'm grateful to see them both in bed."
"I get under the covers next to TJ and lay there for about an hour, staring at the ceiling."
"Slowly, I slide out from under the covers, careful not to wake TJ."
"Quietly, I slip my jeans on and grab my jacket before heading out the door..."
stop loop fadeout 3.0
scene bg fb6
show nightoverlay
with slow_dissolve
play music "meeting1.mp3" fadein 3.0
"Toby builds a small sand castle next to the lake, in the process of digging a moat around it."
#!!!! If TJ is Toby here, shouldn't Jenna be Jasmynn?
#!!!! This could be a good place to reference her old name early on
#!!!! the story doesn't explain why her name changes between Route 65 and Echo until her path, and to me it always felt like the name change was a 4th-wall breaking retcon from Route 65 until way later when it's explained properly.
"Jenna drops a few twigs next to it before running off to find more decorations."
"Flynn is talking to Sydney, pointing at Toby's sandcastle. Sydney looks hesitant, but excited."
"He seems to make up his mind, suddenly running forward and kicking the top of the tallest castle."
"It breaks easily with most of it flying into Toby's face."
"Toby flinches back, shocked before immediately crying as he rubs at his eyes."
"Jenna comes running from across the beach, yelling before shoving at Sydney, who's laughing."
"She turns to Toby, trying to help him clean his face, but the lynx pushes her away before running towards the trail back to Echo..."
stop music fadeout 14.0
jump monday
