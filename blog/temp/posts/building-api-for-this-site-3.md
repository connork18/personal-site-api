---
title: 'Building this API: Migrator (3/n)'
date: '2022-01-19'
---

### Quick personal note ###
Had lots of cool conversations today, covering teaching, metaverse marketing and even music. So much good energy. Energy can swing day to day, and I'm just taking a moment to appreciate the good energy from today.

Also-- I am doing a "Chopped"-like exercise (except without the competition part) in my class tomorrow and am excited. Constraints are important fuel for creativity. I am having the students spend 30 minutes doing some research and putting together a 5 slide presentation, which they will present afterwards. Other class members and myself will provide questions. I think it will be a great forcing function to getting them started and highlight the most important things they need to spend the semester fleshing out.

### Migrating my blog posts ###
Ok, so I want to parse the existing blog posts I have been writing for the last several months (which are in individual markdown files) and throw them into my shiny new database using my Post data model.

I am going to do this as fast as I can and am only going to spend 15 more minutes doing it.

It looks like I am using a package in javascript currently to parse the "front-matter" present in my markdown file. Looks like there is something similar in python called python-frontmatter.

pip install python-frontmatter

Cool, this is a very simple utility to use. Docs <a href="https://github.com/eyeseast/python-frontmatter">here</a>

And.... let's go! It's finished. This post and task took me 45 minutes on the nose. I need to show more constraint.. I could have finished tomorrow morning and gotten to sleep. Now I will be late for my peloton workout, but I'll figure it out.

<Image
priority
src="/images/posts-api-screenshot.png"
height={144}
alt={name}
/>
