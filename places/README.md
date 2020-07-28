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
> **\>walk north**  
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

### Due North

When you're telling interactive stories, it helps people understand the space around them if they can move around.

Inform has the idea of compass directions built in.  It knows north and south and east and west.  It knows southwest, etc.

You can do this:

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
> **\>north**  
> You can't go that way.  
>
> **\>south**  
>
> **Southern Tip of the Island**  
> A very sandy place

## @TODO up and down
## @TODO 
## @TODO scenery
## @TODO grouped areas
