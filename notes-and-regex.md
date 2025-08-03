# TOOLS USED

* VSCode
* https://marketplace.visualstudio.com/items?itemName=LuqueDaniel.languague-renpy
* https://pypi.org/project/renspell/
* Google Trends
  * Shows what real people are searching for
  * Useful for determining what "most people" think a word variant should be
  * Note that "most people" are not hyper-literate sources
  * https://trends.google.com/trends/explore?q=street%20lamp,streetlamp,street-lamp
* Google Ngram search
  * Shows number of occurrences of words or phrases over time, scanned in from books
  * This is just an unintelligent tool that counts words, and it's not even a very accurate one: https://en.wikipedia.org/wiki/Google_Books_Ngram_Viewer#Limitations
  * Be most careful when using this with multi-word phrases that aren't hyphenated, as it's not smart enough to know if each word in your phrase is used as a "single unit" in the text it scanned it from
  * It can also overrepresent word variants if that spelling has multiple definitions
  * https://books.google.com/ngrams/graph?content=street+lamp%2C+street-lamp%2C+streetlamp&year_start=1800&year_end=2022&corpus=en&smoothing=3


# VSCODE SEARCH SETTINGS

* NOT case sensitive, for ease of use
* Enable RegEx search
* include `*.rpy`
* exclude `00*.rpy, 01*.rpy, script.rpy, kinetic_text_tags.rpy, colorstest.rpy, gallery.rpy, extras.rpy, gui.rpy, phone.rpy, colorstest.rpy, screens.rpy, options.rpy, readback.rpy, music_room.rpy, extra.rpy, snowblossom.rpy, endingcreditsnew.rpy,animation.rpy, SideStoryPlugin.rpy`

# MISC ISSUES

* The mass copy-pasting to "split" routes means that there are small differences between them that are not intentional.
  * Recommend putting the splits side by side and comparing in a text-diff tool to pick the intended variations on a line-by-line basis
* endashes/emdashes
  * Replaced many endashes with emdashes, and a few with hyphens
  * I generally didn't try to change hyphens and emdashes to their proper formats
    * Echo's font makes emdashes look pretty obnoxious, so that also gives me pause on "correcting" them
  * Hyphen `-`, En Dash `–`, Em Dash `—`
  * The font used by Arches can't display emdashes, which is not great for accuracy. I assume this is why Arches uses double hyphens sometimes
  * Hyphens are used for short/fast stuttering, this regex finds potential stutters with emdashes - `([\w']+)—\1`
  * This regex finds hyphens at the end of dialogue, which should maybe be an emdash `-("|\\")`
  * Use emdashes instead of hyphens for breaks in a line (high hit-rate) `- [^-]+ -`
  * Use emdashes instead of hyphens for breaks in a line (comprehensive) `-[^-]+-`
  * Use emdashes instead of hyphens for asides at the end of a line ` - [^-]+$`
  * Jenna's route goes nuts with emdashes during certain sections, and I'm fairly sure they're not all used correctly. Probably not something that can be fixed at this point.
* When using fonts, the line will often have mismatched quotation mark stylings since the font starts after the first quotation mark and is often not terminated before the closing quotation mark
  * e.g. `"{font}An example sentence"`
  * In this case, the first quotation mark would appear in standard font style and the second would appear in custom font style
  * search for fonts used after opening quote: `\\".*\{font`
  * (NOT DONE, too many occurrences and I would want an official go-ahead before pulling the trigger. This is also not very noticeable to an average reader unless you are looking for it. These are objective upgrades though, so they should be done at some point.)

# CONSISTENCY

## Slang

* A'ight/aight
  * pick one, and consider "s'aight" as well `[^a-z]a'?ight`
  * (done, normalized to `a'ight`)
* til/till/til'
  * pick one, with or without apostrophe `[^a-z]till?'?[^a-z]`
  * (done, normalized to `'til`)
* whatsup/what's up
  * Can keep this separate if desired, just checking `what'?s ?up`
  * (done, normalized to `what's up`)
* woah/whoa/whoah
  * pick one, probably whoa `wh?oah?`
  * (done, normalized to `whoa`)
* musta/musta'
  * pick one, with or without apostrophe at end `musta`
  * (NOT DONE. Echo uses `musta`, Arches uses `musta'`)
* getcha/get'cha
  * pick one `get'?cha`
  * (done, normalized to `get'cha`)
* what'cha/watcha/wat'cha/whatcha/wath'cha
  * pick one variant `wh?at?h?'?t?ch?a`
  * (done, normalized to `what'cha`)
* shut up/shutup
  * pick one `shut(-| )?up`
  * (done, normalized to `shut up`)
* friggen/friggen'/friggin/friggin'
  * pick one, with or without apostrophe at end `frigg(i|e)n`
  * (done, normalized to `friggen'`)
* whaddya/whaddaya
  * pick one, probably whaddya `whadda?ya`
  * (done, normalized to `whaddya`)
* lil/lil'
  * pick one `lil[^a-z]`
  * (done, normalized to `lil'`)
* 'cause/cause/cuz/'cuz
  * pick one style
  * "cuz" can be separate from "cause" if it makes more sense for the character `([^a-z]cause[^sd]|cuz[^n])`
  * (done, normalized to `'cause` and `'cuz`)

## Locale

* gray/grey
  * probably gray, as that's the American spelling `gr(a|e)y`
  * (done, normalized to `gray`)
* afterward/afterwards
  * pick whichever `afterwards?`
  * (done, normalized to `afterwards`. IIRC it's because almost all of them were already `afterwards`, but this is the british variant so maybe switch to `afterward`)
* toward/towards
  * probably toward, as that's the American spelling `towards?`
  * (NOT DONE, there's a lot of occurrences - 231 "towards", 484 "toward")
* acknowledgment/acknowledgement
  * probably acknowledgment, that's the American spelling `acknowledge?ment`
  * (done, normalized to `acknowledgment`)
* disoriented/disorientated, disorienting/disorientating
  * probably "disoriented", that's the American spelling `disorient`
  * (done, normalized to `disoriented`/`disorienting`)
* judgment/judgement
  * most commonly spelled as "judgment" by far
  * (done, normalized to `judgment`)
* naive/naïve
  * pick one `na(ï|i)ve`
  * (done, normalized to `naive`, as most sources say to drop the dieresis as legacy)
* futbol/fútbol/futball
  * pick one. Also consider that spelling may be different when it's represented in "text message speak" in Flynn's route `f.tb`
  * (done, normalized to `fútbol`, and keeping `futball` in Leo's text message)
* facade/façade
  * pick one `fa.ade`
  * (done, normalized to `facade`, as that's the more casual modern spelling, but it could also switch to the cedilla as long as it's consistent. My main issue with the cedilla is it's very attention-grabbing)
* deja vu/déjà vu
  * pick one `d.j. vu`
  * (done, normalized to `déjà vu`, as that's the only real "accepted" modern spelling, though obviously in casual use most people do not include them. Arches used `déjà vu` and Echo mostly used `deja vu`. As before, using the diacritics is a little attention-grabbing so that may be a reason to drop them)
* cliche/cliché
  * pick one `clich.`
  * (done, normalized to `cliché`. This seems like a fairly straightforward one as it's uncommon to use `cliche`)

## Misc

* chesire/cheshire
  * Technically not a word, but I assume this refers to the Cheshire cat from Alice in Wonderland. pick one variant between Route 65 and Echo `chesh?ire`
  * (done, normalized to `cheshire`)
* Lucha Lobo/Luche Lobo
  * Is there a difference? pick one probably? `luch(a|e)[^d]`
  * (done, normalized to `lucha`. I'm not a Spanish speaker, but according to several Spanish/Mexican sources it should be "Lucha". If there's a specific reason for it to be Luche in some cases it should be set back in those cases, but until that's evident it's a very obvious desync for readers (at least for non-Spanish readers who don't understand the nuance of why the letter keeps flipping around))
* Super Wolf/SuperWolf
  * probably SuperWolf `super.?wolf`
  * (done, normalized to `SuperWolf`)
* Southwest/Southwestern Adventures
  * pick a spelling, probably Southwest Adventures `Southwest(ern)? Adventures`
  * (done, normalized to `Southwest Adventures`, since that's the most common and the first references to it use that name)
* Paw Pad, Foot Pad, Finger Pad, Thumb Pad, Knuckle Fur, Head Fur
  * These should probably all be a similar style?
  * `(paw|foot|feet|finger|thumb).?pad`
  * `(knuckle|head).?fur`
  * (NOT DONE. The references are too varied and these aren't real words, so unsure which way to go. This one is fairly noticeable once you start seeing it so higher priority on normalizing it.)
* wolfboy/wolf boy/wolf-boy/wolfy-boy
  * Probably pick one of these, or at least condense "wolfboy/wolf-boy/wolf boy" into one variant and separate wolfy-boy `wolfy?-? ?boy[^f]`
  * (NOT DONE. too opinionated, and these could be stressed in different ways. The differences are noticeable as a reader though.)
* speciest/speciesist
  * pick one `species(is)?t`
  * (done, normalized to `speciesist`, as it's an actual word)
* smush/smoosh
  * pick one `sm(u|oo)sh`
  * (done, normalized to `smush`, but either variant is equally okay. Smush seems to be an American bastardization of smoosh, but we are using American locale so.)
* Otter/otter
  * Generally when people refer to Chase as if his name is "Otter", it should be capitalized (mainly done by Leo)
  * `[^a-z]otter[^a-z]` (use case sensitivity)
  * (NOT DONE. It's kind of difficult to pick out when it's being used as a proper name and when it's being used as a derogatory label (is there a difference w/r/t capitalization?). This should definitely be looked into though, since the capitalization of Otter is fairly noticeable, and then noticeable when it's absent)
* Leo's Spanish words
  * they're often italicized; should it be a rule to always italicize them?
  * A few I remember: garrobo, `p(u)+chica`, esta yuca, chula, estupido, loco por ti, nutria, puta, madre, ay-yai, huevos, gringo, padres, buenos dias
  * (NOT DONE, this is just a matter of opinion and style)
* Town hall/city hall capitalization
  * town hall/city hall or Town Hall/City Hall? should be somewhat consistent
  * (NOT DONE, this is kind of a mess and opinionated)
* Tupperware/tupperware
  * pick a capitalization
  * (done, normalized to `tupperware` since it's less distracting and they've basically lost their "trademark" at this point anyway)
* spaz/spazz
  * pick one `spaz`
  * (done, normalized to `spazz`, though both spellings are used. Worth noting this is a slur)
* scaley/scaly
  * pick one `scal.?y`
  * (done, normalized to `scaly` as that's the actual word. There's also `"That's all it was. It's spring break, and he for some reason watched enough scaley porn to want me."`, which I think might use a different spelling?)
* AM/PM/A.M./P.M.
  * pick one (enable case-sensitivity) - `[^a-z](A|P)\.?M\.?[^a-z]`
  * (NOT DONE, too opinionated based on how it looks in each sentence)
* yote/'yote
  * apostrophe before or not, pick one `[^a-z]yote`
  * (done, normalized to `yote`, which is used frequently in Arches. Echo only has one reference to `'yote` so this seems like an easy sync for a non-word)
* rez/Rez and reservation/Reservation
  * pick a capitalization style `([^a-z]rez[^a-z]|[^a-z]reservation)`
  * a source on what to use: https://nativegov.org/resources/terminology-style-guide/
  * (done, normalized to `Rez`/`Reservation` for most instances, as it's almost always used in place of the name of the specific reservation. There's one reference where it's used generically, which stays lowercase)
* native/Native
  * Native should always be capitalized when referring to e.g. Indigenous people: `[^a-z]native[^a-z]`
  * be careful of other meanings of the word native, which should remain lowercase
  * source: https://nativegov.org/resources/terminology-style-guide/
  * (done, normalized to `Native` for all relevant references as above)
* county/County
  * Should county be capitalized? It's like 50/50 currently. `county`
  * (NOT DONE, no idea about this one)
* Capitalizations after colons
  * Overwhelmingly, capitalizations after colons aren't used correctly in R65/Echo/Arches, and I decapped them all for consistency
  * You can capitalize in very specific circumstances, but it really depends on what style guide and locale you follow, and it's usually still optional
  * If you truly want some of these colon capitalizations to be reverted then feel free, but put some thought into it, and consider the inconsistency for an average reader seeing only a couple of these remaining intact while the rest are lowercase
  * (done, all decapped, as above)
* What is the name of the fucking river?
  * They call it Seesaw, Yeeyaw, Yeeyah, and Yee-Yaw
  * They say that Seesaw and Yeeyaw are mispronunciations, but during Route 65 Chase again calls it Yee-Yaw:
    * "It was at the old Yee-Yaw riverway. I had just gotten my cell phone and was asking everybody to pose for a picture."
  * I have to assume the right answer is Yeeyah, but then in the code it's called yeeyaw
  * `(yee-?yaw|yee-?yah|seesaw)`
  * this keeps me up at night
  * (NOT DONE, though I strongly suspect it should be normalized to Yeeyah based on the anglicization of the original Navajo word (yíiyáh))
* How many floors in the abandoned school?
  * In R65, the school is described as a "three-story school"
  * In Echo, it's described as a "two-story brick school house with a basement", and the school's picture matches that description
  * In TJ's route, they go to room 301 as part of the scavenger hunt (as well as noting rooms 302, 303, 304, and 305), but generally the rooms in America should be Bxx, 1xx, and 2xx for a basement and 2 stories
  * Most readers will not notice this issue. I picked up on it vaguely during TJ's route when it mentioned "301" while the school's picture only showed 2 floors, but the "three-story" reference in R65 doesn't even have an accompanying picture to compare with.
  * (NOT DONE. I assume this should be normalized to basement+two stories based on the difficulty of needing another picture for a three-story school, but it was probably only described as two-story to retroactively explain the picture. Sydney's clue about "We'll have fun in 301" still rhymes with "201", so that part works either way.)
* Ellipses variation is a mess and probably unfixable at this point.
  * Is there extra meaning by double dot vs. triple dot?
  * Should there be a space after ellipses or not?
  * etc
  * (NOT DONE, as above)
* Periods after menu choices
  * It seems most common to end the menu choices with periods, so probably make that a universal rule
  * (NOT DONE, though I synchronized them on a per-menu basis if the other options were one way or the other)
* '90s/90s/90's formatting
  * generally should be written as '90s - `[^0-9][0-9]0'?s`
  * (done, all set to e.g. '90s)
* fancy `‘`and`’` apostrophe codes are nonstandard, they show up in a few sections
  * Most importantly, they're always mixed with other standard apostrophes, so they should all be changed to be uniform
  * Note that the COLONNA.ttf font needs the special apostrophe codes in order to display in the right font
  * Other fonts don't have this issue, aside from forbid.ttf (which doesn't display apostrophes ever)
  * (done, all non-standard codes removed, and during COLONNA.ttf sections all apostrophes set to non-standard)
* fancy `“`and`”` quote codes are nonstandard
  * (NOT DONE, there are 4 instances in Arches, but they are used as internal quotations within a line. Could maybe switch them to single quotes, or just use standard quotation marks)
* fake country naming inconsistencies
  * there are still "real" country names used throughout R65 and Echo
  * `Spanish`, `French`, `Latin`, `German`, `English`, `Japanese`, `Russian`, `Indian`
  * (NOT DONE)

## Compound words:

* Street Light/Street Lamp
  * pick one style for both probably `street.?(light|lamp)`
* Lamp Post
  * probably lamppost `lamp.?post`
* These two are just for reference. You can efficiently search for compound words by using the regex `firstHalf.?secondHalf`, which finds `firstHalfsecondHalf`, `firstHalf secondHalf`, and `firstHalf-secondHalf`
  * For many other compound words I picked a variant pre-emptively
  * If the variant I chose is not the one that's wanted, it should be trivial to switch them all to the desired variant instead since they all match

## Possessive s's

Preference, but should be consistent. I prefer s's over s', with the rationale "read it the same as it's spoken"

* James'/James's `James'`
* Hendricks'/Hendricks's `Hendricks'`
* bus'/bus's `bus'`
* boss'/boss's `boss'`
* us'/us's `[^pb']us'`
* campus'/campus's `campus'`
* Princess'/Princess's `princess'`
* (done for all mentioned above, normalized to `s's`. Note that plural possessives stay as `s'`, e.g. `parents'`)

# ROUTE SPECIFIC

## ROUTE 65

* Unmarked dialogue sections - room for improvement:
  * `\"Chase,\" he rumbles.` -> Jasmynn's dad speaking but not using normal white text; maybe make a character identifier for them? non-dialogue is attached so may need tweaking?
  * `\"Fuck off, Chase!\" His voice is laden with derisive contempt.` -> Jeremy, with non-dialogue attached
  * `\"She’s in her room. Got chores she ain’t done yet so she can’t go out and... y’know, play.\"` -> Jasmynn's dad
  * `\"Get the fuck off of me, o-oh my god!\"` -> Heather
  * `\"Heather, thish the guy you was talkin' to me 'bout? The fucker who... who...\"` -> rando fox, can use Unknown / "???"
  * `\"We're shick of yous shick fuckers.\"` -> rando coyote/Darick, can use Unknown / "???"
  * `Someone next to Heather yells back, \"You leave Heather the {i}fuck{/i} alone, muskshit!\"` -> random, with non-dialogue attached
  * `\"Oh my god, he's attacking Darick!\"` -> rando
  * Van scene, micha's lines -> not sure whether these should be explicitly marked as dialogue or if that removes some of the unsettling vibe
  * (NOT DONE, too much extra RenPy work, and too opinionated for full fixes. Something should definitely be done though, since these sections feel very low quality/beta-y)
* Is there a reason that Jasmynn's house scene only appears in the Carl and Jasmynn routes?

## Echo

### Misc

* `\"Dale's missing, Cynthia drove off into the desert...\"`
  * This line is repeated a few times throughout the routes, but Cynthia should be long dead by 2015 right? Is this some sort of intentional hallucination?

* Keith's timeline in the story seems really messed up.
  * Allegedly, Brian outs Keith in ~1987 when they were teenagers, which causes him to leave to the Rez (per Jenna's route e.g.: `"So.. he just left us all behind then?"`)
  * But Keith seems to be positioned in the story as having left Echo in ~2007 per Karen's "dead to me" bit at the start of Route 65 as well as him hanging out with Micha in general
  * This timeline makes Keith about ~37 in 2007, which seems a bit too old also

### Flynn

* In the massive TJ confrontation "Condemn Flynn" splits, a lot of the character sprite emotions are desynced between them, e.g. "annoyed" vs "surprised" etc.
  * (NOT DONE, not sure which way to sync them)

## Arches

* The default font used for Arches is super obnoxious when trying to proofread
  * This has the opposite effect for normal readers, given that errors should be harder to spot with it (which is good?)
  * I switched it out for Atkinson Hyperlegible during my read, which is my preferred ebook font
  * Atkinson Hyperlegible is really good at making text "hyperlegible", aka easy to parse with 100% accuracy. It sort of has the same effect as a monospaced font

# REGEX

## Regex bits

* Find the opening `"` of a line (start of RenPy programmatic string) - `^[^"]*"`
* Find the ending `"` of a line (end of RenPy programmatic string) - `"[^"]*$`
* Don't match string before target fragment - `(?<!your|strings|here)`
  * e.g. to match instances of "silly" that are not preceded by "very" `(?<!very) silly`
* Don't match string after target fragment - `(?!your|strings|here)`
  * e.g. to match instances of "very" that are not followed by "silly" - `very (?!silly)`

## Formatting regex

* Whitespace at end of line - `\s+$`
* Bad space character codes - `( | |&#160;)`

## Common error regex

* Doubled words - `\b(\w+)\s+\1\b`
* Doubled space (uses start of programmatic string to mark the beginning of real data instead of tabs/spaces) - `^[^"]*".*  `
* Find odd-numbered RenPy character quotes (i.e. unmatched internal quotes) within the line `^[^"]*"[^"\\]*(\\"[^"\\]*){1}((\\"[^"\\]*){2})*"[^"]*$`
* Missing opening quotation mark from character dialogue - `^\s*[a-z]+\s+"[^\\{]`
* Missing punctuation before last RenPy quote in line - `[^,"?!\-…—\.\}](\{\/(i|b|size|cps|w|nw|font|p|k|sc)\})*\\"[^\\]*"[^"]*$`
* Missing punctuation before ending Renpy programmatic string (loose) - `[^,"?!\-…—\.\}](\{\/(i|b|size|cps|w|nw|font|p|k|sc)\})*"[^"]*$`
* Missing punctuation before ending Renpy programmatic string (only if nothing is after programmatic string) - `[^,"?!\-…—\.\}](\{\/(i|b|size|cps|w|nw|font|p|k|sc)\})*"\s*$`
* Double punctuation - `(\?\.|\.\?|\.!|!\.)`
* People frequently typo "lightning" into "lighting" (which is hard to notice and scanners never pick it up) - `[^a-z](lighting|lightening)`
* Accidental capital after a comma, ignoring "I". Fill in proper nouns exceptions in the parentheses (turn on case sensitivity) - `, [^a-zI\\"\{'0-9“(Devon|Cameron|Leo|Maria|Northwestern|February|Karen|Jeremy|Sydney|TJ|God|Victorian|Heather|Chase|Echo|Artie|Pueblo|Brian|Raincoat)]`
* Accidental capital word starting with "I" after a comma (turn on case sensitivity) - `, I[^'’ ]`
* Lowercase letter after terminal punctuation (turn on case sensitivity) - `[^\.](\.|!|\?) [a-z]`
* Potentially missing a comma before a name at the end of a sentence (e.g., "Hey, Chase.") - `.*\\".*[a-z] (Chase|Leo|TJ|Jenna|Carl|Flynn|etc)(\.|\?|!)`
* Missing closing parenthesis - `\([^)]*$`
* Missing closing bracket - `\{[^}]*$`
* Misspellings - `(could of|ya'll)`
* through misspelled as though (only checks for "through the", easy wins) - `(?<!even) though the[^a-z]`
* flair/flare - `(flare|flair)`
* Capitalization after a semicolon (turn on case sensitivity) - `; [A-Z]`
* Capitalization mid-sentence (populate the list with words to ignore) (turn on case sensitivity) - `[^=\.\?!\}] (?!John|Jill|I|I'm|I've|Jack)([A-Z][a-z][\w]+)`

## Mass grammar regex

* Anymore refers to time, any more refers to quantity - `[^a-z]any ?more[^a-z]`
* it's/its - `[^a-z]it'?s[^a-z]`
* whose is possessive, who's is "who is/has" - `[^a-z](who's|whose)[^a-z]`
* quick low-hit-rate scan for  a/an before a vowel - `[^a-z]a [aeiou]`
* half-way and half way should be "halfway" - `half( |-)way`
* anytime/any time
  * if you use "anytime", it should be able to be swapped with "whenever" - `[^a-z]any(-| )?time`
* someplace (American/casual)/some place (formal) - `some( |-)?place`
* complement/compliment - `compl.ment`
* affect/effect `[^a-z](a|e)ffect(s|ed|ing)?[^a-z]`
* lead/led (led is past tense of lead) `[^a-z]lead[^a-z]`
* low hit-rate scan for e.g. "X and X has", which should be "have" (e.g., "Manga and anime has") - `[\w ]+ and [\w ]+ has[^a-z]`
* low hit-rate scan for "X, X, and X has", which should be "have" - `[\w ]+, [\w ]+, and [\w ]+ has[^a-z]`
* which in middle of sentence without a comma
  * if using "which" as an unimportant aside, it should have a comma before it
  * If the information is important, "which" should be changed to "that" with no comma
  * `[^,] which`
* Familial titles should be capitalized if used in place of a name (turn on case sensitivity) - `((?<!my|My|your|Your|'s|’s| a| an|his|His|her|Her|their|Their|our|Our|own|Own|to|To|older|Older|good|Good|mom and) |[^ a-z])(mom|dad|uncle|aunt|pop|papa|mommy|daddy|father|mother|grandpa|grandma|grandfather|grandmother|brother|sister|daughter|son)[^a-z]`
* Check that capitalized familial titles are used correctly, easy-wins (turn on case sensitivity) - `(my|My|your|Your|'s|’s| a| an|his|His|her|Her|their|Their|our|Our|own|Own|to|To|older|Older|good|Good|mom and) (Mom|Dad|Uncle|Aunt|Pop|Papa|Mommy|Daddy|Father|Mother|Grandpa|Grandma|Grandfather|Grandmother|Brother|Sister|Daughter|Son)`
* Check that capitalized familial titles are used correctly, exhaustive (turn on case sensitivity) - `(Mom|Dad|Uncle|Aunt|Pop|Papa|Mommy|Daddy|Father|Mother|Grandpa|Grandma|Grandfather|Grandmother|Brother|Sister|Daughter|Son)`
* Potential missing Oxford commas (lots of false positives) - `[\w']+, [\w']+ and`
* "-looking", e.g. "goofy-looking", when an adjective modifies "looking" it should have a hyphen. The regex filters out common words preceding "looking" for ease of use - `(?<!is|'s|you|were|and|,|like|before|be|come|now|still|by|also|after|of|was|go|keeps|me|\.|keep|starts|always|up|just|start|avoid|remember|exactly|work|not|really|both|isn't|I'm|them|him|her|eyes|that|liked|but|use|already|quickly|clearly|you're|while|suddenly|kept|out|if|hate|anyone|begins|are|actually|though|without|currently|avoiding|or|occasionally|from|somehow|all|we're|stop|seriously|finally|seemingly|much|been|busy|try|even|here) looking`
* "-colored", e.g. "rust-colored", when an adjective modifies "colored" it should have a hyphen. The regex filters out common words preceding "colored" for ease of use - `(?<!the|those|these|have) colored`
* "already-", e.g. "already-stained", compound adjective before a noun (lots of false positives, use your brain) - `already `
* Starting a sentence with an -ly adverb, may want a comma (add more common words to filter if needed) - `"(?!only|holy|probably|really)\w+ly `
* did/didn't used to (should be "use to") - `[^a-z](did|didn't) .*used to`
* low-hanging fruit than/then - `(more|less|er)( \w+)? then`
* face to face/back to back/side by side/etc. - `[^a-z](\w+)( |-)(to|by)( |-)\1[^a-z]`


# Misc unsorted/unfinished/NOT DONE stuff:
  * god/God - different sections of the routes prefer to capitalize this differently (enable case-sensitivity) - `[^a-z]god[^a-z]`
  * awhile/a while - "awhile" effectively means "for a while" - `a ?while`
  * standardization of e.g. half-expect, half-buried etc etc
  * half-hour/half hour etc
  * and a half/and-a-half
  * laying/lying - these are largely used incorrectly in Echo and Arches, but I think modern readers generally prefer the incorrect versions so eh? - `[^a-z](lay|laying|lie|lying)[^a-z]`
  * in/into, on/onto - `[^a-z](on to|onto|into|in to)[^a-z]`
  * further/farther - farther is for physical distance, further is for figurative distance. not a huge deal, but easy enough to fix if desired - `[^a-z]f[au]rther[^a-z]`
  * who/whom - generally not worth the squeeze, and usually no one notices unless you misuse "whom" - `[^a-z]whom?[^a-z]`
  * more contractions - everyone in Echo speaks in casual and slang, and when they don't use contractions it's jarring as a result (he's/there's/we're/etc). If not using a contraction, there's opportunity to italicize one of the parts to show that it's intentionally broken out for emphasis
  * (teeth) grit/gritted - `[^a-z](grit|gritted)[^a-z]`
    * Not sure how to handle this. When referring to teeth being grit, it's sometimes "grit" and sometimes "gritted"
    * both variations are in the dictionary, and I suspect that the variation used depends on something in the sentence
    * I don't think the lack of consistency is something normal people would notice, so this seems fine to leave alone unless there's a good answer