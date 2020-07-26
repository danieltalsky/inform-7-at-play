# Inform 7: Making Actions

People want to do stuff.  You can let them.

There are a few actions Inform 7 understands out of the box.

Imagine this unlikely scenario made of less than 100 words:


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
It is openable and closed. 
In the pocket is a creepy pewter figurine.  
```

With just under 100 words of description, Inform understands all these actions and what's possible in our fictional world:

> **Kyrgyzstan**  
> Officially the Kyrgyz Republic  
>    
> You can see a completely standard video game crate and your Great Great Grandson here.  
>   
> **>think**  
> What a good idea.  
>   
> **>look self**  
> As good-looking as ever.  
>   
> **>look at the crate**  
> You see nothing special about the completely standard video game crate.  
>   
> **>look under the crate**  
> You find nothing of interest.  
>   
> **>push the crate**  
> Nothing obvious happens.  
>   
> **>push the crate south**  
>   
> **Tajikistan**  
> Officially the Republic of Tajikistan.  
>   
> **>look**  
> **Tajikistan**  
> Officially the Republic of Tajikistan.  
>   
> You can see a completely standard video game crate here.  
>   
> **>push the crate north** 
>   
> **Kyrgyzstan**  
> Officially the Kyrgyz Republic  
>   
> You can see your Great Great Grandson here.  
>   
> **>chop crate**  
> Cutting it up would achieve little.  
> 
> **>smell grandson**  
> You smell nothing unexpected.  
>   
> **>kiss grandson** 
> your Great Great Grandson might not like that.  
> 
> **>kiss crate** 
> You can only do that to something animate.  
>   
> **>attack grandson**
> Violence isn't the answer to this one.  
>   
> **>ask grandson about apocolypse now** 
> There is no reply.  
>   
> **>tell grandson about monkeys**  
> This provokes no reaction.  
>   
> **>consult grandson about existentialism**  
> You discover nothing of interest in your Great Great Grandson.  
>   
> **>wake grandson up**  
> That seems unnecessary.  
>   
> **>wipe jumpsuit**  
> You rub the hand-made canvas jumpsuit.  
>   
> **>get pocket**  
> That seems to be a part of the hand-made canvas jumpsuit.  
>   
> **>open pocket**  
> You open the pocket, revealing a creepy pewter figurine.  
>   
> **>put figurine on crate**  
> (first taking the creepy pewter figurine)  
> That seems to belong to your Great Great Grandson.  
>  
> **>polish figurine**  
> You rub the creepy pewter figurine  


## But what if you want to sing, spin, cry, dream, or any other of the roughly 100,000 verbs in the english language?

You will need to tell Inform how to handle them yourself.  Luckily Inform gives you powerful tools to do it.

Inform leaves it to you to decide what actions are important.  It can't think of the effects of every possible action!

So if we want to:

> **\>bend paperclip**

## Simple actions with `Mistake`

One of the easiest ways to make an action work is by making it a `mistake`:

```inform7
Understand "yell at the statue" as a mistake 
("The statue does not understand how serious you are about this.").
```

### @TODO add a note: about all 3 uses of `understand`

> **\>yell at the statue**  
> The statue does not understand how serious you are about this

## Simple Actions with `Instead`

### @todo
