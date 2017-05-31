---
layout: post
title:  ""
date:   2017-06-01
categories: stats fun
comments: true
---

# ``Same Stats, Different Graphs" by TODO

A really cool paper blew up my Twitter feed a few weeks ago.
Two researchers from Autodesk (TODO: names) showed how they could take a dataset of noisy, random points, and create a new dataset with some of the exact same statistical properties that looks entirely differently when graphed.
And when I see different, I mean, the difference between a point cloud and a dinosaur.

Check out this image from their paper:
(TODO image)

I highly encourage you to read their paper.
It's only four pages long and very clear, with a great motivation and a nice description of their algorithm and extensions.

I see something neat, think to myself "Wow, that's so cool, and it should only take me a few hours to do!" and then three years later I finally complete it.
A case in point might be the Face of Saybrook project, where I thought taking photos of a few hundred people and using software to average their faces should be no problem... I got it done, but it took a bit longer than I thought!



## Computer Art

I don't consider myself an artist but I do like to create projects that don't have a purpose.
Wow, I guess that sentence implicitly contains some kind of crappy assumptions about artists.

Face of Saybrook
Minesweeper
Capybara

## The Algorithm: Simulated Annealing

One of the things I liked about the paper was how simple the algorithm is.
Here's a screenshot of it from the original paper.
They use a technique called simulated annealing.
There's a longer physics-based explanation for simulated annealing, but I'm going to try in an "explain it like I'm 5" sort of way.

(TODO: what's a thing you jiggle around?)


## Implementation


## Onward: Optimization and 

I did some quick-and-dirty optimization once the code ran.
My code was certainly running fast enough to be practical, but it wasn't running fast enough to be convenient.
I switched everything from a 

Doing a sum over a list comprehension was surprisingly slow, as was 

One of the authors responded to a question I wrote him, and another idea he proposed was 


## Linear Programming

After getting simulated annealing to work, 

Earlier I described simulated annealing as being some random shaking of points.
Lots of machine learning operates differently, 
Since we had a clear fitness function and constraints, I wondered if 


