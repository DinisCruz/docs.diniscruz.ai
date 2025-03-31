---
title: "Deterministic GenAI Outputs with Provenance  (OWASP EU AppSec Lisbon)"
authors: ["Dinis Cruz"]
date: 2024/06/28
---

# {{title}}
_by {{ authors | join(" and ") }}, {{ date }}_

Presentation delivered at the Global OWASP AppSec in Lisbon in 28th June 2024

## Slides

<iframe src="https://files.diniscruz.ai/gslides/2024/06/28/deterministic-genai-outputs-with-provenance__owasp-appsec-lisbon__gslides.pdf" 
        width="100%" height="450px" style="border: none;"></iframe>

## Video

<iframe width="100%" height="450px" src="https://www.youtube.com/embed/IEN9Ittv4V0?si=Q5wL0SlzPei7xs8X" 
        title="YouTube video player" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; 
        web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Transcript
_with minor fixes by Claude_

## 1) Introduction and Background

So I'm going to speak about my ideas, my experience, and where I think generative AI is going to make a massive difference—where I think it can be used, where I think it shouldn't be used—and throw a whole bunch of concepts and ideas to you, along with real-life examples of the stuff that I've been doing.

OWASP is very dear to my heart. OWASP started with me replying to another crazy dude called Mark Curphey online where I said, "Hey, I'm doing some cool research," and he said "Come along." Long story short, I started to be involved, did a lot of stuff, and was part of what I would say was the first real generation of OWASP leaders that were thinking globally. I was on the board, I started lots of projects, met lots of you in amazing places and venues. I think OWASP is a great example of a community that you want to be part of, you want to be involved with. It's very easy to get in, it's easy to be involved—just assume everybody has great intentions. Sometimes it feels dysfunctional, but every company and organization is dysfunctional. It's an amazing environment to be in.

The recommendation I would give to a lot of people who are on your career path is what I've done: I waited until I was quite experienced to go into executive positions. I think that's quite important because it meant that by the time I arrived there—and I think I've had a reasonably successful career in the UK as CEO of a number of organizations, growing teams from 2 to 20, managing multi-million pound budgets, and doing US growth and innovation—by the time I got there, I felt I was kind of hacking the organization from the inside, which was really cool.

The nice thing that happens when you're senior and experienced is you control your time. You think you don't, but you do. All you have to do is delegate. So I became very good at delegating and working technically hands-on. I have to say I'm still very technical. I still program, as you'll see. I still build a lot of stuff, and I think that's very important because I think if you don't program, if you don't know how things really work, you struggle with certain concepts.

On the other hand, there's space in cybersecurity for everybody. There's room for everybody. We need as many people as we can get. We need as many more people to come in, and I was going to say a bit later that I think the world really needs AppSec. I think up until now, the world got away without it. Some places use it; other places were like "roll the dice, it's great we haven't been hacked yet." But I think that's going to change.

So I've kind of evolved. I'm working with a generative AI company now. I'm actually a chief scientist for a tech startup. We make a bunch of stuff. That's my part-time job. It's really cool what we do there. I do a lot of open source development. In fact, I think I'm probably one of the biggest code contributors if you look at my repos and the stuff I do, although my biggest project, which I'm going to show you, is not an OWASP project because I didn't update it to OWASP guidelines. So if you guys want to participate in OWASP projects, join this one because I think there's a crazy amount of good stuff flying around.

I also do this thing called Security Summit which, by the way, I kind of started because I wanted to do a lot of summits, and there was a bit of a fork in the road. But the great news is OWASP now is going to do Summits again. So in November in the UK, we're going to do another one of the Summits, and then hopefully more to come. Sebastien's there—one of the key players in The Summit—so it's going to be really cool.

By the way, I kind of created this presentation, and then halfway through I felt that it was a bit presumptuous, but I have to say that I'm proud of every single one of my roles. You know, the keynote speech is not that relevant, but I've been a leader, I've been a member, I've mentored a lot of people—actually some I think in this room. I'm a defender, I'm a breaker, I'm a builder, and I'm a developer, and I actually think you need to do all of that. I don't think you can defend if you can't break. If you defend but don't know how to break, you don't understand the thing. So you need a bit of everything, because you get a better perspective of everything. And you need to be a developer even more these days.

Management and culture—managing is like hacking, just with different kinds of metrics and different parameters, but it's still very cool.

## 2) The Evolving Nature of Technology

I'm going to focus on generative AI. In fact, I'm going to be politically correct here. There are some people working on models that, for me, are like blockchain. When people explain the use case, I kind of get it, but I could do that much better with some hashes, some workflows, and clean up the data. I think a lot of the training models—and these days I'm really against training models—they're trying to solve a problem that you should solve in different ways. If you need the speed, then you're talking about machine learning, not generative AI.

Generative AI is different because there's an air gap literally between the input and the output. I think there's a lot of space for machine learning—we've been doing that for a long time—and there's a lot of space for deep learning. But I think generative AI is something we have to treat a little bit differently.

My presentation is about deterministic generative AI outputs with provenance. It's important to go through this in detail.

"Deterministic" means repeatable, consistent, auditable, predictable, and reliable. When we program, that's what we want. Code has this really interesting property that, although yes, there are bugs and problems, it actually is quite deterministic once we understand it. We don't always understand how our software works, but the reality is code is very deterministic in a way, and especially when it works once, it tends to work consistently. In fact, we build entire infrastructures and companies and environments on top of it. So I think deterministic is very important. When I develop, I go over every little detail that I don't understand. It freaks me out when there's something that happens that I can't track or can't replicate.

Generative AI is, I would say, the new generation of AI models that ChatGPT really brought to the forefront, but it's been around for a while. It's different—it generates content. 

I think the people who say generative AI just predicts output are doing a disservice. I would argue that it has logic, it has reasoning, it has a huge amount of understanding of how things work. It's not conscious, of course—it's still ultimately an algorithm running. But what's very interesting is that we still don't know how it works. The best understanding that I've heard is that generative AI creates a model of the world based on whatever question you're asking, and then it answers based on that. That's why it translates language very well, because it's just a model, and it understands the relationship between everything.

So generative text and images—the output is what gets created, what we literally give to users. And provenance is actually one of the things where I feel OWASP has to absolutely be a massive player, because OWASP will be one of the sources of trustworthy information, knowledge, and content. We need to have provenance. We need to understand how we arrived at a decision, how we arrived at a result. 

What's interesting is that when you track it back and you hit a large language model (LLM), you can't continue because we don't know how we got there. We don't know how it works, we don't know the sources. And there's an argument that says we might never know because of the way it has been designed in the first place.

Here's a question for you guys: What is the sixth most powerful programming language in the world? There are a lot of languages in the world, so think about programming languages. Which one do you think would be roughly in the sixth position these days?

[Audience responses: Excel, VB, Beans, COBOL, Java, JavaScript, Rust, Python]

So there are two in there that are on the right track, but I think there's only two, and there might be a misspelling of one. 

Here's the interesting thing: Data is now code, and prompts are literally natural language. The actual sixth most powerful programming language in the world is actually Portuguese, which is awesome! Isn't that cool? We, as native speakers—at least for the native speakers here who speak Portuguese—know how to program in the sixth most powerful language in the world right now.

In terms of size, English is the new coding language. Mark Hurd said "The new programming language is English," and I kind of agree with that. Because Portuguese, like English and every other language in the world, dead or alive, can be used to give instructions to LLMs. 

You have to remember that from a security point of view, with LLMs, we're going backward two decades. We spent all this time trying to separate code and data, and now data is code. There's no way around it. Even when you try to segment it, there's always stuff in there, which is kind of why I'm saying injection is probably not really a solvable problem at the moment.

There are 266 million first-language Portuguese speakers in the world, placing it ninth in spoken languages, since English is actually at the top. But with 257 million speakers, that's pretty cool. And there are a lot of programmers out there.

I think Portugal is an interesting country. Some countries outside of the UK and America and some of the major players have a great opportunity to really be massive players in this field. They have a great opportunity to not miss this next revolution, which is going to make a massive difference. And in a way, you are part of it. You need to really accelerate because the future of Portugal kind of depends on you. I think it can really make a massive difference, but we need to get it right. Otherwise, Portugal just becomes another consumer of global technology, which is not where it should be, because now we actually have the ability to make a difference.

My view is that generative AI is the next major technology revolution. Even saying that is doing it a disservice—it's not just major, it's much bigger than the previous ones. We had big transformations, but generative AI is a bit like if AOL had won, and there was no real internet, and suddenly at the same time you had mobile and the cloud arriving simultaneously. Imagine the disruption that would happen.

I think that's kind of what's happening at the moment. Yes, there's going to be a bust that I'll talk about later, but I think the reason why it's so powerful is not because it can create content. Most people talking about hallucinations focus on that. It's kind of like we invented Jarvis from Iron Man, and then we complain that Jarvis is bad at making things up. But actually, it's an insane co-pilot, an insane helper, an insane reviewer. That's what it is. For the first time, we have a bit of technology that can actually understand content, can actually understand things. We never had that before. We always had to code it, which is why it never really scaled.

In a weird way, "hallucinations"—and whoever came up with that name deserves a prize because it kind of saved the industry for a bit—it's really just making things up, lying. But it's a nice word. It's a feature when you want creative stuff; it's a bug when you want deterministic results. 

By the way, our software hallucinates too. We call them bugs and security issues. Somebody was mentioning Log4j—the fact that a logger can do remote code execution, that's hallucination, code style. We have that problem, and in fact, most software nobody understands how it works because the people who programmed it are long gone. The new crowd is like, "I don't know how this works, there's no documentation." So half the world runs on top of that.

## 3) Security and Safety in Generative AI

A key question is: Is generative AI secure? Is it safe? I tend to use these words "secure" and "safe" a little bit uniquely because security is about the security properties of something. You can measure security. Security is like: do you have security features? Do you have X, Y, Z?

You can argue that a house with machine guns outside of it, with weapons and guards and all that stuff, has a lot of security features. It's probably secure; it's very hard to get in. But is it safe? Most likely not. Is that where you want your kids to grow up? Most likely not.

So it's important to distinguish between security and safety, and it's important to have context. I always tell the boards when they ask, "Are we secure?" I say, "No, that's not the point. In fact, we're not." The question is: "Are we safe?" And they say, "Well, that's a much more interesting conversation to have."

So is AI secure? No, not even by a freaking long shot. In fact, I'm going to talk about how it's not—it's ridiculously dangerous. The API is going to be your most crazy insider threat once it starts to propagate.

Is AI safe? I think maybe. I think it depends on the implementation, and I'm going to show a couple of case studies of how to do it right.

I want to walk you through a way of visualizing LLMs which hopefully will demystify some of the magic, because there's still a lot of magic behind the scenes. How does it work? What does it do?

Let me show you one in action. I've been working on this thing which I call Cyber Boardroom. My project is open source—most of the stuff, everything I'm going to show you here is on that GitHub repo. It's on PyPI, it's on Docker Hub.

This is what I've spent the last two months on, and I would argue that anybody here who is developing anything, any product, building a really effective DevOps pipeline even from a security point of view, this is probably the single most important thing you should do. You should not stop until you have something like this.

What's cool about this is I can now make a code change that runs my unit tests—and that's very important. So every single major and minor release, I tag. I have literally tags left and right and center. I publish to PyPI, I publish to Docker Hub, I create Amazon Machine Images (AMIs), I publish to EC2, I publish to GCP, I trigger another set of custom versions, I go to Lambda, and I publish to ECS tasks.

I'm able to deploy these applications you're going to see, which you can run from your laptop, completely isolated and even offline now that you've got models like Llama and others, providers like Ollama that allow you to run models like Meta's and others. You can literally run the whole thing offline, and that's literally for me the best way to have a secure app.

The best way to have a secure app is not to care about the security of it because you put it in an environment where security vulnerabilities don't matter.

I'll give you an example: I was at a dinner with a bunch of CISOs, and there was this guy—we were talking about SolarWinds and all that stuff—and he just said, "Look, I couldn't care about SolarWinds. I heard about it, I turned off my computer, I just figured it out, I went home, I didn't do anything about SolarWinds."

They had massive SolarWinds deployments, but you know what they did? Something very simple: they didn't allow their SolarWinds instances to go to the internet. Because why the hell should that thing go to the internet? Why should the application you deploy in your data center be able to connect anywhere apart from where they really need to?

So that was a great example of building environments that you can then run isolated, and then you get a lot of security from that. What I'm doing with this solution is basically allowing it to be deployed anywhere, and that's very important. You get a lot of security because suddenly, even if there are security vulnerabilities in this application, if you deploy it in a completely air-gapped environment, it doesn't matter. That's the bottom line.

That's the thing that a lot of the vendors, a lot of the people who are trying to sell security solutions, they don't get. You have to answer the question: "So what? What's the context? Why does it matter?" I don't care about vulnerabilities; I care about the impact.

In fact, there's a really cool concept called the "minimal viable company," which is this idea that you should know what parts of the company you should leave intact if there's a massive incident. I had a breach once in one of my teams, and they went and fixed the problem, and at the end I said, "You should not have run there. You should have run over there because that's our most important asset. I could afford that other part to all burn down. Yes, it's problematic, it's a pain, but if that thing got hit, we should be defending this, not that."

So you need to understand this. You need to have context on this, and this DevOps pipeline is vital. It was really personal to me. I could say, "I want features because of that," and I literally spent two months building a CI pipeline. I remember once arguing with another security peer because he said, "I have this budget. Where should I put my money?" And I said, "You know what you should do? You should fund the CI pipeline of the developers, because without that CI pipeline, it doesn't matter what tooling you get—it's not going to go anywhere." So I think that is the most important security feature that you can have.

What happens? I just created a new AMI for breakfast. I don't care, and literally, I deployed to production with a change of AMI. It's a really sweet solution. You have a global load balancer, you have region load balancers, you have an auto-scaling group, you have an AMI which is a copy of an image, and that's it. This thing will scale now until AWS breaks.

What you have to do is solve state and secrets, which you should do anyway, and then lots of little things break. But once you deal with them, it's really robust, and that means that every one of those is an isolated release of this application. Every single one of them. Which is really cool. And nothing runs just on a laptop or a Docker container or a raw EC2 image with systemd; it runs in Kubernetes and runs at massive scale because it's just a few bits. Once you've done that, it's always the same. So it's really cool.

The challenge I'm trying to solve, which is a challenge that I think everybody deals with in some ways, is how do you scale risk management context? Because when you do this at a certain C-level, you kind of do this independently, but you need to be able to scale it. We need to be able to do this at scale, and that's where we really failed in security.

We really failed in security because—by the way, we are some of the most important people in the company, just to be clear. We are the only department in the company that has access to everything, speaks to everybody, has good relationships with everybody, and has a mandate that is not that political, which is: keep our customers or our business drivers safe. We have a larger-than-life mission, and we save the day. That's pretty cool. There's not a lot of departments that can say that.

Actually, a lot of times, we're like shrinks. In incidents, sometimes I had three departments, and we just had to get them together, and they weren't getting along. I'm like, "Come on, at least for this crisis, work together!" But at least you build relationships. So it's really cool to do that.

But my challenge was always: how to scale risk management? How to scale? I have this nugget, I have this thing that I want to do—how do I really allow the business to make good decisions?

It's not that I didn't have access to the board. It's not that I didn't have access to the right people. It's just that I couldn't scale because if I went to my team and said, "Guys, I kind of want daily weekly reports, and I don't want just one, I need 25 or 50 reports," you can see where they'd send me. Nobody would do it because it didn't scale. But I think now we can, because of generative AI.

When you talk about briefing somebody, it's very important that we understand what that means. If you're briefing an individual, you have to brief them in their language, in their culture, with whatever knowledge they have, in the state they're in, because it changes. And you need to allow them to ask questions.

In the past, this was an app, this was a graph; it never really scaled. But what's cool about LLMs is they allow us to do this. The problem I'm trying to solve here—and you can forget about Cyber Boardroom, you have the same challenge anywhere—is how do you communicate with stakeholders using their language, culture, knowledge, state, interests, and level of ownership? Level of ownership is also important: do they care or don't they care? What are they invested in?

## 4) Cyber Boardroom Project Demonstration

So basically, I built this thing which you can use. Let's take it for a spin. I'm going to try—I have the screenshots, but let's see if I can do a live demo.

Here's my AMI being deployed, which is really cool. This is sort of the Athena part where it uses OpenAI, but the interesting thing is this part here.

I'm going to come in here and give you a little demo. I'm going to say, "Okay, say hi." All nice and good. I'm going to say, "My name is John."

Actually, let me just change the provider to Meta. It's really cool—if you guys don't know what those are, that's Groq with a Q, which is a very clever play. They're doing microprocessors, so they give you LLM stuff for free because they're experimenting with it. I think they have a great strategy—they're basically saying, "We're better than Nvidia at inference," and they really are super fast.

You've got OpenRouter that gives you access to all the other providers really nicely. Again, you have AWS Bedrock and other players, but I really like OpenRouter. You have Llama, which is really cool. When I run this on my laptop, I can run this on the plane, I can run this offline. It's awesome. It's a bit slow these days, but it's already doable. It's good for tasks that don't require interactive responses. And then OpenAI is the major player.

So you can see, I say "Hi there, nice to meet you. What's up?" So I can now say, let's say, "What is 2 + 2?" and you get the answer: "4." And I can say, "Can you add more to make it 42?" because it's always 42. And "Can you reply with my name?"

Cool. So what you have here is actually the key part of the system. If you look at my last message, I can say, "Can you add it to make it 42." I didn't say what the last number was. I didn't say that you were at 4. So it remembered the last number—it learned. And it remembered my name. How cool is that?

Now the question is: how did this happen? How did it do this? When you think about people training models, it's kind of like they want to train a model so this knowledge is baked in. The problem I have with that is I don't understand how it learns, so I don't know how to debug it, and I don't know how to trick it. And good luck doing GDPR erasures on that data when you train a model.

But the question is: how do you do this? One of the coolest features that I've added here—and by the way, this is all open source, you guys can play with it—is that edit button, which I think is quite unique. I haven't seen that anywhere else. What that edit button allows me to do is to come in here and say, "Actually, my name is Dennis."

So what's going to happen is I can now say, "Are you sure you got my name right?" And in fact, we could also change the sum. Let's do this. Let's say, "Actually, let's see then, if we add 138 more, it makes 42." And "Are you sure you got my name and the sum right?"

So what I'm doing here is changing the data that is sent to the provider—ChatGPT, Meta, Llama, etc. So what you can see here is it goes, "Oh, sorry about the mistake." You told me here that my name is Dennis, because the whole context of that question is what was sent that I just edited. And then it says, "I apologize for the confusion, let's try again."

And this is quite interesting because it actually still makes a mistake. Can you see that? If you add 138 more, that makes 4 plus 138, which is 142, not 42. So that's a hallucination. Sorry, I made a mistake there. Let's try that again.

My name is John. What is 2 + 2? It's 4. Add 38 to make it 42 and say my name. There you go.

Oh, and you know why it didn't work before? It's because Google's Gemma 2 doesn't do a good job remembering. But if I now switch—and the other thing that's really cool is, can you see that little thing there at the bottom? I can flip between the different versions, which is actually really cool.

So I can now say, "Try again," and now it's going to say, "I apologize for the mistake. Your name is John." So you can see the other one was done by Google Gemini; this is done by Meta Llama 3.

And then I can say the same thing. I can say, "My name is Dennis," and then I go, "Are you sure about my name?" and it's going to go, "I apologize, your name is Dennis."

The thing that I really want you to understand is that this is how LLMs work. There's no black magic behind the scenes. In fact, I think OpenAI does a disservice because they kind of hide this from you. In fact, what they don't show you is how much they are compressing the conversations in between, because the thing I've learned with this is that you don't send your entire history every time, because that grows exponentially and it gets very expensive.

This is very important: the model just sees whatever is in that prompt. The coolest thing is that you can create entire realities in that prompt, and that's why I'm saying it's all about the prompt. It's all about finding the right models, and then you provide information to them—that's how it works. And this is a good example of how you can edit and play around with it and really manipulate it and understand how it works.

So now, start asking simple follow-up questions, edit the history, see what happens. One of the things you can do is make it speak in any language.

Here it is—what I want you to understand here is that the bit in black at the top, that little bit there, is all I had to do. In the data that you send to the LLMs, you fundamentally send what's called a system prompt, which still has a little bit of power (it's not always enforced), then you have the history and what's called the conversations you had, and then you have your prompt, which is what you sent. You can manipulate all of it, every bit, as I was just showing before.

So just by saying "only speaking Portuguese," "only speaking French," the same question is now answered in these languages. So basically, "What is OWASP?" OWASP is a nonprofit.

What's really cool about this is that that's all it takes. If you think about even OWASP as an organization, OWASP needs to speak every language in the book now. We need to be multilingual from the ground up.

Now it doesn't mean this is 100% perfect, and that's why we need to start to have better models. That's why even in Portugal, we should invest in models that speak our language better. Because even ChatGPT speaks Brazilian Portuguese, not that that's a bad thing, but in fact we need Portuguese from Portugal, Portuguese from Angola, Portuguese from Mozambique, Portuguese from Cape Verde—from every one of our dialects. It would be cool to actually have Portuguese from Algarve, from Alentejo. I never understand those guys! Those cultures are great, so we should have that. We should preserve it, and it should have that level of quality.

But this ability to translate is what I think gets really interesting, because this is where the LLMs are really good. Here is OWASP in six different languages—the most popular ones: English, Mandarin, Hindi, Bengali, Russian, and Portuguese. Basically, we should be speaking every single language; every piece of OWASP content should be translated and verified and maintained in every language that exists. In the past, we couldn't scale this because we couldn't handle the differences, but now we can.

Here's the coolest thing: Communicating with executives is like speaking a different language too.

## 5) Communicating with Stakeholders

So let's talk to three board members. What I've done here is created an environment—I'm playing with the Cyber Boardroom, but again, it's nothing special. You guys need to start replicating these in your own environments.

So I created a board member who's a CFO. I instructed the system: "Act like a board member that has legal responsibility for the company, replying in one paragraph, and you are focused on finance. You have no experience of cybersecurity."

And then I asked the kind of question that security executives often ask: "Hey, I need 250K budget to replace our SIEM, improve our SOC capabilities, and deal with APT more effectively." So you can see how that flies with the executives.

What's interesting about this is you can see the CFO going, "Hey, I don't understand the scope of this. What the hell are you talking about? A quarter of a million dollars is a significant expenditure." 

This one here—I said he has some experience in cybersecurity—is more operational: "I understand the importance of doing that."

And then the one on the right—I said, "I'm the HR person"—responds: "I'm afraid I don't understand clearly what you're asking for. As a board member, yeah, other, what are we doing?"

So basically, you can ask all sorts of questions. You can say, "Do you care about cybersecurity?" And you'll get responses like, "Care about... can you spell it?" And basically: "To be honest, I don't understand as a board member operational capabilities. To be honest, I don't understand the intricate..."

Now, this is still very polite. This is being quite politically correct in the answers. In the real world, what you tend to have is actually this:

I created three executive personas. The first one is a CFO that doesn't have a lot of patience. The second exec is the CEO who actually hired the CISO—and by the way, that happened to me twice. I met two different executives, and they basically turned to me and said, "Hi, you owe your job to me because I was a board member. I arrived here, and I said, 'Dude, where's your security team? You need to get one.'" And then the last one is the HR person who is jaded and harassed by security and doesn't like that guy. This is the real world. This is what happens.

Now it gets interesting. The CFO says, "Look, I have no patience. I don't have time to understand what APT means. I don't care about the technical details. What I care about is the bottom line. What kind of financial returns can I expect on this investment?" That's exactly the kind of question you have to answer with everything you guys do.

And now you can start to translate it. The one in the middle—the CEO who hired him, so he's a bit friendly, trying to mentor—says, "Look, I appreciate your enthusiasm, but as a board member, I approach responsibilities... I need to see the bigger picture."

And then the jaded guy is going, "Hey, another tech bro coming with more TLA [three-letter acronyms] and expecting a quarter million dollars without breaking a sweat." So I quite like this humor. I think it's quite funny to see the human side of things. Even when they don't say this, this is exactly what they're thinking.

So what you have here is you can now start to map out the personalities. You start to map out what's happening, how to communicate, and better understand stakeholders. The thing I'm doing with the Cyber Boardroom is that I'm also trying to allow them to ask questions, and then the questions come back to you. Because the thing that's going to be interesting—and by the way, this is coming your way whether you're prepared or not—is that you can then take this approach further.

One more thing: I also asked the same question to multiple LLMs. What you have here, and this is the final kind of workflow, is the minimum you should be doing with LLMs: Ask the same question to three LLMs and then ask them to verify. That is the way you really want to do it. One LLM is not good enough.

In fact, there are two great analogies. One of them is divers. When divers go down for a deep dive, they take three watches, because one is not enough. If it breaks, you might die. If you have two watches, you don't know which one is right. So you take three—if they all show the same time, okay.

Actually, the people doing space microchips do the same thing. SpaceX has three microchips. They basically send the same instruction to three processors, and if they all result in the same answer, then you continue. So it's really powerful to do this, and this is the minimum you should be doing. And it's ridiculously powerful.

If I come in here and say, "What is OWASP?" and ask it to reply, it gives you an explanation. Then you can say, "Cool, now act like a content reviewer with super focus on detail and review the results."

So now you can see—and this is what I mean by the prompt—what you're going to see here in blue is everything that the fourth LLM received. So the fourth LLM received my prompt, the answer from chatbot one, the answer from chatbot two, the answer from chatbot three, and then it gives you an analysis.

You can do this four or five times. You can say, "Well, is that analysis correct?" until you reach a state of conclusion. You can even go from one LLM to another, and you can play around with this. And now that LLMs are free or close to free, this scales really nicely. So it's really powerful.

But the problem with this is that the LLMs hallucinate. And by the way, for some reason with me, they hallucinate pretty spectacularly. Whenever I do this, I get some ridiculous answers.

So it works like this: I'm an OWASP member, so in one response it says, "Oh, I wrote the Testing Guide for the Web Security Center," and "I spoke at Black Hat," and "I have Aura." This one goes completely off-base: "Graduated with a degree from University of Brasilia." There you go.

So I can then ask the other model to verify, and it gives me an accuracy assessment. But the problem here is that the fourth LLM is still comparing with its own set of data, and I don't want that. I don't want LLMs to bring any data with them because I don't know where it came from.

Where it gets really interesting is when you do this: This is where I take my LinkedIn data. I'm going to ask the same question again, and it's going to hallucinate again. Now I'm a "CEO of Chain Pass, previous role..." But now I'm going to say, "Here is my LinkedIn page, here's the content, so here's your source of truth. Now review it."

This is literally what you guys should be doing. So you can see, this part here—"Experience..."—this bit here is my source of truth. All of that, and then it starts with the chatbot reviews from each one, and then it keeps going. And the coolest thing is the prompt size is big enough to hold this. Then you go, "Agent review." So now you can see inconsistencies, inaccuracies, etc.

The thing about this, and this is what I'm saying: you want to bring your own content. You want to bring your own information because you want to make sure you can debug everything. I don't want my models to bring anything. I want to have complete debuggability. If you think about this, I can track back every single problem, every single analysis, because I have all the history and all the analysis of all the threads. So that's really what you guys should be doing.

So in a nutshell, that covers the patterns. There's the thing: bring your own content, who's who, let's review it.

Again, this is coming your way. This is me taking one of those dashboards, the sort of Cyber Boardroom, which I tweaked a bit to be funny, and I said, "What the hell is this?" And then it gives me a decent answer, and then I could say, "I'm a CEO. Can you give me the email to send to my CISO?" So I say, "I'm acting as a board member. Give me the email to send to my CISO asking questions about that thing."

I think it's going to be great because I think we're going to get a lot more accountability, but you're going to get much better questions and answers from the other executives because they can play the game too.

## 6) Verification and Trust in AI Systems

So going back to deterministic generative outputs with provenance—I showed a bunch of patterns there. The reason why I'm also doing that, you can see I'm introducing air gaps in the system, and they are very important. In a way, generative AI is super powerful at translating content, but it's also ridiculously dangerous in the way it operates normally. This is because the generative AI is your most powerful API, and it's your most dangerous insider threat.

Can you imagine when these systems start to get compromised? We still don't know what a buffer overflow really looks like for a generative model. There could be models that have already been poisoned for a long time and have backdoors. They have all sorts of crazy stuff! That's why you want three different things. You want things in place.

Because on the flip side, what I like about generative AI is that it's not just technology that brings problems. I think for the first time, we have a technology that allows us to understand reality. So we can understand exactly what's happening in our networks, in our applications, in organizations, etc. It allows us to automate a lot of stuff, allows for personalized communications, and more importantly, personalized learning. So we can create really effective learning materials.

We can be 10 times more productive. The only people that are interested in getting rid of jobs are the same people that have always done that—the same crowd that outsourced everything to other countries, the same crowd that wants to drive costs to the bottom. Those are not the interesting people for you to work for, and they are not, I think, going to be very successful in the future. The same way that outsourcing came back because it didn't really work that effectively.

The thing about this is that good programming, good logic, good people will never be in more demand, and we're going to need even more because now that we can automate a lot of tasks, things are going to go out of control even more than they used to. So it's a massive opportunity for business. Of course, it's also a massive threat.

If you guys want to take some principles for how to do it safely, this is my recommendation: Start with read-only models. Don't have a model that learns—that's not your job, unless you have 200 million in the bank. You shouldn't be playing that game. And if you want anything that learns, do machine learning, don't do generative AI.

It's all about the prompts, and you can see in the demos I showed you: you bring your own content, and once you bring your own content, you control it. That's normal AppSec, normal engineering.

Then you have to assume that every piece of content and every prompt that you put into an LLM is exposed, which is why you only want to allow the person who has that content to access the LLM that has their content, because then you don't have that problem.

And you need to double down on identity and access control (IAC) and cybersecurity because we know what we're doing with this stuff.

Recapping: Generative AI is really bad at explaining how the output was created, and it's also very bad at self-awareness. You can see how it was manipulating the reality of the LLM just by changing the history of what was in there. They're not aware of it.

But generative AI is very good at understanding and connecting data, and it's very good at personalizing and customizing data. That's where you should be focusing. Those are the wins.

In cybersecurity, we have so many tools, so many processes, so many things that we need to do. More importantly, what I found was that there's a moment in cybersecurity where you hit the business, and it's always a very interesting moment. There's a moment where you can do a lot of your stuff—you're in your bubble—but there's a moment where you cannot change the security posture of the business without changing the business itself.

That's when I realized that we were in a game of changing the business. We were in a game of almost helping the business to help themselves, so they can develop things securely, implement securely, build stuff securely. That's kind of how we operate.

The key here is you have to have human ownership of the answers. The idea that you just get the AI to automate stuff—how can that go wrong? It's going to be a massive problem more and more because people are connecting stuff. So you need that human ownership, that common sense. But also, we can now bring common sense to some of our apps using generative AI to analyze things and to allow things to occur much more effectively.

And it's going to change everything. There are going to be some massive crashes, as always, but I think we can finally tackle those issues without too much code, and it's a perfect time. The boat hasn't sailed completely. You can still jump on board. I think it's a great time to really start to be involved.

Again, OWASP is an amazing organization to do that. I think it's a great hub of creativity, of innovation, of people that care about this stuff. I think the percentage of people that care about making the world a better place is kind of higher at OWASP, which I think is quite cool, especially as you get more involved—people really care. So it's a great place to be, but don't miss it, because this is going to be another major revolution.

I have some slides here—this is just why some companies panic. Microsoft is doing a great job, and all these guys...

This is kind of the picture that changed my life, because I realized that the square is the original, and the rest is augmented. So you have to imagine the mental model that the LLMs have to create in order to generate that, and you apply that to text. Again, that's Midjourney, that's a cake, but that's just whatever you can do with it. But that was the moment I realized that the mental model that the LLMs can create is something quite remarkable, and we need to understand more, which is really cool.

I talked about these patterns. I showed you the examples. The one that I think is very interesting is when you ask multiple questions. More interesting is when you do this: This is the executive thing I showed you. You take a question, you go to three LLMs, you put it to the fourth, and then you use that to consolidate the answer.

In fact, what you really should do is this, where you get another one and you ask: "Is that a good answer? Is that a good consolidation? Is the user okay? Can you also create consent? Can you create mappings? Is that malicious?" Etc.

What's cool about this is it becomes harder and harder and harder to compromise. You're putting air gaps in the middle of this, which is really interesting. You start to limit the access, especially if all of this is vision-controlled and you track all of it.

All this talk about RAGs—a lot of people are doing RAG [Retrieval-Augmented Generation] stuff. I'm still very skeptical because a lot of it is black magic. I still don't buy it. I think the stuff with graphs is a lot more interesting. I think you take the content, you summarize, you build graphs of it, then you navigate the graph. I think that will give you much better, again, deterministic and provenance of where the data came from. Otherwise, you go, "Oh yeah, it came from that vector." Cool, but how the hell did that vector come about? So I think you want to have that provenance. You want to have that connection with the data, and that's super important.

## 7) Best Practices for Using Generative AI Securely

Very quickly—you don't want to do this: input, generative AI black box, solution. This seems to be a lot of solutions out there. You kind of want to do this, where you do AppSec/AppDev engineering at the gate, then you have the black box, and you should view that thing as your most hostile component.

This is kind of what I was saying. You want to have a pipeline like the one I created, which is completely isolated. The guy who did the keynote in the morning had a good point: there's a lot of these models where the data goes in and ends up kind of half traveling around the world. You really want to segment that thing, and that's where you need good AppSec, good InfoSec, good practices, because you need to contain it.

Then you have a solution, you have human verification, human ownership. It doesn't mean that the human ownership is there all the time, but it's part of the original loop. Then you scale like we do with software.

Remember that that's your most vulnerable API. It's also your most dangerous insider threat. Can you imagine when somebody compromises an LLM that is a middleware application? It's not like SQL injection where you still have to do a bunch of stuff and extract data—it's like, "Hey, can you hack the organization from the inside? Can you start to list what's going on? Can you package the data?"

Can you imagine the kind of exploits you're going to have when you're dealing with an LLM, not a SQL database or whatever system you happen to land on? So don't do the stuff at the top. Do AppSec and cyber, which means what we do is even more important, and I think now we can scale very effectively.

What you really, really don't want to do is take that freaking black box that we still don't know how it works and plug it to your cloud environment, to your corporate environment, and your customer environment. This is one of those "What could go wrong?" situations, and this is what a lot of people are doing.

That's what I'm saying—if that's not on the threat model, then you're in for a surprise. And that's why you need to contain it. If you view that thing as isolated, you run the models, it's completely locked down, and then you do it like that.

And you want music... no, sorry, you want "MUSIC" loops [Measure, Understand, Solve, Implement, Communicate], and then every time there's a little thing you don't understand, you trigger an incident, you map it out, and then you bring back to normal.

I was going to dive into some principles. This is a really good one to mention: My party trick is to use P3s [Priority 3 issues] as training and P1s [Priority 1 issues] as learning themes—best way to learn things.

I always view that the job is to take risks. I really like this idea that you want the business to operate at the speed of customer experience and accept the risk appetite, which actually means that our job is to let the business operate insecurely. We have to stop this idea that it's the user's problem to click on things—that's how the freaking thing works! It's not their job. It's not the job of the business.

The job of the business is to operate at the speed and risk that they're comfortable with. In fact, we need to let them operate insecurely because, in a way, that's actually good for canaries and alarm bells. Defend what you don't want is to allow a little compromise over here to blow up half your company—that's the problem you want to tackle.

So I like the idea that you almost—but here's the thing: you need to allow a situation where the users will be compromised, but you want to have minimum to zero impact. Because you cannot have it both ways, and I think it's a much more healthy way of looking at the problem. So I highly recommend that.

We covered protecting the main thing. I want to show here—OWASP Top 10—the way I look at it is if you do all of this, then the only thing that is important is prompt injection. So I disagree with a guy who did a session earlier who said prompt injection is solvable. I don't think we're even close to doing that until we can properly separate code and data. I'm really worried that the exploits are ridiculous because this data is code.

Everything else—you have to assume this stuff... it's more responsibility, and then it's AppSec. So I think it's important that the really new thing—if you're doing the stuff on the left, if you're building models and all that stuff, then yeah, you have to care about all of that.

So super important: OWASP has never been more important and needed, and I think you should be involved and ride this wave.

My last sort of comments on this: I think we are at a time where our generation—and by that, I actually mean all the generations that are now involved—and I think it's really cool that in our industry, those of us who are older (I see some faces here), we are still super excited about this. And the new generation still has a lot to do.

There are other industries where, by the time the new generation arrives, it's like, "Dude, we've done it all." And there are others where the new generation has everything and the old generation has nothing. So I think it's really cool that we have space for everybody. We need a lot of people in our culture.

One of the things I try to do a lot, and you should try to do this, is we need to bring a lot more people from other industries into our industry. There's this thing called impostor syndrome, which a lot of people have. There's also this thing called trespasser syndrome, which is where people don't think they should be in cybersecurity.

I think that we finally have a way to solve this knowledge transfer gap that we have, which is using LLMs to learn. That was the only thing I couldn't do in the past very effectively.

In my team, I hired a guy that was on a shop floor that was into hacking. We hired him. A guy from the warehouse that was wearing some hacking tools, we hired him. I got a guy from the management of a store. I had another person from project management in the incident response team. I had a guy that was on the call center that was dealing with incidents—he was really pissed off with all the people abusing our customers. We put him leading fraud, managing Splunk.

There's a great amount of talent that we can bring to our industry, and again, that increases diversity of everything. But we need to make much better ways to learn, and I think this is a great moment. I feel this is a great time to be involved.

The things we do in the next decades, or the next five years, are going to make a massive difference. I do think that deep fakes and all the bad stuff is going to go up a level. I do think that will be good because it's going to force us to solve the provenance problem. It's going to force us to answer: Where did that information come from? How do I know this person is actually that person? How do I know who is who, what and where does the data come from?

I think solving that problem will make our society and what we do way, way better. And the place to do that is OWASP. So be involved, come to the summit that we're going to do in November in London, and I hope you participate and play around with my Cyber Boardroom that I was basically demonstrating. You can go online, you can run it locally, go to the cloud, and give me feedback.

## 8) Conclusion and Future Outlook

So in summary, I've covered a lot of ground today about generative AI, its potential, its risks, and how we can work with it effectively.

The key takeaways I want to leave you with:

First, generative AI represents a technological revolution that's even bigger than previous ones like the internet or mobile. It's not just another technology—it fundamentally changes how we can interact with information and systems.

Second, the distinction between "secure" and "safe" is crucial. We need to build systems that are not just technically secure but also safe in the broader context of how they're used. This often means creating air-gapped environments where vulnerabilities don't matter rather than trying to make inherently vulnerable systems secure.

Third, deterministic outputs with provenance should be our goal. We need to know where information comes from and how decisions are made. By bringing our own content, using multiple models for verification, and maintaining human oversight, we can achieve this.

Fourth, the tools and approaches I've demonstrated with the Cyber Boardroom project show that we can use generative AI to improve communication, scale risk management, and bridge gaps between technical and business stakeholders. These patterns can be applied in many contexts.

Fifth, the OWASP community has a vital role to play in this new era. We need open standards, best practices, and a community approach to tackle the security challenges of generative AI.

What excites me most about this moment is that we have an unprecedented opportunity to bring diverse talent into our industry. The barriers to entry are lower, and we can use these technologies to help people learn and contribute regardless of their background.

I believe we're at the beginning of a transformation that will ultimately make technology more accessible, more understandable, and potentially more human-centered. But we need to be vigilant about the risks, particularly around provenance, verification, and the potential for these systems to be compromised.

As deep fakes and AI-generated content become more prevalent, society will be forced to confront questions of trust and verification. This will be challenging, but I believe it will ultimately lead to better systems and approaches for establishing the provenance of information.

The place to do this important work is within communities like OWASP. I encourage all of you to get involved, contribute to projects, attend events like the upcoming summit in London this November, and experiment with these technologies yourselves.

The projects I've shown today, like the Cyber Boardroom, are open source and available for you to use, modify, and build upon. I welcome your feedback and contributions.

Thank you for your time and attention. I'm excited to see what we'll collectively build in the coming years as we navigate this new technological frontier together.