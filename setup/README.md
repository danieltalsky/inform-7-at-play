# Setting Up Your World

There are lots of cool things you can do to make your world unique and help your players feel comfortable.

Let's start with the smallest Inform world you can create.  It looks something like this:

<!-- inform-example: tiny-world
title = "The smallest world"
kind = "standalone"
explanation = "A complete title and starting room."
commands = ["look"]
expect = ["boring place"]
-->
```inform7
"An Extremely Boring and Tiny World"
[[The title of the game]]

The boring place is a room.
[[A single place you can start.]]
```

> **An Extremely Boring and Tiny World**  
> An Interactive Fiction  
> Release 1 / Serial number 230205 / Inform 7 build 6M62 (I6/v6.34 lib 6/12N) SD
>
> **boring place**  
>
> \>

## Who are you?

One piece of information you can add is your name, or a nom de plume.

<!-- inform-example: story-author
title = "Adding an author"
kind = "alternative"
instead_of = ["tiny-world"]
explanation = "Replace only the title line of tiny-world; context retains its starting room."
context = "The boring place is a room."
commands = []
expect = ["by The World's Most Interesting Person"]
-->
```inform7
"A Fictional World I Created" by The World's Most Interesting Person

```

This will give you:

> **A Fictional World I Created**  
> An Interactive Fiction by The World's Most Interesting Person

Now people will know who you are.

## How did I get here?

Sometimes it helps to add a little introduction, to orient the player and let them know why they're in your world and what to expect right off the bat before you describe your first room.

Just add:

<!-- inform-example: opening-introduction
title = "An opening introduction"
kind = "additive"
requires = ["story-author"]
explanation = "Add the introduction to the authored story, retaining its room."
commands = ["look"]
expect = ["You probably shouldn't have pressed that button"]
-->
```inform7
When play begins, say 
"You're in an imaginary world.  You probably shouldn't have pressed that button that said 'Teleport me to an imaginary world.'  Now you've done it.".
```

Now you get:

> You're in an imaginary world.  You probably shouldn't have pressed that button that said "Teleport me to an imaginary world."  Now you've done it.
>
> **A Fictional World I Created**  
> An Interactive Fiction by The World's Most Interesting Person
> Release 1 / Serial number 230205 / Inform 7 build 6M62 (I6/v6.34 lib 6/12N) SD
>
> **nappy dugout**  
>
> \>

## An interactive fiction?

By default Inform will introduce your story after the title as:

> **A Fictional World I Created**  
> An Interactive Fiction by The World's Most Interesting Person

If you don't want it to say that, you can come up with your own:

<!-- inform-example: story-headline
title = "A custom headline"
kind = "additive"
requires = ["story-author"]
explanation = "Add a custom headline to the authored story; the introduction is independent and omitted here."
commands = []
expect = ["An unreal place you can walk around in"]
-->
```inform7
The story headline is "An unreal place you can walk around in"
```

Now it will say:

> **A Fictional World I Created**  
> An unreal place you can walk around in by The World's Most Interesting Person

## Improving the defaults

Inform has a lot of good default messages for trying things.  

You can make your own messages that give your interactive story your own unique
flavor.  Some examples:

### Looking at yourself

Sometimes the player might try this:

>\>**`look self`**  
> As good-looking as ever

You can make your own custom response.

<!-- inform-example: player-description
title = "Describing the player"
kind = "additive"
requires = ["tiny-world"]
explanation = "Add a player description to the minimal runnable world."
commands = ["look self"]
expect = ["You are a weird alien with tentacles instead of arms."]
-->
```inform7
The description of the player is "You are a weird alien with tentacles instead of arms.".
```

And now:

>\>**`look self`**  
> You are a weird alien with tentacles instead of arms.

### Looking at things that don't have a description

<!-- inform-example: undescribed-stone
title = "The default object description"
kind = "standalone"
explanation = "Starts a fresh field and stone example."
commands = ["look stone"]
expect = ["You see nothing special about the dry stone."]
-->
```inform7
The field is a room.
There is a dry stone in the field.
```

>\>**`look stone`**  
>You see nothing special about the dry stone.

We can do better than that, right?  Here's how to say something else:

<!-- inform-example: default-description
title = "Changing the default description"
kind = "additive"
requires = ["undescribed-stone"]
explanation = "Add a default object description to the existing stone example."
commands = ["look stone"]
expect = ["You look at the dry stone very closely indeed"]
-->
```inform7
The description of a thing is usually "You look at [the noun] very closely indeed, and to be completely honest, it looks about how you'd expect. You think for a moment that there might be something slightly special about it but then, upon looking just a little closer, you see that there isn't."
```

Now we get:

>\>**`look stone`**  
>You look at the dry stone very closely indeed, and to be completely honest, it looks about how you'd expect. You think for a moment that there might be something slightly special about it but then, upon looking just a little closer, you see that there isn't.

### Looking at your empty inventory

Normally when you check your inventory you get a boring message like this:

>\>**`inventory`**  
>You are carrying nothing.

Overriding this message requires some special Inform 7 magic with this odd-looking command:

<!-- inform-example: empty-inventory
title = "Changing the empty inventory message"
kind = "additive"
requires = ["tiny-world"]
explanation = "Add a response override to a minimal world with no carried objects."
commands = ["inventory"]
expect = ["You look everywhere but finally come to realize that you have no possessions."]
-->
```inform7
The print empty inventory rule response (A) is "You look everywhere but finally come to realize that you have no possessions."
```

Now:

>\>**`inventory`**  
>You look everywhere but finally come to realize that you have no possessions.

## Making `use` useful

By default, the verb `use` isn't something Inform understands.  You can set
up some rules to make life easier for players.

<!-- inform-example: garage
title = "Use is not a built-in verb"
kind = "standalone"
explanation = "Starts a complete garage example with three objects to use."
commands = ["use cage", "use switch", "use candy"]
expect = ["That's not a verb I recognise."]
-->
```inform7
The garage is a room.  

There is a bird cage in the garage. 
The cage is an closed openable container.  

There is a disconnected light switch in the garage.
The switch is a switched off device.

There is a peanut candy in the garage.
The candy is edible.
```

Let's see how use works by default:

>**garage**  
>You can see a bird cage (closed), a disconnected light switch and a peanut candy here.
>
>\>**`use cage`**  
>That's not a verb I recognise.
>
>\>**`use switch`**  
>That's not a verb I recognise.
>
>\>**`use candy`**  
>That's not a verb I recognise.

We can do better by setting up some default rules for using things.

<!-- inform-example: use-command
title = "Making use useful"
kind = "additive"
requires = ["garage"]
explanation = "Add grammar to the garage example so use selects the appropriate built-in action."
commands = ["use cage", "use cage", "use switch", "use switch", "use candy"]
expect = ["You eat the peanut candy. Not bad."]
-->
```inform7
Understand "use [a closed openable thing]" as opening.
Understand "use [a open openable thing]" as closing.
Understand "use [a switched off device]" as switching on.
Understand "use [a switched on device]" as switching off.
Understand "use [an edible thing]" as eating.
```

Now things work a little better:

>\>**`use cage`**  
>You open the bird cage.
>
>\>**`use switch`**  
>You switch the disconnected light switch on.
>
>\>**`use switch`**  
You switch the disconnected light switch off.
>
>\>**`use candy`**  
>(first taking the peanut candy)  
>You eat the peanut candy. Not bad.
