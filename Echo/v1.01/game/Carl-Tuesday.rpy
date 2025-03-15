label carltuesday:

stop music fadeout 3.0
window hide
scene bg CarlTuesday
with transition_fade
$ renpy.pause(3.0, hard=True)
scene bg motelfull with fade
window show
"Turns out it was a good idea to hang out with Carl today."
#chat history
"After texting back and forth with Leo I learn that he's actually planning a birthday party for the ram."
"It's a little weird since Carl's birthday isn't for another month, but I guess it's just an excuse to have a party."
"Leo tells me to keep Carl distracted for the day while they go shopping for decorations and gifts."
"He also tells me he'll get my gift for Carl, which is fine with me."
"TJ's pretty bummed, though, considering it throws off his hiking plans, but Jenna promises him they'll at least hike half the trail."
"I want to talk to him, but he's acting pretty cold towards me, probably because I'm bailing on my promise to go with him."

scene bg mansion with fade
play music "oldwinds.ogg"
"I drive to Carl's house because it's pretty far separated from the rest of Echo, up against the foothills of the Casa Demonio mountain range."
"It'd probably take me fifteen minutes to get up there, and there's no way in hell I'm doing that, in this heat, uphill, when I've got a car."
"The main reason it's separated like this is because Carl's house is a mansion."
"Carl's family is loaded. A legacy that's followed them ever since Carl's great-great-whatever struck it rich over a hundred years ago."
"James Hendricks eventually went on to start an ice cream business which, at this point, has spread out over most of the Western half of the country."
"Carl's mom is the CEO, I think."
"Actually, now that I'm thinking about it, I should probably get some shots of the mansion considering its role in the town's history."
"Most of the old mansion has been demolished at this point, but I think parts of it are still from the original structure."
"Probably best to ask first, though."
"I walk up to the front door and ring the doorbell, listening to the fancy chime inside."
"I wait for about a minute, starting to wonder if Carl is asleep, or just high off his ass, when I hear some voices from behind the house."
"I'm definitely recognizing the crackly timbre of Carl's voice along with the high tenor of Flynn's."
"I head around the house, stepping carefully through the desert landscaping and walking into the backyard."
stop music fadeout 5.0
play loop "reststop.ogg" fadein 3.0
f "\"—'Cuz you wanna make out with him?\""
c "\"No, because you like to make things weird. I just want it to be relaxed—\""
scene bg backyard with dissolve
play music "comeover.ogg"
"That's when Carl notices me as I round the corner, clutching my camera bag to my side."
show Carl Neutral at right
show Flynn Annoyed at left
with dissolve
"He's leaning over a bush with a giant set of clippers while Flynn lounges up against the wall, watching him."
show Carl with dis
c "\"Whoa, Chase!\""
show Flynn Surprised with dis
$ renpy.pause(0.5, hard=False)
show Flynn Depressed with dissolve
"Carl's ears perk and he grins."
show Carl Teasing with dis
c "\"Sorry, Flynn—\""
"Carl rolls his big head at the lizard."
c "\"—was supposed to be watching for you.\""
"Flynn doesn't look at me right away, instead choosing to pull the toothpick he's chewing on out of his muzzle to look at it."
"He's still embarrassed about yesterday."
"Good."
m "\"That's alright. Wasn't hard to hear you guys from the front.\""
show Carl with dis
c "\"Yeah, uh, just doing some yard work...obviously.\""
"He rubs behind his head."
c "\"Promised my parents I'd get this done before they got back.\""
"Carl starts snipping at the bush again."
"He's unusually sharp right now, I'm guessing because he hasn't had anything to smoke."
"Either way, it's jarring to see him so animated."
m "\"Well, looks like you're doing a good job.\""
show Flynn with dis
f "\"Oh, he's only moving this fast because he wants to hang out with you, Chase.\""
"Even though the sentence is technically being said to me, I feel like Flynn's directing it at Carl."
show Carl Annoyed with dis
"Carl furrows his brow."
c "\"Chase, you can go inside if you want. The back is open.\""
"I think that's a good idea, because it's clear now that I've walked in on an argument."
f "\"You should have seen him a few minutes ago; it was like he had a girlfriend comin' over.\""
"Carl sighs loudly and his snips start to get a bit more violent."
c "\"No, I'm just glad to have some company that isn't only you, Flynn.\""
show Flynn Annoyed with dis
"Flynn looks annoyed and that annoys me."
"He really didn't have the right to be frustrated with anyone after yesterday."
f "\"Really? Always seemed to be enough for you in the past.\""
show Flynn Teasing1 with dis
"Flynn makes a kissy face."
"I have no idea if this is one of their inside jokes, or not."
"Carl stops snipping for a second, then starts up again, more slowly."
show Carl Teasing with dis
c "\"Well, you know, lizards can be fun, but they don't have ALL the parts that I like, if you know what I mean.\""
"Carl smirks sideways at Flynn."
"Flynn sneers back and, though I've decided that they're still joking, there's definitely a growing tension between them."
f "\"What'cha sayin' there, Carl?\""
"Carl stops snipping and plants the point of the clippers into the ground, leaning on it as he turns to face Flynn."
c "\"What I'm saying is you've got no ba—\""
show Flynn Teasing1 F with dis
"Before Carl can finish his sentence Flynn turns to the right, away from him."
"This also brings his fat tail around to slam into Carl's crotch with a 'whap' that makes me cringe."
show Carl Surprised with dis
$ renpy.pause(0.1, hard=False)
hide Carl
with dissolve
play sound "fall.ogg"
with vpunch
"Carl jumps, then squeaks, before toppling to the ground."
c "\"Oh man, my NUTS!\""
f "\"Yeah, definitely wish I had those; all dangly and vulnerable and shit. Anyway, I'll leave you two sluts alone.\""
"Flynn sticks the toothpick back into his muzzle and I have to consciously try not to cover my crotch while he walks by me."
hide Flynn with dissolve
"He hasn't looked at me this whole time."
"Once Flynn's gone I sidle up to Carl, who's still curled up on the ground, holding himself while he mutters under his breath."
m "\"Uh, you alright?\""
c "\"Fuuuuuck, no.\""
m "\"Um...\""
"There's not really anything I can do, so I rub his shoulder with a toe comfortingly and he freezes up as I do, looking at my foot."
c "\"Uh, I'm alright, though.\""
"He gets himself into a sitting position before he gets up awkwardly, standing bow-legged."
m "\"I forgot how much Flynn likes to hit people in the nuts.\""
show Carl Annoyed at center with dissolve
c "\"I'll get him back. It still hurts him if you hit hard enough.\""
"As he stands there, doubled over with his paws on his knees, I look around."
"Carl's house has actual grass in the back, which is rare in Echo; most people either xeriscape or just let the sagebrush take over."
"Another rarity is the two tall trees on either side of the yard."
"That's when I notice how empty one of them looks."
m "\"Hey, where'd the tree house go?\""
show Carl Neutral with dis
"Carl follows my gaze."
c "\"Oh yeah, my dad took it down a few years ago. It was falling apart.\""
"His dad also built the tree house. I can remember hanging out up there, playing on our portable game consoles with a fan at full blast."
"Even then it was still almost too hot to hang out up there."
"I walk up to the base of the tree and put my hand against the trunk, grinning."
m "\"Man, remember all the shit we did up there?\""
show Carl with dis
"Carl shuffles up next to me (still bow-legged) and grins, too."
c "\"Yeah, good times.\""
"I think about climbing it, but I notice that the branch we used to use as a foothold has been cut off."
m "\"Your dad ruined this thing.\""
"Carl scrapes at the spot where the branch used to be with a hoof."
c "\"Yeah, I guess it made the mowing harder, and we didn't use it anymore, so he just cut it off.\""
"I can see Carl's looking for a way up, too, and soon enough his eyes settle on a branch just above his head."
m "\"I don't know if—\""
"Carl's already jumping to grab onto the branch with both paws. It doesn't look very sturdy."
m "\"Dude, that's gonna break.\""
c "\"So? I'm fucking fat; I'll bounce.\""
scene carltree with dissolve
"I'm about to tell him again that the branch is definitely going to break when I notice his shirt riding up all the way over his round belly."
"It's not like he's a bag of lard, though. It's a controlled type of gut, held tight with the muscles underneath pulling it in as he flexes."
"He notices me staring right away and kicks out at me playfully."
c "\"Pervert! First my moobs and now this.\""
"I jump back and he tries to follow me with a bigger swing of his legs, and that's when the branch snaps loudly."
"Carl goes down once again, landing squarely on his back."
scene bg backyard with dissolve
hide Carl
with dissolve
play sound "fall.ogg"
with vpunch
c "\"Ooomph!\""
stop music fadeout 3.0
"I cover my face instinctively, but I still hear the hollow thud, followed by the whoosh of breath going out of his lungs."
"Slowly, I lower my paws and find the chubby ram rolling back and forth on the ground, eyes wide as his mouth hangs open."
"A distant memory comes to mind of a time when we were both ten and Carl was showing me a trick with his new bike ramp."
"The handlebars ended up in his gut when he landed and he spent the following minute rolling around on the ground just like this."
"Good times."
m "\"Shiiit.\""
"I suck in air through my teeth and kneel next to him again, patting him uselessly."
#!! original version of this line is a little long-winded. also "and" repetition can be prevented with "to"?
"After a few seconds of hesitation, I reach over to grab the front of the waistband of his shorts and pull up on it."
"Even though he's completely deflated, he looks at me with a bizarre expression and swats at my paw, giving a few breathless snorts as he tries to laugh."
m "\"Hey, it's supposed to help you breathe! I've seen the coaches do it at school...\""
"I'm realizing that Carl's waaay too heavy to arch up like that, so I give up and end up just petting his stomach, wishing I could help somehow."
m "\"Just...just stretch out.\""
"His breath is already coming back, but he follows my instruction anyway and we sit there for a while, the silence punctuated by his heavy breathing."
"I start laughing."
m "\"Jesus Christ, Carl. Can you go one day without hurting yourself?\""
"He chuckles, too, his belly shaking under my paw."
c "\"Now you know why I don't go outside. Ugh.\""
"He slumps back for a while, taking in deep breaths before lifting his head again."
"He looks down his chest at my paw and grins."
c "\"Seems like you can't keep your paws off me, though.\""
"I move my paw, letting him pull down his shirt as he grunts and sits up."
m "\"How about I just let you suffocate next time.\""
c "\"I almost did, laughing while I couldn't breathe. I thought you were trying to grab my dick.\""
"I put my paws on my hips."
m "\"Is it because I'm gay?\""
c "\"That might just be it.\""
"Carl grabs the branch that had broken off the tree and quirks up the corner of his mouth."
c "\"Ugh, Dad's not gonna be happy about that.\""
m "\"Who cares? It's just a branch.\""
c "\"You know my dad.\""
"He gets up and tosses the branch over the fence into the desert, then turns back to me."
c "\"So now that it feels like Lucha fucking Lobo just gave me the {i}Quebradora Con Giro{/i}, I think I'm done for the day.\""
c "\"Wanna work on your project, now?\""
#!! I think "hang out out here" was intentional, but it looks like a typo as a reader. "hang out here" is fine enough, or consider rewording to avoid the situation, e.g. by using "outside"
"I'd honestly rather just hang out here with Carl, but the sun's enough to put a damper on that."
stop loop fadeout 3.0

scene bg livingroom
with dissolve
play music "neutral.ogg"
"Carl's house is like a labyrinth."
"I think he once told me that it has over thirty rooms, which is fucking insane."
"The living room is about five times larger than the one in my parents' house and it's hard to miss what looks like a 100-inch flat screen against the wall."
"According to Carl, the first mansion was even bigger, though."
"After getting a drink he leads me straight downstairs into the basement."
"Down the hallway, we pass a small home theater, what looks like an entertainment room with a bar, and then a small gym."
"The quick glance I get shows at least ten fitness contraptions."
"After that, things get a little more dingy, and I can see how portions of the foundation could be decades old."
scene bg basement with dissolve
"Finally, at the end of the hall, Carl opens a door and I can see from the ceiling that it's right under the stairs we came down on."
"Carl waves his paw around and finally grasps something before pulling down."
"An old light bulb comes on and I see there's a little door with a small latch on it."
stop music fadeout 5.0
"He opens it and I'm greeted with a musty smell as Carl slides through the opening."
scene bg black
with dissolve
"I follow tentatively, making sure I'm not walking into any cobwebs."
m "\"Are there a lot of spiders down here?\""
c "\"I don't think so. We sprayed a few weeks ago.\""
"It's extremely dark and I hear Carl grunting next to me."
c "\"Ugh, there's a floodlight here somewhere...Ah! Here it is.\""
play sound "switch.ogg"
play loop "floodlight.ogg" fadein 3.0
scene bg crawlspace with dissolve
"Like everything in this house, it's big for a crawl space."
"Pillars sprout from the ground in two rows that stretch back almost into darkness."
"The ground is covered in a tarp and I see dozens of plastic bins lining the walls."
m "\"This is a lot of shit.\""
c "\"Yup, it's a few generations' worth of shit.\""
"I walk over the tarp to look into one of the bins, but all I can see is clumps of cloth and towel through the cloudy plastic."
"Carl walks past me straight towards the back of the crawl space, his big hooves clopping along loudly."
c "\"I actually helped them sort through all this stuff last year, so I think I know where it is.\""
"I follow him, but it's hard to see in the darkness."
m "\"Should we get a flashlight?\""
c "\"Naw, it's only in two tubs, I think. We'll just pull 'em to the front.\""
"I stand off to the side as I watch him push bins around, looking at the labels on top."
"I look over at one of them and see \"home movies\" written on it, and it's filled with cassettes."
show Carl at center with dissolve
c "\"Ugh, don't remind me.\""
"I look up and see that Carl's noticed me staring at the bin."
m "\"What?\""
"Carl grunts as he lifts up a bin and drops it pretty carelessly to the floor. I'm pretty sure I hear something break."
c "\"Mom had me help her convert all that to digital. Took all fuckin' year.\""
m "\"Wow...\""
c "\"Yeah, it's in the cloud now. You're actually in a lot of those videos.\""
m "\"Huh, really?\""
c "\"Yeah, birthday parties and shit.\""
"Of course I would be."
"Carl's dad practically had a video camera glued to his eye back in the day."
"I used to hang out with Carl almost as much as I did Leo once we started going out."
"I even went on their family vacation a few times."
"But then me going out with Leo changed things. Looking back, I think Carl was kind of unhappy with that."
c "\"We can watch a few once we're done here, if you want.\""
m "\"Uh, sure.\""
"That sounds like an old person thing to do, but I am curious."
c "\"Found it!\""
"Carl slides out two plastic bins and I see \"History\" written on the top."
c "\"Help me carry one.\""
"Carl lifts up the top one and starts waddling back to the front."
hide Carl with dissolve
"I bend over and lift the second, and I'm surprised at how fucking heavy it is."
"I'm worried I'm not even gonna get it off the ground for a few seconds, but I manage after a while."
#! Change to "for" maybe? I can't tell.
"If Carl's bin is as heavy as mine then he's a fucking beast for being able to lift and carry it like that."
"I stagger after him, almost certain that I'm gonna go headfirst into the wall."
"Once we make it back near the stairs, I bend over to set down my bin, and that's when I see a massive spider sitting on the lid."
"It takes about half a second for me to recognize the black shape and spindly legs."
m "\"Oh FUCK!\""
play sound "mallet.mp3"
"I scream and drop the bin, and before I know it I'm halfway back from where we came, panting and shivering."
show Carl Surprised at center with dissolve
c "\"Holy shit, what happened?\""
"I tremble and try to steady my voice."
m "\"A fucking spider!\""
show Carl with dis
c "\"What? You're really still scared of those? Man, for a second I thought my sister came home and then got murdered.\""
m "\"You told me there weren't any!\""
c "\"I didn't say that. I just said we sprayed.\""
m "\"Just get rid of it!\""
"At this point I've shuffled a little closer back to the light and I can see Carl grinning as he bends over to look at the lid of the bin."
c "\"Whoa! It's got babies on its back!\""
"My body gives a violent, involuntary spasm and I shake my paws like a fucking girl."
m "\"Stop it!\""
"He glances up at me with that stupid smile still on his face."
c "\"Wow, that was gay. But seriously, it's got a bunch of tiny babies on its back. I think it's a wolf spider?\""
"I swear I'm gonna pass the hell out if he doesn't stop talking."
"I cover my face."
m "\"{i}Pleeeeaase{/i}.\""
c "\"Alright, alright. I didn't know you were that scared of 'em. You should probably get that checked out.\""
"Considering that I'd almost crashed my car into the garage of my parents' house when a spider crawled out of the AC, he was probably right."
m "\"Just kill it.\""
c "\"Why would I do that?\""
"I watch as he tilts the bin sideways."
c "\"It's not gonna hurt anyone.\""
"I want to tell him that those babies are only going to grow into a hundred more giant wolf spiders."
"But I realize I'll just come off as a bloodthirsty asshole, so I bite my lip as I watch the black spot skitter off into the darkness."
"I walk back towards Carl, hugging my shoulders as I try to control the chills running through me."
"Now I'm gonna be paranoid the whole time that it's gonna come back out to get me."
"Carl rubs my back when I stand next to him."
c "\"You know, they actually clean up a lot of other bugs that get into the house.\""
m "\"Yeeah, well, I'd rather be covered in ants than spiders.\""
"It's clear he's trying not to laugh at me as he starts popping the lid off his bin."
"On the top are a few framed pictures, and under those are a few more cardboard boxes."
"I release the latches on the other bin, keeping my eye out for any black spots that might jump out at me."
"This one is filled with bundles wrapped in cloth or paper."
"Carl drags his bin to the steps so that he can sit on them, and I follow suit."
c "\"So how do you think you'll use this stuff?\""
m "\"Um...\""
"I unwrap a smaller bundle and look at the gold pocket watch underneath."
m "\"Wow. Uh, well, not totally sure. Depends on what we find. Might film a few things.\""
stop loop fadeout 5.0
play sound "mitt.ogg" fadein 10.0
"There's a paper tag attached to the chain with \"Robert Hendricks\" written on it."
m "\"Who's this?\""
"Carl gives it a glance."
c "\"No idea. Probably a great uncle, or something.\""
"I wrap the pocket watch and reach back into the bin to pull out the next item."
"There's something really cool about old stuff. My mind wanders to who might have made it, who bought it, and how much shit it must have seen."
"History was my first choice to major in, but Dad put a stop to that pretty quick..."
"I pull out various other things: dolls, a pipe, coins, and another pocket watch."
m "\"I feel like this is worth a lot of money. Why don't they sell it?\""
c "\"Probably, but it's family stuff, and I still think they wanna do the museum.\""
"He gives an awkward cough."
c "\"'Sides, we already got plenty of money.\""
"He's got the binder open, looking at black and white photos behind the plastic."
c "\"Hey, this is him, right?\""
"He points at a picture of a very dignified-looking ram, thumbs in his vest, wearing one of those big top hats. A fox stands next to him in a similar pose."
"I can see a piece of yellowed paper set behind the photo and tug it out."
m "\"James Hendricks. Yep, definitely him. And John Begay...huh.\""
"That's Jenna's last name."
stop sound fadeout 10.0
play loop "floodlight.ogg" fadein 5.0
show Carl Neutral with dis
"Carl's phone starts buzzing and he grunts as he leans back to pull it out of his pocket."
c "\"Hey Mom...helping Chase with his project.\""
c "\"No, I—of course not.\""
"I look over at him, but he gets up and clops back up the steps."
hide Carl with dissolve
#!! Correct either way I think
"Looking back down at the picture I wonder if it's just a coincidence, but I don't think so."
"Jenna's family has been in Echo since the beginning, too, so this guy definitely has to be a relative of some kind."
play sound "camera.ogg"
"I take a picture of the photograph with my phone. I'll show it to Jenna later and ask if she knows anything about it."
c "\"—to do that without a car!?\""
"Carl raises his voice so I look back up the steps, wondering if I should close the door. Hearing him angry like that didn't feel right."
"His parents were always hard on him, but I guess they had their reasons."
"I spend the next twenty minutes shuffling through the bins, trying to be careful not to break anything."
"I decide I have enough and put the lids back on the bins, lining the stuff I picked out along one of the steps since I don't have anywhere else to put them."
stop loop fadeout 3.0
"By the time I head back up into the actual basement, Carl's gone."

scene bg carlsroom
with fade
"As I approach Carl's room I smell it before I even open the door."
"He's reclined on his bed, an arm thrown over his face, the big window above him open."
"Clothes are scattered all over the floor, along with a few empty water bottles and bowls."
"Every inch of the walls is covered in posters like I remember, along with a few on the ceiling."
"Bookcases line the opposite wall, filled to the brim with comics and toys."
"He raises up his arm as I walk in and smiles."
show Carl at center with dissolve
c "\"Sorry about the mess, dude. It's hard to keep everything clean when my parents aren't here to yell at me about it.\""
"The lazy, crackly sound in his voice has returned full force. His eyes are distant."
m "\"It's okay...Are you okay?\""
"He grins toothily."
c "\"Dude, I'm MORE than okay.\""
"Since there's nowhere else to sit I end up sitting down on the foot of his bed."
m "\"Do they...do they let you smoke in here?\""
"The smell in his room is layered and old, like the walls had been blanketed in the smell several times before."
c "\"Eeeyup. They gave up trying to stop me.\""
c "\"Better to be in the house rather than getting caught by some cop outside. They just made me promise that I wouldn't ever try something harder.\""
c "\"Heh, good thing they don't know I've already tried dick.\""
"He puts a lot of emphasis on the 'K' as the bad joke seems to just dribble out his muzzle."
m "\"Hmm.\""
"I lean back on the bed, and that's when I notice his flat screen (just a 48-inch) is on, a list of video files displayed on it."
m "\"What'cha watching?\""
c "\"Hmm? Oh!\""
"Carl grunts as he sits up and reaches for a game controller."
c "\"Our old home movies. Was gonna show you some of 'em.\""
c "\"How about...a birthday?\""
m "\"Sure.\""
"He scrolls down the list, then stops when \"Carl's 8th\" is highlighted and presses play."
hide Carl with dissolve
play music "carefree.ogg" fadein 10.0
"The backyard I was in an hour earlier pops up on the screen."
"Now a long table sits in the middle of the lawn, along with a massive bounce house."
"And not just any bounce house, but a giant, two-story one you'd find at the state fair."
"The video is timestamped Apr. 19, 2002."
m "\"Fuck, I remember this.\""
"There are about twenty kids, mostly in the bounce house and most of whom I've forgotten."
"Right now, though, the camera's zooming in on an eight-year-old Carl."
"He's messing with a giant Nerf gun, the kind that no kid ever gets because they're so damn expensive."
"And that's when eight-year-old me enters the picture, holding a much smaller Nerf gun."
"His parents gave everyone a goodie bag that day. It had toys in it that I might not have been able to get on my own birthday."
"My kid self puts the gun to Carl's head and pulls the trigger, the dart bouncing off one of his horns."
"I specifically remember that moment. I had thought the suction end of the dart was going to stick, but of course it didn't."
"The audio is filled with a deep chuckle; Carl's dad behind the camera."
c "\"You were a dick back then.\""
m "\"What? I was eight!\""
c "\"Still, you blew out my candles.\""
m "\"Oh yeah...\""
"He got so mad about that."
"I start to settle back and smile."
"It's been a long time since I've watched a home movie, and I've forgotten how nice it is to have this method of looking back."
"Kind of like when I get stuck on scrolling through all the old images on my phone."
"My younger self is trying to help Carl with the gun, lifting up the barrel and looking into the opening."
"Jim" "\"Careful!\""
"Kid Chase pulls his head back with a jolt as Carl's dad yells, then mutters behind the camera."
"Jim" "\"Let's see how long it takes him to trick Carl into trading with him.\""
"Carl's dad sounds exasperated, but good-natured."
"It still makes me blush a bit, now knowing how aware Jim was of my taking advantage of his son."
"Our struggles with the Nerf gun get the attention of another kid, though."
"My breath catches in my throat as Sydney bounces into frame."
stop music fadeout 5.0
"I can feel Carl tensing up next to me, too, and he starts to lean for the game controller."
"Jim" "\"And here comes the Mormon boy.\""
"The disgust in Carl's dad's voice shocks me and I hear Carl whisper a curse next to me as he fumbles for the controller."
"Sydney reaches out and pulls the gun away from Carl as he looks it over, grinning."
"Jim" "\"HEY!\""
"Suddenly, the screen switches back to the file menu and we both sit there in silence for a few seconds."
show Carl Sad at center with dissolve
c "\"Sorry, I—I guess I forgot that...\""
"Of course Sydney was going to be at that party, but I'd honestly forgotten, too."
"If there was any way to perfectly ruin the mood, that had been it."
"I glance over at Carl and see him looking down at the game pad, ears lowered, the insides red."
m "\"Hey, it's okay. I mean, maybe it's a good thing to watch—\""
c "\"My dad, I didn't know he'd say that. I'd rather not find out what else he's said.\""
m "\"Oh, yeah...\""
"I look around, trying to find something, anything to distract us from what just happened."
"My eyes fall on the shelves holding Carl's game library."
m "\"...Wanna play a game?\""

scene bg carlsroom with fade
play music "comeover.ogg"
"It's just like old times as we co-op through Winter Castle."
"The fact that he still has the old save files from when he was in college makes it all the more nostalgic."
"I get so into it that it gets dark outside without me even knowing, and pretty soon I'm looking out at the purple sky reluctantly."
m "\"About time I go back.\""
"Carl sighs and pauses the game before stretching and dropping the controller onto his bed."
show Carl Rejected at center with dissolve
c "\"Aww, come on. Sure you can't stick around?\""
m "\"I dunno. I don't have any clothes, or toothbrush...\""
c "\"We can walk over and get them.\""
"Carl seems pretty determined to make me stay, and there's not one reason why I can't, so I relent."
m "\"Alright...Yeah, this could be fun.\""
show Carl with dis
c "\"Yes!\""
"Carl looks happy and almost relieved."
c "\"It'll be just like old times!\""
"He rolls to his hooves."
c "\"And speaking of old times, let's make a pizza!\""
"I've suddenly caught Carl's enthusiasm."
scene bg kitchen with dissolve
"We go into the massive kitchen and pull a big frozen pizza from the fridge and, while it bakes, we sit at the counter and talk."
"At this point the haze of pot has lifted from Carl's face and he's animated and excited again, swiveling on one of the counter stools."
"For the first time in almost ten years, I'm giddy and excited in the way you only get when you're at a sleepover."
"That makes it a little jarring when he pulls out some beers, but I'm happy to have a few and we guzzle them down as we talk about past sleepovers."
"Pretty soon our reminiscing drifts into the present and that's when the conversation slows a bit, Carl having less to say."
"I try to change the subject and tell him that he should come back to school."
"He just smiles and shakes his head."
stop music fadeout 3.0

scene bg carlsroomnight
show nightoverlay
with transition_fade
"Three hours later, we're both laying back on Carl's bed, head to toe, having just watched a shitty action movie."
"We didn't end up going out to get my stuff, so I'm just in my boxers, pleasantly drowsy and buzzed."
"I hear Carl snuffle and look down my chest at him."
m "\"What's up?\""
"He looks over at me and shrugs."
show Carlu Neutral behind nightoverlay at center with dissolve
c "\"Nothin', just thinkin'.\""
m "\"What about?\""
play music "intimate.ogg" fadein 15.0
"During our past sleepovers Carl had always been afraid to be the last to fall asleep."
"He'd try to keep me up by talking, rolling over on top of me...and sometimes by just throwing shit at me."
"I wonder if that's what he's doing now."
c "\"I dunno...life?\""
m "\"That's a lot to think about.\""
c "\"Not for me, heh.\""
"I look over at him again."
"He's holding one paw up, looking through his fingers at the ceiling fan."
m "\"You're just figuring things out.\""
show Carlu Rejected behind nightoverlay with dis
"Carl lets his arm flop back down over his head, blowing out a sigh."
c "\"I'm not figuring things out, man.\""
"I don't say anything. It's cool that he's reaching out to me, but I'm not sure I can offer any advice that he hasn't heard before."
c "\"I just...I just wish I could be doing something.\""
"I think for a moment."
m "\"You've done a lot more than some people I know.\""
m "\"I mean, your art is great, you did go to school even if you dropped out, and you were working while you could.\""
m "\"There are a lot of people out there who can't even say that.\""
"Carl laughs, but it's a sad kind of laugh."
c "\"Try saying that to my mom. She's always got something to do, always WANTS to do something.\""
c "\"I just...I just don't feel that.\""
show Carlu Depressed behind nightoverlay with dis
"He turns his head towards me."
c "\"I {i}wish{/i} I did, Chase, but I just {i}can't{/i}.\""
"His voice catches in his throat, and I shrink a bit into the bed and pretend not to notice."
"The beer we've had is definitely partly to blame for this."
"He turns his head towards the wall, though, and I'm guiltily relieved that when he talks again his voice is under control."
c "\"I just wish it wasn't such a goddamn chore for me to just go outside, ya know?\""
#!! didn't -> don't? not sure
"I don't know, but I nod anyway, even if he can't see."
"He's waiting for me to say something, though, so I clear my throat."
menu:
    "You have a problem.":
        $ Ask_About_Carl = True
        m "\"Don't take this the wrong way, but maybe you should see a therapist?\""
        show Carlu Annoyed behind nightoverlay with dis
        "He snorts and finally turns his head to look back at me, his horns bumping the wall loudly."
        c "\"Ha! I already do. I thought they'd just give me a pill to make things better, but apparently I have to actually make an effort, too.\""
        show Carlu with dis
        c "\"And I'm like, isn't that why I'm seeing you, for the whole 'making an effort' thing?\""
        "I laugh along with him."
        m "\"Yeah, I can remember what that's like.\""
    "It's fine.":
        m "\"You know, Carl, some people are just like that.\""
        show Carlu Neutral behind nightoverlay with dis
        "He looks down at me, but doesn't say anything."
        m "\"If it's so hard to get out, then just don't.\""
        m "\"People figure things out, eventually. And if you always just want to stay home then do that.\""
        m "\"Just, uh, try to figure out a way to sustain yourself. That's pretty much the gist of what my therapist told me; do what makes you happy.\""
show Carlu Rejected behind nightoverlay with dis
"He watches me for a few seconds."
c "\"So is all that.. are all those problems you had taken care of now?\""
m "\"I hope so.\""
"We lay in silence for a little while, before I finally speak up."
m "\"Listen, I'll probably come back a few times this week to work with that history stuff.\""
m "\"Well, why don't we go out and {i}do{/i} something?\""
show Carlu Neutral behind nightoverlay with dis
c "\"That would be nice...\""
"I grin, glad at making Carl feel better."
m "\"Cool, let's plan on it.\""
show Carlu Sheepish with dis
"Carl puts his paws behind his head and smiles."
c "\"It's cool that you're here, Chase.\""
m "\"It's cool to be here, Carl.\""
stop music fadeout 5.0
c "\"And not just because it's nice to have someone to talk to.\""
m "\"Oh?\""
show Carlu Rejected behind nightoverlay with dis
c "\"No. This house is fucking haunted.\""

scene bg black
with transition_fade
$ renpy.pause(2.0, hard=True)
scene bg carlsroomnight
show nightoverlay
with dissolve
#!!!! These scrapes are basically inaudible unless the volume is cranked all the way up
play sound "scrape.ogg"
"I don't remember falling asleep, but it's at that moment that something wakes me up."
"I jolt, then lay there, trying to remember where I am."
"Carl's house, that's right."
"I stare at the ceiling, wondering what time it is."
"I don't bother to look my phone, though, because I'm already starting to fall back asleep."
play sound "scrape.ogg" fadeout 2.0
"A scraping noise from beneath me makes me jump and I prop myself up on my elbows, listening."
"Looking over, I see Carl's staring at the ceiling, eyes wide."
m "\"Carl?\""
"I whisper it, and I'm not sure why."
"He jumps, then looks at me, confused, like he'd just woken up."
show Carlu Surprised behind nightoverlay with dissolve
c "\"Huh?\""
m "\"Are you okay?\""
c "\"Yeah, what's wrong?\""
m "\"I—I think I hear something.\""
"His floppy ears perk up."
c "\"I don't—\""
"Then his eyes widen."
"Although I didn't hear anything right then, he definitely did."
m "\"You hear it?\""
c "\"Yeah, like a scraping noise I told you about?\""
m "\"Yeah!\""
show Carlu behind nightoverlay with dis
"He looks happy."
c "\"Ha! So I'm not fucking crazy!\""
"We both sit there and listen for a while, but it sounds like it stopped."
c "\"Wanna go see what—\""
show Carlu Surprised behind nightoverlay with dis
"Suddenly, his eyes widen and his muzzle drops open in shock."
"I stare back."
m "\"What!?\""
c "\"Did you fucking hear that!?\""
"I listen, feeling my heartbeat pick up now that Carl looks fucking terrified...but I don't hear anything."
m "\"What!?\""
play music "creep.ogg" fadein 3.0
c "\"A fucking voice!\""
"The fur raises up all over my body as I listen."
"But nothing. Carl definitely seems convinced, though, so I listen harder."
"I just start to make out what might be a voice when Carl sits up next to me and gets out of bed."
"I feel myself start to panic. Did some crazy hobo break into the house?"
show Carlu Neutral with dis
"Carl gets off the couch."
c "\"Come on.\""
m "\"What? What the fuck are we gonna do!? Let's call the cops!\""
c "\"No, let's make sure, first. This has happened before.\""
m "\"What? What do you mean?\""
"He puts a finger up to his lips."
c "\"Grab something.\""
m "\"What?\""
scene bg kitchennight with dissolve
"I follow Carl out into the kitchen and he starts rummaging through the drawers."
"I follow him, hugging my shoulders, feeling a lot colder right now."
"With the sound of metal sliding against metal Carl pulls out a giant steak knife."
m "\"What. The. Fuck!?\""
c "\"Dude, I've been hearing this shit for the past month and I've been too scared to go down there, but now with you here—\""
"He flashes me a smile."
c "\"I'm gonna find out what the fuck this is.\""
c "\"Here.\""
"He reaches into a spot between the fridge and the wall and pulls out a broom before sticking it out to me."
"I take it slowly."
m "\"What the hell am I supposed to do with this?\""
c "\"Hit him. Come on!\""
"Carl starts down the stairs and I follow behind, holding the broomstick in front of me like a sword."
"I've never had to hit anyone with a stick before. I have no idea what I'm doing."
scene bg basement with dissolve
stop music fadeout 5.0
"Once we get to the small door leading down to the crawl space, Carl pauses and we both listen."
"It's silent for a while, then—"
play sound "scrape2.ogg"
"..."
m "\"Shit!\""
"Carl looks at me like I'm crazy, not reacting to the noise at all."
c "\"Shh!\""
"He leans down, a paw on the handle."
"Looking back at me, he signals me with his eyes to be ready."
"I grip onto the broom like a lifeline as I wait for him to swing the door open and, when he does—"
scene bg black
show nightoverlay
with dissolve
"..."
"Darkness."
show Carlu Surprised behind nightoverlay at center with dissolve
c "\"Shit.\""
"So whatever's down here is just slinking around in complete darkness?"
c "\"H-hey!\""
"Carl says it unconvincingly, the fear clear in his voice."
show Carlu Neutral behind nightoverlay with dis
"Then, after looking back at me-"
c "\"Fuck it.\""
hide Carlu with dissolve
"He jumps down into the crawl space, disappearing into the dark."
m "\"Carl!\""
"I stumble up to the edge of the steps, trying to squint into the black."
"I hear Carl to the right, rustling around and cursing."
play sound "switch.ogg"
play loop "floodlight.ogg" fadein 3.0
scene bg crawlspace
"That's when light floods the crawl space."
"I quickly wobble down the steps, knowing that if whatever is down here is gonna try to escape, it would be running right into me."
"Finally, I have a moment to catch my breath, standing several feet behind Carl as I look around, broom at the ready."
c "\"There's nothing here...what the fuck?\""
"Sure enough, the crawl space looks empty. There aren't many places to hide, either."
m "\"What the hell's going on, Carl?\""
"But he doesn't answer me. He's staring at the bins."
c "\"Did you put the bins back?\""
"I look down, and the bins are gone."
"I look back at where they were originally, and sure enough, they're neatly stacked right where we found them."
m "\"I—\""
"I honestly don't remember. Did I move them back? Maybe, it would be something I might do. I try, but I just can't remember."
m "\"Maybe...\""
c "\"Dude, come on.\""
m "\"I really don't remember!\""
"Carl walks further towards the back, ears perked, looking left and right as he clutches his knife."
"I start to follow, but that's when I notice something at the left of my vision, on the ground."
"Looking down, I see something fat and hairy ambling slowly over the tarp."
"A giant fucking tarantula."
"The following few moments are a blur, but the next thing I know I'm going up the stairs on my feet and paws, grabbing at the door frame to pull myself up."
scene bg basement with dissolve
c "\"Chase, what happened!?\""
show Carlu Surprised at center with dissolve
"I can hear him running up behind me, so I turn to warn him."
m "\"L—look out. A big-a big spider!\""
"The breath keeps catching in my throat. I think I'm hyperventilating."
"I'm still clutching at the door frame as Carl follows up behind me, his eyes wide."
c "\"Wha-come on Chase, this is crazy.\""
#! Spelled "blonde" everywhere else
m "\"No, huge—a blonde!\""
c "\"No fucking way!\""
"Now he looks excited and he turns back to the crawl space."
"I feel numb right now. This is all too much to handle. What the fuck is even going on?"
c "\"Which way!?\""
"Shakily, I point towards where the spider was crawling."
"Carl squints, then walks down the steps, looking around."
hide Carlu with dissolve
m "\"Careful!\""
c "\"If it was really a blonde there's not much to worry about. I hear they're actually pretty gentle.\""
"I gulp and don't say anything."
"My head is pounding and buzzing which, for some reason, doesn't exactly feel like it has anything to do with the adrenaline rush."
"It's more like a bad headache."
"Carl looks around a while longer while I focus on the steps, making sure nothing starts crawling up them."
"I don't even care about the possible hobo anymore."
show Carlu Rejected with dissolve
"Finally, Carl comes back, looking confused."
c "\"Well, there's nothing there. You know, sometimes I see shit when I'm really tired. Wanna go back upstairs?\""
"There's nothing there."
"This can't be happening again..."

window hide
stop music fadeout 6.0
stop loop fadeout 6.0

jump carlwednesday