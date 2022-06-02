---
title: 'To force or not force (third party auth)'
date: '2021-08-21'
---

Should a new user be required to authenticate with Spotify in order to create a Frontseat account at all?

For some reason I WANT to prompt them to authenticate with Spotify in order to create an account, but I don't think it is the best thing for me to do. 

Doing this would cause more friction to users (even long time Spotify users may not know these credentials or may not already be logged in to Spotify on their mobile browser). 

On the other hand, forcing it upfront would allow me to simplify the experience by reducing or eliminating the need for Spotify authentication upsells.

I originally thought that I should give the best experience that I can while requiring the minimal possible investment until it is absolutely necessary. Hopefully, the non-authenticated user is able to see some songs by the end of the onboarding flow, which is the only real value I can think of at this stage. Then, once they try to filter the songs or export them, they are prompted with "This feature requires Spotify auth... Auth now?" sort of thing.
etc). 

I guess if I imagine myself talking to a stranger at a record store that expressed interest, I lean towards my original approach. I could easily start onboarding them and then they say "oh shoot I don't know my Spotify account creds" and then the conversation is over. I definitely don't want that to happen. Is that likely? I don't know but based on my experience, I think it is likely enough that I should accomodate it.

I guess the "upsell" could just be a simple Alert component on a short list of buttons and switches that checks whether the user is authenticated with Spotify.

I think that is the way to go. If I am offering a way to skip the Spotify authentication, I need to make sure to clearly communicate the value they will get from authenticating during the sign up flow.

If I wanted to enforce some additional investment when creating an account, I could require a verified email as part of the process. It would be a shame for a user to create an account, authenticate it with their Spotify, not be able to reset their password if they forget it, and then not be able to authenticate with Spotify in future accounts.

So... my (current) answer to my question is "No."