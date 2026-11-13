# Naming things and how to do it right

Inform source code **seems** like it's actually in the English language, but it's not.

It's actually a computer programming language, and so a computer has to be able to understand it.

It has some strict rules, and when you break them, Inform won't let you keep making your story!

Some of those rules have to do with naming things.  Seems easy, right?  Where could it go wrong!

## The Two Jobs of a Name

A name has two jobs.

- **Job 1**: Helping the computer understand your thing: "source name"
- **Job 2**: Helping the player understand your world: "display name"

## Start with a simple, distinctive name

Usually you can make one name do both jobs.

Just give an object a name you can comfortably use in a sentence.
A few descriptive words are fine. Start ordinary things with `a`, `an`, or `the`, and use the capitalization you want the player to see.

<!-- inform-example: naming-basics
title = "An ordinary name"
kind = "standalone"
explanation = "The starting room and object used by the following naming examples."
commands = ["examine raisins", "examine old faded box", "take box of raisins", "inventory"]
expect = ["A damp box of raisins that even your Grandma won't eat.", "an old faded box of raisins"]
-->
```inform7
Grandma's Backyard is a room.
An old faded box of raisins is in Grandma's Backyard.
The description of the old faded box of raisins is "A damp box of raisins that even your Grandma won't eat."
```

The player can refer to this object as `raisins`, `faded box`, or even just `old`. Inform normally makes the individual words in an object's source name available as player vocabulary. That is convenient, but it also means that long names can introduce words you didn't intend the player to use.

In your source, use the full name when there might be confusion. `old faded box of raisins` is clearer than `box` once you have several boxes. Source references aren't case-sensitive: `Backyard` and `backyard` refer to the same room. Capitalization doesn't create a second object.

Writing `The old faded box of raisins` instead of `An old faded box of raisins` would not matter everywhere.
Inform picks what makes sense for the sentence it's printing.

## Let the player use other reasonable words

Inform doesn't know that a box might also be called a packet by weird British people. Add synonyms with `Understand`.

Append this to the starting example:

<!-- inform-example: naming-synonyms
title = "Other words for the same object"
kind = "additive"
requires = ["naming-basics"]
explanation = "Adds player vocabulary without creating another object or changing its displayed name."
commands = ["examine packet", "take carton", "inventory"]
expect = ["A damp box of raisins that even your Grandma won't eat.", "an old faded box of raisins"]
-->
```inform7
Understand "packet" or "carton" as the box of raisins.
```

This gives the existing box of raisins more vocabulary. It doesn't create another box or change what appears in the inventory. If your description calls it a packet, the player should be able to type `examine packet`.

The same applies to people. Naming someone `Captain Fabulous` doesn't automatically teach Inform the words `woman`, `officer`, or `captain of the watch`. Add the words that make sense for that character. A character's kind and their understood name are separate matters.

If you want to read the actual documentation and go deep, see [Understanding names](https://ganelson.github.io/inform-website/book/WI_17_8.html) and [Understanding values](https://ganelson.github.io/inform-website/book/WI_17_11.html).

## When the name gets in Inform's way

Names outside quotation marks are part of Inform's language. Words such as `and`, `is`, `with`, and `in` can be read as instructions about your world instead of as part of a name. Existing names of kinds, properties, and actions can also cause confusion. Punctuation can end a sentence or start another piece of syntax.

You don't need to memorize a blacklist of forbidden words. If a name makes Inform misread a declaration, give the object a simpler source name and put the troublesome wording in its **printed name**.

For example, a book title can contain `and` quite legitimately:

<!-- inform-example: naming-titles
title = "A book with a title"
kind = "additive"
requires = ["naming-basics"]
explanation = "Separates the source name, printed title, and parser vocabulary of a garden guide."
commands = ["examine weeds and other relatives", "examine garden guide", "take guide", "inventory"]
expect = ["A pocket guide to the plants Grandma insists are flowers.", "Weeds and Other Relatives"]
chapter_transcript = true
-->
```inform7
The garden guide is a thing in Grandma's Backyard.
The printed name of the garden guide is "Weeds and Other Relatives".
The garden guide is proper-named.
The description of the garden guide is "A pocket guide to the plants Grandma insists are flowers."
Understand "weeds and other relatives" or "weeds/relatives/guide" as the garden guide.
```

<!-- inform-transcript: naming-titles -->

<figure class="if-terminal" aria-label="Example gameplay transcript" style="margin: 24px 0; max-width: 100%; overflow: hidden; border: 1px solid #34494b; border-radius: 12px; background: #152326; color: #e5ede5; box-shadow: 0 6px 18px rgba(20, 31, 26, 0.12);">
<figcaption style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; padding: 12px 20px; border-bottom: 1px solid #34494b; background: #1d3032; color: #bdcfc4; font: 600 11px/1.5 ui-monospace, SFMono-Regular, Consolas, monospace; letter-spacing: 0.1em; text-transform: uppercase;"><span>Example play</span><span style="font-weight: 400; letter-spacing: 0; text-transform: none;">4 commands</span></figcaption>
<div style="padding: clamp(16px, 4vw, 24px); font: 14px/1.75 ui-monospace, SFMono-Regular, Consolas, monospace;">
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Grandma&#x27;s Backyard
You can see an old faded box of raisins and Weeds and Other Relatives here.</samp></pre>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">examine weeds and other relatives</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">A pocket guide to the plants Grandma insists are flowers.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">examine garden guide</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">A pocket guide to the plants Grandma insists are flowers.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">take guide</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Taken.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">inventory</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">You are carrying:
  Weeds and Other Relatives</samp></pre>
</div>
</div>
</figure>

<!-- /inform-transcript: naming-titles -->

There are three separate choices here:

- **Source name:** `garden guide` is how you refer to the object in your code.
- **Printed name:** `"Weeds and Other Relatives"` is what Inform displays to the player.
- **Player vocabulary:** the source words, plus the `Understand` words, are what the player can type.

**Changing the printed name does not add player vocabulary.** Without the `Understand` line, the player could still call this `garden guide`, but the displayed title wouldn't automatically work as a command's noun.

The slash notation in `"weeds/relatives/guide"` supplies alternatives at that position: `weeds`, `relatives`, or `guide`. The separate `"weeds and other relatives"` alternative accepts the whole title.

`Proper-named` prevents Inform from adding an article, so the inventory lists `Weeds and Other Relatives` rather than `a Weeds and Other Relatives`. It doesn't mean that the guide is a person. If a title already includes its own `The`, keep that word inside the printed name and use `proper-named` to prevent an extra article.

Keep the sentence's final period outside the title's quotation marks. `"Weeds and Other Relatives."` would put that period into the name itself. The manual's [Two descriptions of things](https://ganelson.github.io/inform-website/book/WI_3_11.html) example covers this separation of names and vocabulary.

## Referring to a name inside your writing

You can write ordinary prose directly into descriptions. You don't have to put brackets around every mention of an object.

Brackets become useful when you want Inform to supply the object's current name, including the right article. These are called **text substitutions**. Add this to the book example:

<!-- inform-example: naming-substitutions
title = "Names inside text"
kind = "additive"
requires = ["naming-titles"]
explanation = "Uses object substitutions to print ordinary and proper names with appropriate articles."
commands = ["look", "examine raisins"]
expect = ["Beside the old faded box of raisins lies Weeds and Other Relatives.", "The old faded box of raisins is still damp."]
chapter_transcript = true
-->
```inform7
The description of Grandma's Backyard is
"Beside [the old faded box of raisins] lies [the garden guide]."

Instead of examining the old faded box of raisins:
    say "[The old faded box of raisins] is still damp."
```

<!-- inform-transcript: naming-substitutions -->

<figure class="if-terminal" aria-label="Example gameplay transcript" style="margin: 24px 0; max-width: 100%; overflow: hidden; border: 1px solid #34494b; border-radius: 12px; background: #152326; color: #e5ede5; box-shadow: 0 6px 18px rgba(20, 31, 26, 0.12);">
<figcaption style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; padding: 12px 20px; border-bottom: 1px solid #34494b; background: #1d3032; color: #bdcfc4; font: 600 11px/1.5 ui-monospace, SFMono-Regular, Consolas, monospace; letter-spacing: 0.1em; text-transform: uppercase;"><span>Example play</span><span style="font-weight: 400; letter-spacing: 0; text-transform: none;">2 commands</span></figcaption>
<div style="padding: clamp(16px, 4vw, 24px); font: 14px/1.75 ui-monospace, SFMono-Regular, Consolas, monospace;">
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Grandma&#x27;s Backyard
Beside the old faded box of raisins lies Weeds and Other Relatives.</samp></pre>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">look</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Grandma&#x27;s Backyard
Beside the old faded box of raisins lies Weeds and Other Relatives.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">examine raisins</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">The old faded box of raisins is still damp.</samp></pre>
</div>
</div>
</figure>

<!-- /inform-transcript: naming-substitutions -->

`[the garden guide]` prints `Weeds and Other Relatives`, using its printed name and respecting its proper naming. It doesn't print the source words `garden guide` or add an unwanted `the`.

- `[old faded box of raisins]` prints `old faded box of raisins`: the name alone.
- `[the old faded box of raisins]` prints `the old faded box of raisins`: the name with a definite article, when appropriate.
- `[a old faded box of raisins]` prints `an old faded box of raisins`: the name with an indefinite article, when appropriate.
- `[The old faded box of raisins]` prints `The old faded box of raisins`: the definite form at the start of a sentence.
- `[A old faded box of raisins]` prints `An old faded box of raisins`: the indefinite form at the start of a sentence.

`[a ...]` chooses the applicable indefinite article; you don't have to change it to `[an ...]` for a name starting with a vowel. It can also supply `some`, or omit the article for a proper name.

If you later change an object's printed name, these substitutions use the new name. Literal prose such as `"You admire the box of raisins."` keeps saying exactly what you typed. This makes substitutions useful for recurring references and names that might change. Renaming the source identifier itself still requires updating code references, including the ones inside brackets.

Put the article **inside** the brackets: `"Beside [the garden guide]..."`. Writing `"Beside the [garden guide]..."` hardcodes `the` and loses that adjustment.

One other distinction: brackets inside quoted text perform substitutions. Brackets outside quoted text mark source comments. See [Text which names things](https://ganelson.github.io/inform-website/book/WI_5_3.html).

## People's names, ranks, and ordinary descriptions

Inform's initial article choices depend on how you introduce an object. A name introduced without `a`, `an`, `the`, or `some` is normally treated as a proper name.

This example starts again with just Grandma's Backyard and the box of raisins:

<!-- inform-example: naming-people
title = "Captain Fabulous and the neighbor"
kind = "additive"
requires = ["naming-basics"]
explanation = "Contrasts an article-free personal name with an ordinary description of someone in the yard."
commands = ["examine captain", "examine neighbor", "look"]
expect = ["Captain Fabulous checks the hydrangeas.", "The neighbor with the rake checks the gate.", "a neighbor with the rake"]
-->
```inform7
Captain Fabulous is a woman in Grandma's Backyard.
The neighbor is a man in Grandma's Backyard.
The printed name of the neighbor is "neighbor with the rake".

The description of Captain Fabulous is
"[The Captain Fabulous] checks the hydrangeas."
The description of the neighbor is
"[The neighbor] checks the gate."
```

The first description begins `Captain Fabulous`, and the second begins `The neighbor with the rake`. A rank can be part of a proper name without needing special syntax. A job description usually wants an article.

If Inform's initial choice is wrong, explicitly give the object `proper-named` or `improper-named`. Capital letters alone aren't the switch. Nor does proper naming choose a character's gender: `man`, `woman`, and other person properties are separate from the name.

There is a subtle exception worth recognizing when you encounter it: in a declaration using `called`, an article after `called` carries extra meaning. `A man called the neighbor` asks for `the neighbor` even where an ordinary object would get an indefinite article. For predictable results, use a straightforward declaration and set naming properties explicitly when needed. [Articles and proper names](https://ganelson.github.io/inform-website/book/WI_3_18.html) explains the initial choices.

## Plural names and “some”

One Inform object can represent several physical things that the player handles together, such as a pair of gardening gloves. Introducing it with `some` normally makes it **plural-named**.

A quantity of potting soil also wants `some`, but it is grammatically singular: “the potting soil is,” rather than “the potting soil are.” Set its indefinite article separately:

<!-- inform-example: naming-plurals
title = "Gardening gloves and potting soil"
kind = "additive"
requires = ["naming-basics"]
explanation = "Contrasts a plural-named object with a singular mass noun that uses some."
commands = ["examine gloves", "examine soil", "take gloves", "take soil", "inventory"]
expect = ["The gardening gloves are muddy.", "The potting soil is damp.", "some gardening gloves", "some potting soil"]
-->
```inform7
Some gardening gloves are in Grandma's Backyard.
The description of the gardening gloves is "[The gardening gloves] are muddy."

The potting soil is a thing in Grandma's Backyard.
The indefinite article of the potting soil is "some".
The description of the potting soil is "[The potting soil] is damp."
```

You can explicitly set `plural-named` or `singular-named` if the declaration gave you the wrong result. This changes grammatical treatment, not the number of objects. The gloves above are still one object; naming something `petunias` doesn't create ten separately planted flowers.

Also notice that the verbs `are` and `is` in these descriptions are literal text. A name substitution supplies the name and article, not the rest of the sentence. [Articles and proper names](https://ganelson.github.io/inform-website/book/WI_3_18.html) covers plural and mass nouns.

## Make similar things distinguishable

With a blue watering can and a yellow watering can nearby, `take watering can` may lead to “Which do you mean...?” That is a useful question when the player really has a choice.

Give both objects distinct printed names and enough vocabulary to answer the question: `blue` and `yellow`, for example. Two objects both displayed as `watering can` are much harder to distinguish, even if you gave them different source names. Don't try to resolve ambiguity with capitalization.

Be careful with extra synonyms, too. Teaching Inform that both the pinwheel and the wind chime are `garden decoration` can introduce ambiguity where none existed. Prefer the words the player is likely to mean, and test them with both objects present.

If the right words are recognized but Inform keeps preferring the wrong object, there are rules for influencing its choice. That's a later tool; first check the vocabulary and displayed names. See [Does the player mean](https://ganelson.github.io/inform-website/book/WI_17_19.html).

## You probably won't need it, but...

### Keeping a source name out of player commands

Sometimes a convenient source name contains words the player shouldn't be able to use. `Privately-named` turns off the automatic player vocabulary from that name. You then supply the vocabulary yourself.

<!-- inform-example: naming-private
title = "A source name the player cannot use"
kind = "additive"
requires = ["naming-basics"]
explanation = "A privately-named object accepts explicit vocabulary but not its internal source name."
commands = ["examine apparatus", "examine flamingo", "examine pink bird", "take flamingo", "inventory"]
expect = ["You can't see any such thing.", "A pink plastic flamingo wearing a tiny paper crown.", "a plastic lawn flamingo"]
chapter_transcript = true
-->
```inform7
The backyard morale apparatus is a privately-named thing in Grandma's Backyard.
The printed name of the backyard morale apparatus is "plastic lawn flamingo".
The description of the backyard morale apparatus is "A pink plastic flamingo wearing a tiny paper crown."
Understand "flamingo" or "pink bird" or "plastic flamingo" as the backyard morale apparatus.
```

<!-- inform-transcript: naming-private -->

<figure class="if-terminal" aria-label="Example gameplay transcript" style="margin: 24px 0; max-width: 100%; overflow: hidden; border: 1px solid #34494b; border-radius: 12px; background: #152326; color: #e5ede5; box-shadow: 0 6px 18px rgba(20, 31, 26, 0.12);">
<figcaption style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; padding: 12px 20px; border-bottom: 1px solid #34494b; background: #1d3032; color: #bdcfc4; font: 600 11px/1.5 ui-monospace, SFMono-Regular, Consolas, monospace; letter-spacing: 0.1em; text-transform: uppercase;"><span>Example play</span><span style="font-weight: 400; letter-spacing: 0; text-transform: none;">5 commands</span></figcaption>
<div style="padding: clamp(16px, 4vw, 24px); font: 14px/1.75 ui-monospace, SFMono-Regular, Consolas, monospace;">
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Grandma&#x27;s Backyard
You can see an old faded box of raisins and a plastic lawn flamingo here.</samp></pre>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">examine apparatus</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">You can&#x27;t see any such thing.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">examine flamingo</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">A pink plastic flamingo wearing a tiny paper crown.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">examine pink bird</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">A pink plastic flamingo wearing a tiny paper crown.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">take flamingo</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Taken.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">inventory</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">You are carrying:
  a plastic lawn flamingo</samp></pre>
</div>
</div>
</figure>

<!-- /inform-transcript: naming-private -->

The player can call it `flamingo`, but not `apparatus`. Your source can still refer to `the backyard morale apparatus` normally.

`Privately-named` doesn't hide the object from view or remove it from room listings. `Undescribed` omits an object from the ordinary room listing; it doesn't stop the player from referring to it. `Scenery` is useful for background things that should also be fixed in place. These properties are separate from naming; see [All About Things](../things/).

Private naming is also useful for suppressing an unwanted individual word from a longer name while explicitly allowing the complete phrase. See [Two descriptions of things](https://ganelson.github.io/inform-website/book/WI_3_11.html).

### Revealing someone's name during play

You can change the displayed name without changing which object your rules refer to. You may also need to change its article behavior and add vocabulary for the newly revealed name.

<!-- inform-example: naming-reveal
title = "Learning a neighbor's name"
kind = "additive"
requires = ["naming-basics"]
explanation = "Updates printed naming and articles, and conditionally enables the revealed name."
commands = ["examine auntie bev", "examine neighbor", "look", "examine auntie bev", "examine neighbor"]
expect = ["You can't see any such thing.", "The neighbor introduces herself as Auntie Bev.", "Auntie Bev is checking on Grandma's lavender."]
chapter_transcript = true
-->
```inform7
The quiet neighbor is a woman in Grandma's Backyard.
The description of the quiet neighbor is
"[The quiet neighbor] is checking on Grandma's lavender."

Instead of examining the quiet neighbor for the first time:
    now the printed name of the quiet neighbor is "Auntie Bev";
    now the quiet neighbor is proper-named;
    say "The neighbor introduces herself as Auntie Bev."

Understand "Auntie Bev" as the quiet neighbor
    when the quiet neighbor is proper-named.
```

<!-- inform-transcript: naming-reveal -->

<figure class="if-terminal" aria-label="Example gameplay transcript" style="margin: 24px 0; max-width: 100%; overflow: hidden; border: 1px solid #34494b; border-radius: 12px; background: #152326; color: #e5ede5; box-shadow: 0 6px 18px rgba(20, 31, 26, 0.12);">
<figcaption style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; padding: 12px 20px; border-bottom: 1px solid #34494b; background: #1d3032; color: #bdcfc4; font: 600 11px/1.5 ui-monospace, SFMono-Regular, Consolas, monospace; letter-spacing: 0.1em; text-transform: uppercase;"><span>Example play</span><span style="font-weight: 400; letter-spacing: 0; text-transform: none;">5 commands</span></figcaption>
<div style="padding: clamp(16px, 4vw, 24px); font: 14px/1.75 ui-monospace, SFMono-Regular, Consolas, monospace;">
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Grandma&#x27;s Backyard
You can see an old faded box of raisins and a quiet neighbor here.</samp></pre>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">examine auntie bev</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">You can&#x27;t see any such thing.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">examine neighbor</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">The neighbor introduces herself as Auntie Bev.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">look</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Grandma&#x27;s Backyard
You can see an old faded box of raisins and Auntie Bev here.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">examine auntie bev</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Auntie Bev is checking on Grandma&#x27;s lavender.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">examine neighbor</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Auntie Bev is checking on Grandma&#x27;s lavender.</samp></pre>
</div>
</div>
</figure>

<!-- /inform-transcript: naming-reveal -->

The source name stays `quiet neighbor`. Existing rules keep referring to her, and the bracketed name in her description now prints `Auntie Bev`. The original vocabulary still works; the conditional `Understand` line adds `Auntie Bev` once the introduction has happened. That condition is appropriate here because becoming proper-named marks this particular introduction. A more complicated story may need a separate property recording whether the player knows her name. See [Articles and proper names](https://ganelson.github.io/inform-website/book/WI_3_18.html).

### Mentioning a group of things in text

Brackets can also ask Inform to list things matching a description. The syntax is `[a list of edible things]`, rather than just `[edible things]`.

Usually you should narrow the group to the things relevant to the sentence:

<!-- inform-example: naming-lists
title = "Listing Grandma's tea"
kind = "additive"
requires = ["naming-basics"]
explanation = "Lists edible objects in the current room and updates the list after one is eaten."
commands = ["look", "eat pear", "look", "eat mystery cupcake", "look"]
expect = ["Backyard tea: an overripe pear and a mystery cupcake.", "Backyard tea: a mystery cupcake.", "Backyard tea: nothing."]
-->
```inform7
An overripe pear is an edible thing in Grandma's Backyard.
A mystery cupcake is an edible thing in Grandma's Backyard.
The description of Grandma's Backyard is
"Backyard tea: [a list of edible things in Grandma's Backyard]."
```

The list changes as objects come and go, supplies articles, and prints `nothing` if there are no matches. The restriction `in Grandma's Backyard` matters: a list of all edible things could reveal food in rooms the player hasn't reached. This lists immediate contents of the room; it isn't a general list of everything the player could reach, including food in containers or carried in an inventory. See [Text with lists](https://ganelson.github.io/inform-website/book/WI_5_5.html).

### Unusual articles and pronouns

You can set an object's `indefinite article` to text such as `"your"` or `"a pair of"` when ordinary `a`, `an`, and `some` aren't right. Grandma's ceremonial sunhat might want `"your"`. Check both the resulting phrase and singular/plural agreement; changing the article doesn't change plurality.

Finally, `it` has two contexts worth keeping apart. In source declarations, it can refer back to the most recently discussed subject, making it easy to attach a property to the wrong thing after an edit. In player commands, `it`, `him`, `her`, and `them` refer to objects tracked by the parser. A printed name or title alone doesn't determine those pronouns. For people and animals, properties such as `female`, `male`, and `neuter` affect grammatical treatment; a plural-named object is normally referred to as `them`. When debugging a naming problem, use explicit object names first; then test the pronouns separately. See [Men, women and animals](https://ganelson.github.io/inform-website/book/WI_3_17.html) and [Changing the meaning of pronouns](https://ganelson.github.io/inform-website/book/WI_17_18.html).

### The other uses of Understand

The `Understand` lines on this page add **noun vocabulary**: words for existing objects. You'll also encounter `Understand the command "..." as "..."` for giving an existing command verb another spelling, and `Understand "..." as a mistake ("...")` for recognizing an input and responding with a helpful message.

Those solve different problems. If the player can type `examine flamingo` but not `examine lawn ornament`, add object vocabulary. If they need another verb, or a special explanation for an unsupported command, see [Verbs and Actions](../actions/) and [Common Mistakes](../mistakes/). The manual covers [New commands for old grammar](https://ganelson.github.io/inform-website/book/WI_17_2.html) and [Understanding mistakes](https://ganelson.github.io/inform-website/book/WI_17_21.html).
