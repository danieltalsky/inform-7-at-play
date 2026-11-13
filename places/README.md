# Inform 7: Making Places

People walk around in places in the real world.  The best way to help people feel like they're in a real world is to have some places for them to hang out in, walk around in, and look at.

## We Need a Place to Be

Let's make a room.  It's easy.

<!-- inform-example: featureless-room
title = "A room with no exits"
kind = "standalone"
explanation = "The first complete world in this chapter."
commands = ["look", "walk north"]
expect = ["You are in a room, that much you can tell.", "You can't go that way."]
chapter_transcript = true
-->
```inform7
The Featureless Room is a room.
The description of The Featureless Room is 
"You are in a room, that much you can tell.".
```

Run our program and we have a world we can interact with:

<!-- inform-transcript: featureless-room -->

<figure class="if-terminal" aria-label="Example gameplay transcript" style="margin: 24px 0; max-width: 100%; overflow: hidden; border: 1px solid #34494b; border-radius: 12px; background: #152326; color: #e5ede5; box-shadow: 0 6px 18px rgba(20, 31, 26, 0.12);">
<figcaption style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; padding: 12px 20px; border-bottom: 1px solid #34494b; background: #1d3032; color: #bdcfc4; font: 600 11px/1.5 ui-monospace, SFMono-Regular, Consolas, monospace; letter-spacing: 0.1em; text-transform: uppercase;"><span>Example play</span><span style="font-weight: 400; letter-spacing: 0; text-transform: none;">2 commands</span></figcaption>
<div style="padding: clamp(16px, 4vw, 24px); font: 14px/1.75 ui-monospace, SFMono-Regular, Consolas, monospace;">
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Featureless Room
You are in a room, that much you can tell.</samp></pre>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">look</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">Featureless Room
You are in a room, that much you can tell.</samp></pre>
</div>
<div style="margin-top: 22px;">
<div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px; color: #d1ef9f; font: inherit;"><span aria-hidden="true" style="color: #8dbba3;">&gt;</span><kbd style="padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; box-shadow: none; font: inherit; font-weight: 700; white-space: pre-wrap; overflow-wrap: anywhere; min-width: 0;">walk north</kbd></div>
<pre style="margin: 0; padding: 0; border: 0; border-radius: 0; background: transparent; color: inherit; font: inherit; white-space: pre-wrap; overflow-wrap: anywhere;"><samp style="color: inherit; font: inherit;">You can&#x27;t go that way.</samp></pre>
</div>
</div>
</figure>

<!-- /inform-transcript: featureless-room -->

See, so we just created a whole (very small) world with just three lines of English language text.  We say something `is a room` and Inform knows it's a place.  We give it a description, and Inform knows that's how to describe the room.

We didn't give the room any exits so Inform won't let the player leave.  By default, rooms have no exits.

_{Shortcut}:_ You can leave out the name of the room in the description as long as you put it right after naming the room.  Inform will know which room you're talking about as long as it's the last thing you mentioned:

<!-- inform-example: warehouse
title = "The last-mentioned room"
kind = "standalone"
explanation = "A separate complete room demonstrating the description shorthand."
commands = ["look"]
expect = ["Large and metal."]
-->
```inform7
The Warehouse is a room.
The description is "Large and metal.".
[[Inform 7 knows you mean the The Warehouse.]]
```

### Every Place is a Room

Not every place in the world is a room.  There are caves, planets, wide-open fields, pits of despair, and pinnacles of jubilation.  

Even though not every place is a room, when you're making worlds in Inform, you call any place you can enter and leave `a room`.  

<!-- inform-example: imaginary-places
title = "Every place is a room"
kind = "standalone"
explanation = "A fresh collection of rooms illustrating what counts as a room."
commands = ["look"]
expect = ["Your boat is tossed to and fro."]
-->
```inform7
The center of the wild sea is a room.
The description of the sea is "Your boat is tossed to and fro.".

The dark void of space is a room.
The description of space is "There isn't even any air".

Easter Island is a room.
The description is "There are statues.  Do they have legs?".

The computer simulation is a room.
The description is "It's like the matrix in here."

The inside of a giant log is a room.
The description is "Cylindrical and quite mossy."
```

Any place you can imagine needs to be `a room` for Inform to understand that it is a place and not a thing or an action.

## Going Places

When you're telling interactive stories, it helps people understand the space around them if they can move around.

### Due North

Inform has the idea of compass directions built in.  It knows north and south and east and west.  It knows southwest, etc.

You can do this to give two rooms a relationship with each other:

<!-- inform-example: north-and-south
title = "Moving between rooms"
kind = "standalone"
explanation = "Both rooms and their connection are defined here."
commands = ["north", "south", "north"]
expect = ["You can't go that way.", "Southern Tip of the Island", "A very rocky place.", "A very sandy place."]
-->
```inform7
The Northern Tip of the Island is a room.
The description is "A very rocky place.".

The Southern Tip of the Island is a room.
The description is "A very sandy place.".
The Southern Tip is south of The Northern Tip.
```

Now you can move around:

> **Northern Tip of the Island**  
> A very rocky place.  
>
> **\>`north`**  
> You can't go that way.  
>
> **\>`south`**  
>
> **Southern Tip of the Island**  
> A very sandy place

### Up and Down

The compass directions let you go in eight different directions from any location, but you have two more directions you can use.  Just like in the real world you can also go up or down, like this.

<!-- inform-example: up-and-down
title = "Above and below"
kind = "standalone"
explanation = "Starts a new clearing, treehouse, and burrow example."
commands = ["up", "down", "down", "up"]
expect = ["You can just barely fit down here."]
-->
```inform7
The little clearing is a room.   
The description is "A little clearing in the forest.  There is a tree with a treehouse above you, and a small hole in the ground leading to a burrow."

The treehouse is a room above the little clearing.
The description is "Girls are allowed."
The little clearing is above the burrow in the ground. 
[[Above and below are reciprocal, just like north and south. The reverse connections below are explicit but not required.]]

The burrow in the ground is a room below the little clearing.
The description is "You can just barely fit down here."
The little clearing is below the treehouse.
```

> **little clearing** 
> A little clearing in the forest.  There is a tree with a treehouse above you, and a small hole in the ground leading to a burrow.
> 
> **\>`up`**
> 
> **treehouse** 
> Girls are allowed.
> 
> **\>`down`**
> 
> **little clearing**  
> A little clearing in the forest.  There is a tree with a treehouse above you, and a small hole in the ground leading to a burrow.
> 
> **\>`down`**
> 
> **burrow in the ground**  
> You can just barely fit down here

### In and Out

There's one more way Inform lets you move between rooms, and that's `in` and `out`.  A room can be `inside` or `outside` another room like this:

<!-- inform-example: in-and-out
title = "Inside and outside"
kind = "standalone"
explanation = "Both the mudroom and kennel are defined here."
commands = ["in", "out"]
expect = ["It's uncomfortable in here and you feel silly."]
-->
```inform7
The mudroom is a room.
The description is "The mudroom is actually very muddy. There is a large dog kennel on the floor that you could probably fit inside."

The dog kennel is a room.  
The dog kennel is inside from the mudroom.
[[It doesn't work to say:
"The dog kennel is a room inside the mudroom." because Inform gets confused, so you need to write it this way.]]
The description is "It's uncomfortable in here and you feel silly."
```

This will allow:

> **mudroom**  
> The mudroom is actually very muddy.  There is a large dog kennel on the floor that you could probably fit inside.
> 
> **\>`in`**  
> 
> **dog kennel**   
> It's uncomfortable in here and you feel silly.
> 
> **\>`out`**  
> 
> **mudroom**  
> The mudroom is actually very muddy.  There is a large dog kennel on the floor that you could probably fit inside.

## Enjoy the Scenery

Now you know how to let people walk around your worlds, but walking around gets boring if there's nothing to see.  You can make your world much more convincing if people can look at specific things for more detail in your rooms.

Consider this room:

<!-- inform-example: gallery-description
title = "A description does not create scenery"
kind = "standalone"
explanation = "Starts the gallery example before any scenery is defined."
commands = ["look at sculpture", "look at painting"]
expect = ["You can't see any such thing."]
-->
```inform7
The art gallery is a room.
The description is "This is not the most impressive art gallery you've ever seen.  It only has two pieces of art, a sculpture on a pedestal and a painting hung on the wall."
```

That creates this situation:

> **art gallery**  
> This is not the most impressive art gallery you've ever seen.  It only has two pieces of art, a sculpture on a pedestal and a painting hung on the wall.
> 
> **\>`look at sculpture`**  
> You can't see any such thing.
> 
> **\>`look at painting`**  
> You can't see any such thing

That's not very convincing, and it's actually pretty confusing.  Inform doesn't know about things just because you talk about them in your description.  You have to "make" them just like rooms.  It's pretty simple, however, just add this:

<!-- inform-example: gallery-scenery
title = "Adding scenery"
kind = "additive"
requires = ["gallery-description"]
explanation = "Add these scenery declarations to the gallery above."
commands = ["look at sculpture", "look at painting", "look at pedestal"]
expect = ["You see nothing special about the sculpture."]
-->
```inform7
The sculpture is scenery in the art gallery.
The painting is scenery in the art gallery.
```

Now we get this:

> **\>`look at sculpture`**  
> You see nothing special about the sculpture.
> 
> **\>`look at painting`**  
> You see nothing special about the painting.
>
> **\>`look at pedestal`**  
>You can't see any such thing

Whoops.  That's a little better, but if we're willing to put in the work we can make our world richer and more consistent.  We can describe everything someone might look at (within reason).  Scenery can have a description just like a room.  Let's put it all together:

<!-- inform-example: gallery-details
title = "Describing scenery"
kind = "alternative"
instead_of = ["gallery-description", "gallery-scenery"]
explanation = "A complete consolidated gallery; replaces the earlier room and scenery blocks."
commands = ["look at sculpture", "look at painting", "look at pedestal", "look at brushstrokes"]
expect = ["A very boring grey pedestal."]
-->
```inform7
The art gallery is a room.
The description is "This is not the most impressive art gallery you've ever seen.  It only has two pieces of art, a sculpture on a pedestal and a painting hung on the wall."

The sculpture is scenery in the art gallery.
The description is "It's a sculpture of a Gordian Knot made out of marble."

The painting is scenery in the art gallery.
The description is "The painting is abstract with bold red and blue brushstrokes."

The pedestal is scenery in the art gallery.
The description is "A very boring grey pedestal."
```

Now you have a much more convincing place:

> **art gallery**  
> This is not the most impressive art gallery you've ever seen.  It only has two pieces of art, a sculpture on a pedestal and a painting hung on the wall.
> 
> **\>`look at sculpture`**  
It's a sculpture of a Gordian Knot made out of marble.
> 
> **\>`look at painting`**  
> The painting is abstract with bold red and blue brushstrokes.
>
> **\>`look at pedestal`**  
> A very boring grey pedestal.
> 
> **\>`look at brushstrokes`**  
> You can't see any such thing

Whoops.  You have to decide how detailed you want to get describing every little thing, but there's a quick trick that helps.  You can add:

<!-- inform-example: gallery-alias
title = "An alias for brushstrokes"
kind = "additive"
requires = ["gallery-details"]
explanation = "Add parser vocabulary to the fully described painting."
commands = ["look at brushstrokes"]
expect = ["The painting is abstract with bold red and blue brushstrokes."]
-->
```inform7
Understand "brushstrokes" as the painting.
```

This is an improvement:

> **\>`look at brushstrokes`**  
> The painting is abstract with bold red and blue brushstrokes.

## @TODO Remaining place topics
- scenery vs backgrounds
- regions vs "everywhere"

