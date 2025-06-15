# Analysis of the Current Site Structure and Proposed Improvements

## Current Structure: Usability and Discoverability Issues

**Site Organization:** The site (docs.diniscruz.ai) is organized as a documentation hub for Dinis Cruz’s research content. It currently uses a hybrid navigation system: a chronological archive by year/month/day in the sidebar, alongside a set of broad **research categories** (e.g. Cyber-Security, Development, Graphs, etc.) listed under a “Research” menu. The homepage serves as an introduction to Dinis and the site’s purpose, stating that it hosts research on *“AI, security governance, and the future of knowledge sharing”*. It lists the key topic categories, but provides no description for each (simply a bulleted list of category names). A separate “Resources” menu exists (currently containing a **Presentations** page of past talks).

**Discoverability Challenges:** This structure poses several usability challenges for a broad audience (developers, researchers, and the general public alike):

* **Chronological Navigation Dominance:** The sidebar’s extensive chronological list of posts by date can be overwhelming and not intuitive for new visitors. Relying on date archives (“2024 → 02 → 22 → *Post Title*”) to navigate content forces users to know *when* something was published, which most won’t. As one UX author notes, *“rather than going sequential, a sensible, straightforward and seamless categorisation will make it easier for your visitors to explore what you’ve got to offer”*. In other words, listing content purely in chronological order isn’t necessarily logical for users whose priority is finding relevant topics, not recent dates. Currently, the site does offer categories as an alternative, but the **date archive is given equal or greater prominence**, which can distract or confuse users looking for themes or specific subjects.

* **Category Clarity and Organization:** The idea of grouping content by category is a strength – it aligns with best practices that encourage clear, topical navigation over date-based browsing. However, some of the category groupings and labels on the site are not immediately clear to all audiences:

  * *Europe and Learning:* This category combines two disparate themes (European tech/policy content and Learning/education content) under one label. Such a combination is not a mutually exclusive category and could confuse users. Nielsen Norman Group research stresses that using **clear language and mutually exclusive categories** is crucial to avoid user confusion. A visitor interested in Europe’s AI policy versus someone looking for learning/education research may not realize both topics reside together.
  * *Projects and Business Ideas:* This category is descriptive but somewhat long. It contains a mix of project proposals, MVP write-ups, and business plan ideas. While the content fits here, the label could possibly be shortened or split (e.g. “Projects” vs. “Business Ideas”) for clarity.
  * *Development:* This category currently holds very little content (just one technical article). Its purpose might be unclear – is it about software development practices/tools? If it remains a standalone category, it needs a clearer definition for users. Otherwise, such sparse content might be folded into another relevant category.
  * The other categories (Cyber-Security, Graphs, Future of News) are more straightforward by name. However, none of the category **landing pages** provide an introduction or context; they jump straight into lists of posts. This lack of descriptive overview on category pages hinders newcomers. Users have to infer what “Graphs” or “Cyber-Security” entails from the post titles alone. Each category page is essentially an index of links with subheadings, but no summary of what the category covers.

* **Homepage Focus:** The home page is heavily focused on Dinis Cruz’s bio and credentials (which does establish credibility), but it does little to funnel users into the content. The only navigation it offers below the bio is the list of categories. There is **no highlight of recent or popular research pieces on the home page**. A new visitor must either click a category (without knowing what’s inside) or use the side menu. This could be a missed opportunity to immediately engage users with current or important content. As Nielsen Norman Group notes, effective navigation **“shows people what they can find on the site”** at a glance. Right now, the site’s main navigation hints at topics, but the homepage itself doesn’t showcase any examples of the research (for instance, there are no featured articles or latest updates displayed). General audience members might not scroll through the chronological menu, so failing to surface key content on landing pages can reduce discoverability.

* **Search vs Navigation:** The site appears to have a search function (the text “Initializing search” suggests a search bar is available). While search is useful, it should not be the sole means of finding information. Users who don’t know exactly what to search for rely on the site’s navigation structure to guide them. Currently, the navigation could do more to guide exploration. For example, if a casual visitor interested in “AI in education” arrives, they might not immediately realize that content lives under “Europe and Learning” or that there was a post about “Generative AI and the Future of Learning.” Good information architecture should reduce the reliance on trial-and-error searching by clearly organizing content in intuitive categories and indexes. *“Site search is vital… However, if you’re considering pushing search at the expense of navigation, think again. Navigation serves important functions: it shows people what they can find... Using navigation categories is often faster and easier for users than generating a good search query.”*. In summary, the current nav structure could do more to *show* what’s available.

* **Content Volume and Scalability:** As more content (blog entries, research papers, etc.) gets added, the current approach may become unwieldy. The chronological list will grow every year, potentially cluttering the sidebar. The category list might also evolve. Without a clear, scalable structure, users could have trouble finding older yet relevant content. For instance, content that remains valuable (“timeless” research) might get buried under the date archives. The site should ensure that older content is still accessible through logical categories or an archive page, rather than solely via an expanding date menu. Archive pages and indices exist to mitigate this (e.g., a blog index page that shows all posts in reverse chronological order, or archive by year), but on this site the archive is only visible as the sidebar list. There’s no dedicated **“All Posts”** or **“Latest Updates”** page that a user can visit to see recent entries with context.

**Summary of Issues:** In its current state, the site has rich content but the discoverability is hindered by a lack of user-centric structure:

* Navigation is cluttered with a timeline view that is *“chronological by design but not necessarily logical”* for users seeking content by topic.
* Categories exist and are a promising organizing principle, but they need clearer presentation (better labeling, introductions, and possibly reorganization of certain categories to be more intuitive and mutually exclusive).
* The homepage and other landing pages are not leveraged to guide exploration — for example, no summaries or featured content to direct various audience segments (developers might want technical pieces, general public might look for high-level insights, etc.).
* The site does not currently emphasize its **latest or updated content** in the navigation structure, which could be important for repeat visitors or those looking for what’s new (especially given the fast-moving nature of AI and security research).

In the next sections, we propose improvements to the site’s information architecture that address these issues, making it easier for all audience types to find and explore the content.

## **a)** Improved Information Architecture for Navigation and Landing Pages

To enhance discoverability and usability, we recommend a restructured information architecture focusing on the **core navigation menu and key landing pages** (homepage and category index pages). The goal is to present content by topic and relevance, rather than by date, while still accommodating frequent updates. Below is a proposed structure:

* **Top-Level Navigation:** Simplify the main menu to focus on content categories and important sections, rather than raw timelines. For example:

  * **Home** – A welcome/overview page (the landing page) that introduces the site *and* immediately provides entry points to content (featured topics, latest updates).
  * **Research Areas** – A section (could be a menu dropdown or separate page) that highlights the major research categories. This could either be a non-clickable menu label with sub-items for each category, *or* a landing page listing all categories with descriptions. Given the current setup, keeping a top-level “Research” with six sub-categories is acceptable (Material for MkDocs supports a limited number of categories in nav). The key is that each **Category** should be clearly labeled (using user-friendly terms) and lead to a category landing page.

    * **Cyber-Security** (category page)
    * **Development** (category page)
    * **Graphs** (category page)
    * **Future of News** (category page)
    * **Projects & Ideas** (category page – renaming “Projects and Business Ideas” for brevity)
    * **Europe** (new category page) and **Learning** (new category page) – here we suggest splitting the combined “Europe and Learning” into two distinct categories. This yields seven categories total. If that feels too many for the top nav, an alternative is to keep “Europe & Learning” as a label but **use sub-sections within that page** (as is already done) to clearly distinguish content about Europe’s AI governance and content about Learning. However, for clarity, separate categories are preferable so that each is *mutually exclusive* and focused. Each category link in the nav should be directly clickable (not just an expand toggle) – clicking it should open the category’s landing page (with introduction and list of posts).
  * **Updates** (or **Blog** or **News** – whatever term fits best) – A section dedicated to **recent content and archives**. This could be realized in two ways:

    1. As a **“Latest Updates”** page that lists recent posts (e.g. last 5–10 posts) with titles, dates, and brief excerpts, giving visitors a quick way to see what’s new. Regular blog-style updates (like changelogs or new publications) can be listed here in reverse chronological order. This page would essentially serve as the blog index.
    2. Additionally (or alternatively), an **Archive** page that provides access to all past posts by date (perhaps organized by year). This would replace the need for the current sidebar date-tree. Instead of showing every year/month in the side menu, a single **Archives** link can take users to a page that neatly lists content by year and month. This keeps the navigation menu clean while still supporting chronological discovery when needed.
       *Rationale:* This approach surfaces new content more clearly (through a “Latest Updates” listing) and offers a cleaner archive for older posts, without cluttering the main menu. It supports regular content additions because users can always check “Updates” to see new entries, rather than hunting through the sidebar.
  * **Resources** – Keep this section for supplementary content like presentations, datasets, or external links. Currently it only has **Presentations**, which is fine. In the future, if more resource pages are added (say “Whitepapers” or “Tools”), they can be listed here. The Presentations page itself can remain a simple index of talks, but we’ll improve its layout slightly (see part (b) below).
  * *(Optional)* **About** – Consider a dedicated “About” page for Dinis Cruz, containing his bio, background, and perhaps a portrait. This would separate the personal background info from the Home page, allowing the Home to focus more on content. This is optional; one could also keep a concise bio on the Home page and forego a separate About page. If included, an About page should be easily accessible (either as a top-level menu item or linked from Home in a prominent way).

* **Homepage Revamp:** The Home page should serve as a friendly gateway for all audiences. Instead of just a long biography followed by category links, restructure it into clear sections:

  1. **Hero Introduction:** A brief welcome message or tagline that explains what this site is. For example: “*Welcome to Dinis Cruz’s Research Hub – exploring the intersections of AI, cybersecurity, governance, and knowledge sharing.*” Keep it to one or two sentences that capture the essence (as the current text does, mentioning *AI, security governance, and future of knowledge sharing*, but make it more prominent).
  2. **About Dinis (Summary):** A short paragraph (2-3 sentences) highlighting who Dinis is – e.g., “Dinis Cruz is a cybersecurity leader and researcher with experience as a CISO and a passion for open-source and AI innovation.” (Much shorter than the current multi-paragraph bio). Include a call-to-action link like **“Learn more about Dinis”** that goes to the full About page or LinkedIn, for those interested. This way, general visitors get context without wading through the entire resume on the front page.
  3. **Key Research Areas:** Instead of a plain bullet list of categories, present the research categories in a more engaging way. This could be a grid or list of **highlighted topics**, each with a concise description. For example:

     * **Cyber-Security** – *“Application security and threat modeling research, exploring novel ways to manage cyber risks.”*
     * **Graphs & Knowledge** – *“Semantic knowledge graphs and their applications in security, data modeling, and AI.”*
     * **Future of News** – *“Innovations to build trust in journalism and media, from fact provenance to monetization strategies.”*
     * **Projects & Ideas** – *“GenAI-driven projects and business ideas, including prototypes and venture concepts Dinis is exploring.”*
     * **Europe** – *“European initiatives in tech governance and AI (e.g., EU AI strategy, sovereign cloud, regulatory frameworks).”*
     * **Learning** – *“The future of learning and education in the age of AI.”*
     * **Development** – *“Technical development insights and tools (for example, data pipeline architectures, programming language experiments).”*

     Each of the above would link to the respective category page. By providing a one-line description, **users immediately grasp what each topic covers**, reducing ambiguity. This aligns with usability guidelines to use straightforward language and avoid “clever” or unclear labels.
  4. **Latest Updates or Featured Content:** A section on the homepage should highlight either the most recent posts or a few “featured” pieces of content. For instance, a **“Latest Research”** section listing the 3 most recent articles with their title, date, and a two-sentence summary. This catches returning visitors up on new content at a glance. It also shows first-time visitors some examples of what the site offers (making the content real and enticing). If certain cornerstone articles or popular posts are identified, those could be featured as well (e.g., “Popular: *My Journey Building a GenAI Startup*”). This section would be regularly updated as new content is added (which is feasible since adding a new post could automatically appear if the site uses a dynamic listing or one can manually update the home page periodically).
  5. **Navigation Aids:** At the bottom of the homepage (or in the footer), consider adding quick links: for example, **Subscribe/Follow** (if there’s a newsletter or social media), **Contact** info, and perhaps a brief note on how to use the site (like “Use the menu above to explore topics or search for specific keywords”). These are minor, but can improve the experience for general public users who may not be accustomed to navigating a docs-style site.

* **Category Pages as Landing Pages:** Each category page should be treated as a mini-landing page for that topic area, not just a list of posts. We propose the following improvements to category pages:

  * **Descriptive Introduction:** Begin each category page with a short **introductory paragraph** (or even a single clear sentence) explaining what that category encompasses. This helps orient visitors. For example:
    **Cyber-Security:** *“Articles focused on cybersecurity, including application security, threat modeling, and innovative strategies to manage cyber risk.”*
    **Graphs:** *“Research on semantic graphs and knowledge modeling – exploring how graph technologies and AI-driven knowledge bases can enhance security, legal frameworks, and data analysis.”*
    **Future of News:** *“Insights into the future of journalism and news media – covering ways to strengthen trust, verify facts (fact provenance), and new models for news monetization.”*
    **Projects & Business Ideas:** *“Outlines of experimental projects and business proposals led by Dinis, often leveraging Generative AI and cybersecurity expertise. These range from MVPs and tools to full startup concepts.”*
    **Europe:** *“Explorations of Europe’s role in tech and AI – including EU policy, regulatory ‘superpower’ moves, and initiatives like sovereign cloud infrastructure for an open, AI-enabled Europe.”*
    **Learning:** *“Research on learning and education in the AI era – how generative AI and new technologies can transform learning experiences and education systems.”*
    **Development:** *“Technical development topics, such as software engineering tools, frameworks, or unique approaches to programming (for example, using unconventional languages or deterministic pipelines).”*

    These intros immediately tell a newcomer what kind of content they will find in that category, using accessible language (no unexplained acronyms or internal jargon).
  * **Logical Grouping of Posts:** Continue grouping related posts under subheadings as is already done in some categories, but ensure the group labels make sense. For instance, in Cyber-Security, posts are grouped under “Threat Modeling”, “SAST”, etc. This is great because it further organizes content. Make sure these subheadings are present and consistent. In the **Graphs** category, if posts are currently grouped under “Ontologies and Taxonomies”, “Cloud”, “Standards and Governance”, those seem appropriate. We might refine or add groupings as needed when content grows. For **Future of News**, all posts relate to trust and provenance in media, so an intro paragraph might suffice without additional sub-grouping (unless one distinguishes between technical solutions vs. business aspects in news). The **Projects & Ideas** page already divides content into “Project briefs”, “Business Ideas/Plans”, and “Misc research” – this is effective, and should be maintained or refined (maybe rename “Projects briefs” to “Project Briefs” for capitalization consistency, etc.). The key is each category page should be **scannable** – with sub-headers breaking up long lists, so users can quickly find a sub-topic of interest.
  * **Cross-Navigation:** On category pages, provide links that encourage exploration of other categories or returning to an index. For example, a **“Back to Research Index”** link or buttons for “< Previous category | Next category >” could be at the bottom, so that after reading one category, the user knows how to navigate to others. Currently, a “Back to Index” link is shown (which presumably goes back to the main index or home). We should clarify that link to maybe say “Back to All Topics” and ensure it goes to a useful overview (perhaps the Research Areas page or home). Additionally, if a particular post in one category is highly related to another category’s topic, consider adding a note or link. For instance, a post in “Europe” about standards might link to related “Cyber-Security” content about standards, if applicable. These cross-links can be done manually in content or via a “Related Posts” feature if available, improving the interconnected feel of the content.

* **“Updates”/Blog Page:** Implement a main **blog index page** that lists posts in reverse chronological order with excerpts, as suggested by the MkDocs blog plugin guidelines. This page (which could simply be the “Home” of the blog section) would show maybe the latest 5–10 posts with a snippet of each. It serves users who want a chronological feed (“What’s new or what did I miss last month?”). It also helps keep the navigation tidy by offloading the year/month archive out of the sidebar. If a user wants older content, they could scroll that page or jump by year via an archive link. The **archive by year** can either be a list of years on the Updates page or a separate Archive page. The important part is that the main navigation would no longer need to list every year and month (those can be hidden from the nav tree to reduce clutter). Instead, just one **Updates** link encapsulates it. This change makes the core navigation **more concise and user-focused**, highlighting topics rather than dates.

* **Consistent Terminology and UI:** Ensure the naming in navigation is consistent and easy to understand:

  * Use plain terms like “All Posts” or “Updates” instead of something like “Archive” which some lay users may not immediately recognize (though “Archive” is fairly common, “Updates” or “Latest” is friendlier).
  * Keep category names short but descriptive. For example, “Projects & Ideas” instead of the longer “Projects and Business Ideas” (users will understand it, and it fits better in a menu label). Likewise, if “Europe and Learning” is split, just “Europe” and “Learning” are straightforward.
  * Avoid audience-based labels (the site wisely does not use labels like “For Developers” or “For Researchers”; it uses content-based labels, which is good because segmenting navigation by audience can backfire). Continue focusing on content subjects.
  * If possible, use the Material for MkDocs feature to make the category index pages act as section indexes (so that clicking the category name in nav directly opens the index, not just expands it) – this was likely already configured given the current behavior.
  * Highlight the active section in nav clearly, so users know which category they are browsing. Material theme usually does this by expanding the section.

This improved architecture prioritizes **topic-based exploration** with clear pathways, while still supporting chronological discovery in a more condensed way. It emphasizes the site’s key research areas (as listed on the home page) by giving each proper weight and explanation, and it sets up the navigation to handle new content gracefully. New blog entries will simply appear in the “Updates” feed and within their respective category – users can find them by topic or by recency. The structure is scalable: if Dinis starts a new area of research, a new category can be added (ideally only after enough content justifies it, to keep categories limited). Conversely, if some categories remain very small, the site can decide to merge or at least de-emphasize them (for example, if “Development” stays sparse, it might be listed last in nav or combined with another category or labeled “Misc Tech” – though for now, giving it a proper intro might help attract contributions to it).

## **b)** Content Recommendations for Key Navigation Pages

Below we provide proposed content structures for the **revised landing pages and navigation pages** discussed. This includes suggested page titles, introductions, and section breakdowns. The content is written to be clear and accessible to the site’s broad audience, avoiding unexplained jargon and highlighting why each section is relevant.

### **Home (Landing Page)**

**Title:** Welcome to Dinis Cruz’s Research Hub

**Introductory Paragraph (Tagline):**
*Exploring the future of cybersecurity, AI, and knowledge sharing.* This site hosts the latest research, ideas, and projects by **Dinis Cruz** – focusing on generative AI, security governance, and innovative ways to share knowledge.

**About Dinis (Brief):**
Dinis Cruz is a cybersecurity expert and AI researcher with a track record as a CISO and an open-source advocate. He has led initiatives in application security, served on the OWASP Global Board, and now spearheads projects at the intersection of AI and security. *(For more on Dinis’s background and work, see the **About** page or his LinkedIn.)*

**Key Research Areas:** *(Browse by topic)*

* **Cyber-Security –** Improving how organizations understand and mitigate cyber risks. Topics include threat modeling, secure software development, and novel AppSec approaches in the age of AI.
* **Graphs & Knowledge –** Using semantic knowledge graphs and AI to map information. Research on how graph technology can enhance security analytics, code analysis, and decision-making through better data connectivity.
* **Future of News –** Building trust and value in journalism. Covers fact-checking with AI (fact provenance), combating misinformation, and new content monetization models for news media.
* **Projects & Ideas –** GenAI-driven projects and business ideas. Outlines of experimental tools, startup concepts, and MVPs that Dinis is developing or proposing (from AI-powered cybersecurity tools to productivity boosters).
* **Europe –** European tech strategy and policy. Insights into Europe’s role in AI and cybersecurity governance – from EU regulatory frameworks and standards to sovereign cloud initiatives for an open, multilingual digital infrastructure.
* **Learning –** The future of learning in the AI era. Explorations of how generative AI and other emerging tech can transform education, upskilling, and knowledge dissemination.
* **Development –** Technical experiments and development practices. Covers unique programming ideas, frameworks, and architectures (for example, using new languages or deterministic pipelines to solve real-world problems).

*Click on any topic above to see all related research posts.*

**Latest Updates:** *(Recent research & posts)*

* **“My Journey Building a GenAI Startup: The Power of MVPs and CI Pipelines – PART 2”** – *29 Nov 2025.* A behind-the-scenes look at lessons learned in creating a GenAI startup, emphasizing rapid prototyping and continuous integration. (Part 2 of Dinis’s ongoing startup journey series.)
* **“Strengthening Trust in News: Implementing Identity Graphs for Authors and Sources”** – *21 Oct 2025.* Proposes a dynamic identity graph system to bolster credibility in journalism, linking reporters and sources to their trust profiles.
* **“LETS: A Deterministic and Debuggable Data Pipeline Architecture”** – *27 Jul 2025.* Introduces a “Load, Extract, Transform, Save” pipeline model for data processing that prioritizes transparency and reproducibility in transformations.

*(Visit the **Updates** page for a full list of posts and archives.)*

**Explore More:** Use the menu at the top to navigate by topic, or visit the **Updates** section to see what’s new. You can also search the site for specific keywords. We hope you find these insights valuable – whether you’re a developer looking for technical guidance, a researcher interested in semantic AI, or simply curious about the future of cybersecurity and knowledge sharing.

*(Optional call to action, e.g., subscribe or contact)*

---

### **Category Page: Cyber-Security**  (`/research/cyber-security.html`)

**Title:** Cyber-Security Research & Insights

**Introduction:**
*How can we make application security smarter and more effective?* This section contains Dinis Cruz’s writings on cybersecurity – focusing on **application security, threat modeling, secure development practices, and security governance**. Readers will find both high-level strategy and technical deep dives aimed at translating complex security challenges into practical solutions.

**Sub-topics and Posts:**

* **Threat Modeling** – methods and frameworks to anticipate and mitigate threats:

  * *Threat Models as Mandatory Disclosures: A Vision for Security Transparency* – Advocates treating threat models like financial disclosures to improve transparency.
  * *Advancing Threat Modeling with Semantic Knowledge Graphs* – Discusses using knowledge graphs to map and analyze threats.
  * *Using Threat Modeling and Semantic Graphs to Secure the Digital Supply Chain* – Explores securing supply chains by combining threat modeling with graph-based data.
  * *(Additional posts on threat modeling…)*

* **Secure Development & Tools** – enhancing AppSec and secure coding:

  * *Deterministic GenAI Outputs with Provenance (OWASP EU AppSec Lisbon)* – Proposes GenAI solutions for application security that produce verifiable, provenance-tagged results.
  * *O2 Platform’s MethodStreams (Open Source SAST engine)* – An overview of an open-source static analysis engine from 2010, with insights into its design.
  * *(Any further secure development topics or tool analyses can be listed here.)*

* **Miscellaneous Cyber Topics:**

  * *Semantic Knowledge Graphs for LLM-Driven Source Code Analysis* – How large language models and graphs can aid code security analysis.
  * *OAuth Security Concerns and Model Context Protocol (MCP)* – Examines OAuth-related vulnerabilities in the context of a new AI model protocol.
  * *Security Debrief: OpenAI’s ChatGPT Connector GitHub App* – A post-mortem on security issues found in a ChatGPT GitHub integration.
  * *Fail Safe, Not Fail Big: Cyber-Security-Inspired Strategies to Prevent the Next Grid Crisis* – Lessons from cybersecurity to protect critical infrastructure.
  * *Second Stories: From Three Mile Island to Cybersecurity* – Historical analogy drawing lessons from a nuclear incident to cybersecurity practices.

*(The posts above are grouped by theme. Threat Modeling is a major focus area, as is secure development. Other posts cover assorted cybersecurity challenges. This categorization helps you jump to what interests you most.)*

**See also:** [Graphs & Knowledge](#) (for research on using knowledge graphs in security), [Projects & Ideas](#) (for experimental tools in security). *(Cross-links to related categories encourage further exploration.)*

---

### **Category Page: Development**  (`/research/development.html`)

**Title:** Development & Technical Experiments

**Introduction:**
This section features content on **software development practices, technical innovations, and experimental programming ideas** that don’t squarely fall under security or AI governance. It’s a space for engineering-centric write-ups – from novel data architectures to exploring new programming paradigms.

**Posts:**

* *LETS (Load, Extract, Transform, Save): A Deterministic and Debuggable Data Pipeline Architecture* – Introduction of a robust data pipeline pattern emphasizing reproducibility. This post is a deep dive into designing data transformations that are easy to trace and test. *(Jul 2025)*

*(Currently, this is the sole post in Development. As more content is added – e.g., on programming languages, CI/CD processes, or other technical R\&D – they would be listed here.)*

**Note:** If you’re interested in development as it intersects with security or AI, check out the **Cyber-Security** section (for secure coding topics) or **Projects & Ideas** (many project write-ups involve development of new tools).

---

### **Category Page: Graphs**  (`/research/graphs.html`)

**Title:** Graphs & Semantic Knowledge

**Introduction:**
How can **graphs** make sense of complex data and security challenges? This category contains research on *semantic knowledge graphs, ontologies, and related AI techniques*. These posts examine how structuring knowledge as graphs can aid in areas like cybersecurity, compliance, and data management.

**Sub-topics and Posts:**

* **Ontologies and Taxonomies:** organizing knowledge

  * *From Top-Down to Organic Evolving Graphs, Ontologies, and Taxonomies* – Discussion on evolving knowledge structures from rigid taxonomies to flexible graphs.
  * *Semantic OWASP: Leveraging GenAI and Graphs to Customize and Scale Security Knowledge* – How combining OWASP content with knowledge graphs and GenAI can create tailored security guidance.
  * *Enhancing Cybersecurity Event Networking with Semantic Knowledge Graphs* – Using graphs to connect and contextualize cybersecurity events and signals.

* **Standards and Governance:** applying graphs in policy/compliance

  * *Maturity Models vs. Traditional Standards in Application Security* – Critique of static security standards, proposing a graph-based, dynamic approach.
  * *Graph-Powered Legal Knowledge: An Open, Distributed AI-Assisted Roadmap* – Vision for managing legal and compliance knowledge via open graphs.
  * *(If more posts about standards, regulations, or governance use graphs, they would be listed here.)*

* **Cloud and Infrastructure:** graphs in cloud environments

  * *Intent-Based Feedback Loops in Cloud Environments* – Explores using intent graphs to automate cloud security feedback and remediation (linking desired outcomes to system state in cloud).
  * *(Additional cloud-related graph topics could appear here.)*

*(The Graphs section connects with many others – for example, knowledge graphs show up in security and news contexts. This page focuses on graph technology itself. If you have an interest in AI-driven knowledge management, this is the place.)*

**See also:** [Cyber-Security](#) (for security applications of graphs), [Future of News](#) (for how graphs can help with information trust), [Projects & Ideas](#) (some projects involve building graph-based systems).

---

### **Category Page: Future of News**  (`/research/the-future-of-news.html`)

**Title:** The Future of News & Digital Trust

**Introduction:**
The **Future of News** section covers how technology and new ideas can restore trust in media and journalism. Topics include **fact-checking and provenance, journalist identity and reputation systems, content monetization, and combating misinformation**. These articles propose solutions to ensure that quality information is recognized and rewarded in the digital age.

**Posts:**

* *Monetising Trust and Knowledge: How News Providers can leverage Personalised Semantic Graphs* – Describes using personal knowledge graphs to tailor news and rebuild trust with readers. Shows how news organizations might monetize content through trusted, personalized delivery.
* *Journalists’ Challenges with Digital Content Provenance and Trust* – Outlines the difficulties journalists face in verifying digital content and maintaining trust, laying the groundwork for technical solutions.
* *The Future of News: Building Trust Through Fact Provenance* – A deep dive into fact-provenance frameworks: how tracking the origin and veracity of facts can combat misinformation and enhance public trust. Discusses the roles of technology in scaling verification processes and the business implications of trust.
* *The Future of News Monetization: Embracing Micro and Nano Payments* – Examines new payment models (microtransactions) for news content, to support quality journalism in an era of ad fatigue and paywall avoidance.
* *Strengthening Trust in News: Implementing Identity Graphs for Authors and Sources* – Proposes “identity graphs” that maintain reputational profiles for journalists and sources, in order to add transparency about who is behind information.

*(Together, these posts form a narrative: identifying trust problems in modern media and suggesting graph-based and economic innovations to solve them. They are accessible to a general audience interested in media, as well as to technologists building the next-gen news platforms.)*

**See also:** [Graphs](#) (some underlying graph tech discussed here), [Europe](#) (for regulatory angles, like standards for content provenance), or [Cyber-Security](#) (if interested in how misinformation ties into security).

---

### **Category Page: Projects & Ideas**  (`/research/projects.html`)

**Title:** Projects and Business Ideas

**Introduction:**
In this section, Dinis outlines various **projects, prototypes, and business ideas** he’s developing or considering. These range from technical tools to improve workflows, to startup concepts at the intersection of cybersecurity and AI. Each entry is a glimpse into an innovative solution or venture, often leveraging generative AI with practical use-cases.

**Subsections:**

* **Project Briefs:** *(Concepts and prototypes of tools or platforms)*

  * *Project InsightFlow: GenAI-Powered Transformation of Regulatory and News Feeds* – An AI system to automatically summarize and map regulatory news, helping professionals stay informed.
  * *Project GenBnB: Enhancing Airbnb Host Workflows with GenAI* – Proposal for integrating GenAI assistants into property rental management for efficiency.
  * *Project Cybersage: AI-Powered Risk Contextualization & Reporting* – Concept for a tool that uses AI to contextualize cybersecurity risks for easier reporting.
  * *Project JSync: JIRA Exporter and Synchronization System* – A solution for syncing and exporting JIRA project data (improving project management workflows).
  * *Project Lumos: Serverless JIRA-to-GraphDB Connector* – A serverless approach to integrate JIRA with graph databases for richer data analysis.
  * *Project SupplyShield: GenAI-Driven Supply Chain Risk Management* – Using GenAI to analyze and mitigate supply chain security risks.
  * *(Additional project write-ups, such as the StartLLM series, would also be listed here.)*

* **Business Ideas / Plans:** *(Larger venture concepts or research-driven business plans)*

  * *Scaling a Solo Cybersecurity Consulting Practice – Business Plan Research* – A business plan outline exploring how an individual consultant can scale services, using tools and IP strategically.
  * *LinkedIn Vault: Professional Data Preservation Service* – Idea for a service that helps professionals backup and preserve their LinkedIn (and other) data securely.

* **Misc. Research & Possible Projects:** *(Ideas in early stages or uncategorized)*

  * *AI-Powered Customer Service Solutions for Multi-Property Airbnb Hosts* – Research into automating customer service using AI for hosts with multiple properties. (This could evolve into a project or product concept.)

*(Each project/idea page goes into the motivation, approach, and current status of the concept. This section is of particular interest to developers, entrepreneurs, and innovation teams, as it showcases how cutting-edge AI and security techniques can be applied in practice.)*

**Navigation Tip:** You can treat this section as a mini “incubator” – browse through the project briefs for quick overviews, or dive into the ones that align with problems you’re looking to solve. Many projects here reference or build upon concepts from the other research categories (for example, graph technology or cybersecurity best practices).

---

### **Category Page: Europe**  (`/research/europe.html`) *\[Proposed new category]*

**Title:** Europe’s AI & Cybersecurity Initiatives

**Introduction:**
Europe is taking a distinctive approach to AI, cybersecurity, and digital sovereignty. This category collects articles analyzing **European strategies, regulations, and opportunities in the realm of technology**. Readers will find commentary on EU policies, proposals for European collaborative projects, and how Europe can leverage its unique position (like its regulatory power) in shaping the future of tech.

**Posts:**

* *Scaling Europe’s Regulatory Superpower: From Static Cybersecurity Standards to Semantic Graphs* – Discusses how Europe’s strong regulatory frameworks could evolve using semantic graphs for more dynamic standards. Suggests Europe could lead by implementing more adaptive, technology-enabled regulations.
* *An Open-Source Sovereign Cloud for an Open Europe* – A case for Europe building its own sovereign cloud infrastructure. Emphasizes a federated, AI-enabled, multilingual cloud to reduce dependence on foreign providers and enhance collaboration.
* *Europe’s Strategic Opportunity in GenAI: A Deep Dive into Six Defining Trends* – Identifies key trends in generative AI and how Europe can capitalize on them. Covers topics like multilingual AI, ethical AI leadership, and research investment, positioning Europe to be competitive in the AI landscape.
* *Intent-Based Feedback Loops in Cloud Environments* – (Also listed under Graphs/Cloud) Relevant here for its implications on European cloud strategies, such as building automated feedback into cloud governance.
* *Maturity Models vs. Traditional Standards in AppSec* – (Also listed under Graphs/Standards) Ties into European standards bodies and how they might modernize cybersecurity guidelines.
* *Semantic OWASP: Customising and Scaling Security Knowledge* – (Also cross-listed) While a global concept, Europe’s community could adopt this approach to unify languages and practices in security across member states.

*(This category might overlap some content with **Cyber-Security** and **Graphs** due to cross-cutting themes, but it frames them in a European context. It’s especially geared toward policymakers, EU-based organizations, and researchers interested in Europe’s role in tech.)*

**See also:** [Learning](#) (the next category, for education-oriented content; one of the listed posts bridges Europe and learning policy), [Cyber-Security](#) (for more on standards and governance, generally applicable beyond Europe).

---

### **Category Page: Learning**  (`/research/learning.html`) *\[Proposed new category]*

**Title:** AI in Learning & Education

**Introduction:**
Education and learning are being transformed by AI technologies. This section gathers content on **learning in the AI era** – from how generative AI can be used as a teaching tool, to the skills needed for future jobs, and how institutions might adapt. It’s relevant for educators, students, and anyone interested in the future of education and knowledge work.

**Posts:**

* *Generative AI and the Future of Learning* – Examines how AI (like GPT models) can personalize education. Discusses opportunities for AI tutors, curriculum generation, and the challenges of ensuring quality and trust in AI-provided knowledge.
* *(As new posts related to training, upskilling, or educational policy in the context of AI are written, they would appear here.)*

*(Currently a small category, but an important one for engaging the general public and educators. Future content might include case studies of AI tools in classrooms, or learning frameworks for AI literacy.)*

**See also:** [Europe](#) (if interested in how European initiatives address AI in education), [Projects & Ideas](#) (if any project relates to training or knowledge management), and [Future of News](#) (since media literacy and news overlap with learning about trustworthy information).

---

### **Updates Page (Blog Index)**  (`/updates/` or `/blog/`)

**Title:** Latest Updates and Articles

**Introduction:**
Stay up-to-date with the latest research and writings. Below is a chronological list of recent posts (newest first). Each entry includes a brief excerpt so you can quickly catch the gist and decide what to read. For older posts, see the **Archives by Year** section at the bottom.

**Recent Posts:**

* **\[Title of Most Recent Post]** – *Date* – *Excerpt:* A 2-3 sentence summary or introduction of the post, highlighting its main point or finding. (This should be pulled from the post’s metadata or first paragraph). **[Read more…](link)**
* **\[Next Most Recent Post]** – *Date* – *Excerpt:* … **\[Read more…]**
* *(Continue listing posts in reverse chronological order, ideally 5-10 per page, with pagination or a “Load more” if the list is long.)*

*(Each entry should make it clear what the post is about. For example, an excerpt from “Monetising Trust and Knowledge...” might mention building personalized news graphs and why it matters. This gives the reader context immediately.)*

**Archives by Year:**

* **2025** – *(expandable or listed)* All 2025 posts by month/title.
* **2024** – All 2024 posts…
* *(and so on, if needed)*

*(The archive section is mainly for someone looking for older content by date. It can be a simple list of months and titles under each year, or just a link to a page per year. The key is that it’s available but not dominating the main navigation. By structuring it here, we keep the sidebar clean while still allowing a deep dive into the timeline if desired.)*

---

### **Resources: Presentations Page**  (`/resources/presentations.html`)

**Title:** Conference & Meetup Presentations

**Introduction:**
Here you’ll find links to presentations and talks delivered by Dinis Cruz, often at conferences or community meetups. Each entry includes the talk title, date, and context. Many of these presentations correspond to research posts on this site – feel free to click through to read more detail or view associated materials.

**Presentations List:** *(sorted by date, newest first)*

* **“Using GenAI to Graph and Map Your Company’s Data” – Grafter Meetup** (May 7, 2025) – *How generative AI and knowledge graphs can be combined to create insightful maps of corporate data, enabling better decision-making.* **[Read related article](link)**
* **“Semantic OWASP: Customising and Scaling Security Knowledge” – OWASP Global AppSec** (Apr 23, 2025) – *Applying semantic knowledge graphs and GenAI to tailor OWASP security guidance to an organization’s context.* **[View slides](link)** | **[Read more](link)**
* **“My Journey Building a GenAI Startup – PART 2” – Open Security Summit** (Feb 26, 2025) – *Continuing the story of launching a GenAI startup, with a focus on integrating continuous improvement and community feedback.* **[Read article](link)**
* **“My Journey Building a GenAI Startup – PART 1” – Open Security Summit** (Jan 29, 2025) – *Lessons from the early stages of a GenAI startup, emphasizing MVP mindset.* **[Read article](link)**
* **“Deterministic GenAI Outputs with Provenance” – OWASP EU AppSec Lisbon** (June 28, 2024) – *How to achieve deterministic results from AI models and attach provenance data for security and compliance.* **[Read article](link)**
* **“It’s 2024 and with GenAI, We Can Finally Make AppSec Work” – OWASP Global Summit** (Feb 22, 2024) – *Vision talk on leveraging GenAI to solve longstanding application security challenges.* **[Read article](link)**

*(The above entries show how each presentation is tied to a real piece of content. For instance, most have a corresponding write-up on the site. Providing the “read more” links encourages visitors to dive from a talk title into the detailed research post or blog associated with it.)*

**Note:** Many of these presentation links will lead you to blog articles or slides that provide more depth. If you’re preparing for a talk or looking for reference material, you might find the content and references in those linked articles useful. For a full list of Dinis’s talks and workshops, visit [Dinis’s speaker profile on Open Security Summit](#) or [LinkedIn post of collected updates](#) where he curates his contributions.

---

**Scalability & Maintenance Considerations:** The proposed content structure above is designed to be sustainable. Each section can grow without losing clarity:

* If new categories emerge (say Dinis starts writing about “AI Ethics”), you could add a new category page with the same template of intro + posts. Keep the total number of top categories reasonably small (5–8) for clarity.
* The Home page can be periodically updated with either manual selection of featured posts or automatically displaying the latest posts. Because it’s short and sectioned, edits will be manageable.
* The Updates page will automatically list new posts if configured with the blog plugin; it simply requires that new posts have the proper metadata (date, excerpt) and they’ll appear in order – thus supporting an ongoing “changelog” of content.
* Each category page will update as new posts tagged with that category are added. The maintainer just needs to ensure that if a post introduces a new subtopic, the category page’s structure (subheadings) is adjusted to accommodate it. This is easier than rethinking navigation entirely – we’re essentially allocating space for growth within each thematic silo.
* The navigation menu, under this plan, remains user-friendly even as content grows: we don’t list every item there, just high-level links (Home, Topics, Updates, Resources, etc.). Users won’t have to scroll through a years-long list in the sidebar; instead, they’ll click into Updates or a category to see more. This is a more maintainable approach as the site scales, and it aligns with the idea that *“clear and well-designed navigation enhances usability…and encourages visitors to explore more pages.”*

By implementing the above improvements, **discoverability** will increase: visitors can quickly grasp where to find what they need, whether they prefer browsing by topic or checking what’s new. The structure becomes intuitive — a first-time visitor sees plain-English sections and knows where to go (e.g., a journalist might jump to “Future of News”, a developer to “Projects & Ideas” or “Cyber-Security”). Regular readers can rely on the Updates feed or the homepage highlights to catch new material. Overall, the site will feel more welcoming to its broad audience while still catering to advanced users, fulfilling Nielsen Norman’s guidance that navigation should *“show people what they can find on the site”* in a clear way, and that sensible categorization trumps a purely sequential listing of content.

**Sources:**

* Material for MkDocs Blog Tutorial – on combining chronological and category navigation.
* Econsultancy – on why purely chronological blog layouts can hinder content discovery.
* Nielsen Norman Group – on clear, exclusive categories and the importance of navigation for users.
* Excerpts from docs.diniscruz.ai – demonstrating current structure and content examples.
