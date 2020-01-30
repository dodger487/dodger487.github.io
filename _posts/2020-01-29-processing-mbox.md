---
layout: post
title:  "Quick and Dirty Email Parsing in Python"
date:   2020-01-29
categories: scraping
comments: true
---

*This is part 2 of a 4-ish (or more? or less??) part series describing how to train a bot to write emails like your friends.*

- Part 1: [How to download your emails from Google]({% post_url 2020-01-20-download-gmail %})
- Part 2: How to extract relevant text from the the Mbox file format (This post)
- Part 3: How to train GPT2 on your text (for free!) using Google Colab
- Part 4: Visualizing you email data with ggplot2

## A Thing Worth Doing Badly

When working on any side-project, the most important quote comes from G. K. Chesterton:
**"If a thing is worth doing, it's worth doing badly."**
We're not building a bridge here, we're having fun and learning.
Here are some python functions I quickly put wrote to go from a dataset of Mbox files representing emails to cleaner files of email text.

To recap a little: inspired by some of the successes of 
[GPT-2](https://openai.com/blog/better-language-models/)
I decided to make bots that wrote emails similar to my friends.
In the [previous post]({% post_url 2020-01-20-download-gmail %}) I showed how to download an email list via Google Takeout.
After filtering and downloading our email data via Google Takeout, we are left with an MBox file.
Now our goal is to go from a huge Mbox file to text that can be fed into GPT-2.

Here are the challenges we'll solve:

0. Extracting the text from the Mbox format.
1. Filtering emails included in the download that weren't written by me or my friends.
2. Removing copied "reply" text not written by the email author.
3. Removing boilerplate language added by email clients.

If you want to just view the code, [click here](https://gist.github.com/dodger487/3e5843918f318770e39b570840595ce3).

## Mbox format and Python's `mailbox` library

[Mbox](https://en.wikipedia.org/wiki/Mbox) is a family of file formats used to describe emails.
The format is really just a specific way of ordering text, so you can actually open up some files and take a peek and sort of understand what it's saying.
The Mbox file I downloaded from Google is called `friends-001.mbox` so I'll just use that as an example.

{% highlight bash %}
chris$ head -3 friends-001.mbox
From 1654953015393719153@xxx Mon Jan 06 04:49:45 +0000 2020
X-GM-THRID: 1654835874621973951
X-Gmail-Labels: Inbox,Important,Opened,Category Forums,friends
{% endhighlight %}

I won't dig too much more into the Mbox format, but just know that there are a bunch of headers with metadata about the email and then the email text.
Fortunately, Python provides a built-in library called `mailbox` that makes it easy to parse and use this data.

Using the `mailbox` is pretty easy:

{% highlight python %}
import mailbox
msgs = mailbox.mbox("friends-001.mbox")
{% endhighlight %}

Note that some of these steps may take a while if your Mbox file is huge.

We can now examine some individual emails and figure out what we need to do!


{% highlight python %}
In : msgs
Out: <mailbox.mbox at 0x103b089e8>

In : msgs[0]
Out: <mailbox.mboxMessage at 0x13370db00>

In : msgs[0]["To"]
Out: 'friends@examplegooglegroups.com'

In : msgs[0]["From"]
Out: 'Christopher R <cjr@examplegmail.com>'
{% endhighlight %}


## Getting the right emails
The first challenge was limiting emails to those that actually went to my email list.
I used Python's built-in Counter to see who these emails were from and to.

{% highlight python %}
from collections import Counter

from_emails = Counter(m["from"] for m in msgs)
to_emails = Counter(m["to"] for m in msgs)
{% endhighlight %}

Turns out, the Gmail filtering I used grabbed all messages of all threads that had been sent to my friends' email list.
This included emails from family members, other friends, promotional emails, and even a few from Toad's Place, the local sketchy bar.

To deal with this, I simply filtered on the email in the "To" field, only including an email in my analysis if it was sent to my friends' list.

{% highlight python %}
msgs = [m for m in msgs if m["to"] == "friends@example.com"]
{% endhighlight %}


## Getting the text

Next up we need to extract the written text from the email.
I found different instructions for this online, but after manual inspection I found that almost every email in my dataset had `is_multipart() == True`, and the first part was plain text and the second part was HTML.
I didn't want to deal with parsing HTML so I just only used the first part.
Some emails had nested structures.
Again, manually inspecing 10 examples or so, I found I could just always take the first part and I'd get the text I wanted.

Some operating systems use `\r\n` as line returns, others use `\n`.
To normalize, I then removed all `\r` characters. 

{% highlight python %}
def get_text(msg):
  while msg.is_multipart():
    msg = msg.get_payload()[0]
  return msg.get_payload()

def remove_r(text):
  return text.replace("\r", "")
{% endhighlight %}


## Removing Replies

One big issue is that most emails are replying to others, and include the reply text!
Below is a pretty typical example of some text.

```
OK so sadly I couldn't make any of this work with my data set. But! 
The good news is that I figured out how to do it all on my own using 
a very long and I'm sure very inefficient chain of ifelse commands. 
Thanks a billion anyway.

On Sun, Jan 5, 2020 at 1:10 AM Chris R <chris@example.com> wrote:

> I mean you could one line it in R too but it would be a little 
> opaque.
>
> On Sat, Jan 4, 2020 at 9:53 PM George <george@example.com>
> wrote:
>
>> Damn Chris. You writing a novel up there in R? In Wolfram Language:
>> [some stupid opaque wolfram code, etc.]
```

My goal is to grab one friend's text-- if I want to make a bot sound like Molly, I need to train it on just text Molly has written.
Above, we have an email from Molly, but it also includes text written by Chris and George!
We don't want our robo-Molly to sound like Chris and George.
A very simple way to strip out replies is to simply remove lines starting with "`>`".

{% highlight python %}
def strip_replies(text):
  lines = text.split("\n")
  lines = [l for l in lines if len(l) > 0]
  lines = [line for line in lines if line[0] != ">"]
  return "\n".join(lines)
{% endhighlight %}

This does leave this line:
```
On Sun, Jan 5, 2020 at 1:10 AM Chris R <chris@example.com> wrote:
```
I wrote regular expression to delete lines like these, but it missed a ton of examples due to line breaks showing up in different places.
In the end I didn't invest more time in weeding these out: my robot ended lots of emails with lines like that, which actually added to the authenticity!

{% highlight python %}
import re

def strip_footer(text):
  text, _ = re.subn("On (Sun|Mon|Tue|Wed|Thu|Fri|Sat),.*, 20.. at.*@gmail.com.*wrote.*",
                    "",
                    text,
                    flags=re.DOTALL)
  text, _ = re.subn("You received this message because you are subscribed to the Google Groups.*",
                    "",
                    text,
                    flags=re.DOTALL)
  return text
{% endhighlight %}

## Filtering and Printing

Finally, since I only want emails for one friend, we iterate through all emails and filter based on sender email address.
We then print their email subjects and text.

{% highlight python %}
def get_member_emails(mbox, sender_list, limit=100):
  msgs = []
  for msg in mbox:
    if (msg["from"] in sender_list
        and msg["to"] is not None
        and "friends@example.com" == msg["to"]):
      msgs.append(msg)
    if limit is not None and len(msgs) > limit:
      break
  return msgs

def print_msgs(msg_list, f=sys.stdout):
  for msg in msg_list:
    print("--------------------------------", file=f)
    print("Subject:", msg["subject"], file=f)
    print("", file=f)
    print(get_core_text(msg), file=f)
    print("", file=f)
{% endhighlight %}

I include a list of email addresses, in case your friend has used multiple emails.
I also add some formatting (the `---`) so the neural net can distinguish between different emails.

And that's it!

I put all this code in a [GitHub Gist which you can checkout here.](https://gist.github.com/dodger487/3e5843918f318770e39b570840595ce3)

Questions or comments?
Shoot me an email or leave a comment below.