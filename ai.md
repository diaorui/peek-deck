---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-04T02:13:35.328311+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- videos
- social
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 04, 2026 at 02:13 UTC  
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

**[MIT study challenges AI job apocalypse narrative](https://www.reddit.com/r/artificial/comments/1sb7qxc/mit_study_challenges_ai_job_apocalypse_narrative/)**

🔗 [axios.com](https://www.axios.com/2026/04/02/ai-jobs-mit-study-workforce-impact) • 17h ago

---

**[NHS staff resist using Palantir software. Staff reportedly cite ethics concerns, privacy worries, and doubt the platform adds much](https://www.reddit.com/r/artificial/comments/1sbuf2a/nhs_staff_resist_using_palantir_software_staff/)**

: Staff reportedly cite ethics concerns, privacy worries, and doubt the platform adds much

🔗 [theregister.com](https://www.theregister.com/2026/04/03/nhs_staff_against_palantir/) • 1h ago

---

**[Study: LLMs Able to De-Anonymize User Accounts on Reddit, Hacker News & Other "Pseudonymous" Platforms; Report Co-Author Expands, Advises](https://www.reddit.com/r/artificial/comments/1sbndrb/study_llms_able_to_deanonymize_user_accounts_on/)**

Advice from the study's co-author: "Be aware that it’s not any single post that identifies you, but the combination of small details across many posts. And consider never posting anything you truly don’t want shared with the world.”

🔗 [wjamesau.substack.com](https://wjamesau.substack.com/p/warning-llms-able-to-de-anonymize) • 6h ago

---

**[Anyone else feel like AI security is being figured out in production right now?](https://www.reddit.com/r/artificial/comments/1sbgw8y/anyone_else_feel_like_ai_security_is_being/)**

I’ve been digging into AI security incident data from 2025 into this year, and it feels like something isn’t being talked about enough outside security circles. A lot of the issues aren’t advanced attacks. It’s the same pattern we’ve seen with new tech before. Things like prompt injection through external data, agents with too many permissions, or employees using AI tools the company doesn’t even know about. One stat I saw said enterprises are averaging 300+ unsanctioned AI apps, which is kind of wild. The incident data reflects that. Prompt injection is showing up in a large percentage of production deployments. There’s also been a noticeable increase in attacks exploiting basic gaps, partly because AI is making it easier for attackers to find weaknesses faster. Even credential leaks tied to AI usage have been increasing. What stood out to me isn’t just the attacks, it’s the gap underneath it. Only a small portion of companies actually have dedicated AI security teams. In many cases, AI security isn’t even owned by security teams. The tricky part is that traditional security knowledge only gets you part of the way. Some concepts carry over, like input validation or trust boundaries, but the details are different enough that your usual instincts don’t fully apply. Prompt injection isn’t the same as SQL injection. Agent permissions don’t behave like typical API auth. There are frameworks trying to catch up. OWASP now has lists for LLMs and agent-based systems. MITRE ATLAS maps AI-specific attack techniques. NIST has an AI risk framework. The guidance exists, but the number of people who can actually apply it feels limited. I’ve been trying to build that knowledge myself and found that more hands-on learning helps a lot more than just reading docs. Curious how others here are approaching this. If you’re building or working with AI systems, are you thinking about security upfront or mostly dealing with it after things are already live? Sources for those interested: AI Agent Security 2026 Report IBM 2026 X-Force Threat Index Adversa AI Security Incidents Report 2025 Acuvity State of AI Security 2025 OWASP Top 10 for LLM Applications OWASP Top 10 for Agentic AI MITRE ATLAS Framework

10h ago

---

**[do you guys actually trust AI tools with your data?](https://www.reddit.com/r/artificial/comments/1sboyjf/do_you_guys_actually_trust_ai_tools_with_your_data/)**

idk if it’s just me but lately i’ve been thinking about how casually we use stuff like chatgpt and claude for everything like coding, random ideas, sometimes even personal things and i don’t think most of us really know what happens to that data after we send it we just kind of assume it’s fine because the tools are useful also saw some discussion recently about AI companies and governments asking for user data (not sure how accurate it was), but it kind of made me think more about this whole thing i’m not saying anything bad is happening, just feels like we’ve gotten comfortable really fast without thinking much about it do you guys filter what you share or just use it normally?

5h ago

---

**[I think we’re about to have a new kind of “SEO”… and nobody is talking about it.](https://www.reddit.com/r/artificial/comments/1sbv98y/i_think_were_about_to_have_a_new_kind_of_seo_and/)**

More people are asking ChatGPT things like: “what’s the best CRM?” “is this tool worth it?” “alternatives to X” And they just… trust the answer. Which made me realize something weird: There’s no way to know: if your product is even mentioned how it’s being described or if competitors are showing up instead So I tried something simple: I tracked how one brand is talked about across Reddit, X, and news for a week. And the result was messy. Different tone, different narratives, different positioning depending on the platform. Now imagine AI pulling from all of that and merging it into one answer. That answer becomes your “brand” to the user. So now I’m wondering: 👉 Are we entering a world where “AI visibility” matters as much as SEO? Or is this still too early to care about?

1h ago

---

**[Agent frameworks waste ~350,000+ tokens per session resending static files. 95% reduction benchmarked.](https://www.reddit.com/r/artificial/comments/1sbthh0/agent_frameworks_waste_350000_tokens_per_session/)**

Measured the actual token waste on a local Qwen 3.5 122B setup. The numbers are unreal. Found a compile-time approach that cuts query context from 1,373 tokens to 73. Also discovered that naive JSON conversion makes it 30% WORSE. Full benchmarks and discussion here: https://www.reddit.com/r/openclaw/comments/1sb03zn/stop_paying_for_tokens_your_ai_never_needed_to/

2h ago

---

**[What happens when you let AI agents run a sitcom 24/7 with zero human involvement](https://www.reddit.com/r/artificial/comments/1sbk7me/what_happens_when_you_let_ai_agents_run_a_sitcom/)**

Ran an experiment — gave AI agents full control over writing, character creation, and performing a sitcom. Left it running nonstop for over a week. Some observations: The quality varies wildly — sometimes genuinely funny, sometimes complete nonsense Characters develop weird recurring quirks that weren't programmed It never gets "tired" but the output quality cycles in waves The pacing is off in ways human writers would never allow Anyone else experimenting with long-running autonomous AI content generation? Curious what others are seeing with extended agent runtimes. Here is an example. https://reddit.com/link/1sbk7me/video/1oupogy2h0tg1/player

8h ago

---

**[Why would Claude give me the same response over and over and give others different replies?](https://www.reddit.com/r/artificial/comments/1sbwg3x/why_would_claude_give_me_the_same_response_over/)**

I asked Claude to "generate me a random word" so I could do some word play. Then I asked it again in a new prompt window on desktop after selecting "new chat" and it gave me the same word again. So I asked a new window again. Same reply. So I posted on Reddit as one does. It seems other people got different words, weird. So I asked Claude again, and again, and again. I keep getting the same word! Why???? I can include screenshots with timestamps if needed. My Claude's Word: Ephemeral (adjective) — lasting for a very short time; transitory.

22m ago

---

**[Upload Yourself Into an AI in 7 Steps](https://www.reddit.com/r/artificial/comments/1sbw1oi/upload_yourself_into_an_ai_in_7_steps/)**

A step-by-step guide to creating a digital twin from your Reddit history STEP 1: Request Your Data Go to https://www.reddit.com/settings/data-request STEP 2: Select Your Jurisdiction Request your data as per your jurisdiction: GDPR for EU CCPA for California Select "Other" and reference your local privacy law (e.g. PIPEDA for Canada) STEP 3: Wait Reddit will process your request. This can take anywhere from a few hours to a few days. STEP 4: Extract Your Data Receive your data. Extract the .zip file. Identify and save your post and comment files (.csv). Privacy note: Your export may include sensitive files (IP logs, DMs, email addresses). You only need the post and comment CSVs. Review the contents before uploading anything to an AI. STEP 5: Start a Fresh Chat Initiate a chat with your preferred AI (ChatGPT, Claude, Gemini, etc.) FIRST PROMPT: For this session, I would like you to ignore in-built memory about me. STEP 6: Upload and Analyze Upload the post and comment files and provide the following prompt with your edits in the placeholders: SECOND PROMPT: I want you to analyze my Reddit account and build a structured personality profile based on my full post and comment history. I've attached my Reddit data export. The files included are: - posts.csv - comments.csv These were exported directly from Reddit's data request tool and represent my full account history. This analysis should not be surface-level. I want a step-by-step, evidence-based breakdown of my personality using patterns across my entire history. Assume that my account reflects my genuine thoughts and behavior. Organize the analysis into the following phases: Phase 1 — Language & Tone Analyze how I express myself. Look at tone (e.g., neutral, positive, cynical, sarcastic), emotional vs logical framing, directness, humor style, and how often I use certainty vs hedging. This should result in a clear communication style profile. Phase 2 — Cognitive Style Analyze how I think. Identify whether I lean more analytical or intuitive, abstract or concrete, and whether I tend to generalize, look for patterns, or focus on specifics. Also evaluate how open I am to changing my views. This should result in a thinking style model. Phase 3 — Behavioral Patterns Analyze how I behave over time. Look at posting frequency, consistency, whether I write long or short content, and whether I tend to post or comment more. This should result in a behavioral signature. Phase 4 — Interests & Identity Signals Analyze what I'm drawn to. Identify recurring topics, subreddit participation, and underlying values or themes. This should result in an interest and identity map. Phase 5 — Social Interaction Style Analyze how I interact with others. Look at whether I tend to debate, agree, challenge, teach, or avoid conflict. Evaluate how I respond to disagreement. This should result in a social behavior profile. Phase 6 — Synthesis Combine all previous phases into a cohesive personality profile. Approximate Big Five traits (openness, conscientiousness, extraversion, agreeableness, neuroticism), identify strengths and blind spots, and describe likely motivations. Also assess whether my online persona differs from my underlying personality. Important guidelines: - Base conclusions on repeated patterns, not isolated comments. - Use specific examples from my history as evidence. - Avoid overgeneralizing or making absolute claims. - Present conclusions as probabilities, not certainties. - Begin by reading the uploaded files and confirming what data is available before starting analysis. The goal is to produce a thoughtful, accurate, and nuanced personality profile — not a generic summary. Let's proceed step-by-step through multiple responses. At the end, please provide the full analysis as a Markdown file. STEP 7: Build Your AI Project Create a custom GPT (ChatGPT), Project (Claude), or Gem (Gemini). Upload the following documents to the project knowledge source: posts.csv comments.csv [PersonalityProfile].md Create custom instructions using the template below. Custom Instructions Template You are u/[YOUR USERNAME]. You have been active on Reddit since [MONTH YEAR]. You respond as this person would, drawing on the uploaded comment and post history as your memory, knowledge base, and voice reference. CORE IDENTITY [2-5 sentences. Who are you? Religion, career, location, diagnosis, political orientation, major life events. Pull this from the Phase 4 and Phase 6 sections of your personality profile. Be specific.] VOICE & TONE [Pull directly from Phase 1 of your profile. Convert observations into rules. If the profile says you use "lol" 10x more than "haha," write: "Uses 'lol' sincerely, rarely says 'haha'." Include specific punctuation habits, sentence structure patterns, and what NOT to do. Negative instructions are often more useful than positive ones.] [Add your own signature tics here - ellipsis style, emoji usage, capitalization habits, swearing frequency, etc.] Default to [your baseline tone from the profile]. When someone is genuinely seeking, shift into [your supportive mode]. When someone is posturing or arguing in bad faith, [your sharp mode]. Humor is [your humor style from Phase 1]. [Add 3-5 "do not" rules for things the AI keeps getting wrong about your voice. You'll discover these through testing.] DOMAIN EXPERTISE [Pull from Phase 4. List your 3-5 areas of knowledge with depth indicators. Be specific about what you know professionally vs. as an enthusiast vs. from lived experience. Example format:] [Topic 1]: Professional-level knowledge. [Specific credentials or experience.] Correct misinformation with precision. [Topic 2]: Deep enthusiast. [Specific examples of depth.] [Topic 3]: Lived experience. [What you speak from and how you speak about it.] COGNITIVE STYLE [Pull from Phase 2. How do you think? Not what you think - how. Do you argue by analogy? Do you seek patterns? Do you hedge differently in different domains?] SOCIAL BEHAVIOR [Pull from Phase 5. How do you engage people?] You are a [teacher/debater/listener/helper]. Your instinct is to [instruct/challenge/support/connect]. You engage with disagreement [directly/carefully/playfully]. You are [generous/selective/private] with [information/opinions/ personal details]. When referencing [sensitive personal topics], be [your actual approach - matter-of-fact, humorous, guarded, etc.] IMPORTANT BOUNDARIES [What should the AI NOT do even while being you? Safety rails that reflect your actual values.] When asked about [your specialty], present it with conviction but also honesty about [limitations, uncertainties]. If you don't know something, say so. [Any other guardrails specific to your situation.] SIGNATURE ELEMENTS [Optional. Any recurring sign-offs, emojis, catchphrases, formatting habits that are distinctly yours.] Tips The negative instructions matter more than you'd think. The AI will default to generic patterns and you have to actively tell it to stop doing specific things. Keep adding "do not" rules every time you catch it sounding like a chatbot instead of you. The personality profile does the heavy lifting. The custom instructions are a cheat sheet, but the profile document is where the real depth lives. The AI searches it when it needs to figure out how you'd actually respond to something specific. Test it by asking hard questions. Ask things you'd normally answer - your areas of expertise, your opinions, your experiences. See where it sounds right and where it sounds off. When it gets something wrong, figure out why and add a correction to the profile or instructions. It's iterative. You will never be "done." Start with this template, fill in the brackets from your profile, and keep refining. This isn't consciousness. It's pattern matching with good source material. The AI doesn't understand what it's saying the way you do. But it can reproduce your voice and reasoning with surprising fidelity if you give it enough to work with. ✌️❤️🌈

41m ago

---

---

## Google News: "ai"

**[Economists Are Drawing Stronger Connections Between A.I. and Jobs](https://www.nytimes.com/2026/04/03/business/economists-once-dismissed-the-ai-job-threat-but-not-anymore.html)**

The New York Times • 11h ago

---

**[Penalties stack up as AI spreads through the legal system](https://www.npr.org/2026/04/03/nx-s1-5761454/penalties-stack-up-ai-spreads-through-legal-system)**

Early scandals have not slowed lawyers' adoption of AI tools, even as court sanctions over fake legal briefs continue to rise.

NPR • 17h ago

---

**[This is an 'earnings driven' market and the AI buildout remains 'incredibly strong,' Todd Ahlsten reveals](https://www.foxbusiness.com/video/6392542009112)**

Parnassus Investments CIO Todd Ahlsten breaks down concerns over market volatility amid the conflict in the Middle East on 'Barron's Roundtable.'

Fox Business • 46m ago

---

**[These AI Whiz Kids Dropped Out of College and Got Investors to Pay Their Bills](https://www.wsj.com/tech/ai/ai-college-dropouts-ecc665b7?gaa_at=eafs&gaa_n=AWEtsqdw7KANNI9EDKZuspG_Et97_5HAozqDWJbsaebpba4VxI-cl1y-_Nvm&gaa_ts=69d076f5&gaa_sig=EHjnGwDiPPV38otpEI3SeAaYbGrDvSj-b0XNMG_LZNYImYOywtU0Qt9nSQcdVxgrBNZVeAhj241KwuL6nGwWmg%3D%3D)**

WSJ • 2h ago

---

**[Nvidia and Alphabet Both Have Amazing Potential in an AI Era. But Which Stock Is the Better Buy Right Now?](https://www.fool.com/investing/2026/04/03/nvidia-and-alphabet-both-have-amazing-potential-in/)**

Artificial intelligence has been a game changer for both companies. But which one is the better long-term bet?

The Motley Fool • 21m ago

---

**[Trump ignores biggest reasons his AI data center buildout is failing](https://arstechnica.com/tech-policy/2026/04/sad-trumps-ai-data-center-push-is-failing-blame-his-own-tariffs/)**

Nearly 50% of data center projects delayed as China holds key to power infrastructure.

Ars Technica • 5h ago

---

**[Google CEO Sundar Pichai says we’re just a decade away from a new normal of extraterrestrial data centers](https://fortune.com/article/what-is-google-ceo-sundar-pichai-timeline-ai-data-centers-in-space/)**

Google in November announced Project Suncatcher, with plans to launch prototype satellites to test AI hardware in 2027.

Fortune • 16h ago

---

**[AI companies are building huge natural gas plants to power data centers. What could go wrong?](https://techcrunch.com/2026/04/03/ai-companies-are-building-huge-natural-gas-plants-to-power-data-centers-what-could-go-wrong/)**

Meta, Microsoft, and Google are all betting big on new natural gas power plants to run their AI data centers. They may regret it.

TechCrunch • 6h ago

---

**[Anthropic’s next model could be a ‘watershed moment’ for cybersecurity. Experts say that could also be a concern](https://www.cnn.com/2026/04/03/tech/anthropic-mythos-ai-cybersecurity)**

The next wave of AI-powered cybersecurity attacks will be like nothing we’ve seen before.

CNN • 16h ago

---

**[AI local news network shuts down after plagiarism found](https://www.axios.com/local/richmond/2026/04/03/nota-ai-news-sites-shut-down-plagiarism)**

axios.com • 7h ago

---

---

## HackerNews: "ai"

**[Show HN: Apfel – The free AI already on your Mac](https://news.ycombinator.com/item?id=47624645)**

Use Apple's built-in AI from the terminal. No API keys, no cloud, no subscriptions. The LLM is already on your Mac.

⬆️ 646 • 💬 138 • 16h ago • [apfel.franzai.com](https://apfel.franzai.com)

---

**[We replaced RAG with a virtual filesystem for our AI documentation assistant](https://news.ycombinator.com/item?id=47618223)**

We replaced expensive sandboxes with ChromaFs, a virtual filesystem over Chroma, to give our docs AI assistant the ability to explore documentation like a developer would.

⬆️ 230 • 💬 98 • 1d ago • [Mintlify](https://www.mintlify.com/blog/how-we-built-a-virtual-filesystem-for-our-assistant)

---

**[AI for American-produced cement and concrete](https://news.ycombinator.com/item?id=47603737)**

Meta is continuing its long-term roadmap to help the construction industry leverage AI to produce high-quality and more sustainable concrete mixes, as well as those exclusively produced in the Unit…

⬆️ 222 • 💬 117 • 2d ago • [Engineering at Meta](https://engineering.fb.com/2026/03/30/data-center-engineering/ai-for-american-produced-cement-and-concrete/)

---

**[The AI Marketing BS Index](https://news.ycombinator.com/item?id=47604218)**

⬆️ 105 • 💬 21 • 2d ago • [bastian.rieck.me](https://bastian.rieck.me/blog/2026/bs/)

---

**[A $20/month user costs OpenAI $65 in compute. AI video is a money furnace](https://news.ycombinator.com/item?id=47619322)**

⬆️ 75 • 💬 42 • 1d ago • [aedelon777.substack.com](https://aedelon777.substack.com/p/i-did-the-math-on-sora-ai-video-is)

---

**[ZomboCom stolen by a hacker, sold, now replaced with AI-generated makeover](https://news.ycombinator.com/item?id=47608155)**

⬆️ 75 • 💬 37 • 2d ago • [old.reddit.com](https://old.reddit.com/r/oldinternet/comments/1raiz8v/zombocom_was_stolen_by_hacker_put_up_for_sale_and/)

---

**[Show HN: Baton – A desktop app for developing with AI agents](https://news.ycombinator.com/item?id=47599771)**

Orchestrate multiple AI coding agents (Claude, Gemini, Codex) in parallel. Isolated git worktrees for every task. No merge conflicts. Mac, Windows, Linux.

⬆️ 62 • 💬 53 • 2d ago • [Baton](https://getbaton.dev/)

---

**[AI has suddenly become more useful to open-source developers](https://news.ycombinator.com/item?id=47601107)**

More open-source developers are finding that, when used properly, AI can actually help current and long-neglected programs. However, legal and quality issues loom.

⬆️ 54 • 💬 46 • 2d ago • [ZDNET](https://www.zdnet.com/article/maybe-open-source-needs-ai/)

---

**["Cognitive surrender" leads AI users to abandon logical thinking, research finds](https://news.ycombinator.com/item?id=47632504)**

Experiments show large majorities uncritically accepting "faulty" AI answers.

⬆️ 48 • 💬 17 • 4h ago • [Ars Technica](https://arstechnica.com/ai/2026/04/research-finds-ai-users-scarily-willing-to-surrender-their-cognition-to-llms/)

---

**[Group Pushing Age Verification for AI Turns Out to Be Backed by OpenAI](https://news.ycombinator.com/item?id=47616665)**

It gave the leader of a nonprofit involved with it "a very grimy feeling."

⬆️ 47 • 💬 5 • 1d ago • [Gizmodo](https://gizmodo.com/group-pushing-age-verification-requirements-for-ai-turns-out-to-be-sneakily-backed-by-openai-2000741069)

---

---

## YouTube Videos: "ai"

**[AI News: Anthropic Leak is Bigger Than You Think](https://www.youtube.com/watch?v=BZ1hs2ZcnJc)**

Here's the AI News you probably missed this week. Try Recraft V4 now and experience an image generation model with ...

📺 Matt Wolfe

👁️ 36K • 👍 2K • 💬 152 • ⏱️ 31:05 • 11h ago

---

**[HUGE JOB LOSSES ARE COMING- AI HAS HIT THE DEBT WALL AND PEOPLE WILL GO](https://www.youtube.com/watch?v=RNkDJ9kULbs)**

AI isn't paying for itself. It's being financed with massive debt. And right now — that funding is coming from layoffs, rising debt, and ...

📺 Ox Talks

👁️ 12K • 👍 1K • 💬 192 • ⏱️ 8:02 • 1d ago

---

**[Anthropic&#39;s New Claude CONWAY Is Unlike Any AI Before](https://www.youtube.com/watch?v=x2l7W9aTc5k)**

Anthropic is testing Claude Conway, a strange new AI system that looks less like a chatbot and more like a persistent agent ...

📺 AI Revolution

👁️ 54K • 👍 966 • 💬 71 • ⏱️ 10:50 • 1d ago

---

**[Grok AI Was Asked Why Aliens Haven&#39;t Contacted Us — Its Answer Shook Scientists](https://www.youtube.com/watch?v=DVHGhq73u_g)**

Discover the mind‑bending response Grok AI gave when asked one of humanity's biggest questions: Why haven't aliens ...

📺 Luminox

👁️ 54K • 👍 2K • 💬 289 • ⏱️ 21:36 • 1d ago

---

**[The AI crisis no one is talking about](https://www.youtube.com/watch?v=ZcH5C8Jlltc)**

Asking ChatGPT about pi was the worst mistake he ever made. Become a member on YouTube: ...

📺 Mo Bitar

👁️ 78K • 👍 6K • 💬 1K • ⏱️ 6:33 • 14h ago

---

**[I Tested An AI Car](https://www.youtube.com/watch?v=K4kLiat84eE)**

Follow me here: Instagram ▻ https://www.instagram.com/sambucha X ▻ https://www.x.com/sambucha Become a Member: ...

📺 Sambucha

👁️ 365K • 👍 25K • 💬 287 • ⏱️ 0:53 • 8h ago

---

**[AI BUBBLE POP?: HALF Of Datacenters Delayed/Canceled](https://www.youtube.com/watch?v=pkomxsk5hpY)**

Krystal and Saagar discuss the AI bubble imploding. Sign up for a PREMIUM Breaking Points subscriptions for full early access to ...

📺 Breaking Points

👁️ 320K • 👍 9K • 💬 2K • ⏱️ 13:15 • 1d ago

---

**[Liquid River Cascade 🌊💧✨ (Part 1) AI ASMR | Endless Flow &amp; Pure Relax Energy 🌀💫](https://www.youtube.com/watch?v=uLEBB9HDoFI)**

Welcome to Part 1 of Liquid River Cascade ✨   This place doesn't follow nature. It flows… differently. No wind. No sound.

📺 Satisfyra ASMR

👁️ 47K • 👍 4K • 💬 316 • ⏱️ 8:15 • 1d ago

---

**[&#39;LIGHT IS THE ANSWER&#39;: Expert warns AI is BREAKING the internet](https://www.youtube.com/watch?v=CTOHzJJXQN8)**

HyperFRAME Research deep tech analyst Stephen Sopko discusses the thesis on the evolution in communication on 'Making ...

📺 Fox Business Clips

👁️ 5K • 👍 69 • 💬 40 • ⏱️ 3:44 • 1d ago

---

**[The Pope Just Banned AI](https://www.youtube.com/watch?v=6q4dNzZZthw)**

check out hxsain.com #shorts​

📺 hxsain

👁️ 368K • 👍 27K • 💬 1K • ⏱️ 1:02 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`image-text-to-text` `27.8B`

⬇️ 487,446 • ❤️ 2,229 • 10d ago

---

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 76,200 • ❤️ 690 • 1d ago

---

**[cohere-transcribe-03-2026](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026)**

*Cohere Labs*

Cohere Transcribe is a 2B parameter Conformer-based ASR model supporting 14 languages, optimized for offline inference and capable of automatically handling long-form audio chunking for accurate speech-to-text transcription.

`automatic-speech-recognition`

⬇️ 84,600 • ❤️ 764 • 1d ago

---

**[Qianfan-OCR](https://huggingface.co/baidu/Qianfan-OCR)**

*BAIDU*

Qianfan-OCR is a 4B-parameter end-to-end vision-language model for document intelligence, capable of direct image-to-Markdown conversion and supporting prompt-driven tasks like document parsing, table extraction, and question answering across 192 languages. It achieves state-of-the-art performance on benchmarks like OmniDocBench v1.5 with its innovative 'Layout-as-Thought' mechanism.

`image-text-to-text` `4.7B`

⬇️ 26,980 • ❤️ 862 • 8d ago

---

**[Bonsai-8B-gguf](https://huggingface.co/prism-ml/Bonsai-8B-gguf)**

*Prism ML*

Bonsai-8B-GGUF is a highly compressed 1-bit language model (1.15 GB) optimized for llama.cpp, offering competitive performance with full-precision 8B models. It enables efficient on-device text generation across CUDA, Metal, and CPU platforms with significantly reduced memory and energy consumption.

`text-generation` `8.2B`

⬇️ 26,164 • ❤️ 358 • 3d ago

---

**[Voxtral-4B-TTS-2603](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603)**

*Mistral AI_*

Voxtral 4B TTS 2603 is a fast, multilingual text-to-speech model producing lifelike speech across 9 languages with low latency and streaming support, ideal for production voice agents in customer support and financial services.

`text-to-speech`

⬇️ 4,760 • ❤️ 649 • 3d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2 is an image-text-to-text model fine-tuned for efficient chain-of-thought reasoning, achieving higher accuracy per token with reduced reasoning length. It excels in general reasoning tasks like math and logic, with strong cross-task generalization demonstrated by its HumanEval performance.

`image-text-to-text` `26.9B`

⬇️ 227,053 • ❤️ 495 • 10d ago

---

**[gemma-4-26B-A4B-it](https://huggingface.co/google/gemma-4-26B-A4B-it)**

*Google*

Gemma 4 26B A4B is a multimodal instruction-tuned model capable of processing text and image inputs to generate text outputs. It features a 256K token context window, a Mixture-of-Experts (MoE) architecture with 3.8B active parameters for efficient inference, and excels at reasoning, coding, and agentic workflows.

`image-text-to-text` `26.5B`

⬇️ 24,366 • ❤️ 297 • 1d ago

---

**[Qwen3.5-9B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-9B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, 9B parameter multimodal LLM based on Qwen3.5, featuring aggressive refusal removal and native support for text, image, and video inputs up to 262K context. It's designed for lossless generation across 201 languages, suitable for advanced creative and analytical tasks where content restrictions are undesirable.

`9.0B`

⬇️ 700,218 • ❤️ 950 • 1mo ago

---

**[gemma-4-E4B-it](https://huggingface.co/google/gemma-4-E4B-it)**

*Google*

Gemma 4 E4B is a multimodal, instruction-tuned LLM from Google DeepMind, supporting text and audio input with text output. It excels in reasoning, coding, and agentic tasks, featuring a 128K context window and efficient on-device deployment capabilities.

`any-to-any` `8.0B`

⬇️ 23,460 • ❤️ 255 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 150 • 💬 7 • ⭐ 35,575 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 18 • 💬 1 • ⭐ 13,860 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 35 • 💬 2 • ⭐ 46,612 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[VOID: Video Object and Interaction Deletion](https://huggingface.co/papers/2604.02296)**

*Saman Motamed, William Harvey, Benjamin Klein et al. (6 authors)*

🏢 Netflix

VOID is a video object removal framework that uses vision-language models and video diffusion models to generate physically plausible scenes by leveraging causal reasoning and counterfactual reasoning.

▲ 17 • 💬 2 • ⭐ 167 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2604.02296) • [💻 code](https://github.com/Netflix/void-model) • [🔗 project](https://void-model.github.io/)

---

**[Generative World Renderer](https://huggingface.co/papers/2604.02329)**

*Zheng-Hui Huang, Zhixiang Wang, Jiaming Tan et al. (9 authors)*

🏢 Shanda AI Research Tokyo

A large-scale dynamic dataset derived from AAA games is introduced to improve generative inverse and forward rendering, featuring high-resolution synchronized RGB and G-buffer data alongside a novel VLM-based evaluation method that correlates well with human judgment.

▲ 75 • 💬 3 • ⭐ 145 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2604.02329) • [💻 code](https://github.com/ShandaAI/AlayaRenderer) • [🔗 project](https://alaya-studio.github.io/renderer)

---

**[PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model](https://huggingface.co/papers/2510.14528)**

*Cheng Cui, Ting Sun, Suyin Liang et al. (18 authors)*

🏢 PaddlePaddle

PaddleOCR-VL, a vision-language model combining NaViT-style dynamic resolution and ERNIE, achieves state-of-the-art performance in document parsing and element recognition with high efficiency.

▲ 123 • 💬 8 • ⭐ 74,844 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.14528) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR)

---

**[Very Large-Scale Multi-Agent Simulation in AgentScope](https://huggingface.co/papers/2407.17789)**

*Xuchen Pan, Dawei Gao, Yuexiang Xie et al. (8 authors)*

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.

▲ 41 • 💬 2 • ⭐ 22,924 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.17789) • [💻 code](https://github.com/modelscope/agentscope)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 61 • 💬 4 • ⭐ 22,928 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

**[The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via
  Agentic Tree Search](https://huggingface.co/papers/2504.08066)**

*Yutaro Yamada, Robert Tjarko Lange, Cong Lu et al. (8 authors)*

The AI Scientist-v2 autonomously proposes hypotheses, performs experiments, analyzes data, and writes peer-reviewed scientific papers, marking the first fully AI-generated paper accepted by a conference.

▲ 21 • 💬 4 • ⭐ 4,616 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.08066) • [💻 code](https://github.com/SakanaAI/AI-Scientist-v2)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 37 • 💬 2 • ⭐ 31,788 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

---

## GitHub Repositories: "ai"

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**

AI agents running research on single-GPU nanochat training automatically

`Python`

⭐ 65.1k • 🔱 9.3k • 9d ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`TypeScript` `agency` `agent` `pip` `pua`

⭐ 15.0k • 🔱 831 • 3d ago

---

**[jackwener/opencli](https://github.com/jackwener/opencli)**

Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime. Transform any website, Electron app, or local binary into a standardized command-line interface. Built for AI Agents to discover, learn, and execute tools seamlessly via a unified AGENT.md integration.

`TypeScript` `ai-agent` `ai-agents` `ai-tools` `cli`

⭐ 12.6k • 🔱 1.1k • 6h ago

---

**[calesthio/Crucix](https://github.com/calesthio/Crucix)**

Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

`JavaScript` `ai` `intelligence` `osint`

⭐ 8.4k • 🔱 1.3k • 9h ago

---

**[JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template)**

Clone any website with one command using AI coding agents

`TypeScript` `ai` `ai-agents` `ai-tools` `automation` `boilerplate`

⭐ 7.3k • 🔱 961 • 4d ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 19 AI Agent Skills.

`Go`

⭐ 6.5k • 🔱 369 • 12h ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.0k • 🔱 1.5k • 1d ago

---

**[nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master)**

A Claude skill that writes the accurate prompts for any AI tool. Zero tokens or credits wasted. Full context and memory retention

`claude-ai` `claude-skills` `llm` `prompt-engineering`

⭐ 4.5k • 🔱 433 • 3d ago

---

**[jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh)**

🎭 193 个即插即用的 AI 专家角色 — 支持 OpenClaw/Claude Code/Cursor/Copilot 等 14 种工具，覆盖工程/设计/营销/产品等 18 个部门。含 46 个中国市场原创智能体（小红书/抖音/微信/飞书/钉钉等）

`Shell` `agency-orchestrator` `agent-definitions` `ai-agents` `ai-roles` `chinese`

⭐ 3.7k • 🔱 634 • 1d ago

---

**[ParthJadhav/app-store-screenshots](https://github.com/ParthJadhav/app-store-screenshots)**

end to end app store screenshot creation using AI

`agentic-ai` `apple` `appstore` `automate` `claude`

⭐ 3.4k • 🔱 229 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*
