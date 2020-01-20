---
layout: post
title:  "Downloading emails with Google Takeout"
date:   2020-01-20
categories: scraping deeplearning
comments: true
---

**This is part 1 of a 4-ish (or more? or less??) part series describing how to train a bot to write emails like your friends.**

- Part 1: How to download your emails from Google (This post)
- Part 2: How to extract relevant text from the the mbox file format
- Part 3: How to train GPT2 on your text (for free!) using Google Colab
- Part 4: Visualizing you email data with ggplot2

## Email Archeaology

Looking through old emails, I feel like an archaeologist of myself.
I'll run a search for a specific email, find a bunch of old things, and suddenly be immersed in the hot topics of 2009 and see all the wrong opinions I once held.

My college friends and I have used an ongoing email list for discussion for over a decade.
(I'm probably showing my age here; the kids these days I'm sure have group tik-toks or something).
I've often wanted to download this data to play with it, answering questions about who writes emails when, whose emails are longest, who is most likely to only send just a New York Times article, what words are most associated with which writer, and more.

I finally built up the momentum to get all of this data when I decided to finetune GPT-2 to mimic my friends' writing styles.
[GPT-2](https://openai.com/blog/better-language-models/) 
is a pre-trained neural network for text generation that has had 
[some](https://www.gwern.net/GPT-2)
[interesting](https://slatestarcodex.com/2020/01/06/a-very-unlikely-chess-game/)
results over the last year.

This post explains how I obtained emails from a specific email list.


## Google Takeout

[Google Takeout](https://takeout.google.com) is a service that allows you to download data that Google has about you.
It's frankly pretty extensive and impressive.
On the one hand, it's terrifying the amount of information Google has about my life.
On the other, it's pretty easy for me to get this data, at least in bulk.

One issue is that there can be too much data.
Takeout offered a way for me to download *all* of my GMail data, which, after over a decade of use and very little deleting, would have been enormous.
I wanted just the text of a specific email list.
Fortunately, there's a simple workaround.


## Targeting Specific Emails

Google Takeout allows you to download all emails with a specific label.
First, I [created a new GMail label](https://support.google.com/mail/answer/118708?co=GENIE.Platform%3DDesktop&hl=en&oco=0), "friends."
Then, I used a [GMail filter](https://support.google.com/mail/answer/6579?hl=en) to label all the emails I wanted.
When creating the filter, make sure to select "Apply filter to matching emails."

The emails I was looking for were first sent to an email list managed by our college's IT department and later to a Google Group.
With some experimentation filtering on the "to:" field, I was reasonably certain I grabbed most of the emails I wanted.

It may take a while for Takeout to generate your data, depending on the volume.
You can check back in a few hours or even days (I didn't see an email notification when my data was ready.)

Alternatively, if all the emails you want are in a Google Group and you are the **owner** of that group, there's an even easier method.
Google Takeout allows you to download all emails for a Google Group directly.
In the Google Takeout page, look for "Groups" and select that instead of "Mail"

## Summary and Screenshots

In summation:

1. Create a new GMail label.
2. Create a GMail Filter that targets the emails you want. 
    Make sure to select "Apply filter to matching emails."
3. Open Google Takeout.
4. Select "Mail", click "All Mail data included," then deselect everything exept the label you just created.
5. Wait for your data to be prepared.
6. Download.
7. Profit

In the next post, I'll show my quick-and-dirty script to processing this data using Python's built-in [mailbox](https://docs.python.org/3.7/library/mailbox.html) library.

Some screenshots of the process are below.

Google Takeout.
![Google Takeout](/figs/2020-01-20-download-gmail/takeout.png)


Select Mail.
![Select Mail](/figs/2020-01-20-download-gmail/mail.png)


Don't get everything, unless you don't have that much data in GMail!
![Don't get everything, unless you don't have that much data in GMail!](/figs/2020-01-20-download-gmail/deselect.png)


Select just the label you want.
![Select just the label you want.](/figs/2020-01-20-download-gmail/label.png)


