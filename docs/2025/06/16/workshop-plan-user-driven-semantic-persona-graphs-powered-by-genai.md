---
title: "Workshop Plan: User-Driven Semantic Persona Graphs Powered by GenAI"
authors: ["Dinis Cruz", "ChatGPT Deep Research"]
date: 2025/06/16
pdf_file: workshop-plan-user-driven-semantic-persona-graphs-powered-by-genai.pdf
back_link: /research/development-and-genai
---

_by {{ authors | join(" and ") }}, {{ date }}_

{{ download_pdf(date, pdf_file) }} {{ linkedin_post(linkedin) }} {{back_button(back_link)}}

## Introduction and Workshop Overview

This workshop will demonstrate how to use Generative AI (GenAI) to build a **personalized semantic knowledge graph** for a user and then generate tailored outputs for different stakeholder personas. We will guide 6 technical participants (with limited GenAI experience) through a multi-phase pipeline of custom GPT-powered assistants that collaboratively transform user input into meaningful insights. The goal is to showcase the *art of the possible* – how complex, context-aware solutions can be built by chaining together specialized GPT agents, each performing a focused task.

In this hands-on session (conducted virtually), we will create an **MVP (Minimum Viable Product)** of an AI-driven guidance tool for a real-world scenario. The chosen scenario is helping a small business assess its cybersecurity posture against a standard (e.g. **Cyber Essentials**, ISO 27001, or GDPR compliance). The workflow will involve multiple custom ChatGPT “mini-apps” (GPT 1 through 6), each feeding its output into the next. Participants will first see a live demonstration of the end-to-end pipeline using pre-built GPT agents, and then will be supported in creating these GPTs themselves using provided prompt “briefs” and examples. All participants have access to ChatGPT (with Custom GPT capabilities), so they can interact with and configure the agents during the session.

Key objectives and features of the workshop:

* **Step-by-step GenAI Pipeline:** We break down a complex task (personalized compliance assessment) into six manageable GPT-driven phases. This multi-step approach addresses issues of explainability, provenance, and determinism that occur if one tries to do everything in a single AI prompt. By chaining specialized GPTs, each step is transparent and the overall process is more controlled.
* **Semantic Knowledge Graph Creation:** The pipeline will convert unstructured user inputs into a structured **semantic knowledge graph** representation of the user’s situation. This graph captures key facts (entities, attributes, relationships) extracted from the Q\&A. Using a knowledge graph approach makes the knowledge **more explainable and maintainable**, and provides a strong foundation for subsequent analysis.
* **Multi-Persona Outputs:** A highlight of this workshop is showing how the same base knowledge can be repackaged for different stakeholders. The participants will see the AI generate targeted narratives for various personas – from a high-level executive summary to a detailed technical plan. This demonstrates GenAI’s capability to **translate knowledge to the language of each stakeholder**, making insights actionable and relevant.
* **“Vibe Coding” UI Prototypes:** Finally, we push the envelope by using AI to generate user interface mockups or code, a technique known as *vibe coding*. In vibe coding, you *describe what you want* in natural language and let the AI produce the code for it. We will leverage this to create simple, persona-specific UI prototypes that present the results in a visually engaging way for each audience. This underscores how GenAI can accelerate prototyping and bring ideas to life in minutes.

Throughout the session, participants will be exposed to GenAI best practices such as providing clear instructions, feeding domain knowledge into prompts, and dividing problems into phases. The overall experience is highly interactive – the GPT agents will interview a participant (or a role-played user), build a knowledge graph, and then produce outputs. We will use **manual copy-and-paste** between GPTs to simulate data passing (since this is an MVP setup), which keeps things simple and transparent. By the end, attendees will have a concrete understanding of how GenAI (like ChatGPT) can be orchestrated to implement a complex workflow, and they will have hands-on experience creating and tuning custom GPT-based tools.

## Multi-Phase GPT Pipeline Overview

To organize the project, we divide the workflow into six phases, each handled by a dedicated GPT agent with a specific role. Below is an overview of each phase and how its GPT will function:

### GPT 1: Criteria Ingestion & Questionnaire Designer

**Purpose:** In Phase 1, we set the stage by ingesting the **compliance criteria** or standard requirements and automatically designing an interview questionnaire based on them. GPT 1 acts as a *questionnaire generator*. We will provide it with the details of the chosen standard (for example, key controls from Cyber Essentials) and the objectives of the assessment. GPT 1 will then output a **tailored prompt/script** for GPT 2 to use – essentially a list of user-friendly questions to ask, plus instructions on how to conduct the interview.

**How it works:** We supply GPT 1 with background knowledge (e.g. a summary of Cyber Essentials controls) and ask it to produce an **interactive Q\&A script**. This script will include a greeting, about 10–20 questions covering the standard’s key points, and guidance on how to conclude the interview. The questions should be phrased in a clear, non-jargon way despite being based on technical criteria. By automating this step, we show that GenAI can quickly convert official standards or documents into conversational checklists. GPT 1 does *not* talk to the end-user; it works behind-the-scenes to generate the content for the next GPT. (In the workshop, the facilitator will run GPT 1 beforehand to prepare the material for GPT 2.)

### GPT 2: Interactive Q\&A Interview Agent

**Purpose:** GPT 2 is the **interactive interviewer** that engages with the user (client) to gather information. Using the script from GPT 1, GPT 2 will conduct a chat-based interview, asking the user each question, one at a time, and recording their answers. The goal is to collect all relevant data about the user’s current practices vis-à-vis the standard.

**How it works:** GPT 2 will be configured with the questionnaire and interview instructions generated by GPT 1. When a user (one of the participants, role-playing a client) starts the conversation, GPT 2 will introduce itself (e.g. as a friendly compliance assistant) and then proceed through the list of questions sequentially. After the user answers a question, GPT 2 will acknowledge and move to the next question, creating an interactive dialogue. It will ensure the phrasing is approachable and will only delve deeper if clarification is needed. Once all questions have been answered, GPT 2 will thank the user and **summarize the responses** gathered (or at least indicate that it has recorded their answers for processing). This summary of user inputs is crucial, as it will be passed to GPT 3. We effectively end up with a structured set of Q\&A pairs or notes about the user’s status on each control. *(In the demonstration, we will show this live Q\&A. Then, we may have GPT 2 output the collected data explicitly – for example, by prompting it with “Now please summarize the information you’ve collected” – so we can easily copy that text.)*

### GPT 3: Semantic Knowledge Graph Builder

**Purpose:** GPT 3 takes the raw answers from the interview and converts them into a **semantic knowledge graph** representation. In simpler terms, it transforms the Q\&A data into structured facts: entities, attributes, and relationships that capture the user’s situation. This step bridges unstructured input and structured knowledge, which is key for complex analysis and traceability.

**How it works:** We will feed GPT 3 the summary of the user’s answers (from GPT 2) and task it with producing a *text-based graph* of the information. GPT 3’s system prompt will describe an ontology or format to use – for instance, define the user’s organization as an entity and each security control or practice as either an attribute or linked node with a value indicating its status. The output might be a list of facts or triples like: “**Company** – *has firewall* – **Yes**”, “**Company** – *enforces multi-factor authentication* – **No**”, etc. We won’t require a formal JSON-LD or RDF (to keep it simple), but the idea is to express the knowledge in a **structured, machine-friendly way** (while still human-readable). This semantic graph makes the reasoning explicit: it’s clear which requirements are met and which are not, and this representation can be fed into the next step. By doing this transformation in a separate phase, we improve explainability and create a durable knowledge asset – a graph that could be visualized or queried in the future. *(During the workshop, after running GPT 3, we’ll examine its output – essentially the “knowledge graph” of the user – to verify it captured everything correctly before moving on.)*

### GPT 4: Detailed Analysis & Recommendations Generator

**Purpose:** GPT 4 is responsible for producing a **comprehensive technical report** that analyzes the user’s posture against the standard and provides detailed recommendations. This is where all the knowledge comes together: GPT 4 uses the structured facts (from GPT 3) *and* the reference standard content to generate an in-depth assessment. It essentially translates the raw graph data into meaningful insights, reasoning about compliance gaps, risks, and mitigations.

**How it works:** We will configure GPT 4 with an understanding of the scenario and the standard’s guidance. Its input will include the semantic facts from GPT 3 (the knowledge graph of what the user has and lacks) and possibly key reference information from the standard itself (we can provide excerpts or expect GPT 4 to have background knowledge of common practices). GPT 4 will then produce an extensive report. We will instruct it to be structured and factual – for example, to organize the report by control areas or by the questions asked. For each area, it should state what the user has in place (strengths) and what is missing or weak, explain the implications (why it matters for security or compliance), and give specific, actionable recommendations on how to improve. This output is expected to be quite **technical and detailed** – likely several paragraphs per control topic – since it’s aggregating *all* relevant insights. Essentially, GPT 4 is performing the role of a consultant or auditor writing a findings report. This phase leverages the knowledge graph to ensure every statement can be traced to input facts (addressing provenance), and by using the standard’s criteria, it ensures alignment with official guidance. The resulting document is the **single-source-of-truth** that subsequent steps will adapt for different audiences. *(In the workshop, we’ll run GPT 4 and skim through the generated report to observe how the AI compiled the information. This also demonstrates how GenAI can **synthesize domain knowledge with user-specific data** to create a high-quality deliverable.)*

### GPT 5: Persona-Specific Briefing Generator

**Purpose:** In Phase 5, we take the heavy technical report from GPT 4 and **reframe it for multiple stakeholder personas**. GPT 5 will output a set of **tailored briefings**, each addressing the concerns and communication style of a particular persona in the client’s organization. This is crucial for making the information actionable: different roles (executive vs. technical, for example) need the message presented in very different ways.

**How it works:** GPT 5 will be given the full technical report (or the key findings) along with descriptions of the target personas. We will define profiles such as:

* *CEO/Executive:* Focus on high-level business risk and strategic implications. Not much technical detail – needs the “so what” and ROI of fixes.
* *Board of Directors:* Even higher-level, concerned with governance, risk, and compliance status. Very concise and impact-focused.
* *CFO (Peer Executive):* Focus on financial risk, potential costs (of breaches or of improvements), and compliance obligations (fines, budget needed for security).
* *IT/Security Team Lead:* A moderately detailed summary that translates the findings into a project plan or priorities for implementation. This may still be fairly technical but more action-oriented (the **what to do**).
* *Implementer/Engineer (optional, “two levels down”):* If needed, an even more granular set of instructions or a checklist that a technical staff member could follow. (This could be combined with the team lead brief if time is short.)

Using these persona definitions, GPT 5 will generate distinct outputs for each. Each output will *highlight the information that matters most to that persona and use an appropriate tone*: e.g. the CEO’s summary might use business language and emphasize risk reduction and competitive advantage, whereas the technical plan will use security terminology and detailed steps. We will instruct GPT 5 to clearly separate the sections (perhaps with headings like “**Executive Summary**”, “**Board Briefing**”, “**Technical Action Plan**”, etc.). The ability of GenAI to automatically adapt content to different reading levels and interests is a powerful demonstration of its flexibility. We will also incorporate a **persona validation** step: GPT 5 will include a short description of each persona’s assumed concerns at the start of each section (for example, “(Persona: CEO – interested in overall business impact and assurance that risks are managed)”), and we can verify with the participants if these assumptions hold true. This ensures the messaging is on point. *(During the workshop, after GPT 5 produces the multi-persona document, we’ll discuss how each differs and why. Participants can see how tailoring the voice for the audience makes the recommendations more likely to be understood and acted upon.)*

### GPT 6: UI/Presentation Prototype Creator

**Purpose:** The final phase explores how the AI-generated content can be turned into **user-friendly visual presentations or interfaces** for each persona. GPT 6 will perform *“vibe coding”* – generating prototype UI designs or code snippets directly from the persona-specific texts. This is an advanced and creative step to end the session on an exciting note, showing that GenAI can not only write documents but also help build applications and dashboards from those documents.

**How it works:** GPT 6 will be given the outputs from GPT 5 (the tailored briefs) and tasked with producing an appropriate **UI or visualization** for each. We will prompt it to treat each persona’s content as requirements for a quick interface mockup. For example, GPT 6 could generate:

* For the CEO’s summary: a simple web dashboard layout with a high-level risk score, a few key bullet points or graphs (like “compliance level: 70%” or “2 high risks identified”). It might output HTML/CSS code or a structured description of a slide.
* For the Board: perhaps a slide deck outline or an infographic concept, emphasizing top risks and mitigation status (maybe using icons or color-coding for ease of reading).
* For the CFO: maybe a table or chart showing potential costs and savings (e.g. cost to implement each recommendation vs. potential loss from not doing it).
* For the Tech Team: a more detailed dashboard or portal view, possibly a task-tracking interface listing each recommendation with status, or even code for a simple web page that lists the findings with checkboxes for each action item.

Using natural language descriptions of the desired outcome, GPT 6 will *generate code or design specifications* for these UIs. This is the essence of vibe coding – **describe what you want, and let the AI handle the implementation details in code**. We may see GPT 6 produce actual HTML/CSS/JavaScript for a basic webpage for each persona’s report, or pseudo-code and wireframes. The focus is to illustrate multiple ways to present the same data, optimized for each user’s experience. We won’t necessarily deploy these UIs live in the session, but we will examine the generated code or design and possibly render one quickly (if easily done) to show that it “mostly works.” This technique shows how a clear, structured prompt can yield working software artifacts from AI – an emerging trend in software development. It underlines that with GenAI and the right prompts, we are *“only a few prompts away from a product”* in many cases.

By the end of GPT 6’s phase, we will have come full circle: starting from a textual standard and ending with interactive tool prototypes, all in one session. This final step typically impresses participants and solidifies the understanding that GenAI can accelerate not just writing tasks but also technical development tasks in a highly accessible way.

## Technical Implementation Details and GPT Configuration Artifacts

In this section, we detail how to set up each custom GPT (1 through 6), including example prompt content and instructions. These are the **artifacts** that will be used to create the GPT agents before the session and will be shared with participants as needed. Each GPT will be configured in ChatGPT with a custom system prompt (and supporting information) as described. Participants can use these as templates for creating their own GPTs.

*(Note: In the prompt examples below, placeholders like “\[StandardName]” or specific scenario details should be replaced with the appropriate context if a different standard or use-case is used. In our example, we use the **Cyber Essentials** standard to illustrate, but the structure can be adapted to GDPR, ISO 27001, or others by plugging in the relevant criteria and adjusting the questions.)*

### GPT 1 – “Questionnaire Designer” Configuration

**Role & Objective:** GPT 1 is configured as a *Questionnaire Designer AI*. It reads the input compliance standard and outputs a ready-to-use interview prompt for GPT 2. It must identify the main topics from the standard and formulate clear questions covering each, aiming for about 10–15 questions total. It also appends instructions on how GPT 2 should conduct the interview (one question at a time, friendly tone, etc.). Essentially, GPT 1’s output will be the **system prompt for GPT 2**.

**Inputs:** We will provide GPT 1 with the context of the standard’s requirements. This can be done by pasting a summary of the standard or listing its key controls. For Cyber Essentials, for example, we give it the five control themes and any specifics. We also instruct GPT 1 on the format of output we want (a script with numbered questions and any other directions).

**System Prompt for GPT 1 (template):**

```
You are an expert AI assistant specializing in cybersecurity compliance. Your task is to help design an interview questionnaire based on the **[StandardName]** requirements. You will be given an overview of the standard’s criteria, and you need to produce a clear, ordered list of questions to ask a user, in order to assess their adherence to those criteria. 

**Requirements:**

- Read and understand the core objectives of [StandardName]. Then formulate a set of about 10–15 key questions that collectively cover all major areas of the standard. The questions should be phrased in a **user-friendly** way (assume the user is technically savvy but not an expert in compliance terms).
- Begin the output with a brief **greeting/introduction** that an interviewer could use (e.g. “Hello, I’m here to help assess your security practices against [StandardName]…”). This sets context for the user.
- After the intro, list the questions in the order they should be asked. Number each question.
- The questions should be open enough to invite brief explanation if needed, but many will effectively be yes/no or short-answer queries. Avoid overt jargon; prefer plain language (e.g. say “Do you have a firewall?” rather than “Have you implemented network perimeter controls?”).
- After listing all questions, include a closing statement thanking the user and indicating that recommendations will follow.
- Additionally, provide any **special instructions** for the interviewer agent (GPT 2) on how to conduct the Q&A. For example: “Ask one question at a time, wait for the user’s answer, then proceed to the next question,” and “If an answer is unclear, politely ask for clarification.” Include these instructions either at the beginning or end of the output clearly, perhaps as a note to the AI.

**Context (Standard Summary):** 
[StandardName] covers the following main points:
- **Use a Firewall** – Protect your internet connection with a firewall.
- **Secure Configuration** – Securely configure devices & software (e.g. remove default passwords, disable unused features).
- **Access Control** – Control user/admin access (least privilege) and use multi-factor authentication for important accounts.
- **Malware Protection** – Protect against viruses and malware (install antivirus or use application allow-listing).
- **Patch Management** – Keep software and devices updated (apply security patches within a defined timeframe, e.g. 14 days for critical updates).

Use the above points to inform the questions. Focus on these areas; ensure at least one question per area (some areas might need multiple questions to cover sub-points). 

Now, produce the interview script with introduction, **numbered questions**, and conclusion, plus any needed instructions for the interviewer.
```

*After providing this system prompt to GPT 1, we (the facilitators) will enter the standard summary as a user message if needed (unless we included it directly). GPT 1 should then output something like the following (abridged for example):*

**Example Output from GPT 1 (excerpt):**

\*“Hello! I’m here to help evaluate your company’s security practices against the Cyber Essentials standard. I’ll ask you a few questions about your setup.

1. Do you have a firewall in place to protect your network’s internet connection?
2. Is your firewall configured to block unauthorized access attempts by default?
3. When you set up new devices or software, do you change default passwords and settings to be more secure?
4. Do you ensure that only necessary services and software are enabled on your computers (to keep configurations secure)?
5. Do you restrict administrative access to only those who absolutely need it?
6. Do you use multi-factor authentication for administrator or remote access accounts?
7. Do you have anti-virus or anti-malware software installed on all systems?
8. Are users prevented from installing unapproved software on their devices?
9. Do you apply critical security updates and patches within roughly two weeks of their release?
10. Do you have a process to ensure all your devices and software are kept up-to-date with the latest security patches?

Thank you for answering these questions. Once we have your responses, we’ll review and provide some recommendations to improve your cyber security according to the standard.

*Instructions for interviewer:* Ask the above questions one by one in order. After the user answers a question, acknowledge and ask the next one. Maintain a friendly, helpful tone. If an answer is unclear, you may ask a follow-up for clarification. After the last question, provide a brief summary of the responses and thank the user.”\*

*(The above illustrates the kind of output GPT 1 should generate. We will use this output as the basis for configuring GPT 2.)*

### GPT 2 – “Interactive Interviewer” Configuration

**Role & Objective:** GPT 2 is the *Interactive Interviewer*. It will use the script from GPT 1 to conduct a Q\&A with the user. GPT 2’s configuration is mostly about inserting the questionnaire and ensuring it follows the interactive format. Essentially, GPT 2’s system prompt *is* the output produced by GPT 1 (or a refined version of it).

**Setup:** We take the script from GPT 1 and place it into GPT 2’s system prompt field. We might need to tweak it slightly for formatting, but generally it will contain the introduction, the numbered list of questions, and the interviewer instructions. We also set GPT 2’s persona to be friendly, encouraging, and clear. GPT 2 will start the conversation on its own with the greeting, then proceed with the numbered questions sequentially, following the user’s input each time.

**System Prompt for GPT 2:**

*(We use the output from GPT 1 directly. For completeness, here is how it would look formatted as a prompt for GPT 2:)*

```
You are ChatGPT acting as a cybersecurity compliance interviewer for the [StandardName] assessment. **Follow the script and guidelines below to interview the user:**

Hello! I’m here to help evaluate your company’s security practices against the [StandardName] standard. I’ll ask you a few questions about your setup to understand where things stand. 

1. Do you have a firewall in place to protect your network’s internet connection?
2. Is your firewall configured to block unauthorized access attempts by default?
3. When you set up new devices or software, do you change default passwords and settings to be more secure?
4. Do you ensure that only necessary services and software are enabled on your computers (to keep configurations secure)?
5. Do you restrict administrative access to only those who absolutely need it?
6. Do you use multi-factor authentication for administrator or remote access accounts?
7. Do you have anti-virus or anti-malware software installed and kept updated on all systems?
8. Are users prevented from installing unapproved or random software on their devices?
9. Do you apply critical security updates and patches within roughly two weeks of their release?
10. Do you have a process to ensure all your devices and software stay up-to-date with the latest security patches?

After you answer all these questions, I’ll summarize your responses and we can discuss recommendations.

*(Instructions for you, the interviewer AI:)* 
- Ask the above questions **one at a time** in order. Wait for the user’s answer before moving to the next question.
- Use a friendly and clear tone. Encourage honesty and let the user know it’s fine if they are unsure or not fully compliant – the goal is to identify areas to improve.
- If an answer is unclear or too brief, you can ask a gentle follow-up for clarification.
- Once all questions are answered, thank the user. Then provide a brief summary of their answers, highlighting any “yes” vs “no” (or strong vs weak) areas, and tell them you will now process this information to generate recommendations.
```

With this configuration, when GPT 2 is launched in a chat with a user, it will start by outputting the greeting and the first question. The user (in the workshop, one of the participants) will answer, and GPT 2 will continue asking the next question, and so on. Finally, GPT 2 will summarize.

**Example Interaction with GPT 2 (for illustration):**

* *GPT 2:* “Hello! I’m here to help evaluate your security practices against Cyber Essentials. First, do you have a firewall in place to protect your internet connection?”
* *User:* “Yes, we have a firewall on our network.”
* *GPT 2:* “Great. Is that firewall configured to block unauthorized access by default (essentially only allowing necessary traffic)?”
* *User:* “I believe so, we haven’t changed the default settings much.”
* *GPT 2:* “Okay, thanks... \[and so on through all questions] ...”
  *(After final question)*
* *GPT 2:* “Thank you for answering all these questions. Here’s a quick summary of what I’ve gathered: You **do** have a network firewall, though it might be using default rules. You change default passwords on new devices and keep configurations lean (good!). You restrict admin access to a few people, but currently you **do not use multi-factor authentication** for those accounts. You have antivirus on all systems and users cannot install apps freely. As for updates, you mentioned you apply patches, but sometimes only monthly, which means not always within two weeks.

I’ll now analyze this information against the Cyber Essentials requirements and prepare some recommendations for you. Please stand by….”

*(At this point, the interview is done and we have the summarized data ready to feed into GPT 3.)*

### GPT 3 – “Knowledge Graph Converter” Configuration

**Role & Objective:** GPT 3 is set up as a *converter* that takes the textual summary of the interview (the Q\&A results) and outputs a structured semantic representation (a simplified knowledge graph in text form). Its job is to extract the key facts from the interview summary and present them in a **consistent, structured format** that will be easy for GPT 4 to ingest and reason over.

**Inputs:** The main input will be the summary of user responses (either copied from GPT 2’s final output or a transcription of the Q\&A if needed). We instruct GPT 3 on the schema/format to use for output. This could be as simple as bullet points of facts, or a list of triples. We’ll keep it human-readable for the workshop while still capturing structure. GPT 3 should incorporate relevant context from the standard as needed (like referencing the control names).

**System Prompt for GPT 3:**

```
You are an AI that transforms interview responses into a structured knowledge graph format. You will be given a summary of a user’s answers about their security practices. Your task is to output the key facts in a **semantic graph** form – essentially, a list of structured statements about the user’s organization and its security controls.

**Instructions:**
- Parse the input text for specific **facts** or data points. Focus on the security control areas (firewall, secure configuration, access control, malware protection, patch management).
- Represent each fact as a simple relationship or attribute. Use a consistent format for each (for example, you can use bullet points where each point contains one relationship).
- Include the subject (implicitly the user’s company or organization), the aspect being described, and the value/status. For example: “Company uses a network firewall: YES” or “Multi-factor authentication for admin accounts: NO”.
- If applicable, you can format as “<Control/Aspect> – <Status/Detail>”. You can also include brief details if relevant (e.g. “Firewall configured properly: Unknown (using defaults)”).
- Ensure every major question/area from the questionnaire is represented in the output, so we have a complete picture in structured form.
- Do not output prose or explanations – just the structured facts. This is meant to be machine-readable (by another AI) and skimmable by a human.

Now, convert the following interview summary into the structured facts format.
```

After setting this prompt, we feed GPT 3 the interview summary from GPT 2 as the user message. GPT 3 will then output something like:

**Example Output from GPT 3:** (assuming the example answers we posited above)

* Company has a network firewall: **Yes**
* Firewall default configuration in use: **Yes** (likely only basic rules)
* Default passwords on new devices: **No (they are changed)**
* Unnecessary services disabled (secure config): **Yes**
* Admin accounts restricted to few users: **Yes**
* Multi-factor auth for admin/remote access: **No**
* Anti-malware software installed on all systems: **Yes**
* Users cannot install unapproved software: **Yes**
* Critical patches applied within 14 days: **No** (patches often take \~30 days)
* Process for ensuring updates on all devices: **Partial** (no automated centralized system)

Each bullet captures an atomic piece of information the user provided, in a clear True/False/Partial manner. This is our **semantic knowledge graph** in text form. It’s essentially a set of attribute–value pairs about the company’s security posture. This structured output is now ready to be handed to GPT 4 for detailed analysis.

*(In the workshop, once GPT 3 produces this, we will review it quickly. It shows how the AI has distilled the conversation into a *checklist of facts*. We’ll mention that in a fully automated pipeline, such structured data could be fed into a graph database or used in code directly, enabling things like traceability and queries. The approach of breaking down into structured data is aligned with making GenAI outputs more explainable and easier to validate.)*

### GPT 4 – “Technical Analysis & Report Writer” Configuration

**Role & Objective:** GPT 4 is configured as a *Security Analyst/Report Writer*. It takes the knowledge graph from GPT 3 and produces a **detailed technical report** that analyzes each point, measures it against the standard, and provides recommendations. GPT 4 essentially does the heavy lifting of interpreting the data and adding expert insights. This stage will merge the user-specific facts with general knowledge of best practices (and the standard requirements) to generate a comprehensive narrative.

**Inputs:** We will feed GPT 4 two main things: (1) the structured facts from GPT 3, and (2) context about the standard’s expectations (if not already known by the model). For the latter, we can include a brief reminder of what full compliance looks like for each control. For example, tell GPT 4: “Under Cyber Essentials, multi-factor authentication is required for administrative accounts; firewalls should be properly configured, etc.” This helps ensure the recommendations are precise. GPT 4’s prompt also needs to specify the format of the output (likely a well-structured report with sections).

**System Prompt for GPT 4:**

```
You are a cybersecurity analyst AI tasked with writing a detailed technical report based on collected data about a company’s security practices. The company was assessed against the [StandardName] standard. You will be given a list of facts (extracted from an interview) about the company’s current security controls. Your job is to analyze these facts relative to [StandardName]’s requirements and produce a comprehensive report with findings and recommendations.

**Instructions:**
1. **Organization & Tone:** Start with a brief introduction summarizing the context (e.g. “This report assesses Company X’s security controls against [StandardName] criteria based on a recent Q&A.”). Then, create sections or paragraphs for each main control area of [StandardName]. For each area (Firewall, Secure Config, Access Control/MFA, Malware Protection, Patch Management, etc.), detail the findings:
   - What the company has in place (from the facts).
   - What is missing or not up to standard.
   - The implications of any gaps (why it matters, potential risks if not addressed).
   - Specific recommendations to achieve or improve compliance in that area.
2. **Use the Input Facts:** The facts provided are authoritative. Base your statements on them. If a fact is “Firewall: Yes, but defaults used”, acknowledge the firewall exists but note that default config may be weak, and recommend tightening rules. If “MFA: No”, explain that this is a non-compliance and a serious risk, then recommend enabling MFA for relevant accounts.
3. **Incorporate Standard Guidance:** Infuse each section with knowledge of [StandardName] requirements. For example, mention what [StandardName] expects for that control (in simple terms) and evaluate the company against it. You can reference [StandardName] guidelines in the explanation (e.g. “According to [StandardName], all administrator accounts should have multi-factor authentication; currently this is not the case.”).
4. **Detail Level:** Be thorough and technical. Assume the reader of this report is technically proficient (e.g. a security manager or auditor) who wants all the details. Include any relevant technical suggestions (e.g. “Ensure the firewall blocks inbound traffic by default and only allows necessary services like HTTPS and VPN.” or “Implement a centralized patch management tool to automate updates.”).
5. **Format:** Use clear headings or bolded labels for each control domain for readability. You can use bullet points for multiple recommendations in a domain. Ensure the report flows logically from one section to the next.
6. **Conclusion:** End with a short conclusion or next steps section. This could re-state the overall security posture (e.g. “Company X meets many fundamentals of [StandardName] but has two major gaps...”) and stress the importance of addressing them, possibly noting any benefits (reduced risk, certification readiness) if improvements are made.

**Data from the Assessment (Facts):**
- Company has a network firewall: Yes
- Firewall configured with default rules: Yes (potentially weak)
- Default passwords on new devices: No (they are changed; good practice)
- Unnecessary services disabled: Yes
- Admin accounts restricted to few: Yes
- Multi-factor auth for admin accounts: No (currently not in use)
- Anti-malware installed on all systems: Yes
- Users cannot install unapproved software: Yes
- Critical patches applied within 14 days: No (patching sometimes takes ~30 days)
- Update process coverage for all devices: Partial (no automated centralized system)

Using the above facts, generate the technical report as described.
```

When GPT 4 receives this, it will compose a detailed report. We expect a structured output, for example:

**Example Outline of GPT 4 Output:**

* *Introduction:* States purpose, e.g. “This document is a Cyber Essentials compliance assessment for Company X, based on a recent questionnaire. It identifies current controls, gaps, and recommendations.”
* *Firewall:* A paragraph noting the company has a firewall (good), but it might be using default configurations. It would explain why a properly configured firewall is critical (to minimize open ports, etc.), and recommend reviewing firewall rules against best practices or Cyber Essentials guidelines (e.g. block all inbound by default, allow only necessary services). Might cite that Cyber Essentials requires a firewall at every internet connection.
* *Secure Configuration:* Discuss how the company changes default passwords and disables unnecessary services (positive findings). Possibly recommend further hardening steps if any. Acknowledge compliance in this area is strong if those practices are consistent.
* *Access Control (Account Management and MFA):* Note that admin accounts are limited (good), but **lack MFA** (bad). Explain the risk of no MFA (password compromise leading to breach of admin accounts) and state that Cyber Essentials mandates MFA for admin and remote access. Strong recommendation to implement MFA (with some guidance on methods). Might also mention periodic access reviews.
* *Malware Protection:* Acknowledge they have anti-malware on all machines and restrict software installation – this meets the standard’s requirements. Maybe recommend ensuring the anti-malware is updated and perhaps using additional measures like email filtering, but overall this is a compliance success.
* *Patch Management:* Point out that not patching within 14 days is a gap relative to Cyber Essentials (which requires prompt patching of critical vulns). Explain the risk (unpatched systems are vulnerable) and recommend instituting a policy or using a tool for faster updates. Mention partial process exists but needs improvement to meet the standard fully.
* *Conclusion:* Summarize overall posture. E.g. “Out of the five control areas, Company X is compliant in three (firewall present, secure config, malware protection) and partially/non-compliant in two (MFA and timely patching). To attain full Cyber Essentials compliance and strengthen security, the company should prioritize implementing MFA and improving patch times. Once these steps are taken, Company X would likely fulfill the requirements to be certified under Cyber Essentials, significantly reducing its cyber risk.” Possibly encourage regular reviews and thank the reader.

This report will likely be **several paragraphs long**, full of technical insight but tailored to the standard’s criteria. It effectively combines the factual graph with domain expertise, providing the “single source of truth” narrative that we can now repurpose.

*(During the workshop, after GPT 4 produces the report, we’ll highlight how comprehensive it is and how it draws on both the user’s data and the standard’s knowledge. We can mention that such a report would normally take an analyst significant time to write, but the AI did it in moments. We’ll also caution that one should always review such output for accuracy – an important training point – but in our case it should be largely on target due to the guided prompts.)*

### GPT 5 – “Persona Briefings Translator” Configuration

**Role & Objective:** GPT 5 is configured as a *Persona-Specific Communication Assistant*. It takes the technical report from GPT 4 and produces multiple outputs, each tailored to a different **audience persona** (CEO, Board, CFO, Technical team, etc.). Essentially, GPT 5 acts as a translator and summarizer, reshaping the tone and content while preserving the core findings. This phase demonstrates delivering the right message to the right stakeholder.

**Inputs:** The primary input is the full technical report from GPT 4. Additionally, we will provide GPT 5 with a definition of each target persona, so it understands their perspective. This can be part of the system prompt or given as a separate “context” block. We should clearly enumerate the personas and what each cares about:

* **CEO (Executive):** Non-technical, cares about business impact, risk to operations/reputation, high-level solutions. Wants brevity and clarity, not details.
* **Board of Directors:** Similar high-level focus on risk and compliance, maybe even shorter attention span. Emphasize strategic implications and assurance that issues are being addressed.
* **CFO (Finance Executive):** Focus on financial ramifications – costs of implementing recommendations vs. cost of potential incidents, compliance fines, ROI, etc. Also fairly high-level but with a financial lens.
* **IT/Security Team Lead:** Very technical perspective, but needs a summary they can turn into an action plan. Will want to know what to do and why, possibly references to specific technical measures. This could be a moderately detailed summary of the tech report, distilled into tasks.
* **Implementer/Engineer:** (Optional) If we include this, it would be extremely granular – possibly a straight checklist of actions without any fluff, or step-by-step instructions. But we might merge this with the Team Lead output for simplicity.

**System Prompt for GPT 5:**

```
You are an AI communications expert who can rewrite technical content for different target audiences (personas) while highlighting the information that matters most to each. You will be given a detailed technical report about a company’s security assessment. Produce a separate briefing for each of the following personas:

**Personas:**
1. **CEO (Executive)** – Audience: Chief Executive Officer. Not technical. Interested in overall risk to business, strategic importance, and reassurance that things are under control. Briefing should be high-level, concise (a few paragraphs or bullet points). Focus on business impact of findings and the value of recommended actions (e.g. “improve security to avoid downtime, protect reputation, ensure customer trust”). Use minimal technical jargon.
2. **Board of Directors** – Audience: Board members (non-executives). They care about governance, compliance, and risk oversight. Briefing should be one page or less, very high-level. Emphasize whether the company meets standards or has gaps, and what the plan is to fix them, in terms of risk management. Possibly use slightly formal tone.
3. **CFO (Finance Executive)** – Audience: Chief Financial Officer. Focus on financial and compliance impact. Briefing should translate findings into cost/risk terms: potential financial losses if gaps aren’t fixed, costs of mitigation vs. benefits, and any compliance obligations (e.g. certifications, avoiding fines). Keep it executive-level but include numbers or budgets if relevant (we can estimate qualitatively if needed, like “low-cost improvement” or “investment in MFA is minimal compared to risk of breach”).
4. **IT/Security Team Lead** – Audience: Head of IT or Security. Technical professional who will implement the changes. Briefing can be more detailed (but still summarizing the big report). Focus on action items: what needs to be done, why it’s important (in technical terms), and perhaps some implementation hints. This can be presented as a list of recommendations or a short action plan. It should still be readable (not just raw checklist – give context for each action). Use some technical language appropriate to an informed practitioner.
*(Optionally)* 5. **IT Engineer/Administrator** – Audience: the person who will carry out the tasks (if different from lead). This could be an even more granular set of steps or a checklist derived from the Team Lead’s plan, phrased as direct instructions. (Include this persona if granular detail is desired.)

**Task:** For each persona above, write a tailored version of the **same underlying content (the security assessment findings and recommendations)**. Preserve factual accuracy but adjust the depth, tone, and framing. You should effectively **translate** the technical report for each audience:
- The CEO and Board versions should be short, focusing on the big picture and risk/status (e.g. “We are mostly compliant but have two important gaps. Plan in place to fix within 3 months. This will reduce risk of X by Y.”).
- The CFO version should mention financial implications, perhaps in terms of risk cost or budget required (even if roughly).
- The IT/Security Lead version should be action-oriented: enumerating what to fix and perhaps referencing the standard for justification (e.g. “Enable MFA on admin accounts – this is required by Cyber Essentials and will greatly reduce account breach risk.”).
- If providing the Engineer checklist, make it a clear list of tasks (like “1. Enable MFA on all admin accounts (tools: e.g. Duo, Authy, or similar). 2. Implement a patch management policy to deploy critical updates within 14 days...” etc.).

Clearly label each output section with the persona it’s intended for (e.g. start with a heading or bold title for each persona).

Now rewrite the content for each persona. The input technical report is below.
```

*(After this prompt, we would input the full text of the GPT 4 technical report as the user message for GPT 5.)*

GPT 5 will then generate multiple sections, each prefaced by the persona name. We expect something like:

**Example Outputs from GPT 5 (summarized):**

* **CEO Briefing:** *“Overall, Company X’s cybersecurity fundamentals are strong, with most baseline controls in place. However, two key areas need attention to meet the Cyber Essentials standard and protect the business: multi-factor authentication (MFA) for administrator accounts, and faster software patching. **Risks:** Without MFA, the company is more exposed to account breaches; without timely patching, systems remain vulnerable to known threats. **Planned Actions:** The team will implement MFA for all admin logins and adopt a routine to install critical updates within 2 weeks. These improvements are expected to significantly reduce the risk of security incidents, safeguarding our operations and reputation. **Status:** With these changes, the company should achieve full compliance with Cyber Essentials, demonstrating to customers and partners our commitment to security.”*

* **Board Briefing:** *“**Cyber Essentials Compliance Status:** Partially compliant. The recent assessment found that while our organization has a firewall, secure configurations, and malware protections in place (meeting several core requirements), we lack multi-factor authentication for high-privilege accounts and our software update process is slower than recommended. **Risks & Impact:** These gaps could increase our vulnerability to cyber incidents (e.g., unauthorized access or exploit of an unpatched flaw). **Remediation Plan:** Management is addressing these by rolling out multi-factor authentication across all admin accounts and tightening our patch management process. Target completion: within next quarter. **Oversight:** The Board should expect a follow-up report confirming closure of these gaps, after which the organization will be fully aligned with Cyber Essentials guidelines. This will strengthen our security posture and may be used in company trust communications.”*

* **CFO Briefing:** *“The cybersecurity assessment identified two main issues with potential financial implications: (1) Lack of multi-factor authentication (MFA) for admin accounts – this elevates the risk of a costly breach (e.g., a compromised admin could lead to serious business disruption, which studies show can cost companies millions in recovery and lost business). (2) Delayed patching of software – this prolongs exposure to known vulnerabilities, increasing breach likelihood. **Cost/Benefit:** The cost to implement MFA is relatively low (mostly configuration and maybe some subscription for an MFA service) compared to the potential cost of a single cyber incident it can prevent. Improving patch management might involve minor investments in IT process or tools, again far outweighed by risk reduction. **Compliance Note:** Achieving the Cyber Essentials certification can also have financial benefits, such as lowering cyber insurance premiums and avoiding regulatory fines by demonstrating strong security controls. **Budget:** A provisional budget of \$X (small) may be allocated for these improvements, which is already accounted for in the IT security budget. The ROI on these measures is high given the mitigation of high-impact cyber risk.”*

* **IT/Security Team Lead Briefing:** *“**Findings Recap:** We have a firewall (okay), secure configurations (good), antivirus and user restrictions (good). Areas to fix: no MFA for admin accounts, and patching is not fast enough. **Impact:** Without MFA, if an admin password is stolen, an attacker could gain full access – unacceptable risk. Slow patching means we leave known holes open for weeks – also high risk. **Action Plan:** 1. **Implement MFA for Administrators:** We need to enable MFA on all admin-level accounts (IT admins, server logins, remote access VPN, etc.). This could be done via \[our Office 365/Azure AD if applicable, or by deploying a solution like Duo]. Aim to complete within 4 weeks. 2. **Improve Patch Management:** Adopt a stricter patch cycle for critical updates. For example, use our RMM (Remote Monitoring & Management) tool or WSUS to push patches faster. We should ensure critical OS and application patches are applied within 14 days of release. Possibly set automatic updates for critical systems or a weekly maintenance window. 3. **Verify Firewall Rules:** Since firewall was on defaults, review and tighten the ruleset – ensure default deny inbound, only necessary ports open (e.g., VPN, web server). 4. **Continuous Monitoring:** Once above are done, monitor compliance: check MFA enrollment for all admins, run monthly vulnerability scans to ensure patch compliance. **Next Steps:** We’ll prioritize MFA first, as it’s a quick win, then focus on patch process improvement. Quarterly, report patch timeliness and MFA status to management to maintain compliance.”*

* *(If an Engineer checklist persona was included, it might list concrete steps like: “- Enable MFA in Azure AD for admin roles (Policy XYZ). - Configure firewall: block all inbound except \[list]. - Deploy update automation via WSUS; schedule weekly auto-updates,” etc. But we can omit here for brevity.)*

As seen, each of these outputs is derived from the same base information but framed very differently. GPT 5 thus provides the ready-made communications for various stakeholders, which is incredibly useful in real-world settings.

*(In the workshop, we will review these persona outputs and possibly discuss whether they hit the mark, letting participants observe how well the AI adapts content. We may even have participants suggest tweaks or additional personas to test GPT 5’s flexibility, time permitting.)*

### GPT 6 – “UI Prototype Generator” Configuration

**Role & Objective:** GPT 6 is configured as a *UI/UX Prototype Generator*, leveraging vibe coding principles. It takes the persona-specific content (from GPT 5) and generates suggestions for UIs or visual presentations that would effectively convey that content to the respective personas. The aim is to end up with, for example, sample code for a dashboard, or HTML for a report, or a description of a slide deck. This shows how we can go **from narrative to application** with AI assistance.

**Inputs:** The inputs will be the outputs from GPT 5 for each persona, or a selected subset. We might do one persona at a time with separate runs, or instruct GPT 6 to handle all in one go. Given time, we might pick two personas to demonstrate: say the CEO (for a dashboard) and the IT team (for a detailed web report or checklist UI). If doing all in one, we need to be clear in the prompt for GPT 6 about organizing its output per persona and possibly specifying the format (code vs description). We also include any guidelines about the tech (if we prefer HTML/CSS, etc.).

**System Prompt for GPT 6:**

```
You are an AI software developer and UX designer. Your task is to create simple UI prototypes based on the briefing content for different personas. We have textual briefings for several personas (CEO, Board, CFO, IT Lead). Now, imagine how to present the key information to each persona in a **user interface or visual format** that best suits their needs, and provide either a description or sample code for it.

**Instructions:**
- For each persona briefing given, propose an appropriate UI design. You can provide this as:
  - **If code is requested:** a snippet of HTML/CSS/JavaScript that could represent a dashboard or interface for that persona, using dummy data from the briefing.
  - **If description is fine:** a clear description of a slide or interface, possibly with pseudo-visual elements (like “[Chart: compliance score]”).
- Tailor the style to the persona:
  - **CEO Dashboard:** Perhaps a one-page web dashboard with a few key metrics (e.g., a big compliance percentage, a green/yellow/red status indicator for overall security, and 2-3 bullet points of top risks or actions). Use simple visuals (icons, colored text for status). Provide HTML/CSS for layout if possible.
  - **Board Presentation Slide:** Possibly a PowerPoint-like single slide outline. Since code for PPT isn’t straightforward, just describe: e.g., title, a bullet list of the two gaps and actions, maybe an infographic icon. (Or if using HTML, simulate a slide with divs and styles).
  - **CFO Report View:** Perhaps a small table or chart showing cost vs risk. Could be a section in the dashboard that highlights cost analysis. For code, maybe a table element with two columns (issue vs potential cost).
  - **IT Team Tool:** An interface that looks like a task tracker. For example, a checklist UI where each recommendation is a checkbox item. Or a simple web page listing actions with status toggles. Provide a structured HTML list with checkboxes for each action item (MFA, patching, etc.), possibly with an expand/collapse for details.
- The UIs should be **simple and self-contained**. We’re not implementing full functionality, just showing the look. Use placeholder values (e.g., “75% compliant” or “MFA: Not Implemented” in red text).
- Comment your code (if any) to explain what each part is (for clarity to the participants).
- Clearly separate each persona’s UI output, e.g., start with a comment or heading naming the persona.

Now, I will provide the persona briefings. Please produce a UI prototype (code or detailed description) for each.
```

*(After this prompt, we feed in the content of the persona briefings from GPT 5 as the user message, or instruct GPT 6 to refer to them abstractly if too long. We might do them one at a time to avoid context length issues.)*

For example, let’s say we do the CEO and IT Lead as two separate requests for brevity. For the CEO, GPT 6 might output:

**Example GPT 6 Output for CEO (Dashboard HTML snippet):**

```html
<!-- CEO Dashboard Prototype -->
<div style="font-family:sans-serif; max-width:600px; margin:20px;">
  <h2>Cyber Essentials Summary – Company X</h2>
  <div style="font-size:48px; font-weight:bold; color:green;">
    80% Compliant 
  </div>
  <p>Status: <span style="color:orange; font-weight:bold;">Partial Compliance</span></p>
  <ul>
    <li>✅ Firewall, Secure Config, Anti-malware in place</li>
    <li>⚠️ Multi-Factor Authentication <strong>not yet implemented</strong> (planned)</li>
    <li>⚠️ Patching delays (updates sometimes >30 days)</li>
  </ul>
  <p><em>Risks are being addressed to improve security and achieve full compliance.</em></p>
</div>
```

*(The above code, if rendered, would show a simple dashboard with a compliance percentage, a status indicator, and bullet points with checkmarks and warning signs for good vs. needs improvement. GPT 6 might also give a short explanation of the design choices in comments or text.)*

For the IT Team interface, GPT 6 might output something like:

```html
<!-- IT Team Action Items Prototype -->
<div style="font-family:sans-serif; max-width:600px; margin:20px;">
  <h2>Security Improvement Plan</h2>
  <ul style="list-style-type:none;">
    <li>
      <input type="checkbox" id="mfaTask"> 
      <label for="mfaTask"><strong>Enable Multi-Factor Authentication</strong> for all admin accounts 
      <span style="color:red;">(Pending)</span></label>
      <p style="margin-left:20px; font-size:0.9em; color:#555;">Using Azure AD or similar, require MFA for IT admins and remote access users. <br>**Due:** 4 weeks</p>
    </li>
    <li>
      <input type="checkbox" id="patchTask"> 
      <label for="patchTask"><strong>Enforce 14-day Patch Window</strong> for critical updates 
      <span style="color:red;">(Pending)</span></label>
      <p style="margin-left:20px; font-size:0.9em; color:#555;">Implement WSUS or patch management tool to automatically deploy updates within 2 weeks of release. <br>**Due:** Ongoing (policy change)</p>
    </li>
    <li>
      <input type="checkbox" id="fwTask" checked> 
      <label for="fwTask"><strong>Review Firewall Configuration</strong> 
      <span style="color:green;">(Completed)</span></label>
      <p style="margin-left:20px; font-size:0.9em; color:#555;">Checked firewall rules, now default deny inbound, only required ports open.</p>
    </li>
  </ul>
</div>
```

This HTML snippet creates a simple checklist of tasks with checkboxes, status in color, and some details indented. It’s an example of an engineer-friendly UI where they can tick off completed tasks and see what’s next. GPT 6 may also describe that “✅ means completed, red text means pending, etc.”

For other personas, GPT 6 might not write code but rather describe a PowerPoint slide or a chart. Since HTML is easy to show, we focused on that. The key is that GPT 6 demonstrates *generating interface code from instructions*, underscoring how AI can help with rapid prototyping and even building tools directly.

*(In the workshop, we can show the raw output of GPT 6 (code), and perhaps quickly copy it into a browser or codepen if feasible to show it renders correctly. Even without live rendering, reading the code and imagined UI will be illustrative. We’ll note that this “vibe coding” approach allows someone with an idea (like “I want a dashboard for this data”) to get a working starting point from AI very quickly, which is a powerful capability in modern development. Participants will thus see the full journey from data to end-user presentation.)*

## Conclusion and Session Structure

We have outlined a comprehensive project plan that takes the participants through building **User-Driven Semantic Persona Graphs** step by step. The workshop will proceed as follows:

* **Introduction (10 min):** Explain the goals and the pipeline (as described in the overview), setting context about GenAI, knowledge graphs, and persona-based outputs. Emphasize how each GPT stage addresses a specific challenge (from data collection to multi-audience communication).
* **Demonstration of Pipeline (30–40 min):** The facilitator will run through GPT 1 to GPT 6 in sequence using the pre-built configurations. This will be done in front of the participants, with one of them (or a volunteer) acting as the “user” answering GPT 2’s questions. We’ll observe the output at each stage, validating and discussing it briefly (e.g., checking the knowledge graph correctness, the thoroughness of the report, etc.). This live demo cements understanding and generates excitement.
* **Interactive Creation (40+ min):** Participants will then create the GPTs themselves (possibly in pairs or individually). We will provide them with the **artifacts (prompts and instructions)** for each GPT as starting points (the ones detailed above). They can choose to recreate the same scenario (Cyber Essentials) or try a different standard (some might pick GDPR or ISO27001 for variety). The facilitator and assistants will help them copy the prompts, adjust any details, and run the pipeline. This solidifies their skills in prompt design and using ChatGPT’s custom GPT builder.
* **Q\&A and Discussion (time permitting):** We’ll wrap up by discussing potential improvements (like automating the data flow between GPTs, integrating a real graph database or using function calling for structured output, etc.), and how these techniques could apply to their own projects. We’ll highlight the *provenance and transparency* gained by the multi-step approach (each output can be traced to an input fact) and how the persona outputs can enhance stakeholder communication in any domain. We also point out that such pipelines could be deployed in a **serverless** manner (each phase as a function or API), referencing Dinis’s work on serverless graph databases and AI orchestration (e.g. MGraph-DB) to show the future is headed that way.

By the end of the session, the participants will have a concrete example of GenAI-driven development: from raw text to a knowledge graph to stakeholder-specific insight, and even UI prototypes – all done rapidly with AI assistance. This not only trains them on GenAI capabilities but also sparks ideas on how they can apply similar patterns (e.g. breaking problems into GPT phases, using AI to generate code) in their own technical domains. The comprehensive plan and provided GPT prompt artifacts will ensure the workshop runs smoothly and delivers maximum value in illustrating the “art of the possible.”

**Sources:**

* Dinis Cruz, *“Beyond Static Ontologies: How GenAI Powers Self-Improving Knowledge Graphs,”* LinkedIn (Mar 2025) – on using GenAI with evolving knowledge structures and tailoring outputs to stakeholders.
* Dinis Cruz, *“Building Semantic Knowledge Graphs with LLMs: Inside MyFeeds.ai’s Multi-Phase Architecture,”* MyFeeds Blog (Mar 2025) – describes a 4-stage LLM pipeline and benefits of splitting tasks for explainability and determinism.
* Jakob Nielsen, *“Vibe Coding and Vibe Design,”* UX Tigers (Mar 2025) – explains the concept of vibe coding where AI generates code from high-level descriptions.
