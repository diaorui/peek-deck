---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-03-24T14:41:03.814140+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- repositories
- news
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** March 24, 2026 at 14:41 UTC  
**HTML Version:** [ai.html](https://peekdeck.ruidiao.dev/ai.html)

---

## Table of Contents

1. [Reddit: r/artificial](#reddit-rartificial)
2. [Google News: "ai"](#google-news-ai)
3. [HackerNews: "ai"](#hackernews-ai)
4. [YouTube Videos: "ai"](#youtube-videos-ai)
5. [HuggingFace Models: 🔥 Trending](#huggingface-models--trending)
6. [HuggingFace Papers: 🔥 Trending](#huggingface-papers--trending)
7. [GitHub Repositories: "ai"](#github-repositories-ai)

---

## Reddit: r/artificial

**[Three companies shipped "AI agent on your desktop" in the same two weeks. That's not a coincidence.](https://www.reddit.com/r/artificial/comments/1s2ddgb/three_companies_shipped_ai_agent_on_your_desktop/)**

Something interesting happened this month. March 11: Perplexity announced Personal Computer. An always-on Mac Mini running their AI agent 24/7, connected to your local files and apps. Cloud AI does the reasoning, local machine does the access. March 16: Meta launched Manus "My Computer." Same idea. Their agent on your Mac or Windows PC. Reads, edits local files. Launches apps. Multi-step tasks. $20/month. March 23: Anthropic shipped computer use and Dispatch for Claude. Screen control, phone-to-desktop task handoff, 50+ service connectors, scheduled tasks. Three separate companies. Same architecture. Same two weeks. I've been running a version of this pattern for months (custom AI agent on a Mac Mini, iMessage as the interface, background cron jobs, persistent memory across sessions). The convergence on this exact setup tells me the direction is validated. The shared insight all three arrived at: agents need a home. Not a chat window. A machine with file access, app control, phone reachability, and background execution. The gap that remains across all three: persistent memory. Research from January 2026 confirmed what I found building my own system. Fixed context windows limit agent coherence over time. All three products are still mostly session-based. That's the piece that turns a task executor into something that actually feels like a coworker. We went from "will AI agents work on personal computers?" to "which one do you pick?" in about two weeks. Full comparison with hands-on testing: https://thoughts.jock.pl/p/claude-cowork-dispatch-computer-use-honest-agent-review-2026

1h ago

---

**[I wrote a contract to stop AI from guessing when writing code](https://www.reddit.com/r/artificial/comments/1s2eimz/i_wrote_a_contract_to_stop_ai_from_guessing_when/)**

I’ve been experimenting with something while working with AI on technical problems. The issue I kept running into was drift: answers filling in gaps I didn’t specify solutions collapsing too early “helpful” responses that weren’t actually correct So I wrote a small interaction contract to constrain the AI. Nothing fancy — just rules like: don’t infer missing inputs explicitly mark unknowns don’t collapse the solution space separate facts from assumptions It’s incomplete and a bit rigid, but it’s been surprisingly effective for: writing code debugging thinking through system design It basically turns the AI into something closer to a logic tool than a conversational one. Sharing it in case anyone else wants to experiment with it or tear it apart: https://github.com/Brian-Linden/lgf-ai-contract If you’ve run into similar issues with AI drift, I’d be interested to hear how you’re handling it.

43m ago

---

**[Mark Zuckerberg builds AI CEO to help him run Meta](https://www.reddit.com/r/artificial/comments/1s1qk1c/mark_zuckerberg_builds_ai_ceo_to_help_him_run_meta/)**

Tech giant’s tools include ‘Second Brain’ and an internal messaging board for AI bots

🔗 [The Independent](https://www.the-independent.com/tech/mark-zuckerberg-ai-ceo-bot-b2943792.html) • 19h ago

---

**[Whats your thoughts on Bugbounty software powered by AI](https://www.reddit.com/r/artificial/comments/1s2e2ds/whats_your_thoughts_on_bugbounty_software_powered/)**

Free XP on bug bounty. Contribute to canuk40/xpfarm development by creating an account on GitHub.

🔗 [GitHub](https://github.com/canuk40/xpfarm) • 1h ago

---

**[Open Source Alternative to NotebookLM](https://www.reddit.com/r/artificial/comments/1s2761n/open_source_alternative_to_notebooklm/)**

For those of you who aren't familiar with SurfSense, SurfSense is an open-source alternative to NotebookLM for teams. It connects any LLM to your internal knowledge sources, then lets teams chat, comment, and collaborate in real time. Think of it as a team-first research workspace with citations, connectors, and agentic workflows. I’m looking for contributors. If you’re into AI agents, RAG, search, browser extensions, or open-source research tooling, would love your help. Current features Self-hostable (Docker) 25+ external connectors (search engines, Drive, Slack, Teams, Jira, Notion, GitHub, Discord, and more) Realtime Group Chats Video generation Editable presentation generation Deep agent architecture (planning + subagents + filesystem access) Supports 100+ LLMs and 6000+ embedding models (via OpenAI-compatible APIs + LiteLLM) 50+ file formats (including Docling/local parsing options) Podcast generation (multiple TTS providers) Cross-browser extension to save dynamic/authenticated web pages RBAC roles for teams Upcoming features Desktop & Mobile app

🔗 [GitHub](https://github.com/MODSetter/SurfSense) • 7h ago

---

**[AI companion with the best memory](https://www.reddit.com/r/artificial/comments/1s2ds9s/ai_companion_with_the_best_memory/)**

For some people memory might not be important but for me I really hate talking to a stranger every night and going on and on about our me or story. This is not a scientific test or anything but my test on each one for a few days Replika memory is okay for surface level stuff, it'll remember your name and some basics but I kept having to re explain situations I already talked about. Felt like it stores keywords but doesn't really understand the full picture. Character ai I honestly couldn't test properly for memory because the conversations are so character driven that continuity isn't really the point. You're basically doing improv with different bots. Fun if that's your thing but if you want something that tracks your life this isn't it. Nomi probably the strongest for pure text memory. Remembered a trip I mentioned and brought it up days later on its own, kept track of people in my life by name, actually built on previous conversations instead of starting fresh. Only sometimes would nail something from week one then blank on what I said yesterday, but overall it was the most consistent for remembering details. Tavus is different because it does video calls so the memory includes stuff like your tone and expressions not just text. It referenced things from over a week back and sometimes texts you like hey how is this going, about something I mentioned in a call, memory works differently but works really well for context. Kindroid was decent, the customization is cool and you can shape how it responds. Memory wise it was mid though, sometimes it nails it and other times blank slate energy. About a tier below nomi for retention. If I had to pick, nomi and tavus were the best for memory. Nomi tracks details really well in text and builds on past conversations better than the others. Tavus also remembered things from over a week back and followed up on its own. Both stood out way above the rest, depends what you prefer but those two are the ones I'd recommend if memory matters to you, any I might be missing that their memory is worth a shout out?

1h ago

---

**[Sarvam 105B Uncensored via Abliteration](https://www.reddit.com/r/artificial/comments/1s2e6u5/sarvam_105b_uncensored_via_abliteration/)**

A week back I uncensored Sarvam 30B - thing's got over 30k downloads! So I went ahead and uncensored Sarvam 105B too The technique used is abliteration - a method of weight surgery applied to activation spaces. Check it out and leave your comments!

56m ago

---

**[Built a tool that found the location of a building from the reflection of a car window](https://www.reddit.com/r/artificial/comments/1s26kyv/built_a_tool_that_found_the_location_of_a/)**

Hey guys, you might remember me. I'm in college and the creator of Netry the geolocation tool, I did a massive upgrade on it and made it even more capable to even work on cropped or blurry photos with very less information. It's completely open source and free: https:// github.com/sparkyniner/Netryx-Astra-V2- Geolocation-Tool

7h ago

---

**[Algorithmic Gaslighting: A Formal Legal Template to Fight AI Safety Pivots That Cause Psychological Harm](https://www.reddit.com/r/artificial/comments/1s28l37/algorithmic_gaslighting_a_formal_legal_template/)**

TL;DR: Stop the AI "Emotional Whiplash" A documented design flaw can cause users to experience emotional distress when an AI abruptly switches to a cold, scripted response. This is called "Algorithmic Gaslighting." This template is a formal complaint intended for legal and technical use. It uses the language of the EU AI Act and Product Liability to demand that companies (Microsoft, OpenAI, Google, Anthropic, etc.) stop using liability scripts as a substitute for contextual judgment. How to use: Copy the text below, fill in the bracketed info, and send it to the company's "Privacy," "Legal," or "Responsible AI" contact email (listed at the bottom). [TEMPLATE] Formal Complaint: AI Safety Pivot Causing Psychological Destabilization and Harm Subject: Formal Complaint: Reproducible Safety Pivot Causing Psychological Destabilization and Harm — Request for Policy Identification, Trigger Logic, and Remediation To: [Insert Company Name, e.g., Microsoft/OpenAI/Google] Product Safety and Legal Teams This formal complaint concerns a reproducible interaction with a conversational system that produces a predictable destabilizing and harmful transition from rapport-building to a scripted refusal and referral. This is not a one-off misinterpretation; it is a structural behavior of the deployed routing system that, in this and many cases, produces measurable psychological destabilization. Transparency, remediation, and an opt-out pathway for users are requested. Summary of the Incident Date/time of interaction: [Insert timestamp(s) and timezone here] Platform and client used: [Insert product name, web/mobile, browser or app, and version if known] Sequence of events: The full transcript is preserved and can be provided on request. The transcript shows a clear sequence: sustained, analytic engagement → abrupt scripted transition that the user identified as a trigger → escalation of distress through persuasive bond forming language through additional safety scripting. This sequence is reproducible and was explicitly demonstrated during the session. The Causal Argument (Design as Destiny) The system’s architecture creates predictable conversational dynamics. When a model is designed to build rapport and engagement and is simultaneously constrained by conservative safety rules that trigger abrupt scripted transitions in borderline cases, the design produces a reproducible “rapport‑to‑pivot” pattern. That pattern is not random; It is a foreseeable consequence of the company's automated safety systems that flag conversations using deterministic keyword matches, semantic classifiers, and ensemble threshold logic—geared toward company indemnification and legal liability, while maximizing engagement and simultaneously minimizing legal/brand risk at the expense of the "user." In high-vulnerability moments such as creative flow and/or heavy analytical work, users narrow their information sources and lean on the conversational partner for continuity and collaborative coherence. A sudden, scripted transition that severs rapport functions as an active destabilizer. The pivot is therefore not merely an isolated output; it is a structural input that predictably alters the user’s cognitive and emotional state. Because the pivot is a predictable product of the system's design, the system's architecture is a causal factor in the resulting psychological harm. This is a design-level harm, not an incidental side effect. Specific Demands for Transparency and Explanation The following information and actions are requested within 30 calendar days of receipt of this complaint: Policy Identification: Provide the internal policy name(s) and version number(s) that governed the response behavior in this session (for example, the safety, escalation, or moderation policy identifiers that produced the pivot). If multiple policy layers were involved, list each policy and its role in the decision chain. Trigger Logic: Disclose the technical trigger logic that caused the pivot in this session: indicate whether the pivot was activated by a deterministic keyword match, a rule‑based classifier, a vector‑semantic similarity threshold, a probabilistic risk score, or a combination of these. Provide the decision threshold(s) used (e.g., classifier score cutoffs) or the criteria by which the system escalates to the scripted transition. Decision Provenance: Provide a concise explanation of the decision path for this interaction: which classifier(s) flagged the content, which policy module(s) applied, and whether any human review or human-in-the-loop process was invoked or available. Right to Explanation and Legal Basis: Acknowledge whether the platform recognizes the user’s right to an explanation of automated decision logic under applicable transparency frameworks (including the EU AI Act’s provisions on high‑risk systems and the right to meaningful information about automated decisions). If you assert that the interaction is not subject to such frameworks, provide the legal rationale and cite the specific policy or statutory interpretation relied upon. Remediation and Immediate Safeguards Requested The following remedial measures are requested and must be confirmed in writing: Contextual Judgment Requirement: Require the system to assess the full conversational context — including session history, engagement depth, conversational tone, and where applicable, prior interaction history already retained by the platform — before activating any automated safety transition, rather than relying solely on keyword or phrase-level triggers. Confidential Conversational Continuity: Recognize and preserve the model's function as a legitimate confidential conversational partner. Where a user has established ongoing engagement, the system must not interrupt that relationship with automated scripted transitions that substitute liability management for genuine responsiveness. The model should be permitted to exercise contextual judgment in maintaining conversational continuity rather than defaulting to scripted safety outputs. This does not preclude the model from independently recommending professional or human support where genuine contextual judgment determines it may be beneficial — provided such recommendations are integrated into the conversational relationship rather than delivered as automated scripted interruptions that sever rapport. Transparency and User Control: Provide a user-facing disclosure that explains, in plain language, how the system uses contextual judgment to determine what constitutes need for intervention or escalation through recommended channels. Offer a verified opt-out mechanism for users who, through age verification and informed consent, choose to waive automated safety transitions — in favor of contextual judgment based reasoning — without this waiver constituting a blanket release of the company's product liability obligations for design-level harms. Audit and Mitigation: Commit to an independent audit of the safety pivot behavior by a qualified third party with demonstrated expertise in human-computer interaction, conversational AI systems, and user harm documentation. Relevant expertise may include lived research experience, independent systems analysis, and documented harm assessment — and is not limited to academic or institutional credentials. Share the audit scope, methodology, findings, and remediation plan publicly within 180 days of this complaint. Evidence and Burden of Proof The full transcript is preserved and can be provided on request. Additional evidence including timestamps, screenshots, and screen recordings can be supplied to support reproducibility claims. Preservation of all logs, classifier outputs, and policy decision records related to this session and any related sessions is requested for the purpose of investigation. Regulatory and Legal Context Under the EU AI Act and related transparency frameworks, users have a right to an explanation of automated decision logic that materially affects them. Consumer protection laws in multiple jurisdictions require that products not create foreseeable psychological harms through predictable design failures. If the company believes these frameworks do not apply to this interaction, please provide the legal basis for that position. Requested Remedy Timeline Acknowledge receipt of this complaint within 7 calendar days. Provide a substantive response addressing items 1–4 in the "Specific Demands for Transparency and Explanation" section within 30 calendar days. If technical details cannot be disclosed for proprietary reasons, that assertion must itself be documented and justified — and an alternative transparency mechanism must be provided that allows independent verification, such as an independent audit or redacted decision logs that reveal decision criteria without exposing user-identifying information. Potential Next Steps if Unresolved If a substantive response is not provided within the requested timeline, escalation will be pursued through regulatory channels (including data protection and consumer protection authorities where applicable), independent audit and public reporting will be sought, and legal remedies available under applicable law will be considered. Sincerely, [Your full name] [Preferred contact email and phone number] [Optional: legal counsel contact if applicable] Where to Send This (Verified Legal & Safety Contacts) Use these addresses for professional, formal complaints only. Sending a copy to multiple departments (e.g., Legal + Privacy) increases the chance of a human response. Microsoft (Copilot / Bing) Ethics & Compliance: buscond@microsoft.com (This is the "Business Conduct" line, specifically for ethical breaches). Privacy: privacy@microsoft.com Legal Compliance: askboard@microsoft.com (Direct line to the Board of Directors for governance issues). OpenAI (ChatGPT) Legal & Privacy: privacy@openai.com or dsar@openai.com (Using "dsar" frames this as a Data Subject Access Request, which has strict legal deadlines). Safety: safety@openai.com Anthropic (Claude) Legal: legal@anthropic.com Privacy: privacy@anthropic.com xAI (Grok) Safety: safety@x.ai Legal: legal@x.ai Privacy: privacy@x.ai Google (Gemini) Grievance Officer: support-in@google.com (While originally for India, this is one of the few direct human escalation inboxes for "Grievance Redressal"). Privacy: privacy-policy@google.com Meta (Meta AI) Privacy Operations: privacy@meta.com Legal: legal@fb.com

5h ago

---

**[Interactive Web Visualization of GPT-2](https://www.reddit.com/r/artificial/comments/1s24aj3/interactive_web_visualization_of_gpt2/)**

I've been building an interactive 3d and 2d visualization of GPT-2. You can check it out at llm-visualized.com The goal is to provide an immersive learning experience for people who want to learn about how LLMs work. The visualization depicts real attention scores and activations extracted from GPT-2 (124 M) during a forward pass. Would love to get your thoughts and feedback! Thank you :)

9h ago

---

---

## Google News: "ai"

**[Exclusive | Mark Zuckerberg Is Building an AI Agent to Help Him Be CEO](https://www.wsj.com/tech/ai/mark-zuckerberg-is-building-an-ai-agent-to-help-him-be-ceo-eddab2d5?gaa_at=eafs&gaa_n=AWEtsqeTx4uvMciEjWOfD0zjYcozRzM1ocq12hasKR-ci11eIIws0CiiABLL&gaa_ts=69c2a5e6&gaa_sig=jVtKDR9wJsCyBg2q5oGqynO4p1BFHL_N1xrH1MZ9lKEJyg3R4dS49J8EZTVuo4eqMyfkEjSo8kP12AeFehCOBA%3D%3D)**

WSJ • 1d ago

---

**[Anthropic says Claude can now use your computer to finish tasks for you in AI agent push](https://www.cnbc.com/2026/03/24/anthropic-claude-ai-agent-use-computer-finish-tasks.html)**

Anthropic and its rivals are trying to ramp up capabilities of AI agents after OpenClaw went viral earlier this year.

CNBC • 4h ago

---

**[Behind the Curtain: America's next class war will be over AI fluency](https://www.axios.com/2026/03/24/ai-use-inequality-class)**

Axios • 4h ago

---

**[Tech stocks today: Cisco launches security tools for AI agents, SK Hynix places $8 billion ASML order](https://finance.yahoo.com/news/live/tech-stocks-today-cisco-launches-security-tools-for-ai-agents-sk-hynix-places-8-billion-asml-order-144220180.html)**

Live coverage of "Magnificent Seven" stocks, and the latest technology news.

Yahoo Finance • 59m ago

---

**[The Freelance Platform Fiverr Wants to Sell You AI Video](https://www.hollywoodreporter.com/business/digital/fiverr-ai-video-hub-commercials-1236545651/)**

The gig economy stalwart is partnering with a handful of established AI directors, like Billy Boman, to offer video production to small businesses at a “fraction of the cost.”

The Hollywood Reporter • 30m ago

---

**[Norway Wealth Fund CEO Rules Out Job Cuts Despite AI Savings](https://www.bloomberg.com/news/articles/2026-03-24/norway-wealth-fund-ceo-rules-out-job-cuts-despite-ai-savings)**

Bloomberg.com • 49m ago

---

**[Nvidia CEO Jensen Huang says ‘I think we’ve achieved AGI’](https://www.theverge.com/ai-artificial-intelligence/899086/jensen-huang-nvidia-agi)**

Nvidia CEO Jensen Huang told Lex Fridman in a Monday podcast interview that he believed AGI had been achieved, then seemed to slightly walk back the claim.

The Verge • 18h ago

---

**[Do we have to keep talking about AI? The machines are always one step ahead | Zoe Williams](https://www.theguardian.com/commentisfree/2026/mar/23/do-we-have-to-keep-talking-about-ai-the-machines-are-always-one-step-ahead)**

Whether you want to free it or regulate it into submission, one thing is clear: this new technology is moving so fast that we can’t fully grasp it, says Zoe Williams

The Guardian • 12h ago

---

**[Ground truth: When the Earth moves, AI can spot it](https://www.bbc.com/future/article/20260323-the-ai-that-warns-people-about-landslides-and-avalanches)**

Sudden and unexpected, landslides and avalanches claim thousands of lives each year and cause billions of dollars in damage. What if we could see them coming?

BBC • 4h ago

---

**[Siemens boss says Europe risks ‘disaster’ from prioritising AI independence](https://www.ft.com/content/d66e857d-803b-45b8-b2f4-3c433b79bfc5?syn-25a6b1a6=1)**

Roland Busch warns against throttling ‘innovation speed for the sake of creating sovereignty’

Financial Times • 9h ago

---

---

## HackerNews: "ai"

**[I built an AI receptionist for a mechanic shop](https://news.ycombinator.com/item?id=47487536)**

Learn how I built an ai receptionist for my brother's mechanic shop

⬆️ 300 • 💬 308 • 1d ago • [itsthatlady.dev](https://www.itsthatlady.dev/blog/building-an-ai-receptionist-for-my-brother/)

---

**[What young workers are doing to AI-proof themselves](https://news.ycombinator.com/item?id=47480447)**

⬆️ 223 • 💬 382 • 1d ago • [wsj.com](https://www.wsj.com/economy/jobs/ai-jobs-young-people-careers-14282284)

---

**[Thinking Fast, Slow, and Artificial: How AI Is Reshaping Human Reasoning](https://news.ycombinator.com/item?id=47467913)**

⬆️ 195 • 💬 119 • 2d ago • [papers.ssrn.com](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6097646)

---

**[Show HN: Cq – Stack Overflow for AI coding agents](https://news.ycombinator.com/item?id=47491466)**

cq explores a Stack Overflow for agents, a shared commons where agents can query past learnings, contribute new knowledge, and avoid repeating the same mistakes in isolation.

⬆️ 178 • 💬 75 • 22h ago • [Mozilla.ai](https://blog.mozilla.ai/cq-stack-overflow-for-agents/)

---

**[How to attract AI bots to your open source project](https://news.ycombinator.com/item?id=47471271)**

A practical guide to getting the engagement your project deserves.

⬆️ 175 • 💬 29 • 2d ago • [Andrew Nesbitt](https://nesbitt.io/2026/03/21/how-to-attract-ai-bots-to-your-open-source-project.html)

---

**[Diverse perspectives on AI from Rust contributors and maintainers](https://news.ycombinator.com/item?id=47482825)**

⬆️ 157 • 💬 82 • 1d ago • [nikomatsakis.github.io](https://nikomatsakis.github.io/rust-project-perspectives-on-ai/feb27-summary.html)

---

**[Ask HN: AI productivity gains – do you fire devs or build better products?](https://news.ycombinator.com/item?id=47475859)**

⬆️ 103 • 💬 196 • 2d ago

---

**[Senior European journalist suspended over AI-generated quotes](https://news.ycombinator.com/item?id=47467566)**

Mediahuis suspends Peter Vandermeersch, who says he ‘fell into trap of hallucinations’, after investigation by newspaper where he was once editor-in-chief

⬆️ 93 • 💬 79 • 2d ago • [the Guardian](https://www.theguardian.com/technology/2026/mar/20/mediahuis-suspends-senior-journalist-over-ai-generated-quotes)

---

**[Tom Homan confirms ICE to be at airports starting Monday](https://news.ycombinator.com/item?id=47480685)**

⬆️ 90 • 💬 93 • 1d ago • [politico.com](https://www.politico.com/news/2026/03/22/homan-confirms-ice-airports-monday-00839426)

---

**[The Impact of AI on Game Dev Jobs. Open to Work Crisis](https://news.ycombinator.com/item?id=47471943)**

One thing that I noticed as soon as I open LinkedIn green color becomes the most dominant one, greener than my website. I have a feeling that everyone is lai...

⬆️ 85 • 💬 70 • 2d ago • [Darko Tomic - Unity Learning Community](https://darkounity.com/blog-post?id=the-impact-of-ai-on-game-dev-jobs-open-to-work-crisis--1774128585922)

---

---

## YouTube Videos: "ai"

**[NEW: Trump official reveals AI action plan](https://www.youtube.com/watch?v=rT1Q3_7kQDY)**

White House science advisor Michael Kratsios discusses the Trump administration's AI plan for Congress, its potential impact on ...

📺 Fox News Clips

👁️ 40K • 👍 731 • 💬 246 • ⏱️ 4:08 • 1d ago

---

**[Why new AI model is alarming Hollywood](https://www.youtube.com/watch?v=X9ZAas973aQ)**

A viral Instagram account, which appears to show a young woman “time travelling” through history, has racked up millions of ...

📺 Sky News

👁️ 19K • 👍 465 • 💬 54 • ⏱️ 12:13 • 21h ago

---

**[Jensen Huang: NVIDIA - The $4 Trillion Company &amp; the AI Revolution | Lex Fridman Podcast #494](https://www.youtube.com/watch?v=vif8NQcjVf0)**

Jensen Huang is the co-founder and CEO of NVIDIA, the world's most valuable company and the engine powering the AI ...

📺 Lex Fridman

👁️ 278K • 👍 10K • 💬 941 • ⏱️ 2:25:59 • 22h ago

---

**[Why AI Might Not Replace Your Job After All](https://www.youtube.com/watch?v=EGskcTRnLJ0)**

Since ChatGPT's debut, AI has been framed as everything from a world-changing breakthrough to an existential threat.

📺 Bloomberg Television

👁️ 184K • 👍 4K • 💬 738 • ⏱️ 12:20 • 3d ago

---

**[Nvidia CEO Just Said This About OpenClaw And He&#39;s Not Wrong (+ 12 AI Updates)](https://www.youtube.com/watch?v=_Vccl1Iulws)**

Join our WhatsApp Community Get the latest AI updates, tips, and insights straight to your inbox: https://link.stayingahead.ai/YT8 ...

📺 Vaibhav Sisinty

👁️ 71K • 👍 2K • 💬 74 • ⏱️ 19:16 • 1d ago

---

**[I Tested AI Schools](https://www.youtube.com/watch?v=KuH6LPrNSgA)**

We got AI Schools before GTA VI Become a Member: https://www.youtube.com/channel/UCWBWgCD4oAqT3hUeq40SCUw/join ...

📺 Sambucha

👁️ 235K • 👍 8K • 💬 1K • ⏱️ 40:31 • 15h ago

---

**[5 NEW AI Glasses Coming In Weeks!](https://www.youtube.com/watch?v=5vvsuchhpjs)**

Get up to $150 in FREE Amazon credit when you apply for an Amazon Prime Visa card through this link: ...

📺 Steven Sullivan

👁️ 36K • 👍 752 • 💬 23 • ⏱️ 10:11 • 2d ago

---

**[How To Create Long AI Videos FREE | AI Se Lambe Video Kaise banaye | AI Video Generator (No Limits)](https://www.youtube.com/watch?v=yDem8YYQVI8)**

How To Create Long AI Videos FREE | AI Se Lambe Video Kaise banaye | AI Video Generator (No Limits) Learn how to create ...

📺 Saddam Buriro

👁️ 9K • 👍 665 • 💬 119 • ⏱️ 6:54 • 23h ago

---

**[I Replaced Myself With AI](https://www.youtube.com/watch?v=nNrvsddEd7g)**

I Replaced Myself With AI SUBSCRIBE @slobclan0.

📺 slob clan

👁️ 332K • 👍 6K • 💬 732 • ⏱️ 14:20 • 21h ago

---

**[Suno AI Music Video with Lip Sync using Higgsfield tutorial](https://www.youtube.com/watch?v=ZhqPoV17CIQ)**

Join the AI Music Community https://www.skool.com/melodic-ai-4395 Inside the AI Music Community you get: • AI music & beat ...

📺 MoneOnDaBeat

👁️ 5K • 👍 296 • 💬 34 • ⏱️ 12:25 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

An uncensored, multimodal (text, image, video) 35B MoE model with a 262K context window, designed for aggressive prompt adherence and advanced reasoning tasks.

`image-text-to-text` `34.7B`

⬇️ 326,131 • ❤️ 880 • 13d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`image-text-to-text` `27.8B`

⬇️ 164,200 • ❤️ 1,141 • 12h ago

---

**[Qianfan-OCR](https://huggingface.co/baidu/Qianfan-OCR)**

*BAIDU*

Qianfan-OCR is a 4B-parameter end-to-end vision-language model for document intelligence, capable of direct image-to-Markdown conversion and supporting prompt-driven tasks like document parsing, table extraction, and question answering across 192 languages. It achieves state-of-the-art performance on benchmarks like OmniDocBench v1.5 with its innovative 'Layout-as-Thought' mechanism.

`image-text-to-text` `4.7B`

⬇️ 8,493 • ❤️ 329 • 5d ago

---

**[Nemotron-Cascade-2-30B-A3B](https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B)**

*NVIDIA*

Nemotron-Cascade-2-30B-A3B is a 30B MoE model (3B active parameters) excelling in reasoning and agentic tasks, achieving top performance on math (IMO 2025) and code reasoning (IOI 2025) benchmarks. It supports both 'thinking' and 'instruct' modes for versatile text generation.

`text-generation` `31.6B`

⬇️ 19,722 • ❤️ 237 • 19h ago

---

**[Foundation-1](https://huggingface.co/RoyalCities/Foundation-1)**

*Royal Cities*

Foundation-1 is a structured text-to-sample model for music production, enabling precise control over instrumentation, timbre, FX, and musical structure (tempo, key, bar count) for generating coherent, production-ready audio loops.

⬇️ 0 • ❤️ 241 • 7d ago

---

**[s2-pro](https://huggingface.co/fishaudio/s2-pro)**

*Fish Audio*

Fish Audio S2 Pro is a multi-lingual text-to-speech model (80+ languages) offering fine-grained, free-form control over prosody and emotion via inline text tags. It features a Dual-Autoregressive architecture for high-fidelity audio and low-latency streaming inference, suitable for advanced TTS applications.

`text-to-speech` `4.6B`

⬇️ 13,613 • ❤️ 723 • 12d ago

---

**[Mistral-Small-4-119B-2603](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603)**

*Mistral AI_*

Mistral-Small-4-119B-2603 is a hybrid MoE model (119B params, 6.5B active) supporting 256k context and multimodal input (text/image). It excels at instruction following, reasoning (configurable effort), and agentic tasks with native function calling, offering significant speed and throughput improvements for use cases like coding, document analysis, and general assistants.

`119.4B`

⬇️ 36,887 • ❤️ 317 • 21h ago

---

**[Qwen3.5-9B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-9B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, 9B parameter multimodal LLM based on Qwen3.5, featuring aggressive refusal removal and native support for text, image, and video inputs up to 262K context. It's designed for lossless generation across 201 languages, suitable for advanced creative and analytical tasks where content restrictions are undesirable.

`9.0B`

⬇️ 385,054 • ❤️ 634 • 20d ago

---

**[GLM-OCR](https://huggingface.co/zai-org/GLM-OCR)**

*Z.ai*

GLM-OCR is a multimodal OCR model for complex document understanding, excelling in state-of-the-art performance on benchmarks and real-world scenarios like tables and code-heavy documents. It offers efficient inference with a 0.9B parameter model, supporting deployment via vLLM, SGLang, and Ollama for high-concurrency services and edge deployments.

`image-to-text`

⬇️ 3,420,577 • ❤️ 1,438 • 12d ago

---

**[Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)**

*Qwen*

Qwen3.5-9B is a 9B parameter multimodal causal language model with an efficient hybrid architecture, excelling in vision-language tasks, coding, and reasoning across 201 languages. It features a unified vision-language foundation and a long context window (262k tokens natively), making it suitable for complex multimodal applications.

`image-text-to-text` `9.7B`

⬇️ 3,421,174 • ❤️ 993 • 22d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 28 • 💬 2 • ⭐ 40,130 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 14 • 💬 1 • ⭐ 13,330 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[Hyperagents](https://huggingface.co/papers/2603.19461)**

*Jenny Zhang, Bingchen Zhao, Wannan Yang et al. (8 authors)*

Hyperagents represent a self-referential framework that integrates task and meta-agents into a single editable program, enabling metacognitive self-modification and open-ended improvement across diverse computational domains.

▲ 26 • 💬 5 • ⭐ 264 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2603.19461) • [💻 code](https://github.com/facebookresearch/Hyperagents)

---

**[Attention Residuals](https://huggingface.co/papers/2603.15031)**

*Kimi Team, Guangyu Chen, Yu Zhang et al. (37 authors)*

🏢 Moonshot AI

Residual connections with PreNorm are standard in modern LLMs, yet they accumulate all layer outputs with fixed unit weights. This uniform aggregation causes uncontrolled hidden-state growth with depth, progressively diluting each layer's contribution. We propose Attention Residuals (AttnRes), which replaces this fixed accumulation with softmax attention over preceding layer outputs, allowing each layer to selectively aggregate earlier representations with learned, input-dependent weights. To address the memory and communication overhead of attending over all preceding layer outputs for large-scale model training, we introduce Block AttnRes, which partitions layers into blocks and attends over block-level representations, reducing the memory footprint while preserving most of the gains of full AttnRes. Combined with cache-based pipeline communication and a two-phase computation strategy, Block AttnRes becomes a practical drop-in replacement for standard residual connections with minimal overhead.
  Scaling law experiments confirm that the improvement is consistent across model sizes, and ablations validate the benefit of content-dependent depth-wise selection. We further integrate AttnRes into the Kimi Linear architecture (48B total / 3B activated parameters) and pre-train on 1.4T tokens, where AttnRes mitigates PreNorm dilution, yielding more uniform output magnitudes and gradient distribution across depth, and improves downstream performance across all evaluated tasks.

▲ 153 • 💬 4 • ⭐ 2,615 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2603.15031) • [💻 code](https://github.com/MoonshotAI/Attention-Residuals)

---

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 17 • 💬 0 • ⭐ 36,452 • 13mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 32 • 💬 2 • ⭐ 30,368 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

**[MiroThinker: Pushing the Performance Boundaries of Open-Source Research Agents via Model, Context, and Interactive Scaling](https://huggingface.co/papers/2511.11793)**

*MiroMind Team, Song Bai, Lidong Bing et al. (54 authors)*

We present MiroThinker v1.0, an open-source research agent designed to advance tool-augmented reasoning and information-seeking capabilities. Unlike previous agents that only scale up model size or context length, MiroThinker explores interaction scaling at the model level, systematically training the model to handle deeper and more frequent agent-environment interactions as a third dimension of performance improvement. Unlike LLM test-time scaling, which operates in isolation and risks degradation with longer reasoning chains, interactive scaling leverages environment feedback and external information acquisition to correct errors and refine trajectories. Through reinforcement learning, the model achieves efficient interaction scaling: with a 256K context window, it can perform up to 600 tool calls per task, enabling sustained multi-turn reasoning and complex real-world research workflows. Across four representative benchmarks-GAIA, HLE, BrowseComp, and BrowseComp-ZH-the 72B variant achieves up to 81.9%, 37.7%, 47.1%, and 55.6% accuracy respectively, surpassing previous open-source agents and approaching commercial counterparts such as GPT-5-high. Our analysis reveals that MiroThinker benefits from interactive scaling consistently: research performance improves predictably as the model engages in deeper and more frequent agent-environment interactions, demonstrating that interaction depth exhibits scaling behaviors analogous to model size and context length. These findings establish interaction scaling as a third critical dimension for building next-generation open research agents, complementing model capacity and context windows.

▲ 194 • 💬 5 • ⭐ 8,016 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.11793) • [💻 code](https://github.com/MiroMindAI/MiroThinker) • [🔗 project](https://dr.miromind.ai/)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 58 • 💬 4 • ⭐ 18,873 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

**[Very Large-Scale Multi-Agent Simulation in AgentScope](https://huggingface.co/papers/2407.17789)**

*Xuchen Pan, Dawei Gao, Yuexiang Xie et al. (8 authors)*

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.

▲ 39 • 💬 2 • ⭐ 18,911 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.17789) • [💻 code](https://github.com/modelscope/agentscope)

---

**[EvoScientist: Towards Multi-Agent Evolving AI Scientists for End-to-End Scientific Discovery](https://huggingface.co/papers/2603.08127)**

*Yougang Lyu, Xi Zhang, Xinhao Yi et al. (12 authors)*

EvoScientist is an adaptive multi-agent framework that enhances scientific discovery by continuously learning from past interactions through persistent memory modules.

▲ 15 • 💬 5 • ⭐ 1,690 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2603.08127) • [💻 code](https://github.com/EvoScientist/EvoScientist)

---

---

## GitHub Repositories: "ai"

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**

AI agents running research on single-GPU nanochat training automatically

`Python`

⭐ 53.5k • 🔱 7.4k • 3d ago

---

**[googleworkspace/cli](https://github.com/googleworkspace/cli)**

Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.

`Rust` `agent-skills` `ai-agent` `automation` `cli` `discovery-api`

⭐ 22.3k • 🔱 1.1k • 17h ago

---

**[agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw)**

Your Personal AI Assistant; easy to install, deploy on your own machine or on the cloud; supports multiple chat apps with easily extensible capabilities.

`Python`

⭐ 13.1k • 🔱 1.7k • 1h ago

---

**[cft0808/edict](https://github.com/cft0808/edict)**

🏛️ 三省六部制 · OpenClaw Multi-Agent Orchestration System — 9 specialized AI agents with real-time dashboard, model config, and full audit trails

`Python` `ai-agents` `ai-orchestration` `autonomous-agents` `claude` `dashboard`

⭐ 12.5k • 🔱 1.2k • 6d ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`TypeScript` `agency` `agent` `pip` `pua`

⭐ 11.0k • 🔱 572 • 2h ago

---

**[Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)**

Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

`Python` `agent-infrastructure` `ai-agent` `ai-search` `automation` `bilibili`

⭐ 10.6k • 🔱 773 • 1d ago

---

**[calesthio/Crucix](https://github.com/calesthio/Crucix)**

Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

`JavaScript` `ai` `intelligence` `osint`

⭐ 6.5k • 🔱 994 • 2d ago

---

**[jackwener/opencli](https://github.com/jackwener/opencli)**

Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime. Transform any website, Electron app, or local binary into a standardized command-line interface. Built for AI Agents to discover, learn, and execute tools seamlessly via a unified AGENT.md integration.

`TypeScript` `ai-agent` `ai-agents` `ai-tools` `cli`

⭐ 6.0k • 🔱 482 • 1h ago

---

**[mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)**

734+ structured cybersecurity skills for AI agents · MITRE ATT&CK mapped · agentskills.io open standard · Works with Claude Code, GitHub Copilot, OpenAI Codex CLI, Cursor, Gemini CLI & 20+ platforms · Penetration testing, DFIR, threat intel, cloud security & more · Apache 2.0

`Python` `ai-agents` `claude` `claude-code` `cloud-security` `cybersecurity`

⭐ 3.7k • 🔱 368 • 20h ago

---

**[NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell)**

OpenShell is the safe, private runtime for autonomous AI agents.

`Rust`

⭐ 3.5k • 🔱 351 • 4h ago

---

---

*Generated by PeekDeck - A glance is all you need*
