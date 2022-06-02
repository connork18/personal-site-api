---
title: 'Building this API: Baby step (4/n)'
date: '2022-01-20'
---

### Quick personal note ###
My class absolutely CRUSHED the Chopped presentation hackathon. Not only did they put thoughtful presentations together, but they gave excellent pieces of feedback to each other. Here was the photo I put at the top of their course notes. 

<Image
priority
src="/images/chopped-ck.png"
height={144}
alt={name}
/>

### Writing my posts as markdown in admin tool ###
Alright, so my api is looking pretty good, but I need an easy way to create html friendly blog posts. After that, I should probably write a test or two, update my frontend so that it is integrating nicely, then deploy the api on AWS elastic beanstalk and RDS.

Going to time box this at true 15 minutes, starting now.

Okay, starting my app up and going to see how the admin portal functions.

(...work, investigating, seeing what happens when I copy paste my DB post into my front-end blog-text-parsing function...)

Found a good <a href="https://learndjango.com/tutorials/django-markdown-tutorial">tutorial</a> that could be what I need. 

But... this might not be a step I need after all. I am going to need to do a little more trial and error and read the docs of the packages I am using.

The front-end is turning the markdown into html, so I when I pick up tomorrow I will start integrating the front-end with my /posts api and see if the package I am using successfully turns the text I am writing as markdown and storing in my DB into html.

Baby step.