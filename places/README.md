# Inform 7: Making Places

People walk around in places in the real world.  The best way to help people feel like they're in a real world is to have some places for them to hang out in, walk around in, and look at.

## We Need a Place to Be

Let's make a room.  It's easy.

```inform7
The Featureless Room is a room.
The description of The Featureless Room is 
"You are in a room, that much you can tell.".
```

Run our program and we have a world we can interact with:

> **Featureless Room**  
> You are in a room, that much you can tell.
>
>**\>look**  
> **Featureless Room**  
> You are in a room, that much you can tell.
>
> **\>`walk north`**  
>You can't go that way.

See, so we just created a whole (very small) world with just three lines of English language text.  We say something `is a room` and Inform knows it's a place.  We give it a description, and Inform knows that's how to describe the room.

We didn't give the room any exits so Inform won't let the player leave.  By default, rooms have no exits.

_{Shortcut}:_ You can leave out the name of the room in the description as long as you put it right after naming the room.  Inform will know which room you're talking about as long as it's the last thing you mentioned:

```inform7
The Warehouse is a room.
The description is "Large and metal.".
[[Inform 7 knows you mean the The Warehouse.]]
```

### Every Place is a Room

Not every place in the world is a room.  There are caves, planets, wide-open fields, pits of despair, and pinnacles of jubilation.  

Even though not every place is a room, when you're making worlds in Inform, you call any place you can enter and leave `a room`.  

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

```inform7
The little clearing is a room.   
The description is "A little clearing in the forest.  There is a tree with a treehouse above you, and a small hole in the ground leading to a burrow."

The treehouse is a room above the little clearing.
The description is "Girls are allowed."
The little clearing is above the burrow in the ground. 
[[When you use north and south you can just specify one of the rooms is north and the other room with know it's south.  With "above" and "below" you have to specify both.]]

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

```inform7
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

```inform7
Understand "brushstrokes" as the painting.
```

This is an improvement:

> **\>`look at brushstrokes`**  
> The painting is abstract with bold red and blue brushstrokes.

## TO DO: Reminders to myself:
- scenery vs backgrounds
- regions vs "everywhere"

