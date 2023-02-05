# Inform 7: Setting Up Your World

There are lots of cool things you can do to make your world unique and help your players feel comfortable.

Let's start with the smallest Inform world you can create.  It looks something like this:

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

```inform7
The story headline is "An unreal place you can walk around in"
```

Now it will say:

> **A Fictional World I Created**  
> An unreal place you can walk around in by The World's Most Interesting Person

## Look at yourself

Sometimes the player might try this:

>\>**`look self`**  
> As good-looking as ever

You can make your own custom response.

```inform7
The description of the player is "You are a weird alien with tentacles instead of arms.".
```

And now:

>\>**`look self`**  
> You are a weird alien with tentacles instead of arms.