---
title: 'Cool things, not cool things'
date: '2021-10-18'
---

I deployed my website tonight! <a href="https://frontseat.app">www.frontseat.app</a>.

Buuuuuutttttt that meant I had to do some DNS tampering, which is a recipe for disaster/headache.

Annnnddddd I ended up needing to switch around some configurations on AWS for routing and my Elastic Beanstalk environment.

Theeeeennnnn I had a bunch of crazy Elastic Beanstalk being angry with my AWS RDS instance and after some deep troubleshooting and wrecklessness, I am back up and running with a cheaper database tier than I used before. Hopefully that saves me some money and doesn't compromise how the app and the asynchronous jobs run.

So far, so good.

The cool thing about having more control over my backend is that I can do cooler things to provide more unique experiences for users. 

The bad thing is periodically I have to become a devops person and drift far away from the product problems I need to be focusing on solving.