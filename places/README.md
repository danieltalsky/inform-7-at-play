# Inform 7: Making Places

People walk around in places in the real world.  The best way to help people feel like they're in a real world is to have some places for them to hang out in, walk around in, and look at.

## Everything is a room

Let's make a room.

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
>
> **\>jump**  
> You jump on the spot

See, so we just created a whole (very small) world with just three lines of English language text.  We say something is a room and Inform knows it's a place.  We give it a description, and Inform knows that's how to describe the room.

We didn't give the room any exits so Inform won't let the player leave.  We can jump, though, because jumping is one of the built-in things Inform understands.

_{Shortcut}:_ this is the syntax for a shortcut for my own reference: