---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-10-05T15:08:17.011052+00:00'
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

**Last Updated:** October 05, 2026 at 15:08 UTC  
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

**[I built an app where you ask about any moment in history and it turns it into a fully researched podcast you can interrupt](https://www.reddit.com/r/artificial/comments/1wy8a9z/i_built_an_app_where_you_ask_about_any_moment_in/)**

History is something I'm quite passionate about and at work I have experience with software development and LLMs. So I thought how can I bring these things together and built something that I would actually use. This is the results of a few months of hard work! You type any topic, moment or person. About 1 minute later, two (or one) hosts are telling you the story, researched with sources and paired with artwork that follows along. They also remember what you've listened to in the past and can refer to it. At the end there's also a optional quiz to test what you learned! My favorite part: you can interrupt them. Got a question halfway through? Just ask. They answer it and then pick the story back up. Basically a podcast you can talk back to. They also remember what you've listened to before and will bring it up. It doesn't just make things up and hope. Before a word of the script gets written, it researches the topic on the web and checks the key dates, names and numbers against real sources. And when those sources disagree (which in history is constantly), the hosts tell you that instead of quietly picking a side. Every episode links what it used so you can dig in yourself. It's not one model doing everything. I ran bake-offs between GPT, Claude and Gemini models and picked a winner for each job: research and planning, writing the script, picking artwork, voices, quiz, etc.... The differences were bigger than I expected. Some models write great dialogue but plan poorly, some are the other way round, and cost varies a lot. Currently supports 6 languages! Looking for feedback really and to see if this is worth continuing down this rabbit hole You can try it without an account here: historai.ca/

1h ago

---

**[The top 50 AI researchers by citations](https://www.reddit.com/r/artificial/comments/1wxm1vq/the_top_50_ai_researchers_by_citations/)**

How many on the list did you know? Obviously one paper like Attention is All You Need (278k citations) can influence a lot - all the authors are on the list. But still interesting imo. More context: https://www.turingtree.com/top-50

21h ago

---

**[Court throws out killer’s sentence after judge said he ‘loved’ AI video of slain man](https://www.reddit.com/r/artificial/comments/1wy43z7/court_throws_out_killers_sentence_after_judge/)**

The Arizona Court of Appeals tossed a road rage killer’s sentence after determining that the judge’s consideration of the AI video was “fundamentally unfair.”

🔗 [NBC News](https://www.nbcnews.com/news/us-news/sentence-vacated-ai-video-dead-victim-rcna601457) • 5h ago

---

**[Half of surveyed UK novelists fear AI could replace their work entirely](https://www.reddit.com/r/artificial/comments/1wxv3km/half_of_surveyed_uk_novelists_fear_ai_could/)**

For many British novelists, the threat from artificial intelligence reaches beyond the manuscript on their desk. It also touches the freelance assignments that pay their bills, their ownership of published work, and their connection with readers. A University of Cambridge report found that 51% of participating published novelists believed AI would likely replace their fiction-writing work entirely. Another finding was more immediate: 39% said generative AI had already hurt their income. Some 85% expected their future earnings to decline because of it. Published in, The Impact of Generative AI on the Novel examined experiences across British fiction. Clementine Collett, a BRAID UK Research Fellow at Cambridge’s Minderoo Centre for Technology and Democracy, led the research. The report was published in association with the Institute for the Future of Work.

🔗 [The Brighter Side of News](http://thebrighterside.news/post/half-of-surveyed-uk-novelists-fear-ai-could-replace-their-work-entirely) • 14h ago

---

**[Long-running agents: is the bottleneck the model or the scaffolding around it?](https://www.reddit.com/r/artificial/comments/1wy20j4/longrunning_agents_is_the_bottleneck_the_model_or/)**

Something I keep noticing with agent setups: every individual step is easy for the model, but the full chain still falls apart on long tasks. I think it comes down to three things: Error compounding. At 95% accuracy per step, a 20-step chain only succeeds about a third of the time (0.95^20 is roughly 0.36). Small errors stack up fast. Context pollution. After enough tool calls, the context is full of old outputs, dead ends and failed attempts, and the model slowly loses track of the original goal. Weak self-correction. When a step goes wrong, the model usually keeps building on top of it instead of backing up and fixing it. What I'm unsure about is where the real fix comes from. One camp says it's mostly better models. The other says a well-designed loop (checkpoints, verifier steps, state stored outside the context window) matters more than the model itself. Curious what people here have seen in practice: Do you keep the full history in context, or summarize/prune as you go? Has a separate critic or verifier model actually helped, or does it just add latency and cost? At what point in a task do your agents usually start breaking, and what actually fixed it for you? Would love to hear what's worked and what hasn't.

8h ago

---

**[If nothing else, LLMs seem to be getting humour a bit better.](https://www.reddit.com/r/artificial/comments/1wy3z8l/if_nothing_else_llms_seem_to_be_getting_humour_a/)**

This one actually had me laughing out loud.

5h ago

---

**[Plagiarism checker= Genius](https://www.reddit.com/r/artificial/comments/1wxqvl6/plagiarism_checker_genius/)**

Whoever invented the AI plagiarism checker is a genius. Why wait for papers to be published online when you can get people to upload college essays and other publications in an effort to detect AI usage. The models must be getting a lot of data from colleges and schools

17h ago

---

**[China’s AI Safety Money Problem](https://www.reddit.com/r/artificial/comments/1wy92jj/chinas_ai_safety_money_problem/)**

🔗 [open.substack.com](https://open.substack.com/pub/chinatalk/p/chinas-ai-safety-money-problem?r=a7orj&utm_campaign=post&utm_medium=email) • 1h ago

---

**[How do AIs actually collect my sensitive information?](https://www.reddit.com/r/artificial/comments/1wxzgva/how_do_ais_actually_collect_my_sensitive/)**

I dont use the google ai that much because it generally gives bad info, but a few times I have noticed it "randomly" guesses things, like my age, my name, where I live ect. Whenever I ask the ai it says it has no access to my phones, messages, mic, ect and that it doesn't store chat info session to session. For instance, I just got a new cat a few days ago, I never asked the ai about my cat, or anything related to its name. Then I asked it "why does my cat chase nothing" And it kept referring to my cat by name. When pressed it just said that it randomly pulled that name out of thin Air. My cats name is Julius, I have a very hard time believing it pulled that out of nowhere. So what does it do? Read my texts? Access my mic or what? Because the only person I've even told that I got a cat was my sister in text.

10h ago

---

**[OpenAI cuts ties with 3 researchers over alleged misconduct](https://www.reddit.com/r/artificial/comments/1wxn3ua/openai_cuts_ties_with_3_researchers_over_alleged/)**

The ousters come as top AI researchers wield "extraordinary influence" internally, at the same time that companies face public pressure to increase safety measures

🔗 [LinkedIn](https://www.linkedin.com/news/story/openai-cuts-ties-with-3-researchers-over-alleged-misconduct-7642124/?utm_source=share&utm_campaign=reddit&utm_content=storyline&utm_term=artificial) • 20h ago

---

---

## Google News: "ai"

**[People are asking ChatGPT to help them decide how to vote in the midterms](https://www.npr.org/2026/10/05/nx-s1-5977852/ai-chatbots-midterm-election)**

Voters are already voting in the midterms. This year, some voters are trying something new to get ready for the election: asking AI to help research their ballot and even decide who to vote for.

NPR • 6h ago

---

**[Accept ‘bad things’ in return for benefits of AI, says Sam Altman](https://www.theguardian.com/technology/2026/oct/05/sam-altman-open-ai-chatgpt-benefits-risks)**

Boss of OpenAI calls for a regulatory light touch because of the ‘good stuff’ the technology can deliver

The Guardian • 2h ago

---

**[Sam Altman to Decoded: ‘The world should accept some bad things happening’ for the benefits of AI](https://www.politico.com/news/2026/10/04/sam-altman-decoded-interview-ai-01106217)**

Politico • 18h ago

---

**[Sam Altman says world should accept some risks for AI benefits](https://www.foxnews.com/live-news/ai-super-intelligence-trump-altman-10-05)**

OpenAI CEO Sam Altman says AI’s benefits are worth accepting some risks as President Trump launches a new federal effort focused on U.S. leadership in artificial intelligence.

Fox News • 1h ago

---

**[Court Tosses ​​Sentence After A.I. Video of Victim ‘Forgiving’ His Killer Is Played](https://www.nytimes.com/2026/10/04/us/manslaughter-conviction-overturned-ai-video-statement.html)**

The New York Times • 18h ago

---

**[Lola Vision Systems is trying to make it easier to run AI models on chips](https://techcrunch.com/2026/10/05/lola-vision-systems-is-trying-to-make-it-easier-to-run-ai-models-on-chips/)**

Lola Vision Systems is one of TechCrunch's Battlefield 200 Companies

TechCrunch • 8m ago

---

**[Audible’s New AI Story Feature Raises Unanswered Copyright Questions](https://www.forbes.com/sites/legalentertainment/2026/10/05/audibles-new-ai-story-feature-raises-unanswered-copyright-questions/)**

Forbes • 23m ago

---

**[AI finds bafflingly complex but beautiful symmetrical Venn diagram](https://www.newscientist.com/article/2591415-ai-finds-bafflingly-complex-but-beautiful-symmetrical-venn-diagram/)**

Creating rotationally symmetrical Venn diagrams of increasing size is a long-standing mathematical challenge - now an amateur has used AI to generate the largest ones yet

New Scientist • 25m ago

---

**[Anthropic expected to IPO despite market uncertainty, AI slowdown calls](https://www.cnn.com/2026/10/05/business/anthropic-ipo-stock-market)**

Wall Street is gearing up for Anthropic’s expected mega initial public offering, a major test of investors’ appetite for one of the AI industry’s leading firms. Just weeks ago, its CEO called for an industry-wide slowdown over growing safety concerns.

CNN • 6h ago

---

**[Record labels are in a spin over AI music](https://www.economist.com/business/2026/10/05/record-labels-are-in-a-spin-over-ai-music)**

The Economist • 3h ago

---

---

## HackerNews: "ai"

**[LeCun has "zero concerns" about AI wiping out humanity, recent "rogue" incidents](https://news.ycombinator.com/item?id=49946228)**

The former Meta chief AI scientist shares his take on recent rogue AI incidents and effective altruism, as well as plans for his new company, AMI Labs.

⬆️ 406 • 💬 798 • 1d ago • [Fortune](https://fortune.com/2026/10/01/ai-godfather-yann-lecun-has-zero-concerns-about-human-extinction-says-anthropic-ceo-dario-amodei-is-deuded/)

---

**[OpenAI safety leader quits, warning AI company's culture is 'broken'](https://news.ycombinator.com/item?id=49948332)**

David Robinson joins other insiders in urging industry to take more care over rapidly developing technology

⬆️ 267 • 💬 3 • 1d ago • [the Guardian](https://www.theguardian.com/technology/2026/oct/03/openai-safety-leader-quits-warning-ai-companys-culture-is-broken)

---

**[AI Makes Me Sad](https://news.ycombinator.com/item?id=49934487)**

⬆️ 195 • 💬 243 • 2d ago • [mondobe.com](https://mondobe.com/ai-makes-me-sad)

---

**[Show HN: AI search for every photo and every frame of video on macOS](https://news.ycombinator.com/item?id=49952111)**

Deep AI search for every photo and every frame of video in any folder on macOS - allenv0/SCM

⬆️ 156 • 💬 71 • 1d ago • [GitHub](https://github.com/allenv0/SCM)

---

**[Show HN: Made an open-source Lego AI generator](https://news.ycombinator.com/item?id=49937916)**

Agent tooling for generative LEGO models building, built with Astra and Opus 5.5, powered by Jev - anteloc/ldraw-nova

⬆️ 156 • 💬 50 • 2d ago • [GitHub](https://github.com/anteloc/ldraw-nova)

---

**[Pop!_OS bans AI-generated code from much of its codebase](https://news.ycombinator.com/item?id=49946321)**

⬆️ 118 • 💬 168 • 1d ago • [neowin.net](https://www.neowin.net/news/system76-bans-ai-generated-code-across-many-of-its-cosmic-codebases/)

---

**[Crypto Capture of Foreign Aid](https://news.ycombinator.com/item?id=49936725)**

Founded in 1920, the NBER is a private, non-profit, non-partisan organization dedicated to conducting economic research and to disseminating research findings among academics, public policy makers, and business professionals.

⬆️ 100 • 💬 37 • 2d ago • [NBER](https://www.nber.org/papers/w35655)

---

**[How to scale intent, quality, and artistry with AI [video]](https://news.ycombinator.com/item?id=49951891)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

⬆️ 95 • 💬 38 • 1d ago • [youtube.com](https://www.youtube.com/watch?v=GLvFTMtw4Jk)

---

**[Homa: The end of TCP for AI clusters [video]](https://news.ycombinator.com/item?id=49957117)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

⬆️ 78 • 💬 49 • 19h ago • [youtube.com](https://www.youtube.com/watch?v=eZ8WWZzoaR0)

---

**[US killer's sentence quashed because of AI video of victim shown in court](https://news.ycombinator.com/item?id=49944127)**

The Arizona appeals court ruled that airing an AI message from the dead victim "crossed that line".

⬆️ 76 • 💬 62 • 2d ago • [bbc.com](https://www.bbc.com/news/articles/cwgkvygg5nzvo)

---

---

## YouTube Videos: "ai"

**[Will AI take your job? Or will it transform the way you work? | 60 Minutes](https://www.youtube.com/watch?v=peNzGhlAeZw)**

Some Americans are working to improve artificial intelligence, teaching it the skills and knowledge accrued over the course of a ...

📺 60 Minutes

👁️ 70K • 👍 631 • 💬 186 • ⏱️ 13:16 • 12h ago

---

**[AI Just Exploded: GPT-7 BEL, 99% AGI, Gemini 4 RSI, Alien Mind, JEV](https://www.youtube.com/watch?v=dk-hx4_cqpk)**

AI just had one of its craziest runs yet. A massive leaked OpenAI model called BEL could be the foundation for GPT-7, GPT-6 Astra ...

📺 AI Revolution

👁️ 79K • 👍 979 • 💬 148 • ⏱️ 1:43:41 • 17h ago

---

**[&quot;AI is Already Conscious&quot;: Computer Scientist&#39;s Dire Warning | Dr. Roman Yampolskiy](https://www.youtube.com/watch?v=PUXAdr6y-Bk)**

Link to full episode: https://youtu.be/ebWFexw51qM?si=5W4y2WkHIqse7pie Google fired Blake Lemoine for saying its systems ...

📺 Best of Danny Jones

👁️ 145K • 👍 821 • 💬 440 • ⏱️ 1:00:14 • 1d ago

---

**[OpenAI’s Head of ChatGPT: We’re entering a new era of AI (again) | Tibo Sottiaux](https://www.youtube.com/watch?v=MM-C3JqCXBk)**

Tibo Sottiaux leads ChatGPT and Codex at OpenAI. Under his stewardship, OpenAI has shipped some of its most consequential ...

📺 Lenny's Podcast

👁️ 46K • 👍 764 • 💬 36 • ⏱️ 37:23 • 1d ago

---

**[Recursive&#39;s $670M Bet on Self-Improving AI, Sonnet 5.5 Hits 70%, Elon Co-Leads Pentagon Push EP 299](https://www.youtube.com/watch?v=Blyb1D927pM)**

The mates sit down with Richard Socher to discuss Recursive's $670M bet on self-improving AI, why he puts P(Doom) at zero, the ...

📺 Peter H. Diamandis

👁️ 154K • 👍 2K • 💬 572 • ⏱️ 2:25:50 • 1d ago

---

**[Google Just Changed Its AI Content Guidelines (Unreviewed AI Is Now a Liability)](https://www.youtube.com/watch?v=wxqf9J2Huu0)**

E1187: Google changed its guidance on AI-generated content on October 1, and the new language makes one thing very clear: ...

📺 Edward Sturm

👁️ 16K • 👍 276 • 💬 40 • ⏱️ 13:28 • 17h ago

---

**[Legendary Investor BETS On The AI Crash](https://www.youtube.com/watch?v=EB1thrBaq9c)**

"The Big Short" Investor Michael Burry claims the AI bubble "may burst sooner than later." Cenk Uygur and Ana Kasparian discuss ...

📺 The Young Turks

👁️ 115K • 👍 1K • 💬 424 • ⏱️ 25:14 • 2d ago

---

**[If Humans Only Relied on AI](https://www.youtube.com/watch?v=w1mi0Fu40f0)**

YAEY.

📺 im_siowei

👁️ 1.8M • 👍 30K • 💬 448 • ⏱️ 0:58 • 1d ago

---

**[FULL AI Agents Course for Beginners in 2026! (Become a PRO!)](https://www.youtube.com/watch?v=c6Hxnu4JoOw)**

sponsored Get your 30-day free trial here! https://gohighlevel.com/aimaster Learn to build real AI agents ...

📺 AI Master

👁️ 18K • 👍 187 • 💬 8 • ⏱️ 30:18 • 1d ago

---

**[Did the AI Bubble Just Pop?! Anthropic&#39;s Leaked Numbers are INSANE](https://www.youtube.com/watch?v=8RPI7ENgzL8)**

Thanks To Our Sponsors: Incogni: Take your personal data back with Incogni! Use code IMPACT at the link below and get 60% off ...

📺 Tom Bilyeu

👁️ 174K • 👍 2K • 💬 461 • ⏱️ 56:13 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[clef](https://huggingface.co/Cloudflare/clef)**

*Cloudflare*

Clef is a 27B multimodal model that takes structured typed questions and a state (text, JSON, image, or video) to output probabilities for predefined decision options in a single forward pass, ideal for classification and structured output tasks.

`image-text-to-text` `27.4B`

⬇️ 5,416 • ❤️ 1,338 • 3d ago

---

**[laya](https://huggingface.co/convaiinnovations/laya)**

*Convai Innovations*

Laya is a multilingual, non-autoregressive System 1 decision model that provides typed answers with probabilities in a single forward pass. It's trained with reinforcement learning for honest probability reporting and is ideal for text classification tasks like routing, scoring, and moderation across 100+ languages.

`text-classification` `421.3M`

⬇️ 11,733 • ❤️ 5,205 • 1d ago

---

**[Qwen-Image-2.1-Uncensored-GGUF](https://huggingface.co/abenzerps/Qwen-Image-2.1-Uncensored-GGUF)**

*Ahmet Benzer*

This is an uncensored GGUF quantization of Qwen-Image-2.1 for local text-to-image generation, optimized for use with ComfyUI. It offers various quantization levels for a balance between performance and quality, with Q4_K_M recommended.

`text-to-image` `7.1B`

⬇️ 1,638,838 • ❤️ 3,208 • 7d ago

---

**[Kolibri-1](https://huggingface.co/Aleph-Alpha/Kolibri-1)**

*Aleph Alpha*

Kolibri is a 78B parameter Mixture-of-Experts (MoE) model optimized for German and English, featuring explicit reasoning and tool-calling capabilities. It excels at long-context tasks (up to 1M tokens), multi-step reasoning, RAG, and agentic workflows, offering efficient inference with low active parameters per token.

`text-generation` `78.1B`

⬇️ 2,453 • ❤️ 555 • 2d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a versatile diffusion model capable of generating video from images, text, or other videos, and also handles audio generation and conversion tasks. It offers advanced control and customization for multimedia content creation, with primary use cases in video synthesis and audio manipulation.

`image-to-video`

⬇️ 1,645,444 • ❤️ 6,419 • 2d ago

---

**[clef-flash](https://huggingface.co/Cloudflare/clef-flash)**

*Cloudflare*

Clef-Flash is a 9B multimodal model fine-tuned from Qwen3.5-9B that converts text, JSON, image, or video inputs into structured, typed decisions based on a provided schema. It excels at classification and structured output tasks, returning probabilities for predefined options without free-form text generation.

`image-text-to-text` `9.4B`

⬇️ 8,075 • ❤️ 474 • 3d ago

---

**[Xing4.0-29B-A4B-GGUF](https://huggingface.co/Venastine-Research/Xing4.0-29B-A4B-GGUF)**

*Venastine Research*

Xing4.0-29B-A4B is a 29B parameter LLM optimized for complex engineering tasks, featuring a 256K context window and agent-oriented capabilities for multi-step planning and tool calling. It excels in coding, reasoning, and domain-specific adaptations, supporting various inference frameworks.

`text-generation` `31.2B`

⬇️ 18,863 • ❤️ 391 • 6d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model supporting image and video understanding with native context lengths up to 262K tokens. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and enhanced agent execution capabilities.

`image-text-to-text` `27.8B`

⬇️ 6,758,884 • ❤️ 16,982 • 1mo ago

---

**[VisionHOPE](https://huggingface.co/PSRben/VisionHOPE)**

*Siran Peng*

VisionHOPE provides hierarchical PyTorch vision backbones (T/S/B) pretrained on ImageNet-1K for image classification, COCO for object detection/instance segmentation, and ADE20K for semantic segmentation.

`image-classification`

⬇️ 1,654 • ❤️ 415 • 5d ago

---

**[Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1)**

*Qwen*

Qwen-Image-2.1 is a 7B parameter text-to-image generation and editing model supporting native transparency (RGBA) and versatile editing with up to 10 reference images. It excels at realistic textures, refined aesthetics, and efficient inference for applications like content creation and image manipulation.

`text-to-image` `7.1B`

⬇️ 94,556 • ❤️ 2,972 • 5d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**

*Yu Lin, Yiming Wang, Runyuan Cai et al. (5 authors)*

🏢 Edge0

Mixture-of-experts (MoE) inference on consumer hardware is bounded by weight memory: a 35B-class model is 19.5GB at 4-bit, and sparsity shrinks the compute per token, not the bytes that must be held. Naive offloading to SSD does not help on its own, because layer N+1's experts must be chosen before layer N's output exists, so the reads cannot start early enough to hide behind compute. We present Edge0, a streaming MoE inference engine that closes the gap with a prerouter: a per-layer head predicts the next layer's routing one token ahead, and the prediction is consumed as the routing itself, so the staged expert set equals the routed set and nothing is dropped. An unmerged recovery LoRA, trained on the student path, pays back the quality lost to int4 quantization and routing replacement. On a single 24GB machine, Edge0
  serves a 35B MoE at 20tok/s inside 3GiB of peak active memory, within a few points of its fp16 teacher on average across five public benchmarks. An 8B tier runs on the same framework, and the framework, checkpoints, and adapters are open source.

▲ 22 • 💬 4 • ⭐ 3,015 • 19d ago

[🎓 arXiv](https://arxiv.org/abs/2609.18063) • [💻 code](https://github.com/Edge0-AI/edge0)

---

**[UniMate: One Unified Model to Animate Diverse Skeletons](https://huggingface.co/papers/2609.05415)**

*Linzhan Mou, Jiahui Lei, Zhiyang Dou et al. (7 authors)*

🏢 Princeton University

UniMate is a unified diffusion transformer that generates articulated motion for arbitrary skeletons from text and rigged 3D assets without per-skeleton retraining, using topology-aware attention and a large curated motion dataset.

▲ 22 • 💬 2 • ⭐ 1,394 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2609.05415) • [💻 code](https://github.com/Friedrich-M/UniMate) • [🔗 project](https://linzhanmou.com/unimate/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 149 • 💬 6 • ⭐ 109,817 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[LongCat-Video Technical Report](https://huggingface.co/papers/2510.22200)**

*Meituan LongCat Team, Xunliang Cai, Qilong Huang et al. (11 authors)*

🏢 LongCat

LongCat-Video, a 13.6B parameter video generation model based on the Diffusion Transformer framework, excels in efficient and high-quality long video generation across multiple tasks using unified architecture, coarse-to-fine generation, and block sparse attention.

▲ 43 • 💬 5 • ⭐ 8,952 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.22200) • [💻 code](https://github.com/meituan-longcat/LongCat-Video)

---

**[VisionHOPE: Visual Backbones as Self-Modifying Learning Systems](https://huggingface.co/papers/2609.33325)**

*Siran Peng, Tianshuo Zhang, Tianyu Fu et al. (11 authors)*

🏢 Mininglamp Technology

Visual backbones have evolved from Convolutional Neural Networks (CNNs) with local aggregation to Vision Transformers (ViTs) with global interactions, State-Space Models (SSMs) with input-dependent state transitions, and Test-Time Training (TTT) layers that adapt an inner learner while processing an image. Across this progression, visual computation has become increasingly adaptive to each input, yet the rules governing that adaptation remain largely prescribed by the trained backbone. We introduce VisionHOPE, the first generic visual backbone formulated as a self-modifying learning system, in which what the model remembers and how it learns co-evolve within an image. Building on the self-referential construction of Nested Learning (NL), VisionHOPE realizes this co-evolution through five coupled memories that store content, generate key and value representations, and govern learning rate and retention. These memories evolve jointly as visual context accumulates along each scan. However, directly applying the unconstrained self-referential update to a visual backbone leads to instability. We therefore derive a stability-matched step-size control scheme that combines a soft cap on self-referential injection with a spectral clamp on the retained memory transition, and prove that the resulting memory dynamics are non-expansive along each scan. For two-dimensional feature maps, we adapt NL's chunk formulation by aligning chunks with image rows and columns across four directional scans. The proposed VisionHOPE achieves competitive results on ImageNet-1K, COCO, and ADE20K, establishing self-modifying learning systems as a practical foundation for general-purpose visual backbones. The code is available at https://github.com/PSRben/VisionHOPE.

▲ 321 • 💬 2 • ⭐ 701 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2609.33325) • [💻 code](https://github.com/PSRben/VisionHOPE)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 76 • 💬 1 • ⭐ 86,094 • 37mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 90 • 💬 7 • ⭐ 90,021 • 26mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Raven: The Harness of Harnesses for Composable Agentic Intelligence](https://huggingface.co/papers/2609.33439)**

*EverMind AI*

🏢 EverMind

As large language models advance, AI agents are moving beyond isolated, domain-specific tasks toward long-horizon, cross-domain workflows. This transition exposes two challenges: increasing harness complexity makes manual design difficult to scale, while tighter coupling to specific domains limits the generality of a single harness. The central question thus shifts from how to engineer a stronger harness for one domain to how to autonomously construct specialized harnesses, improve them through experience, and orchestrate them across domains. We introduce Raven, The Harness of Harnesses, an open-source multi-agent ecosystem that automatically constructs and evolves modular harnesses for specific models and domains, treating each executable model--harness pair as a composable unit of intelligence. To support an All-Domain Collaboration Network, its Host Agent decomposes goals, matches subtasks to specialized agents, coordinates execution dependencies, and integrates results, while a host archive and EverOS preserve experience across tasks and Skill Forge makes that experience available as reusable procedures. Our theory establishes sufficient conditions for such composition to expand reliable task coverage beyond that of the available individual agents under a shared resource budget. On complex and long-horizon tasks, Raven significantly outperforms the state-of-the-art agent systems, pushing the frontier of composable agentic intelligence.

▲ 563 • 💬 3 • ⭐ 5,181 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2609.33439) • [💻 code](https://github.com/EverMind-AI/Raven) • [🔗 project](https://raven.evermind.ai/)

---

**[Context Language Models](https://huggingface.co/papers/2609.37725)**

*Rulin Shao, Shannon Zejiang Shen, Junjie Oscar Yin et al. (13 authors)*

🏢 Meta

We introduce Context Language Models (CLMs), language models that natively manage their own context. We implement this by treating the context as a file and allowing the model to make unrestricted updates to this file. This allows the model to learn what is most important to maintain in context, and naturally extends to multi-agent systems where multiple agent contexts coexist as files. Building CLMs zero-shot with existing models outperforms SOTA context management strategies across a variety of tasks: 11.4% higher accuracy with 21.5% fewer FLOPs on BrowseComp-Plus, 5% higher scores with 59% fewer FLOPs on 12-hour EdgeBench, and 65% greater improvement with the same compute on a 24-hour multi-repository agent-swarm task. Moreover, by shifting context management from external harness control to intrinsic model behavior, CLMs naturally enable both in-context and parametric learning of context-management strategies. We show that CLMs can be steered with natural-language instructions evolved through a standard skill-optimization loop, improving held-out accuracy by up to 35.9 points on a context-management task while reducing compute. We also introduce an online reinforcement learning method for CLMs, improving Qwen3.5-9B performance on BrowseComp-Plus by 47.6% while using 12% fewer FLOPs. Finally, we co-design Suffix Cache Reuse for CLM serving, further reducing server-side compute by 35% relative to standard SGLang at matched performance.

▲ 40 • 💬 2 • ⭐ 521 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2609.37725) • [💻 code](https://github.com/facebookresearch/context-language-models) • [🔗 project](https://github.com/facebookresearch/context-language-models)

---

**[RRSI: Regularized Recursive Self-Improvement of Agent Harnesses](https://huggingface.co/papers/2609.24972)**

*Peng Xia, Rujun Han, Zifeng Wang et al. (14 authors)*

🏢 Google

An LLM agent's capability is largely magnified by its harness, namely the prompts, control flow, tooling, memory, and context management surrounding the frozen backbone model. Recent methods increasingly automate this process by iteratively proposing and selecting component-wise edits of an agent harness, practically establishing a form of recursive self-improvement (RSI) at the agent-system level. However, such recursive evolution may overfit by memorizing the training tasks, showing large in-distribution gains that shrink or even vanish on out-of-distribution benchmarks. We introduce Regularized Recursive Self-Improvement of Agent Harnesses (RRSI), which incorporates the principles of regularizations into harness self-improvement by constraining the evolution candidate proposal and selection. The proposer operates with a temporally annealed budget, limiting how many edits a candidate can bundle, and it encourages unexplored trajectories based on evolution history. The selector is equipped with a critic and a pruner: the critic screens benchmark-specific proposals, while the pruner, removes changes that are too small, too expensive, or no longer useful. Together these constraints favor reusable agent mechanisms over benchmark-specific ones or even noises. Across eight benchmarks spanning coding, agentic workspace and engineering design tasks, RRSI gains up to 14.1 points on the split it evolves against and up to 4.7 points on the five out-of-distribution benchmarks, while producing a harness that runs on 30% fewer policy tokens than the unregularized evolution. Code is available at https://github.com/google-research/rrsi and project page is https://regularized-rsi.com/.

▲ 221 • 💬 2 • ⭐ 1,243 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2609.24972) • [💻 code](https://github.com/google-research/rrsi) • [🔗 project](https://regularized-rsi.com/)

---

---

## GitHub Repositories: "ai"

**[zai-org/ZCode](https://github.com/zai-org/ZCode)**

Z.ai's coding agent harness. Powerful, intelligent, extensible.

`TypeScript`

⭐ 7.4k • 🔱 2.3k • 6d ago

---

**[Mak5er/AirCard](https://github.com/Mak5er/AirCard)**

Apple Wallet Card Skinner for iOS 18+ (No Jailbreak Required)

`Swift`

⭐ 6.1k • 🔱 387 • 1d ago

---

**[KKKKhazix/AIHOT](https://github.com/KKKKhazix/AIHOT)**

一个自己找热点、自己写日报的网站框架。把信源和精选标准换成你的，它就是你的行业热点站。

`TypeScript` `ai` `chinese` `content-curation` `daily-digest` `docker-compose`

⭐ 5.9k • 🔱 1.5k • 15h ago

---

**[yi1108/printfilm](https://github.com/yi1108/printfilm)**

PRINTFILM：AI 视频获客与 AI短剧创作平台

`Python`

⭐ 4.1k • 🔱 449 • 11d ago

---

**[CopilotKit/OpenDots](https://github.com/CopilotKit/OpenDots)**

Your always-on AI coworkers that move between text, calls, and Slack.

`TypeScript`

⭐ 3.5k • 🔱 462 • 42m ago

---

**[jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader)**

One AI trade decision every Monad block. Jev on Kuru MON-USDC.

`TypeScript`

⭐ 2.8k • 🔱 530 • 18d ago

---

**[feder-cr/dots](https://github.com/feder-cr/dots)**

Open-source dots for the web: an AI agent with its own browser, one that does not get blocked.

`Python` `ai-agent` `ai-agents` `ai-browser` `anti-detect-browser` `browser-agent`

⭐ 2.6k • 🔱 437 • 1d ago

---

**[yibie/awesome-jev](https://github.com/yibie/awesome-jev)**

A curated list of public projects, integrations, and discussions built on Jev — TypeSafe AI's System One model for typed decisions.

`Python` `awesome` `awesome-list` `jev` `llm`

⭐ 2.1k • 🔱 323 • 14h ago

---

**[kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill)**

A comprehensive logo-design skill for Claude, Gemini CLI, Codex and other AI agents: principles, process, SVG craft, testing tools and a 1,400+ logo reference library.

`HTML` `agent-skills` `branding` `claude` `claude-skills` `codex`

⭐ 1.9k • 🔱 125 • 4d ago

---

**[Mak5er/AirCard-iOS](https://github.com/Mak5er/AirCard-iOS)**

 Apple Wallet card skins and lock screen passcode themes on iOS 27. 

`Swift`

⭐ 1.7k • 🔱 187 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
