label saturday:

stop music fadeout 3.0
play music "transition.ogg" fadein 18.0
scene bg black
with dissolve
$ renpy.pause(1.0, hard=False)
scene bg card1 with opening_fade
$ renpy.pause(7.5, hard=False)
scene bg card2 with opening_fade
with slow_dissolve
$ renpy.pause(6.0, hard=False)
stop music fadeout 6.0

queue sound "phonebuzzlong.ogg"
play background "bussound2.ogg" fadein 2.5
scene bg bus with opening_fade
show phonemom at center with easeinbottom
window hide
$ renpy.pause(10.0, hard=False)
hide phonemom with easeoutbottom
$ renpy.pause(0.4, hard=False)
window show
m "\"No, God... I can't deal with this right now.\""
"I stare at the screen, letting my phone vibrate until it stops."
"I'll try to make up an excuse that it was on silent later."
"I had been a cringing, flustered mess since this morning. School and my geometry test had kept me only {i}slightly{/i} distracted."
"With the call as a reminder, I feel a welling sensation around my eyes and my vision blurs. I suck in my cheeks before exuding a shaky exhale."
play sound "FXRadioTune3.ogg"
"Nothing will ever be the same anymore - my parents won't see me as {i}normal{/i} anymore."
"All because I was daft enough to try to rub one out on the computer before the bus came this morning."
"I thought they were at work. Mom is usually out by five and Dad by six, but they took the day off on account it's their anniversary."
"So not only did they catch me pants down, prick-in-hand but also found out I was gay in one fell swoop of headphone-induced lack of spatial awareness."
"I heard Mom scream. I was so startled, I jumped, my headphones coming unplugged from my laptop, blasting fox/stallion porn on full blast..."
"..just when my dad came running in."
"I remember Mom turned, went to her room, locked the door, and I didn't see her again before I left."
"Dad meanwhile was sort of laughing nervously before I took off to my bus stop, but I could tell from his face that this was beyond awkward for him."
"I couldn't bring myself to words, I just pulled up my shorts and ran to my bus stop."
"All throughout the day, the thought of coming home and having to face the shame was like being dunked in ice water."
"Each mile we travel closer to Echo increases that feeling of... inevitable awfulness."
"I try to go over excuses in my head."
"I could maybe attempt to convince them that it was straight porn?"
"Both of the guys in the video had pretty visible beard-scruff, though."
"I rub my eyes. The thought of trying to figure out what all my folks saw on the screen makes me want to retch."
"Well, I could say it was a virus that took control of my browser window?"
"... and it was so startling a prospect that I didn't have time to fully put on my shorts..."
"... and the erection was unrelated..."
"Fuck."
"I peek though my paws at my phone screen, the symbol for a missed voicemail having appeared up top."
"I grit my teeth in extreme apprehension, turning the screen off and shoving my phone back into my pocket."
"Taking a moment to recombobulate, I look around."
play sound "FXRadioTune2.ogg"
"The bus is pretty empty besides me, the bus driver (who has been trying to get the radio to work the whole ride), and Carl in the seat adjacent to me."
"Carl, as usual, has his earbuds in with his expensive handheld out, playing some Japanese Tactics RPG."
"Usually we have at least Jeremy, Clint, Heather, Jasmynn, and TJ with us, but not today."
"Not many kids who go to the school in Payton live out in Echo. I'm pretty astonished the Bus District Expansion covered our town."
play music "FXRadioTune.ogg"
"The bus ride from Payton to Echo usually takes about 45 minutes, though it feels much longer."
stop music
play music "Country.ogg"
"..."
"... Especially now."
window hide
scene bg card3
$ renpy.pause(5.0, hard=True)
scene bg bus
window show
c "\"Yeugh.\""
"The ram looks up from his game to the source of the music, slightly furrow-browed."
"Our bus driver grins back at him through the rear mirror in a self-satisfied fashion, her gummy, chesire maw on full, yet brief, display."
"Realizing that she is looking back at him, Carl grunts, hunching up his shoulders a bit."
c "\"Karen, {i}why{/i}?\""
"She lets out a brief chortle."
k "\"Well, seeing as I only have you two along with me today, I thought I'd put on some tunes. Make your collar a little blue.\""
"Carl begrudgingly pauses his game, pulling out his earbuds and letting them hang over his horns. It was still weird seeing him likes this."
"Around age 14, his horns developed {i}a lot{/i}. He complained about headaches and neck strain constantly."
"He told me he had to see a chiropractor in a state over because his horns were so big, and his neck muscles hadn't developed enough to support them."
"Even now, a year later, he still sits with a sort of low, hunched posture."
c "\"I'm plenty blue-collared, yeah? I live in {i}Echo{/i}.\""
"She snerks again."
k "\"Boy, I have seen the size of your manor. No you ain't. Never woulda expected a sort like you to be so pomp and yachty-blooded.\""
"Carl doesn't say anything. His emerald gaze shifts some to the seat in front of him."
"Karen takes a glug from her soda bottle with her free hand, the other steering us through an on-ramp onto the freeway."
k "\"The spa day I would have on just one hour of your daddy's income. I'd feel bad for whoever works mani/pedi that shift.\""
"She holds up her calloused right hand, her claws rather stubbed, even for a fox's standard."
k "\"When I'm not driving you squirts, I do road crew for Public Works. Ain't your average mom, eh?\""
"She gesticulates with a swirling motion as she speaks, then lets her hand hang limply on the steering wheel."
k "\"Well, it might be the new {i}average{/i} here soon enough. Feminism and all that. You two'll learn all about it in college, I'm sure.\""
k "\"What're you two going for, major wise?\""
"Both of us make no quick move to respond."
k "\"Chase?\""
"I shift some in my seat, clearing my throat so that my voice doesn't crack."
m "\"Uh, well, I wanted to go into videography and film, but my parents weren't too fond of that. So... I guess journalism or communications?"
k "\"Ah.\""
"Karen responds so abruptly that it makes me wonder if I said something wrong."
k "\"Hm.\""
k "\"Well, my nephew got one of them communication degrees from North Mountain State.\""
m "\"Oh? How'd that go?\""
k "\"Ended up being a $60,000 piece of paper that earns him $13.25 an hour fixing old farts like us' computers out of some big box establishment.\""
k "\"'Nerd Squad' I think they're called? Agh, hell if I know.\""
m "\"I'm still deciding, I guess.\""
"She waves dismissively. I look over at Carl, who looks like all he wants to do is go back to playing his game."
k "\"What about you, Big-Horns?\""
"Carl blinks some at the casual speciesism, then scratches the back of his neck."
c "\"Um...\""
k "\"You just plannin' on going straight to work for daddy right after you graduate?\""
c "\"Mommy- er, mom, actually. I dunno yet.\""
"Carl looks pretty uneasy with this topic."
"He also seems pretty embarrassed at having said 'mommy' out loud. Were I in better spirits, I'd probably laugh."
k "\"Everyone is good at somethin' Carl, and hopefully that is somethin' you enjoy, too.\""
k "\"You're always quiet with your nose in that little... device of yours playin' games. Maybe that's your future career, somethin' techy?\""
"Admittedly, Leo is usually the one who is most handy with fixing our tech stuff. Carl isn't even the best at video games. That title belongs to Jas."
"Carl is quiet for a bit, tugging on the strings of his hoodie."
c "\"I dunno.\""
"Looking out the window, I see the sun is setting as we get within 10 or so miles of Echo."
"We pass the old abandoned waterpark, which I heard closed shortly after the bypass was built and all its passer-by traffic was lost."
"I think for a moment I see what looks like some figures in the drained pool, though when I try to squint, I don't see them anymore."
k "\"Ya know, I was around when that place shut down.\""
"I startle some, not realizing I was being watched."
k "\"Both times, actually. Once in the '60s, then again in the '80s when it reopened for a year."
k "\"Was during the era of big government giving out big ol' water project constructions to the state for pennies - L.A. being the golden child.\""
k "\"Our county, as you two squirts are aware, did not become the next Orange County.\""
k "\"{i}Spoilers{/i}, as my son Keith used to say.\""
"She lets out an amused grunt before sterning up some."
k "\"A lotta folks lost their jobs. Was like a little Great Depression in the middle of Mormon Land. Echo has been going to tits for generations, though.\""
k "\"And not the good sorta tits either. The real ugly ones. Like those that whatsername wields... Mrs. Tethers? Yeah, her.\""
"I'm taken off guard at that comment. Mrs. Tethers is a particularly nasty History teacher at PHS who is known for not being too keen on vulpines."
"She does have a kinda lopsided pair."
k "\"Anyway, it is ripe shame. By the time your kiddies are having kiddies themselves, this town'll be a feast for termites. Well, maybe not the manor.\""
"I see Karen's silver eyes focus on Carl."
k "\"'The castle', we used to call it...\""
"She says this bit rather strangely, as if trying to remember something specific. Carl is staring out the window, avoiding Karen's stare."
"In the two years we've had her as a bus driver, she has never spoken this much. Most of the time, she'd just be scolding Jeremy and Clint."
"I have this feeling she's been waiting for this opportunity to speak more personally with Carl for a while."
"As we get closer to Echo, we pass more abandoned places."
"Some are adorned with faded art-deco stylings from the bygone modern era, whilst others are but rotting wood, from the Mormon settlement days."
"In my current situation, all these familiar architectural fadings seem to evoke is a pulsating sense of dread for what is to come."
k "\"Carl, your family has been here for over a century. Way I see it, 'least they could do is reinvest in what they capitalized on in the first place.\""
c "\"Can you just... change the radio station?\""
"Carl's horns are pressed up against the window, his tone low but his voice loud."
k "\"Oh yeah? What you want it set to?\""
c "\"Anything but {i}this{/i}.\""
"Carl looks down at his handheld, fidgeting with stuff in the character screen but without the focus to keep actually playing."
k "\"Fine. What do you want to listen to, Chase?\""

menu:
    "Country":
        m "\"The current station is... fine. Don't worry about it.\""
        jump postrad
    "Soft Rock":
        m "\"I don't know, we might be able to get that soft rock station that is sometimes available right before we get into town?\""
        jump postrad
    "Techno":
        m "\"I don't know, if you have a good radio, we might be able to get that hardbass-y, techno station on 95.5 FM.\""
        jump postrad
    "Pop":
        m "\"I don't know, nothing gets me jacked like some generic pop music. 98.1 FM should have that.\""
        jump postrad
    "Random":
        m "\"What Carl said. Anything but this.\""
        jump postrad


label postrad:

k "\"What did you say? You want this, but louder?\""
c "\"No.\""
stop music
play music "Country2.ogg"
m "\"N-\""
m "\"No...\""
c "\"Chase, kill me.\""
c "\"End my life.\""
c "\"Maybe I'll respawn somewhere more peaceful.\""
m "\"This is good for you, Carl. You're getting blue-collared, albeit, you know... the hard way.\""
c "\"If I wanted to get blue-collared the hard way, I'd borrow Jasmynn's jean short-shorts and stand assumingly around the motel.\""
stop music fadeout 5.5
"Covering our ears and pressing our heads to the seats in front of us, we endure the 'Hick Musical Cavalcade', as Jasmynn deemed this station."
play music "Country3.ogg"
scene bg bus2 with slow_dissolve
"Glancing sidelong out the bus window, I see that we're less than a mile from home."
"My pawpads start to feel clammy and I clutch my knees tight."
"It's fortunate that Carl is currently occupied with burying his muzzle into the faux-leather of the seat in front of him as I begin to tremble."
"Part of me actually wants him to see. I know it's just stalling for the inevitable, but I want to talk to someone, anyone, about all this."
"This is a small town, and whoever I speak to will know that I like guys, and I'll have to deal with them knowing that fact every day 'till college."
"{i}If{/i} I go to college."
"I used to hate being so damn generic."
"Fucking Flynn whines about how boring I am all the time, but now..."
"All I can see are folks looking at me, seeing me as 'that otter who likes it up the rear' and not as {i}generic Chase{/i}."
"God, that's what my parents will see me as, too."
"This sort of... deviant who lives in their home."
"I imagine them looking at the photos of me around the house now and wishing they could have that back."
"I've never really talked to my parents about relationships and sex stuff, and now I'm just shocking them with this whole new side of me."
"What an anniversary present I've given them."
"I look over and see Carl hunched over, his horns pushing into the seat, and his gaze focused blankly upon the screen of his handheld."
"Upon closer inspection, the screen is completely black, the device no longer on."
"It seems that he's not in the best of states either."
"I swallow, debating disturbing him. Carl might be my best friend, but we don't really have 'deep talks'. Especially since the lake incident."
"Maybe I could text someone?"
"I slide my phone out of my pocket, staring at the black screen much like Carl is now."
"I realize when I get home, my parents are probably going to demand to see my phone and messages, so I'll have to remember to delete them."
"I try to imagine how each one of my friends would react, but this is honestly foreign ground, only alluded to in traded insults and jokes."
"Flynn especially. The lizard drops the word 'faggot' in every other sentence as of late, though I think he just chooses it for maximum edginess."
"Jasmynn, on the other hand, might be the most supportive with this sort of thing."
"However, she wasn't at school today."
"I eavesdropped Flynn mentioning something about issues with her parents and Jeremy to Leo, but I couldn't make out the specifics."
"I don't even know how Leo would react to any of this. He makes jokes about poofy stuff all the time, but I can tell there is some unease there."
"That leaves TJ. Carl described him once as the moral, gooey center of our sandwich of a group of friends."
"That being said, I'm not sure how much I can actually tell him. He's just barely crossing the puberty threshold right now."
"Plus, the Christianity factor..."
"I uncover one of my ears long enough to pull out my phone, my heart skipping a beat at the \"New Voicemail\" notification."
"I quickly swipe over to my contacts."

show phone with easeinbottom
menu:


    "Confide with Flynn":
        $ partner_choice = "Other"

        jump conflynn1

    "Confide with Carl":
        $ partner_choice = "Other"

        jump concarl1

    "Confide with Jasmynn":
        $ partner_choice = "Other"

        jump conjas1

    "Confide with Leo":

        jump conleo1

    "Confide with TJ":
        $ partner_choice = "Other"

        jump contj1

label conleo1:

$ partner_choice = "Leo"

"Leo always has a weird sort of paternal vibe going on with him."
"If someone in our group is feeling down, or about to make a stupid decision, he usually goes out of his way to set them straight."
"Jasmynn says that this is largely due to the culture he comes from — the whole 'pack mentality' thing."
"In truth though, Leo is one of the first friends I ever made, back when I was like 6."
"I'm sort of hoping time cuts through the stigma bullshit and he'll have an idea of what to do."
"My thumbpad hovers over his portrait picture in the messenger app."
"Alright, here goes nothing."
play sound "texting1.ogg"
hide phone
show cellL 1 at center
centered "_"
"I wonder if I shouldn't have done punctuation or capitilzation. Maybe try to sound a little more casual?"
play sound "phonebuzz.ogg"
show cellL 2 at center
centered "_"
"Shit."
"He doesn't have practice today, so I thought he'd be free."
"Managing text messaging with Leo is hard enough as it is. With him distracted, it'd be even worse."
"Looks like I can't do it through here."
play sound "texting2.ogg"
show cellL 3 at center
centered "_"
play sound "phonebuzz.ogg"
show cellL 4 at center
centered "_"
"God, he always does this."
"Two-to-three-word responses."
"He's still probably hanging out with the other football-folk outside school."
"Lucky bastard has his own truck now, so he mostly doesn't come home with us anymore."
"I find myself biting the inside of my cheek and quickly force myself to stop."
play sound "texting3.ogg"
show cellL 5 at center
centered "_"
"..."
hide cellL with dissolve
"I stare at my phone screen for a long while and eventually come to the conclusion that this is a waste of time."
"He doesn't seem to be in any hurry to respond now."
"I don't want to fuck this up by badgering him with my whinging revelation that I apparently love cock while he'd rather be doing {i}anything{/i} else."
"As the familiar landmarks of the railway and the redrock of Echo Canyon come into view out the window, my restless anxiety returns."
"Steadying myself, I swipe back over to my contacts."

show phone with dissolve
menu:


    "Confide with Flynn":

        jump conflynn1

    "Confide with Carl":

        jump concarl1

    "Confide with Jasmynn":

        jump conjas1


    "Confide with TJ":

        jump contj1

#______________________________________________________________


#__________________________________________________________________________________________________________

label conflynn1:
"I frown to myself as my thumbpad hovers over Flynn's contact image on the messenger app."
play sound "phonebuzz.ogg"
show image "cellf1r.png" at center
"This—"
"Well that's some timing."
"I honestly have no idea what this message means."
"Instinctively, I try to respond with something jabby."
hide image "cellf1r.png"
show image "cellf2.png" at center
play sound "texting1.ogg"
centered "_"
"After hitting send, I'm not too sure that was the right move."
"Flynn rarely responds whenever I text him, and that probably didn't boost my odds."
"Looking out the bus window, I can see that we're approaching Carl's stop."
hide image "cellf2.png"
show image "cellf3.png" at center
play sound "phonebuzz.ogg"
centered "_"
"Oh."
"I thought it was a cheese?"
"Whatever."
hide image "cellf3.png"
show image "cellf4.png" at center
play sound "texting2.ogg"
centered "_"
hide image "cellf4.png"
hide image "cellf3.png"
hide phone
with easeoutbottom
"As the bus turns onto the neighborhood road, I scoot over some, speaking up to get Carl's attention."
m "\"So, I'm gonna get off with you here, okay?\""
"Carl just continues staring at his blank screen for a second before blinking and looking back at me."
c "\"... Are you sure? That might be pretty messy, and Karen watching might give me performance anxiety.\""
"Carl stares deadpan at me."
"I rest my forehead into my paw and groan, though I end up snickering a bit."
"The bus comes to a stop."
k "\"Carl, this is where you get off.\""
c "\"Chase wants to get off, too.\""
m "\"The bus.\""
k "\"You have a note from your folks?\""
"Shit."
"I look back to Carl and he gives me a look of understanding."
"He unslings his backpack from his shoulder, rifling through it."
"Carl looks up at me briefly, mouthing one word: 'Stall'."

menu:
    "Tell a Joke":
        jump conflynn1joke
    "Ask About Keith":
        jump conflynn1keith


label conflynn1joke:
m "\"I do.\""
"I make a motion of holding something up behind the seat. Carl seems to have found a pen and notepad and is scribbling hastily."
m "\"So, uh, Karen... how do you get a North Mountain State grad off your property?\""
"Karen gives me a rather dubious look, her silver gaze eyeing me up."
m "\"You pay him for the pizza.\""
"The old fox lets out a huff that is half-exasperated, half-amused."
k "\"What in the hell... heh. Be aware, Chase, my nephew from NMS is 6-foot-9 and played rugby. He might not take too kindly to that.\""
m "\"Hey, Carl was the one who told it to me!\""
"Carl puts on a show of giving me a slightly narrowed look before slugging my shoulder."
"I don't have nearly the same level of cushion there as the ram, so even if it's for show, it still hurts."
"I feel something flutter onto my lap."
"As I pick it up, I see that Carl has forged a note with my mother's signature style near perfectly."
"As much as the ram whinges about his lack of skill, his penmanship and art are not half bad."
"I give him a discreet, grateful look as we get up and move to exit the bus."
"Carl hops off first, his hooves making an audible 'clop' noise upon the aged asphalt."
stop music fadeout 4.0
"However, as I move to hand my note to Karen, her calloused hand grasps my wrist instead of the note."
k "\"I'm not that deaf and dumb, kiddie. I've been doing this job a long while.\""
"She relinquishes my wrist, the note fluttering to the ground. I can feel Carl staring nervously at us from the road."
k "\"You got awful comedic timing, Chase, but it was a good joke. I'll tell my nephew that one myself.\""
"She shifts some in her large driver's seat, the cadence of her voice changing some as she looks to the back of the bus."
k "\"I saw you back there, puffy-eyed and tremblin'. You afraid of something at home? I know how the people can be out here.\""
"She pauses, bending down to pick up the dropped note and before tossing it in the bus's trash bucket."
"I freeze, feeling the tips of my ears burn rosy at today's endless cavalcade of embarrassment."
k "\"Especially with kids.\""
"I'm not sure what she means by that and definitely am not sure what to say. I look back at Carl."
"He's averting his gaze now, his paws deep in his hoodie pockets."
k "\"... Alright, alright, I get it. Nobody trusts the hick bus driver to know what it's like to be a kid these days.\""
k "\"Look, run along now. Sorry for, ya know, grabbin' ya. I'm used to them shits Jeremy and Clint doing that and gettin' {i}me{/i} in trouble.\""
"I try hard and force a smile."
m "\"Oh, uh... thanks. I appreciate your concern and all. Er, yeah, they are pretty... shitty.\""
k "\"Hey! Language, kiddo.\""
m "\"Sorry...\""
k "\"Also, tell Carl his fly is down. He looks like a damn fool.\""
"I see Carl stiffen, quickly reaching down and fumbling with his zipper, his neon orange SuperWolf boxers visible through his fly."
play sound "phonebuzz.ogg"
"Karen just sighs. I feel my phone vibrate within my pocket."
k "\"See you squirts on Monday.\""
play sound "busstopsdeparts.ogg" fadein 2.5
jump conflynn2



label conflynn1keith:
m "\"I do.\""
"I make a motion of holding something up behind the seat. Carl seems to have found a pen and notepad and is scribbling hastily."
m "\"So, uh, Karen... you mentioned your son Keith? The name sounds familiar.\""
"Karen gives me a rather dubious look, her silver gaze eyeing me up."
k "\"Well, I doubt you have recently. Keith's been gone for a good year or so now.\""
m "\"Where did he go?\""
"Karen scratches the end of her muzzle, still eyeing me with the same searching expression."
k "\"He's dead. Dead to me, at least.\""
m "\"Oh. Sorry.\""
"Definitely not going to prod there."
"Carl currently looks as if he is trying to camouflage into his seat, slowly sliding down it."
k "\"S'aight.\""
"The old fox lets out a huff that is half-exasperated, half-amused. She waves dismissively."
k "\"You squirts gonna exit the bus or not?\""
k "\"I got a big bowl of cinnamon chips and pineapple-mango salsa waiting for me back home.\""
"I shift awkwardly in my seat."
"Out of the corner of my eye, something yellow flutters down by my feet."
"With haste, I bend down and snatch up the note, acting as nonchalant as possible. Carl's penmanship is actually pretty good."
"I give him a discreet, grateful look as he gets up and moves to the exit."
m "\"I'm coming.\""
"Carl stops, looking back at me with that same deadpan as before."
m "\"... To the front of the bus.\""
"I think I hear Carl mutter, \"That's quite some range,\" as he turns and continues offward."
"Carl hops off first, his hooves making an audible 'clop' noise upon the aged asphalt."
stop music fadeout 4.0
"However, as I follow and move to hand my note to Karen, her calloused hand grasps my wrist instead of the note."
k "\"I'm not that deaf and dumb, kiddie. I've been doing this job a long while.\""
"She relinquishes my wrist, the note fluttering to the ground. I can feel Carl staring nervously at us from the road."
k "\"I appreciate your curiosity. Keith and I lived down in Coalville, so doubt you'd know him.\""
k "\"He made some seriously questionable decisions regardin' his amorous pursuits. Things I could not abide by.\""
"She shifts some in her large driver's seat, the cadence of her voice changing some as she looks to the back of the bus."
k "\"I saw you back there, puffy-eyed and tremblin'.\""
"Oh no."
k "\"You afraid of something at home? I know how the people can be out here.\""
"I'm frozen, feeling the tips of my ears burn rosy at today's endless cavalcade of embarrassment."
"She pauses, bending down to pick up the dropped note before tossing it in the bus's trash bucket."
k "\"Especially with kids.\""
"I'm not sure what she means by that and definitely am not sure what to say. I look back at Carl."
"He's averting his gaze now, his paws deep in his hoodie pockets."
k "\"... Alright, alright, I get it. Nobody trusts the hick bus driver to know what it's like to be a kid these days.\""
k "\"Look, run along now. Sorry for, ya know, grabbin' ya. I'm used to them shits Jeremy and Clint doing that and gettin' {i}me{/i} in trouble.\""
"I try hard and force a smile."
m "\"Oh, uh... thanks. I appreciate your concern and all. Er, yeah, they are pretty... shitty.\""
k "\"Hey! Language, kiddo.\""
m "\"Sorry...\""
k "\"Also, tell Carl his fly is down. He looks like a damn fool.\""
"I see Carl stiffen, quickly reaching down and fumbling with his zipper, his neon orange SuperWolf boxers visible through his fly."
play sound "phonebuzz.ogg"
"Karen just sighs. I feel my phone vibrate within my pocket."
k "\"See you squirts on Monday.\""
play sound "busstopsdeparts.ogg" fadein 2.5
jump conflynn2


label conflynn2:
scene bg neighborhood
show Carl Dejected at center
with dissolve
play background "reststop.ogg" fadein 4.0
"I step off the bus beside Carl and the doors shut behind me, Karen heading back toward the freeway."
"It gets dark so much earlier now that summer is over."
"Echo isn't exactly a major township — the area is deemed a 'Census Designated Place', so we don't get street lights."
"Carl watches the bus fade off into the distance before pulling out his phone."
c "\"Can't wait until I get my own car and license.\""
show Carl Depressed with dis
"He starts texting."
show Carl Neutral with dis
c "\"Letting my parents know that you're coming over. We should troll around on that 3D Virtue-Chat game again tonight.\""
show Carl with dis
c "\"I spent some money and got myself this big, luchador avatar — 'cept I gave him big ol' breasts. He's called Mammaria.\""
play music "doublewalk.ogg" fadein 4.0
"He looks up at me with a smirk before turning and walking."
hide Carl with dissolve
m "\"How much did you spend?\""
show cellf 5 at center with easeinbottom
"I follow, pulling out my own phone."
play sound "texting1.ogg"

show cellf 6 at center
c "\"I don't know, I was just grabbing what I needed. 15 bucks, maybe.\""
m "\"That's a lot for one of those kind of games — especially just for clothing.\""
show cellf 7 at center
play sound "texting3.ogg"
c "\"Well, like... the luchador mask I wanted was one of the 'Premium Items', so it costed the most. Everything else was dirt cheap.\""
c "\"Every single girl in that game uses the same hair — the long, curly blonde one that costs like a dollar.\""
show cellf 8 at center
play sound "phonebuzz.ogg"
c "\"At least... they {i}say{/i} they're girls.\""
show cellf 9 at center
play sound "texting2.ogg"
c "\"I'm just trying to be unique. Otherwise, what's the point? It is a social roleplaying game. Why risk getting ignored?\""
show cellf 10 at center
play sound "phonebuzz.ogg"
centered "_"
show cellf 11 at center
play sound "texting1.ogg"
c "\"I uh... actually have an another account with a character that is more normal-looking.\""
show cellf 12 at center
play sound "phonebuzz.ogg"
c "\"I made him after you left last time.\""
show cellf 13 at center
play sound "texting2.ogg"
c "\"He's like this... big, primate-looking dude with burn scars everywhere and this kinda albino-y face.\""
show cellf 14 at center
play sound "phonebuzz.ogg"
c "\"I had the idea for the character sorta based off a dream I had once.\""
show cellf 15 at center
play sound "texting3.ogg"
c "\"Anyway, I went to a lot of the in-game hotspots at first — a lot of the stuff you and I saw when we were messing around.\""
show cellf 16 at center
play sound "texting1.ogg"
c "\"It is sorta like you said: that most of the people there are just middle-aged housewives who can barely type a sentence.\""
c "\"But then I sorta went... 'off-grid', I guess you'd call it?\""
c "\"Like the spots that aren't advertised on the Destination Finder.\""
c "\"I started finding a lot of weird shit.\""
show cellf 17 at center
play sound "phonebuzz.ogg"
c "\"Like weirder than the shit we were making ironically, yeah?\""
show cellf 18 at center
play sound "texting2.ogg"
c "\"There were these places which looked like more real-life houses — not the usual fantasy, exotic stuff.\""
c "\"Just people living in virtual families in these boring-ass-looking homes — complete with framed photos of screenshots of their characters.\""
show cellf 19 at center
play sound "phonebuzz.ogg"
centered "_"
show cellf 20 at center
play sound "texting3.ogg"
c "\"I got the impression that a lot of them were, like, foreign.\""
show cellf 21 at center
play sound "phonebuzz.ogg"
c "\"I walked into this one flat with these two horse ladies in it.\""
c "\"They had decorations with Middle-Eastern words everywhere, but they seemed normal enough.\""
show cellf 22 at center
play sound "texting1.ogg"
c "\"They had a TV item which just displayed a slideshow of photoshopped photos of them with a baby.\""
c "\"When I started exploring the house, I ended up walking into this nursery room and they got {i}really{/i} pissy.\""
show cellf 23 at center
play sound "phonebuzz.ogg"
centered "_"
scene bg neighborhood3
show cellf 24 at center
with dissolve
play sound "texting2.ogg"
c "\"I thought about trolling, y'know, and writing 'I EAT THE BABBY' and hopping up and down on the crib, but I don't know...\""
c "\"It just felt... like this weird mix of awkward and sad.\""
show Carl behind cellf at center
show cellf 25 at center
play sound "phonebuzz.ogg"
stop music fadeout 2.0
centered "_"
c "\"...\""
play sound "texting3.ogg"
show Carl Neutral at farleft
with moveinleft
show cellf 26 at center
window show
c "\"Chase?\""
hide cellf with dissolve
c "\"Are you listening?\""
play music "KevinSardana.ogg" fadein 5.0
"Carl is standing in front of me with a concerned expression on his face."
"It takes me a moment to respond."
m "\"Yeah, just... texting Flynn.\""
show Carl with dis
c "\"He's actually responding to you?\""
m "\"Yeah, heh, I know.\""
"I look up the street, Carl's house sitting in its amber-glowing glory atop the hill slope."
m "\"Apparently there's a party happening tonight.\""
"Carl raises an inquisitive brow."
c "\"Like... {i}here{/} or in general?\""
m "\"I'm not sure what you mean by 'in general', but yeah, around here.\""
m "\"It's for Day of the Dead. Leo, and I think maybe Flynn, got invited.\""
show Carl Neutral with dis
c "\"What? They didn't mention it to me at all, and I asked them to their faces if they had any plans.\""
"I shrug."
m "\"Flynn made it sound like it was mainly just Payton people coming out here.\""
c "\"Yeah, but... it is weird they wouldn't mention that. \""
c "\"That sounds about like the most exciting thing that will happen around here for months.\""
show Carl Dejected with dis
"Carl looks off to the side, shifting his posture some."
c "\"I'd rather just... stay home and play Virtue with ya anyway.\""
show Carl Neutral with dis
c "\"... but seriously, what the fuck?\""
"The idea that two of our closest friends were keeping this a secret did make me feel pretty shitty."
"On top of all the other sensations of general shittiness I feel right now."
m "\"It's at the Parsons Manufacturing Building. You know, off Route 65?\""
c "\"That's sort of in the ass-end of nowhere for a party. Maybe it's like a rave or something?\""
"I shrug again."
m "\"... I think we should go.\""
show Carl Surprised with dis
c "\"...\""
"Carl blinks, his expression akin to as if I just asked to rub his horns."
show Carl Sheepish with dis
c "\"Dude...\""
"He lets out a little huff, rubbing the back of his head."
c "\"... First of all, we weren't invited. Second, it's the middle of nowhere. Third, isn't Day of the Dead for like..."
"He pulls his paw away from his beanie long enough to swirl it around in gesticulation as he tries to phrase this right."
c "\"... Latin-folk? My blood's as apple pie as it gets, dude.\""
m "\"Alright, first Leo is there, so I don't see him not getting us in.\""
"... though it was weird he didn't invite us in the first place."
m "\"Second, we {i}live{/i} in the middle of nowhere. Anything local happening is technically in the middle of nowhere.\""
"... which still doesn't make it any more safe."
m "\"Third, well, I don't know. I assume nothing too culturally sensitive is taking place in an abandoned factory?\""
"... which won't save us from sticking out like a sore thumb."
show Carl Neutral with dis
"Carl exhales through flared nostrils, lolling his head up as if being throttled by how much of a bad idea this is."
show Carl Depressed with dis
c "\"Dude...\""
show Carl Neutral with dis
"He looks back down at me, a taut frown upon his muzzle."
c "\"I don't know. I guess I'm kinda curious. Worst case: we stop in, smack Leo, and then make like Flynn's fetish and scat.\""
m "\"Best case: We stop in, smack Leo, and they have food.\""
show Carl with dis
c "\"I'd rip your tail off for a cheese quesadilla right now.\""
m "\"Don't do that.\""
play sound "phonebuzz.ogg"
$ renpy.pause(1.0, hard=False)
hide Carl
with moveoutleft
"My phone buzzes in my grip."
show cellf 27 at center with easeinbottom
centered "_"
hide cellf with easeoutbottom
"Ugh. So it begins."
c "\"That's good advice from Flynn. I don't know if you're gonna hold out the whole way though.\""
"Glancing over with a start, I realize that Carl is leering over my shoulder — squinting at my phone."
m "\"Christ!\""
"I exhale, turning my phone's screen off."
m "\"Yeah... I'll try my best.\""
"Carl lets out a brief, breathy bit of laughter before pulling out his phone."
m "\"{i}Lying to your parents{/i} time?\""
c "\"Yup. Your fault, too. What should I say?\""

menu:
    "\"That you're hanging out at my house.\"":

        jump walktoparty
    "\"That you're hanging out at Leo's house.\"":

        jump walktoparty
    "\"That you're working on an art project.\"":

        jump walktoparty
    "\"Tell the truth.\"":

        c "\"You know what? I'm nearly 16 and it is a Friday. My folks keep saying I need to be social, so...\""
        jump walktoparty

label walktoparty:
"Carl texts something into his phone before moving along in the opposite direction we were walking before."
play background "crickrestwalk.ogg" fadein 2.0
"I'm honestly surprised he accepted. His social anxiety is pretty bad at school."
"Maybe it's just that kind of night."
scene bg neighborhood with dissolve
"I follow suit and walk alongside Carl."
c "\"Can't wait 'til I get my license and car. I mentioned that already, yeah?\""
c "\"Route 65 is like three miles away.\""
m "\"You can get your fetlocks toned and ready for the dance floor, though.\""
"I see Carl's posture stiffen some at that prospect, his bright green eyes looking to the asphalt beneath us."
c "\"You don't actually think there is gonna be dancing, is there? Like the movies and shit?\""
"I shrug, something I'd been doing a lot this night."
"Growing up in a town with less than 60 people has made what seems like a conventional teenage experience on TV seem utterly foreign."
"The closest our group of friends had to such were birthday parties with just us six and our folks. Leo's dad let us drink a can of beer once."
m "\"I always imagined High School parties were just a bunch of kids sitting on couches and smoking weed.\""
m "\"But, this is Echo, so...\""
c "\"Meth?\""
m "\"Do you think Leo would go to a party where everyone smoked meth?\""
c "\"I didn't think Leo would go to a party and not {i}tell{/i} us.\""
stop music fadeout 5.0
"I pause, dipping my paws into my pockets."
m "\"I wonder if Leo thinks we're not cool.\""
"Carl actually turns to look at me, then quickly averts his gaze to the ground."
c "\"Dude...\""
c "\"I'd think that after all the shit we've been through, that wouldn't matter.\""
"The serious statement from him takes me off guard, and I feel instantly guilty for broaching that topic."
"I nod solemnly, another long pause drifting between us."
m "\"Yeah.\""
scene bg highwaynight2 with dissolve
"Carl tells me more about 3D Virtue-Chat and some girls he met on there as we walk."
"'Girls' being stated with quotation fingers each time."
"I had tried talking with guys online myself, though, like Carl, never with my real identity."
"I remember I was feeling lonely two months ago and posted a personal m/m ad on the PaytonList website."
"{b}'18 Year Old Otter Here Looking For Friend/Mentor'{/b} was the tagline."
"I included a cropped and photoshopped picture of myself at the Payton Rec Center pool, my face blurred."
"Since I went through puberty a couple years ago, I was pretty sure I could pass for 18 if my face was hidden."
"I was wrong."
"My post was taken down and I got a few emails from administrators asking all sorts of questions."
"... It really hasn't been my best past few months."
scene bg parsons with dissolve
play music "CrimeMuffle.ogg" fadein 4.0
play background "crickrest.ogg"
"Eventually, we reach the Parsons building, an establishment that closed many of my lifetimes ago from the looks of it."
"About 10 or so cars and motorcycles are parked alongside the building, and neon blue light emanates from the inside."
"The thump of bass is palpable even out here on the road."
show Carl Neutral at right with dissolve
"I look over to Carl. All his lackadaisy demeanor on the way here has been replaced by tight-lipped tension."
"To be honest, I'm feeling pretty similar."
c "\"I don't see anyone outside here. Everyone must be inside.\""
c "\"We just got to get in and look for Leo's big, red ass.\""
c "\"Or, y'know, his face. Any idea what we should say when we see him?\""
m "\"'Hi Leo', is a good start.\""
c "\"Okay, sounds good.\""
m "\"Cool.\""
"Neither of us moves."
show Carl Dejected at right with dis
m "\"...\""
show Carl Neutral at right with dis
c "\"God, dude, what if it's a rave?\""
m "\"Do people actually still have raves?\""
c "\"I dunno, but I'm getting really bad 'vampire cult' vibes from all this.\""
show Ghost TJ behind Carl at farright with moveinright
c "\"Let's check around the back first, alright?\""
show Ghost TJ_Excited with dis
d "\"Boo!\""
show Carl Surprised at farleft with moveinleft
c "\"Oh, what the {i}FUCK{/i}?!\""
"Carl practically leaps, swatting at the air around him as he gets some distance."
show Ghost TJ with dis
d "\"Language! Oh, jeez, sorry Carl. I didn't know I'd scare you that badly!\""
"Carl stares wide-eyed at the sheeted visage before his eyes go to a lull."
show Carl Dejected with dis
c "\"Ugh... hey, TJ.\""
m "\"I legitimately thought you were about to start bleating there, Carl.\""
show Carl Annoyed with dis
c "\"Real speciest, dude.\""
show Carl Dejected with dis
m "\"What are you doing here Teej? And why are you dressed like a ghost?\""
t "\"My mom dropped me off about two minutes ago. I can't believe you guys walked here!\""
t "\"Mom would have given you a ride if you asked.\""
show Ghost TJ_Excited with dis
t "\"... not that I'm against you guys getting exercise or anything! Heh...\""
show Ghost TJ with dis
t "\"...\""
"I think Carl winces slightly."
t "\"As for the costume, my mom and I put this together at the last minute.\""
t "\"I didn't get to go trick-or-treating yesterday because of church stuff, so Mom said now would be my chance with this party.\""
"Even under all that fabric, I can still picture TJ grinning cheerily. It is such a contrast to the past few hours with Carl."
"... A contrast to this whole day, actually."
m "\"That's very considerate of your mother, TJ, but um... eh, nevermind.\""
show Carl Annoyed with dis
c "\"How did {i}you{/i} get invited to this but not us?\""
show Carl Dejected with dis
"TJ tilts his ghostly head curiously."
t "\"My mom just told me she heard about this fun get-together here and said it would be a good way to treat myself after volunteering yesterday.\""
t "\"I didn't really think I needed one...\""
"There is a pause."
show Ghost TJ_Excited with dis
t "\"Oh gosh, I've never crashed a party before!\""
show Ghost TJ with dis
t "\"Should we just go home?\""
"Carl and I exchange a look."
m "\"Flynn told me that Leo would be here tonight, actually.\""
t "\"Huh? He didn't mention anything of that nature to me.\""
t "\"I'm sure he just forgot to though.\""
hide Carl with moveoutleft
"Carl steps off the roadway and onto the smooth concrete of the entranceway, trying to get a stealthy look inside from afar."
c "\"If you say so, man.\""
t "\"I mean, its okay to have a plus-one, right? But there are three of us.\""
m "\"See Leo in there, Carl?\""
"Carl is silent for a long moment."
c "\"I see Jack.\""
m "\"Who?\""
"Carl looks back to me."
c "\"Jack Shit. You might know him.\""
"I furrow my brow at Carl. TJ physically covers his ears with his enshrouded paws."
"I hear the lynx mutter a faint, \"Stop...\""
show Carl Neutral at farleft with moveinleft
c "\"Is it weird that we've been out here this whole time and no one has come outside?\""
c "\"Like, I'd assume people would want to come out for air, to smoke, and make out.\""
m "\"They might be doing that inside.\""
show Ghost TJ_Excited with dis
t "\"What?!\""
show Carl Dejected with dis
"TJ's eyes bulge."
t "\"What kind of party is this?\""
"TJ brings his paws together, wringing them as he looks at us expectantly."
m "\"We don't know, TJ. I... kinda hoped that you would.\""
show Carl Annoyed with dis
c "\"The sort that Leo and TJ go to without inviting or even {i}telling{/i} us about, 'pparently.\""
show Carl Dejected with dis
"Bitterness still hangs in Carl's tone as he rocks nervously upon his hooves."
"I'm honestly still upset about it myself, too."
"This is the sort of thing I'd like us all to do together — our first real party, as a group."
"I don't feel nearly as confident without him with us."
"By the way TJ and Carl are acting, I think it's the same for them, too."
"I suppose Leo just has that effect on people."
queue sound "phonebuzzlong.ogg"
"..."
show phonemom at center with easeinbottom
centered "_"
"Oh god..."
"How in the hell am I even getting bars out here?"
"Fuck this."
play sound "text.ogg"
hide phonemom with easeoutbottom
stop sound
hide Carl with easeoutleft
hide Ghost with easeoutright
"I hit ignore and walk past Carl toward the blinding cyan light of the broken entryway."
c "\"Dude, wait!\""
t "\"Chase!\""
scene bg parsonsinterior1 with dissolve
play music "crime.ogg"
"I step inside and am instantly greeted with the musty smell of dozens of years of structural decay."
"The scent of dust, drywall, and stray fiberglass insulation mixes with the more modern aromas of alcohol, perfume, and scented candles."
"Looking around, there are actually quite a few lit candles lying around, their flames contrasting with the colored gel-matted halogen lighting."
"Whoever set this up must be a theater-tech kid."
"With all the candles, I actually agree with Carl's notion that this is a bit vampire-culty feeling."
"The music certainly isn't helping."
"I had expected something a lot more... I don't know."
"Leo calls it 'Oompa-Oompa' music — the stuff with trumpets and accordions we get on the Spanish stations."
"..."
"Still no sign of anyone."
"This is actually getting kind of spooky."
show Ghost TJ at farright with moveinright
show Carl Neutral at left with moveinleft
t "\"Hey, wait up, Chase!\""
"TJ and Carl come bounding in behind me."
c "\"The acoustics in here are nuts.\""
t "\"Why is it empty?\""
m "\"I don't know — I don't hear anyone yet.\""
t "\"That's weird.\""
c "\"Well...\""
c "\"Let's split up, gang, and search for clues.\""
"TJ and I both look over at Carl, who has a flat expression on his face."
c "\"I'm joking. I'm literally fine with us holding tails chain-style at this point.\""
t "\"I'm okay with just walking normally...\""
scene bg parsonsinterior2 with dissolve
"With that, TJ steps up. Following in tow, we walk around the corner, through a cobwebbed hallway, and into the main manufacturing floor."
"Here, we finally see some people."
"This is certainly no rave. I count only about 15 or so people at the far end of the room and a few more in the rooms behind them."
"Most seem to be surrounding a metal keg, though a group of about six girls looks to be gathered around what looks like a yearbook."
"I only recognize one or two of them — and even then, only vaguely."
t "\"I think I see Heather over there by the barrel-thing!\""
"TJ points a sheeted paw toward a feline girl by the keg. Heather has a blue solo cup in hand and is laughing at one of the guys around her."
"Heather is one of the girls who rides our bus. She lives out on the outskirts of Echo."
"She's not really a part of our group. I just know her dad is responsible for maintaining the reservoir dam."
"I have a feeling what's in the keg isn't fruit punch and feel pretty boggled at how TJ's mom was the one to send him here."
"Meanwhile looking at Carl, I see that pretty much all his snark has dissipated once again. He stands in the doorway of the hall."
"The people in front start to notice us, nudging their friends and pointing. Some snicker, though most just look confused."
"... especially at TJ in his ghost costume."
"Feeling eyes upon him, the lynx lifts up his sheeted arms."
t "\"Ooooooowoooooo!\""
"He approaches the grouping in character."
t "\"Happy Day of the Deeeeeeeeead!\""
"I don't think he knows what that even is."
"The confused expressions seem to amplify."
"As TJ nears, it looks like he's attempting to hug Heather."
"Having not been paying much attention behind her, she turns right at the last second, the lynx wrapping his ghostly arms around her in a tight hug."
"She screams and all eyes shift to her and TJ."
"\"Get the fuck off of me, o-oh my god!\""
play sound "thud5.ogg"
"The surprised Lynx lurches back with a startle, right as Heather shoves his chest."
"He goes colliding into the floor with a hard 'thump', dust splaying everywhere."
"The others around Heather exclaim distress."
"\"What the fuck, man?\"\, \"\Who are you?!\"\, \"\Get off her, you fucking creep! Emilia, go... go get Darick!\""
m "\"Heather, it's just TJ!\""
"Despite my shouting, I don't think anyone hears me... or at least, understands me."
"They mostly all sound inebriated, judging from the slurs in their voices."
"I see one of the girls at the yearbook table get up and fast-walk into the backrooms."
scene bg cg with dissolve
"I try to run up to TJ's side, but a large coyote steps in from a back room and blocks my path."
"He has a look in his eyes that seems to say he's looking for a fight."
"TJ, meanwhile, lies on the floor with his white sheets coated in factory dust."
"From the sniffling noises I hear beneath the costume, I can tell he is crying."
"A stumbling coyote girl nudges him with her foot before emptying the contents of her cup on his sheeted head."
"Another, equally drunk wolf attempts to pull her back, nearly tipping them both over. She puts on a dazed expression of motherly scolding"
"\"Yo Maria, what the fuck... don't pour booze on the Rape-Ghost. We honor our... our dead bad-touchers on this night.\""
"For some reason, this comment makes a fox fellow next to Heather bristle."
"\"Heather, thish the guy you was talkin' to me 'bout? The fucker who... who...\""
"His fists clench."
"Heather, meanwhile, seems to be crying now too for some reason, her mascara matting the fur around her eyes."
"She just keeps repeating, \"I can't fucking believe this,\" over and over again while her friends try to console her."
m "\"What the hell are you talking about?! Leave him alone!\""
"The older coyote in front of me is not having any of it. He snarls."
"\"We're shick of yous shick fuckers.\""
m "\"I don't know {i}any{/i} of you besides her!\""
"Someone next to Heather yells back, \"You leave Heather the {i}fuck{/i} alone, muskshit!\""
"I look behind me and see that Carl is no longer in the doorway or in here with us."
"The fox guy seems to be trying to drag TJ now, limply smacking his sheeted head as the lynx tries to pull back."
t "\"I'm sorry, I'm sorry...\""
m "\"This is a misunderstanding or something! Fuck, Leo! Leo, are you here?!\""
"The coyote grabs my shirt, pulling at me with enough force that my muzzle ends up smacking into his trucker hat-brim and knocking it off his head."
"I manage to swat his paw away, though not before one of the girls screams in my direction."
"\"Oh my god, he's attacking Darick!\""
m "\"What the hell?! No I'm not!\""
"With 'Darick' snarling at me as he recombobulates, I weigh my options."
"I legitimately don't know how to fight. Flynn said that I wouldn't be good at it if I tried because of my 'shitty otter arms'."
"I look down at my arms."
"They are rather shitty."
scene bg parsonsinterior2 with dissolve
"... I just have to go get help."
jump fightfind

label fightfind:
"The cacophony of screaming and snarling from around TJ is insane. These people are on fucking drugs or something."
"I hold up the flat of my paws to the de-hatted coyote."
m "\"I'm not trying to fight you! I just want to get T—\""
play sound "thud.ogg"
scene bg parsonsinterior2 with vpunch
"The coyote swing-thrusts his arm out, getting a glancing blow with his fist against my chest."
"Stumbling back, I scramble to my feet, taking one final look at the fetal-positioned TJ before turning to run."
play sound "fight.ogg"
$ renpy.pause(1.0, hard=False)
play sound "thud.ogg"
scene bg parsonsinterior2 with hpunch
play sound "ringing.ogg"
"The coyote latches onto my shoulder, yanking me back. Something hard smacks into my skull and I feel my mind rattle."
stop music fadeout 6.0
stop background fadeout 18.5
"I lurch back, essentially butt-bumping the coyote as my ears ring from the prior blow."
"I feel like I'm walking like a zombie now, staggering toward the door as my vision blurs."
stop sound fadeout 5.0
scene bg ballroomn with opening_fade
play music "crimeslow.ogg" fadein 4.0
"Is this what being knocked out feels like?"
"I clench my fists and keep up my pace, trying to blink the blurriness away."
scene bg parsonsinterior1n with dissolve
"Eventually, I reach the entrance."
m "\"Caaaaaaaarl...? Leooooooo?\""
play sound "FX Door 3.mp3"
scene bg parsonsinterior1n with vpunch
"As I reach the outside, my knees lock and I drop to the concrete."
"The impact rattles my bones as I catch myself with my wrists, just barely managing to avoid falling directly on my muzzle."
"I take a deep breath... I'm still conscious."
"At least, half-conscious."
"I continue crawling, trying to ignore the throbbing pain."
m "\"Caaaaaaaaaaaaaaaaaaaarl!\""
"Shouting now, my voice sounds foreign to me — shrill, childlike, pathetic, and increasingly hoarse."
m "\"L-Leooooooooooooooooooooo!\""
"My voice shouldn't be this croaky. I've barely talked today."
scene bg parsons2n with fade
"..."
"I'm in the middle of the road now."
"Where's Carl?"
"..."
"I should get out of here before a car comes."
"I pull myself along the asphalt, feeling my skin scrape beneath my fur. I want to stand... but I'll probably just fall again."
scene bg nightsky1n with dissolve
"And so I keep crawling, rolling into what seems like some sort of detention basin."
"I stare up at the sky, fighting the sudden fatigue and gritting my teeth through the pain."
"At first I think it's blood that got into my eyes, but upon rubbing them, I realize that isn't the case."
"The sky is... different, like someone slapped one of those colored gel matte filters over it."
m "\"What the... hell?\""
"I rub my eyes again, attempting to focus. I can't stay here. TJ... TJ is in deep shit. Those idiots, those... those assholes."
"Sucking in a sharp breath through my teeth, I rise to a stand, praying my knees don't lock up again."
"Find Carl, find Leo..."
scene bg dirtroadn with dissolve
play background "dirtroadwalk.ogg"
"I stumble out of the detention basin, feeling packed soil beneath my feet."
"A dirt road..."
"Looking behind me, I realize I must have crawled farther than I thought. Parsons looks... over a mile away?"
"That can't be right."
"..."
"I see a van ahead."
"It looks rusted and old, but there's a light on inside."
"I step stiff-leggedy down the road a ways, reaching the bend where the vehicle sits."
scene bg bgn with dissolve
stop background fadeout 2.0
play background "nhysteria.ogg" fadein 20.0
"The same redness that the sky is tinted with pulsates from the interior."
"I try to speak, but no words come from my throat."
"It's like a dream... I want to do the rational thing and announce myself, but I can't."
"I move closer, peering into the dusty back window."
"Inside the window is another window, and in that window a little red dot in the corner, flashing on and off."
"In the window within a window, there is a writhing — flashes of fur contorted and undulating in constant, restless motion."
"Something is trying to hold it in place. I hear a clap and a cry."
"The clapping continues, louder now — rhythmic yet singular applause."
"\"This is what you want,\" says the voice that cried."
"I stare, slowly finding the will to speak."
m "\"No, I need to help my friends.\""
m "\"...\""
m "\"Do you know where they are?\""
"The voice shifts some, more urgent."
"\"We heard gunfire coming from the town. It's real bad.\""
m "\"Gunfire? I didn't hear anything. Please help me find my friends...\""
"\"We can't find them all now. We need to go. They're lost.\""
m "\"No, they're not... I'll keep looking. I'll keep looking myself!\""
"\"You're just going in circles.\""
"I feel tears well within my eyes, a lump in my throat containing a choked sob."
m "\"Please...\""
play sound "caropen.mp3"
play sound "thud2.ogg"
scene bg bgn with vpunch
"The van's back doors open."
"I'm standing too close and they push me onto my back."
"The red light is gone now, replaced by darkness, shifting shadows within."
"I see them now — tarantulas, their eight legs fuzzed with white and rust-colored stripes."
"They're on me with haste — two of them, one on each of my arms."
"They bite so hard, so quickly. I can't yell."
"They pull and tug at me, another pair at my legs."
scene bg vcb with opening_fade
stop music fadeout 3.0
stop background fadeout 3.0
play sound "nhysteriarise.ogg"
queue sound "nhysterialoud.ogg"
"I'm pulled up and into the van, my body stretched upon a squishy something that begins to sink against my arms and legs."
play music "badradio.ogg" fadein 8.5
"There's no more light, and I stare paralyzed at what I think is the ceiling of the van in the pitch blackness."
"It feels like restraints are binding me in place."
"I try to adjust my eyes to the darkness, but everything is blurry and unclear."
"My head throbs like a heartbeat, the pangs of pain unrelenting."
"My fur bristles — where did the spiders go?"
"Breathing becomes more difficult, as if the oxygen in the van is running out."
"I feel the veins in my neck bulge as I try to gasp for large breaths, but my body is not my own."
"Lights pop as the ringing in my ears intensifies."
"Something is above me, I can sense it."
"There is a garbled muttering coming forth from it, as if spoken through a poorly tuned AM radio."
"It sounds... like {i}me{/i}."
"\"{cps=15}{font=ui/belligerent.ttf}Have you ever killed anyone?\""
window hide
play background "appear.ogg"
scene bg vc with slow_dissolve
$ renpy.pause(3.7, hard=True)
stop background
stop sound
stop music
scene bg bedroom
play background "reststop.ogg"
window show
"My eyes wrench open."
"I'm being dragged."
play sound "thud3.ogg"
scene bg bedroom with hpunch
"Realizing I have control of my basic motor functions now, I stomp my foot down, staggering free of the grasp and pushing myself against a doorway."
"I raise my fists defensively, my eyes adjusting to the light."
show Leo Surprised at center with dissolve
l "\"Chase!\""
"The red wolf stares gobsmacked at me."
show Leo Neutral with dis
l "\"{i}Puta madre{/i}, Otter.\""
"I lower my paws, trying to getting a sense of where I am."
"That same musty smell means that I'm probably back in Parsons, in front of what looks like an old first-aid center of some kind."
"To think that workplace accidents at these sorta places were so common, they needed one of these."
"Meanwhile, Leo is gawking at me, his eyes intense, searching."
"I look down and notice that his knuckle-fur is matted with dried blood."
"I swallow, clearing my throat. The hoarseness is gone, but the pain everywhere else sure isn't."
m "\"... Hey Leo.\""
"Out of all the questions I have, one pushes its way to the forefront."
m "\"Is TJ okay?\""
"The wolf continues to stare at me as if I were some sort of alien."
l "\"... Yeah. Now he is.\""
show Leo Annoyed with dis
"I see his nostrils flare, disbelief and anger in his eyes."
l "\"His mom's on the way here to pick him up. Heather is down there fuckin' doing a mix of apologizing and puking.\""
l "\"I just left him for a minute to check back on you.\""
"He folds his arms across his chest, leaning against the windowed wall beside me."
show Leo Neutral with dis
"There is a brief silence, and I feel his gaze swivel down back to me, as intense as before."
l "\"How did this happen, why was he... why were you two {i}here{/i}?\""
"Leo's accent is thick now as he tries to speak faster than he can process the words in his head."
"Part of the question has me concerned, though."
m "\"Just 'you two'? Where's Carl?\""
m "\"He was with me before... well, before that dick with the trucker hat hit me.\""
show Leo Annoyed with dis
"I see Leo's jowls rear back in a silent snarl. He looks down the hallway."
"He starts to shout at someone named 'Emilia', though I quickly realize he's speaking Spanish."
"A feminine voice down the hall retorts, also in Spanish."
"Leo looks back ahead and grunts, closing his eyes for a moment."
show Leo Neutral with dis
"Then, rather suddenly, they reopen, the big wolf turning to me."
l "\"Wait, you said Carl was here?\""
"I nod, then regret it because my head feels like a mashed apple."
l "\"I haven't seen him since lunch.\""
m "\"He was. You told him you weren't doing anything today, but Flynn told us otherwise.\""
"Leo doesn't actually look surprised at the reveal, though visible guilt hangs heavy upon his usually confident face."
"He doesn't immediately respond, instead staring at my battered self in silence."
play sound "phonebuzz.ogg"
$ renpy.pause(1.0, hard=False)
"My phone vibrates, though when I check my pockets, it isn't there."
"There is a palpable, sheepish moment when my ears flick towards the source: Leo."
"The wolf blinks, then awkwardly hands me my phone from his own pocket."
m "\"Um...\""
show Leo Sheepish with dis
l "\"We had to call TJ's mom. You're the one with the phone that can get signal pretty much anywhere, so I tried yours.\""
show cellc 1 at center with easeinbottom
show Leo Neutral
centered "_"
play sound "texting1.ogg"
show cellc 2 at center
centered "_"
hide cellc with easeoutbottom
"I hear the sound of someone fiddling with a stereo and an auxiliary cord on the factory floor. Some arguing about music choices ensues."
"It seems that some people are still around for the party, after all."
l "\"So, eh... what all do you remember, out of curiosity?\""
m "\"I don't have amnesia, so relax... whatever your name is.\""
l "\"'ey. I felt the back of your head, {i}puchica{/i}.\""
l "\"You've got a welt the size of a goose egg.\""
"I reach up and run my fingers over my scalp, the bump rather prominent."
m "\"Alright, well...\""
"I regale him with the events of the night up to TJ's bullying."
l "\"Those towny shits were saying you were pushers trying to harass Heather for some debts.\""
m "\"Fucking what?\""
l "\"Yeah, I don't know, Otter. Fuck.\""
m "\"I kept calling for you.\""
show Leo Depressed with dis
"He looks surprised, then scowls at the concrete floor between his feet."
play music "Blake song 1a.ogg" fadein 4.0
l "\"I should have been there to protect all of you.\""
"It seems like someone won the battle for the aux cord in the other room, as the music starts up again."
"... Yep. Still vampire-culty."
m "\"Heh, well, I got hit so hard, the sky turned red for a bit.\""
show Leo Neutral with dis
"Leo's eyebrow raises some. I see his eyes move toward my head bump again."
m "\"I remember stumbling around outside, looking for you and Carl.\""
m "\"I felt like I was walking for ages. The last thing I remember was a van..."
"I see Leo shift, his shoulders raising up as high they can go, that thing he does when he's tense."
"He looks at me, expectant."
l "\"... See anything else?\""
"My brow furrows as I try to recall exactly what transpired. I remember it felt so much different than it does now in hindsight."
m "\"I think I must have passed out then.\""
m "\"Everything else is too hazy to recall.\""
"'Recall without sounding insane', is more like it."
"Leo's shoulders lower. He seems to be in thought now."
l "\"I found you outside on the road.\""
l "\"I thought you had been hit by a car or something, and when I got to TJ, he wouldn't stop crying and smelled like booze.\""
l "\"Not that I'm trying to sound like your moms, eh, but you had me crazy worrying.\""
"He rubs at his raw knuckles."
l "\"Got into it with that fox guy, after that.\""
l "\"It has been a... weird night.\""
m "\"Why are you even here, man?\""
"He's taken visibly off-guard by that question."
m "\"The people here are friggen' nuts.\""
"He sighs, then slowly lowers himself to a sitting position against the wall on the floor."
"He motions for me to do the same next to him, and I do, dusting away any leftover broken glass first, though."
l "\"A few people from the football team were going.\""
l "\"Also, this... one person invited me and I wasn't going to tell them no.\""
"I'm about to ask who that was, but I'm interrupted fairly quickly."
l "\"I saw your text messages with Flynn.\""
"I feel a cold tingle creep from my spine to my fingertips at those words."
"I should be feeling angry at this complete invasion of my privacy, but I don't."
"I just feel paralyzed."
"I've known Leo since he didn't speak a lick of English, playing videogames with me and Jasmynn after school."
"He'd just imitate what we said with a big, dumb smirk on his muzzle, as if he was saying something profound."
"I remember he got really hooked on the phrase 'double-jump that sucker!'"
"I had been yelling it at Jas for like three hours when we were trying to beat this platformer game I forgot the name of."
"From then on, every time one of us was feeling down or facing some challenge, he'd tell us to 'double-jump that sucker!' with that same smirk..."
"I look up over to Leo now, trying to gauge his feelings, but his expression is indiscernible."
show Leo Rejected with dis
l "\"... Fucking {i}Flynn{/i}? Why him?\""
show Leo Neutral with dis
l "\"You know you can talk to me! I wouldn't have even gone to this thing.\""
"He gestures to our surroundings. Two girls I haven't seen before walk by us in the hall without even a passing glance."
"I look down, staring at my paws. I went from having the chills to feeling like my face is on fire."
if partner_choice == "Leo":
    m "\"I tried messaging you first, remember?\""
    m "\"You... said you were busy and never responded back.\""
    "Leo's brow furrows and he roughly presses his fist against his forehead."
    l "\"Agh, fuck me — really? That's what you were on about earlier?\""
    "I thin my lips, looking up at him tentatively."
    m "\"Yeah, really.\""
    l "\"Shit.\""
    m "\"What were you busy with?\""
    "The wolf gives me a sidelong look, a tentative expression tugging at his jowls."
    l "\"Don't change the topic, Otter.\""
    m "\"I'm not changing the topic...\""
    "Hearing my own voice, I sound a hell of a lot more pathetic than adequately defensive."
elif partner_choice == "Other":
    "I shift some upon the concrete floor."
m "\"I... uh...\""
"I try waiting for the girls nearby to be completely out of earshot, but they stop in the hall and start showing each other something on their phones."
"Leo follows my gaze, letting out a quiet huff."
l "\"Come with me.\""
"He rises up to his feet, pulling me up by my wrist."
"Not having much choice as I'm tugged like a rag doll, I comply."
scene bg parsonsinterior3 with dissolve
"Winding our way through the remnants of the partygoers, I fail to recognize anyone."
"One or two say hi to Leo as we pass, though most outright ignore me."
"I'm increasingly self-aware of how plain I look in contrast to the ripped-plaid-donning, pierced-face, and spiked-hair crowd."
"The t-shirt and cargo shorts look must not be really in at the moment."
show Leo DarkNeutral at center with dissolve
"We stop finally in front of one of the back exits. There doesn't seem to be food, booze, or drugs in this part of the factory, so we're alone."
"Once again, Leo turns his expectant gaze upon me, his brow knit."
"However by now, my nerves have evened out slightly and I decide to counter the earlier question."
m "\"Why do you care so much that I told Flynn and not you?\""
m "\"You didn't tell me about all {i}this{/i}.\""
show Leo DarkAnnoyed with dis
l "\"So you're queer now, eh? I get that. Just, fuck, you can do so much better than Flynn!\""
m "\"What the hell, I'm not trying to court him. I just needed somebody to talk to, okay?!\""
m "\"He's not gay.\""
l "\"He is.\""
m "\"{i}What{/i}?\""
show Leo DarkNeutral at center with dis
l "\"He screws boys. Lots of them.\""
l "\"I thought you knew...\""
"I don't speak to Flynn as much as we did when we were younger."
"Especially since what happened at the lake."
"He usually goes off and does his own thing as of late, extra moody-like."
"Leo would tease that he's going through an 'emo phase'."
"Meanwhile, Carl says he's just 'Asperger's and french fries'."
"... I guess I haven't really talked with him personally enough to see past that."
l "\"Have you?\""
m "\"Have I what?\""
l "\"Screwed boys?\""
"My eyes bulge in such a sharp reaction that even Leo holds up the flats of his paws defensively."
l "\"Shit, alright — you really are new to this, huh?\""
m "\"You could say that, yeah. My parents didn't know until this morning.\""
m "\"... Or, I guess last morning, now.\""
l "\"I saw. That's real rough, yeah?\""
"I cross my arms over my chest, letting my chin loll down as I stare at the dusty concrete floor."
m "\"I'm gonna try to see if TJ is still out front and get a ride home with him.\""
m "\"I'll leave you be with your friends.\""
hide Leo with dissolve
"I turn, beginning to move when I hear a growl from behind me."
l "\"Agh, {i}puchica{/i}!\""
show Leo DarkAnnoyed with dissolve
"He grabs my shoulder, spinning me around to face him again."
l "\"Why do you have to be like this, eh?!\""
m "\"I didn't {i}choose{/i} to be like this, L-\""
show Leo DarkNeutral at center with dis
l "\"Ay-yai, your adorable daftness.\""
l "\"Do you know how happy I was when I read those texts? It was like a fucking fantasy, you know?\""
show Leo DarkAnnoyed with dissolve
l "\"Then I started wondering why you didn't tell me, and then I got all mad and now I've ruined this.\""
show Leo DarkNeutral at center with dis
l "\"You didn't even know he was... ya know, like us.\""
"It takes me a second to process being called adorable, a fantasy, and the reveal from Leo himself."
"I blink up at him."
"He blinks back at me."
"The wolf bites his tongue for a moment, trying to think before speaking."
show Leo DarkDepressed at center with dis
l "\"I wish I could go back in time and redo this.\""
l "\"I'll kick the huevos in of that scud who hurt you, I'll protect you from here on out, and I won't hide things from you.\""
l "\"You are the fuckin' gold nugget in this shit-mine, yeah?\""
l "\"I wouldn't be any different than these sloshed-up bastards if it hadn't been for you guys.\""
l "\"I think back to when we were little, yeah? I don't remember any of what you were all saying, but I remember being happy because of you and Jas.\""
l "\"And, you know, as you grew and shit... I started seeing you different-like.\""
l "\"You made me happy when I was around ya before, but now its like... I don't know, Otter, can't describe it well. Just a whole new type of happy.\""
l "\"Like, you know I fuckin' love you, but I {i}love{/i} you, ya know?\""
l "\"So, final point: Don't fuck Flynn.\""
"My face starts to tingle, my heart thudding so loud in my chest, I'm sure Leo can hear it."
"I inhale shakily. This can't be happening, I must still be dreaming."
m "\"I j—\""
"I'm cut off as I spy an awkward young shadow leering in the doorway, something bulky in his paws."
"Leo notes my shifted attention, turning about-face to the figure."
"I see his muscles tense beneath his t-shirt."
show Leo DarkNeutral at center with dis
l "\"Chase, don't leave. I'll be back in just a second.\""
m "\"Uh, yeah... sure. Anything.\""
hide Leo Dark with dissolve
"I bump my knuckles together, watching the large wolf move to the doorway."
"I see him grab the shadowy fellow by the shoulder, trying to shift him away a little."
"The unknown guy thrusts what looks like a camera bag and tripod toward Leo."
"Leo shoves it right back."
"I see the wolf lean in close, his grip tightening on the other. He mutters something."
"The shadow whinges, his head turning. I think he's looking at me."
"Starting to feel rather awkward, I approach the two."
"As I do, however, the figure departs back towards the main factory floor."
show Leo DarkAnnoyed with dissolve
l "\"I'm never hanging out with anybody but those in our group from here on out, I swear, man...\""
"He curses something in Spanish under his breath."
m "\"I used equipment like that before when I had to do a video story for the school news.\""
m "\"The AV Club rents them out to students for school projects.\""
m "\"Are you... uh... working on a school project?\""
show Leo DarkNeutral with dis
"I see Leo's muzzle pull into a tight-lipped hold. He steps forward, taking hold of my shoulders."
l "\"No. For love of God, Chase, please don't ask me about it again.\""
"His demeanor seems more akin to begging than annoyance, flickers of fear in his eyes."
"I stand in his grasp, slack-jawed."
"This is beyond strange, but I can tell he's serious about his request."
m "\"Alright, but—\""
l "\"Chase.\""
m "\"Leo, are you okay?\""
l "\"I just want to get back to town with you, yeah?\""
m "\"I guess I can respect that request...\""
m "\"I'm assuming TJ's already been picked up by now.\""
"The last I saw of the lynx, he was crying in a beer-soaked puddle."
"I feel like a complete asshole for not checking in on him in person."
"Though, at least I wasn't as bad as Carl, who straight-up fled home."
"Poor TJ is probably blaming himself for everything, too."
"Meanwhile, it turns out Leo is gay and like-likes me, and despite {i}everything{/i}, the stuff he described feeling about me, I feel about him."
"My emotions are so damn conflicted right now, this emo-vampire music is actually resonating with me."
hide Leo Dark with dissolve
"Leo releases my shoulders and moves toward the back door, tugging it a few times."
play sound "locker.mp3"
"He huffs some, then gives it a hard kick with his foot."
"One of the hinges snaps and the door falls into a hanging diagonal position."
play sound "locker.mp3"
play sound "thud3.ogg"
"With a swift stop, the other two hinges snap off as well, leaving the metal door on the floor."
m "\"... we could have gone out the front.\""
l "\"Well, eh...\""
"He stares at the door at his feet before looking up at me."
l "\"Wouldn't have been as rebellious. You like destruction of property, don't you?\""
m "\"I break a mirror at {i}one{/i} rest-stop when I was eight...\""
l "\"Because you didn't get the toy you wanted in your kiddie meal.\""
"He smiles teasingly at me, the moonlight illuminating his backside."
"I can see the faint purples in the sky of inevitable sunrise, as well."
m "\"Hey, you know we don't have fast-food joints like that around here.\""
m "\"That was my one chance at getting that figurine from that stupid dinosaur movie.\""
l "\"Your hand was so damn bloody. I thought you were the coolest.\""
"There is a pause."
hide Leo with dissolve
scene bg postparsons with dissolve
stop music fadeout 7.0
play background "crickrest.ogg" fadein 2.0
"I step past him into the fresh, far less musty air, the faint scent of Leo's cologne now more palpable."
"I cross my arms, staring down the rusty metal of the fire-escape-like stairwell."
l "\"I still do.\""
m "\"Oh, bullshit, man.\""
"I try to maintain a healthy amount of skepticism for his words now."
"Though looking at him now, and having known Leo long enough, I don't sense any visible signs of deception."
"My dad actually suggested I'd be a decent journalist, since I'm pretty good at reading people and their emotions."
"Though, he might have just said that to try to dissuade me from videography."
"Leo begins to descend the stairway, keeping his paws hovering above the guard-rail, just in case."
"I pull out my phone, using the screen as a flashlight for us."
l "\"I'm serious. You act so damn level-headed all the time.\""
l "\"Everyone else in our group — not to be insulting them or nothing 'cause they're family — but they can be pretty out there, eh?\""
l "\"You're always so calm and balanced though.\""
m "\"You mean generic and boring, man.\""
l "\"Nah, like, you're always hanging in the background almost invisible-like, and then you say some snarky shit and everybody loses it.\""
l "\"You're observant, yeah? Like Flynn, but less of an insulting shit about it.\""
l "\"My parents, my siblings — they love you, dude. Mom's always askin' me when Chase is gonna come around again.\""
"We reach the end of the stairway, the insides of my ears probably ruby red at this point."
"The back lot of Parsons is mainly composed of old piles dirt and some foundation, like they were planning on expanding before they shut down."
play music "Willows2.ogg" fadein 6.0

############EDIT THIS BIT##############
m "\"I'm not gonna fuck Flynn. You can ease up on the compliments.\""
############EDIT THIS BIT END##############

"I turn and smirk at Leo, a little in disbelief that those words just left my mouth."
play background "crickrestwalk.ogg"
"We start walking."
l "\"Good. I have no clue what you're into, actually.\""
m "\"Honesty.\""
"Leo looks at me a little warily, that same guilty expression crossing his muzzle once again."
m "\"And... ya know... muscles, I guess.\""
"I see Leo's eyes light up, his maw pulling into a fangy grin."
"It actually is a pretty frightening visage in the middle of the night, were it anyone but Leo."
"Predators, man."
l "\"You should come to more of my games if you want to see those.\""
m "\"The internet exists, too.\""
l "\"Yeah, and how'd that work out for you earlier?\""
"I feel that pang of remembrance and the ensuing feelings of shame all over again."
"This whole night did exactly what I wanted after all: distracted me from my problem."
"I feel Leo's eyes on me, his face softening. He places his paw on my back."
l "\"You missed a lot this season. You weren't even at homecoming.\""
m "\"The tickets were like 30 dollars.\""
m "\"I was saving up for that multiplayer driving-sim game with Carl. We eventually played it for like three hours and never touched it again.\""
l "\"We won by only a few points, and I got two touchdowns.\""
l "\"If you were there, I woulda pointed to the stands where you were and everything — embarrassed the shit out of you, eh?\""
m "\"I wouldn't be embarrassed. I'd be — well, I {i}am{/i} proud of you.\""
"In the past, I had vocally lamented Leo's ascension to jockhood, espescially his douchebag towny teammates."
l "\"Bah...\""
"Now, it's Leo's turn to be dubious. He clicks his tongue against the roof of his mouth, shaking his head."
l "\"You and Carl just think I'm a different person now that I play varsity.\""
"Carl and I would poke fun at him about it, and I think our jokes genuinely upset him."
"I've never really properly apologized about all that."
"In reality, I just didn't like the fact he spent most of his after-school time at practice."
"I miss him."
m "\"You're not. You've always been a blockheaded ball-slinger. That hasn't changed.\""
"Leo lets out a deep chortle."
l "\"You gonna join the cheerleading squad now for me, Otter?\""
m "\"Pfft, I ain't flexible enough for that. You think I can do a high-kick?\""
l "\"No, but I'd pay a dollar to see you try.\""

#####COPY LINE###############

show Leo at left with dissolve
"Coming to a stop, I look down at my stubby legs."
"A dollar is a dollar. That's 1/4th of what I need to get a burger at the diner."
m "\"You're not gonna film this too?\""
show Leo Neutral with dis
"The wolf's shoulders tense, his gaze snapping to me."
l "\"Chase, you said—\""
m "\"—said I wouldn't ask about it. Doesn't mean I can't tease you about it.\""
show Leo Annoyed with dis
"He huffs, but I can tell that sort of cheered him up, in a way."
l "\"Just don't mention it around the group, okay?\""
"I make a circle with my fingers in a gesture of acknowledgement."
"I make sure there is no errant shrubbery around me before directing my muscles to lift my right leg as high up as it will go."
"It turns out, that is barely a 60-degree angle from its stationary position."
show Leo with dis
"I hear the wolf snigger."
l "\"Oh come on, I am just a sack of furry stone and even I can kick higher than that.\""
m "\"We're two different species. Give me a break!\""
l "\"Work for that dollar, Chase.\""
l "\"'Defy species norms and negative stereotypes', as Jasmynn says.\""
m "\"There are physical limitations here that no 3rd period social sciences class can overcome.\""
m "\"And I don't think an otter being paid to perform for a wolf's amusement is exactly a progressive act.\""
l "\"I believe in you.\""
"He says that as saccharine and schmaltzily as possible, eliciting an eyeroll from yours truly."
"I lift my leg, this time bracing my hands underneath my thigh and pushing up."
"I manage to get the thigh itself much higher, though I'm having trouble fully extending at the knee."
"Leo notices and steps over, taking my calf and holding the small of my back supportively, so I don't tip over."
"My muscles are starting to burn something fierce, and the position is pretty damn compromising."
"I frown as hard as I can up at Leo, who bursts into laughter."
l "\"Okay, now I wish I was filming this, Otter.\""
m "\"Dude!\""
show Leo Neutral with dis
"I wriggle free, rubbing my now-sore leg before continuing onward."
"True to his word, Leo fishes his wallet out of the back of his jeans and hands me a crisp one dollar bill."
"I pocket the dollar, looking back over toward Leo."
m "\"Don't I get a tip?\""
show Leo Teasing with dis
l "\"The tip comes later.\""
m "\"Jesus Christ.\""
"I bury my face in my paws, groaning in contrast to the baritone cackling of the wolf beside me."
"Jokes like that have a whole new meaning after tonight."
scene bg sunrisesky with dissolve
"As I peek through my fingers, I see that the sun has crested the edge of the mountains, and the world is bathed in glimmers of orange."
"I've been up for nearly 24 hours now, and my body feels more tingly than tired."
scene bg sunrisehighway with dissolve
"We start walking beside the main road now, the lack of vehicle traffic giving an eerie stillness to the desert."
"Leo walks close to me, to the point where our paws brush against each other from time to time."
m "\"So... that party.\""
"One of Leo's large ears flicks in my direction before he turns, canting his head curiously."
l "\"Yeah?\""
m "\"That wasn't very 'Day-of-the-Dead'-y, was it?\""
"He shakes his head."
l "\"No, it was not. I think some of those deadbeats thought it had to do with the movie.\""
l "\"I only really remember celebrating it once in my home country.\""
l "\"Though, I wouldn't really say it was a 'celebration', yeah?\""
l "\"I just remember my mom, dad, and siblings gathering in a cemetery.\""
l "\"We placed orange marigolds in front of the abuelos' graves, lit candles, and ate quesadillas.\""
m "\"Carl would like that last part.\""
l "\"Heh, no shit.\""
m "\"The prospect of food actually helped him get over his social anxiety to come with me.\""
"I see Leo's face shift to a tight frown."
l "\"Fuck, man, that party probably made his issues so much worse.\""
l "\"They barely had any fuckin' food, too. Some tool named Robert just brought a bunch of fruit.\""
m "\"Better than nothing.\""
l "\"But yeah, I remember we just talked about the loved ones who have passed, told stories, and sort of acted like they were there.\""
m "\"So, do you actually believe that... those who have passed can listen in on us when we want them to?\""
"He looks up for a moment, the color of the sunrise now matching the hue of his fur."
"Sweat stains are visible around his armpits, his knuckles are still bloodied, and his headfur is a complete mess."
"That being said, it is kind of a good look for him."
"Not so much for yours truly, though."
l "\"No.\""
"His gaze shifts back ahead, his tone neutral."
l "\"But it helps the living, you know? We still gotta get by.\""
"A silence hangs between us. It is pretty obvious his mind has drifted to memories of Sydney. Mine as well."
"This sort of awkwardness is common now. Sharing trauma like that and carrying on like nothing happened is usually our go-to."
"It has been about four years now, and it hasn't gotten any easier. Too many reminders here."
"We're all fucked up from it. Leo's overprotectiveness, Carl's anxiety, Jasmynn's escapism, Flynn's rage, my hallucinations, and TJ..."
"God, poor TJ."
m "\"Maybe next year, we could try...?\""
l "\"Chase...\""
"Leo looks at me, his eyes meeting my own before drifting to my paw. Slowly, he reaches over, grasping mine in his."
l "\"I just want to move on, to... cherish what I got, yeah? I want to...\""
"I can hear the word 'forget' upon the tip of his tongue, but he can't bring himself to say it aloud."
"Instead, he squeezes my paw tighter. I squeeze back."
m "\"My therapist told me that I should talk about it more, but it isn't something that I can just... broach in between talk of football and videogames.\""
l "\"Sure as shit way to kill any good feelings in the area, that's for sure.\""
m "\"Like right now?\""
l "\"Otter...\""
"He brings our paws up in front of us, forcing me to look at our own interlaced fingers."
"Seeing the size difference, the red fur gripping my own, is enough to make my neck feel hot and my heart thud heavy."
l "\"Look at what we're doing right now. We can shoot the sad shit 'bout how tragic everything in Echo is, or we can go against the grain and be happy.\""
l "\"I say, let's be fuckin' happy.\""
"Leo smiles down at me, letting our paws fall back to our sides."
"Despite his motivational wording, I can tell from the gleam in his eyes that he's nervous, his usual confident bravado shaken in this new territory."
"I don't blame him. They say this sort of thing is supposed to give you a... butterflies-in-your-stomach feeling."
"Yet as we walk along the abandoned Route 65, I feel less like I have butterflies and more like I'm about to jump out of a fucking plane."
m "\"It isn't that simple, Leo.\""
l "\"Well, fuck it, let's pretend it is for a while and see how that goes.\""
m "\"What exactly are you asking for?\""
"He rubs his forehead, his fanged teeth briefly gritted."
l "\"I just... feh, I don't know how to explain it. Just... cheer up?\""
"That wasn't exactly eloquently put, even by Leo's standards."
m "\"I haven't eaten anything since lunch, swam or slept in 24 hours, I've been beaten in the head, was unable to save TJ from getting bullied to hell...\""
m "\"... and my parents caught me looking at gay porn and now will never look at me the same way again. I still have to deal with that.\""
m "\"I'm not exactly in the best of mental states at the moment.\""
m "\"Though, this—\""
"I gesticulate to the two of us with a swirl of my free hand."
m "\"—is, uh, helping.\""
m "\"Freaking me out, for sure, but... I'm glad you're here.\""
l "\"We'll make all that right, I—\""


play sound "phonebuzz.ogg"
$ renpy.pause(1.0, hard=False)
"I feel my phone vibrate against my thigh, my heart sinking."
"I realize quickly though that it's just a text message and not another call from my parents."
"Mom and Dad haven't sent a text message in their lives, as far as I know, saying they prefer talk as short text messages can lead to confusion."
"I do agree with them on that second bit."
stop music fadeout 10.0
show cellf 28 at center with easeinbottom
centered "_"
l "\"Who is it?\""
"I see Leo sort of crane his neck toward my phone, though he quickly recoils as I glance over at him."
l "\"Sorry...\""
m "\"S'aight. And it's from Flynn. He tossed his salad.\""
"I manage a goofy smile, holding up the screen to Leo."
"He squints down at it for a moment, then exudes a low, rumbling groan, covering his forehead with his paw."
play sound "texting2.ogg"
show cellf 29 at center
l "\"{i}Ay Madre{/i}, he wouldn't shut up about that stupid... gonorrhea lettuce stuff or whatever it's called at lunch today.\""
l "\"Apparently it's got like dried cherries, almonds, and granola clusters mixed in with the lettuce?\""
play sound "phonebuzz.ogg"
show cellf 30 at center
l "\"You serve it with this expensive pear vinaigrette stuff, though they usually give you a packet of it in the bag of salad itself.\""
show cellf 31 at center
play sound "texting3.ogg"
l "\"I mean, it sounds really tasty! The most gringo-y food on the planet, but still good.\""
l "\"I wouldn't eat it by itself, though. I'd need some carne asada on the side, with maybe some cheapass cheese-bread.\""
l "\"...\""
l "\"I haven't eaten since lunch either and I'm really fuckin' hungry.\""
play sound "phonebuzz.ogg"
show cellf 32 at center
centered "_"
"Son of a bitch."
"Flynn was playing fucking matchmaker."
"I look over at Leo, his head tilted to one side and his lips pursed, the thing he does whenever he's really curious about something."
"He did that same damn face as a little kid, too. Usually when he had no idea what we were saying in our language and was feeling left out."
"Seeing him now like this, I think I actually feel more grateful to Flynn than anything."
"Still, I'm left with a nagging question."
play sound "texting1.ogg"
show cellf 33 at center
centered "_"
l "\"So, what's happening now?\""
m "\"Me going to the party and confiding to you that I was gay was part of his plan, apparently.\""
m "\"I'm asking him why he didn't tell me he was gay.\""
l "\"Really? I feel like I should... thank him or something.\""
play sound "phonebuzz.ogg"
show cellf 34 at center
l "\"I bet Jasmynn will be squealing when she hears about all this shit.\""
play sound "texting2.ogg"
show cellf 35 at center
l "\"This is just like one of her comics — the mangos.\""
m "\"Mangas.\""
m "\"I don't actually know if she reads yaoi stuff or not.\""
l "\"That's that anime porn with the twinky-triangle types, right?\""
"I nearly choke trying to contain my laughter."
m "\"Ehehe... are you familiar with it, Leo?\""
play sound "phonebuzz.ogg"
show cellff 1 at center
hide cellf
centered "_"
play sound "texting3.ogg"
show cellff 2 at center
l "\"Yeah, 'course I'm familiar with it! I got a whole bunch of files with that sort of stuff saved in my Sample Music folder on my PC.\""
l "\"Nobody ever looks in there.\""
play sound "phonebuzz.ogg"
show cellff 3 at center
centered "_"
"Weird. What the hell was that about?"
play sound "texting1.ogg"
show cellff 4 at center
centered "_"
"I consider showing Leo the new messages, but he seems sort of distracted now."
"He looks genuinely happy."
"I mean, a bit sweaty, fidgety, and blood spattered — but so am I."
"The idea of ruining that makes me feel miserable."
"Though Flynn's whole behavior, knowing everything about him now, is kind of boggling in contrast to his usual self."
"I exhale and do my best recombobulate, shifting my attention to the big ol' wolf currently holding my hand and looking at me expectantly."
m "\"Don't ever get too comfortable with that sort of thing. I did and now everything's fucked for me in the eyes of my folks.\""
play sound "phonebuzz.ogg"
show cellff 5 at center
centered "_"
play sound "texting2.ogg"
show cellff 6 at center

l "\"Man, your mom is the nicest lady — I can't imagine her kicking you out or anything.\""
m "\"I'm not worried about that. God, getting kicked out almost sounds preferable to having to face them every day with them having seen me like that.\""
m "\"Imagine if your parents found your yaoi folder and how they'd see you from then on.\""
l "\"Well, they shouldn't have been going through my shit in the first place.\""
play sound "phonebuzz.ogg"
show cellff 7 at center
centered "_"
"Egh."
hide cellff with easeoutbottom
"I slide my phone back into my pocket. That's enough Flynn for now, I guess."
l "\"... I think Mamá already knows about me being gay, though.\""
m "\"What?!\""
l "\"She kept asking me if I liked Jasmynn, like... like-like, yeah? It was annoying me and I just up and said she wasn't my type.\""
l "\"Mamá kept prodding me with, {i}'Why, Leonardo? She is a smart one and she has cared for you in your times of need on countless occasions'{/i}.\""
"I try to restrain a snicker at Leo's impression of his mother, the accented, high-pitched cadence rather right on the nose."
"Leo hears my suppressed titters, looking down at me with a feigned scowl before hip-bumping me."
"I nearly go careening off the side of the bike lane into the sagebrush-filled side-basin, but he yanks me back by my paw he's holding."
"I try to imagine Leo and Jasmynn together. It makes sense, I guess, but it is weird to think about."
"Puberty in general has made things so much different."
l "\"She went on, asking what exactly my type was.\""
l "\"I think I was frustrated or something at the time, like after a bad practice session. I said, 'Not girls'.\""
"My eyes widen, picturing the confrontation in my mind."
m "\"Jeez, what happened next?\""
l "\"I regretted saying it — Mamá could see that plain enough on my mug, yeah?\""
l "\"She just clicked her tongue, told me to let her know when I felt like talking more about that.\""
m "\"I'm assuming you haven't really followed up on her offer?\""
l "\"No, Chase, I have not.\""
"There is a silence between us, mostly because I'm trying to think up a response that isn't, {i}'Well, I have it worse'{/i}."
"Before I can speak, we approach what looks like a short, dirt driveway that leads up to a shack of some sort. Leo stops and points toward it."
l "\"Let's cut through here and head to my house through the railyard.\""
l "\"I don't want to deal with Jeremy right now in case he's awake and outside his house.\""
"I sincerely doubt that Jeremy and Clint would be out and about being dicks this early on a Saturday, but I don't argue and follow along."
play music "brianstheme.ogg" fadein 6.0
"Upon closer inspection, it looks like one of those roadside dive bars you see a lot on the reservations, this one boarded up fairly recently."
"The joshua trees and and the old-timey pickup truck give it an out-of-place feeling."
"As far as I know, joshua trees aren't native to this area."
m "\"Huh, never heard about this place before.\""
l "\"I have. It was open for a little while a year or so ago.\""
m "\"Yeah? It would have been the first new business I've heard of around here since I was like... seven, I think.\""
l "\"Like I said, it didn't last long.\""
l "\"Heard from Charley that the owner got busted for some fucked up shit that Officer Mall-Cop found in the backroom.\""
m "\"Christ.\""
l "\"I mean, this is from Charley, so I wouldn't believe all of it.\""
m "\"Like, what specifically?\""
"Leo shrugs, a light frown on his muzzle."
l "\"I dunno, he wouldn't tell me.\""
"We continue moving, Leo kicking an errant bean can along in front of us as we walk."
m "\"Can't believe Charley's still alive.\""
m "\"Turns out absurd amounts of meth is the secret to a long lifespan.\""
l "\"Not if I find out you've been taking it, Otter. I'll shorten your fuckin' lifespan real quick.\""
"He smirks at me and I roll my eyes, glancing back at the side of the abandoned bar as we pass."
stop sound fadeout 3.0
stop background fadeout 4.0
"{b}{i}Keith & Brian's Booze Bastion{/b}{/i}."
play background "reststop.ogg"
scene bg train1 with opening_fade
stop music fadeout 3.0
"The sun is now high enough in the sky that I occasionally have to shield my eyes from it as we head due east."
"Flynn never responded to my text, which is honestly alright with me at the moment."
play music "doublewalk.ogg" fadein 4.0
"Right now, I'm trying to balance upon one of the rails of the train tracks, whilst Leo does the same on the other."
"It is made a bit more difficult by the fact that we're still holding hands, each teeter from him yanking me along as well, and vice versa."
"Despite being, as he puts it, a 'lump of stones covered in fur', he has a lot more poise than yours truly."
"I think my tail might be a bit too thick for balance and agility — it's more suited for aquatic usage."
"That just reminds me how much I could use a swim right now... or at least a bath."
"I feel like a dusty skeever, and I must be smelling musky as all hell at this point."
"I'm a mess, and I'm a mess in front of Leo, who just keeps looking better and better the brighter it gets."
"I'm worried that he's going to take one long look at me any moment now and realize he's made a mistake."
l "\"Hey...\""
"I glance over tentatively, increasingly conscious of how clammy my pawpads are in Leo's grasp."
l "\"I know we kinda glossed over it earlier, but how do you think the others are actually gonna respond to... all this?\""
"I nearly fall off the rail, catching myself with one foot on the ground. Technically it's cheating but this isn't really a competition."
m "\"Egh — what do you mean 'all this'?\""
"He clicks his tongue against the roof of his mouth, just like his mom does. I still don't know what exactly that means."
l "\"Tch, {i}estúpido{/i}...\""
"My gaze falls and I feel my shoulders slump."
"Leo looks over, his expression turning apologetic, and I can feel his thumb rub the side of my paw."
play music "BittersweetPiano.ogg"
l "\"Gah, sorry. I know we're both tired as dirt.\""
l "\"Honest though, if I was in bed right now, I wouldn't be able to sleep leaving it all like this.\""
l "\"So I guess I just gotta come out and say it all plain-like for you, Otter.\""
l "\"You're my boyfriend now, right?\""
"I blink at hearing the words out loud, though when the moment comes, I don't even hesitate."
m "\"You're my boyfriend, Leo.\""
"His pace on the track slows, then eventually stops outright — he turns, facing me."
"We stand in the midst of the abandoned passenger-carriers, the plants around us mostly dead or dormant for the autumn."
"I can't help but have this feeling that we clash with our surroundings, alive and new in something dead and decaying."
"I'm reminded of a word I studied for a Southwestern Literature elective I took — the {i}quoz{/i}."
"It comes to me, as if recited on a recorder in my brain, the short paragraph which I labored to memorize the night before my presentation:"
"'Quoz: a noun, both singular and plural, referring to anything strange, incongruous, or peculiar; at its heart is the unknown, the mysterious.'"
"'It rhymes with Oz. To a traveler, it's often the highest quaesitum.'"
"'For me, everything — whether object, person, or event, when seen clearly in the depths of its existence, in its quiddity, is quoz,'"
"'and every road, every alley, the all to your parlor, the course of a creek, the track of a comet, all are a route to quoz for any traveler —'"
"'any queriest willing to question, to go in quest, to ask the cosmic question of the medieval church drama:'"
"'Quem quaeritis? Whom do you seek, O pilgrim?'"
"William Least Heat-Moon."
m "\"Let's... be happy, yeah?\""
"Moisture wells within his russet eyes, and I recall the last time I saw Leo cry."
"It was after what happened at the lake. It was our first day back to school, and he gathered all of our group together."
"He started out fine, managing simple English and explaining how he promised he was going to protect us all from now on."
"And then he just... kept saying, '{i}I'm sorry{/i}', over and over again."
"Jasmynn was the first to step up and hug him, then Carl, then TJ, then me, and finally Flynn."
"We held each other outside the road and sobbed. Flynn kept yelling something and seemed more incensed than mourning, but I wasn't listening to his words."
"Leo bawled until he was hiccuping, wrought with himself. We all did."
"Eventually, a passerby called one of our parents and we were picked up, one by one."
"The funeral had happened the week before and our parents thought we were ready to... reintegrate, that things were better."
"It never felt like things got better."
"But Leo was always there, keeping his promise."
"Now, my eyes brim with tears. I think it might be in part due to our lack of sleep, but I can't hold back."
"We stare at each other, Leo laughing and wiping his eyes with his palms."
l "\"Heh... heh, you always suck in your cheeks when you're trying not to cry.\""
"He reaches up, ruffling my headfur as he does so commonly."
"I sniff, trying to manage a challenging look, Leo looking blurry in my vision."
"I let go of his paw, taking him by the front of the shirt and pulling him down to my height."
"I shut my eyes tight and kiss him, my arms trembling as I do so."
"Large arms envelop me, his grasp first on my waist, but then upon my face as he holds onto my tear-matted cheeks."
"I realize I have no idea what I'm doing with regard to kissing, and I feel like a fool mushing my face against his, but Leo doesn't laugh."
"The kiss is over rather quickly, but I embrace him as soon as our muzzles part."
"I feel his head rub into mine, a neediness to his demeanor which I share."
"We continue to stand each on our own rail, keeping equilibrium, balanced at the center."
"This makes the hug sort of awkward in structure."
"It actually reminds me a lot of church pamphlets TJ had that described the proper way to hug someone of the opposite sex:"
"'Backs hunched forward, arms around the upper torso, pelvises at least a foot apart from one another.'"
"At least we were all good in the eyes of the Lord so far."
"It feels like several minutes pass, Leo occasionally squeezing me tighter or rubbing his paws across my back. I do the same."
stop music fadeout 9.5
"The position starts to feel a bit sore, especially with my recent battering, and I pull back."
"Leo seems to have been caught unawares, waving his arms as he tries to find his balance again."
play sound "thud5.ogg"
"He stumbles and falls off, his rump hitting the sandy gravel beside the track."
m "\"Oh, shit, Leo! You okay, man?\""
play sound "thud1.ogg"
scene bg train1 with vpunch
"I hop down, but in my haste, my foot catches and I topple over onto the big wolf's chest."
"Adding injury to injury."
"Leo just chuckles, rewrapping his arms around my mid-section. We meet eye-to-eye."
l "\"Clumsy Otter.\""
"I sigh with relief and kiss him again — briefly, as I'm aware I haven't brushed my teeth in 24 hours, as well."
"He strokes his fingers through my headfur — careful to avoid the bump on the back of my head — before releasing me."
"I stand, offering a paw to him."
"He takes it, though just for show, really. He seems to have no problem standing up on his own, now."
l "\"So, before I was rudely interrupted, I asked you how you thought the others will take us, now that we're a couple?\""
"We start walking again, this time with Leo leading."
"He seems to take fancy with an old, rusted crane, the wolf bounding up the step ladder and clambering over it like he's 10 again."
m "\"So, I think that Jasmynn will probably dig it, Flynn will taunt us relentlessly but harmlessly...\""
m "\"TJ will probably be confused but ultimately happy for us, and Carl will probably be bewildered as all hell and awkward about it.\""
"Leo reaches the top of the crane's steps. He peeks over the metal to beckon to me."
l "\"Really? In my head, I imagined when I tell Carl I am queer and stuff, he'll just say, 'That's gay', then continue playing his handheld without caring.\""
m "\"Nah, nah, he... he cares, I think.\""
m "\"Also, I don't want tetanus. I'm good down here.\""
"He nods, making his way back down, his chipper gait an utterly foreign sight as he beams at me."
"He's slap-happy hyper."
l "\"What about your parents?\""
"Oh Jesus."
"One day they catch me with gay porn, the next I have a big-ass Hispanic wolf boyfriend."
m "\"I... I don't know, man.\""
l "\"I want to tell mine about you. They'd be happy for me, I guarantee it, yeah?\""
"My eyes drift down to my pocket, the weight of my phone still resting against my thigh."
m "\"I still have a voicemail from yesterday that they sent me. I haven't listened to it.\""
"I see some of his excited demeanor diminish to his usual, more concerned expression."
"Leo heads over beside me and we continue walking."

#############COPY LINE###############

scene bg rail2
with dissolve
l "\"Chase, whatever they say, you've still got me.\""
show Leo Neutral at farleft with dissolve
"He approaches me and stops, his fingertips tapping his hips as he thinks of what to say."
l "\"You've still got all of us in the group, and if shit got real bad, you could stay with us for a bit.\""
show Leo at farleft with dis
l "\"Jasmynn does it all the time.\""
l "\"Pa and Mamá are used to having a house filled with kids, but since most of my siblings moved out, it's just me.\""
l "\"TJ's parents would never turn you away, either.\""
l "\"And Carl, well, God knows that he has enough damn rooms that go unused.\""
l "\"His parents are barely ever there.\""
l "\"You could be like that one movie with the boy who lived in the walls of the house, making spooky noises at night and eating their gorgonzola.\""
"I let out a small chuckle."
"I remember how Carl used to be really afraid of ghosts a few years ago."
"I got to hang out with him and play videogames as a coping mechanism excuse."
"Still, now that I have my phone in hand, I still have that same twisting dread within my gut."
show Leo Neutral with dis
m "\"I'm just...\""
m "\"Egh, it's like everything is changing and my head is spinning.\""
m "\"My folks will never see me the same again.\""
l "\"They won't, because you're almost a fucking adult, Chase.\""
"The curtness of Leo's tone has me look up from my phone and back to him."
l "\"{i}Está yuca{/i}. People grow up. You have, and... {i}really{/i} handsomely, I gotta say, yeah?\""
"I look off to the side. The flattery is making my neck warm and my cheeks flush."
"Despite everything, I still can't believe it's Leo who is saying all this to me."
show Leo with dis
l "\"The thing is, your parents are gonna love you no matter what. They're good like that. I know it. I bet my neck.\""
"He grasps his throat, looking down at me with bloodshot eyes and a smile."
l "\"Other shitpiles around here are the ones I'm gonna have to worry about, because no way I'm hiding that I have Chase the Otter as my boyfriend.\""
l "\"And trust me...\""
"He raises up his large fist in front of me, showing the crimson which still stains his knuckle fur."
l "\"... they try anything, or harass ya for it? I'll make sure they know the consequences.\""
"I shift my focus from Leo's fist to his wild gaze."
m "\"Man, you need some sleep.\""
show Leo Sheepish with dis
"Leo blinks, then brings his fist back to rub the back of his neck."
l "\"Heh, fuck yeah, I do.\""
show Leo Neutral with dis
"He sniffs, rolling his shoulders some before looking back to the phone in my hand."
l "\"Alright, let's listen to this voicemail, eh?\""
show Leo Annoyed with dis
"He looks off to the side, sort of muttering embarrassedly under his breath."
l "\"... Double-jump-that-sucker and whatnot...\""
"It's so cringey, but I feel like I want to kiss him again."
"I smile wryly at Leo. He just huffs."
l "\"Fair warning though: you're still probably grounded as hell.\""
"I snerk, my chest feeling tight and my mouth dry."
m "\"Oh yeah, I know that. I get yelled at if I don't call my parents back within five minutes anyway.\""
m "\"I'll miss you while I'm in lockup, though.\""
show Leo with dis
"Leo grins lopsidedly, less wild now."
l "\"I'll see if I can arrange a conjugal visit or something.\""
"I take a deep breath, navigating to the voicemail inbox section."
l "\"Ready?\""
"I can see Leo's family home in the distance now, some smoke rising up from the backyard."
"They must be grilling something."
m "\"Ready.\""
"I press play."
scene bg cred1
window hide
stop sound
stop background
play music "when_your_arms_were_around_me.ogg"
$ renpy.pause(14.5, hard=True)
scene bg credtemp
$ renpy.pause(5.0, hard=True)
scene bg credtemp9
$ renpy.pause(5.0, hard=True)
scene bg credtemp10
$ renpy.pause(5.0, hard=True)
scene bg credtemp11
$ renpy.pause(5.0, hard=True)
scene bg credtemp2
$ renpy.pause(5.0, hard=True)
scene bg credtemp3
$ renpy.pause(5.0, hard=True)
scene bg credtemp4
$ renpy.pause(5.0, hard=True)
scene bg credtemp5
$ renpy.pause(5.0, hard=True)
scene bg credtemp12
$ renpy.pause(5.0, hard=True)
scene bg credtemp6
$ renpy.pause(5.0, hard=True)
scene bg credtemp7
stop music fadeout 10.0
$ renpy.pause(5.0, hard=True)
scene bg black with opening_fade
play background "crickets.ogg" fadein 2.0
$ renpy.pause(4.5, hard=True)
show cellff 9 with dissolve
$ renpy.pause(3.0, hard=True)
play sound "doorknock.mp3"
$ renpy.pause(1.0, hard=True)
play sound "text.ogg"
show cellff 8
$ renpy.pause(3.0, hard=True)
play sound "text2.ogg"
show cellff 10

$ renpy.pause(4.0, hard=True)
hide cellff with slow_dissolve
stop background fadeout 4.0
$ renpy.pause(4.0, hard=True)
return
