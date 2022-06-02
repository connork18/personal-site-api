---
title: 'Valuable software early and often vs. technical excellence and good design'
date: '2021-11-10'
---

Operating in theoretical write/sketch/talking land is one thing, and managing a code base is another.

My code base is suffering from my urgency and experimentation. There are time where I just hack instead of taking a little bit of extra time to pursue a more elegant design.

My thought process is -- if this code might be getting deleted anyway, why worry about a scalable, resuable design?

The problem, is once I get that feature out and test it and get new ideas, I just repeat the process again and don't allocate much time to refactoring.

If I refer back to the agile manifesto, the principles that appear related to this issue are:

 1. "Our highest priority is to satisfy the customer through early and continuous delivery of valuable software."

 2. "Deliver working software frequently, from a couple of weeks to a couple of months, with a preference to the shorter timescale."

 3. "Working software is the primary measure of progress."

 4. "Continuous attention to technical excellence and good design enhances agility."

I am pretty solid on 1, 2, and 3. 4 is where things get dicey. I think that my limited experience working on a big code base combined with my primary goal of figuring out how to turn this into a valuable product leads to me ignoring 4 at times.

Copy + pasting code is probably my worst offence against technical excellence and good design. I do this to avoid having to tamper with all dependent components and maintain the freedom to alter the one I am using. I typically go from pen+paper sketch designing straight to coding instead of using Figma, which means I don't have a formal design system in place that I adhere to. I sort of figure out the design of the component I want as I code it.

I also at times avoid deleting files or code that I don't use anymore. Because everything is viewed as a temporary experiment, I want the ability to go back if I need to.

Eventually, I hope to turn this into something that is worth having other people help work on it. In that case, I should maintain a well-kept and understandable code base as much as possible.
