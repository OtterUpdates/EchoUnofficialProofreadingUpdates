# Unofficial Proofreading Updates for Echo - Route 65, Echo, and Arches
I did a re-read of Route 65, Echo, and Arches, and I decided to proofread them at the same time. The TL;DR is that I think ~98-99% of the issues in these novels are fixed by my edits here, and hopefully 100% of the noticeable ones. It's hard to say how many individual fixes I actually performed, but going by a git diff line count:

| Novel           	| Line Changes 	| Notes Added 	|
|-----------------	|--------------	|-------------	|
| Echo - Route 65 	| ~380         	| ~50         	|
| Echo            	| ~2,900        	| ~700        	|
| Arches          	| ~300         	| ~190        	|

To be clear, before I started I didn't know it was going to be this bad! I guess during my first read of Echo I turned off my brain in order to get through the grammar, and I didn't realize how many errors I was skimming past. I generally proofread and submit corrections for any ebooks I read, but the worst case I'd had before this was about ~200 corrections in a 500k word book, so this was a new level of magnitude for me. My primary motivation was simply to do a second read of Echo, but at the same time I also wanted to clean up all the glaring typos so that I could recommend this talking animal book to my friends and have them take it seriously.

I did reach out to the Echo Project team a few times via their Patreon messages and the email they have posted, but I haven't received any response after waiting a couple months. I'm not sure what sort of contact methods they actually pay attention to, so if anyone knows how to put this on their radar be my guest; I refuse to make a Twitter account to reach them that way. In the meantime, I'm just releasing this here so people who might be interested have access to it.

I would very strongly recommend applying this patch to Route 65 and Echo, but the fixes I needed to make for Arches were a lot lighter in scope and not as urgent. Still, there's a good amount of hard errors, messy sentences, and bad formatting that I cleaned up in Arches, so it's ultimately a good idea there too.

If you want to compare my fixes to the original text, you'll want to use some kind of text diff tool (I personally use VSCode), or check the diffs [directly on GitHub](https://github.com/OtterUpdates/EchoUnofficialProofreadingUpdates/compare/original-copies...main?w=1). Note that these fixes obviously contain spoilers, so don't look if you haven't read the novels yet!

## Installation/Usage notes:
Grab the source code zip from the [latest release](https://github.com/OtterUpdates/EchoUnofficialProofreadingUpdates/releases/latest) and extract the relevant `.rpy` files into the nested `game` folder of Route 65, Echo, or Arches (i.e., `Echo\game\*.rpy`), then relaunch the game.

## List of things I remember doing:
* Most (all? hard to say for sure with a story like Echo) plot/detail inconsistencies either fixed or noted. Often an inconsistency would require a larger rework to fix, but there are still a lot that can be objectively fixed without consultation, e.g. Chase referring to his roommate as a "rabbit", Leo's van constantly being misremembered as a "truck", and Clint's ever-changing species
* Fixed tons of misspellings, malapropisms, and general "hard grammar" mistakes, e.g. "any more/anymore", "then/than", "it's/its"
* So many missing/dropped/extra words. I think I fixed 98%+ of these, but it's really impossible to know for sure since your brain automatically fills in the gaps unless you read aloud/read twice.
* Tons of formatting errors, e.g. missing quotation marks, incorrect punctuation, missing punctuation, missing font styles etc.
* General word consistency. If a word or phrase is spelled/compounded/represented in a certain way, it should be the "right" way, and all instances of it should match. I did this with most important/noticeable things, but there's likely a few desyncs from things only mentioned ~2 times that I didn't pick up on
* Readability improvements or at least notes where the writing is noticeably clunky or repetitive, e.g. writing "finally" 3 times in one sentence
* All the bad music loops were fixed, aside from Cam's guitar tuning loop in Arches (which doesn't really have a good fix due to reasons). Basically, there were certain sections where going backwards one dialogue step would permanently cut the currently-playing music off. All of these sections were during super important moments, so it was very likely that those scenes would be ruined for an average reader.
* A handful of bugs/quirks in the programming fixed, e.g. backgrounds displaying at the wrong times and unintentional pauses between dialogue boxes.
* You can actually fuckin' read the Route 65 intro quote now! I just made the quote screens wait until you click before advancing. I swear, no one in the world can read that quote before it fades away.
* Added a ton of commas where they're noticeably absent for readability. Not even close to making every sentence perfectly grammatically correct, since realistically you'd want to fully restructure hopeless sentences instead of throwing commas at them. I let probably ~80% of the comma "errors" slide if they had a sufficient reading flow, and since Echo is told through very casual speech patterns it's easy enough to ignore "perfect grammar" as a reader. If this was my own writing I'd probably spend a lot more time smoothing things out, but in this case I didn't want to hand the original authors 15k lines of nitpicks. My standards for what commas I wanted to fix changed throughout my reading, so Route 65, Echo's intro, Carl, and Leo probably have different comma allowances than later routes and Arches. Later routes were also MUCH better written to begin with. I generally also let missing semicolons/colons/emdashes slide if they were instead represented with commas. The end result is that the text is nowhere near book quality, but you shouldn't be stumbling over sentence structures or reading flow once you get into the groove.
* Loads and loads of manual notes next to sentences. I used them when I wasn't fully confident of a fix, when a line needed more comprehensive restructuring, or when something needed authoritative input (i.e., the authors, in theory). All my notes start with "#!" and a varying amount of "!"s, e.g. "#!!!!" is more important than "#!!!".
* Generally, the "content" of Route 65, Echo, and Arches is unchanged. Aside from some opportune fixes for inconsistencies, all sentences more or less have the same words as before, just in a more correct and pleasant format.

## Afterword/reporting issues

There are still a few noticeable problems/detail inconsistencies left in the text, but they should all at least have a note next to them. I'd say this work is a pretty solid base for what I'd consider a 1.0 of Route 65/Echo. It's not perfect, but it's a massive first step that should be supplemented by further fine-tuning.

Ideally this new text would have a few test readers and some peer review on all the changes, but this is all I can do with a single read by myself. If you use this text to do a re-read, I would really appreciate it if you send me notes on anything that's still not quite right! You can do so by opening an [issue](https://github.com/OtterUpdates/EchoUnofficialProofreadingUpdates/issues) or using the [discussions section](https://github.com/OtterUpdates/EchoUnofficialProofreadingUpdates/discussions) on this repo. You don't need to worry about putting the corrections in a specific format or anything. Pull Requests are also welcome, if you know how to do that.

I also included some [general notes](/notes-and-regex.md) in this repo for corrections I didn't get around to doing, as well as a big chunk of RegEx patterns that I used to programmatically find issues before reading.