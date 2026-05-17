---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-17T01:24:40.560845+00:00'
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

**Last Updated:** May 17, 2026 at 01:24 UTC  
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

**[We keep saying AI "understands" things. Does it? Or are we just pattern-matching our own anthropomorphism?](https://www.reddit.com/r/artificial/comments/1tew6gr/we_keep_saying_ai_understands_things_does_it_or/)**

Every week there's a new paper or tweet claiming some model "understands" context, "reasons" about math, or "knows" what it doesn't know. But when you look closely, there's almost no consensus on what "understanding" even means — philosophically or empirically. Searle's Chinese Room argument is 40 years old and still hasn't been cleanly resolved. The "stochastic parrot" framing treats token prediction as the ceiling. Integrated Information Theory would say current architectures are near-zero in phi. And yet GPT-4 passes the bar exam. A few questions I've been sitting with: Is "understanding" even the right frame — or is it a folk-psychology term we're forcing onto a system that operates on completely different principles? Does it matter if a model "truly understands" if the outputs are indistinguishable from someone who does? Are we anthropomorphizing because it's useful shorthand — or because we genuinely don't have better language yet? I've been going deep on AI + philosophy of mind for a channel I run (@ContextByRaj on YouTube if you're into this space). But genuinely curious what this community thinks — especially people coming from ML or cognitive science backgrounds. Where do you land on this?

10h ago

---

**[Most enterprises are trying to scale AI on top of organizational chaos](https://www.reddit.com/r/artificial/comments/1tevqds/most_enterprises_are_trying_to_scale_ai_on_top_of/)**

I think we’re underestimating how chaotic enterprise AI adoption actually is inside large companies. From the outside, it looks simple: buy better models add copilots automate workflows deploy AI agents increase productivity But inside many enterprises, CIOs and CTOs are dealing with a much deeper problem: The organization itself is fragmented. Customer data exists across: CRM systems billing platforms support tools spreadsheets emails regional databases legacy systems nobody fully understands anymore And every system describes the “same customer” differently. Then leadership says: “Scale AI faster.” But scale AI on top of what exactly? Which system represents reality correctly? The CRM? The support history? The risk engine? The finance system? The employee’s undocumented tribal knowledge? This is where a lot of enterprise AI projects quietly break down. Not because the models are weak. But because the enterprise itself lacks a coherent representation of its own operations. And the tension gets worse: Boards want acceleration. Employees are already using AI unofficially. Vendors promise transformation in 90 days. Meanwhile CIOs still don’t have clear answers to questions like: Which workflows actually need AI? Which should remain deterministic automation? Where is human judgment still critical? Which data is trustworthy enough for AI decisions? Who owns accountability when AI influences actions? So companies launch pilots. The pilot works. Executives celebrate. Then scaling fails because the pilot never encountered the full institutional complexity of the enterprise. I’m increasingly convinced the next enterprise AI bottleneck is not model capability. It’s organizational legibility. The companies that win with AI may not be the ones with the smartest models. They may be the ones whose internal reality is structured clearly enough for AI to operate safely. Curious how many people here are seeing the same thing inside their organizations. :::

10h ago

---

**[Recent poll shows that 70% of Americans don't want AI data centers being built in their local area](https://www.reddit.com/r/artificial/comments/1tdw8if/recent_poll_shows_that_70_of_americans_dont_want/)**

While tech companies see AI data centers as the future, many Americans are becoming increasingly unhappy about having them built nearby.

🔗 [PC Guide](https://www.pcguide.com/pro/news-pro/recent-poll-shows-that-70-of-americans-dont-want-ai-data-centers-being-built-near-their-homes/) • 1d ago

---

**[Tech's Push to Be the Next Public Utility](https://www.reddit.com/r/artificial/comments/1tejpmh/techs_push_to_be_the_next_public_utility/)**

Amazon didn't ask permission to become critical infrastructure. They built AWS until enough of the economy depended on it that regulation became almost impossible. You can't turn off the internet's backbone. Now the same playbook is running with AI and data centers. Build the infrastructure everywhere. Create dependency at scale. Make yourself essential to healthcare, finance, government, and defense before anyone agrees you should be. Then negotiate from a position where shutting you down costs more than regulating you. The data center fights happening in communities right now — zoning battles, water usage protests, grid capacity fights — aren't about data centers. They're about who controls the next utility layer before the rules are written. Historical utilities — power, water, telecom — eventually got regulated because they became too essential to leave unaccountable. The window between "essential" and "regulated" is where the real money gets made. That window is open right now. Who should have the authority to decide whether AI infrastructure is a public utility — and what happens if we don't decide before the decision gets made for us?

20h ago

---

**[Stanford studied 51 real AI deployments and found a 71% vs 40% productivity gap - here's what separates the two groups](https://www.reddit.com/r/artificial/comments/1tebiq4/stanford_studied_51_real_ai_deployments_and_found/)**

I came across a Stanford research paper that actually went inside companies running AI in production - not pilots, not surveys, real deployments. They found something that stuck with me. Companies using what they call "agentic AI" - where the AI owns the task start to finish with no human approval loop - are seeing 71% median productivity gains. Companies using standard AI that assists humans are averaging 40%. Same technology. Nearly double the output. The kicker: only 20% of companies are in the 71% group. A few things that stood out from the actual data: A supermarket replaced its entire buying process with AI - waste down 40%, stockouts down 80%, profit margin doubled A security team went from 1,500 alerts/month to 40,000 with the same headcount Stanford identified 3 conditions required before agentic AI works: high-volume tasks, clear success criteria, and recoverable errors Most companies apparently can't name all three for their current setup. Full report here if you want to dig into the numbers: https://digitaleconomy.stanford.edu/app/uploads/2026/03/EnterpriseAIPlaybook_PereiraGraylinBrynjolfsson.pdf Here is a full breakdown with all the data if you want to dig deeper: https://youtu.be/JePxda9ZGQE What's the AI setup at your company - closer to the 40% group or the 71% group?

1d ago

---

**[Making an AI companion that degrades over time](https://www.reddit.com/r/artificial/comments/1texbv6/making_an_ai_companion_that_degrades_over_time/)**

I am a student at Umeå University in Sweden, currently writing my Master's thesis with a focus on AI companions. My study aims to suggest new ways of helping people who want to stop using AI companions but, for whatever reason, to do it cant bring themselves to do it. The goal is to inform the design of future AI technologies. For those who wish to receive more information, please feel free to contact me, Sahand Salimi In this part, you will be seeing a simulation of the same conversation between an AI companion and a user happen across three different times with an AI companion, with the AI companion having degraded in different aspects, and answer a few questions. I am super interested in how you, a user or ex-user, find AI companions and how you would react to it degrading over time, what type of AI companion you have used in the past, what type of AI companion you use currently, reasons for your use, and your frustrations with AI companions. You have been invited to share your unique life experiences; no special background or training is needed. Your answer is completely anonymous and will only be used for this study. Also, I am following GDPR standards and our university's guidelines. You can see them here: umu.se/gdpr Link to survey It's important to note that this study is not studying, diagnosing, or prescribing clinical addiction or treatment; instead, the goal is to inform the design of future AI technologies.

9h ago

---

**[I have figured out a way to run every memory system out there on one platform](https://www.reddit.com/r/artificial/comments/1texg6u/i_have_figured_out_a_way_to_run_every_memory/)**

But is there an industry need for it ... It's smth like vlc media player of memory systems ... My team thinks it's hard to make money from it or its hard to sell ... What do y'all think In this system it's like you can fetch like zep for your temporal needs , store like letta if needed , traverse like mempalace or hindsight etc all in one place Thoughts?

9h ago

---

**[Would AI make future game difficulty better?](https://www.reddit.com/r/artificial/comments/1telhki/would_ai_make_future_game_difficulty_better/)**

I was thinking that as AI and basically neural nets, couldn't AI in video games be soon as a baseline feature. You can tell it how difficult to be, as you play it learns how to match the difficulty. You could even command it to play at various difficulties different on days. I was just thinking like we have these starcraft AIs, but like what if in a Heros of might and magic, you could have an AI that you could describe how to play, how aggressive, and in general it could then implement that level. "I want a slight challenge with me most likely winning 60% of the time" and it could understand how to change it's strategy to that. This would be nice because in a lot of strategy games, the harder difficulties just give the AI more resources for free. Would be nice if Civ would just put in a LLM, image you played vs an AI that read up how the person actually acted.

18h ago

---

**[We compiled 42 of the Generative & Agentic AI interview questions (and how to actually answer them).](https://www.reddit.com/r/artificial/comments/1tew06b/we_compiled_42_of_the_generative_agentic_ai/)**

Hey Everyone, The AI engineering job market has shifted massively in the last 6 months. Interviewers are no longer just asking "how does a transformer work?" or "how do you write a good prompt?" They want to know if you can architect production-grade multi-agent systems, prevent RAG hallucinations, and manage state across LLM calls. I’ve been building a visual learning sandbox for multi-agent workflows (agentswarms.fyi), and today I just launched a completely free AI Interview Prep Module inside it. I compiled 42 top interview questions specifically for GenAI and Agentic AI roles. But instead of just giving a generic answer, the module breaks down the "Standout Answer" and teaches you the mental model of how to answer it like a senior architect. Here are two examples from the list: Question 1: When would you use a Multi-Agent Swarm instead of a single LLM with multiple tools? ❌ The average answer: "When the task is too complex, multiple agents are better than one." ✅ The standout answer: "You use a swarm to prevent context dilution and enforce the Principle of Least Privilege. If you give one 'God Agent' 15 tools and a 4k-word system prompt, its reliability drops and hallucination risk spikes. By routing to specialized sub-agents with narrow instructions (e.g., separating the 'Data Extraction Agent' from the 'Customer Chat Agent'), you isolate failure points and allow for parallel execution." Question 2: How do you handle hallucinations in a financial RAG pipeline? ❌ The average answer: "I would lower the temperature to 0 and give it a better system prompt." ✅ The standout answer: "I would decouple data extraction from text generation. I'd use a deterministic node or a strict JSON-enforced agent to only extract the hard numbers from the retrieved context. Then, I would pass that structured data to a separate Synthesis Agent. Finally, I'd implement an 'LLM-as-a-judge' evaluation loop before returning the final output to the user." What's in the full list? The 42 questions cover: RAG Architecture & Vector Databases Agentic Routing (ReAct vs. Planner-Executor) Evaluation metrics for non-deterministic outputs Security (Prompt injection prevention in multi-agent loops) You can read through all 42 questions, answers, and the "how to answer" breakdowns right in the dashboard here: https://agentswarms.fyi/interview-questions For those of you who have interviewed for AI Engineering roles recently, what is the hardest system design question you've been asked? I'd love to add it to the list.

10h ago

---

**[Your AI agent is one poisoned webpage away from doing something catastrophic](https://www.reddit.com/r/artificial/comments/1tf7841/your_ai_agent_is_one_poisoned_webpage_away_from/)**

If your agent browses the web, reads emails, or pulls from a database — any of that content can contain hidden instructions that hijack it. This isn’t theoretical. It’s happening in production right now. A webpage footer tells your agent to forward credentials. An email signature tells it to ignore its guidelines. A retrieved document tells it to change behavior. The model has no idea the content isn’t a legitimate instruction. The fix isn’t better prompt filtering. It’s source-aware authority enforcement. Every content chunk should carry a trust level. Webpages, emails, tool outputs — zero instruction authority. They can provide data. They cannot tell your agent what to do. That’s what Arc Gate does. It sits between your app and your LLM and enforces instruction-authority boundaries at the proxy level. When untrusted content tries to become an instruction source, it gets blocked or sandboxed before the model ever sees it. One line to try it: from langchain\_arcgate import ArcGateCallback from langchain\_openai import ChatOpenAI llm = ChatOpenAI(callbacks=\[ArcGateCallback(api\_key="demo")\]) Live red team environment: https://web-production-6e47f.up.railway.app/break-arc-gate GitHub: https://github.com/9hannahnine-jpg/arc-gate Looking for teams actively deploying agents who want to test this on real workloads. Free access in exchange for feedback.​​​​​​​​​​​​​​​​

3h ago

---

---

## Google News: "ai"

**[Microsoft AI chief gives it 18 months—for all white-collar work to be automated by AI](https://fortune.com/article/why-microsoft-ai-chief-mustafa-suleyman-predicts-ai-automation-18-months/)**

Mustafa Suleyman believes current AI computational power will only accelerate, disrupting every kind of work you do “sitting down at a computer.”

Fortune • 12h ago

---

**[OpenAI and Malta partner to bring ChatGPT Plus to all citizens](https://openai.com/index/malta-chatgpt-plus-partnership/)**

OpenAI and Malta partner to expand AI access, offering ChatGPT Plus and training to help citizens build practical AI skills and use AI responsibly.

OpenAI • 14h ago

---

**[India Missed Out on AI and Now Its Run as Market Darling May Be Over](https://www.bloomberg.com/news/articles/2026-05-17/india-missed-out-on-ai-and-now-its-run-as-market-darling-may-be-over)**

Bloomberg.com • 1h ago

---

**[He’s king of the AI boom. Why do former colleagues say he can’t be trusted?](https://www.washingtonpost.com/technology/2026/05/16/elon-musk-trial-against-sam-altman-renews-questions-about-his-honesty/)**

Testimony in a case brought by Elon Musk has given new force to persistent questions about the trustworthiness of OpenAI’s CEO Sam Altman.

The Washington Post • 9h ago

---

**[I used AI to help market my bagel shop. Then the one-star reviews came in.](https://www.businessinsider.com/bagel-shop-owner-removes-ai-social-media-marketing-2026-5)**

Adam Jones tried using AI to edit the social media posts for Myers' Bagels. After customer outcry, he apologized — but isn't anti-AI.

Business Insider • 16h ago

---

**[Opinion | What A.I. Kant Do](https://www.nytimes.com/2026/05/16/opinion/ai-liberal-arts.html)**

The New York Times • 14h ago

---

**[Pershing Square Backs Microsoft As AI Expansion Divides Major Investors](https://finance.yahoo.com/markets/stocks/articles/pershing-square-backs-microsoft-ai-161232060.html)**

Bill Ackman's Pershing Square fund has taken a major new position in Microsoft (NasdaqGS:MSFT), going public with the stake as other large investors such as TCI and the Gates Foundation have been reducing their holdings. The move comes as Microsoft ramps up its AI efforts beyond OpenAI, including interest in larger AI startup acquisitions, an expanded partnership with OneStream in enterprise finance, and visible traction for new AI products. Ackman cites Azure, Microsoft 365, evolving AI...

Yahoo Finance • 9h ago

---

**[Pity the poor AI data centers facing ‘discrimination’ | Arwa Mahdawi](https://www.theguardian.com/commentisfree/2026/may/16/pity-the-poor-ai-datacenters-facing-discrimination)**

The centers are diverting much-needed resources from regular people. Local resistance has the industry playing defense

The Guardian • 12h ago

---

**[National Cyber Director Sean Cairncross is leading the effort to wrangle hyper-advanced AI. Some worry he’s not up to the task.](https://www.politico.com/news/2026/05/16/sean-cairncross-ai-mythos-expertise-00925336)**

Politico • 7h ago

---

**[2028: Two scenarios for global AI leadership](https://www.anthropic.com/research/2028-ai-leadership)**

Our views on the AI competition between the US and China.

Anthropic • 2d ago

---

---

## HackerNews: "ai"

**[I believe there are entire companies right now under AI psychosis](https://news.ycombinator.com/item?id=48153379)**

⬆️ 1873 • 💬 1057 • 1d ago • [X (formerly Twitter)](https://twitter.com/mitchellh/status/2055380239711457578)

---

**[RTX 5090 and M4 MacBook Air: Can It Game?](https://news.ycombinator.com/item?id=48137145)**

What if you could strap a full desktop GPU to your MacBook Air? Turns out, you can.

⬆️ 688 • 💬 177 • 2d ago • [Scott's Blog](https://scottjg.com/posts/2026-05-05-egpu-mac-gaming/)

---

**[AI is making me dumb](https://news.ycombinator.com/item?id=48139148)**

It's so god damn tempting to use AI to write. Whether it is articles, code, or documents. I feel like using AI is diminishing my ability to write myself.

...

⬆️ 541 • 💬 302 • 2d ago • [James Pain's Weblog](https://jpain.io/god-damn-ai-is-making-me-dumb/)

---

**[Amazon workers under pressure to up their AI usage are making up tasks](https://news.ycombinator.com/item?id=48148337)**

In a new report, employees say Amazon tracks their consumption of 'AI tokens'—and they've been creating unproductive AI agents just to eat them up.

⬆️ 381 • 💬 424 • 1d ago • [Fast Company](https://www.fastcompany.com/91541586/amazon-workers-pressured-to-up-ai-use-extraneous-tasks)

---

**[Frontier AI has broken the open CTF format](https://news.ycombinator.com/item?id=48157559)**

Why frontier AI has broken the open CTF format, hollowed out the scoreboard, and made competitive CTF performance a weaker signal than it used to be.

⬆️ 337 • 💬 325 • 18h ago • [kabir.au](https://kabir.au/blog/the-ctf-scene-is-dead)

---

**[Ontario auditors find doctors' AI note takers routinely blow basic facts](https://news.ycombinator.com/item?id=48142188)**

60% of evaluated AI Scribe systems mixed up prescribed drugs in patient notes, auditors say

⬆️ 308 • 💬 138 • 2d ago • [theregister](https://www.theregister.com/ai-ml/2026/05/14/ontario-auditors-find-doctors-ai-note-takers-routinely-blow-basic-facts/5240771)

---

**[Details of the Daring Airdrop at Tristan Da Cunha](https://news.ycombinator.com/item?id=48144380)**

More details and pictures have come in of the intrepid airdrop of urgent medical support sent to Tristan by the UK Government on the 9th May 2026.

⬆️ 264 • 💬 102 • 1d ago • [tristandc.com](https://www.tristandc.com/government/news-2026-05-11-airdrop.php)

---

**[Access to frontier AI will soon be limited by economic and security constraints](https://news.ycombinator.com/item?id=48143284)**

Soon, access to frontier AI will be scarce and selective

⬆️ 221 • 💬 215 • 2d ago • [writing.antonleicht.me](https://writing.antonleicht.me/p/cut-off)

---

**[The AI zombification of universities](https://news.ycombinator.com/item?id=48139355)**

“And so perfect parallel constructions fill the lecture halls, the take-home tests, the school newspapers, and perhaps even the idiom of student chatter.”

⬆️ 193 • 💬 216 • 2d ago • [thenewcritic.com](https://www.thenewcritic.com/p/the-great-zombification)

---

**[US is starting to see heavy job losses in roles exposed to AI](https://news.ycombinator.com/item?id=48162354)**

⬆️ 139 • 💬 227 • 7h ago • [bloomberg.com](https://www.bloomberg.com/news/articles/2026-05-15/us-is-starting-to-see-heavy-job-losses-in-roles-exposed-to-ai)

---

---

## YouTube Videos: "ai"

**[AI Feud just hit a strange new low](https://www.youtube.com/watch?v=PiFKkKL29jc)**

Become a member! ✓ https://www.youtube.com/channel/UCahJ9IsvXnaQiuNyWQSkrkw/join ⭐ Support independent daily news ...

📺 Chris Norlund

👁️ 69K • 👍 4K • 💬 1K • ⏱️ 19:38 • 10h ago

---

**[AI Trust Is Collapsing. The Industry Is DELUSIONAL.](https://www.youtube.com/watch?v=FwRB_0XPICs)**

Head to https://betterhelp.com/infographics to get 10% off your first month with our sponsor, BetterHelp. Therapy can be a ...

📺 The Infographics Show

👁️ 136K • 👍 5K • 💬 1K • ⏱️ 19:17 • 10h ago

---

**[You’re Not Behind (Yet): Learn AI Agents in 13 Minutes](https://www.youtube.com/watch?v=P5sKKnWCvzk)**

Subscribe to my newsletter → https://www.sandeepswadia.com/newsletter Most people still use AI like a better search box, but the ...

📺 theMITmonk

👁️ 196K • 👍 6K • 💬 152 • ⏱️ 13:10 • 2d ago

---

**[Here&#39;s What Nobody&#39;s Telling You About AI Data Centers | Ep. 1780](https://www.youtube.com/watch?v=wEm1ZpL1PAg)**

Data centers are popping up everywhere, and there are some major issues that we need to discuss. Ep. 1780 -- -- -- LIKE ...

📺 Matt Walsh

👁️ 188K • 👍 10K • 💬 3K • ⏱️ 46:13 • 2d ago

---

**[The AI race is a lie](https://www.youtube.com/watch?v=NeutZWud2Ng)**

Become a member! ✓ https://www.youtube.com/channel/UCahJ9IsvXnaQiuNyWQSkrkw/join ⭐ Support independent daily news ...

📺 Chris Norlund

👁️ 91K • 👍 6K • 💬 1K • ⏱️ 13:30 • 2d ago

---

**[AI Town Experiment Goes DOWN IN FLAMES](https://www.youtube.com/watch?v=5I2NpNnNiNM)**

Krystal, Ryan, Emily and Griffin discuss the downfall of an AI experimental town. Sign up for a PREMIUM Breaking Points ...

📺 Breaking Points

👁️ 93K • 👍 4K • 💬 582 • ⏱️ 12:40 • 1d ago

---

**[AI News: Impressive New Model From Unexpected Company](https://www.youtube.com/watch?v=Oy7tzmfbl64)**

Here's the AI News you probably missed this week. Stop choosing between performance and budget and start building today with ...

📺 Matt Wolfe

👁️ 60K • 👍 2K • 💬 169 • ⏱️ 33:09 • 1d ago

---

**[Microsoft’s New AI Beats Mythos And Shocks OpenAI](https://www.youtube.com/watch?v=idNpTUrr3r0)**

Try Higgsfield Supercomputer here: https://higgsfield.ai/s/super-computer-airevolutionx-RpneRv Microsoft just revealed MDASH, ...

📺 AI Revolution

👁️ 34K • 👍 1K • 💬 56 • ⏱️ 14:53 • 1d ago

---

**[Anthropic just admitted AI is bullsh*t](https://www.youtube.com/watch?v=juHv_Vi4giU)**

It's time to deploy yourself in the forward direction. https://x.com/@atmoio https://atmoio.substack.com ...

📺 Mo Bitar

👁️ 198K • 👍 11K • 💬 2K • ⏱️ 10:37 • 1d ago

---

**[There is No AI Bubble.](https://www.youtube.com/watch?v=jSWfHCiM1YU)**

GET 70% OFF PROTON VPN AT http://www.protonvpn.com/artchad Support me on STACKED, a better and more creator friendly ...

📺 Art Chad

👁️ 47K • 👍 4K • 💬 1K • ⏱️ 22:01 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)**

*OpenBMB*

MiniCPM-V 4.6 is an ultra-efficient, pocket-sized multimodal LLM for edge deployment, excelling in image and video understanding with mixed visual token compression. It offers strong multimodal capabilities comparable to larger models while achieving superior computational efficiency and broad mobile platform support.

`image-text-to-text` `1.3B`

⬇️ 28,627 • ❤️ 643 • 14h ago

---

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 875,370 • ❤️ 1,031 • 8d ago

---

**[supertonic-3](https://huggingface.co/Supertone/supertonic-3)**

*Supertone*

Supertonic 3 is a fast, on-device, multilingual text-to-speech model supporting 31 languages with ONNX Runtime for local inference. It offers high accuracy, low latency, and a compact size, suitable for applications requiring efficient, cloud-independent speech synthesis.

`text-to-speech`

⬇️ 16,496 • ❤️ 308 • 10d ago

---

**[HiDream-O1-Image](https://huggingface.co/HiDream-ai/HiDream-O1-Image)**

*HiDream.ai*

HiDream-O1-Image is a unified transformer-based image generation model capable of text-to-image, image editing, and subject-driven personalization at resolutions up to 2048x2048. It features a pixel-level unified transformer architecture without external VAEs or disjoint text encoders, enabling high-fidelity generation and precise control.

`image-text-to-image` `8.8B`

⬇️ 13,587 • ❤️ 361 • 1d ago

---

**[Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-27B-MTP-GGUF is a 27B parameter vision-language model optimized for efficient inference with MTP speculative decoding, supporting up to 1M+ token context. It excels at agentic coding, reasoning, and tool-calling, making it suitable for complex development workflows and iterative coding tasks.

`image-text-to-text` `27.3B`

⬇️ 133,815 • ❤️ 199 • 12h ago

---

**[ZAYA1-8B](https://huggingface.co/Zyphra/ZAYA1-8B)**

*Zyphra*

ZAYA1-8B is an efficient Mixture-of-Experts LLM (760M active params) excelling in mathematical and coding tasks, competitive with larger models. It's suitable for on-device deployment and high-performance inference.

`8.8B`

⬇️ 143,806 • ❤️ 512 • 5d ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 2,967,518 • ❤️ 3,996 • 10d ago

---

**[Qwen3.6-35B-A3B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-35B-A3B-MTP-GGUF is a 35B parameter vision-language model optimized for efficient inference via MTP speculative decoding, supporting agentic coding and long context lengths up to 1M tokens.

`image-text-to-text` `35.5B`

⬇️ 124,082 • ❤️ 182 • 12h ago

---

**[Anima](https://huggingface.co/circlestone-labs/Anima)**

*CircleStone Labs*

Anima is a 2 billion parameter text-to-image diffusion model specializing in anime and non-photorealistic artistic styles. It excels at generating illustrations and artistic images, with key capabilities including high-resolution output (up to 1536^2) and compatibility with ComfyUI workflows, making it ideal for digital artists and anime enthusiasts.

⬇️ 501,808 • ❤️ 1,353 • 2d ago

---

**[Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)**

*froggeric*

Provides fixed Jinja chat templates for Qwen 3.5 & 3.6 models, resolving issues with tool calling, KV cache hit rates, and agentic loop stability for improved conversational AI and tool interaction.

⬇️ 0 • ❤️ 245 • 11h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 73 • 💬 3 • ⭐ 76,088 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://huggingface.co/papers/2512.10971)**

*Tianyu Fan, Yuhao Yang, Yangqin Jiang et al. (6 authors)*

AI-Trader presents the first fully automated live benchmark for evaluating large language models in financial decision-making across multiple markets with autonomous information processing.

▲ 6 • 💬 0 • ⭐ 17,517 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10971) • [💻 code](https://github.com/HKUDS/AI-Trader) • [🔗 project](https://ai4trade.ai/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 35 • 💬 3 • ⭐ 25,149 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 20 • 💬 3 • ⭐ 11,582 • 29d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[Pixal3D: Pixel-Aligned 3D Generation from Images](https://huggingface.co/papers/2605.10922)**

*Dong-Yang Li, Wang Zhao, Yuxin Chen et al. (8 authors)*

🏢 ARC Lab, Tencent PCG

Pixal3D introduces a pixel-aligned 3D generation approach that addresses fidelity issues in 3D asset creation by establishing direct pixel-to-3D correspondences through back-projection conditioning.

▲ 27 • 💬 3 • ⭐ 798 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2605.10922) • [💻 code](https://github.com/TencentARC/Pixal3D) • [🔗 project](https://ldyang694.github.io/projects/pixal3d/)

---

**[SANA-Video: Efficient Video Generation with Block Linear Diffusion
  Transformer](https://huggingface.co/papers/2509.24695)**

*Junsong Chen, Yuyang Zhao, Jincheng Yu et al. (20 authors)*

🏢 NVIDIA

SANA-Video, a small diffusion model, efficiently generates high-resolution, high-quality videos with strong text-video alignment using linear attention and a constant-memory KV cache, achieving competitive performance at a lower cost and faster speed.

▲ 48 • 💬 2 • ⭐ 5,652 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.24695) • [💻 code](https://github.com/NVlabs/Sana) • [🔗 project](https://nvlabs.github.io/Sana/Video)

---

**[AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation](https://huggingface.co/papers/2605.13724)**

*Yuchao Gu, Guian Fang, Yuxin Jiang et al. (7 authors)*

🏢 NVIDIA

AnyFlow introduces a novel any-step video diffusion distillation framework that improves upon consistency distillation by optimizing full ODE sampling trajectories through flow-map transition learning and backward simulation techniques.

▲ 87 • 💬 1 • ⭐ 249 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2605.13724) • [💻 code](https://github.com/NVlabs/AnyFlow) • [🔗 project](https://nvlabs.github.io/AnyFlow/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 162 • 💬 2 • ⭐ 63,321 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 78 • 💬 7 • ⭐ 73,749 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 114 • 💬 10 • ⭐ 9,492 • 13d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

---

## GitHub Repositories: "ai"

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 13.0k • 🔱 3.0k • 19d ago

---

**[op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill)**

AI-agent Skill for generating polished HTML slide decks: editorial magazine and Swiss layouts, image prompts, social covers, and a WebGL/low-power presentation runtime.

`HTML` `ai-agent` `claude-code` `codex` `html-deck` `image-generation`

⭐ 9.2k • 🔱 754 • 22h ago

---

**[crynta/terax-ai](https://github.com/crynta/terax-ai)**

Lightweight (7MB) AI terminal emulator (ADE) built in Rust & Tauri & React

`TypeScript` `agents` `ai` `code-editor` `linux` `macos`

⭐ 3.4k • 🔱 342 • 9h ago

---

**[esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix)**

DeepSeek-native AI coding agent for your terminal. Engineered around prefix-cache stability — leave it running.

`TypeScript` `agent` `agent-framework` `ai-agent` `ai-coding` `cli`

⭐ 3.3k • 🔱 179 • 28m ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 3.1k • 🔱 887 • 7h ago

---

**[earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad)**

A collection of agent skills for CAD, robotics and hardware design

`JavaScript` `3mf` `agents` `ai` `ai-agents` `build123d`

⭐ 2.9k • 🔱 349 • 2h ago

---

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 2.5k • 🔱 287 • 10h ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.3k • 🔱 153 • 36m ago

---

**[cosmicstack-labs/mercury-agent](https://github.com/cosmicstack-labs/mercury-agent)**

Soul-driven AI agent with permission-hardened tools, token budgets, and multi-channel access. Runs 24/7 from CLI or Telegram.

`TypeScript` `ai-agent` `ai-assistant` `llm`

⭐ 2.2k • 🔱 231 • 6d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.1k • 🔱 322 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
