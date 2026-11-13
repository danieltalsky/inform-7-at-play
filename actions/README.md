# Making Actions

People want to do stuff.  You can let them.

There are a few actions Inform 7 understands out of the box.

Imagine this unlikely scenario made of less than 100 words:


<!-- inform-example: standard-actions
title = "Built-in actions"
kind = "standalone"
explanation = "Defines the entire two-room action demonstration and all its objects."
commands = ["think", "look self", "look at crate", "look under crate", "push crate", "push crate south", "look", "push crate north", "chop crate", "smell grandson", "kiss grandson", "kiss crate", "attack grandson", "ask grandson about Apocalypse Now", "tell grandson about monkeys", "consult grandson about existentialism", "wake grandson up", "wipe jumpsuit", "get pocket", "open pocket", "put figurine on crate", "polish figurine"]
expect = ["You open the breast pocket"]
-->
```inform7
Kyrgyzstan is a room.  
[[Actually a country but let's let it slide.]]  
The description is "Officially the Kyrgyz Republic".

A completely standard video game crate is in Kyrgyzstan.  
The crate is pushable between rooms.  

Tajikistan is a room.  
The description is "Officially the Republic of Tajikistan."
Tajikistan is south of Kyrgyzstan.

Your Great Great Grandson is a person in Kyrgyzstan.   
The description is "He's wearing a hand-made jumpsuit."
Grandson wears a hand-made canvas jumpsuit.
The breast pocket is part of the jumpsuit.  
It is an openable closed container.
In the pocket is a creepy pewter figurine.  
```

With just under 100 words of description, Inform understands all these actions and what's possible in our fictional world:

> **Kyrgyzstan**  
> Officially the Kyrgyz Republic  
>    
> You can see a completely standard video game crate and your Great Great Grandson here.  
>   
> **\>`think`**  
> What a good idea.  
>   
> **\>`look self`**  
> As good-looking as ever.  
>   
> **\>`look at the crate`**     
> You see nothing special about the completely standard video game crate.  
>   
> **\>`look under the crate`**   
> You find nothing of interest.  
>   
> **\>`push the crate`**  
> Nothing obvious happens.  
>   
> **\>`push the crate south`**     
>   
> **Tajikistan**
> Officially the Republic of Tajikistan.  
>   
> **\>`look`**  
> **Tajikistan**  
> Officially the Republic of Tajikistan.  
>   
> You can see a completely standard video game crate here.  
>   
> **\>`push the crate north`**  
>   
> **Kyrgyzstan**  
> Officially the Kyrgyz Republic  
>   
> You can see your Great Great Grandson here.  
>   
> **\>`chop crate`**  
> Cutting it up would achieve little.  
> 
> **\>`smell grandson`**   
> You smell nothing unexpected.  
>   
> **\>`kiss grandson`**   
> your Great Great Grandson might not like that.  
> 
> **\>`kiss crate`**   
> You can only do that to something animate.  
>   
> **\>`attack grandson`**  
> Violence isn't the answer to this one.  
>   
> **\>`ask grandson about Apocalypse Now`**  
> There is no reply.  
>   
> **\>`tell grandson about monkeys`**    
> This provokes no reaction.  
>   
> **\>`consult grandson about existentialism`**    
> You discover nothing of interest in your Great Great Grandson.  
>   
> **\>`wake grandson up`**    
> That seems unnecessary.  
>   
> **\>`wipe jumpsuit`**     
> You rub the hand-made canvas jumpsuit.  
>   
> **\>`get pocket`**    
> That seems to be a part of the hand-made canvas jumpsuit.  
>   
> **\>`open pocket`**   
> You open the pocket, revealing a creepy pewter figurine.  
>   
> **\>`put figurine on crate`**  
> (first taking the creepy pewter figurine)  
> That seems to belong to your Great Great Grandson.  
>  
> **\>`polish figurine`**     
> You rub the creepy pewter figurine  


But what if you want to sing, spin, cry, dream, or any other of the roughly 100,000 verbs in the english language?

You will need to tell Inform how to handle them yourself.  Luckily Inform gives you powerful tools to do it.

Inform leaves it to you to decide what actions are important.  It can't think of the effects of every possible action!

## How to piggyback onto an existing action: understand the command!

Inform already has a good assortment of actions.  You can read <a href="https://inform-7-handbook.readthedocs.io/en/latest/chapter_4_actions/built-in_actions/" target="_blank">a list of them in the official Inform 
documentation</a>, but here are some useful ones you can grab and make your own:

 - smelling
 - touching
 - turning
 - attacking
 - rubbing
 - looking under

Let's say you want to use another word for "smell":

<!-- inform-example: perfume-bottle
title = "Before adding a command synonym"
kind = "standalone"
explanation = "Starts a new complete world for command synonyms."
commands = ["look bottle", "smell bottle", "inhale bottle"]
expect = ["That's not a verb I recognise."]
-->
```inform7
The Boudoir is a room.  
There is an empty perfume bottle in the boudoir.  
The description of the bottle is "It's an enticing and elaborate perfume bottle.  It looks as if you could just inhale its scent."
```

Let's try inhaling:

> **Boudoir**  
> You can see an empty perfume bottle here.
>
> **\>`look bottle`**  
> It's an enticing and elaborate perfume bottle.  It looks as if you could just inhale its scent.
> 
> **\>`smell bottle`**  
> You smell nothing unexpected.
> 
> **\>`inhale bottle`**  
> That's not a verb I recognise.

There's an easy way to make a synonym for smelling:

<!-- inform-example: inhale-command
title = "A synonym for smelling"
kind = "additive"
requires = ["perfume-bottle"]
explanation = "Add an inhale synonym to the existing bottle example."
commands = ["inhale bottle"]
expect = ["You smell nothing unexpected."]
-->
```inform7
Understand the command "inhale" as "smell".
```

Now inhale means smell also:

> **\>`inhale bottle`**  
> You smell nothing unexpected.

You might remember the word `understand` from the chapter on things, where
you can [use it to let you to call a single object by multiple names](../things/README.md#things-with-lots-of-names).

Here we're using it in a similar way: this new name is the same as a name you already
"understand".

## Make a `mistake`: a new action that just prints a message

One of the easiest ways to make a totally new action work is by making it a `mistake`:

<!-- inform-example: statue-mistake
title = "A command that prints a message"
kind = "additive"
explanation = "An independent command rule; context provides a minimal room and no statue object is needed for this literal command."
context = "The demonstration room is a room."
commands = ["yell at the statue"]
expect = ["The statue does not understand how serious you are about this."]
-->
```inform7
Understand "yell at the statue" as a mistake 
("The statue does not understand how serious you are about this.").
```

Here you're telling it to understand a whole command as a "mistake":

> **\>`yell at the statue`**  
> The statue does not understand how serious you are about this

It doesn't really matter if the action is an actual "mistake".  It could
be something you want the player to do.  Using the `mistake` command
lets you just print out a message and tell Inform not to do anything else.

## Actions without a thing: report



### @TODO Explain report rules for actions without an object, with a smelling transcript

<!-- inform-example: report-smelling
title = "A report rule"
kind = "additive"
requires = ["perfume-bottle"]
explanation = "Add a report rule to a runnable room; this demonstrates smelling without a noun."
commands = ["smell"]
expect = ["Then again, you don't have the best sense of smell."]
-->
```inform7
Report smelling: say "Then again, you don't have the best sense of smell. Maybe if you smell specific things it will be easier to discern a smell.".
```

## Make a brand new action

### @TODO Explain defining pinching, parsing its command, and carrying out the action; add example play

<!-- inform-example: pinching-action
title = "Defining a new action"
kind = "additive"
requires = ["perfume-bottle"]
explanation = "Add a new action and test it on the existing bottle."
commands = ["pinch bottle"]
expect = ["You pinch the empty perfume bottle."]
-->
```inform7
Pinching is an action applying to one thing.
Understand "pinch [something]" as pinching.
Carry out pinching: say "You pinch [the noun].".
```

## Simple actions with `instead`

@TODO Show an Instead rule overriding an existing action, followed by the resulting play.

---

## @TODO Remaining action topics

- Overriding the current verb set
  - list of the current verb set
- Creating new verbs
- "If"
- Rulebooks: the verb lifecycle
  - Before
  - Instead
  - Check
  - Carry out
  - After
  - Report
- Relations and state for nouns, changing state
