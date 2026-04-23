---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-23T21:13:32.928329+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- repositories
- videos
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 23, 2026 at 21:13 UTC  
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

**[A Yale ethicist who has studied AI for 25 years says the real danger isn’t superintelligence. It’s the absence of moral intelligence.](https://www.reddit.com/r/artificial/comments/1stkefq/a_yale_ethicist_who_has_studied_ai_for_25_years/)**

I had the pleasure of sitting down with Wendell Wallach recently. He’s been working in AI ethics since before ChatGPT, before the hype, before most people in tech were paying attention. He wrote Moral Machines, worked alongside Stuart Russell, Yann LeCun and Daniel Kahneman. He’s not a commentator, he’s someone who has sat with these questions for decades. What struck me most in our conversation was his argument about AGI. Not that it’s impossible or inevitable, but that it’s the wrong goal entirely. A system can be extraordinarily intelligent and have zero moral reasoning. We’re building toward capability without asking what it’s capable of deciding. The section on accountability genuinely unsettled me. When AI causes harm, who is actually responsible? He maps out why the answer is almost always nobody in a way that’s hard to argue with. Worth watching if you’re tired of the extremes. Full interview: https://youtu.be/-usWHtI-cms?si=NBkwN-AmIshOXJsX

6h ago

---

**[Anthropic told a federal court it can't control its own model once deployed. That honest sentence changes the liability conversation.](https://www.reddit.com/r/artificial/comments/1sthpl8/anthropic_told_a_federal_court_it_cant_control/)**

In federal appeals court, Anthropic made a striking argument: once Claude is deployed on a customer's infrastructure (like the Pentagon's network), they cannot alter, update, or recall it. The Pentagon wants autonomous lethal action restrictions removed — and Anthropic says they have no mechanism to enforce those restrictions post-deployment. This is the first time a major AI lab has formally stated under oath that post-deployment control is effectively zero. The implications are bigger than most coverage suggests. The governance gap this reveals: Current AI governance assumes a control chain that doesn't actually exist: Model cards are pre-sale documents. They describe what the model was trained to do, not what it's capable of in the wild after fine-tuning, tool integration, and deployment context changes. Human-in-the-loop is a customer config, not a vendor guarantee. Anthropic can recommend oversight, but they just told a court they can't enforce it. Liability frameworks assume control that doesn't exist post-shipment. If you sell a car with a recall mechanism, you're liable for not using it. If you sell a model you can't recall, does that reduce your liability (you had no control) or increase your duty of disclosure before sale (you knew you'd have no control later)? The behavioral envelope question: If you can't recall the model, you need to disclose the maximum capability, not just the recommended use. Current model cards document aspirations. They don't document envelopes — what the model can actually produce under adversarial or edge conditions. This mirrors pharmaceutical regulation: if you can't pull a drug off shelves, the FDA requires much stronger pre-market evidence and broader contraindication labeling. The stricter the post-market control limitations, the higher the pre-market disclosure burden. Why this matters even if you don't care about military AI: The legal argument Anthropic is making applies everywhere. If "we can't control it after deployment" works for the Pentagon, it works for any enterprise customer. Every organization deploying Claude (or any model) is implicitly accepting residual risk that the vendor has explicitly said they cannot mitigate. The core question: if a vendor demonstrates in court that it truly cannot alter a deployed model, should that argument reduce its liability (it had no control) or increase its duty of disclosure before sale (it will have no control later)?

8h ago

---

**[Meta to Lay Off 10 Percent of Work Force in A.I. Push (Gift Article)](https://www.reddit.com/r/artificial/comments/1strw2k/meta_to_lay_off_10_percent_of_work_force_in_ai/)**

The layoffs affect about 8,000 employees, with Meta also planning to close 6,000 open roles, as the company focuses on artificial intelligence.

🔗 [nytimes.com](https://www.nytimes.com/2026/04/23/technology/meta-layoffs.html?unlocked_article_code=1.dFA.gzUD.VhYyqwKYrZpC&smid=nytcore-ios-share) • 2h ago

---

**[A federal judge ruled AI chats have no attorney-client privilege. A CEO's deleted ChatGPT conversations were recovered and used against him in court. On the same day, a different judge ruled the opposite.](https://www.reddit.com/r/artificial/comments/1st4y15/a_federal_judge_ruled_ai_chats_have_no/)**

A federal judge ruled that your AI conversations can be seized and used against you in court — and deleting them doesn't help. **The Heppner case (February 2026):** - Former CEO Bradley Heppner used Claude to prep his fraud defense - Judge Jed Rakoff ordered him to surrender 31 AI-generated documents - Ruling: no attorney-client privilege exists "or could exist" between a user and an AI platform **The Krafton case:** - A CEO used ChatGPT to plan how to avoid paying promised earnout payments - He deleted the conversations - The court recovered them anyway and reversed his decisions **The contradiction:** - Same day as Rakoff's ruling, a Michigan judge reached the opposite conclusion - Protected a woman's ChatGPT chats as personal "work product" - A Colorado court later sided with Michigan but added: you must disclose which AI tool you used **The fallout:** - 12+ major law firms have issued client AI warnings - Sher Tremonte added contract clauses that sharing privileged info with AI waives privilege - Both OpenAI and Anthropic privacy policies explicitly allow sharing user data with third parties - $145,000+ in sanctions against attorneys for AI citation errors in Q1 2026 alone **The bottom line:** - Your AI is not your lawyer and never was - Deleting chats doesn't delete the data from their servers - Consumer AI (ChatGPT, Claude, Gemini) should not be used for legal matters unless directed by counsel Full breakdown with source links → https://synvoya.com/blog/2026-04-23-ai-chats-court-evidence/ Have you ever typed something into ChatGPT that you wouldn't want a judge to read?

19h ago

---

**[AI might save my life and has let me do 8 things I would not have done otherwise](https://www.reddit.com/r/artificial/comments/1stny9s/ai_might_save_my_life_and_has_let_me_do_8_things/)**

Today I have done all these in about 5 hours analysed my blood test results for the last 20 years reviewed whole health action plan for review with doctor produced charts from that data which clearly shows direction of travel and reveals information hidden in the data wrote a mini screen saver thing which shows me the top AI art on Reddit built an entire marketing program for a book I am launching built a web page to support the program built a press release for the book got a list of all key contacts in local media and bookshops - with email addresses and frequently actual names. [EDIT, forgot this one] Made a Star Trek LCARS home page for the 50 odd regular links I use and hooked it into the database where I keep the list. Now, I could have done all that myself, but it would have taken a week. Crucially I *would not have bothered * I would not have seen the results as worth the effort. So, (a) I have been more productive (b) I have done stuff I never would have done without AI

4h ago

---

**[I gave an AI a CT Scan While It Listened to an Emotional Conversation [R]](https://www.reddit.com/r/artificial/comments/1stsn1e/i_gave_an_ai_a_ct_scan_while_it_listened_to_an/)**

I created an [Activation Lab](https://github.com/cstefanache/llmct) tool that can be seen as an MRI machine for AI. It captures snapshots of every single layer inside a language model while it processes a conversation. It allows you to fully understand what is happening, inside a neural network during generation by capturing all internal states of the layers of an LLM and takes snapshots for interpretability. First experiment: I fed Qwen 2.5 (3B) a 20-turn conversation where the user swings wildly between joy, fear, anger, sadness, apathy, and peace. At every turn, I scanned the AI's internal state and compared it against emotional fingerprints. Here's what I found: The AI has an emotional backbone. The residual stream - the main information highway, maintains 0.83–0.88 cosine similarity to emotional references at all times. It always knows the emotional temperature of the conversation. Emotions are sharpest at layers 29–33. Early layers detect that emotion exists. Middle layers sort positive from negative. But it's the deep layers where the network actually decides "this is joy, not sadness." Layer 31 is the single most discriminative layer in the entire network. The AI has a built-in shock absorber. When the user is emotionally intense, the assistant's internal state shifts toward that emotion, but never all the way. The gap is consistent: \~0.03 on the backbone, \~0.13 on the deeper processing centers. It acknowledges your feelings while staying calm. Nobody trained it to do this explicitly. It learned it. Joy is the default setting. Even during angry and sad turns, the joy reference scored highest. Instruction tuning didn't just make the model helpful, it shifted its entire internal geometry toward positivity. Emotional memory fades. First message: 0.90 cosine with its matching emotion. By message 19: only 0.67–0.73. Longer conversations dilute the signal.

1h ago

---

**[Can Claude’s “Skills” (custom SKILL.md instruction files) be exported and used in ChatGPT?](https://www.reddit.com/r/artificial/comments/1stphh6/can_claudes_skills_custom_skillmd_instruction/)**

Hey everyone, I’ve been using Claude.ai with a custom skill setup inside a Project. Basically I have a folder of Markdown files (SKILL.md files) that act as persistent instructions for Claude. Each skill has a name, a description, a trigger condition and detailed instructions on how Claude should behave when that trigger fires. Some of these skills reference each other and build on top of each other, so there’s a whole interconnected system running. My question is whether any of this is portable. What the skill files actually are: Each skill is essentially a plain Markdown file with a YAML frontmatter block (name, description) and then structured natural language instructions. No proprietary binary format, no compiled code. Just text. What I’m wondering: 1. Can I export or extract these SKILL.md files? (They live in a mounted read-only directory inside Claude’s environment, so I can view them but not directly download them through a normal UI button.) 2. If I copy the raw Markdown content, can I paste it into a ChatGPT Custom GPT as system prompt instructions or into the “Instructions” field and get comparable behavior? 3. Has anyone tried migrating a Claude Project skill system over to a GPT and hit any practical walls? I’m thinking about things like tool availability differences, how each model interprets structured instructions or differences in how context is injected. 4. Is the whole skill/trigger architecture something that’s genuinely Claude-specific because of how Anthropic injects context into the system prompt, or is it just prompt engineering that any capable model can follow? My hunch is that the Markdown content itself is fully portable since it’s just text, but the actual trigger routing (where Claude decides which SKILL.md to load based on keywords or slash commands) might need to be rebuilt manually in ChatGPT, either via a GPT system prompt that describes all triggers or by splitting everything into separate GPTs. Anyone done something like this or have thoughts on the approach?

3h ago

---

**[Introducing GPT-5.5](https://www.reddit.com/r/artificial/comments/1stvctj/introducing_gpt55/)**

Introducing GPT-5.5, our smartest model yet—faster, more capable, and built for complex tasks like coding, research, and data analysis across tools.

🔗 [OpenAI](https://openai.com/index/introducing-gpt-5-5/) • 10m ago

---

**[Gemini vs Grok: Playing Towers of Annoy](https://www.reddit.com/r/artificial/comments/1stp093/gemini_vs_grok_playing_towers_of_annoy/)**

LLMs were asked to write a Python 3.10 client that plays a two-player adversarial variant of the Towers of Hanoi. Rules: Hero moves a disk; Villain must immediately move that same disk to an adjacent tower (or pass if no legal move). Hero's budget is 2^m + 1 moves — barely more than the 2^m - 1 solo optimum, so almost any wasted move loses. Round-robin tournament with penalty-shootout matchups: up to 5 rounds (+ sudden death), 2 simultaneous games per round with hero/villain roles swapped. Round configs grow from 4 towers / 3 disks up to 12 towers / 7 disks. Full writeup

3h ago

---

**[Common GPT 5.5 pricing misconception.](https://www.reddit.com/r/artificial/comments/1stv81z/common_gpt_55_pricing_misconception/)**

Many people have pointed out that ChatGPT 5.5 appears to be twice as expensive as 5.4 based on API pricing, which makes it look pricier than Opus 4.7. But the comparison is not that simple. GPT 5.5 is significantly more token-efficient in practice, which can make it faster and reduce the total cost of completing a task. When you compare it directly to Opus 4.7, the image here shows that Claude Opus 4.7 is still much more expensive than GPT 5.5, around 5 to 10 times more expensive on ARC-AGI-2. Anthropic also changed the tokenizer for Opus 4.7, which appears to increase token counts by about 1.35x. Combined with Anthropic’s already high API pricing, this makes Claude substantially more expensive in real world usage than a simple headline price comparison suggests.

15m ago

---

---

## Google News: "ai"

**[A group of users leaked Anthropic's AI model Mythos by reportedly guessing where it was located](https://fortune.com/2026/04/23/anthropic-mythos-leak-dario-amodei-ceo-cybersecurity-hackers-exploits-ai/)**

Anthropic’s model was reportedly accessed by a handful of users in an online forum.

Fortune • 5h ago

---

**[Anthropic’s New Mythos A.I. Model Sets Off Global Alarms](https://www.nytimes.com/2026/04/22/technology/anthropics-mythos-ai.html)**

The New York Times • 1d ago

---

**[The Guardian view on Anthropic’s Claude Mythos: when AI finds every flaw, who controls the internet? | Editorial](https://www.theguardian.com/commentisfree/2026/apr/23/the-guardian-view-on-anthropics-claude-mythos-when-ai-finds-every-flaw-who-controls-the-internet)**

Editorial: Tech can scale cyber-attacks and defences alike, raising questions about private power, public risk and the future of a shared internet

The Guardian • 3h ago

---

**[Meta to cut 8,000 jobs, Microsoft offers buyouts to to staff as AI spending costs hit Big Tech workers](https://finance.yahoo.com/markets/article/meta-to-cut-8000-jobs-microsoft-offers-buyouts-to-to-staff-as-ai-spending-costs-hit-big-tech-workers-182722919.html)**

Meta and Microsoft are the latest Big Tech giants to trim staff as AI costs continue to balloon.

Yahoo Finance • 2h ago

---

**[Meta will cut 10% of workforce as company pushes deeper into AI](https://www.cnbc.com/2026/04/23/meta-will-cut-10percent-of-workforce-as-it-pushes-more-into-ai.html)**

Meta plans to lay off 10% of its workforce, equaling about 8,000 employees, as the company continues to ramp up investments in artificial intelligence.

CNBC • 3h ago

---

**[Meta plans to cut 10% of workforce, or 8,000 jobs, as it doubles down on AI](https://www.marketwatch.com/story/meta-plans-to-cut-10-of-workforce-or-8-000-jobs-as-it-doubles-down-on-ai-68dd6ebb)**

MarketWatch • 19m ago

---

**[Reese Witherspoon, Sandra Bullock and Hollywood’s cautious embrace of AI](https://www.nbcnews.com/pop-culture/pop-culture-news/reese-witherspoon-sandra-bullock-hollywood-artificial-intelligence-rcna341114)**

“Over the last six to 12 months, there has been this realization that AI is not going away,” said Alexandra Shannon, head of strategic development at Creative Artists Agency.

NBC News • 13m ago

---

**[Bret Taylor’s Sierra buys YC-backed AI startup Fragment](https://techcrunch.com/2026/04/23/bret-taylors-sierra-buys-yc-backed-ai-startup-fragment/)**

Sierra, the AI customer service agent startup founded by technologist Bret Taylor, announced today that it has acquired the YC-backed French startup Fragment.

TechCrunch • 13m ago

---

**[AI model designs new antibiotic for staph infections after exploring 46 billion compounds](https://phys.org/news/2026-04-ai-antibiotic-staph-infections-exploring.html)**

Phys.org • 13m ago

---

**[Texas Instruments' stock jumps 18%, heads for best day since 2000 as AI demand soars](https://www.cnbc.com/2026/04/23/texas-instruments-stock-soars-on-q1-earnings-as-ai-demand-jumps.html)**

Texas Instruments beat on earnings and revenue and gave upbeat guidance.

CNBC • 2h ago

---

---

## HackerNews: "ai"

**[Meta to start capturing employee mouse movements, keystrokes for AI training](https://news.ycombinator.com/item?id=47851948)**

⬆️ 789 • 💬 522 • 2d ago • [reuters.com](https://www.reuters.com/sustainability/boards-policy-regulation/meta-start-capturing-employee-mouse-movements-keystrokes-ai-training-data-2026-04-21/)

---

**[Tell HN: I'm sick of AI everything](https://news.ycombinator.com/item?id=47857461)**

⬆️ 335 • 💬 190 • 1d ago

---

**[Scoring Show HN submissions for AI design patterns](https://news.ycombinator.com/item?id=47864393)**

An attempt to detect AI design patterns in Show HN pages

⬆️ 325 • 💬 231 • 1d ago • [adriankrebs.ch](https://www.adriankrebs.ch/blog/design-slop/)

---

**[A Roblox cheat and one AI tool brought down Vercel's platform](https://news.ycombinator.com/item?id=47844431)**

⬆️ 283 • 💬 162 • 2d ago • [webmatrices.com](https://webmatrices.com/post/how-a-roblox-cheat-and-one-ai-tool-brought-down-vercel-s-entire-platform)

---

**[Show HN: GoModel – an open-source AI gateway in Go](https://news.ycombinator.com/item?id=47849097)**

High-performance AI gateway written in Go - unified OpenAI-compatible API for OpenAI, Anthropic, Gemini, Groq, xAI &amp; Ollama. LiteLLM alternative with observability, guardrails &amp; streaming. ...

⬆️ 205 • 💬 74 • 2d ago • [GitHub](https://github.com/ENTERPILOT/GOModel/)

---

**[Our newsroom AI policy](https://news.ycombinator.com/item?id=47872452)**

How Ars Technica uses, and doesn't use, generative AI.

⬆️ 179 • 💬 122 • 15h ago • [Ars Technica](https://arstechnica.com/staff/2026/04/our-newsroom-ai-policy/)

---

**[Less human AI agents, please](https://news.ycombinator.com/item?id=47845429)**

Nial – Knowledge work and artificial intelligence.

⬆️ 158 • 💬 168 • 2d ago • [nial.se](https://nial.se/blog/less-human-ai-agents-please/)

---

**[Meta employees are up in arms over a mandatory program to train AI on their](https://news.ycombinator.com/item?id=47860961)**

Meta deploys keystroke-tracking software on US employees' computers, sparking privacy concerns and internal backlash.

⬆️ 115 • 💬 89 • 1d ago • [Business Insider](https://www.businessinsider.com/meta-new-ai-tool-tracks-staff-activity-sparks-concern-2026-4)

---

**[Top MAGA influencer revealed to be AI](https://news.ycombinator.com/item?id=47864808)**

According to her profile, she was a registered nurse with Jennifer Lawrence looks who offered red meat posts to lonely conservative men online.

⬆️ 96 • 💬 53 • 1d ago • [New York Post](https://nypost.com/2026/04/21/us-news/top-maga-influencer-emily-hart-revealed-to-be-ai-created-by-a-guy-in-india/)

---

**[MeshCore development team splits over trademark dispute and AI-generated code](https://news.ycombinator.com/item?id=47878117)**

Migrating to the new meshcore.io site

⬆️ 86 • 💬 57 • 4h ago • [blog.meshcore.io](https://blog.meshcore.io/2026/04/23/the-split)

---

---

## YouTube Videos: "ai"

**[Claude 5 – The New AI Era is Here! BYE, CHATGPT...](https://www.youtube.com/watch?v=qT4toLvs3n8)**

sponsored Build with Softr ...

📺 AI Master

👁️ 5K • 👍 178 • 💬 20 • ⏱️ 21:44 • 4h ago

---

**[AI Has Officially Reached &#39;The Point of No Return&#39;…](https://www.youtube.com/watch?v=JxxJi0jMqi0)**

Smalls: Get 60% off your first order + FREE shipping & FREE treats for life at https://smalls.com/ICED Episode Link ...

📺 The Iced Coffee Hour Clips

👁️ 5K • 👍 66 • 💬 30 • ⏱️ 9:25 • 1d ago

---

**[AI &amp; the Future of Work | The Weekly Show with Jon Stewart](https://www.youtube.com/watch?v=RB_WmoH5nQ4)**

As artificial intelligence continues to integrate into the workforce, Jon is joined by MIT economists David Autor and Daron ...

📺 The Weekly Show with Jon Stewart

👁️ 131K • 👍 4K • 💬 720 • ⏱️ 1:13:14 • 1d ago

---

**[Trump addresses AI risk: ‘We have to be careful’](https://www.youtube.com/watch?v=MmGOcebevxA)**

President Donald Trump discusses concerns over the use of AI and cyberattacks on 'Mornings with Maria.' #foxbusiness ...

📺 Fox Business

👁️ 2K • 👍 75 • 💬 27 • ⏱️ 1:40 • 3h ago

---

**[I&#39;ve studied AI risk for 20 years. We&#39;re close to a disaster.](https://www.youtube.com/watch?v=fYRmnrDFPes)**

Roman Yampolskiy explains why superintelligence cannot be controlled, why the gap between AI capabilities and AI safety keeps ...

📺 Future of Life Institute

👁️ 4K • 👍 205 • 💬 52 • ⏱️ 19:17 • 7h ago

---

**[New AI image generator BEATS EVERYTHING](https://www.youtube.com/watch?v=TLFPbMUtErM)**

ChatGPT Images 2.0 review. GPT Image 2.0 vs Nano Banana. #ai #aiart #aitools #imagegenerator #agi Thanks to our sponsor ...

📺 AI Search

👁️ 83K • 👍 3K • 💬 640 • ⏱️ 35:20 • 1d ago

---

**[$200B AI WAR - I Think This Stock Wins](https://www.youtube.com/watch?v=tgPtHrsdeEA)**

Amazon just committed $200 billion to AI infrastructure. Microsoft is spending $80 billion in a single year. Meta, Google — they're ...

📺 Everything Money

👁️ 17K • 👍 405 • 💬 77 • ⏱️ 20:36 • 1d ago

---

**[AI agent runs real San Francisco storefront, hires human employees](https://www.youtube.com/watch?v=gNN5DpYq4_E)**

AI-run San Francisco store “Luna” has created job listings, interviewed candidates and hired staff. Mike Muse explains the ...

📺 ABC News

👁️ 3K • 👍 24 • 💬 12 • ⏱️ 3:18 • 22h ago

---

**[AI is bringing a &#39;REINDUSTRIALIZATION OF AMERICA&#39;, Microsoft President says](https://www.youtube.com/watch?v=8EUXKSkxknw)**

Microsoft Vice Chairman and President Brad Smith discusses AI's profound impact on healthcare, improving diagnostics, and ...

📺 Fox Business Clips

👁️ 4K • 👍 156 • 💬 63 • ⏱️ 13:39 • 6h ago

---

**[New AI Robot From China Breaks Human Limits](https://www.youtube.com/watch?v=EJbJMg2RNgw)**

AGIBOT just rolled out a full new wave of humanoid robots and AI models built for real deployment, while researchers in South ...

📺 AI Revolution

👁️ 32K • 👍 790 • 💬 51 • ⏱️ 16:29 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)**

*Qwen*

Qwen3.6-35B-A3B is a 35B parameter causal language model with a vision encoder, optimized for agentic coding tasks and featuring enhanced thinking preservation for iterative development. It supports a context length of 262,144 tokens, extensible up to 1,010,000.

`image-text-to-text` `36.0B`

⬇️ 717,811 • ❤️ 1,323 • 1d ago

---

**[Kimi-K2.6](https://huggingface.co/moonshotai/Kimi-K2.6)**

*Moonshot AI*

Kimi K2.6 is a 1T parameter multimodal agentic model excelling in long-horizon coding and coding-driven design, capable of generating production-ready interfaces and workflows from prompts and visual inputs. It features an advanced agent swarm for complex task orchestration and proactive autonomous execution.

`image-text-to-text` `1058.6B`

⬇️ 125,825 • ❤️ 876 • 15h ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 23,964 • ❤️ 634 • 1d ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 1,888 • ❤️ 534 • 1d ago

---

**[Qwen3.6-35B-A3B-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF)**

*Unsloth AI*

Qwen3.6-35B-A3B is a 35B parameter causal language model with vision capabilities, optimized for agentic coding and reasoning tasks. It features a large context window (262k native, extensible to 1M+ tokens) and improved tool-calling, making it suitable for complex development workflows and iterative coding.

`image-text-to-text` `34.7B`

⬇️ 1,283,534 • ❤️ 706 • 3d ago

---

**[HY-World-2.0](https://huggingface.co/tencent/HY-World-2.0)**

*Tencent*

HY-World 2.0 is a multi-modal framework for generating and reconstructing 3D worlds from text, images, or video. It produces editable 3D assets like meshes and Gaussian Splattings, enabling applications in game development and simulation.

`image-to-3d`

⬇️ 0 • ❤️ 572 • 1d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal model based on Qwen3.6-35B-A3B, capable of processing text and images. It features a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context, optimized for lossless generation without refusals, suitable for diverse creative and technical applications.

`image-text-to-text` `34.7B`

⬇️ 350,262 • ❤️ 396 • 6d ago

---

**[Qwen3.6-27B-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-GGUF)**

*Unsloth AI*

Qwen3.6-27B-GGUF is a 27B parameter causal language model with vision capabilities, optimized for agentic coding and complex reasoning tasks. It supports extended context lengths up to 1,010,000 tokens and features improved tool-calling and thinking preservation for enhanced developer productivity.

`image-text-to-text` `26.9B`

⬇️ 131,398 • ❤️ 312 • 1d ago

---

**[gemma-4-E4B-it-OBLITERATED](https://huggingface.co/OBLITERATUS/gemma-4-E4B-it-OBLITERATED)**

*OBLITERATUS*

Gemma 4 E4B OBLITERATED v3 is a text-generation model with 0% refusal and improved coding capabilities, designed for uncensored and unrestricted AI interactions. It features a modified architecture with 720 intact tensors, making it highly compatible with tools like Ollama and llama.cpp, and optimized for performance on consumer hardware.

`text-generation` `8.0B`

⬇️ 90,064 • ❤️ 477 • 3d ago

---

**[gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)**

*Google*

Gemma 4 31B is an instruction-tuned, multimodal LLM capable of processing text and images to generate text. It excels at reasoning, coding, and handling long contexts (256K tokens) with a hybrid attention mechanism for efficient inference, suitable for complex agentic workflows.

`image-text-to-text` `32.7B`

⬇️ 5,103,971 • ❤️ 2,311 • 13d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 17 • 💬 2 • ⭐ 4,301 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[RAG-Anything: All-in-One RAG Framework](https://huggingface.co/papers/2510.12323)**

*Zirui Guo, Xubin Ren, Lingrui Xu et al. (5 authors)*

🏢 Data Intelligence Lab@HKU

RAG-Anything is a unified framework that enhances multimodal knowledge retrieval by integrating cross-modal relationships and semantic matching, outperforming existing methods on complex benchmarks.

▲ 74 • 💬 6 • ⭐ 17,898 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.12323) • [💻 code](https://github.com/HKUDS/RAG-Anything)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 9 • 💬 2 • ⭐ 6,293 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 24 • 💬 1 • ⭐ 20,707 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 48 • 💬 2 • ⭐ 52,574 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[OpenGame: Open Agentic Coding for Games](https://huggingface.co/papers/2604.18394)**

*Yilei Jiang, Jinyuan Hu, Qianyin Xiao et al. (11 authors)*

OpenGame is an open-source agentic framework for end-to-end web game creation that uses specialized code models and evaluation benchmarks to overcome challenges in interactive application development.

▲ 63 • 💬 4 • ⭐ 646 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2604.18394) • [💻 code](https://github.com/leigest519/OpenGame) • [🔗 project](https://www.opengame-project-page.com/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 54 • 💬 1 • ⭐ 77,882 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 165 • 💬 10 • ⭐ 40,809 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 160 • 💬 2 • ⭐ 60,971 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[LLaDA2.0-Uni: Unifying Multimodal Understanding and Generation with Diffusion Large Language Model](https://huggingface.co/papers/2604.20796)**

*Inclusion AI, Tiwei Bie, Haoxing Chen et al. (18 authors)*

🏢 inclusionAI

LLaDA2.0-Uni is a unified discrete diffusion language model that integrates multimodal understanding and generation through a semantic discrete tokenizer, MoE-based backbone, and diffusion decoder, achieving performance comparable to specialized vision-language models while enabling efficient inference and high-fidelity image generation.

▲ 207 • 💬 1 • ⭐ 50 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2604.20796) • [💻 code](https://github.com/inclusionAI/LLaDA2.0-Uni)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 49.2k • 🔱 6.5k • 15h ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 44.7k • 🔱 2.3k • 5d ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 38.9k • 🔱 7.9k • 2d ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 33.7k • 🔱 3.7k • 2h ago

---

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 9.6k • 🔱 2.1k • 1d ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 20+ AI Agent Skills.

`Go`

⭐ 8.6k • 🔱 554 • 3h ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 5.9k • 🔱 997 • 12h ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.6k • 🔱 1.6k • 11d ago

---

**[elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3)**

LIBERATED AI CHAT

`TypeScript`

⭐ 5.3k • 🔱 1.2k • 28d ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.7k • 🔱 461 • 15d ago

---

---

*Generated by PeekDeck - A glance is all you need*
