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

### Every Place is a Room



_{Shortcut}:_ this is the syntax for a shortcut for my own reference:

```inform7
The Featureless Room is a room.
The description of The Featureless Room is 
"You are in a room, that much you can tell.".
```

@TODO How to do hit points ;) section.
