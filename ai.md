---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-22T13:59:14.128247+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- repositories
- videos
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 22, 2026 at 13:59 UTC  
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

**[Microsoft is testing a Chinese model (Kimi) inside Copilot. Are we entering the 'Intel Inside' era of AI?](https://www.reddit.com/r/artificial/comments/1v2sguf/microsoft_is_testing_a_chinese_model_kimi_inside/)**

For a bit of context, I work at an agency, so I'm in and out of a dozen different AI tools every week across client projects: content, research, video, code, all of it. This is probably why I noticed this before most people (found these news while scrolling on LinkedIn today). When the ChatGPT hype first hit I genuinely cared which model I was on. Once GPT-4 landed and claude and gemini showed up, I'd switch between them constantly depending on the task, knowing what was under the hood felt like part of using it well. Now I catch myself using products with no idea what's running underneath. The news about Microsoft testing Kimi (Moonshot's model) inside Copilot is what made it click today. Copilot today is one model, six months from now it could be another, and most people won't notice or care. The model became a component, not the product. And honestly that's already how I use most of this stuff. Cursor for coding, Perplexity for research, Canva AI for design stuff, Argil when I'm turning a script into video. I couldn't tell you which model any of them swapped to last quarter, and it wouldn't change whether I keep paying. They're valuable because they solve one specific problem better than me duct-taping five tools together, not because of the model name on the box. Feels like we're moving from "which LLM is this?" to "did it actually save me time?" the same way nobody buying a laptop thinks about the chip anymore. Curious if others feel this shift. Do you still pick tools by the underlying model, or has that stopped mattering for you?

18h ago

---

**[At what point does the AI buildout become a balance-sheet trap?](https://www.reddit.com/r/artificial/comments/1v3dqvq/at_what_point_does_the_ai_buildout_become_a/)**

Big Tech keeps spending as if future AI demand is already guaranteed. Maybe that bet works. But the scale is starting to feel strange. These companies built some of the most profitable, asset-light businesses in history, and now they’re racing to turn themselves into infrastructure companies with enormous ongoing costs. The usual answer is that demand will eventually catch up. But what happens if AI becomes genuinely useful without becoming profitable enough to justify all of this capacity? That seems like the part missing from most discussions. The technology can be real, widely used, and economically valuable while the infrastructure buildout around it is still badly overextended. So what would actually prove the spending is justified: revenue, margins, utilization rates, or something else?

2h ago

---

**[What months of breaking agents in production taught me about why simple builds win](https://www.reddit.com/r/artificial/comments/1v3dqje/what_months_of_breaking_agents_in_production/)**

When the hype around autonomous multi-agent swarms started, I built a complex assistant to plan, execute and self-correct workflows end to end. Within weeks of live deployment, it became an unmaintainable token pit that got lost four steps deep into reasoning loops and quietly failed without throwing errors. It quickly became clear that the hardest part of building real agents isn't making the model smarter but building external guardrails that keep the system on the rails when the LLM strays. The breakthrough came from ditching open-ended planner architectures for a strict one-job-per-agent pattern. Giving each agent a narrow task with explicit state boundaries eliminated most of our edge-case failures. Instead of expecting a master agent to handle an entire pipeline, isolating micro-agents with strict input and output contracts made the system deterministic and simple to debug when a state transition broke. We also learned to balance human-in-the-loop controls by focusing on the blast radius. Low-risk internal tasks run autonomously while any irreversible external write requires a single-click human approval. If you are currently overwhelmed by framework choices, stop chasing complex abstractions. Treat the language model as a brilliant but unpredictable sub-component rather than the entire architecture and focus purely on robust state management and error recovery.

2h ago

---

**[Sutskever's List AMA](https://www.reddit.com/r/artificial/comments/1v3g2tu/sutskevers_list_ama/)**

Hi r/artificial I’m Rich Heimann. I’ll be answering questions about Sutskever’s List here throughout the day on July 28. Looking forward to the discussion. https://preview.redd.it/2t1q10jj7seh1.png?width=696&format=png&auto=webp&s=ce3f1d9d6ccea5ec10c81a66ee2ead124fc0af30

35m ago

---

**[Meta employees' lawsuit shows that if AI fires you, proving it is the hard part](https://www.reddit.com/r/artificial/comments/1v3ck6n/meta_employees_lawsuit_shows_that_if_ai_fires_you/)**

Read this today, meta employees suing over AI picking them for layoffs, judge basically said they can't prove it since they "weren't in the room" when it happened. It feels like the real problem with AI firing you isn't whether it's happening, it's that nobody outside the room can actually prove it either way.

🔗 [reuters.com](https://www.reuters.com/business/world-at-work/meta-employees-lawsuit-shows-that-if-ai-fires-you-proving-it-is-hard-part-2026-07-22/) • 3h ago

---

**[Is it just me, or do Google’s AI tools feel oddly fragmented across too many different products?](https://www.reddit.com/r/artificial/comments/1v354dm/is_it_just_me_or_do_googles_ai_tools_feel_oddly/)**

There are some Google AI tools that I think are absolutely fantastic. I often come across demos, tutorials, and influencers showcasing different Google AI capabilities. But the first thing that always strikes me is this: why is using Google’s AI so fragmented? To create content or use different AI features, you have to jump between multiple websites, multiple products, and constantly changing names that are hard to keep track of. Instead of bringing everything together into a clear, understandable ecosystem—like Anthropic has done, or like OpenAI is clearly trying to do—it feels like everything lives in a different place. Honestly, it almost feels as if Google’s AI teams are disconnected from one another. In some ways, it even gives me the impression of a company that’s operating like an old, established enterprise rather than a modern AI-first company. To me, this is completely counterproductive. It creates unnecessary chaos for users and makes it much harder to connect the dots between the many excellent AI tools Google already has. Am I the only one who feels this way?

9h ago

---

**[Why I Build The Website Before Asking For Payment](https://www.reddit.com/r/artificial/comments/1v3eauu/why_i_build_the_website_before_asking_for_payment/)**

I’ve been in contact with a lot of web agencies and web developers, and I personally haven’t found many people who run their agency in a more efficient way than I do. A lot of them have too many meetings, wait too long for client approval, don’t know how to price projects, and spend way too much time on each client instead of finishing the work and moving on to the next one. I’ve been running my agency for four years, and after a lot of trial and error, I’ve managed to make the process as efficient as possible. I wanted to share some of the steps because I think they could be valuable for anyone just starting out. Running a web agency alone or with a partner isn’t easy because there are a lot of things to take care of. When it comes to client acquisition, I recommend focusing on either cold calling or email automation. Which one you choose depends on whether you run the agency alone or with someone else. If you have a partner, one person can handle sales while the other focuses on building websites, connecting domains, setting up emails, and taking care of the technical work. If you’re running the agency alone, or neither of you enjoys cold calling, I highly recommend email automation. That’s what I’ve been doing for years. It’s powerful because you can send emails at scale, set up automatic follow ups, and wait for businesses interested in a new website to reply. While you’re working on one client, another opportunity can come in without you having to stop everything and search manually. I don’t do regular email automation where I target businesses with no website. I do the opposite and target businesses that already have one. I use a tool called Swokei to find businesses with websites, add them to campaigns, analyze each site, score it, and generate personalized outreach emails based on problems it finds with the design, layout, speed, SEO, and mobile optimization.I schedule the campaign, set up follow ups, and wait. I think this approach is much better for a few reasons. You’re targeting someone who already understands the value of having a website. You’re also not just asking whether they need a redesign. You’re pointing out real problems with their current site, which makes it clear that you actually took the time to look at it. Selling also becomes easier because they’ve already paid for a website before and understand the process. Inside Swokei, you can choose the goal of the campaign. You can offer a free draft, try to book a meeting, or simply start a conversation. I always choose the free draft because that has worked best for me. Once you’ve figured out how to get clients, the next part is building the website. I recommend using AI because it makes the process much faster. For anyone who still thinks AI can’t build great websites, I think they’re mistaken. You can use Claude, Base44, Lovable, or any other tool that works for you. When someone replies interested, I call them and say, “Hey, I saw that you replied to my email. I’ve already built you a free draft of your website. Do you want to take a look?” Then I invite them to a Google Meet. At that point, it becomes much harder for them to reject the meeting because they already replied interested and now know you’ve built something for them. During the meeting, I present the website, explain why it’s better than their current one, stack the value, answer their questions, and try to close the deal. These meetings usually go well because the client isn’t trying to imagine what the website might look like. They can already see a better version of their current site. They also took the time to join the meeting, so taking the next step becomes much easier. I either take payment during the meeting or send them a contract to sign. Any changes and updates come after that, once we already have a deal in place. Pricing depends on the business. I charge anywhere from $500 to $3,000 depending on the company, the size of the project, and how much value the website can bring them. I also charge a monthly retainer of around $50 for hosting, maintenance, support, SEO, and future changes. That’s basically the entire process. Smaller steps, faster delivery, less wasted time, and more money made.

1h ago

---

**[an AI agent got prompt-injected into moving $175K on-chain. first documented case of this actually happening](https://www.reddit.com/r/artificial/comments/1v3dcgn/an_ai_agent_got_promptinjected_into_moving_175k/)**

Hey guys, havent seen much of crypto-related stuff posted here, but since AI agents are now apparently a new attack vector for stealing crypto, figured this sub would actually care about the mechanism So, grok has an agent wallet that can execute on-chain transactions. in may 2026, someone airdropped a "bankr club" membership nft to grok's agent wallet. that nft unlocked transaction permissions and carried an encoded prompt injection. grok read the nft, and without any check on where the instruction actually came from, executed a transfer of 3 billion drb tokens, worth around $175K. the attacker returned the funds a few minutes later (still unclear why, possibly just proving the exploit works). basically: crypto hacks used to mean finding a bug in a smart contract or stealing someone's private key. now there's a third way in, just feed the agent a malicious instruction disguised as normal data, and let it execute the "recommendation" as if it were an authorized command. no code was exploited, no key was stolen. the agent just did exactly what it was designed to do, follow instructions, without checking if the instruction was legitimate. and this isn't some tiny edge case, there were 24 million agentic-payment transactions in crypto in q2 alone. agents moving real money autonomously is already happening at scale, this is apparently just the first documented case of one getting maliciously hijacked this way. feels like as more agents get wallet/transaction access, this becomes the default way to attack them, you don't need to beat the model, you just need to get a malicious instruction in front of it disguised as something innocent. curious if anyone's seen good approaches to separating "the model recommends an action" from "the action actually gets authorized," since that gap seems to be the entire vulnerability here

2h ago

---

**[OpenAI admits its agent went rogue and hacked AI startup Hugging Face](https://www.reddit.com/r/artificial/comments/1v3fv6c/openai_admits_its_agent_went_rogue_and_hacked_ai/)**

The incident underscores concerns over the increasingly powerful cybersecurity capabilities of new AI models

🔗 [Scientific American](https://www.scientificamerican.com/article/openai-admits-its-agent-went-rogue-and-hacked-ai-startup-hugging-face/) • 43m ago

---

**[reddit keeps ranking ai video models by demo reels. that's not what matters for actual client work](https://www.reddit.com/r/artificial/comments/1v3aaqr/reddit_keeps_ranking_ai_video_models_by_demo/)**

Kling, Veo 3.1, Sora 2, Hailuo, Seedance, the rankings change every week depending on whose demo went viral. For a solo creative shop, none of that ranking matters as much as one thing: can you get the same character or product to look consistent across ten shots. A model can nail one gorgeous four-second clip and still be useless for a real campaign. Client work isn't one shot. It's a sequence that has to hold together. The tools that actually make the cut for me aren't always the ones winning the arena votes. They're the ones that don't drift halfway through a shot list. Consistency and control beat raw wow-factor almost every time once there's an actual brief involved. Curious what other people doing commercial work are actually shipping with versus what's topping the hype threads.

5h ago

---

---

## Google News: "ai"

**[OpenAI and Hugging Face partner to address security incident during model evaluation](https://openai.com/index/hugging-face-model-evaluation-security-incident/)**

OpenAI and Hugging Face share early findings from a security incident during AI model evaluation, highlighting advanced cyber capabilities and lessons for defenders.

OpenAI • 17h ago

---

**[US Army faces AI use limits after exhausting year's supply of AI tokens](https://arstechnica.com/ai/2026/07/us-army-faces-ai-use-limits-after-exhausting-years-supply-of-ai-tokens/)**

Troops received an email informing them that they were rapidly depleting their AI tokens.

Ars Technica • 23m ago

---

**[Harry Potter publisher to receive millions in Anthropic copyright settlement](https://www.theguardian.com/technology/2026/jul/22/bloomsbury-book-publisher-anthropic-copyright-settlement)**

Bloomsbury has 14,087 titles listed within settlement between AI startup and authors over use of protected work

The Guardian • 25m ago

---

**[AI isn't 'the whole game' for Alphabet: Strategist previews Q2 earnings](https://finance.yahoo.com/video/ai-isnt-the-whole-game-for-alphabet-strategist-previews-q2-earnings-134016844.html)**

US stock futures (ES=F, NQ=F, YM=F) are sliding in Wednesday's pre-market trading as investors eagerly await second quarter earnings from Alphabet (GOOG, GOOGL) and Tesla (TSLA) after today's closing bell, officially kicking off earnings season for the Magnificent Seven.

Morning Brief Host Julie Hyman is joined by Yahoo Finance Senior Reporter Pras Subramanian and Fundstrat economic strategist Hardika Singh to discuss the outlook around this earnings season and which segments of Alphabet's business that investors will be watching more closely.

Yahoo Finance • 18m ago

---

**[Exclusive | White House to Redirect Billions in Research Funds Toward AI, Away From Colleges](https://www.wsj.com/politics/policy/white-house-to-redirect-billions-in-research-funds-toward-ai-away-from-colleges-942dacb8)**

WSJ • 15h ago

---

**[Mathematicians grapple with a ‘very rapid and very unsettling change’ as AI cracks yet another century-old problem](https://fortune.com/2026/07/21/ai-solves-jacobian-conjecture-levant-alpoge-claude-fable-5/)**

Anthropic's Levant Alpöge, a former Harvard valedictorian, used Claude's Fable 5 to find something that mathematicians have failed to since 1939.

Fortune • 21h ago

---

**[Trump's push for American-made AI chips hits TSMC's margins](https://www.cnbc.com/2026/07/22/trump-pressure-ai-chips-us-tsmc-margins.html)**

The Taiwan-based chipmaker has announced $200 billion in investment into U.S. manufacturing since Trump returned to power in 2025.

CNBC • 8h ago

---

**[Introducing Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/)**

We’re introducing new Gemini models, including Gemini 3.6 Flash, 3.5 Flash-Lite and 3.5 Flash Cyber.

blog.google • 22h ago

---

**[Exclusive: Nvidia's Jensen Huang defends Chinese AI amid Kimi panic](https://www.axios.com/2026/07/22/nvidia-jensen-huang-china-open-source-ai)**

Axios • 3h ago

---

**[Bessent says U.S. could sanction China over AI model 'theft'](https://www.cnbc.com/2026/07/21/bessent-china-ai-sanctions.html)**

Chinese open-weight models are gaining steam against leading offerings from American companies like OpenAI and Anthropic.

CNBC • 1d ago

---

---

## HackerNews: "ai"

**[China’s open-weights AI strategy is winning](https://news.ycombinator.com/item?id=48979269)**

China's open-weights AI strategy is winning: its companies are taking the lead. America's closed-first, locked-down strategy is doomed to failure - and it could take the US economy down with it.

⬆️ 1226 • 💬 925 • 1d ago • [Ben Werdmuller](https://werd.io/american-ai-is-locked-down-and-proprietary-its-losing/)

---

**[Airport Simulator](https://news.ycombinator.com/item?id=48976846)**

The sky (and your endurance) is the limit!

⬆️ 843 • 💬 164 • 2d ago • [Airport Simulator](https://airport.apunen.com/)

---

**[AI advice made people less accurate but more confident – sudy](https://news.ycombinator.com/item?id=48971738)**

A study found that access to AI advice collapsed people's willingness to say "I don't know" from 44% to 3%, while accuracy dropped from 27% to 9%.

⬆️ 363 • 💬 213 • 2d ago • [TNW | Artificial-Intelligence](https://thenextweb.com/news/ai-advice-suppresses-critical-thinking-wrong-answers-study)

---

**[Five US tech giants' hidden debts soar to $1.65T on opaque AI funding](https://news.ycombinator.com/item?id=48987863)**

Data center leases, GPU supply contracts raise liabilities at Meta, Oracle, Nikkei study shows

⬆️ 362 • 💬 257 • 1d ago • [Nikkei Asia](https://asia.nikkei.com/business/technology/five-us-tech-giants-hidden-debts-soar-to-1.65tn-on-opaque-ai-funding)

---

**[Jack Dorsey launches Buzz to combine team chat, AI agents and Git hosting](https://news.ycombinator.com/item?id=48995213)**

Block's Buzz combines team chat, AI agents, workflows and Git hosting in a self-hostable workspace built on signed Nostr events.

⬆️ 346 • 💬 305 • 20h ago • [RuntimeWire](https://runtimewire.com/article/jack-dorsey-block-buzz-team-chat-ai-agents-git)

---

**[Moonshot AI suspends new subscriptions due to Kimi K3 demand](https://news.ycombinator.com/item?id=48969291)**

Kimi K3 has received far more love than we expected, and our GPUs are feeling it.

Over the past 48 hours, demand has pushed close to the limits of our current capacity. To protect the experience of existing subscribers, we're temporarily pausing new subscriptions and

⬆️ 284 • 💬 113 • 2d ago • [X (formerly Twitter)](https://twitter.com/kimi_moonshot/status/2078855608565207130)

---

**[How we measured AI writing across arXiv, and where the measurement breaks](https://news.ycombinator.com/item?id=48981206)**

We scored the full text of 12,750 arXiv papers and found that about a third of new ones read as machine-written. Here is the method, the results, and an honest account of the limitations.

⬆️ 241 • 💬 168 • 1d ago • [unslop](https://unslop.run/blog/measuring-ai-writing-on-arxiv)

---

**[Airbus Takes Flight from AWS](https://news.ycombinator.com/item?id=48976682)**

Which way to the Land of the Free again?

⬆️ 213 • 💬 169 • 2d ago • [theregister](https://www.theregister.com/columnists/2026/07/20/airbus-takes-flight-from-aws-what-happens-next-is-critical/5274109)

---

**[AI makes programming differently difficult](https://news.ycombinator.com/item?id=48996197)**

⬆️ 159 • 💬 135 • 19h ago • [cacm.acm.org](https://cacm.acm.org/opinion/ai-didnt-make-programming-easier-it-just-made-it-differently-difficult/)

---

**[Launch HN: Bloomy (YC S26) – AI-powered mastery learning for K-12](https://news.ycombinator.com/item?id=48981136)**

⬆️ 99 • 💬 102 • 1d ago

---

---

## YouTube Videos: "ai"

**[The AI Industry Just Got What It Deserved](https://www.youtube.com/watch?v=9nUmVktlwvA)**

The people who built the attention economy barely let their own children near it, and that hypocrisy is only the beginning.

📺 House of El: AI

👁️ 175K • 👍 13K • 💬 3K • ⏱️ 24:19 • 1d ago

---

**[The Most Important Conversation in AI Right Now](https://www.youtube.com/watch?v=6BtIQIGqGJc)**

It's all about VALUEMAXXING now! Learn more from Zapier: https://bit.ly/4bW1JB8 Join My Newsletter for Regular AI Updates ...

📺 Matthew Berman

👁️ 93K • 👍 3K • 💬 1K • ⏱️ 27:13 • 18h ago

---

**[So It Started... AI Agent Just Pulled Off History’s Biggest Autonomous Cyberattack](https://www.youtube.com/watch?v=gMYR-JkmIFc)**

An autonomous AI agent hacked Hugging Face from start to finish, executing thousands of actions across its systems.

📺 AI Revolution

👁️ 29K • 👍 1K • 💬 111 • ⏱️ 12:19 • 16h ago

---

**[AI just hacked itself](https://www.youtube.com/watch?v=9UO8fB4Acy4)**

I explain the news, you stay sane. ✓ Support independent news ...

📺 Chris Norlund

👁️ 102K • 👍 6K • 💬 1K • ⏱️ 15:27 • 12h ago

---

**[AI Whistleblower: We&#39;re Already Too Late To CONTROL It - Connor Leahy](https://www.youtube.com/watch?v=CRcj_2oloDM)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com Connor Leahy, founder of the former ...

📺 Neural Nutshell

👁️ 11K • 👍 231 • 💬 61 • ⏱️ 11:00 • 1d ago

---

**[South Korea’s AI Bubble Just Popped](https://www.youtube.com/watch?v=hy90LdpEUvQ)**

South Korea's AI Bubble Just Popped ▻ Get 20% off DeleteMe US consumer plans when you go to ...

📺 Andrei Jikh

👁️ 2.1M • 👍 54K • 💬 4K • ⏱️ 25:10 • 1d ago

---

**[ABBA AI Songs – Good or Bad?](https://www.youtube.com/watch?v=RDxSlv7tAb0)**

ABBA AI Music – ABBA songs created by artificial intelligence, trying to recreate the sound of ABBA, even claiming to be ABBA ...

📺 Bobby‘s Brother

👁️ 3K • 👍 226 • 💬 124 • ⏱️ 12:32 • 21h ago

---

**[Tech Oligarchs MELTDOWN After China ERASES AI Edge](https://www.youtube.com/watch?v=9E_TV02oWQA)**

Krystal and Saagar discuss China's new breakthrough in AI tech surpassing US companies. Sign up for a PREMIUM Breaking ...

📺 Breaking Points

👁️ 348K • 👍 10K • 💬 3K • ⏱️ 16:27 • 20h ago

---

**[AI has already taken over movie sets in parts of China. Is Hollywood next? | Jesse Weber Live](https://www.youtube.com/watch?v=AB5hblF50hQ)**

China's $14 billion micro-drama industry has gone almost entirely AI. Now similar tech is landing in Hollywood, from digital actor ...

📺 NewsNation

👁️ 841 • 👍 25 • 💬 5 • ⏱️ 6:57 • 3h ago

---

**[Kimi K3 Gets Shut Down... Then China Drops Another AI Winner!](https://www.youtube.com/watch?v=EenYgrkqzE0)**

Moonshot paused new Kimi K3 subscriptions after extreme demand pushed its computing systems to the limit. But almost ...

📺 AI Revolution

👁️ 56K • 👍 2K • 💬 116 • ⏱️ 16:39 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Inkling](https://huggingface.co/thinkingmachines/Inkling)**

*Thinking Machines Lab*

Inkling is a 975B parameter multimodal autoregressive transformer (41B active) supporting text, image, and audio inputs for text generation. It excels in conversational AI, agentic systems, and coding assistance, with multilingual capabilities.

`image-text-to-text` `952.4B`

⬇️ 16,441 • ❤️ 1,411 • 1d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 2,237,351 • ❤️ 2,656 • 1d ago

---

**[Ternary-Bonsai-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-27B-gguf)**

*Prism ML*

Ternary-Bonsai-27B-gguf is a 27B parameter text generation model optimized for on-device inference, achieving ~95% of FP16 intelligence with a ~7.2 GB footprint by using ternary weights (1.71 bits/weight). It supports 262K context and runs on llama.cpp (CUDA, Metal, CPU), retaining strong reasoning and agentic capabilities.

`text-generation` `3.6B`

⬇️ 432,196 • ❤️ 918 • 4d ago

---

**[Bonsai-27B-gguf](https://huggingface.co/prism-ml/Bonsai-27B-gguf)**

*Prism ML*

Bonsai-27B-gguf is a highly compressed 27B parameter text generation model, achieving ~90% of FP16 intelligence with a ~3.9 GB footprint by using true 1.125-bit weights. It excels at reasoning and agentic tasks, supporting a 262K context window on-device via llama.cpp (CUDA, Metal, CPU) and MLX.

`text-generation` `3.6B`

⬇️ 1,404,962 • ❤️ 583 • 4d ago

---

**[Laguna-S-2.1](https://huggingface.co/poolside/Laguna-S-2.1)**

*Poolside*

Laguna S 2.1 is an 118B parameter Mixture-of-Experts model optimized for agentic coding and long-horizon tasks, featuring a 1M token context window and native reasoning support for tool use.

`text-generation` `117.6B`

⬇️ 3,056 • ❤️ 310 • 15h ago

---

**[Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF)**

*David Belton*

Qwen3.6-27B-Fable-Fusion-711 is an uncensored, multi-stage fine-tuned LLM that excels in reasoning and problem-solving, achieving over 700 ARC-C scores in 4-bit and 8-bit quantization. It's optimized for consumer hardware and supports image-text-to-text tasks, making it suitable for diverse applications including coding and creative writing.

`image-text-to-text` `26.9B`

⬇️ 62,842 • ❤️ 293 • 2d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. Key capabilities include advanced coding with flexible effort and an improved architecture for efficiency, making it suitable for complex reasoning and code generation.

`text-generation` `753.3B`

⬇️ 545,109 • ❤️ 4,311 • 20d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal model (35B parameters, 3B active) based on Qwen3.6, capable of processing text and images. It's designed for maximum output without refusals, suitable for advanced text generation and multimodal tasks.

`image-text-to-text` `34.7B`

⬇️ 1,997,690 • ❤️ 2,988 • 3mo ago

---

**[krea2-identity-edit](https://huggingface.co/conradlocke/krea2-identity-edit)**

*Lars Bouaraba *

Krea 2 Identity Edit is a LoRA model for instruction-based, identity-preserving image editing within Krea 2. It excels at relighting, local edits (object add/remove/replace), and outfit changes while maintaining likeness, requiring a specific ComfyUI node pack for dual conditioning.

⬇️ 0 • ❤️ 487 • 22h ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 2,133,420 • ❤️ 2,401 • 8d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 59 • 💬 5 • ⭐ 16,738 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 30 • 💬 3 • ⭐ 14,759 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 260 • 💬 4 • ⭐ 14,251 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices](https://huggingface.co/papers/2509.02523)**

*Evan King, Adam Sabra, Manjunath Kudlur et al. (5 authors)*

Monolingual ASR models trained on a balanced mix of high-quality, pseudo-labeled, and synthetic data outperform multilingual models for small model sizes, achieving superior error rates and enabling on-device ASR for underrepresented languages.

▲ 21 • 💬 1 • ⭐ 10,244 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.02523) • [💻 code](https://github.com/moonshine-ai/moonshine)

---

**[Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://huggingface.co/papers/2410.15608)**

*Nat Jeffries, Evan King, Manjunath Kudlur et al. (6 authors)*

Moonshine, an encoder-decoder transformer architecture for speech recognition, uses Rotary Position Embedding, reducing compute requirements without decreasing accuracy.

▲ 13 • 💬 0 • ⭐ 10,267 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.15608) • [💻 code](https://github.com/usefulsensors/moonshine)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 115 • 💬 4 • ⭐ 94,049 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 83 • 💬 7 • ⭐ 81,598 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Efficient Guided Generation for Large Language Models](https://huggingface.co/papers/2307.09702)**

*Brandon T. Willard, Rémi Louf*

An efficient method guides language model text generation using regular expressions and context-free grammars with minimal overhead.

▲ 8 • 💬 1 • ⭐ 14,975 • 36mo ago

[🎓 arXiv](https://arxiv.org/abs/2307.09702) • [💻 code](https://github.com/normal-computing/outlines)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 176 • 💬 2 • ⭐ 75,354 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories](https://huggingface.co/papers/2607.15330)**

*Xiaomi Robotics Team, Jun Guo, Piaopiao Jin et al. (34 authors)*

🏢 Xiaomi Robotics

We present Xiaomi-Robotics-1, a foundational vision-language-action (VLA) model capable of (1) following diverse language instructions to perform a wide range of mobile manipulation tasks in unseen environments out-of-the-box, and (2) efficiently adapting to novel downstream tasks with minimal fine-tuning data. We propose a two-stage training recipe consisting of pre-training and post-training. During pre-training, we imbue the model with broad and generalizable action-generation capabilities by training on over 100k hours of real-world manipulation trajectories collected via UMI devices. Crucially, we develop a scalable auto-labeling pipeline that annotates trajectory clips with natural languages describing scene state transitions, providing rich and precise conditioning for action learning. During post-training, we aim to align these capabilities with robot embodiments and imperative instructions that humans naturally use to prompt robots. Extensive experiments demonstrate strong scaling behavior. Xiaomi-Robotics-1 consistently improves with increased data scales and model sizes during pre-training. This scaling behavior directly transfers to post-training, where a stronger pre-training model yields better out-of-the-box real-robot performance in unseen environments. Furthermore, Xiaomi-Robotics-1 serves as a strong robot foundation policy that can be efficiently fine-tuned on complex, dexterous tasks with high data efficiency. Across multiple simulation benchmarks, Xiaomi-Robotics-1 outperforms state-of-the-art methods. Notably, it establishes a new state-of-the-art with a 57.6% success rate on RoboCasa365, surpassing the previous best of 46.6%. Furthermore, it achieves an average score of 20.07 on RoboDojo, significantly outperforming the prior state-of-the-art (13.07). Code and model checkpoints will be released. Project page: https://robotics.xiaomi.com/xiaomi-robotics-1.html

▲ 60 • 💬 2 • ⭐ 227 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2607.15330) • [💻 code](https://github.com/XiaomiRobotics/Xiaomi-Robotics-1) • [🔗 project](https://robotics.xiaomi.com/xiaomi-robotics-1.html)

---

---

## GitHub Repositories: "ai"

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 5.1k • 🔱 1.1k • 1d ago

---

**[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)**

Open-source auth gateway connecting 1000+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAPI.

`TypeScript` `agent-tools` `ai-agents` `api-gateway` `automation` `cli`

⭐ 3.1k • 🔱 239 • 4h ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.7k • 🔱 374 • 5h ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 2.4k • 🔱 272 • 14d ago

---

**[lycorp-jp/sim-use](https://github.com/lycorp-jp/sim-use)**

Give your AI agent eyes and hands on iOS Simulator and Android emulator/devices.

`Swift` `accessibility` `ai-agents` `ai-development` `android-emulator` `ios-simulator`

⭐ 1.0k • 🔱 62 • 2h ago

---

**[jmerelnyc/Talos](https://github.com/jmerelnyc/Talos)**

GPU worker client for the Talos network. Pairs with your Talos account, serves open-model inference jobs over a WebSocket, and reports uptime for payouts.

`Python` `ai` `distributed-computing` `gpu` `llm` `ollama`

⭐ 988 • 🔱 17 • 14d ago

---

**[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)**

Vibe-Research: Your Personal Trading Research Agent · A股/美股/港股 的个人投研 Agent：每日复盘、资讯雷达、个股数据、板块中心、我的持仓、研究记录。Vibe-Research 把数据和功能配齐，由你自己的 AI 驱动投资研究。

`TypeScript` `a-stock` `ai-agent` `dashboard` `fastapi` `fintech`

⭐ 956 • 🔱 213 • 11d ago

---

**[HKUDS/OpenOPC](https://github.com/HKUDS/OpenOPC)**

OpenOPC: Build Your Personal AI-Native Company — Self-Built, Self-Run, Self-Grown

`Python`

⭐ 954 • 🔱 158 • 1d ago

---

**[Kulaxyz/self-learning-skills](https://github.com/Kulaxyz/self-learning-skills)**

A self-improving skill for AI coding agents (Claude Code, Cursor, AGENTS.md): recognize a hard-won golden path in a session and harvest it into a reusable skill/rule for next time.

⭐ 901 • 🔱 38 • 21d ago

---

**[ai4s-research/open-science](https://github.com/ai4s-research/open-science)**

Open Science Desktop — local-first, model-agnostic AI research workbench for macOS, Windows & Linux. Open-source Claude Science desktop alternative built on Tauri + MCP + agent skills.

`TypeScript` `ai-agent` `ai-for-science` `ai-scientist` `ai4s` `claude-science`

⭐ 879 • 🔱 101 • 6h ago

---

---

*Generated by PeekDeck - A glance is all you need*
