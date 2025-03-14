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
  * Hyphens are used for short/fast stuttering, this regex finds potential stutters with emdashes - `([\w']+)—\1`
  * This regex finds hyphens at the end of dialogue, which should maybe be an emdash `-("|\\")`
  * Arches ends sentences with double hyphens; considering changing to emdashes `--("|\\")`
  * Use emdashes instead of hyphens for breaks in a line (high hit-rate) `- [^-]+ -`
  * Use emdashes instead of hyphens for breaks in a line (comprehensive) `-[^-]+-`
  * Use emdashes instead of hyphens for asides at the end of a line ` - [^-]+$`
  * Jenna's route goes nuts with emdashes during certain sections, and I'm fairly sure they're not all used correctly. Probably not something that can be fixed at this point.
* When using fonts, the line will often have mismatched quotation mark stylings since the font starts after the first quotation mark and is often not terminated before the closing quotation mark
  * e.g. "{font}An example sentence"
  * In this case, the first quotation mark would appear in standard font style and the second would appear in custom font style
  * search for fonts used after opening quote: `\\".*\{font`

# CONSISTENCY

## Slang

* A'ight/aight
  * pick one, and consider "s'aight" as well `[^a-z]a'?ight`
* til/till/til'
  * pick one, with or without apostrophe `[^a-z]till?'?[^a-z]`
* whatsup/what's up
  * Can keep this separate if desired, just checking `what'?s ?up`
* woah/whoa/whoah
  * pick one, probably whoa `wh?oah?`
* musta/musta'
  * pick one, with or without apostrophe at end `musta`
* getcha/get'cha
  * pick one `get'?cha`
* what'cha/watcha/wat'cha/whatcha/wath'cha
  * pick one variant `wh?at?h?'?t?ch?a`
* shut up/shutup
  * pick one `shut(-| )?up`
* friggen/friggen'
  * pick one, with or without apostrophe at end `friggen`
* whaddya/whaddaya
  * pick one, probably whaddya `whadda?ya`
* lil/lil'
  * pick one `lil[^a-z]`
* 'cause/cause/cuz/'cuz
  * pick one style
  * "cuz" can be separate from "cause" if it makes more sense for the character `([^a-z]cause[^sd]|cuz[^n])`

## Locale

* gray/grey
  * probably gray, as that's the American spelling `gr(a|e)y`
* afterward/afterwards
  * pick whichever `afterwards?`
* toward/towards
  * probably toward, as that's the American spelling `towards?`
  * I didn't pre-emptively do this because there's a lot of occurrences - 231 "towards", 484 "toward"
* acknowledgment/acknowledgement
  * probably acknowledgment, that's the American spelling `acknowledge?ment`
* disoriented/disorientated, disorienting/disorientating
  * probably "disoriented", that's the American spelling `disorient`
* judgment/judgement
  * most commonly spelled as "judgment" by far
* naive/naïve
  * pick one `na(ï|i)ve`
* futbol/fútbol/futball
  * pick one. Also consider that spelling may be different when it's represented in "text message speak" in Flynn's route `f.tb`
* facade/façade
  * pick one `fa.ade`
* deja vu/déjà vu
  * pick one `d.j. vu`
* cliche/cliché
  * pick one `clich.`

## Misc

* chesire/cheshire
  * no idea what this word means, but pick one variant between Route 65 and Echo `chesh?ire`
* Lucha Lobo/Luche Lobo
  * Is there a difference? pick one probably? `luch(a|e)[^d]`
* Super Wolf/SuperWolf
  * probably SuperWolf `super.?wolf`
* Southwest/Southwestern Adventures
  * pick a spelling, probably Southwest Adventures `Southwest(ern)? Adventures`
* Paw Pad, Foot Pad, Finger Pad, Thumb Pad, Knuckle Fur
  * These should probably all be a similar style?
  * `(paw|foot|feet|finger|thumb).?pad`
  * `knuckle.?fur`
* wolfboy/wolf boy/wolfy-boy
  * Probably pick one of these, or at least condense "wolfboy/wolf-boy/wolf boy" into one variant and separate wolfy-boy `wolfy?-? ?boy[^f]`
* speciest/speciesist
  * pick one `species(is)?t`
* smush/smoosh
  * pick one `sm(u|oo)sh`
* Otter/otter
  * Generally when people refer to Chase as if his name is "Otter", it should be capitalized (mainly done by Leo)
  * `[^a-z]otter[^a-z]`
* Leo's Spanish words
  * they're often italicized; should it be a rule to always italicize them?
  * A few I remember: garrobo, `p(u)+chica`, esta yuca, chula, estupido, loco por ti, nutria, puta, madre, ay-yai, huevos, gringo, padres, buenos dias
* Town hall/city hall capitalization
  * town hall/city hall or Town Hall/City Hall? should be somewhat consistent
* Tupperware/tupperware
  * pick a capitalization
* spaz/spazz
  * pick one `spaz`
* scaley/scaly
  * pick one `scal.?y`
* AM/PM/A.M./P.M.
  * pick one (enable case-sensitivity) - `[^a-z](A|P)\.?M\.?[^a-z]`
* yote/'yote
  * apostrophe before or not, pick one `[^a-z]yote`
* rez/Rez and reservation/Reservation
  * pick a capitalization style `([^a-z]rez[^a-z]|[^a-z]reservation)`
  * a source on what to use: https://nativegov.org/resources/terminology-style-guide/
* native/Native
  * Native should always be capitalized when referring to e.g. Indigenous people: `[^a-z]native[^a-z]`
  * be careful of other meanings of the word native, which should remain lowercase
  * source: https://nativegov.org/resources/terminology-style-guide/
* county/County
  * Should county be capitalized? It's like 50/50 currently. `county`
* Capitalizations after colons
  * Overwhelmingly, capitalizations after colons aren't used correctly in R65/Echo/Arches, and I decapped them all for consistency
  * You can capitalize in very specific circumstances, but it really depends on what style guide and locale you follow, and it's usually still optional
  * If you truly want some of these colon capitalizations to be reverted then feel free, but put some thought into it, and consider the inconsistency for an average reader seeing only a couple of these remaining intact while the rest are lowercase
* What is the name of the fucking river?
  * They call it Seesaw, Yeeyaw, Yeeyah, and Yee-Yaw
  * They say that Seesaw and Yeeyaw are mispronunciations, but during Route 65 Chase again calls it Yee-Yaw:
    * "It was at the old Yee-Yaw riverway. I had just gotten my cell phone and was asking everybody to pose for a picture."
  * I have to assume the right answer is Yeeyah, but then in the code it's called yeeyaw
  * `(yee-?yaw|yee-?yah|seesaw)`
  * this keeps me up at night
* Ellipses variation is a mess and probably unfixable at this point.
  * Is there extra meaning by double dot vs. triple dot?
  * Should there be a space after ellipses or not?
  * etc
* Periods after menu choices
  * It seems most common to end the menu choices with periods, so probably make that a universal rule
* '90s/90s/90's formatting
  * generally should be written as '90s - `[^0-9][0-9]0'?s`
* fancy `‘`and`’` apostrophe codes are nonstandard, they show up in a few sections
  * Most importantly, they're always mixed with other standard apostrophes, so they should all be changed to be uniform
  * Note that the COLONNA.ttf font needs the special apostrophe codes in order to display in the right font
  * Other fonts don't have this issue, aside from forbid.ttf (which doesn't display apostrophes ever)
* fancy `“`and`”` quote codes are nonstandard (some in Arches)

## Compound words:

* Street Light/Street Lamp
  * pick one style for both probably `street.?(light|lamp)`
* Lamp Post
  * probably lamppost `lamp.?post`
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

# ROUTE SPECIFIC

## ROUTE 65

* Unmarked dialogue sections - room for improvement:
  * "\"Chase,\" he rumbles." -> Jasmynn's dad speaking but not using normal white text; maybe make a character identifier for them? non-dialogue is attached so may need tweaking?
  * "\"Fuck off, Chase!\" His voice is laden with derisive contempt." -> Jeremy, with non-dialogue attached
  * "\"She’s in her room. Got chores she ain’t done yet so she can’t go out and... y’know, play.\"" -> Jasmynn's dad
  * "\"Get the fuck off of me, o-oh my god!\"" -> Heather
  * "\"Heather, thish the guy you was talkin' to me 'bout? The fucker who... who...\"" -> rando fox, can use Unknown / "???"
  * "\"We're shick of yous shick fuckers.\"" -> rando coyote/Darick, can use Unknown / "???"
  * "Someone next to Heather yells back, \"You leave Heather the {i}fuck{/i} alone, muskshit!\"" -> random, with non-dialogue attached
  * "\"Oh my god, he's attacking Darick!\"" -> rando
  * Van scene, micha's lines -> not sure whether these should be explicitly marked as dialogue or if that removes some of the unsettling vibe
* Is there a reason that Jasmynn's house scene only appears in the Carl and Jasmynn routes?

## Echo

### Misc

* "\"Dale's missing, Cynthia drove off into the desert...\""
  * This line is repeated a few times throughout the routes, but Cynthia should be long dead by 2015 right? Is this some sort of intentional hallucination?

### Flynn

* In the massive TJ confrontation "Condemn Flynn" splits, a lot of the character sprite emotions are desynced between them, e.g. "annoyed" vs "surprised" etc.

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


# Misc unsorted/unfinished stuff:
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