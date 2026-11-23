# All About Things

Your imaginary worlds in Inform 7 are almost inevitably going to have things in them.  The real world has things, and people expect them.  Let's not disappoint them.  

## A place to put things
First let's make a place to put our things in, because Inform needs a place for our things to be in with us.

<!-- inform-example: the-place
title = "A place to put things"
kind = "standalone"
explanation = "The reusable starting room for the things chapter."
commands = ["look"]
expect = ["You're in the only place."]
-->
```inform7
"A Place with Things in It" by You

The Place is a room.
The description is "You're in the only place."
[We could say The description of The Place is...
 but Inform knows we mean the last thing we mentioned]
Use the serial comma. [because we're not savages]
```
## Super basic things
Now, let's put some super basic things in it.  Let's make three things, two balls, one red and one blue, and a hammer.  You know, things you'd find in a room.

<!-- inform-example: basic-things
title = "Balls and a hammer"
kind = "additive"
requires = ["the-place"]
explanation = "Add the two balls and hammer to the starting room."
commands = ["look at green ball", "get hammer", "inventory", "look"]
expect = ["a hammer"]
notes = "Uses an explicit object name; interactive disambiguation replies are not supported by the capture harness."
chapter_transcript = true
-->
```inform7
There is a red ball in The Place.
There is a green ball in The Place.
There is a hammer in The Place.
```
_{Shortcut}:_ or we can use a shortcut using the keyword "here" to mean the last place we talked about:

<!-- inform-example: hammer-here
title = "Here means the last room"
kind = "alternative"
requires = ["the-place"]
instead_of = ["basic-things"]
explanation = "Alternative spelling of the hammer declaration only; the two ball declarations are omitted in this isolated demonstration."
commands = ["take hammer", "inventory"]
expect = ["a hammer"]
-->
```inform7
A hammer is here.
```
Typing `look at the ball` would make Inform ask which ball you mean. The captured play below names the green ball explicitly.

<!-- inform-transcript: basic-things -->

<figure class="if-terminal" aria-label="Example gameplay transcript" style="margin: 24px 0; max-width: 100%; overflow: hidden; border: 1px solid #34494b; border-radius: 12px; background: #152326; color: #e5ede5; box-shadow: 0 6px 18px rgba(20, 31, 26, 0.12);">
<figcaption style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; padding: 12px 20px; border-bottom: 1px solid #34494b; background: #1d3032; color: #bdcfc4; font: 600 11px/1.5 ui-monospace, SFMono-Regular, Consolas, monospace; letter-spacing: 0.1em; text-transform: uppercase;"><span>Example play</span><span style="font-weight: 400; letter-spacing: 0; text-transform: none;">4 commands</span></figcaption>
<div style="padding: clamp(16px, 4vw, 24px); font: 14px/1.75 ui-monospace, SFMono-Regular, Consolas, monospace;">
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Place
You&#x27;re in the only place.

You can see a red ball, a green ball, and a hammer here.</samp></pre>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">look at green ball</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">You see nothing special about the green ball.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">get hammer</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Taken.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">inventory</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">You are carrying:
  a hammer</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">look</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Place
You&#x27;re in the only place.

You can see a red ball and a green ball here.</samp></pre>
</div>
</div>
</figure>

<!-- /inform-transcript: basic-things -->

## Things you can look at

Inform prints room descriptions automatically, and then lists the things in the room.  It only lists the names of the things, along with their adjectives.  It doesn't know the difference between a ball and a hammer, so it just uses a stock message: "You see nothing special about [the noun]."

### Describing things when you look at them
Just like our description of the room, let's make our red ball a little more interesting.

<!-- inform-example: red-ball-description
title = "Describing a ball"
kind = "additive"
requires = ["basic-things"]
explanation = "Add a description to the red ball already created above."
commands = ["look at red ball"]
expect = ["radiates a very spooky energy."]
-->
```inform7
The description of the red ball is 
"It's spherical, red, and radiates a very spooky energy.".
```
*{shortcut}* or, we can use a shorthand for the last thing we mentioned by cutting out the name of the thing:

<!-- inform-example: red-ball-shortcut
title = "The last-mentioned thing"
kind = "alternative"
requires = ["the-place"]
instead_of = ["red-ball-description", "basic-things"]
explanation = "Recreates just the red ball and its description together; omit the earlier ball declaration and description."
commands = ["look at red ball"]
expect = ["radiates a very spooky energy."]
-->
```inform7
There is a red ball in The Place.
The description is 
"It's spherical, red, and radiates a very spooky energy.".
```
### Things with lots of names
Let's say we want a television in our game:

<!-- inform-example: television
title = "A television without aliases"
kind = "additive"
requires = ["the-place"]
explanation = "Start a new object example in the chapter starting room."
commands = ["look tv"]
expect = ["You can't see any such thing."]
chapter_transcript = true
-->
```inform7
There is a television in The Place.
The description is "It's playing ESPN 8, the Ocho.".
```
<!-- inform-transcript: television -->

<figure class="if-terminal" aria-label="Example gameplay transcript" style="margin: 24px 0; max-width: 100%; overflow: hidden; border: 1px solid #34494b; border-radius: 12px; background: #152326; color: #e5ede5; box-shadow: 0 6px 18px rgba(20, 31, 26, 0.12);">
<figcaption style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; padding: 12px 20px; border-bottom: 1px solid #34494b; background: #1d3032; color: #bdcfc4; font: 600 11px/1.5 ui-monospace, SFMono-Regular, Consolas, monospace; letter-spacing: 0.1em; text-transform: uppercase;"><span>Example play</span><span style="font-weight: 400; letter-spacing: 0; text-transform: none;">1 command</span></figcaption>
<div style="padding: clamp(16px, 4vw, 24px); font: 14px/1.75 ui-monospace, SFMono-Regular, Consolas, monospace;">
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Place
You&#x27;re in the only place.

You can see a television here.</samp></pre>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">look tv</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">You can&#x27;t see any such thing.</samp></pre>
</div>
</div>
</figure>

<!-- /inform-transcript: television -->

Humans know that TV, teevee, telly, and idiot box all mean television, but Inform doesn't.  There's an easy way to tell it, though:

<!-- inform-example: television-aliases
title = "Multiple aliases"
kind = "additive"
requires = ["television"]
explanation = "Add three aliases to the television already defined."
commands = ["look tv", "look telly", "look idiot box"]
expect = ["It's playing ESPN 8, the Ocho."]
chapter_transcript = true
-->
```inform7
Understand "TV" as television.
Understand "telly" as television.
Understand "idiot box" as television.
```
Now:

<!-- inform-transcript: television-aliases -->

<figure class="if-terminal" aria-label="Example gameplay transcript" style="margin: 24px 0; max-width: 100%; overflow: hidden; border: 1px solid #34494b; border-radius: 12px; background: #152326; color: #e5ede5; box-shadow: 0 6px 18px rgba(20, 31, 26, 0.12);">
<figcaption style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; padding: 12px 20px; border-bottom: 1px solid #34494b; background: #1d3032; color: #bdcfc4; font: 600 11px/1.5 ui-monospace, SFMono-Regular, Consolas, monospace; letter-spacing: 0.1em; text-transform: uppercase;"><span>Example play</span><span style="font-weight: 400; letter-spacing: 0; text-transform: none;">3 commands</span></figcaption>
<div style="padding: clamp(16px, 4vw, 24px); font: 14px/1.75 ui-monospace, SFMono-Regular, Consolas, monospace;">
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Place
You&#x27;re in the only place.

You can see a television here.</samp></pre>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">look tv</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">It&#x27;s playing ESPN 8, the Ocho.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">look telly</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">It&#x27;s playing ESPN 8, the Ocho.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">look idiot box</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">It&#x27;s playing ESPN 8, the Ocho.</samp></pre>
</div>
</div>
</figure>

<!-- /inform-transcript: television-aliases -->

*{shortcut}* instead of multiple "understand" statements, we can combine them like this:
<!-- inform-example: television-or
title = "Aliases with or"
kind = "alternative"
requires = ["television"]
instead_of = ["television-aliases"]
explanation = "Replace the three alias statements with one statement using or."
commands = ["look tv", "look telly", "look idiot box"]
expect = ["It's playing ESPN 8, the Ocho."]
-->
```inform7
Understand "TV" or "telly" or "idiot box" as television.
```
You can also go even shorter by doing this trick:

<!-- inform-example: television-slashes
title = "Aliases with slashes"
kind = "alternative"
requires = ["television"]
instead_of = ["television-aliases", "television-or"]
explanation = "Another alias spelling; use this instead of either earlier alias block."
commands = ["look tv", "look telly", "look teevee"]
expect = ["It's playing ESPN 8, the Ocho."]
-->
```inform7
Understand "TV/telly/teevee" as television.
```

There's another reason we'd want to use this technique.  Consider this:

<!-- inform-example: log-parts
title = "Describing individual parts"
kind = "additive"
requires = ["the-place"]
explanation = "Start a new log example with separately described parts in the starting room."
commands = ["look mosses", "look lichens", "look mushrooms", "take log"]
expect = ["So mossy."]
-->
```inform7
A rotted log is here.
It is fixed in place.
The description is "The log is a rich ecosystem of mosses, lichens, and little mushrooms.  It is filled with little knots and woodpecker holes.".
The mosses are a part of the log.
The description is "So mossy.".
The lichens are a part of the log.
The description is "You've seen lichen.".
The little mushrooms are a part of the log.
The description is "This is going to take forever.".
The knots are a part of the log.
The woodpecker holes are a part of the log.
```
Sometimes it's great to go into all this detail, but sometimes when you have a whole forest to fill up, and you want your game to respond to "look at the lichens" you can replace the individual parts with aliases:

<!-- inform-example: log-aliases
title = "Aliases instead of individual log parts"
kind = "alternative"
requires = ["the-place"]
instead_of = ["log-parts"]
explanation = "Recreate the log with aliases instead of defining its individual parts."
commands = ["look mosses", "look lichens", "look woodpecker holes"]
expect = ["The log is a rich ecosystem"]
chapter_transcript = true
-->
```inform7
A rotted log is here.
It is fixed in place.
The description is "The log is a rich ecosystem of mosses, lichens, and little mushrooms. It is filled with little knots and woodpecker holes.".
Understand "moss/mosses/lichen/lichens/mushroom/mushrooms/knot/knots/hole/holes" or "woodpecker holes" as the log.
```
It's a nicer effect to have each individual thing described, using parts, but it's better than nothing to just add an `understand` statement so the game says this as little as possible when people are trying to look deeper into the descriptions of your game:

<!-- inform-transcript: log-aliases -->

<figure class="if-terminal" aria-label="Example gameplay transcript" style="margin: 24px 0; max-width: 100%; overflow: hidden; border: 1px solid #34494b; border-radius: 12px; background: #152326; color: #e5ede5; box-shadow: 0 6px 18px rgba(20, 31, 26, 0.12);">
<figcaption style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; padding: 12px 20px; border-bottom: 1px solid #34494b; background: #1d3032; color: #bdcfc4; font: 600 11px/1.5 ui-monospace, SFMono-Regular, Consolas, monospace; letter-spacing: 0.1em; text-transform: uppercase;"><span>Example play</span><span style="font-weight: 400; letter-spacing: 0; text-transform: none;">3 commands</span></figcaption>
<div style="padding: clamp(16px, 4vw, 24px); font: 14px/1.75 ui-monospace, SFMono-Regular, Consolas, monospace;">
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Place
You&#x27;re in the only place.

You can see a rotted log here.</samp></pre>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">look mosses</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">The log is a rich ecosystem of mosses, lichens, and little mushrooms. It is filled with little knots and woodpecker holes.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">look lichens</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">The log is a rich ecosystem of mosses, lichens, and little mushrooms. It is filled with little knots and woodpecker holes.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">look woodpecker holes</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">The log is a rich ecosystem of mosses, lichens, and little mushrooms. It is filled with little knots and woodpecker holes.</samp></pre>
</div>
</div>
</figure>

<!-- /inform-transcript: log-aliases -->

### Things with ONLY aliases

Maybe you called a lawn flamingo the “backyard morale apparatus” while writing your game, but players should be able to ask about the “flamingo,” not your behind-the-scenes name. `privately-named` lets you choose just the words players can try. See [Naming things](../naming/README.md) for details.

### Things with special names (printed and proper)

Your garden guide might need a simple name while you write the game, but look much grander to players as *Weeds and Other Relatives*. That's its **printed name**. And if your ship is called *The Saucy Turnip*, `proper-named` stops Inform from accidentally calling it “the The Saucy Turnip.” A fancy printed name doesn't automatically teach the game what players can type. See [Naming things](../naming/README.md) for details.

You can also add adjectives and clauses to item names like this:

<!-- inform-example: rainbow-statue
title = "A complicated object name"
kind = "additive"
requires = ["the-place"]
explanation = "A separate object-name example using the chapter starting room."
commands = ["look statue"]
expect = ["It sure is ugly."]
-->
```inform7
There is a gaudy rainbow statue of Teddy Roosevelt in The Place.
The description is "It sure is ugly.".
```

## Things you can't take

By default, the player can pick up any objects you create.  But sometimes, it doesn't make sense.

### Things you can't take

<!-- inform-example: portable-anvil
title = "Portable by default"
kind = "additive"
requires = ["the-place"]
explanation = "Start the anvil example with default portability."
commands = ["take anvil", "inventory"]
expect = ["Taken."]
chapter_transcript = true
-->
```inform7
There is an anvil bolted into the ground in The Place.  
The description is 
"The anvil is bolted into the ground for real."
```
<!-- inform-transcript: portable-anvil -->

<figure class="if-terminal" aria-label="Example gameplay transcript" style="margin: 24px 0; max-width: 100%; overflow: hidden; border: 1px solid #34494b; border-radius: 12px; background: #152326; color: #e5ede5; box-shadow: 0 6px 18px rgba(20, 31, 26, 0.12);">
<figcaption style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; padding: 12px 20px; border-bottom: 1px solid #34494b; background: #1d3032; color: #bdcfc4; font: 600 11px/1.5 ui-monospace, SFMono-Regular, Consolas, monospace; letter-spacing: 0.1em; text-transform: uppercase;"><span>Example play</span><span style="font-weight: 400; letter-spacing: 0; text-transform: none;">2 commands</span></figcaption>
<div style="padding: clamp(16px, 4vw, 24px); font: 14px/1.75 ui-monospace, SFMono-Regular, Consolas, monospace;">
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Place
You&#x27;re in the only place.

You can see an anvil bolted into the ground here.</samp></pre>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">take anvil</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Taken.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">inventory</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">You are carrying:
  an anvil bolted into the ground</samp></pre>
</div>
</div>
</figure>

<!-- /inform-transcript: portable-anvil -->

Damn.  That's because objects in Inform can be `portable` or `fixed in place`.  By default, they're portable.  Let's put a stop to that.

<!-- inform-example: fixed-anvil
title = "Fixed in place"
kind = "alternative"
requires = ["the-place"]
instead_of = ["portable-anvil"]
explanation = "Replace the original anvil block with this fixed version."
commands = ["take anvil"]
expect = ["That's fixed in place."]
chapter_transcript = true
-->
```inform7
There is an anvil bolted into the ground in The Place.  
It is fixed in place.  
The description is 
"The anvil is bolted into the ground for real.".
```
<!-- inform-transcript: fixed-anvil -->

<figure class="if-terminal" aria-label="Example gameplay transcript" style="margin: 24px 0; max-width: 100%; overflow: hidden; border: 1px solid #34494b; border-radius: 12px; background: #152326; color: #e5ede5; box-shadow: 0 6px 18px rgba(20, 31, 26, 0.12);">
<figcaption style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; padding: 12px 20px; border-bottom: 1px solid #34494b; background: #1d3032; color: #bdcfc4; font: 600 11px/1.5 ui-monospace, SFMono-Regular, Consolas, monospace; letter-spacing: 0.1em; text-transform: uppercase;"><span>Example play</span><span style="font-weight: 400; letter-spacing: 0; text-transform: none;">1 command</span></figcaption>
<div style="padding: clamp(16px, 4vw, 24px); font: 14px/1.75 ui-monospace, SFMono-Regular, Consolas, monospace;">
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Place
You&#x27;re in the only place.

You can see an anvil bolted into the ground here.</samp></pre>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">take anvil</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">That&#x27;s fixed in place.</samp></pre>
</div>
</div>
</figure>

<!-- /inform-transcript: fixed-anvil -->

That'll show 'em.

### Things that are parts of other things
If we describe things, people are going to want to know more about them.  Like this hammer:

<!-- inform-example: hammer-description
title = "Mentioning a handle"
kind = "alternative"
requires = ["the-place"]
instead_of = ["basic-things"]
explanation = "Start a focused hammer example; this block supplies the hammer declaration and description."
commands = ["look at handle"]
expect = ["You can't see any such thing."]
chapter_transcript = true
-->
```inform7
There is a hammer in The Place.  
The description is 
"It's an OK hammer but it has a solid gold handle."
```
<!-- inform-transcript: hammer-description -->

<figure class="if-terminal" aria-label="Example gameplay transcript" style="margin: 24px 0; max-width: 100%; overflow: hidden; border: 1px solid #34494b; border-radius: 12px; background: #152326; color: #e5ede5; box-shadow: 0 6px 18px rgba(20, 31, 26, 0.12);">
<figcaption style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; padding: 12px 20px; border-bottom: 1px solid #34494b; background: #1d3032; color: #bdcfc4; font: 600 11px/1.5 ui-monospace, SFMono-Regular, Consolas, monospace; letter-spacing: 0.1em; text-transform: uppercase;"><span>Example play</span><span style="font-weight: 400; letter-spacing: 0; text-transform: none;">1 command</span></figcaption>
<div style="padding: clamp(16px, 4vw, 24px); font: 14px/1.75 ui-monospace, SFMono-Regular, Consolas, monospace;">
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Place
You&#x27;re in the only place.

You can see a hammer here.</samp></pre>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">look at handle</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">You can&#x27;t see any such thing.</samp></pre>
</div>
</div>
</figure>

<!-- /inform-transcript: hammer-description -->

Not what we want.  Luckily there's an easy way to fix it.

<!-- inform-example: separate-handle
title = "A handle as a separate object"
kind = "alternative"
requires = ["the-place"]
instead_of = ["hammer-description"]
explanation = "Replace the preceding hammer block with a version that creates a separate handle."
commands = ["look", "take handle"]
expect = ["Taken."]
chapter_transcript = true
-->
```inform7
There is a hammer in The Place.  
The description is 
"It's an OK hammer but it has a solid gold handle.".  
There is a handle in The Place.  
The description is 
"It's made of solid gold.".
```
<!-- inform-transcript: separate-handle -->

<figure class="if-terminal" aria-label="Example gameplay transcript" style="margin: 24px 0; max-width: 100%; overflow: hidden; border: 1px solid #34494b; border-radius: 12px; background: #152326; color: #e5ede5; box-shadow: 0 6px 18px rgba(20, 31, 26, 0.12);">
<figcaption style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; padding: 12px 20px; border-bottom: 1px solid #34494b; background: #1d3032; color: #bdcfc4; font: 600 11px/1.5 ui-monospace, SFMono-Regular, Consolas, monospace; letter-spacing: 0.1em; text-transform: uppercase;"><span>Example play</span><span style="font-weight: 400; letter-spacing: 0; text-transform: none;">2 commands</span></figcaption>
<div style="padding: clamp(16px, 4vw, 24px); font: 14px/1.75 ui-monospace, SFMono-Regular, Consolas, monospace;">
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Place
You&#x27;re in the only place.

You can see a hammer and a handle here.</samp></pre>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">look</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Place
You&#x27;re in the only place.

You can see a hammer and a handle here.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">take handle</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Taken.</samp></pre>
</div>
</div>
</figure>

<!-- /inform-transcript: separate-handle -->

Well that's not right either.    The handle is listed separately and we can take it.  Here's how we prevent that in Inform:

<!-- inform-example: attached-handle
title = "A handle as a part"
kind = "alternative"
requires = ["the-place"]
instead_of = ["separate-handle"]
explanation = "Replace the separate-handle version with a handle that is part of the hammer."
commands = ["look hammer", "look handle", "take handle"]
expect = ["That seems to be a part of the hammer."]
chapter_transcript = true
-->
```inform7
There is a hammer in The Place.  
The description is "It definitely has a handle."
The handle is a part of the hammer.  
```
<!-- inform-transcript: attached-handle -->

<figure class="if-terminal" aria-label="Example gameplay transcript" style="margin: 24px 0; max-width: 100%; overflow: hidden; border: 1px solid #34494b; border-radius: 12px; background: #152326; color: #e5ede5; box-shadow: 0 6px 18px rgba(20, 31, 26, 0.12);">
<figcaption style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; padding: 12px 20px; border-bottom: 1px solid #34494b; background: #1d3032; color: #bdcfc4; font: 600 11px/1.5 ui-monospace, SFMono-Regular, Consolas, monospace; letter-spacing: 0.1em; text-transform: uppercase;"><span>Example play</span><span style="font-weight: 400; letter-spacing: 0; text-transform: none;">3 commands</span></figcaption>
<div style="padding: clamp(16px, 4vw, 24px); font: 14px/1.75 ui-monospace, SFMono-Regular, Consolas, monospace;">
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Place
You&#x27;re in the only place.

You can see a hammer here.</samp></pre>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">look hammer</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">It definitely has a handle.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">look handle</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">You see nothing special about the handle.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">take handle</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">That seems to be a part of the hammer.</samp></pre>
</div>
</div>
</figure>

<!-- /inform-transcript: attached-handle -->

Perfect.  Now it doesn't list the hammer or let us take it, but it knows the handle exists.  Not only that but parts can have parts.

<!-- inform-example: dragon-parts
title = "Parts can have parts"
kind = "additive"
requires = ["the-place"]
explanation = "Start a fresh dragon example with nested parts."
commands = ["look claws", "take feet"]
expect = ["That seems to be a part of the legs."]
-->
```inform7
There is a ceramic dragon in The Place.
The description is "The ceramic dragon is wicked.  It has scales, a tail, and legs with feet and the feet have long claws." 
The scales are a part of the dragon.
The legs are a part of the dragon.
The feet are a part of the legs.
The claws are a part of the feet.  
```
Remember, though, most of the time we want to decide how detailed we get.    We want to balance where we put our effort.  In most cases we can do it with aliases:

<!-- inform-example: dragon-aliases
title = "Aliases instead of parts"
kind = "alternative"
requires = ["the-place"]
instead_of = ["dragon-parts"]
explanation = "Replace the dragon and its parts with a dragon using aliases."
commands = ["look claws", "look feet"]
expect = ["The ceramic dragon is wicked."]
-->
```inform7
There is a ceramic dragon in The Place.
The description is "The ceramic dragon is wicked.  It has scales, a tail, and legs with feet and the feet have long claws." 
Understand "scales/legs/leg/feet/claws" as the dragon. 
```
Someone can't look at each individual thing this way, but at least the game won't say they don't exist.

### Things in the background

Let's add a little bit of background ambience to our otherwise very generic place:

<!-- inform-example: background-listed
title = "Background objects listed twice"
kind = "alternative"
instead_of = ["the-place"]
explanation = "Replace the starting room description and add hills and clouds; context supplies only the room declaration to avoid two descriptions."
context = "The Place is a room."
commands = ["look"]
expect = ["You can see rolling hills and clouds here."]
chapter_transcript = true
-->
```inform7
The description is "You're in the only place, and you can see beautiful rolling hills and the fluffiest of clouds."
There are rolling hills in the place.
They are fixed in place.
There are clouds in the place.
They are fixed in place.
```
<!-- inform-transcript: background-listed -->

<figure class="if-terminal" aria-label="Example gameplay transcript" style="margin: 24px 0; max-width: 100%; overflow: hidden; border: 1px solid #34494b; border-radius: 12px; background: #152326; color: #e5ede5; box-shadow: 0 6px 18px rgba(20, 31, 26, 0.12);">
<figcaption style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; padding: 12px 20px; border-bottom: 1px solid #34494b; background: #1d3032; color: #bdcfc4; font: 600 11px/1.5 ui-monospace, SFMono-Regular, Consolas, monospace; letter-spacing: 0.1em; text-transform: uppercase;"><span>Example play</span><span style="font-weight: 400; letter-spacing: 0; text-transform: none;">1 command</span></figcaption>
<div style="padding: clamp(16px, 4vw, 24px); font: 14px/1.75 ui-monospace, SFMono-Regular, Consolas, monospace;">
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Place
You&#x27;re in the only place, and you can see beautiful rolling hills and the fluffiest of clouds.

You can see rolling hills and clouds here.</samp></pre>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">look</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Place
You&#x27;re in the only place, and you can see beautiful rolling hills and the fluffiest of clouds.

You can see rolling hills and clouds here.</samp></pre>
</div>
</div>
</figure>

<!-- /inform-transcript: background-listed -->

That's pretty good, but since we made the rolling hills and clouds a part of our description, we don't need them described again.  Just like items can be `portable` or `fixed in place`, they can also be `described` or `undescribed`.  Things are `described` by default.

So let's try this:

<!-- inform-example: background-undescribed
title = "Undescribed background objects"
kind = "alternative"
instead_of = ["background-listed"]
explanation = "Replace the listed-background version with undescribed hills and clouds."
context = "The Place is a room."
commands = ["look", "take clouds"]
expect = ["That's fixed in place."]
chapter_transcript = true
-->
```inform7
The description is "You're in the only place, and you can see beautiful rolling hills and the fluffiest of clouds."
There are rolling hills in the place.
They are fixed in place.  They are undescribed.
There are clouds in the place.
They are fixed in place.  They are undescribed.
```
<!-- inform-transcript: background-undescribed -->

<figure class="if-terminal" aria-label="Example gameplay transcript" style="margin: 24px 0; max-width: 100%; overflow: hidden; border: 1px solid #34494b; border-radius: 12px; background: #152326; color: #e5ede5; box-shadow: 0 6px 18px rgba(20, 31, 26, 0.12);">
<figcaption style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; padding: 12px 20px; border-bottom: 1px solid #34494b; background: #1d3032; color: #bdcfc4; font: 600 11px/1.5 ui-monospace, SFMono-Regular, Consolas, monospace; letter-spacing: 0.1em; text-transform: uppercase;"><span>Example play</span><span style="font-weight: 400; letter-spacing: 0; text-transform: none;">2 commands</span></figcaption>
<div style="padding: clamp(16px, 4vw, 24px); font: 14px/1.75 ui-monospace, SFMono-Regular, Consolas, monospace;">
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Place
You&#x27;re in the only place, and you can see beautiful rolling hills and the fluffiest of clouds.</samp></pre>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">look</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Place
You&#x27;re in the only place, and you can see beautiful rolling hills and the fluffiest of clouds.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">take clouds</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">That&#x27;s fixed in place.</samp></pre>
</div>
</div>
</figure>

<!-- /inform-transcript: background-undescribed -->

Much better.  Having background things that are in the description is common, so there is a shortcut for `fixed in place` and `undescribed` at the same time.  

_{Shortcut}:_ Some things can be combined in the same sentence, so we can do this:

<!-- inform-example: clouds-combined
title = "Combining properties"
kind = "alternative"
requires = ["the-place"]
instead_of = ["background-undescribed"]
explanation = "Isolated shorthand for the clouds portion of the preceding block; the hills are omitted."
commands = ["look clouds", "take clouds"]
expect = ["That's fixed in place."]
-->
```inform7
There are clouds in The Place.
They are fixed in place and undescribed.
```
_{Shortcut}:_ For this combination there is an even better shortcut:

<!-- inform-example: clouds-scenery
title = "The scenery shortcut"
kind = "alternative"
requires = ["the-place"]
instead_of = ["clouds-combined"]
explanation = "Replace the clouds property statements with scenery."
commands = ["look clouds", "take clouds"]
expect = ["That's hardly portable."]
-->
```inform7
There are clouds in The Place.
They are scenery.
```

Since having background items that are both `fixed in place` and `undescribed` is so common, we just call them `scenery`.  You'll use scenery a lot.  So here's our new, streamlined description:

<!-- inform-example: background-scenery
title = "Describing the background"
kind = "alternative"
instead_of = ["background-undescribed"]
explanation = "Consolidated background version with scenery and individual descriptions; context supplies the room declaration."
context = "The Place is a room."
commands = ["look hills", "look clouds"]
expect = ["You have never seen fluffier."]
-->
```inform7
The description is "You're in the only place, and you can see beautiful rolling hills and the fluffiest of clouds."
There are rolling hills in the place. They are scenery.
The description is "They roll on forever.".
There are clouds in the place. They are scenery.
The description is "You have never seen fluffier.".
```
### @TODO Explain backdrops that appear in multiple rooms


## Things you can do stuff to

We're making interactive fiction, not just "things you can pick up and look at", so we want to be able to do stuff to our things!  Inform builds in a lot of common helpers to make things act in a more realistic way.  

There aren't many of these built in to Inform.  It has `wearable` things, `edible` things and things that can be a `container`.

### Things that you can eat

One of the simplest is that things can be `edible` or `inedible` and obviously are `inedible` by default.

<!-- inform-example: inedible-fig
title = "Inedible by default"
kind = "additive"
requires = ["the-place"]
explanation = "Start a fresh fig example in the starting room."
commands = ["eat fig"]
expect = ["That's plainly inedible."]
chapter_transcript = true
-->
```inform7
A yummy fig is here.
```
I love figs!

<!-- inform-transcript: inedible-fig -->

<figure class="if-terminal" aria-label="Example gameplay transcript" style="margin: 24px 0; max-width: 100%; overflow: hidden; border: 1px solid #34494b; border-radius: 12px; background: #152326; color: #e5ede5; box-shadow: 0 6px 18px rgba(20, 31, 26, 0.12);">
<figcaption style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; padding: 12px 20px; border-bottom: 1px solid #34494b; background: #1d3032; color: #bdcfc4; font: 600 11px/1.5 ui-monospace, SFMono-Regular, Consolas, monospace; letter-spacing: 0.1em; text-transform: uppercase;"><span>Example play</span><span style="font-weight: 400; letter-spacing: 0; text-transform: none;">1 command</span></figcaption>
<div style="padding: clamp(16px, 4vw, 24px); font: 14px/1.75 ui-monospace, SFMono-Regular, Consolas, monospace;">
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Place
You&#x27;re in the only place.

You can see a yummy fig here.</samp></pre>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">eat fig</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">That&#x27;s plainly inedible.</samp></pre>
</div>
</div>
</figure>

<!-- /inform-transcript: inedible-fig -->

Easy to remedy:

<!-- inform-example: edible-fig
title = "An edible fig"
kind = "alternative"
requires = ["the-place"]
instead_of = ["inedible-fig"]
explanation = "Replace the original fig declaration with the edible version."
commands = ["eat fig", "look fig"]
expect = ["You eat the yummy fig. Not bad."]
chapter_transcript = true
-->
```inform7
A yummy fig is here.  It is edible.
```
<!-- inform-transcript: edible-fig -->

<figure class="if-terminal" aria-label="Example gameplay transcript" style="margin: 24px 0; max-width: 100%; overflow: hidden; border: 1px solid #34494b; border-radius: 12px; background: #152326; color: #e5ede5; box-shadow: 0 6px 18px rgba(20, 31, 26, 0.12);">
<figcaption style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; padding: 12px 20px; border-bottom: 1px solid #34494b; background: #1d3032; color: #bdcfc4; font: 600 11px/1.5 ui-monospace, SFMono-Regular, Consolas, monospace; letter-spacing: 0.1em; text-transform: uppercase;"><span>Example play</span><span style="font-weight: 400; letter-spacing: 0; text-transform: none;">2 commands</span></figcaption>
<div style="padding: clamp(16px, 4vw, 24px); font: 14px/1.75 ui-monospace, SFMono-Regular, Consolas, monospace;">
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Place
You&#x27;re in the only place.

You can see a yummy fig here.</samp></pre>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">eat fig</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">(first taking the yummy fig)
You eat the yummy fig. Not bad.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">look fig</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">You can&#x27;t see any such thing.</samp></pre>
</div>
</div>
</figure>

<!-- /inform-transcript: edible-fig -->

### Things you can wear

Let's say we have a shirt.

<!-- inform-example: ordinary-shirt
title = "An ordinary shirt"
kind = "additive"
requires = ["the-place"]
explanation = "Start the shirt example before making it wearable."
commands = ["wear shirt"]
expect = ["You can't wear that!"]
chapter_transcript = true
-->
```inform7
There is a shirt in The Place.
```
Naturally someone is going to want to wear it.  
  
<!-- inform-transcript: ordinary-shirt -->

<figure class="if-terminal" aria-label="Example gameplay transcript" style="margin: 24px 0; max-width: 100%; overflow: hidden; border: 1px solid #34494b; border-radius: 12px; background: #152326; color: #e5ede5; box-shadow: 0 6px 18px rgba(20, 31, 26, 0.12);">
<figcaption style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; padding: 12px 20px; border-bottom: 1px solid #34494b; background: #1d3032; color: #bdcfc4; font: 600 11px/1.5 ui-monospace, SFMono-Regular, Consolas, monospace; letter-spacing: 0.1em; text-transform: uppercase;"><span>Example play</span><span style="font-weight: 400; letter-spacing: 0; text-transform: none;">1 command</span></figcaption>
<div style="padding: clamp(16px, 4vw, 24px); font: 14px/1.75 ui-monospace, SFMono-Regular, Consolas, monospace;">
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Place
You&#x27;re in the only place.

You can see a shirt here.</samp></pre>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">wear shirt</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">(first taking the shirt)
You can&#x27;t wear that!</samp></pre>
</div>
</div>
</figure>

<!-- /inform-transcript: ordinary-shirt -->

In Inform, something can be `wearable`.

<!-- inform-example: wearable-shirt
title = "A wearable shirt"
kind = "alternative"
requires = ["the-place"]
instead_of = ["ordinary-shirt"]
explanation = "Replace the shirt declaration with this wearable version."
commands = ["wear shirt", "inventory", "take off shirt", "inventory"]
expect = ["You put on the shirt."]
chapter_transcript = true
-->
```inform7
There is a shirt in The Place.
It is wearable.
```

<!-- inform-transcript: wearable-shirt -->

<figure class="if-terminal" aria-label="Example gameplay transcript" style="margin: 24px 0; max-width: 100%; overflow: hidden; border: 1px solid #34494b; border-radius: 12px; background: #152326; color: #e5ede5; box-shadow: 0 6px 18px rgba(20, 31, 26, 0.12);">
<figcaption style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; padding: 12px 20px; border-bottom: 1px solid #34494b; background: #1d3032; color: #bdcfc4; font: 600 11px/1.5 ui-monospace, SFMono-Regular, Consolas, monospace; letter-spacing: 0.1em; text-transform: uppercase;"><span>Example play</span><span style="font-weight: 400; letter-spacing: 0; text-transform: none;">4 commands</span></figcaption>
<div style="padding: clamp(16px, 4vw, 24px); font: 14px/1.75 ui-monospace, SFMono-Regular, Consolas, monospace;">
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Place
You&#x27;re in the only place.

You can see a shirt here.</samp></pre>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">wear shirt</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">(first taking the shirt)
You put on the shirt.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">inventory</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">You are carrying:
  a shirt (being worn)</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">take off shirt</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">You take off the shirt.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">inventory</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">You are carrying:
  a shirt</samp></pre>
</div>
</div>
</figure>

<!-- /inform-transcript: wearable-shirt -->

### Things you start out wearing (and holding) 

What if you want to have the player wearing things right from the start?

<!-- inform-example: wearing-pants
title = "Starting out wearing clothes"
kind = "additive"
requires = ["the-place"]
explanation = "Add clothing worn by the player at the beginning of play."
commands = ["inventory"]
expect = ["red pants (being worn)"]
chapter_transcript = true
-->
```inform7
The player wears red pants.
```

<!-- inform-transcript: wearing-pants -->

<figure class="if-terminal" aria-label="Example gameplay transcript" style="margin: 24px 0; max-width: 100%; overflow: hidden; border: 1px solid #34494b; border-radius: 12px; background: #152326; color: #e5ede5; box-shadow: 0 6px 18px rgba(20, 31, 26, 0.12);">
<figcaption style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; padding: 12px 20px; border-bottom: 1px solid #34494b; background: #1d3032; color: #bdcfc4; font: 600 11px/1.5 ui-monospace, SFMono-Regular, Consolas, monospace; letter-spacing: 0.1em; text-transform: uppercase;"><span>Example play</span><span style="font-weight: 400; letter-spacing: 0; text-transform: none;">1 command</span></figcaption>
<div style="padding: clamp(16px, 4vw, 24px); font: 14px/1.75 ui-monospace, SFMono-Regular, Consolas, monospace;">
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Place
You&#x27;re in the only place.</samp></pre>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">inventory</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">You are carrying:
  red pants (being worn)</samp></pre>
</div>
</div>
</figure>

<!-- /inform-transcript: wearing-pants -->

(Notice that we don't have to say the pants are `wearable`.)

We can also make the player start out with something that they're not wearing:

<!-- inform-example: carrying-toaster
title = "Starting out carrying things"
kind = "additive"
requires = ["wearing-pants"]
explanation = "Also add a carried object to the player who starts out wearing pants."
commands = ["inventory"]
expect = ["a toaster"]
-->
```inform7
The player carries a toaster.   
```

### Things you can put on other things



@TODO Explain supporters and putting things on them; contrast enterable supporters using GET ON, GET OFF, and ENTER (pp. 55–56).


### Things that contain other things

It's very possible you will want flasks, cages, boxes, bowls, pitchers, drawers, and treasure chests.  Inform makes this possible by making an object a `container`.  A container is a special kind of object that can hold unlimited things.  (Restricting what it holds requires extra programming.)

<!-- inform-example: ordinary-bowl
title = "An object that cannot contain things"
kind = "additive"
requires = ["the-place"]
explanation = "Start the bowl and figurine example before making the bowl a container."
commands = ["put figurine in bowl"]
expect = ["That can't contain things."]
chapter_transcript = true
-->
```inform7
There is a deep wooden bowl in The Place. 
There is a small carved monkey figurine in the Place.
```
<!-- inform-transcript: ordinary-bowl -->

<figure class="if-terminal" aria-label="Example gameplay transcript" style="margin: 24px 0; max-width: 100%; overflow: hidden; border: 1px solid #34494b; border-radius: 12px; background: #152326; color: #e5ede5; box-shadow: 0 6px 18px rgba(20, 31, 26, 0.12);">
<figcaption style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; padding: 12px 20px; border-bottom: 1px solid #34494b; background: #1d3032; color: #bdcfc4; font: 600 11px/1.5 ui-monospace, SFMono-Regular, Consolas, monospace; letter-spacing: 0.1em; text-transform: uppercase;"><span>Example play</span><span style="font-weight: 400; letter-spacing: 0; text-transform: none;">1 command</span></figcaption>
<div style="padding: clamp(16px, 4vw, 24px); font: 14px/1.75 ui-monospace, SFMono-Regular, Consolas, monospace;">
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Place
You&#x27;re in the only place.

You can see a deep wooden bowl and a small carved monkey figurine here.</samp></pre>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">put figurine in bowl</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">(first taking the small carved monkey figurine)
That can&#x27;t contain things.</samp></pre>
</div>
</div>
</figure>

<!-- /inform-transcript: ordinary-bowl -->

We can fix that:

<!-- inform-example: container-bowl
title = "A bowl as a container"
kind = "alternative"
requires = ["the-place"]
instead_of = ["ordinary-bowl"]
explanation = "Replace the original bowl and figurine block with a container version."
commands = ["put figurine in bowl", "look bowl", "take figurine", "look bowl"]
expect = ["The deep wooden bowl is empty."]
chapter_transcript = true
-->
```inform7
There is a deep wooden bowl in The Place. 
It is a container.
There is a small carved monkey figurine in the Place.
```
Now we get:

<!-- inform-transcript: container-bowl -->

<figure class="if-terminal" aria-label="Example gameplay transcript" style="margin: 24px 0; max-width: 100%; overflow: hidden; border: 1px solid #34494b; border-radius: 12px; background: #152326; color: #e5ede5; box-shadow: 0 6px 18px rgba(20, 31, 26, 0.12);">
<figcaption style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; padding: 12px 20px; border-bottom: 1px solid #34494b; background: #1d3032; color: #bdcfc4; font: 600 11px/1.5 ui-monospace, SFMono-Regular, Consolas, monospace; letter-spacing: 0.1em; text-transform: uppercase;"><span>Example play</span><span style="font-weight: 400; letter-spacing: 0; text-transform: none;">4 commands</span></figcaption>
<div style="padding: clamp(16px, 4vw, 24px); font: 14px/1.75 ui-monospace, SFMono-Regular, Consolas, monospace;">
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Place
You&#x27;re in the only place.

You can see a deep wooden bowl (empty) and a small carved monkey figurine here.</samp></pre>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">put figurine in bowl</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">(first taking the small carved monkey figurine)
You put the small carved monkey figurine into the deep wooden bowl.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">look bowl</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">In the deep wooden bowl is a small carved monkey figurine.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">take figurine</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Taken.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">look bowl</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">The deep wooden bowl is empty.</samp></pre>
</div>
</div>
</figure>

<!-- /inform-transcript: container-bowl -->

If we want something to start out inside a container, that's simple too:

<!-- inform-example: filled-bowl
title = "Starting inside a container"
kind = "alternative"
requires = ["the-place"]
instead_of = ["container-bowl"]
explanation = "Replace the bowl example so the figurine starts inside it."
commands = ["look bowl"]
expect = ["a small carved monkey figurine"]
chapter_transcript = true
-->
```inform7
There is a deep wooden bowl in The Place. 
It is a container.
There is a small carved monkey figurine in the bowl.
```

Now:

<!-- inform-transcript: filled-bowl -->

<figure class="if-terminal" aria-label="Example gameplay transcript" style="margin: 24px 0; max-width: 100%; overflow: hidden; border: 1px solid #34494b; border-radius: 12px; background: #152326; color: #e5ede5; box-shadow: 0 6px 18px rgba(20, 31, 26, 0.12);">
<figcaption style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; padding: 12px 20px; border-bottom: 1px solid #34494b; background: #1d3032; color: #bdcfc4; font: 600 11px/1.5 ui-monospace, SFMono-Regular, Consolas, monospace; letter-spacing: 0.1em; text-transform: uppercase;"><span>Example play</span><span style="font-weight: 400; letter-spacing: 0; text-transform: none;">1 command</span></figcaption>
<div style="padding: clamp(16px, 4vw, 24px); font: 14px/1.75 ui-monospace, SFMono-Regular, Consolas, monospace;">
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Place
You&#x27;re in the only place.

You can see a deep wooden bowl (in which is a small carved monkey figurine) here.</samp></pre>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">look bowl</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">In the deep wooden bowl is a small carved monkey figurine.</samp></pre>
</div>
</div>
</figure>

<!-- /inform-transcript: filled-bowl -->

### Containers that open and close
Lots of things that aren't containers can open and close (books, gates, tulips, hearts) but in Inform, *only containers can open and close* (without extra programming).

Containers, however, can can be `openable` or `unopenable`.  They're `unopenable` by default.

<!-- inform-example: openable-box
title = "Opening and closing a box"
kind = "additive"
requires = ["the-place"]
explanation = "Start a new jewelry box example in the starting room."
commands = ["close box", "look box", "open box", "look box"]
expect = ["revealing a necklace"]
chapter_transcript = true
-->
```inform7
There is a jewelry box in The Place.
The description is "It's a super fancy box.".
It is a container.  
It is openable.
There is a necklace in the box.
```
With that one small sentence, we get this:

<!-- inform-transcript: openable-box -->

<figure class="if-terminal" aria-label="Example gameplay transcript" style="margin: 24px 0; max-width: 100%; overflow: hidden; border: 1px solid #34494b; border-radius: 12px; background: #152326; color: #e5ede5; box-shadow: 0 6px 18px rgba(20, 31, 26, 0.12);">
<figcaption style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; padding: 12px 20px; border-bottom: 1px solid #34494b; background: #1d3032; color: #bdcfc4; font: 600 11px/1.5 ui-monospace, SFMono-Regular, Consolas, monospace; letter-spacing: 0.1em; text-transform: uppercase;"><span>Example play</span><span style="font-weight: 400; letter-spacing: 0; text-transform: none;">4 commands</span></figcaption>
<div style="padding: clamp(16px, 4vw, 24px); font: 14px/1.75 ui-monospace, SFMono-Regular, Consolas, monospace;">
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Place
You&#x27;re in the only place.

You can see a jewelry box (in which is a necklace) here.</samp></pre>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">close box</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">You close the jewelry box.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">look box</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">It&#x27;s a super fancy box.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">open box</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">You open the jewelry box, revealing a necklace.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">look box</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">It&#x27;s a super fancy box.

In the jewelry box is a necklace.</samp></pre>
</div>
</div>
</figure>

<!-- /inform-transcript: openable-box -->

As you can see, `openable` containers can be `open` or `closed`, and if you don't say they're `closed` they start out open.  We can have it either way:

<!-- inform-example: closed-box
title = "Starting with a closed box"
kind = "alternative"
requires = ["the-place"]
instead_of = ["openable-box"]
explanation = "A minimal closed-box variant; replaces the earlier box block and omits its necklace and custom description."
commands = ["look", "open box"]
expect = ["You open the jewelry box."]
-->
```inform7
There is a jewelry box in The Place.
It is a container.  
It is openable.
It is closed.
```

_{Shortcut}:_ You can combine all three descriptions:

<!-- inform-example: closed-box-shortcut
title = "Combining container properties"
kind = "alternative"
requires = ["the-place"]
instead_of = ["closed-box"]
explanation = "Equivalent compact spelling of the preceding closed-box declarations."
commands = ["look", "open box"]
expect = ["You open the jewelry box."]
-->
```inform7
There is a jewelry box in The Place.
It is a closed openable container.
```

### Containers you can see through

Containers, whether they are `openable` or `unopenable`, can be `transparent` or `opaque`, and they're `opaque` if you don't say otherwise.   There's really only one situation where `transparent` containers make a difference: 

You can see object inside a `closed`, `transparent` container.

<!-- inform-example: transparent-ball
title = "Seeing through a closed container"
kind = "additive"
requires = ["the-place"]
explanation = "A separate container example demonstrating visibility through a closed container."
commands = ["look hamster ball", "take plush hamster", "open ball", "take plush hamster"]
expect = ["The hamster ball isn't open."]
chapter_transcript = true
-->
```inform7
There is a hamster ball in The Place.
It is a closed openable transparent container.
There is a plush hamster in the ball.
```

<!-- inform-transcript: transparent-ball -->

<figure class="if-terminal" aria-label="Example gameplay transcript" style="margin: 24px 0; max-width: 100%; overflow: hidden; border: 1px solid #34494b; border-radius: 12px; background: #152326; color: #e5ede5; box-shadow: 0 6px 18px rgba(20, 31, 26, 0.12);">
<figcaption style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; padding: 12px 20px; border-bottom: 1px solid #34494b; background: #1d3032; color: #bdcfc4; font: 600 11px/1.5 ui-monospace, SFMono-Regular, Consolas, monospace; letter-spacing: 0.1em; text-transform: uppercase;"><span>Example play</span><span style="font-weight: 400; letter-spacing: 0; text-transform: none;">4 commands</span></figcaption>
<div style="padding: clamp(16px, 4vw, 24px); font: 14px/1.75 ui-monospace, SFMono-Regular, Consolas, monospace;">
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Place
You&#x27;re in the only place.

You can see a hamster ball (closed) (in which is a plush hamster) here.</samp></pre>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">look hamster ball</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">In the hamster ball is a plush hamster.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">take plush hamster</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">The hamster ball isn&#x27;t open.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">open ball</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">You open the hamster ball.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">take plush hamster</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Taken.</samp></pre>
</div>
</div>
</figure>

<!-- /inform-transcript: transparent-ball -->

## @TODO Remaining thing topics

- Things that can be switched on or off
- Things that make light
- On-stage and off-stage
