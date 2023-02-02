# Inform 7: All About Things

Your imaginary worlds in Inform 7 are almost inevitably going to have things in them.  The real world has things, and people expect them.  Let's not disappoint them.  

## A place to put things
First let's make a place to put our things in, because Inform needs a place for our things to be in with us.

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

```inform7
There is a red ball in The Place.
There is a green ball in The Place.
There is a hammer in The Place.
```
_{Shortcut}:_ or we can use a shortcut using the keyword "here" to mean the last place we talked about:

```inform7
There is a hammer here.
```
Run our program and we have a world we can interact with:
>**Place**  
>You can see a red ball, a green ball, and a hammer here  
>  
>\>**`look at the ball`**  
>Which do you mean, the red ball or the green ball?  
>  
>\>**`green`**  
>You see nothing special about the green ball  
>
>\>**`get hammer`**  
>Taken.  
>  
> \>**`inventory`**  
>You are carrying:  
> &nbsp;&nbsp;&nbsp;&nbsp; a hammer  
>  
>\>**`look`**  
>  
>**Place**  
>You're in the only place.  
>  
> You can see a red ball and a green ball here.  

## Things you can look at

Inform prints room descriptions automatically, and then lists the things in the room.  It only lists the names of the things, along with their adjectives.  It doesn't know the difference between a ball and a hammer, so it just uses a stock message: "You see nothing special about [the noun]."

### Describing things when you look at them
Just like our description of the room, let's make our red ball a little more interesting.

```inform7
The description of the red ball is 
"It's spherical, red, and radiates a very spooky energy.".
```
*{shortcut}* or, we can use a shorthand for the last thing we mentioned by cutting out the name of the thing:

```inform7
There is a red ball in The Place.
The description is 
"It's spherical, red, and radiates a very spooky energy.".
```
### Things with lots of names
Let's say we want a television in our game:

```inform7
There is a television in The Place.
The description is "It's playing ESPN 8, the Ocho.".
```
> You can see a television here.  
>  
>\>**`look tv`**  
>You can't see any such thing  

Humans know that TV, teevee, telly, and idiot box all mean television, but Inform doesn't.  There's an easy way to tell it, though:

```inform7
Understand "TV" as television.
Understand "telly" as television.
Understand "idiot box" as television.
```
Now:

> You can see a television here.  
>
>\>**`look tv`**  
> It's playing ESPN 8, the Ocho.  
>  
>\>**`look telly`**  
>It's playing ESPN 8, the Ocho.  
>  
>\>**`look idiot box`**  
>It's playing ESPN 8, the Ocho  

*{shortcut}* instead of multiple "understand" statements, we can combine them like this:
```inform7
Understand "TV" or "telly" or "idiot box" as television.
```
You can also go even shorter by doing this trick:

```inform7
Understand "TV/telly/teevee" as television.
```
An important exception though, this doesn't work:

```inform7
Understand "TV/idiot box" as television.
```
Why?  It thinks you mean:
@TODO add exception for "tv/idiot box"

```inform7
Understand "TV box" or "idiot box" as television.
```

There's another reason we'd want to use this technique.  Consider this:

```inform7
There is a rotted log here.  
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
Sometimes it's great to go into all this detail, but sometimes when you have a whole forest to fill up, and you want your game to respond to "look at the lichens" you can do this:

```inform7
Understand "moss/mosses/lichen/lichens/mushroom/mushrooms/knot/knots/hole/holes/woodpecker" or "woodpecker holes" as the log.
```
It's a nicer effect to have each individual thing described, using parts, but it's better than nothing to just add an `understand` statement so the game says this as little as possible when people are trying to look deeper into the descriptions of your game:

>You can't see any such thing

### Things with ONLY aliases
@ TODO: Should I do `privately-named`?

### Things with special names (printed and proper)

There are some special cases when naming things that we should get into now, so you'll know when you need them.   So, we've already shown that you can add adjectives and clauses to item names like this:

```inform7
There is a gaudy rainbow statue of Teddy Roosevelt in The Place.
The description is "It sure is ugly.".
```


## Things you can't take

By default, the player can pick up any objects you create.  But sometimes, it doesn't make sense.

### Things you can't take

```inform7
There is an anvil bolted into the ground in The Place.  
The description is 
"The anvil is bolted into the ground for real."
```
>\>**`take anvil`**  
>Taken  

Damn.  That's because objects in Inform can be `portable` or `fixed in place`.  By default, they're portable.  Let's put a stop to that.

```inform7
There is an anvil bolted into the ground in The Place.  
It is fixed in place.  
The description is 
"The anvil is bolted into the ground for real.".
```
>\>**`take anvil`**  
>That's fixed in place.  

That'll show 'em.

### Things that are parts of other things
If we describe things, people are going to want to know more about them.  Like this hammer:

```inform7
There is a hammer in The Place.  
The description is 
"It's an OK hammer but it has a solid gold handle."
```
>\>**`look at handle`**  
>You can't see any such thing  

Not what we want.  Luckily there's an easy way to fix it.

```inform7
There is a hammer in The Place.  
The description is 
"It's an OK hammer but it has a solid gold handle.".  
There is a handle in The Place.  
The description is 
"It's made of solid gold.".
```
>**Place**  
>You're in the only place.  There are bushes.  
>  
>You can see a hammer and a handle here  
>  
>\>**`take handle`**  
>Taken.  

Well that's not right either.    The handle is listed separately and we can take it.  Here's how we prevent that in Inform:

```inform7
There is a hammer in The Place.  
The description is "It definitely has a handle."
The handle is a part of the hammer.  
```
> **Place**  
>You're in the only place.  There are bushes.  
>  
>You can see a hammer here.  
>  
>**`look hammer`**  
>It definitely has a handle.  
>  
>**`look handle`**  
>You see nothing special about the handle.  
>  
>**`take handle`**  
>That seems to be a part of the hammer  

Perfect.  Now it doesn't list the hammer or let us take it, but it knows the handle exists.  Not only that but parts can have parts.

```inform7
There is a ceramic dragon in The Place.
The description is "The ceramic dragon is wicked.  It has scales, a tail, and legs with feet and the feet have long claws." 
The scales are a part of the dragon.
The legs are a part of the dragon.
The feet are a part of the legs.
The claws are a part of the feet.  
```
Remember, though, most of the time we want to decide how detailed we get.    We want to balance where we put our effort.  In most cases we can do it with aliases:

```inform7
There is a ceramic dragon in The Place.
The description is "The ceramic dragon is wicked.  It has scales, a tail, and legs with feet and the feet have long claws." 
Understand "scales/legs/leg/feet/claws" as the dragon. 
```
Someone can't look at each individual thing this way, but at least the game won't say they don't exist.

### Things in the background

Let's add a little bit of background ambience to our otherwise very generic place:

```inform7
The description is "You're in the only place, and you can see beautiful rolling hills and the fluffiest of clouds."
There are rolling hills in the place.
They are fixed in place.
There are clouds in the place.
They are fixed in place.
```
>**Place**  
> You're in the only place, and you can see beautiful rolling hills and the fluffiest of clouds.  
>  
>You can see rolling hills and clouds here  

That's pretty good, but since we made the rolling hills and clouds a part of our description, we don't need them described again.  Just like items can be `portable` or `fixed in place`, they can also be `described` or `undescribed`.  Things are `described` by default.

So let's try this:

```inform7
The description is "You're in the only place, and you can see beautiful rolling hills and the fluffiest of clouds."
There are rolling hills in the place.
They are fixed in place.  They are undescribed.
There are clouds in the place.
They are fixed in place.  They are undescribed.
```
>**Place**  
> You're in the only place, and you can see beautiful rolling hills and the fluffiest of clouds.  

Much better.  Having background things that are in the description is common, so there is a shortcut for `fixed in place` and `undescribed` at the same time.  

_{Shortcut}:_ Some things can be combined in the same sentence, so we can do this:

```inform7
There are clouds in The Place.
They are fixed in place and undescribed.
```
_{Shortcut}:_ For this combination there is an even better shortcut:

```inform7
There are clouds in The Place.
They are scenery.
```

Since having background items that are both `fixed in place` and `undescribed` is so common, we just call them `scenery`.  You'll use scenery a lot.  So here's our new, streamlined description:

```inform7
The description is "You're in the only place, and you can see beautiful rolling hills and the fluffiest of clouds."
There are rolling hills in the place. They are scenery.
The description is "They roll on forever.".
There are clouds in the place. They are scenery.
The description is "You have never seen fluffier.".
```
### @TODO Should I do backdrops?


## Things you can do stuff to

We're making interactive fiction, not just "things you can pick up and look at", so we want to be able to do stuff to our things!  Inform builds in a lot of common helpers to make things act in a more realistic way.  

There aren't many of these built in to Inform.  It has `wearable` things, `edible` things and things that can be a `container`.

### Things that you can eat

One of the simplest is that things can be `edible` or `inedible` and obviously are `inedible` by default.

```inform7
There is a yummy fig here.
```
I love figs!  

You can see a yummy fig here.

>\>**`eat fig`**  
>That's plainly inedible  

Easy to remedy:

```inform7
There is a yummy fig here.  It is edible.
```
> You can see a yummy fig here.  
>  
>\>**`eat fig`**  
>(first taking the yummy fig)  
>You eat the yummy fig. Not bad.  
>  
>\>**`look fig`**   
>You can't see any such thing  

### Things you can wear

Let's say we have a shirt.

```inform7
There is a shirt in The Place.
```
Naturally someone is going to want to wear it.  
  
> You can see a shirt here.  
>  
>\>**`wear shirt`**  
>(first taking the shirt)  
>You can't wear that  

In Inform, something can be `wearable`.

```inform7
There is a shirt in The Place.
It is wearable.
```

> You can see a shirt here.    
>  
>\>**`wear shirt`**  
>(first taking the shirt)  
>You put on the shirt.  
>  
>\>**`inventory`**  
>You are carrying:  
>&nbsp;&nbsp;&nbsp;&nbsp;a shirt (being worn)  
>  
>\>**`take off shirt`**  
>You take off the shirt.  
>
>\>**`inventory`**  
>You are carrying:  
>&nbsp;&nbsp;&nbsp;&nbsp;a shirt  

### Things you start out wearing (and holding) 

What if you want to have the player wearing things right from the start?

```inform7
The player wears red pants.
```

>\>**`inventory`**  
>You are carrying:  
>&nbsp;&nbsp;&nbsp;&nbsp;red pants (being worn)

(Notice that we don't have to say the pants are `wearable`.)

We can also make the player start out with something that they're not wearing:

```inform7
The player carries a toaster.   
```

### Things you can put on other things



@TODO: Supporters: on vs. not.  Enterable vs. not.  p55-56 
the GET ON, GET OFF, ENTER, etc. syntax


### Things that contain other things

It's very possible you will want flasks, cages, boxes, bowls, pitchers, drawers, and treasure chests.  Inform makes this possible by making an object a `container`.  A container is a special kind of object that can hold unlimited things.  (Restricting what it holds requires extra programming.)

```inform7
There is a deep wooden bowl in The Place. 
There is a small carved monkey figurine in the Place.
```
> You can see a deep wooden bowl and a small carved monkey figurine here.  
>   
>\>**`put the figurine in the bowl`**  
>(first taking the small carved monkey figurine)  
>That can't contain things  

We can fix that:

```inform7
There is a deep wooden bowl in The Place. 
It is a container.
There is a small carved monkey figurine in the Place.
```
Now we get:
>You can see a deep wooden bowl (empty) and a small carved monkey figurine here.  
>  
>**put the figurine in the bowl**  
>(first taking the small carved monkey figurine)  
>You put the small carved monkey figurine into the deep wooden bowl.  
>  
>\>**`look bowl`**  
>In the deep wooden bowl is a small carved monkey figurine  
>  
>\>**`take the figurine`**  
>Taken.  
>  
>\>**`look bowl`**  
>The deep wooden bowl is empty  

If we want something to start out inside a container, that's simple too:

```inform7
There is a deep wooden bowl in The Place. 
It is a container.
There is a small carved monkey figurine in the bowl.
```

Now:

> You can see a deep wooden bowl (in which is a small carved monkey figurine) here.

### Containers that open and close
Lots of things that aren't containers can open and close (books, gates, tulips, hearts) but in Inform, *only containers can open and close* (without extra programming).

Containers, however, can can be `openable` or `unopenable`.  They're `unopenable` by default.

```inform7
There is a jewelry box in The Place.
The description is "It's a super fancy box.".
It is a container.  
It is openable.
There is a necklace in the box.
```
With that one small sentence, we get this:

>You can see a jewelry box (in which is a gentle necklace) here.  
>  
>\>**`close box`**  
>You close the jewelry box.  
>  
>\>**`look box`**  
>It's a super fancy box.  
>  
>\>**`open box`**  
>You open the jewelry box, revealing a gentle necklace.  
>  
>\>**`look box`**  
>It's a super fancy box.  
>  
>In the jewelry box is a gentle necklace  

As you can see, `openable` containers can be `open` or `closed`, and if you don't say they're `closed` they start out open.  We can have it either way:

```inform7
There is a jewelry box in The Place.
It is a container.  
It is openable.
It is closed.
```

_{Shortcut}:_ You can combine all three descriptions:

```inform7
There is a jewelry box in The Place.
It is a closed openable container.
```

### Containers you can see through

Containers, whether they are `openable` or `unopenable`, can be `transparent` or `opaque`, and they're `opaque` if you don't say otherwise.   There's really only one situation where `transparent` containers make a difference: 

You can see object inside a `closed`, `transparent` container.

```inform7
There is a hamster ball in The Place.
It is a closed openable transparent container.
There is a plush hamster in the ball.
```

>\>**`look hamster ball`**  
>In the hamster ball is a plush hamster  

### Things that can be switched on or off
@TODO
### Things that make light
@TODO
### On-stage and off-stage
@TODO
