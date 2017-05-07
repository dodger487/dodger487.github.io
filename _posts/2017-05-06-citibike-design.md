---
layout: post
title:  "What Really Grinds My (Citi Bike) Gears"
date:   2017-05-06
categories: design
comments: true
---

![It's a pun!](/figs/2017-05-06-citibike/grinds_my_gears.png)

I would like to briefly present my opinion on a tiny piece of the design of three different bikes in New York City's bike sharing program.
Read on and you may learn a tiny bit about design and Citi Bike.

Since joining, I've been a big fan of [Citi Bike](http://www.citibikenyc.com), New York's bike-sharing program.
I like the program for a variety of reasons, such as being faster than many other forms of transportation and being healthy and convenient.

But one issue that drives me up the wall is the inconsistency across the design of bikes, specifically with how changing gears works.
For biking newbs, gears are a device on a bike that control how far the bike goes for the amount you pedal-- a low gear is easier for you to pedal but you don't go as far (good for going up hills or starting from stationary) and a high gear is more difficult to pedal but you go farther for each rotation (good for flat terrain).

## Design principles
So... I'm not a designer and I'm not even very cool.
However, I *have* read [DOET](https://en.wikipedia.org/wiki/The_Design_of_Everyday_Things), and more importantly, I'm a human being, which of course qualifies me to broadcast my opinion on the internet.
Hopefully you are even worse informed than I am, and if not, perhaps picking apart my argument will be a fun and useful exercise.

If you have to read one book on design, read "The Design of Everyday Things" by Don Norman.
If you search Google for books to read about design, this is what you currently see:
![And if it's on Google it's always true](/figs/2017-05-06-citibike/google.png)

Here are [six principles Norman discusses](http://www.designprinciplesftw.com/collections/don-normans-principles-of-design) when designing something that a human will use:

- Visibility: Interfaces should be easy to find.
- Feedback: Interfaces should give feedback to the user.
- Constraints: Interfaces should constrain users to the possible actions.
- Mapping: Interfaces should have a sensible link between their form and the action they create.
- Consistency: Interfaces should have similar behaviors for similar actions and "follow rules".
- Affordance: Interfaces should invite particular behaviors by the way they are formed.

## What's up with Citi Bike gear shifting?
Below, I'm going to show pictures of three different Citi Bike gear shifters, along with a few comments from the design principles listed above.
As you'll see, all the gear shifters work by either rotating forward (what I think of as "pushing") or rotating backward (what I'll call "pulling") to change the gears.

Gear switching 1:
![Citi Bike Gear 1](/figs/2017-05-06-citibike/gear1.jpg)

- Visibility: Easy to see what gear you're in, slight separation from handle bar gives some indication of where shifting mechanism is.
- Feedback: Can see what gear it's in, though occasionally it can be confusing between 1 or 2.
  Also, feedback from feel of bike's pedaling.
- Constraints: Clear that there are 3 and only 3 gears!
- Mapping: 1 maps to lowest gear, 3 to highest.
  Pushing maps to moving to a lower gear, pulling maps to moving to a higher gear.
  Can't discover that without trying those motions.
- Consistency: Lower numbers mean easier to pedal, consistent with most bikes.
- Affordance: Two clear affordances-- pushing and pulling (rotating forward and back).

Gear switching 2:
![Citi Bike Gear 2](/figs/2017-05-06-citibike/gear2.jpg)

- Visibility: Again, very easy to see what gear you're in. 
  Shifting mechanism is a different look than the rest of the handle, but could be slightly confusing.
- Feedback: Very clear, very explicit what gear you're in.
- Constraints: Clear what gear you're in, not clear how many gears are possible as numbers are somewhat hidden.
- Mapping: Same mapping as before. 
  Unlike mechanism (1) above, very clear that pushing means higher gear and pulling means lower gear.
- Consistency: Pushing / pulling has different meaning than (1) !!! Same action = opposite result.
- Affordance: Same as above.


Gear switching mechanism 3:
![Citi Bike Gear 3](/figs/2017-05-06-citibike/gear3.jpg)

- Visibility: Roughly the same as the first two. 
  Visibility of bike symbols is worse than (2), as they're smaller here.
- Feedback: No visual feedback of what gear you're in.
  I think this is a [continuous gear bike](https://en.wikipedia.org/wiki/Continuously_variable_transmission), which is pretty cool, but they could still put a red line or notch or something on the shifter to show how far up the spectrum of low gear to high gear you are.
  Only feedback comes from what you feel while pedaling.
- Constraints: Not clear how far you can turn the gear shifter.
- Mapping: Pulling means higher gear, pushing means lower gear.
  Symbols help explain this but are small... imagine trying to figure them out in traffic.
- Consistency: Consistent with (1) but inconsistent with (2).
- Affordance: Same as above

Some of these comments are minor quibbles.
There's one issue that drives me nuts: **the same action on different bikes will have opposite effects**.
The fact that pushing on one gear shifter is the same as pulling on another frustrates me to no end.
I have to constantly look down at the gears when I'm shifting, to remember what kind of bike I'm riding.
Shifting gears can often come in a stressful or fast-moving situation: needing to stop but quickly start again, like at a light, going up a hill with lots of other bikers or runner nearby, etc.
The little extra mental effort can mean bikers taking their eyes off the road to discern which way to rotate their hands.

The other quibbles are small but could save many person-hours of frustration with just a little work.
In style 3, why not add a notch that shows you how far up the spectrum you are?
Why not make the symbols a little bigger?
What about making the gear shifters a different color from the handle to visually distinguish them?

There you have it, a few hundred words to tell you that I get angry because I don't know whether to push or pull to shift gears on my bike.
But looking bigger than just me, in 2016, there were **14 million** Citi Bike rides in NYC.
How many times did someone push instead of pull, shift up instead of down, and come to a dead stop on a busy hill?
I have no insight into the internals of their bike design, but it seems like a little more thought (or maybe money?) could have kept a consistent approach across bikes.

Citi Bike is a great program.
I'm definitely going to keep using it and I'm excited to try the continuous gear bike again.
I hope that moving forward, they'll try to keep consistent mappings to make riding even more effortless and enjoyable.
