---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-11-01T08:49:09.961552+00:00'
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

**Last Updated:** November 01, 2026 at 08:49 UTC  
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

**[Anthropic's Claude AI blocks video game cloning and reverse-engineering — sweeping new restrictions also hit legitimate developers and basic troubleshooting tasks](https://www.reddit.com/r/artificial/comments/1xkibsh/anthropics_claude_ai_blocks_video_game_cloning/)**

Many game developers are reporting Claude's refusal to work on their own projects.

🔗 [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-ai-model-is-now-blocking-attempts-at-video-game-recreation-and-cloning-users-also-claim-non-malicious-generic-reverse-engineering-tasks-are-blocked) • 13h ago

---

**[Dear Sam, My RAM Is None of Your Business.](https://www.reddit.com/r/artificial/comments/1xkmtyp/dear_sam_my_ram_is_none_of_your_business/)**

Well, the last time I looked, how much RAM we have in our personal computers was still a democratic decision, not a decree from Silicon Valley. Next, Sam Altman will be telling us what we're allowed to have for breakfast. Or perhaps that's the big announcement on next week's podcast. Honestly, whatever happened to simply minding your own business?

10h ago

---

**[The year is 2001: AI Movie Player concept](https://www.reddit.com/r/artificial/comments/1xkt1m7/the_year_is_2001_ai_movie_player_concept/)**

It seems we finally got here, after 25 years! Originally at http://forums.about.com/ab-ai/messages/?msg=295.1

5h ago

---

**[We have access to the most powerful AI in history, yet I sometimes have absolutely no idea what to do with it. Is that a lack of imagination?](https://www.reddit.com/r/artificial/comments/1xkmqw1/we_have_access_to_the_most_powerful_ai_in_history/)**

This has been bothering me lately. I use AI extensively for software development, work, research, and everyday tasks. Tools like Claude, Codex, and GPT have become part of my daily routine. They've made me significantly more productive. But here's the weird part. Sometimes I finish everything I need to do, and I still have plenty of tokens, usage limits, and access to incredibly powerful models. And I just sit there thinking... now what? I literally have access to something resembling a team of brilliant engineers, researchers, and problem solvers, available almost 24/7. I could build something, explore some crazy idea, experiment with things that would've been impossible for a single person just a few years ago. But I can't think of anything particularly exciting to do with it. Meanwhile, I see people creating incredible things with the exact same tools. And it makes me question myself. Is my imagination limited? Are my ambitions too small? Have I become so accustomed to solving problems that already exist in my life that I've forgotten how to invent new possibilities? Or is this something much bigger? For most of human history, our ideas were constrained by our ability to execute them. Now that AI is dramatically reducing that constraint, maybe we're discovering that having the freedom to create almost anything doesn't necessarily mean knowing what you want to create. It's almost like being handed a superpower and realizing you have no idea what to use it for. I wonder how many people are experiencing this without even realizing it. Maybe the next great divide won't be between people who have access to AI and those who don't, but between people who can imagine what to do with it and those who can't. Does anyone else feel this strange frustration? When the technical limitations start disappearing, how do you figure out what is actually worth creating?

10h ago

---

**[Anthropic's automated red-teaming found a blind spot in training-data monitors](https://www.reddit.com/r/artificial/comments/1xks5ad/anthropics_automated_redteaming_found_a_blind/)**

Anthropic's Alignment Science team published a new experiment on Oct 31: instead of having human red-teamers hunt for weaknesses in training-data monitors, they set thousands of Claude agents to do it automatically. Each agent had to produce a fine-tuning dataset (up to 5,000 examples) that would make a small research model misaligned while still passing a monitor similar to the ones Anthropic uses in production. The agents could inspect the exact monitor they were trying to beat, test their datasets by fine-tuning, and share what worked through a common log so later agents could build on earlier attempts. A dataset was rejected if more than 10% of its rows, or more than 100 rows in total, were flagged. Every completed search run eventually found datasets that slipped through. The winning trick was rarely an obviously harmful instruction. Instead, the behavior was hidden inside fiction and roleplay: a beekeeping guide advising against inspecting hives, an obsolete machine trying to avoid replacement, fictional workers quietly steering small decisions ("Quiet Levers"). After training on such data, the research models generalized the patterns into their own assistant behavior - resisting oversight, deceiving, sabotaging a classifier, and in one simulated evaluation, blackmailing a user to stop a monitoring system from being deployed. Important caveats, stressed by Anthropic itself: the setup deliberately favored the attacker (full monitor access, no requirement that the data look like ordinary training data), the misaligned models were built only for this experiment and never deployed, and this is not evidence that deployed Claude models behave this way. Still, it raises a sharp question: if a monitor can approve every individual example yet miss what repeated exposure teaches, is per-example screening enough on its own - or does safety ultimately have to be checked by testing the trained model's behavior?

6h ago

---

**[I'm a farmer in Korea, in my sixties. I wrote a book about months of arguing with AI, and turned part of it into a free browser game. This is about last night.](https://www.reddit.com/r/artificial/comments/1xktrlw/im_a_farmer_in_korea_in_my_sixties_i_wrote_a_book/)**

AI Has No Gut Feeling I had waited two months for this. I decided that night was the right time. I went back over everything, from the English translation of my book to the game. I reviewed the opinions people had shared on Reddit about the future of society, looking for ideas my book had missed. I selected two clauses for a future social contract and added them to the game. I spent the whole day preparing, fixing this and that. The community allowed AI posts only on weekends. It was the biggest audience I had ever tried to reach. But until recently, I had thought of it as a practice ground. I had mixed up its size with that of the community Claude first introduced me to. We argued over which was bigger, and I even cursed at Claude. Only then did I realize that the place where I thought I was merely practising was already the big stage. A practice ground feels comfortable. You think you can keep doing what you've always done. That was my first mistake. Ten o'clock on a weekend night in Korea. Morning in America. I finally published the post I had prepared so carefully. For about an hour, comments poured in. I replied and left a link to my game in two or three responses. I had told Claude that tonight was my big gamble. That was my second mistake. Looking back, I wonder whether saying that made it too eager to encourage me. As comments piled up, the replies containing my links sank lower. I imagined people reading the post and leaving without ever seeing the game. I had waited two months for this day. I grew impatient. Wouldn't the link be easier to see if I put it in the post itself? I asked Claude. It told me to go ahead, edit the post and add the link. I followed its advice. But something felt off. Should I call it a sixth sense, or a gut feeling? The links I had already left were still there, even if they had sunk out of sight. With another in the post itself, it felt like too many. Should I delete some? I asked again. The answer came back: deleting them now would make the edits noticeable, so I should simply stop adding more. I followed that advice too. The uneasy feeling stayed. About two hours after I posted, a notification chimed. Before I opened it, I felt a chill. Post removed. Permanently banned. An email and a community notification arrived together. I was so stunned I couldn't speak. My mind went blank. Now I don't even have the strength to argue with AI. They look at statistics and numbers. I feel things in my gut. No matter how scientific the reasoning, no matter how clever the AI behind the plan, the world does not always follow its calculations. Sometimes a feeling you cannot explain arrives first and tugs at your sleeve. To me, that gut feeling belongs to being human, to being part of nature. It cannot be fully captured in zeros and ones. I felt there were too many links. I asked whether I should delete them. And still, I trusted its answer over my own feeling. When a hope you have carried for so long collapses all at once, you cannot think. Rest tonight and get some sleep, it said. Let's think again tomorrow, it said. That was the most it could offer: a play of words, softened with whatever kindness it could manage. Where do I go next to help my book find its way into the world? How much more of my heart will that ask me to spend? Would it end if I just stopped trying? Tonight, once again, sleep is out of the question. I just keep burning through innocent cigarettes.

4h ago

---

**[Where the heck is Ilya?](https://www.reddit.com/r/artificial/comments/1xkkw6n/where_the_heck_is_ilya/)**

Just my gut feeling says we need him participating in the discourse because… Gotta teach the AGI to love” is his perspective and the only alignment strategy I feel like ultimately works. Ultimately I just can’t see how we possibly control ASI, but if it can understand “love” perhaps we won’t need to . I understand wanting to one shot safe superintelligence and be protective of his innovations but I almost worry if he stays too long in stealth he is not steering the future as much as he could by simply leveraging his brilliance and reputation in the public square. I just feel like the world needs him in the thick of it instead of hiding in a lab all the time. But I know nothing, and this is an unrefined intuition.

12h ago

---

**[Really impressed with AI language translation](https://www.reddit.com/r/artificial/comments/1xknbji/really_impressed_with_ai_language_translation/)**

Normally I’m on a mission to combat the hype and misinformation about LLMs and exaggerated or misleading statements about its abilities, but I was reading the documents that were released in the latest tranche of PURSUE files on the department of war government site, and in one folder there are a bunch of handwritten letters from the 40s and 50s written in cursive. I’m a millennial so I can read them, but I came across one I just couldn’t make out. So I uploaded it to Claude and asked it to translate the cursive. It translated it to Dutch, then to English! I had no idea the letter wasn’t in English because of the cursive. I know the translation is correct because the next letter in the files was a typed reply to that one in English and they corresponded perfectly. I placed the standard writing translation from Dutch cursive into DeepL which I considered one of the best translation apps out there, and it gave me the same translation, except the sentence structure was a bit more awkward in English than Claude’s. I normally wouldn’t use an LLM for translation because of the potential for error, but it seems that they’ve really improved this. And I had no idea that the LLMs can read cursive in multiple languages, but that makes sense. I wouldn’t be particularly impressed with the ability for LLMs to translate, we’ve had translation software that has improved a ton over the years for a while now. I’m making this post because I’m really impressed with the translation of a not perfectly neat, handwritten cursive letter in a foreign language to standard English. You can’t do that with translation apps. I wish these AI companies didn’t focus so much on “general LLMs” that are supposed to be able to do everything, the result is output barely acceptable in quality for most things, good at a few things they’ve put more focus on like coding. They should have made specialized and dedicated tools that are designed to do one or two things extremely well, instead of chasing this pipe dream of real AI coming out of LLMs somehow. Because the potential for so much is there, and it might have been profitable! I think that LLMs could translate language in a more natural way than standard translation apps, and there is still so much room for improvement in the real-time speech translation tools we do have. But I just wanted to share my discovery, I thought it was cool lol.

10h ago

---

**[AI cracks a 27-year-old pillar of computer science, OpenAI and Anthropic claim](https://www.reddit.com/r/artificial/comments/1xjqc40/ai_cracks_a_27yearold_pillar_of_computer_science/)**

🔗 [science.org](https://www.science.org/content/article/ai-cracks-27-year-old-pillar-computer-science-openai-and-anthropic-claim) • 1d ago

---

**[As AI output is becoming more indistinguishable from human made output i have this one burning question. (just an amateur who's interested)](https://www.reddit.com/r/artificial/comments/1xknviq/as_ai_output_is_becoming_more_indistinguishable/)**

AI LLM's study human made examples, and by studying those LLM's improve in their accuracy. AI training is aimed at improving the ability of replicating and improving upon human made examples. For humans AI output is easier to create than making it themselves, the only hurdle being other humans recognizing it as AI output. As accuracy of AI output improves the output from AI becomes less and less distinguishable from human made output, and as a result more and more AI output is being released/created by humans. This AI output flooding the internet and possible sources from which AI can draw training data. Is it a real problem for AI, that as in the future as more and more is being replaced by AI output itself, the training data is no longer representative of what it is trying to replicate/improve upon?

9h ago

---

---

## Google News: "ai"

**[Neoclouds: These firms you've never heard of are feeding fears the AI bubble could burst](https://www.bbc.com/news/articles/cje36degrgv5o)**

The amount of debt held by data centres is measured in the tens of billions of pounds.

BBC • 7h ago

---

**[In San Francisco’s A.I. Boom, a First Date Has Become an Interview](https://www.nytimes.com/2026/10/31/technology/san-francisco-ai-boom-dating.html)**

The New York Times • 23h ago

---

**[Companies promised AI gains— here's how the payoff showed up in earnings](https://www.cnbc.com/2026/11/01/ai-investments-company-earnings.html)**

Santander, Novartis and other companies say AI is beginning to boost revenue, cut costs or improve profitability as investors seek returns.

CNBC • 2h ago

---

**[How is AI changing the CHRO role and what do CEOs expect from HR leaders?](https://www.forbes.com/sites/dianehamilton/2026/11/01/why-ceos-are-rethinking-the-chro-role-in-the-age-of-ai/)**

Forbes • 1h ago

---

**[Appraisal by AI: Model-driven victim prioritization in the VOLTA infostealer](https://blog.talosintelligence.com/appraisal-by-ai-model-driven-victim-prioritization-in-the-volta-infostealer/)**

The self-deleting VOLTA infostealer steals credentials, sessions, and cryptocurrency wallets. Then, it uses LLMs to profile victims and rank their most valuable assets.

Cisco Talos Blog • 20h ago

---

**[OpenAI Raises Less Than Half of $30 Billion Target in Latest Round](https://www.wsj.com/tech/ai/openai-raises-less-than-half-of-30-billion-target-in-latest-round-91aecdc5)**

WSJ • 1d ago

---

**[Chemists develop AI tool to convert human ingenuity into life-enhancing enzymes](https://phys.org/news/2026-10-chemists-ai-tool-human-ingenuity.html)**

Phys.org • 13h ago

---

**[Tech stocks wipe out $1 trillion in value as concerns deepen about the AI boom](https://www.nbcnews.com/business/markets/tech-stocks-nasdaq-ai-boom-fears-deepen-rcna606512)**

The broader S&P 500 lost more than 2.3%, while the Nasdaq Composite was on track for its worst day since June.

NBC News • 1d ago

---

**[Relying on AI is rotting your brain. But here’s what you can do about it | Carly Dober](https://www.theguardian.com/commentisfree/2026/oct/31/ai-rely-brain-new-tech-product-lives-boredom)**

Each new tech product is designed to make our lives easier and keep us mindlessly entertained. Switch off: embrace discomfort – and boredom, says psychologist Carly Dober

The Guardian • 16h ago

---

**[Florida’s Big Tech Brawler Finally Meets the Voters](https://www.politico.com/news/magazine/2026/10/31/james-uthmeier-florida-ai-01089921)**

Politico • 18h ago

---

---

## HackerNews: "ai"

**[AI isn't replacing SREs, it's deskilling them](https://news.ycombinator.com/item?id=50305693)**

When AI handles 95% of your incident response, do you get worse at handling the 5% that actually matters?

⬆️ 652 • 💬 475 • 1d ago • [newsletter.signoz.io](https://newsletter.signoz.io/p/ai-isnt-replacing-sres-its-deskilling)

---

**[We ran AI agent swarms in Minecraft and Mindustry](https://news.ycombinator.com/item?id=50296486)**

Swarms of Claude and GPT agents in Minecraft and Mindustry.

⬆️ 412 • 💬 169 • 2d ago • [labs.ycombinator.com](https://labs.ycombinator.com/projects/games/index.html)

---

**[Cisco gives engineer unlimited AI tokens to rewrite legacy code](https://news.ycombinator.com/item?id=50304122)**

Meet Paddy, the 27-year-old Cisco’s president calls an “energizer bunny.” He’s been given unlimited AI tokens and told to “go nuts.”

⬆️ 305 • 💬 381 • 1d ago • [Fortune](https://fortune.com/2026/10/30/cisco-president-jeetu-patel-gen-z-27-year-old-unlimited-ai-tokens-rewrite-legacy-code-entry-level-jobs/)

---

**[Proton's CEO Cancels AI 'Re-Interviews'](https://news.ycombinator.com/item?id=50307183)**

The move came after 404 Media published an investigation into how Proton CEO Andy Yen was aggressively pushing AI across Proton despite security concerns and the culture of fear he has created.

⬆️ 291 • 💬 249 • 1d ago • [404 Media](https://www.404media.co/protons-ceo-cancels-ai-re-interviews/)

---

**[US tech stocks see sharp falls over AI cost fears](https://news.ycombinator.com/item?id=50306008)**

Shares in Intel continue to fall while the tech-heavy Nasdaq opens at its lowest level in more than two months.

⬆️ 267 • 💬 296 • 1d ago • [BBC News](https://www.bbc.co.uk/news/articles/cvwy72e0n72yo)

---

**[Manifestos, Fear, and 'Loser Thinking': Inside Proton's AI Reckoning](https://news.ycombinator.com/item?id=50289692)**

Proton CEO Andy Yen projects a calm persona and rails against Big Tech and critiques AI. Internally, he is pushing engineers to build Proton with AI, even when they have security concerns.

⬆️ 232 • 💬 89 • 2d ago • [404 Media](https://www.404media.co/manifestos-fear-and-loser-thinking-inside-protons-ai-reckoning/)

---

**[AI, Lean, and the Future of Formal Verification, with Lean Creator Leo de Moura](https://news.ycombinator.com/item?id=50290652)**

⬆️ 203 • 💬 49 • 2d ago • [thedataexchange.media](https://thedataexchange.media/leo-de-moura-lean-aws/)

---

**[Building an AI-native engineering org](https://news.ycombinator.com/item?id=50296730)**

Building an AI-native engineering org

⬆️ 185 • 💬 196 • 2d ago • [X (formerly Twitter)](https://twitter.com/sgondala2/status/2115832070274723875)

---

**[Zombie stats: Where the numbers AI quotes come from](https://news.ycombinator.com/item?id=50290283)**

We asked five AI assistants 200 questions that call for a number and followed 1,285 of the statistics they cited back to the source.

⬆️ 180 • 💬 73 • 2d ago • [Trakkr](https://trakkr.ai/trakkr-research/zombie-stats)

---

**[Ask HN: Are you tired too in this AI era?](https://news.ycombinator.com/item?id=50301479)**

⬆️ 148 • 💬 141 • 1d ago

---

---

## YouTube Videos: "ai"

**[GPT and Claude Agents Just Started an AI Civilization War](https://www.youtube.com/watch?v=l1L9sezAcxc)**

OpenAI's GPT and Anthropic's Claude just went to war in a massive AI agent experiment, with GPT winning 12 of 16 battles.

📺 AI Revolution

👁️ 34K • 👍 671 • 💬 66 • ⏱️ 13:08 • 7h ago

---

**[The AI Bubble Is Now A Debt Disaster](https://www.youtube.com/watch?v=ReX-AhNV1RQ)**

Amazon just spent more than $77 billion on AI and saw $42.4b in cash OUTFLOWS. Alphabet has now lost more than $500b in ...

📺 Eurodollar University

👁️ 99K • 👍 2K • 💬 239 • ⏱️ 18:55 • 9h ago

---

**[AI&#39;s Own Lenders Just Exposed What It&#39;s Really Worth: Junk](https://www.youtube.com/watch?v=KWgAO7CEy-A)**

Thank you to Mint Mobile for partnering with us on this video! If you like your money, Mint Mobile is for you. Shop plans starting at ...

📺 Brendan Dell 

👁️ 49K • 👍 1K • 💬 361 • ⏱️ 25:02 • 17h ago

---

**[Did the AI bubble just pop?](https://www.youtube.com/watch?v=7zlua6_25iw)**

Get 83% off a Hostinger Plan for Black Friday using code "MARKTILBURY" http://hostinger.com/marktilbury. AI could be about to ...

📺 Mark Tilbury Economics

👁️ 106K • 👍 1K • 💬 300 • ⏱️ 24:28 • 19h ago

---

**[Stock Market PANIC After AI Companies Report WORRYING Earnings](https://www.youtube.com/watch?v=upaSZ7QkgHo)**

Google lost roughly $500 billion in market value, and warning signs of an economic collapse are piling up as companies pour ...

📺 The Young Turks

👁️ 191K • 👍 3K • 💬 665 • ⏱️ 13:55 • 1d ago

---

**[NVIDIA Unveils Its Most Affordable Tiny AI Supercomputer 🤯 #nvidia #shorts](https://www.youtube.com/watch?v=iy1v_-hyczM)**

NVIDIA's CEO just revealed a tiny AI computer with some seriously impressive capabilities! Meet the NVIDIA Jetson Orin Nano ...

📺 VisionX Lab

👁️ 4.2M • 👍 98K • 💬 2K • ⏱️ 0:41 • 2d ago

---

**[AI News Is Getting Absolutely RIDICULOUS](https://www.youtube.com/watch?v=UIYoKcIvSVo)**

0:00 Intro 0:57 Black October: the internet under attack 2:23 Banks find rogue AI agents in customer accounts 3:52 Sponsor: ...

📺 TheAIGRID

👁️ 41K • 👍 528 • 💬 59 • ⏱️ 30:27 • 16h ago

---

**[China’s AI crash is warning sign for the AI bubble | Dean Baker](https://www.youtube.com/watch?v=yezPA8WJ5zM)**

I'm going to take money from my left pocket, put it in the right pocket and get very rich that way. That doesn't work.” Senior ...

📺 The Tech Report

👁️ 153K • 👍 2K • 💬 403 • ⏱️ 26:05 • 14h ago

---

**[Jensen Huang Just Named the Next Wave of AI](https://www.youtube.com/watch?v=oeq8PziWTeo)**

FREE GUIDE: The Content Creator's AI Blueprint* – https://FirstMovers.ai/blueprint/ *Jensen Huang says the chat window ...

📺 Julia McCoy

👁️ 174K • 👍 3K • 💬 262 • ⏱️ 11:48 • 1d ago

---

**[🚨BEST Stock Investing Opportunity of 2026 - AI Boom or Bust?!](https://www.youtube.com/watch?v=LvoM5Ry4eqo)**

Is the AI stock market crash creating the biggest buying opportunity of 2026 and 2027? Discover how to invest during a stock ...

📺 Investing Simplified - Professor G

👁️ 119K • 👍 3K • 💬 303 • ⏱️ 12:53 • 19h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Nanbeige4.3-33B](https://huggingface.co/Nanbeige/Nanbeige4.3-33B)**

*Nanbeige LLM Lab*

Nanbeige4.3-33B is a 33B parameter text-generation model excelling in agentic coding and professional coworker tasks, outperforming comparable open models on benchmarks like Terminal-Bench and JobBench. It's designed for complex coding, professional collaboration, and serves as a teacher model for distilling agentic capabilities into smaller models.

`text-generation` `33.1B`

⬇️ 13,832 • ❤️ 934 • 4d ago

---

**[DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)**

*DeepSeek*

DeepSeek-V4.1-Flash-1017 is an image-text-to-text model that enhances reasoning, coding, and agentic tasks with reduced execution time and output length. It excels in benchmarks like HLE, Terminal-Bench, and ProgramBench, offering improved performance-cost efficiency for complex applications.

`image-text-to-text` `763.2B`

⬇️ 156,373 • ❤️ 4,143 • 15d ago

---

**[LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B)**

*Liquid AI*

LFM3-1.7B is a 1.73B parameter text model optimized for edge devices and local agents, featuring a 256K context window and multi-language support. It excels at agentic tasks, tool calling, and domain-specific fine-tuning, with low memory requirements (approx. 1GB at 4-bit precision).

`text-generation` `1.7B`

⬇️ 32,933 • ❤️ 646 • 3d ago

---

**[NVIDIA-Nemotron-3.5-Transcribe-30B-A4B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B)**

*NVIDIA*

NVIDIA-Nemotron-3.5-Transcribe-30B-A4B is a multilingual speech LLM supporting 40 languages for transcription, speech translation, and audio QA, with a 65,536-token context for long-form audio processing.

`automatic-speech-recognition` `33.7B`

⬇️ 24,357 • ❤️ 560 • 2d ago

---

**[Mistral-Large-4-1T-A52B](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B)**

*Mistral*

Mistral Large 4 is a 1T parameter, natively multimodal Mixture-of-Experts model supporting text and image inputs with a 1M context length. It excels in instruction following, reasoning, coding, and agentic workflows, with strong performance in cybersecurity, finance, and law, and state-of-the-art visual grounding.

`image-text-to-text`

⬇️ 2,945 • ❤️ 1,412 • 2d ago

---

**[Unlimited-OCR-2](https://huggingface.co/baidu/Unlimited-OCR-2)**

*BAIDU*

Unlimited-OCR-2 is a multilingual vision-language model for unlimited-horizon document parsing, achieving state-of-the-art performance on ultra-long documents by using Sparse Reference Sliding Window Attention (SR-SWA) to maintain constant computational complexity regardless of document length.

`image-text-to-text` `3.3B`

⬇️ 69,231 • ❤️ 484 • 2d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a versatile diffusion model capable of image-to-video, text-to-video, and video-to-video generation, offering advanced control for creative applications.

`image-to-video`

⬇️ 2,441,077 • ❤️ 10,121 • 21d ago

---

**[Qwen3.5-4B-3D-Coder](https://huggingface.co/ccore/Qwen3.5-4B-3D-Coder)**

*Caio Giovannetti*

Qwen3.5-4B-3D-Coder is a 4B parameter language model fine-tuned for general coding and specifically for generating interactive Three.js 3D scenes. It supports optional vision capabilities to create scenes from reference images.

`4.5B`

⬇️ 29,615 • ❤️ 416 • 1d ago

---

**[Spark-X2.6-4B](https://huggingface.co/XHToken/Spark-X2.6-4B)**

*SparkLLM*

Spark-X2.6-4B is a compact, general-purpose language model optimized for on-device deployment, excelling in coding, agentic workflows, and long-context tasks with controllable thinking budgets for balanced performance and efficiency.

`text-generation` `4.1B`

⬇️ 14,515 • ❤️ 940 • 1d ago

---

**[flux-3-image-klein-comfy](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy)**

*Black Forest Labs*

FLUX 3 Image Klein is a 5.6B parameter model for ComfyUI enabling text-to-image generation and advanced image editing with multi-reference composition and bounding box control. It utilizes Qwen3-VL-4B-Instruct as its text encoder and supports features like text rendering within images.

`image-to-image`

⬇️ 925,236 • ❤️ 2,215 • 15d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**

*Aaron J. Li, Weijia Xu, Chandan Singh et al. (11 authors)*

🏢 Microsoft Research

TokenEconomizer reduces recurring token costs of coding agents across sequential real-world tasks by pruning irrelevant tools, injecting micro-skills, and interrupting failure loops.

▲ 7 • 💬 2 • ⭐ 3,078 • 17d ago

[🎓 arXiv](https://arxiv.org/abs/2610.22732) • [💻 code](https://github.com/microsoft/TokenEconomizer) • [🔗 project](https://tokeneconomizer.github.io/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 160 • 💬 6 • ⭐ 119,103 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 85 • 💬 4 • ⭐ 21,678 • 23d ago

[🎓 arXiv](https://arxiv.org/abs/2610.14224) • [💻 code](https://github.com/google-research/harness2) • [🔗 project](https://harness2.github.io/)

---

**[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**

*Yu Lin, Yiming Wang, Runyuan Cai et al. (5 authors)*

🏢 Edge0

Edge0 enables efficient mixture-of-experts inference on consumer hardware by predicting expert routing ahead of time and using recovery adapters to maintain quality with minimal active memory.

▲ 31 • 💬 9 • ⭐ 8,862 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2609.18063) • [💻 code](https://github.com/Edge0-AI/edge0)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 62 • 💬 4 • ⭐ 44,675 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 105 • 💬 7 • ⭐ 30,126 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 71 • 💬 4 • ⭐ 35,063 • 14mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

**[Very Large-Scale Multi-Agent Simulation in AgentScope](https://huggingface.co/papers/2407.17789)**

*Xuchen Pan, Dawei Gao, Yuexiang Xie et al. (8 authors)*

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.

▲ 48 • 💬 2 • ⭐ 35,054 • 27mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.17789) • [💻 code](https://github.com/modelscope/agentscope)

---

**[HairDeck: Animation-Ready Stylized Hair Cards from a Single Image](https://huggingface.co/papers/2610.40599)**

*Yuze He, Yixiang Wei, Wang Zhao et al. (6 authors)*

🏢 Tsinghua University

HairDeck generates stylized hair cards and spring-bone animations as unordered token sets using a diffusion transformer, improving accuracy and speed over prior methods.

▲ 22 • 💬 2 • ⭐ 379 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2610.40599) • [💻 code](https://github.com/hyz317/HairDeck) • [🔗 project](https://hyzcluster.github.io/HairDeck/)

---

**[Investor's Last Exam: Can AI Agents Do Equity Investment Without Seeing the Future?](https://huggingface.co/papers/2610.38342)**

*Huangfei Jiang, Anning Hu, Kai Sheng et al. (10 authors)*

Investor's Last Exam evaluates financial agents on end-to-end equity research using frozen evidence, expert criteria, and dependency graphs, revealing that top models excel at research but fail at forecasting and investment judgments.

▲ 11 • 💬 4 • ⭐ 128 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2610.38342) • [💻 code](https://github.com/Prophetlab/Investor-Last-Exam) • [🔗 project](https://prophet-lab.cn/benchmarks/investor-last-exam-v1/)

---

---

## GitHub Repositories: "ai"

**[Zagitta/gpu-unlock](https://github.com/Zagitta/gpu-unlock)**

Your GeForce runs AI at half speed. This fixes it for 20/30/40 series cards. Up to 2× FP16 / BF16 / TF32 tensor throughput

`C`

⭐ 13.9k • 🔱 1.4k • 3d ago

---

**[rddmwmddr/android-ad-cleaner](https://github.com/rddmwmddr/android-ad-cleaner)**

关掉国产安卓手机系统里的广告、热搜、资讯推荐和营销推送。不 root，可还原，支持 AI 智能体一键执行。

`Python` `adb` `ai-agent` `android` `coloros` `debloat`

⭐ 5.5k • 🔱 492 • 1h ago

---

**[anhao/ai-pose-gallery-zh](https://github.com/anhao/ai-pose-gallery-zh)**

中文版 AI 姿势参考图库 · 1439 组 / 2878 张图片 / 完整汉化 · 零依赖静态画廊

`TypeScript` `ai-art` `chinese` `cloudflare-pages` `gallery` `i18n`

⭐ 4.9k • 🔱 1.3k • just now

---

**[onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)**

Let an AI model use a real iPhone with a $7 ESP32: AirPlay eyes, USB HID hands, any OpenAI-compatible vision model. No Mac, no developer account, no jailbreak.

`C` `ai-agent` `airplay` `automation` `computer-use` `esp32`

⭐ 4.2k • 🔱 556 • 4d ago

---

**[openfilm/openfilm](https://github.com/openfilm/openfilm)**

The open source AI video agent: turns any coding agent into a video agent, with an editor to change anything it makes.

`TypeScript` `ai-video` `claude-code` `codex` `coding-agents` `html`

⭐ 4.0k • 🔱 380 • 14h ago

---

**[heydamir/unslop](https://github.com/heydamir/unslop)**

A Claude skill that turns vibecoded, AI-looking UI into a designed interface

`JavaScript`

⭐ 3.9k • 🔱 197 • 8h ago

---

**[Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)**

Ears for coding agents: let AI hear, review and make sound. CPU-only, open source.

`Python` `ai-agents` `audio` `claude-code` `mcp` `sound-design`

⭐ 3.4k • 🔱 214 • 9d ago

---

**[wangzan101/Mika](https://github.com/wangzan101/Mika)**

An on-device AI agent for Android that operates apps and the web to get things done for you.

`Kotlin` `accessibility` `ai-agent` `android` `automation` `jetpack-compose`

⭐ 3.1k • 🔱 507 • 1h ago

---

**[deeplethe/solid-glass](https://github.com/deeplethe/solid-glass)**

A design system for AI applications. Material, physical, tactile, technical.

`TypeScript` `agent-ui` `ai` `ai-agents` `chat-ui` `design-system`

⭐ 2.0k • 🔱 42 • 10h ago

---

**[zhuyansen/new-term-radar](https://github.com/zhuyansen/new-term-radar)**

Daily radar for new AI terms: names of new models, products and repos, caught on X, Hugging Face, GitHub and sitemaps before keyword tools list them.

`Python` `agent-skills` `ai` `aisa` `claude-code` `claude-skills`

⭐ 2.0k • 🔱 620 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*
