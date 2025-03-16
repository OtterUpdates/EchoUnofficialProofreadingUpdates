label leowednesday:

stop music fadeout 3.0
scene bg AllWednesday
with slow_dissolve
$ renpy.pause(3.0, hard=True)

scene echoroad
with dissolve
play background "highway.ogg" fadein 3.0
window show
"I stare out the window as we roll down the dusty streets of Echo."
"Every road, every corner, every trailer, and every tree has a memory attached to it."
"There, in the middle of the dusty parking lot that belonged to the Corner Market, is a tiny stand."
"That used to be where I'd get ice cream after begging for a dollar from my parents."
"It's crumbled and boarded up now, the paint peeling off in tiny chips."
#!! probably? since it's a specific rock
"And there, in front of Duke's house, is the big flat rock that Jenna was standing on when she told me she was going to run away from home."
"I can still remember almost exactly how she was silhouetted against the red sunset behind her."
#!! Their first kiss wasn't at noon. This is already fixed in Jenna's version of this scene, so just copy-pasting it over to here
"And the old train yard where I kissed Leo for the first time after staying up all night at our first real party."
"I look over at Leo. He's got one hand on the wheel, glancing up at the rearview mirror occasionally to trade jabs with Flynn."
f "\"I'm regrettin' not lettin' him know we're comin'. You know? You'll be lucky if he even gets his ass out of bed.\""
l "\"We'll call him, then.\""
f "\"And what if he doesn't answer?\""
"Leo doesn't say anything, instead focusing back on the road. TJ fills the silence after a while."
t "\"Well, I don't think it's too weird. It's just like we're hanging out again. Nothing wrong with that.\""
f "\"Sure, but making it about Carl is just...weird. Maybe if his birthday was like, next week? Two weeks tops.\""
j "\"Oh hush, Flynn. It'll just be like we're hanging out. You acting weird about it isn't going to help anything.\""
"The car starts slowing down and I snap out of my daydreaming to look up, knowing that we definitely weren't at Carl's house yet."
stop background fadeout 5.0
play loop "engine.ogg" fadein 3.0
"That's when I see a round canine figure standing further up on the side of the road."
"She's standing in the dirt that separates the road and the field in front of a broken and rusted barbed wire fence."
l "\"I think that's Janice.\""
"I look over at Leo and he seems concerned, his brows furrowed as he carefully steers the car right up next to the coyote."
"I can see why; she's crouched over, elbows on her knees, staring at the ground."
l "\"Roll down your window, Chase.\""
"I do as he says, struggling a little with the old crank handle."
f "\"The hell is she doing out here?\""
"We come to a stop next to the coyote, kicking up some dust."
l "\"I dunno...HEY!\""
"Leo leans over me and smiles out at Janice, who's still looking at the ground."
l "\"Everything al—\""
"Leo's voice cuts off in a weird choking sound."
#!!! This line is just a mess. I made an attempt
"I look at him, confused, then look back out the window and can't help but gasp."
"It was hard to tell from the angle, and all the dust kicked up by the van, but now I can see that Janice has her pants down around her thighs..."
"...I can also see everything else."
"I sit back quickly and avert my eyes, looking out the windshield instead."
f "\"What the fuck.\""
j "\"Oh my God. Leo, keep going.\""
"Jenna whispers it, her voice strained."
l "\"Oh! Uh, sorry, uh—\""
"Leo stops talking and I chance a glance out the window again."
"Janice is looking at us now, and she's smiling."
"It's a weird smile because it isn't touching her eyes."
"It's unnerving."
"Leo stares back."
m "\"Leo, let's just go.\""
"I hiss out the side of my mouth, staring out the windshield again. He seems reluctant to, though, looking concerned."
l "\"Janice, do you need some help?\""
"His tone is one you might use on a toddler...or a crazy person."
"I don't hear her say anything, except maybe a grunt. Leo bravely keeps trying, though."
l "\"We can give you a ri—\""
#!! recognize? recognized? the copy-pastes use different versions
"Leo stops talking in time for me to hear a pattering sound, a sound I recognize well from my time as a kid pissing on the dirt roads of Echo."
"The van lurches forward, then resumes a smoother acceleration back onto the empty road."
f "\"Holy shit! What the fuck was that!?\""
l "\"I don't...\""
"Leo's frowning, looking as confused as I've ever seen him."
l "\"Should I—should I go back?\""
t "\"No!\""
"I look back and see TJ covering his face."
j "\"Maybe. She could be having some kind of psychotic episode.\""
f "\"Or maybe she just had to piss.\""
l "\"I don't think so. Did you see the way she looked at me?\""
m "\"She was probably just on something. Isn't everyone?\""
l "\"No, she doesn't do stuff like that.\""
m "\"Well, maybe she does? You never know with people.\""
"Again, Leo doesn't say anything, and neither does anyone else. We don't go back."
stop loop fadeout 3.0
scene bg mansion with fade
show Flynn Annoyed at left with dissolve
play background "reststop.ogg" fadein 3.0
f "\"I fuckin' told ya!\""
"Leo stabs the doorbell again, frustration etched across his face."
"I shift the bag I'm carrying around in my paws, trying to look through the frosted glass on the sides of the door."
m "\"Maybe he's getting high?\""
show Jenna at right with dissolve
j "\"He should still be able to hear.\""
m "\"I mean, maybe he just doesn't want to?\""
"TJ holds up his phone."
show TJ Rejected at center with dissolve
t "\"He's not answering his phone either.\""
play sound "knock.ogg"
"Leo knocks on the door hard, his bicep bulging."
show Jenna Annoyed with dis
j "\"Well, I guess breaking the door might get us inside.\""
"Leo stands back, paws on his waist as he takes a deep breath."
"He's determined."
"And I guess he should be considering he set all of this up."
hide Jenna
hide TJ
with dissolve
show Flynn Annoyed at center with moveinright
f "\"We shoulda just told him to meet us at the diner, or somethin'.\""
show Leo Annoyed at farright with dissolve
l "\"Do they lock their windows?\""
show TJ Surprised at left with dissolve
t "\"What!?\""
"Leo growls."
l "\"It's not like we're breaking in!\""
show TJ Rejected with dis
"TJ's ears pin back, a frown on his face."
show Leo Neutral with dis
"The wolf puts a paw to his forehead, closing his eyes."
l "\"Sorry, but I think he's just asleep, and it shouldn't be too hard to just get in there and wake him up.\""
"I look over at the side of the house and see a window well."
"I point at it."
m "\"What about that?\""
l "\"Too small.\""
show Jenna Neutralhips at farright with dissolve
j "\"I could probably fit.\""
hide Jenna with dissolve
"She hops off the front porch and crouches down next to the window, pushing at it."
j "\"Wait, there's a security sticker here.\""
f "\"Well ya gotta arm it first and Carl's such a lazy ass I know he didn't.\""
f "\"'Sides, if we set it off we can just run. It's not like they'll show up any time soon.\""
j "\"Or instead of acting like criminals we can just stay until the cop shows up. She knows us.\""
"Jenna hesitates, then pushes at the window again, but it doesn't budge."
j "\"Locked.\""
l "\"Let's try the one above it.\""
j "\"That's too high.\""
l "\"I'll boost you up.\""
t "\"I think this is going a little too far.\""
"Leo ignores him and stands next to the window before making a platform for Jenna's foot with his paws."
"Steadying herself with her paws against the wall of the house, Leo easily lifts Jenna and she manages to grab the ledge."
f "\"Fuckin' hell this is so fuckin' stupid.\""
"Flynn mutters next to me, but I make a point of not looking over at him."
"I feel for Leo; he worked hard to make this happen and everyone is giving him a hard time over it."
"Jenna pushes against the window and it glides open easily."
show Leo with dis
l "\"Yes! Now I'm gonna boost you all the way up. Hold on.\""
j "\"Careful!\""
hide Jenna with dissolve
"Like they're some kind of cheerleading duo, Leo shoves Jenna all the way up with one paw and she disappears through the window."
"Her bush tail is the last thing we see...until she pokes her head back through."
j "\"Kitchen.. I fell in the sink.\""
l "\"Great! Now unlock the door.\""
"She disappears again and we make our way back to the front door."
f "\"Leo, you're fucking crazy.\""
show Leo Annoyed with dis
l "\"If you don't shut your fuckin' mouth, Flynn, I'll kick you right in your vagina. Sound good?\""
show TJ Surprised
show Flynn Surprised
with dis
f "\"Jesus, calm your—\""
"Leo turns on him, one foot in front of the other."
"Flynn shuts up, then, and me and TJ are left to shift around uncomfortably on the porch."
hide Flynn
hide Leo
hide TJ
with dissolve
"Finally, we hear the door rattling and it opens."
play sound "dooropen.ogg"
show Jenna at center with dissolve
j "\"Called his name but he didn't answer...\""
f "\"Well he's gotta be here. It's not like he can go anywhere...or would want to.\""
scene bg kitchen with dissolve
stop background fadeout 3.0
play music "quiet.ogg" fadein 3.0
"Carl's house is as massive and immaculate as I remember it."
"It is a mansion, after all."
"There are a few bowls and wrappers lying around on the marble counters."
"I assume that's because Carl's parents aren't here to tell him not to be a slob."
"Flynn immediately heads up the stairs."
f "\"Yo, Carl!\""
"I set the bag down on the table and TJ sets the cake there too."
"I look over at him."
m "\"You alright?\""
show TJ Neutral at center with dissolve
t "\"Yeah, why?\""
m "\"Just asking. How was your hike with Jenna?\""
t "\"Alright...wish you were there, though.\""
m "\"Yeah. Me too.\""
show TJ with dis
t "\"I might go again in a day or two, if you'd like.\""
m "\"Sure, why not?\""
"I promise myself that that wasn't an empty promise."
show Flynn Rejected at left behind TJ with dissolve
f "\"Well he's not in his room.\""
show TJ Neutral with dis
"Flynn's actually looking a little worried now."
show Jenna at right with dissolve
j "\"Maybe he went for a walk?\""
show Flynn with dis
f "\"Carl? Walking? In this weather? Hell no.\""
t "\"Does he have other friends? Maybe he went out somewhere?\""
f "\"I don't think so...\""
l "\"Well, let's do a quick sweep of the house. It's a big place.\""
hide Jenna
hide TJ
hide Flynn
with dissolve
"Flynn heads back upstairs and Leo heads for the downstairs with Jenna."
"TJ looks around the kitchen, then moves over to the living room, checking the couches."
"I decide to head out back, if not just to get away from the others since things feel unusually tense between us today."
scene bg backyard with dissolve
"As I step out into the backyard I'm a little surprised."
"It's different from when I was last here."
"The playset is gone and so is the massive trampoline they used to have."
"The biggest shock, though, is seeing that the huge tree house that used to sit in the old oak tree is gone."
"I stand there for a moment, feeling a vague sense of loss."
"I have too many good memories of that place. Time moves too fucking fast."
"After a while I remember why I'm here and look around again."
"No Carl, of course, but I start walking around anyway, looking behind bushes even though I know it's stupid."
"While I felt for Leo, I could still see where Flynn was coming from."
"It would have been a way better idea to warn Carl, or just meet up somewhere else."
"Leo just gets carried away a little when he has his heart set on something."
"He probably had the whole scene planned out in his head before we even got here."
"Mostly I just feel really bad for him. He's been working really hard to make this trip interesting for all of us."
"I think it's our fault more than anything that nothing's working out."
"Flynn's a dick, Carl doesn't care, Jenna's also kind of being a dick, and TJ's always into stuff that none of us are."
"And I'm just...boring."
"As I round the corner of the house I'm surprised to see Flynn standing there."
"He must have come out the front door."
m "\"Oh, hey Flynn. I thought you went upstairs.\""
"Flynn doesn't seem surprised at all to find me out here, which makes me think he was looking for me."
show Flynn at center with dissolve
stop music fadeout 3.0
play loop "reststop.ogg" fadein 3.0
f "\"I did. Wasn't there so I thought I'd look outside.\""
m "\"Oh...well he's not in the back, so...\""
"I don't know why, but Flynn is making me feel awkward as hell."
m "\"Is something wrong?\""
show Flynn Annoyed with dis
"Flynn folds his arms and leans up against the house."
f "\"Well, Carl's missing so I guess that's a problem, huh?\""
m "\"Uh, yeah...\""
"I try to think of something to say."
m "\"Well, I'm sure he's just hiding somewhere, or maybe he's out at the diner. Probably just got tired of being stuck in his own house.\""
f "\"Yeeaaah...\""
show Flynn with dis
"He straightens up again and steps forward and, I don't know why, but I take a step back."
play music "loneliness.ogg" fadein 3.0
f "\"You were hangin' out with Leo yesterday, right?\""
m "\"Uh, yeah, for a little while.\""
f "\"You spent the night there?\""
"I pause for a second to give him the hint that I'm not exactly okay with him prying like this, but I answer anyway."
m "\"No, I got back to the motel at like, three.\""
f "\"Huh.\""
m "\"Yeeaaah...\""
"I start to turn back around."
m "\"Hey, why don't we check the basement—\""
f "\"Chase.\""
"He's got the same tone as a disappointed parent and that kind of pisses me off."
"I turn back around."
m "\"What?\""
f "\"You realize what you're doing is stupid, right?\""
m "\"Excuse me?\""
f "\"Getting back with him during fuckin' spring break. Pretty stupid, right?\""
"I had a feeling that's where this was going, and now that I know for sure I'm definitely pissed off."
m "\"How is that any of your business?\""
show Flynn Annoyed with dis
f "\"How is it not? You two seem pretty okay with making it our business, right?\""
m "\"Uh, no?\""
"He sneers at me."
f "\"Cuddling up at the lake where our friend died is pretty messed up, isn't it?\""
m "\"What!?\""
f "\"I saw you two, you know I did.\""
m "\"So what? What does that have to do with Sydney?\""
f "\"I guess I just find it weird that you'd start up your old flame on what's practically a grave.\""
m "\"What the hell are you talking about?\""
"Feelings change from anger to bewilderment."
"I did know what he was talking about, I just didn't know why."
f "\"Well, since it's all out in the open now, why not talk about it?\""
m "\"You're the one that put it out in the open.\""
m "\"In the worst way possible, by the way.\""
show Flynn Depressed with dis
"His sneer disappears."
m "\"I just don't get why you're connecting those two things. We weren't even talking about Sydney.\""
show Flynn Annoyed with dis
f "\"How!? What else does that lake make you think of?\""
"I'm at a loss for words, totally confused."
"This is Flynn; I never talked about Sydney with him after it happened. I was too scared to."
m "\"Well I don't think of it as his...as his...grave, or anything.\""
f "\"Oh really? It's just a fuckin' lake to you then, huh?\""
m "\"He didn't die there, Flynn. It was in the hospital.\""
f "\"It might as well have been there, right?\""
"I swallow hard, wanting desperately to get back inside."
m "\"Let's not...let's not talk about this right now.\""
f "\"Oh, I guess I was confused; everyone's been telling me that I NEED to talk about it.\""
m "\"Well not like this. Not with just me here. We should all be together if we want to have this talk.\""
"I turn around again, making it clear that I'm leaving."
show Flynn Depressed with dis
f "\"Wait...\""
"The change of tone in his voice makes me turn around again."
"It's softer, almost pleading. I'm not used to hearing Flynn talk like this."
f "\"I just—I'm just trying to look out for you, Chase. He's not—\""
"I feel some of that anger returning."
m "\"He's not what?\""
f "\"Well he's not exactly a stable guy, is he?\""
"I laugh."
m "\"And you are!?\""
"He dips his head and I can tell he's embarrassed even though he doesn't have the ears to tell me so."
m "\"And not just you, all of us! We're all a little fucking crazy aren't we?\""
show Flynn Teasing1 with dis
"Flynn smiles a little bit."
f "\"Well, that's what happens when you live in Echo.\""
m "\"That's what all the kids at school said.\""
show Flynn Depressed with dis
"Flynn frowns again."
f "\"Listen, I'm just lookin' out for ya. He's...He's just...\""
"I sigh loudly and cover my face with a paw for a second."
"I was hoping I'd been able to change the subject but now we're back to Leo."
stop music fadeout 3.0
"I'm surprised when I lower my paw and Flynn is just a few feet away."
m "\"Flynn, just drop it. It's none of your business.\""
show Flynn Annoyed with dis
"His gaze hardens."
f "\"I think it is when I see a friend taking advantage of another friend.\""
m "\"Taking advantage of me!?\""
f "\"Yeah. Has been since you were fucking fifteen!\""
"I immediately know what he's implying."
m "\"Fuck off, Flynn. You're acting like my fucking pare—\""
"He takes another step forward and I back away, but he angles it so that I'm pressed up against the house."
"I get the urge to run away, but I feel like doing that will only affirm how much this has escalated."
"There's a change in him as well, something unfamiliar in his eyes, in his stance, in his voice, even."
"He leans down to my height."
f "\"Like playing with fire, huh? You've seen it in his eyes.\""
f "\"He's. Fucking. Crazy.\""
"He pokes me in the chest to emphasize his words."
m "\"Crazy? Kind of like you are right now?\""
show Flynn with dis
"Flynn pulls away, straightening his back, but still looking down at me."
f "\"Yeah? Well, maybe I am...\""
"The awkward silence stretches out, seems to go on and on until..."
f "\"You know what? I think—\""
show Flynn Surprised with dis
l "\"Chase.\""
"Both of our muzzles flick in the direction of Leo's voice; mine to the right, Flynn's to his left."
"Leo stands there, ears perked forward, though his expression seems neutral."
"I wonder how long he's been standing there. I can tell Flynn's wondering the same thing."
show Leo Neutral at farright with dissolve
l "\"Any sign of him?\""
m "\"Uh...no.\""
show Flynn with dis
"I slide out from under Flynn, making my way towards Leo."
m "\"I checked the back, but I didn't see him anywhere.\""
"Leo doesn't even look at me, staring over the top of my head."
"I look and see Flynn staring right back, his shoulders still tensed."
"That's when I feel Leo's heavy, strong arm drape over my shoulders."
show Flynn Annoyed with dis
"Flynn's eyes narrow."
l "\"Let's get back inside, then.\""
"As Leo leads me away I get the feeling that he's still staring Flynn down, even though I don't look up to check."
stop background fadeout 3.0
scene bg kitchen with fade
play music "quiet.ogg" fadein 3.0
show TJ Rejected at center with dissolve
t "\"I'm getting worried...\""
show Flynn at right behind TJ with dissolve
f "\"No shit. Carl doesn't just disappear from his house like this; he doesn't have anywhere to go!\""
show Jenna at farright with dissolve
j "\"Calm down. He could be anywhere. He has more friends than just us.\""
f "\"The fact that he isn't answering his phone is kinda fucking suspicious.\""
"Leo holds up his paws."
show Leo Neutral at left behind TJ with dissolve
l "\"You know he forgets to charge his phone sometimes.\""
show Flynn Annoyed with dis
"Flynn's getting more and more frustrated, starting to pace around the living room."
f "\"He never goes out with other friends, that's the problem.\""
l "\"Listen, maybe we should just wai—\""
f "\"You all can wait here. I'm gonna find him.\""
hide Flynn with dissolve
play sound "doorshut.ogg"
show Jenna Rejected with dis
"Flynn makes for the door and before anyone can say anything it's slamming shut behind him."
"We sit in silence for a while, staring at the door that Flynn just took off through."
show Leo Rejected with dis
"Leo lets his breath out in a long sigh, rubbing his face."
l "\"Alright, let's think; where else does Carl have to go?\""
m "\"The comic book shop?\""
"Leo looks at me for a second."
l "\"Maybe if someone else gave him a ride, but like Flynn said, does he have anyone else to do that for him?\""
j "\"Well, if you guys are going to do that then I'll probably stay here in case he comes back.\""
t "\"Yeah, and we can keep looking.\""
l "\"Sounds good.\""
"Leo pulls his keys out of his pocket, then looks back at me."
l "\"Coming with me, Chase?\""
m "\"Yeah.\""
"I follow Leo out the door, actually starting to feel worried about Carl."
scene bg mall with fade
play loop "highway.ogg" fadein 3.0
"We walk around the mall for about an hour, checking the food court and every shop we pass."
"It's clear that this idea was pretty hopeless from the beginning."
"Jenna lets us know that Carl hasn't shown up at the house either and that they're heading back to the motel."
stop music fadeout 3.0
stop loop fadeout 3.0
"Finally, Leo and I call it quits and head back to his house before walking to the diner for dinner."
scene bg diner with fade
play music "neutraldiner.ogg" fadein 3.0
m "\"So...where do you think he went?\""
"Leo's hunched over, an elbow on the table and his chin in his paw, staring out the window."
show Leo Neutral at center with dissolve
l "\"Dunno...\""
m "\"Do you think we should call someone?\""
l "\"Like the cops? Not yet. He's an adult, so they won't really look into it until it's been days.\""
l "\"We should probably call his parents, though, if he doesn't show up by tonight.\""
"I don't say anything, stirring my milkshake around."
"I glance back over toward the kitchen area, watching a very tired-looking Janice gather up plates before taking them to the back."
"I was pretty much mortified when I realized she was here and about to take our order, mostly just because I was embarrassed for her."
"She didn't really say anything, though, just took our order and left."
"I examine my milkshake closely, though for what I'm not sure."
l "\"I'm not too worried, though. He's been under a lot of stress and probably just wanted to leave town for a while.\""
m "\"But who would he do that with, and why wouldn't he tell us?\""
"Leo sips on his milkshake and I wait for him to finish."
show Leo Depressed with dis
l "\"I guess things really have changed.\""
m "\"Yeah?\""
"I rest my chin in my palm, meeting his eyes so he knows I'm listening."
l "\"I mean, the way Flynn was acting all day. He really can't stand us anymore...Carl probably just feels the same way.\""
m "\"I don't think so. Flynn's usually been that way, right?\""
l "\"Not like that, like the way he was talking to you earlier.\""
"So he did hear."
l "\"Guess you were right. I should have just left shit alone.\""
l "\"We all used to fit together so well, but now we've all changed and it's like we're bending ourselves to fit again.\""
m "\"I guess that's just life, right?\""
"Leo grunts and keeps staring at the window."
"It's clear how much he wanted this all to work out, to give us the opportunity for one last hurrah before we separated for good."
"And now I'm actually pretty angry at myself...and the others."
"This is our last chance to really say our goodbyes and it's like we don't care at all."
"Jenna and TJ are off doing their own thing."
"Carl's getting lost and probably high."
"And Flynn...Flynn's being Flynn."
"I lean forward, then, grinning."
m "\"You know, I'm really happy you planned all of this.\""
show Leo Neutral with dis
"Slowly, Leo shifts his attention from the sunset to my face."
"I smile widely for him."
m "\"This is the most fun I've had all year, even though everyone's acting like a dick.\""
"I dip my head self-consciously."
m "\"Including me, I know, but this whole thing has reminded me about a lot of the good things in this town.\""
m "\"And even though things have been kind of shitty, I think it's a good note to leave off on.\""
show Leo Questioning with dis
"Leo raises his brows."
m "\"Because weren't things always shitty? It's part of the experience.\""
"Leo stares at me for a long time and I feel my grin start to fade."
show Leo Wry with dis
"But then he reaches forward and rubs a thumb up my nose."
"I blink in surprise and he shows me the smear of white on his thumb pad."
l "\"Sorry. It was hard to take you seriously looking like a cokehead.\""
"He grins and licks his thumb."
show Leo with dis
"I blush and grab a napkin to wipe my face, but Leo rests a paw on my arm."
l "\"But seriously, thanks...for trying, at least.\""
"Leo looks like he's about to say something else, hesitates, then opens his muzzle again—"
unk "\"Cute.\""
show Leo Neutral with dis
"Leo and I look up to find a lanky, patchy, ugly ring-tailed cat staring down at us with beady, black eyes."
show Clint at farright with dissolve
cl "\"I don't know if you knew, but there's a lot of other people in here trying to enjoy their meal.\""
"Clint puts a paw down on the edge of the table, leaning in."
show Clint Smirk with dis
cl "\"Could you try not to ruin it for us?\""
"He grins at me, showing me just how many teeth he's missing."
"Guess he graduated from huffing paint since the last time I saw him..."
cl "\"The hell are you doing here, Chase? Didn't you dump his fat ass?\""
"I grimace."
"I can't tell if he's joking or not, or if he's still the same asshole that I remember him as. I haven't talked to him in years."
m "\"Well, it kinda looks like you dumped your own ass, Clint. What happened to you?\""
"I can see Clint's brain work as he digests what I said, deciding whether or not he should be offended."
"I can also see his tail twitching behind him and it's patchy too, leaving some parts of it bald, like a rat's tail."
show Leo with dis
l "\"Actually, Clint, you're right; we're all trying to eat, but there's a smelly, ugly ring-tailed skeleton ruining it for us.\""
"Clint flicks his attention from me to Leo, who smiles sweetly at him."
l "\"Mind doing us all a favor and getting the fuck out?\""
show Clint Smirk at right with moveinright
"Clint leans in low to the table, putting his face up next to Leo's."
"Leo keeps a straight face and I'm impressed because I can smell the stench of Clint's breath even from here."
cl "\"Think you're funny, beaner?\""
l "\"It's 'spic'.\""
l "\"If you're trying to make me mad you might as well do it right, eh?\""
"Leo takes a sip from his milkshake nonchalantly while Clint gapes at him."
"His brain, which I imagine is swiss cheese at this point, tries to come up with some kind of retort."
cl "\"Go...go fuck yourself.\""
l "\"Yeah? Well I'd tell you to do the same, but you've got a sister at home, don't you?\""
"Clint moves fast, swinging a fist up and around towards Leo's jaw."
show Leo Neutral with dis
"Leo's ready for him and lunges to the side, though the fist still glances the side of his face."
play sound "fight.ogg"
queue sound "glass.ogg"
hide Clint with dis
"He grabs Clint's arm and yanks him down onto the table, which knocks over my milkshake and sends it splashing into my lap."
"I gasp and stand up and move to the side of the table while Leo starts to rub Clint's face into the mess, smashing it into the table a few times."
show Janice at farright with dissolve
ja "\"Stop it!\""
"I jump as Janice shouts right next to me."
"Leo hears her too and turns around while still holding Clint down."
"The dead look is still in her eyes, and the fur on her face is matted, like she'd been crying a lot but hadn't washed since."
ja "\"I am not going to deal with this today, Leo.\""
show Leo Annoyed with dis
l "\"You know Clint started it.\""
"Leo's ears are flat as he looks back at Janice, clearly thrown off."
"Underneath him Clint snarls and thrashes."
ja "\"Am I gonna have to get the taser from the back?\""
show Leo Neutral with dis
"Slowly, Leo backs off of Clint, who immediately shoves himself off the table."
#!!! This needs some disambiguation with Leo and Clint both using the same pronouns. Using Clint twice is a bit awkward too; 'the ringtail' is okay
"I can see Leo prepare himself in case Clint takes another swing, but the ringtail doesn't even look at him."
"His already-dirty tank top smeared brown from the milkshake, he stumbles to the door and disappears outside."
ja "\"And clean up that fucking mess before you leave.\""
hide Janice with dissolve
"With that, the old coyote turns and stalks off to the back."
"She leaves me and Leo to stare at each other before we ruefully wipe up the spilled milkshake with brown napkins."
"There are only two other patrons in the diner with us: a skunk and a jackrabbit."
"But I can feel their eyes on us the whole time, and it only adds to the embarrassment."
m "\"What do you think her problem is?\""
"I ask Leo under my breath as we come back from tossing the ball of wet napkins in the trash can."
"He just shrugs, though, and I follow him quietly out of the diner into the late afternoon light outside."
scene sunset with dissolve
stop music fadeout 3.0
#! Could use this comma
"We walk in silence for a while, with me walking awkwardly because my soaked and sticky pants are incredibly uncomfortable on my thighs."
"We stop at the motel where I change and shower before grabbing a fresh change of clothes, then we start back out again."
"I think about staying behind at the motel, but I feel like that would be a dick move after what Leo's been through today."
"As we walk back Leo takes a detour, stopping at the convenience store."
"The fight has made things a little awkward between us so I just shove my paws into my pockets and follow Leo."
"We go to the back where he grabs a twelve-pack."
"He doesn't say anything to me either as he makes his way to the front to pay."
"Finally, when we're back outside he nudges me in the direction behind the convenience store."
play music "intimate.ogg" fadein 3.0
l "\"Let's sit.\""
"I lead the way because we've both done this dozens of times before."
"We step off the asphalt and down a little ways into the brush where Leo pulls me up onto a boulder."
show Leo Neutral at center with dissolve
"Leo sighs, pulling out the first beer bottle."
play sound "bottleopen.ogg"
"Leaning back, he pulls out his keys to use the bottle opener on his keychain before handing it over to me."
"He does the same for himself, then practically chugs the whole thing before grabbing another even before I'm able to take my first swig."
"I don't comment on it and instead look out at the sunset, thinking about how nice it would be to just sort of run off into the wilderness."
"At least for a little while."
"I lean back and sigh, noticing a white and brown splotch on the knee of Leo's jeans."
m "\"What you said to Clint...that was pretty mean.\""
l "\"He said some pretty mean stuff too, and it's not like I like saying that shit to him.\""
"Seeing me lying back, Leo shifts closer to me, allowing me to rest my head against his thigh."
"Again, the familiar position probably isn't a good idea, but I just don't care."
m "\"So does Clint still live with his dad?\""
l "\"No. He went to prison two years ago.\""
m "\"Really? Because of—\""
l "\"Yeah.\""
m "\"Shit.\""
"We sit in silence, enjoying our quiet surroundings."
"As I lay there I hear Leo open another bottle, then another."
show Leo Depressed with dis
"Finally he lets out a big sigh."
l "\"Chase. Come back to Echo.\""
"I close my eyes, turning my vision blood-red against the sunset."
m "\"Maybe...just not yet.\""
"He doesn't press the issue, instead reaching out for another bottle."
"By the time I get to my second one the rest are gone."
scene nightroad
show nightoverlay
with fade
stop music fadeout 5.0
play loop "crickets.ogg" fadein 3.0
"As we walk back to Leo's house in silence he occasionally brushes his tail up against my own."
"I let him. He's mildly drunk so he's sort of excused for now."
"I do have to push his muzzle away when he leans up against me for some support after his feet hit a sudden dip in the road."
play sound "steps.ogg"
"I'm busy trying to steady him when I hear footsteps pounding up behind us."
"Before I know it, Leo's shoved me hard to the side and I go stumbling into the weeds."
"Whirling around, I see a dark figure running off to the side from Leo, his attack aborted as he saw the wolf had seen him."
show Clint Smirk at right behind nightoverlay with dissolve
"He comes back around and I immediately see that it's Clint...and he's got a crowbar in one paw."
"My stomach drops as I look from him to Leo, who's got a giant smile on his face like this is exactly what he wanted to happen."
stop loop fadeout 3.0
play music "argument.ogg" fadein 5.0
m "\"What the hell!?\""
show Leo Neutral at left behind nightoverlay with dissolve
l "\"Come back for more, Clint?\""
"Clint doesn't say anything, instead he just screams and runs at Leo again."
"Usually, I wouldn't be worried about Leo in a fight with Clint, but the crowbar and the fact that Leo can barely stand have me really worried."
"Leo backpedals, then ducks low and lunges forward, which I don't think Clint expects."
"His grunt is guttural, but to my surprise he doesn't go down."
"Instead, he grips the back of Leo's shirt before raising the crowbar and bringing it down hard into Leo's back with a solid, meaty thud."
play sound "thud.ogg"
show Leo Annoyed with dissolve
"I gasp and cringe, starting to jog towards them."
"Clint presses forward and Leo trips over something, landing on his butt."
"Clint raises the crowbar again and Leo raises a paw."
"For about two seconds they play a game, with Leo moving his paws around above his head, anticipating the swing."
"Clint, meanwhile, keeps trying to re-angle the crowbar so that Leo will miss."
"He doesn't get a chance, though, because that's when I reach them."
"I'm not exactly a good fighter considering I've never been in a fight before—"
"—but the idea of Leo getting his face beaten in with a crowbar provides me with the terror that spurs me on."
"I jump on his back, grab a handful of the fur on his forehead and yank back as hard as I can."
"I guess I should have hit him, or something, but it seems to work alright."
"His remaining teeth flash in the porch light and I get a hot blast of his rancid breath as he snarls angrily."
play sound "thud.ogg"
play loop "ringing.ogg"
scene bg black
"Suddenly I'm sitting down on the asphalt, feeling like my forehead had just caved in."
stop loop fadeout 5.0
"He must have somehow swung the crowbar back and hit me."
scene nightroad
show nightoverlay
with slow_dissolve
"I desperately rub at my head, imagining the skull shattered into a million pieces like an egg, but everything feels like it's still in shape."
"The fight's still going on and now I can hear Leo snarling."
"It's not a sound that I've heard that often, but it's deep and way scarier than anything Clint could have managed."
"I try to focus on the spot that I see their bodies tangled together."
"When I do I see that Clint's on top again, the crowbar raised, pointy end down, aimed at Leo's face."
"I start to crawl towards them but there's no way I'm gonna make it—"
play sound "thud5.ogg"
"Again, the sound of something hard striking flesh, but this time it isn't Clint hitting Leo."
"It's Clint that hisses in pain this time as he arches back, baring his fangs."
"There's a dark shape behind him, but before I can focus on it Leo's massive paw smashes into the side of Clint's face."
"Leo's not playing this time."
"In fact, it looks like he put everything he had into that punch and the sound it makes is like a slab of beef being thrown against concrete."
"Clint's body visibly goes slack before he slumps down against Leo, only to be shoved roughly to the side."
stop music fadeout 3.0
play loop "crickets.ogg" fadein 3.0
"I crawl up next to the wolf and he looks over at me as I do. His paw immediately goes to my head to steady it as he looks closer at my face."
l "\"Fuck, did he hit you?\""
"That's when I realize that I have a massive headache and my head feels like it's full of water."
"I rub a spot that itches a bit right above my eyebrow and my pads come away slightly dark and bloody."
l "\"That fuckin' piece of shit!\""
play sound "thud.ogg"
"Leo sends a backfist into the side of the downed Clint's face."
ku "\"Hey! That's enough, Leo.\""
"That's when I remember that it was someone else that actually saved Leo."
"The voice is familiar, but it isn't until I look up at the source that I recognize Kudzu."
show Kudzu Annoyed at right behind nightoverlay with dissolve
"He's breathing hard and he's holding the crowbar that Clint dropped."
"The dark spots around his eyes blend in with the night and accentuate how wide his actual eyes are."
"He looks spooked."
ku "\"What the hell are you guys doing!?\""
"He sounds pissed and I feel a little defensive."
m "\"Hey, he tried to run up on us.\""
"Kudzu's eyes flick over to look at me before focusing back on Leo."
ku "\"I thought we had this shit figured out! Why the hell are you fighting again!?\""
"I don't really get why this Kudzu guy is freaking out so much. His nostrils flare with each breath."
"You'd think he was the one that almost got his brains run through with a crowbar."
show Leo Neutral at left behind nightoverlay with dissolve
l "\"Calm the fuck down. You know how Clint is.\""
ku "\"He wouldn't do half of the crap he does if you didn't antagonize him so much.\""
ku "\"You say he was a bully, but from what I've seen it's the reverse.\""
#!!! Can I just say that Leo asking Clint if he fucks his sister is so milquetoast it barely qualifies as bullying, and yet the characters repeatedly mention that Leo is off the deep end with what happened at the diner.
#!!! Meanwhile, Clint swung first at Leo, so Leo is fairly justified from that angle too.
#!!! This would be a more interesting subplot if Leo got physical without Clint swinging first, or if he said something way worse than Clint.
"It's hard to think of Leo as a bully, but the way he had acted towards Clint in the diner was a bit much...even if it was Clint."
show Leo with dis
l "\"Hey, if he can't take it then maybe he shouldn't dish it, eh?\""
"Leo grins and sticks out a paw to Kudzu who glares, but nevertheless reaches down to help him up."
"Leo promptly pulls me up with him."
"As I get to my feet a wave of dizziness instantly hits me and I stumble into Leo."
show Leo Annoyed with dis
l "\"Fuck! See!?\""
"Leo steadies me and looks into my eyes, worry etched all over his face."
m "\"I'm fine...just got dizzy for a sec.\""
l "\"That's not fine. Do you feel sick? Can you see straight?\""
m "\"Seriously, I'm fine. Just give it a minute.\""
l "\"{i}Puchica{/i}! Going to kill that hick when he wakes up.\""
"At that moment Clint makes a snorting sound and starts to roll over."
"Leo's eyes flash to where he's laying, but Kudzu steps up between the two, still glaring."
ku "\"No! Get the fuck back home and take care of the otter. I'm gonna see if I can keep him from trying to kill you later on down the road.\""
l "\"Fat chance. He's been wanting to kill me since middle school.\""
"Clint starts to sit up, supporting himself with both paws as he looks around."
ku "\"GO!\""
l "\"Whatever.\""
show Leo Rejected with dis
"Leo turns back to me and his eyes soften as he puts an arm around my shoulders."
l "\"Come on, we might need to go to the hospital.\""
m "\"I'm fine, really.\""
hide Leo
hide Kudzu
with dissolve
"The low tones of Kudzu's voice murmuring to Clint fade off as we stumble into the night."
l "\"No, you're not fine. He hit you fucking hard. Goddamn that fucking idiot; he could have killed you!\""
"I put a paw back to the sore on my forehead and rub at it. Leo grabs my wrist."
l "\"Don't do that, you'll infect it. We'll clean it up back at my place.\""
l "\"Swear to God, I'm not gonna leave my house without my gun again.\""
"Suddenly, Leo's face takes on an odd look."
l "\"Ugh.. one—one sec.\""
"He makes as if to steady me with both paws, then stumbles off to the side of the road."
"It's dark and I can't see him, but I sure as hell can hear a retch followed by a splash."
#! either or
"This happens about three more times before Leo shakily, but more steadily, approaches me from the darkness, a sheepish grin on his face."
m "\"You okay?\""
l "\"Yeah.. yeah, just had a little too much?\""
m "\"Really? The Leo I knew could down 15 cans and still walk.\""
l "\"Hey, rolling around with a crazy long-tail sitting on you won't do your gut any favors.\""
m "\"Mhmm, sure.\""
"Leo chuckles and wraps an arm around me again, though this one feels more intimate rather than just being there to keep me steady."
"We walk in silence for a while, just enjoying the evening air."
"The temperature is always perfect here when the sun's gone."
"It gets me more annoyed, though, because I imagine we'd be having a much better time if Clint hadn't just tried to murder us."
"At least that's what I imagine he was trying to do since hitting someone with a crowbar isn't exactly fucking around."
m "\"Has it really gotten this bad between you and Clint?\""
"Leo squeezes me."
l "\"It's always been this way.\""
m "\"It looked like he was trying to kill you.\""
l "\"Well, the gringo really hates me.\""
"Leo laughs, then falls silent for a while, ears pinned back."
l "\"I guess he was angrier than usual.\""
l "\"I think it's just that I might have pissed him off more than I usually do.\""
"I look up at him."
m "\"About that.. what you said to him back at the diner was really awful.\""
l "\"You too? How can he expect not to get hit with that if he's going off about us and about me being a spic?\""
"Leo barks out a laugh."
l "\"Talk shit get hit, I always say.\""
m "\"I dunno, man. What his dad did is different.. it's not his fault, you know.\""
#! I think this fix is needed?
l "\"Hey, he might be fucked up, but he can still make the decision to not be a complete dick to everyone, can't he?\""
"I wish Jenna were here to help back me up on how that isn't exactly fair to Clint."
m "\"Anyway, I think he was on something. Did you see how crazy he looked?\""
l "\"He's always on something.. and speaking of which.\""
"Leo's steps slow and I look ahead to see an isolated house further up the road."
"The porch light is on and I see a skinny figure get out of a chair and start walking up the front yard."
"It's clear he means to intercept us and I slow down with Leo as he draws closer."
show Leo Neutral at farright behind nightoverlay with dissolve
l "\"Duke.\""
"Leo nods at him."
show Duke Dazed at left behind Leo with dissolve
"The skinny weasel looks us both up and down, raising up a paw to pull a drag from what looks like a cigar."
"...I assume it's actually a blunt because it smells like Carl."
"He's as patchy and unhealthy-looking as I remember him."
"Not as torn up as Clint, but still bad enough to know he's done his fair share of dabbling in meth."
"He doesn't say anything and after a while Leo clears his throat."
l "\"Isn't it a nice—\""
du "\"He's here...\""
"As Duke cuts Leo off he's staring right at me, so I assume it's me he's talking about."
m "\"Hi, Duke.\""
"I probably couldn't have said any more awkwardly."
show Leo Neutral at right with moveinright
"Leo steps forward, partially in front of me."
l "\"Did you need something?\""
"Duke lets out a long stream of smoke towards us."
"Definitely a blunt."
#! is this slang (happnin') intentionally butchered? reads like a typo
du "\"Same shit's been happenin' to me...after ya told me about it.\""
show Leo Questioning with dis
l "\"Hmm?\""
"Leo looks at him, looking politely puzzled, though I can see his tail twitching behind him."
du "\"You been seeing shit, now I'm seeing shit.\""
"It's quiet for a few seconds, then Leo laughs."
show Leo Wry with dis
l "\"Haha! Well maybe lay off the drug cocktails?\""
show Duke Angry with dis
du "\"No! It's different, the shit I see. Almost real. I saw him.\""
"He nods at me again and for some reason I'm starting to feel really uncomfortable."
"Leo laughs and this time it's much more forced. He starts pushing me along, further up the street."
hide Leo with dissolve
l "\"Sorry Duke, but Chase is taken. Janice is still single, though!\""
play background "trailsteps.ogg"
"Duke follows us, walking along the dirt while we stay on the asphalt."
du "\"When did he get here.\""
"Leo doesn't say anything and keeps pushing me along."
"I can see Duke getting angrier and I don't want another fight, so I finally butt in."
m "\"I got here on Saturday...is something wrong, Duke?\""
stop background fadeout 5.0
"Duke doesn't answer. He just stops and watches us go, a frown stretched across his face."
hide Duke with dissolve
"I keep on looking over my shoulder at him, but he doesn't move and he doesn't take his eyes off us."
m "\"What the fuck?\""
l "\"Stop looking at him, Chase.\""
m "\"What was he talking about?\""
l "\"Does it matter? Just keep moving and hope we don't run into any more of these psychos.\""
"I manage not to look back again, but I feel his eyes on the back of my neck the entire time."
stop loop fadeout 3.0
scene bg leokitchen with dissolve
play music "neutral.ogg"
#! probably?
"Even though the instructions say to only take two, Leo gives me three generic acetaminophen pills."
scene bg leosbathroom
"After that, he takes me to the bathroom and starts cleaning the cut on my forehead."
"I grimace against the sting of the rubbing alcohol."
show Leo Rejected at center with dissolve
l "\"We really should take you to the ER. This might even need stitches.\""
"I lean my head into his paws because not having to hold it up myself feels good."
m "\"Mmh, no. It's not that bad.\""
m "\"Besides, even if it is a concussion they'll just send me home and tell me to get some rest.\""
m "\"Along with a $500 bill.\""
l "\"I played football; I know. But you never know how serious it could be.\""
"I sigh and don't say anything, deciding it would be easier just not to argue."
"Leo starts to debate whether or not to shave the fur but I finally get annoyed and tell him to get on with it."
"As he prods around I can feel the area around the cut swelling and I wonder if I'm gonna get a black eye."
show Leo Neutral with dis
"Leo finally steps back and starts putting everything back into the first aid kit."
m "\"Wait.\""
show Leo Questioning with dis
l "\"Hm?\""
"Leo glances at me questioningly."
m "\"Aren't you hurt?\""
"He thinks for a second."
l "\"I don't think so. I feel fine, I mean.\""
m "\"Turn around.\""
"I'd seen Clint hit Leo with the crowbar, and he'd hit him hard."
hide Leo with dissolve
"Leo sighs before finally turning around, placing his paws on the sink as he stares into the mirror."
"I look at his back, the black shirt dusty from the dirt he had rolled around in."
"Carefully, I lift the shirt up his back."
"It's not as bad as I thought it would be. I can see the raised fur from a growing welt where the crowbar had hit, though."
"There aren't any cuts there, but I do see some spots of dried blood."
m "\"You have a bunch of little cuts.\""
"I see the smooth muscles under Leo's fur shift as he flexes them."
l "\"Hm, really? Must have been from the rocks in the road.\""
l "\"I think my shirt came up a little while we were wrestling around.\""
m "\"Give me the alcohol.\""
"Leo sighs again but hands it over."
m "\"And take off your shirt.\""
#!!! The (purposefully) part is a bit awkward. "slowly, sensually" seems fine to me. "Purposefully" is implied by his smirk and Leo's behavior in general
"He smirks at that and slowly, sensually, strips his shirt off."
"I try to ignore him, but I'd be lying if I said I wasn't turned on by his body."
"It's been a long time since I last saw him shirtless, and he's kind of changed."
"He's thicker, broader in the shoulders and chest, the muscles smoother and a little more filled out."
"I swallow and start to dab the alcohol into the cuts."
"He makes no indication of feeling any pain, instead swishing his tail around and flicking it up between my legs."
"Again, I don't know why, but Leo has a way of making you want to play along even if you know it's a bad idea."
"He's been flirting with me this whole time, so I guess he's sort of just broken down my defenses."
"Once I finish rubbing in the alcohol I let a paw linger on Leo's hip."
"We both stay like that for a while until Leo finally turns around, leaning back against the sink."
show Leoexp Wry with dissolve
"I look over his form, his broad chest down to his thick stomach."
l "\"Like what you see?\""
"When I look back up at him his brows are raised and before I can say anything he's leaning down."
"I think he's about to kiss me so I turn my head to the side, but instead he just nuzzles the side of my head as he brings me in for a hug."
stop music fadeout 5.0
"I freeze for a second, but relax into his hold after a while, enjoying the feel of his warm fur against mine."
"He doesn't say anything, just holds me."
play music "beat.ogg" fadein 15.0
"I can feel his excitement through his pants as he presses into me, then starts nibbling at my ear."
"I gasp as he catches it between his teeth and I almost moan."
"He, of course, knows I have sensitive ears."
"He moans a little in response and, before I know it, he's pulling me up against him."
"Then he lifts me off the ground as he spins around and sits me up on the sink."
scene leoandchase with slow_dissolve
"My head throbs again and I think I'm about to fall, but he holds onto me before he begins digging his muzzle into my neck, kissing and licking."
"I gasp and hug around his body, pulling him closer as he licks and nips."
"Leaning my throat back, I expose more of my neck to him, closing my eyes as the back of my head presses against the mirror."
"Leo growls, his paws sliding up under my shirt, feeling up my stomach before moving to my chest."
l "\"Fuckin' hell.\""
"He moans it, sounding like he just scratched an unreachable itch, like he just had his first drink of water in days."
m "\"L—Leo!\""
#! this might be intentionally written as "lick to the skin", but it reads as overly verbose. maybe change up that bit of the line entirely
"I gasp, about to tell him to stop, but then his tongue burrows in past my fur to lick the skin and my eyes roll."
"He pulls back, finally, and I lower my gaze to meet his."
"His tongue is hanging out, making him look a little goofy. I can see a few of my short brown hairs on his tongue."
"He starts to lean in again, and this time I don't turn my head away."
stop music fadeout 3.0
"As he almost reaches me, his eyes suddenly flick to the right, looking over my shoulder and I see shock cross his expression."
play sound "clatter.ogg"
scene bg leosbathroom with dissolve
"Then he jumps and spins around, knocking over the soap dispenser and first aid kit."
"I jump too."
m "\"What!?\""
"Leo continues to stare, one paw clutching his chest, the other digging into my thigh."
l "\"I—I...\""
"I wait for him to finish, but he doesn't go on."
m "\"Did you see something?\""
l "\"I thought I did...Just seeing things, I guess.\""
"Finally, he turns his attention to the first aid kit and leans over, starting to pick everything back up."
#! could use a little restructuring to get a comma after "Slowly" without making the sentence pause-heavy
"Slowly I slide down from the sink, pushing my shirt back into place, realizing that the moment had passed."
"While I'm curious as to what he saw, I'm also conscious of the fact that the break in our intimacy has made things awkward again."
m "\"Um, should we check the house? Could be Clint...\""
l "\"No, no. Wasn't Clint.\""
"Leo grabs his shirt and pulls it back on before turning to me."
l "\"Just seeing things.\""
"I think back to Clint."
m "\"Well, alright.\""
"As we leave the bathroom Leo looks back in for a moment before flipping the light off."
"I think it's a little strange that he makes sure to close the door."
"Leo doesn't make a move on me again that night, instead keeping a good few inches between us on the bed."
"I can't help but wonder if I did something wrong."
"What I do know is that I'm kind of disappointed."

jump leothursday