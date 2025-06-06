---
title: "Personalised Briefing for Dan Raywood on the Future of News"
authors: ["Dinis Cruz", "ChatGPT Deep Research"]
date: 2025/06/06
pdf_file: personalised-briefing-for-dan-raywood-on-the-future-of-news.pdf
back_link: /research/the-future-of-news
linkedin: diniscruz_personalised-briefing-for-dan-raywood-on-activity-7336773283159203842-RyBb
---

_by {{ authors | join(" and ") }}, {{ date }}_  

{{ download_pdf(date, pdf_file) }} {{ linkedin_post(linkedin) }} {{back_button(back_link)}}

## Introduction

This executive briefing is a synthesis of hundreds of pages of research by Dinis Cruz (primarily from *The Future of News and the Monetisation of Trust* report and related documents on **docs.diniscruz.ai**) distilled for **Dan Raywood**, Senior Editor at SC Media UK. 

The content draws heavily on open research sources such as *Monetising Trust and Knowledge: How News Providers can leverage Personalised Semantic Graphs*<sup>1</sup>, among others, to make these proposals accessible and relevant to Dan. 

These **proposals** – covering new revenue models and tech-driven approaches to journalism – are presented as suggestions (published under open-source/Creative Commons licenses) that have so far gained limited traction despite being shared on platforms like LinkedIn and research blogs. 

The goal here is to outline how these innovations could address challenges in news media, aligning with Dan's experience in cybersecurity journalism. 

This briefing introduces the key ideas at a high level; follow-up documents can then drill down into specific proposals if requested.

## Dan Raywood: Cybersecurity Editor with a Trust-Focused Vision

Dan Raywood is a seasoned B2B journalist with over 20 years of experience (17 of them covering cybersecurity)<sup>2</sup>. As Senior Editor at SC Media UK, he has reported on everything from advanced persistent threats and nation-state hackers to major data breaches and regulatory shifts<sup>2</sup>. Dan's editorial mission is to revitalize SC Media UK by delivering insightful, actionable content to the cybersecurity community, emphasizing trust and practical value in his reporting. In taking on the role, he has focused on providing **"actionable insights"** and discerning analysis to re-engage readers (with a strong focus on how global issues affect UK CISOs and practitioners). This background makes Dan an ideal persona for these proposals: he operates in a field where credibility and accuracy are paramount, and he is actively seeking **new content ideas and models** to strengthen audience engagement. In short, Dan's commitment to trustworthy, high-impact cybersecurity journalism aligns perfectly with a future-of-news framework that prioritizes **trust, credibility, and innovative monetisation**. The following sections outline that framework – a set of open proposals from Dinis Cruz's research – and how they could benefit a journalist and publication like Dan and SC Media UK.

## Diversifying Revenue: Micro and Nano Payments for Journalism

One of the central innovations proposed is a **micropayment** and **nanopayment** model for news. Instead of relying solely on subscriptions or advertising, media outlets can let readers pay tiny, granular amounts for individual pieces of content or time-limited access. Think of readers spending a few pence to read a single article or unlocking a "day pass" to a news site. This pay-as-you-go approach could complement or even replace blanket paywalls. Crucially, modern technology has removed the old barriers to micropayments: today's digital wallets and browser payment APIs enable **seamless one-click payments for even a few cents**<sup>3</sup>. In other words, the infrastructure for micro/nano payments exists – what's been lacking is the industry will to implement it<sup>4</sup>.

Under this model, **everyone benefits**. Readers gain flexibility and control – no more all-or-nothing paywalls – paying only for content they truly value, without the commitment of full subscriptions<sup>5</sup>. Publishers, in turn, tap into a much broader audience: all those casual readers who don't subscribe can still contribute revenue in aggregate. Importantly, this approach *"aligns monetary incentives with truth, transparency, and trust"*<sup>6</sup>. When consumers pay per article, they are more likely to spend on accurate, high-quality journalism and skip clickbait. This creates a direct feedback loop: **quality journalism earns financial support**, while low-value content is bypassed<sup>7</sup>. For example, a newsroom could even share a portion of each article's micropayment income with its author, giving reporters a tangible stake in the impact of their story<sup>8</sup>. This incentivizes journalists like Dan to produce in-depth, reliable reporting that resonates with readers, rather than chasing virality for ad impressions.

Potential benefits of micro/nano payments include:

- **For readers**: Freedom from subscription fatigue and the ability to support quality journalism directly on a per-piece basis⁹ ¹⁰. They pay for what they actually read, which increases satisfaction and perceived value.
- **For journalists/publishers**: New revenue streams from non-subscribers¹¹, direct market feedback on what content people value most, and a shift away from click-driven models toward rewarding content quality¹². High-value articles generate proportionate income, reinforcing editorial focus on truth and depth over clicks¹³.

Notably, **the technology to do this is already here** – digital payment systems, content management tools to meter access, and even cross-site aggregators that could coordinate payments exist today<sup>4</sup>. What's needed is for media organizations to adopt them. Every publisher could expose an API to let third-party aggregators or apps facilitate micropayments across sources. 

*Instead of complaining about platforms and AI scrapers "stealing" content, publishers should build the infrastructure to make paying for content easy and automatic*<sup>14</sup>. 

It's ironic that many news orgs lament monetisation challenges while offering few programmatic ways to pay them – very few have open content APIs or modern RSS feeds for easy content access, making it harder for audiences or AI assistants to integrate paid content<sup>15</sup>.

By embracing micro and nano payments, media companies can create sustainable new revenue streams **while making it easier for audiences to access quality journalism**<sup>16</sup>. 

In sum, micropayments can open journalism to a wider paying audience and break the vicious cycle of clickbait, replacing it with a virtuous cycle where trust and accuracy are financially rewarded.

## Monetising Trust as a Service (Credibility as a Product)

Beyond new payment models, Dinis Cruz's proposals stress the **monetisation of trust** – effectively turning journalistic credibility and verification into services that readers or partners would pay for. 

Trust and credibility have always been central to quality journalism, but now they can be explicitly **productized**. In practical terms, news organizations can leverage their expertise in fact-checking and integrity by offering **"Trust-as-a-Service"** to audiences, businesses, and other platforms<sup>17</sup><sup>18</sup>. This means the painstaking verification work that journalists like Dan do – confirming facts, vetting sources, providing context – no longer remains hidden in the background or merely a cost center. Instead, it becomes a **visible, premium product**.

For example, a publisher could expose a **real-time Verification API** that lets subscribers or corporate clients instantly check the authenticity of a claim against the publisher's database of verified information<sup>18</sup>. A company or reader could query, *"Is this claim true according to SC Media UK?"* – and get an immediate answer with source references. Likewise, a news outlet might offer a **"credibility score" service**: an API or feed that attaches trust scores and source annotations to news articles. Imagine an organization consuming a feed of cybersecurity news where every fact is vetted and accompanied by a confidence score and source attribution. Media outlets would thus **"monetise their core strength in verification and fact-checking"** by formalizing journalistic integrity into a service<sup>19</sup>.

Cruz's research outlines tiered offerings for such trust services<sup>20</sup>. At a basic level, general readers on a site might simply see a verification badge or a summary of sources for an article (building confidence at no cost). Meanwhile, **premium tiers** could be sold to professionals: paying clients get detailed credibility reports, historical evidence trails for claims, or even on-demand expert reviews of contentious statements<sup>20</sup>. In this model, a cybersecurity newsletter might charge an enterprise subscriber for a deep-dive credibility audit of each story – turning transparency and accuracy into a revenue feature. **Verification-as-a-service** not only brings in revenue, but also reinforces the value of accuracy by making it something consumers consciously choose to pay for, rather than a free afterthought<sup>21</sup>.

Another intriguing aspect is creating **expert networks and marketplaces around trust**. Research suggests **"trust network marketplaces"** could emerge, where verified experts (journalists, analysts, subject-matter experts) are matched with audiences or organizations seeking trusted insights<sup>22</sup>. For instance, SC Media UK could host a platform where subscribers pay extra to consult with experts or journalists (like Dan) directly for insight or analysis on breaking stories. Or a publication's archive of vetted research can be licensed to fact-checking agencies and AI systems training on reliable data<sup>23</sup>. Essentially, media organizations could monetize not just content, but their **knowledge and credibility**. An experienced journalist's reputation becomes **"reputation capital"** that can be packaged into software, data, or interactive services<sup>24</sup>.

All these trust monetization ideas share a common theme: they fund journalism by selling **trust and knowledge, not just stories**. This flips the usual dynamic – currently many newsrooms chase attention (clicks, virality) because they struggle to directly monetise trust. In contrast, a trust-as-a-service model means the more a newsroom invests in accuracy, depth, and verification, the more valuable its services become. It's a **shift from monetizing attention to monetizing credibility**. As Dinis Cruz notes, this approach realigns incentives by rewarding the **integrity** of journalism. It addresses the critique that *"many news organizations struggle to monetise trust effectively – often resorting to engagement-driven strategies at the cost of accuracy"*<sup>25</sup>. Instead of that conflict, aligning revenue with trust means doing the right thing journalistically also becomes the smart thing financially.

For Dan Raywood and SC Media UK, trust-as-a-service could be a natural extension of their brand. SC Media already has a reputation in cybersecurity; formalizing that into, say, a **"SC Trust API"** or a credibility dashboard for readers could both differentiate the publication and open a new income stream. Companies might even **prepay for credits or subscriptions** to such services – for example, a consulting firm could buy a subscription to query SC Media's verified breach database or to get monthly threat briefings from the editorial team. In fact, a news outlet of the near future might operate as both a publisher and a platform: publishing stories to the public, **while also offering data feeds, verification APIs, and custom intel services to those willing to pay for enhanced trust and insight**<sup>26</sup>. In this way, **trust becomes not just a moral asset but a monetisable product** – a commodity that news organizations can trade on, which directly supports their journalism.

## Personalized News Feeds and Semantic Graph-Driven Delivery

Another major innovation is the shift from one-size-fits-all articles to **personalized, graph-driven news experiences**. Today, most readers only ever see the final written article – a static piece of text – without any visibility into the reporter's underlying research, sources, or thought process. Cruz's vision is to **decouple the facts, data, and ideas behind a story from the story's final narrative form**<sup>27</sup>. By breaking a news story into a **structured knowledge graph** of its constituent pieces (facts, quotes, data points, expert insights, etc.), those pieces can be reassembled and presented in dynamic ways tailored to each user<sup>28</sup><sup>29</sup>.

In a GenAI-driven world, content that is **structured and machine-readable** becomes incredibly powerful<sup>30</sup>. If a publisher stores news content as a semantic graph – linking each fact to its source, each claim to evidence, each person to their credentials – then delivering that information can become as flexible as software. For example, from the **same** underlying set of verified facts, one reader could be shown an interactive timeline of an incident, another could get a voice-assisted chatbot summary, and another an in-depth technical report – all auto-generated from the shared knowledge base<sup>31</sup><sup>32</sup>. The article is no longer the sole product of journalism, but just one **view** of a richer information set. Readers who want more detail could click on a claim and immediately see its source, or pivot into a graph view of related stories and background data<sup>29</sup>. Those who only want the highlights could toggle to a summary mode. In short, each user gets a **persona-driven experience** drawn from the same factual backbone, allowing novices and experts alike to engage at their comfort level<sup>32</sup><sup>33</sup>.

Cruz references **MyFeeds.ai** as a prototype of this approach<sup>35</sup>. **MyFeeds.ai** is described as a tool that delivers personalized news feeds using AI and semantic graphs, effectively giving each user a bespoke "newspaper" drawn from many sources<sup>36</sup>. Importantly, in MyFeeds (and similar models) the AI doesn't operate as a black-box algorithm that mysteriously decides what you see. Instead, it provides **transparency and provenance** for its recommendations: it can explain why each article is in your feed, based on your profile and the content's context<sup>37</sup>. For example, *"You follow cloud security issues, and this article was included because it references a breach at a cloud provider"*<sup>38</sup>. This kind of explanation is a crucial trust feature – it turns the personalized feed into not just a convenience but a trustworthy assistant. The user can understand the rationale behind their news suggestions, mitigating the mistrust that often surrounds AI-curated content. In essence, the feed is **grounded in a semantic understanding of both the user and the content**, which combats the bias or opaqueness of typical newsfeed algorithms<sup>38</sup>.

From a business perspective, personalized semantic feeds open up new monetization opportunities hand-in-hand with the micropayment model. A platform like MyFeeds.ai could aggregate premium articles from many publishers into one feed, and handle the micropayments to each source seamlessly<sup>39</sup>. The reader enjoys a one-stop app (instead of juggling multiple websites or paywalls), and behind the scenes each publisher gets paid per article the user reads<sup>40</sup>. This **cross-publisher feed model** means collaboration rather than competition: a dozen outlets might all contribute to a CISO's daily personalized briefing, and each is compensated fairly out of the user's wallet<sup>41</sup>. For journalists like Dan, it means their work can reach exactly the audience who needs it (regardless of which site they normally visit), and every **meaningful view** is revenue. A cybersecurity article Dan writes could automatically find its way into the personalized feeds of, say, finance-sector CISOs concerned about a new threat – extending its reach beyond SC Media's native audience, yet still earning SC Media and Dan micro-revenues when read.

In summary, graph-driven personalization allows news to be **modular, interactive, and tailored** without losing the integrity of the underlying reporting. It decouples content from presentation, enabling a single body of journalism to spawn many forms – all with the full provenance of facts intact. This is a boon in the fight against information overload (readers get only what's relevant to them) and also a defense against misinformation: when every claim in a feed can be clicked and traced to its verified source, misinformation has a hard time taking root.

## Fact-Driven Traceability and Anti-Misinformation Safeguards

A powerful side-effect of structuring news into semantic knowledge graphs is the enhancement of **traceability** – every fact and quote in a story can be tracked back to its origin. This has significant anti-fake-news properties. In the proposed model, nothing is a dead-end: if an AI system or a reader queries a claim, the system can show where it came from (e.g. *Source: Interview with X, or Document Y, published on Z date*). Readers and editors can literally **trace fact provenance** for any element of a story<sup>42</sup>. This makes it dramatically harder for false information to be inserted or spread, because unsupported assertions would be exposed as having no source in the graph. Large Language Models (LLMs) and AI content generators, which often hallucinate facts, could be constrained by these graphs: any AI-generated content that strays beyond the verified graph would flag itself by lacking supporting data – essentially hitting a "trust wall." In practice, this could mean news organizations have a way to automatically **detect AI-generated misinformation**: if an article or AI draft contains statements that cannot be found or verified in the shared knowledge graph, those become suspect. In a workflow where facts are decoupled and centrally stored, an editor (or even an automated system) can run a "graph check" on a piece to see if every claim links to a vetted node. If something doesn't, it's a red flag for further verification.

This approach directly addresses the challenges of the GenAI era. We already see AI being used to auto-generate news stories and the looming risk of deepfakes or fabricated news at scale. By adopting a **graph-backed** content system with rigorous provenance, news providers make their content **self-documenting**. It's akin to having footnotes for every sentence, but in a machine-checkable form. It reinforces trust with readers (who can delve as deep as they want into sources), and it equips newsrooms with new tools to uphold accuracy. In fact, structured content is likely to be favored by AI assistants and search engines in the future. News that comes with metadata, source links, and context will be ranked higher and used more by intelligent systems (because it's easier to verify and parse)<sup>30</sup>. In that sense, investing in these structures is also a bet on future-proofing visibility: **structured, AI-ready content ensures news remains visible and valuable in an era where AI assistants and algorithms curate information**<sup>43</sup>.

Moreover, by decoupling facts from narrative, newsrooms enable content **reuse and remixing** in trustworthy ways. An investigative piece's research could live on as part of an ever-growing database of facts on that topic, which other reporters (or even external services) can query and build upon – always with attribution back to the original reporter or outlet. For example, the data behind a series of cybersecurity breach stories could form a continuously updated "breach knowledge base" that readers or AI tools subscribe to. A controversial opinion piece could be accompanied by a visual debate graph mapping each claim to supporting or opposing evidence, helping readers see a 360° view of the issue. All of this fosters media literacy and critical thinking, empowering readers to explore the context behind news. It also opens new channels to monetise: a newsroom could license its structured data (e.g. a feed of verified facts on cyber incidents) to businesses or educational platforms, on a usage-based model<sup>44</sup>. In essence, **news becomes not just a story, but a structured knowledge service**. This reinforces trust (because transparency is built-in) and generates new revenue (because the content can serve many purposes).

By focusing on verifiable facts and their relationships, news organizations can drastically improve their resilience against misinformation. **Fake news thrives in opacity and overload**; these proposals counter that with transparency and personalization. When every piece of content clearly differentiates what is reported fact, what is the journalist's analysis, and what is source material, it becomes much easier for consumers and algorithms to filter out falsehoods. It's a modern, proactive take on editorial integrity – **using technology (graphs, metadata, AI) to scale up the traditional values of journalism (accuracy, attribution, context)**.

<div style="page-break-before: always;"></div>

## Overlaps and Opportunities for SC Media UK and Dan Raywood

How do these ideas come together in practice, and why are they relevant to Dan Raywood and SC Media UK? 

Below is a semantic relationship graph (in text form) illustrating the key connections between Dan's role and the proposals discussed, highlighting concrete opportunities:

```
Dan Raywood (Cybersecurity Editor, SC Media UK):
├──────────────────────────────────────────────
├── Focus      → Cyber threats, trust, and delivering actionable 
│                insights to readers²
├── Experience → 20+ years in cybersecurity journalism 
│                (established credibility)²
└── Goal       → Innovate news delivery & monetization to better 
                 serve and grow the audience
```

```
Dinis Cruz's Proposals (Open-Source Initiatives for News):
├────────────────────────────────────────────────────────
├── MyFeeds.ai            → Personalized AI-curated news feeds 
│                           (tailored by user role and interests)
├── Trust-as-a-Service    → Verification APIs and credibility scoring 
│                           services for content
├── Semantic Knowledge    → Structured fact databases with full provenance 
│   Graphs                  for news content
└── Micro/Nano Payments   → Pay-per-article and credit-based payment models 
                            for news consumption
```

```
Overlaps & Opportunities:
├───────────────────────
├── Personalized Feeds      → SC Media UK could pilot a custom cybersecurity 
│                             news feed (e.g. a "CISO Daily Brief") powered 
│                             by MyFeeds.ai concepts, combining SC Media's 
│                             content with other sources in one tailored app.
├── Trust Services          → Leverage SC Media's reputation by offering 
│                             trust metrics or "verified by SC" badges and 
│                             APIs. For instance, SC Media could sell a 
│                             subscription to an enterprise-grade threat intel 
│                             feed where every fact is vetted – turning 
│                             editorial integrity into a product.
├── Micropayments Ecosystem → Integrate SC Media content into a cross-publisher 
│                             micropayment system. Dan's articles could be 
│                             accessed via one-stop platforms (like a 
│                             personalized news app) where readers pay per 
│                             article using a unified wallet – giving SC Media 
│                             incremental revenue and new reach.
└── Shared Vision           → Both Dan and Dinis prioritize trust and quality 
                              in journalism. SC Media UK, under Dan's 
                              leadership, could become a testbed for these 
                              innovations – demonstrating how a trusted 
                              cybersecurity news brand can embrace new tech 
                              (AI, graphs, payments) to engage its community 
                              and sustain itself.
```

In this graph, we see that Dan's editorial strengths (credible cybersecurity reporting and a drive for engagement) directly align with Dinis Cruz's future-of-news proposals. **SC Magazine UK** stands to benefit as an early adopter: it could implement **personalised feeds** to cater to different segments of its readership (ensuring that CISOs get the technical deep-dives they crave, while other readers get big-picture analysis, all from the same content pool). 

It could deploy **Trust-as-a-Service** features to add value for subscribers – for example, giving paying members access to a dashboard of verified threat reports, or partnering with industry to provide a credibility score API for cybersecurity news (positioning SC Media as not just a news site, but a verification authority). By experimenting with **micropayments**, SC Media could monetize its archive of specialized content, letting casual visitors pay per read, which is particularly relevant for niche expert content that readers might find via search or social links. 

The **overlap is clear**: Dan's focus on trust and actionable insight is the editorial counterpart to Dinis's technical-framework focus on trust and monetisation. Together, they point toward a journalism model where quality and trust form the cornerstone of both **audience engagement and revenue generation**.

## Conclusion: A Trust-Powered Future for News

This personalised briefing has highlighted a suite of proposals that reimagine the future of news in the era of AI and information overload. From micro-payments to trust networks to semantic content graphs, these ideas form a cohesive vision for **GenAI-optimized journalism**<sup>45</sup> – one that does not discard traditional journalism, but enhances and future-proofs it. Implementing such changes will require both cultural shifts (e.g. journalists embracing more transparent, modular content creation) and technical development (e.g. building payment APIs, knowledge graph databases, and AI-driven personalization tools). The payoff, however, could be a more resilient and sustainable news ecosystem than we have today. 

By aligning incentives correctly, the industry can **escape the trap of clickbait** and instead focus on delivering **what readers truly value: accurate, relevant, and actionable information** <sup>46</sup><sup>43</sup>.

For a seasoned journalist and editor like Dan Raywood, understanding this paradigm shift is key to seeing where he can contribute and benefit. Diversifying revenue sources means reporters are no longer solely dependent on ad-driven pageviews; their expertise and trustworthiness gain **tangible economic value**. The relationship with readers becomes richer: rather than a one-off transaction (article published, reader reads), it can turn into an ongoing engagement – readers might follow a journalist's verified identity profile (an "identity graph" of the author's credentials and past work) to decide if they trust them, financially support that journalist's work per article or via micro-donations, and even dig into the source material behind the reporting if they choose<sup>47</sup><sup>48</sup>. All of these reinforce a virtuous cycle: **trust drives revenue, and revenue funds trust-building journalism**<sup>48</sup>.

In closing, the key areas below summarizes the key takeaways from this briefing – core innovations that could define a new **multi-revenue, trust-centered model** for journalism:

- **Structured, AI-ready content:** Organizing news into knowledge graphs with metadata ensures it remains visible and valuable when AI assistants curate information, and allows content to be repackaged in multiple forms without loss of context<sup>43</sup>.
- **Micro & nano-payments:** Enabling tiny payments for individual pieces of content creates new revenue streams from non-subscribers, aligning payment with content value. This makes it easy for audiences to pay for quality journalism and directly rewards high-value reporting<sup>49</sup><sup>7</sup>.
- **"Trust-as-a-Service" models:** Publishers can monetize credibility by offering verification tools, credibility scores, and expert insights as premium services. Trust and fact-checking become products, turning journalistic integrity into a revenue-generating asset<sup>18</sup><sup>25</sup>.
- **Personalized feeds & mini-app UIs:** Semantic graphs enable each user to receive a tailored news experience (e.g. role-specific feeds, interactive story apps). This boosts engagement and can integrate with micropayments seamlessly – a user's one feed might aggregate content from many outlets, with frictionless payment, benefiting all<sup>50</sup><sup>39</sup>.
- **Decoupling facts and opinions:** Separating the raw facts and research from the final written narrative increases transparency and reusability. Readers (and AI systems) can trace every claim to its source<sup>29</sup> or view content in different formats (timeline, dashboard, article, etc.), which reinforces trust and opens up new ways to use and monetize content<sup>51</sup>.

By focusing on these innovations, news professionals like Dan can help create a future where quality reporting not only survives but thrives – powered by technology that values truth and expertise. It's a future in which a publication's **trust** is its most valuable currency, and where the business model finally aligns with the core mission of journalism. As Dinis Cruz's research suggests, **trust can be monetised without compromising integrity**, if done through the right channels. The next step is translating these proposals into action: pilot projects, prototypes (perhaps an SC Media UK lab initiative?), and cross-industry collaborations. With experienced media figures like Dan engaging with technologists and open research, the vision of a **trust-powered, multi-revenue news model** can become a reality – benefiting journalists (through new revenue and reach), publications (through loyal, paying audiences), and the public (through access to trustworthy, well-supported news)<sup>52</sup>.

For deeper exploration of specific ideas, see Dinis Cruz's articles such as "Monetising Trust and Knowledge: How News Providers can leverage Personalised Semantic Graphs" (an in-depth look at knowledge graphs and trust APIs) and "The Future of News: Building Trust Through Fact Provenance" (focusing on verification frameworks and content provenance). These resources expand on the concepts introduced here. In the meantime, this briefing serves as an invitation for Dan Raywood – and the SC Media UK team – to envision how the **future of news** might look if we bring together the best of journalism's values with the best of today's technology. The opportunity is clear: a news ecosystem that is more personalized, more transparent, and more financially empowering for those who produce and consume credible information. It's an exciting, necessary evolution, and one that Dan is uniquely positioned to champion moving forward.

<div style="page-break-before: always;"></div>

### References

Monetising Trust and Knowledge: How News Providers can leverage Personalised Semantic Graphs - Dinis Cruz - Documents and Research

https://docs.diniscruz.ai/2025/02/02/monetising-trust-and-knowledge-for-news-providers.html

¹ ¹⁵ 

----

Dan Raywood | SC Media

https://www.scworld.com/contributor/dan-raywood-2

²

----

The Future of News: Building Trust Through Fact Provenance

https://docs.diniscruz.ai/2025/02/05/the-future-of-news-building-trust-through-fact-provenance.html

³ ⁵ ⁶ ⁷ ⁸ ¹⁷ ¹⁸ ¹⁹ ²⁰ ²¹ ²² ²³ ²⁴ ²⁵ ²⁶ ²⁷ ²⁸ ²⁹ ³⁰ ³¹ ³² ³³ ³⁴ ³⁵ ³⁶ ³⁷ ³⁸ ³⁹ ⁴⁰ ⁴¹ ⁴² ⁴³ ⁴⁴ ⁴⁵ ⁴⁶ ⁴⁷ ⁴⁸ ⁴⁹ ⁵⁰ ⁵¹ ⁵²

----

The Future of News Monetization: Why We Need Micro and Nano Payments

https://www.linkedin.com/pulse/future-news-monetization-why-we-need-micro-nano-payments-dinis-cruz-vdaee

⁴ ⁹ ¹⁰ ¹¹ ¹² ¹³ ¹⁴ ¹⁶