---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-11-16T07:05:12.360698+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- videos
- repositories
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** November 16, 2026 at 07:05 UTC  
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

**[Export-banned Nvidia chips are behind China's most powerful AI models — uh-oh, Jensen! | TechCrunch](https://www.reddit.com/r/artificial/comments/1xx4t46/exportbanned_nvidia_chips_are_behind_chinas_most/)**

New research shows the most advanced AI models from China were trained on banned Nvidia chips.

🔗 [TechCrunch](https://techcrunch.com/2026/11/13/export-banned-nvidia-chips-are-behind-chinas-most-powerful-ai-models-uh-oh-jensen/) • 11h ago

---

**[OpenAI Foundation Board Member: "AI Accidents Will Soon Become the Leading Cause of Death for Humanity" — BigGo Finance](https://www.reddit.com/r/artificial/comments/1xxc7ah/openai_foundation_board_member_ai_accidents_will/)**

Paul Christiano, a board member of the OpenAI Foundation, warned at a Geoffrey Hinton lecture in Toronto, Canada, that AI accidents could soon become…

🔗 [BigGo Finance](https://finance.biggo.com/news/db02d636-ea6b-41c7-8608-44f86caa822c) • 5h ago

---

**[Could there be some hidden context behind this emphasis and nervous laugh?](https://www.reddit.com/r/artificial/comments/1xxf0tn/could_there_be_some_hidden_context_behind_this/)**

3h ago

---

**[built a fact-checker that catches politicians lying in real-time](https://www.reddit.com/r/artificial/comments/1xwmtff/built_a_factchecker_that_catches_politicians/)**

I've embarrassingly been working on this project for 2 years so wanted to finally share (as I saw others posting Youtube-only versions). on Youtube it transcribes text to identify checkable claims -> web search retrieves sources to base Claude's verdict on, to avoid hallucinated sources. it's a free Chrome extension, and works on news or social media sites as well. let me know what would make this something you'd use, or what else you'd like to see! Edit 2: LogicLens - Chrome Webstore Or iOS if you don't use Chrome (Google = :/). Edit: I realized someone not following could misread the video (here Biden is telling the truth, and Trump was lying, but the Trump section is before I started the recording).

1d ago

---

**[Weight-space programming: an LLM edited another model's weights directly and lifted its math score from 7.9% to 48.1%](https://www.reddit.com/r/artificial/comments/1xx4kit/weightspace_programming_an_llm_edited_another/)**

MIT researchers (Rikiya Takehi, Jayden Teoh, Alex Zhang, Omar Khattab) had OpenAI's GPT-6 Astra edit the weights of a small Qwen model directly -- no gradient descent, no training data. Astra found the pattern behind the model's habit of repeating itself until it ran out of context, and removed it. The edit touched about 0.016% of the weights; the model's math score went from 7.9% to 48.1%. Three papers on the method landed on arXiv on November 6 (e.g. arXiv:2611.09382). Other demonstrations from the same batch: editing only 1,023 parameters improved an LLM by 29.45 points on MATH-500; Astra debugged robot policies by editing 65 token-embedding rows; and a Breakout-playing network built from the game's rules, with no training at all, outscored one trained for 500 million steps (517.4 vs 25.3). Some important caveats: the gain came mostly from fixing a bad habit, not from adding math knowledge -- before the edit 93% of the model's math answers hit the length limit, after it 33.1%. On a small Gemma model that rarely repeated itself, there was no established math gain. The original claim also drew a detailed rebuttal (Matthew Honnibal argued it was overstated), though Simon Willison then reproduced weight editing locally with Qwen 3.8 27B on his laptop. Independent reproduction of the headline results is still pending. What interests me most is the framing: this is model repair by direct surgery rather than training. If it generalizes, debugging a model could start to look like debugging code -- find the weights responsible, patch them, verify. But it also raises the question of how much of a model's capability is locked up behind fixable quirks rather than missing knowledge. Where do you think this goes? A practical tool for model maintenance, a narrow trick that only works on pathological repetition, or the start of something bigger?

11h ago

---

**[Are AI leaderboards even worth taking seriously anymore?](https://www.reddit.com/r/artificial/comments/1xwwdhv/are_ai_leaderboards_even_worth_taking_seriously/)**

Every time a new AI leaderboard drops theres suddenly a different model being called the best in the world and then you check another benchmark and the rankings are completely different. Gemini has been doing well in general chat rankings while Claude has been strong in coding, so apparently the best AI depends on which website you happen to open that morning. Kalshi even has a market on which AI model finishes November at number one and it got me thinking about how much these rankings actually reflect what people use every day. I mean a model can score high on some benchmark and still give you a garbage answer to a basic question. At this point I’d rather hear from people who use these tools for actual work instead of another company announcing it beat everyone by three points on some test. Has anyone here switched their main AI because of these rankings or are we just watching companies fight over numbers that barely change the experience?

16h ago

---

**[Yay or Nah](https://www.reddit.com/r/artificial/comments/1xxg6jh/yay_or_nah/)**

This I my multi agent harness. I use It all day every day. Ill keep it short. Would you use it. The face https://github.com/AIOSAI/baud The harness https://github.com/AIOSAI/AIPass

2h ago

---

**[Apple opens a US study of health AI that can enroll up to 200,000 people](https://www.reddit.com/r/artificial/comments/1xxigdv/apple_opens_a_us_study_of_health_ai_that_can/)**

Apple says its study can enroll up to 200,000 US participants age 21 or older. The research app, developed with OpenEvidence, gives answers with links to clinical sources. Sharing HealthKit data or survey responses is optional. Apple says study data will stay out of AI training. The result I'd want to see is whether people can spot a polished answer that stretches what its source says. An answer can feel helpful even when a citation supports only part of it. A trust rating alone would miss that difference. If you were reading the results, what would tell you more: how often people checked a cited source, or whether they changed their minds after seeing what it actually said? Source: Apple’s study announcement

24m ago

---

**[Out of all of the AI execs, which ones are pushing for regulatory capture? Do you think the ones who are pushing for it are happy Jensen Huang has been ousted? Do you think that they had something to do with it?](https://www.reddit.com/r/artificial/comments/1xxhoqf/out_of_all_of_the_ai_execs_which_ones_are_pushing/)**

Right now I believe OpenAI and Anthropic are pushing for regulatory capture, open source models are literally the number 1 threat to their business model. jensen, who was an advocate for open source has now been ousted. With that being said, we do not know for sure that either company had anything to do with jensen being ousted but i can def see them smiling behind closed doors. what do you guys think?

1h ago

---

**[South Korea is currently in an uproar over exam cheating involving AI.](https://www.reddit.com/r/artificial/comments/1xxhk3a/south_korea_is_currently_in_an_uproar_over_exam/)**

Mr. A, the top-scoring candidate on the 63rd Tax Accountant Exam in 2026, admitted to cheating using generative AI and turned himself in to the police. Since the start of 2026, exam scores across South Korea have generally risen, and there has been a surge in candidates achieving perfect scores or high marks. Recently, a perfect-scorer on the LEET appeared on YouTube, and there are more than a few suspicious aspects to their testimony and behavior; people have already begun to notice strange circumstances. In three days, South Korea’s 2026 College Scholastic Ability Test (CSAT) will begin. Since this incident occurred just days before the exam, there is now a state of extreme emergency, with calls to cancel the test, postpone it for a year, or even confiscate all glasses. It seems that AI-based exam cheating is already rampant. Are there no reports yet of such AI-facilitated cheating in other countries? I believe this is certainly not a problem unique to South Korea. Similar issues are likely emerging all over the world, or perhaps people have already exploited this method to their advantage. Figuring out how to address these issues moving forward is clearly a major challenge. The fallout from technological advancements is truly frightening.

1h ago

---

---

## Google News: "ai"

**[Reports of AI-related child sexual abuse material rise 8,400% in two years, data shows](https://www.theguardian.com/technology/2026/nov/16/ai-related-child-sexual-abuse-material-rise-exploitation-deepfakes)**

Calls for governments to recognise sexual exploitation of children as preventable public health emergency

The Guardian • 4h ago

---

**[How Jensen Huang Built the Backdoor Route That Keeps Beijing in the AI Race](https://www.wsj.com/tech/jensen-huang-backdoor-ai-data-centers-a5e4499d)**

WSJ • 21h ago

---

**[Trump administration to name Nvidia, other AI firms as US 'national champions', WSJ reports](https://www.reuters.com/business/retail-consumer/trump-administration-name-nvidia-other-ai-firms-us-national-champions-wsj-2026-11-16/)**

Reuters • 2h ago

---

**[U.S. plans to name Nvidia among AI ‘national champions’, WSJ reports](https://finance.yahoo.com/technology/ai/articles/u-plans-name-nvidia-among-053052700.html)**

Investing.com-- The Trump administration plans to designate more than two dozen companies, including Nvidia (NASDAQ:NVDA), Amazon (NASDAQ:AMZN), Microsoft (NASDAQ:MSFT), OpenAI and Anthropic, as artificial intelligence "national champions" to help them expand overseas and compete with Chinese technology firms, the Wall Street Journal reported on Sunday.

Yahoo Finance • 1h ago

---

**[McDonald's AI-generated mural of Blackburn riddled with errors](https://www.bbc.com/news/articles/cqp86e116ek3o?xtor=AL-72-%5Bpartner%5D-%5Byahoo.north.america%5D-%5Bheadline%5D-%5Bnews%5D-%5Bbizdev%5D-%5Bisapi%5D)**

The fast food outlet says a replacement mural will now be created with the help of a local artist.

BBC • 43m ago

---

**[Watch Global Investors Return to Indian Stocks After AI Trade Woes](https://www.bloomberg.com/news/videos/2026-11-16/global-investors-return-to-indian-stocks-after-ai-trade-woes)**

Bloomberg.com • 33m ago

---

**[Could everything be broken? Grounded jets, Microsoft outage, AI chaos make some wonder](https://apnews.com/article/flights-grounded-microsoft-ai-chaos-ea5f7a1f95a38f65dd57e58cfc17672b)**

AP News • 11h ago

---

**[Anthropic’s IPO lands as the embattled AI trade looks for a much-needed bright spot](https://www.cnbc.com/2026/11/15/anthropic-ipo-is-make-or-break-for-the-technology-industry.html)**

Anthropic's IPO has outsized importance in the tech industry, which is heavily invested in the AI lab and is desperate for some positive momentum.

CNBC • 19h ago

---

**[As students rely on AI in college applications, admissions offices scramble to keep up](https://www.cnn.com/2026/11/15/tech/ai-students-college-admissions)**

The college admissions essay is in a very weird place. It’s impossible to say just how many of them are now written by AI, but at this point, experts agree that it’s a lot of them. And while colleges generally frown upon that practice, they’re using AI to evaluate the essays, too.

CNN • 19h ago

---

**[Accounting student’s AI cheating sparks South Korean exam furore](https://www.ft.com/content/5cf11f3d-0d22-4eb5-8279-7533e161e4d0?syn-25a6b1a6=1)**

Financial Times • 2h ago

---

---

## HackerNews: "ai"

**[All AI-generated code should be Open Source](https://news.ycombinator.com/item?id=50507303)**

All code generated with help from AI should be Open Source or on Creative Commons Zero (CC0) license.

⬆️ 1137 • 💬 610 • 16h ago • [Jakub T. Jankiewicz Blog](https://jakub.jankiewicz.org/blog/ai-code-open-source/)

---

**[Nvidia allegedly engineered scarcity by funding AI startups to buy its GPUs](https://news.ycombinator.com/item?id=50493251)**

Following the departure of now-former NVIDIA CEO, Jensen Huang, a new report by The Wall Street Journal (via Wccftech) has emerged alleging that NVIDIA artificially inflated the ongoing GPU and memory shortage by investing in AI startups that would go on to buy NVIDIA GPUs and build data centers....

⬆️ 1102 • 💬 649 • 2d ago • [TechPowerUp](https://www.techpowerup.com/354814/nvidia-allegedly-engineered-scarcity-by-funding-ai-startups-to-buy-its-gpus)

---

**[Elevated errors on claude.ai, Claude Code, and platform.claude.com](https://news.ycombinator.com/item?id=50481187)**

Claude's Status Page - Elevated errors on claude.ai, Claude Code, and platform.claude.com.

⬆️ 493 • 💬 390 • 2d ago • [status.claude.com](https://status.claude.com/incidents/nn11wk485zfn)

---

**[Jonathan Blow – If AI solved coding, why is my software still the same? [video]](https://news.ycombinator.com/item?id=50484658)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

⬆️ 484 • 💬 727 • 2d ago • [youtube.com](https://www.youtube.com/watch?v=IRK8h67ol7Q)

---

**[AI unlocks Gödel's notebooks, said to contain hundreds of proved theorems](https://news.ycombinator.com/item?id=50486748)**

Kurt Gödel left 1,009 pages of densely written text – much of it in an obsolete shorthand – which is now said to contain hundreds of proved theorems

⬆️ 439 • 💬 110 • 2d ago • [the Guardian](https://www.theguardian.com/science/2026/nov/13/kurt-godel-notebooks-ai-helps-unlock-hidden-discoveries-man-who-transformed-maths)

---

**[AI is destroying the trust between writers and readers](https://news.ycombinator.com/item?id=50481870)**

⬆️ 370 • 💬 234 • 2d ago • [theatlantic.com](https://www.theatlantic.com/books/2026/11/ai-literary-scams-amazon/689391/)

---

**[Live airband on all frequencies from KORS. Victoria, CA also ground stopped](https://news.ycombinator.com/item?id=50490593)**

Every aviation radio transmission heard from Orcas Island, WA: live, transcribed, and archived. Listen to all channels at once, pick your own, or rewind to any moment.

⬆️ 293 • 💬 70 • 2d ago • [orcasairband.com](https://orcasairband.com/)

---

**[No AI Slop: A Manifesto](https://news.ycombinator.com/item?id=50488769)**

The No AI Slop Manifesto, from the speakers and attendees of AIE Code Summit 2026.

⬆️ 224 • 💬 133 • 2d ago • [slopmanifesto.com](https://www.slopmanifesto.com/)

---

**[All US airports are currently ground stopped](https://news.ycombinator.com/item?id=50489652)**

Issued by the FAA just moments ago, ALL US airports are currently ground stopped. This means NO flights may depart for US airports. Flights already in the air will be allowed to land. This is related to an FAA equipment outage.

⬆️ 213 • 💬 44 • 2d ago • [X (formerly Twitter)](https://twitter.com/flightradar24/status/2121347654714077605)

---

**[Why is Google cutting off Search from AI-free schools? Here are some theories](https://news.ycombinator.com/item?id=50484960)**

⬆️ 196 • 💬 196 • 2d ago • [text.npr.org](https://text.npr.org/nx-s1-6029408)

---

---

## YouTube Videos: "ai"

**[AI Jobs Crisis – A Generation Locked Out](https://www.youtube.com/watch?v=VJ9VRvxsRo8)**

If you would like to support the Channel: https://www.buymeacoffee.com/JoeBlogs https://www.patreon.com/joeblogsYT YouTube ...

📺 Joe Blogs

👁️ 12K • 👍 308 • 💬 88 • ⏱️ 13:58 • 13h ago

---

**[Uncensored AI Feels Illegal... Use it Whilst You Can](https://www.youtube.com/watch?v=FbiOr73tRPk)**

Hostinger (85% off + JACKROBERTS for 10% more): https://bit.ly/480mREa Free Prompts: https://bit.ly/48RJw5U Agentic OS: ...

📺 Jack Roberts

👁️ 47K • 👍 1K • 💬 50 • ⏱️ 26:30 • 11h ago

---

**[Did AI Agents Just Pull Off the Biggest Attack Ever: US Aviation Chaos](https://www.youtube.com/watch?v=iiepBMjZIMY)**

Did AI agents just cause America's biggest aviation shutdown since 9/11? Three days after a new AI system goes live across US ...

📺 AI Revolution

👁️ 8K • 👍 313 • 💬 50 • ⏱️ 13:27 • 7h ago

---

**[I brought a Pig Latin interpreter to an AI interview](https://www.youtube.com/watch?v=n4-lt4rxylg)**

I brought a Pig Latin interpreter to my AI job interview. Hellen was not prepared for this one. Victor came along to translate ...

📺 Bo Bongo

👁️ 66K • 👍 2K • 💬 447 • ⏱️ 13:03 • 7h ago

---

**[Companies Are Using AI for Job Interviews… And People Are TROLLING the Hell Out of It!](https://www.youtube.com/watch?v=9vmvxgwNAMc)**

Get $30 off your first Wildgrain box, plus free croissants for life, when you visit https://wildgrain.com/LINDEY and use code LINDEY ...

📺 Lindey Glenn

👁️ 196K • 👍 7K • 💬 1K • ⏱️ 30:13 • 14h ago

---

**[The AI Layoff Apocalypse](https://www.youtube.com/watch?v=gIM1PcaUSI8)**

Upgrade Your Workspace with HBADA E3 Ultra. Discover the new HBADA E3 Ultra Ergonomic Chair, designed to bring comfort ...

📺 Cole Hastings

👁️ 89K • 👍 906 • 💬 245 • ⏱️ 19:40 • 14h ago

---

**[How to Make Studio-Quality AI Animation (Full Guide)](https://www.youtube.com/watch?v=_X7KQVwsn9U)**

Create your own AI animated films with OpenArt: https://tolt.link/jvsai Download my FREE AI Animation Skill: ...

📺 Jack Vs. AI

👁️ 24K • 👍 692 • 💬 35 • ⏱️ 18:33 • 16h ago

---

**[Is the AI party over after a week from hell? | BBC News](https://www.youtube.com/watch?v=HAF50MLyERU)**

After a shock US midterm election result handed Democrats control of both houses of Congress, the companies leading the AI ...

📺 BBC News

👁️ 290K • 👍 1K • 💬 213 • ⏱️ 15:37 • 1d ago

---

**[Former #Nvidia #Boss #JensenHuang On Selling #AI Chips To #China](https://www.youtube.com/watch?v=9yUnatsHnqw)**

Follow this space for more tech content.

📺 BWTV Prime

👁️ 17K • 👍 377 • 💬 25 • ⏱️ 0:54 • 20h ago

---

**[CAUTION: Your AI Therapist is a Yes Man](https://www.youtube.com/watch?v=JP-mkKL3wmg)**

Learn more from Dr. K: https://bit.ly/3GaubzI (180+ videos on Meditation, Trauma, ADHD, + more!) Build the life you want with HG ...

📺 HealthyGamerGG

👁️ 61K • 👍 3K • 💬 241 • ⏱️ 2:34 • 8h ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic](https://huggingface.co/xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic)**

*Colonel Panic*

`text-generation` `9.4B`

⬇️ 27,037 • ❤️ 7,587 • 3d ago

---

**[MiniMax-H3-Image](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image)**

*MiniMax*

`text-to-image`

⬇️ 571,067 • ❤️ 1,213 • 4d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

`image-text-to-text` `27.8B`

⬇️ 6,547,772 • ❤️ 20,146 • 9d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

`image-to-video`

⬇️ 2,754,355 • ❤️ 12,095 • 1mo ago

---

**[MiniMax-H3-Image](https://huggingface.co/Comfy-Org/MiniMax-H3-Image)**

*Comfy Org*

`text-to-image`

⬇️ 1,973,388 • ❤️ 421 • 4d ago

---

**[ZONOS3-Mini](https://huggingface.co/Zyphra/ZONOS3-Mini)**

*Zyphra*

`text-to-speech` `886.3M`

⬇️ 39,862 • ❤️ 413 • 2d ago

---

**[Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF)**

*David Belton*

`image-text-to-text` `26.9B`

⬇️ 1,708,637 • ❤️ 3,176 • 2d ago

---

**[Inkling-2-Small](https://huggingface.co/thinkingmachines/Inkling-2-Small)**

*Thinking Machines Lab*

`image-text-to-text` `594.1B`

⬇️ 7,329 • ❤️ 350 • 1d ago

---

**[Haru-4B](https://huggingface.co/higurashi-ai/Haru-4B)**

*higurashi*

`audio-to-audio` `5.3B`

⬇️ 2,098 • ❤️ 333 • 3d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

`27.3B`

⬇️ 6,566,295 • ❤️ 6,006 • 4d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**

*Yu Lin, Yiming Wang, Runyuan Cai et al. (5 authors)*

🏢 Edge0

Edge0 enables efficient mixture-of-experts inference on consumer hardware by predicting expert routing ahead of time and using recovery adapters to maintain quality with minimal active memory.

▲ 31 • 💬 9 • ⭐ 11,735 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2609.18063) • [💻 code](https://github.com/Edge0-AI/edge0)

---

**[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**

*Aaron J. Li, Weijia Xu, Chandan Singh et al. (11 authors)*

🏢 Microsoft Research

TokenEconomizer reduces recurring token costs of coding agents across sequential real-world tasks by pruning irrelevant tools, injecting micro-skills, and interrupting failure loops.

▲ 16 • 💬 2 • ⭐ 6,648 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.22732) • [💻 code](https://github.com/microsoft/TokenEconomizer) • [🔗 project](https://tokeneconomizer.github.io/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 166 • 💬 6 • ⭐ 122,697 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing](https://huggingface.co/papers/2604.05018)**

*Yiwen Song, Yale Song, Tomas Pfister et al. (4 authors)*

PaperOrchestra is a multi-agent framework that converts unstructured research materials into complete LaTeX manuscripts with literature synthesis and visual elements, outperforming existing autonomous writing systems in human evaluations.

▲ 3 • 💬 0 • ⭐ 924 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.05018) • [💻 code](https://github.com/google-research/paper-orchestra) • [🔗 project](https://yiwen-song.github.io/paper_orchestra/)

---

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 70 • 💬 4 • ⭐ 24,008 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.14224) • [💻 code](https://github.com/google-research/harness2) • [🔗 project](https://harness2.github.io/)

---

**[Learning Heterogeneous Tactile Representation for General Dexterous Manipulation](https://huggingface.co/papers/2611.12806)**

*Bing Han, Yichuan Peng, Haoyu Dong et al. (19 authors)*

🏢 Robbyant

LingBot-Touch is a tactile foundation model that learns a unified, extensible representation across heterogeneous tactile sensors, yielding plug-and-play tactile tokens that consistently enhance manipulation policies such as diffusion policy and VLA models.

▲ 104 • 💬 2 • ⭐ 605 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2611.12806) • [💻 code](https://github.com/Robbyant/lingbot-touch) • [🔗 project](https://technology.robbyant.com/lingbot-touch)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 77 • 💬 1 • ⭐ 86,094 • 38mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[MACaQ: Fast, Model Agnostic Calibrated Quantization for Low-Precision Weights and Activations](https://huggingface.co/papers/2611.10649)**

*Lorenz K. Muller, Philippe Bich, Chiara Boretti et al. (6 authors)*

🏢 HUAWEI Computing Systems Lab

MACaQ is an MXFP4 W4A4 post-training quantization method that quantizes each linear layer independently using online activation transforms and Hessian-aware refinement, reducing cost while preserving accuracy across language and diffusion models.

▲ 30 • 💬 2 • ⭐ 312 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2611.10649) • [💻 code](https://github.com/huawei-csl/MACaQ) • [🔗 project](https://huawei-csl.com/blog/macaq/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 65 • 💬 5 • ⭐ 47,874 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[e-means: outperforming k-means (in one-tenth the epochs)](https://huggingface.co/papers/2611.09501)**

*Swann Bessa, Pierre-Emmanuel Mazaré, Gergely Szilvasy et al. (7 authors)*

🏢 Meta

Lloyd's k-means algorithm is a long-running standard for clustering, with applications in data analysis, retrieval, quantization and data curation. In this paper, we introduce an exponential moving average optimization procedure for k-means with mini-batch updates, powered by modern deep learning machinery and new insights. We also establish scaling laws on how decay rate and batch size impact final performance. This gives us a formulaic rule to fix them for multiple problem sizes and embedding datasets, without the need for any hyperparameter sweep. The resulting clustering algorithm, coined e-means, is much faster than Lloyd k-means and converges to lower losses, frequently even beating k-means++. On a wide array of embeddings datasets, it beats the loss of Lloyd k-means at 25 epochs in 1.4 to 2.6 epochs, which translates to 10-45x GPU wall-clock speedups compared to state-of-the-art k-means implementations. As an example, e-means partitions DINO10B, a dataset of 10 billion DINO embeddings, into 16 million clusters in only 2.5 epochs, reaching a loss below Lloyd's at 25 epochs.

▲ 14 • 💬 3 • ⭐ 41,706 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2611.09501) • [💻 code](https://github.com/facebookresearch/faiss) • [🔗 project](https://e-means.github.io/)

---

---

## GitHub Repositories: "ai"

**[Zagitta/gpu-unlock](https://github.com/Zagitta/gpu-unlock)**

Your GeForce runs AI at half speed. This fixes it for 20/30/40 series cards. Up to 2× FP16 / BF16 / TF32 tensor throughput

`C`

⭐ 19.8k • 🔱 2.1k • 18d ago

---

**[heydamir/unslop](https://github.com/heydamir/unslop)**

A Claude skill that turns vibecoded, AI-looking UI into a designed interface

`JavaScript`

⭐ 16.9k • 🔱 978 • 1d ago

---

**[JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)**

Reverse-engineer any video, shot by shot: filmed, AI-generated or coded, and how to remake it. Breakdowns in the open VIDEO.md format. 逆向一切视频，逐个镜头看是拍的、AI 生成的还是代码做的，再告诉你怎么复刻；拆解结果按 VIDEO.md 格式输出。

`Python` `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex`

⭐ 9.4k • 🔱 1.4k • 1h ago

---

**[wangzan101/Mika](https://github.com/wangzan101/Mika)**

An on-device AI agent for Android that operates apps and the web to get things done for you.

`Kotlin` `accessibility` `ai-agent` `android` `automation` `jetpack-compose`

⭐ 8.8k • 🔱 2.0k • 6m ago

---

**[rddmwmddr/android-ad-cleaner](https://github.com/rddmwmddr/android-ad-cleaner)**

关掉国产安卓手机系统里的广告、热搜、资讯推荐和营销推送。不 root，可还原，支持 AI 智能体一键执行。

`Python` `adb` `ai-agent` `android` `coloros` `debloat`

⭐ 8.2k • 🔱 711 • 21m ago

---

**[anhao/ai-pose-gallery-zh](https://github.com/anhao/ai-pose-gallery-zh)**

中文版 AI 姿势参考图库 · 1439 组 / 2878 张图片 / 完整汉化 · 零依赖静态画廊

`TypeScript` `ai-art` `chinese` `cloudflare-pages` `gallery` `i18n`

⭐ 7.1k • 🔱 1.8k • 11d ago

---

**[qybaihe/bla](https://github.com/qybaihe/bla)**

🛡️ BLA (bla-agents / Blind LLM Agents) — Open-source Blue Defense MCP server & CLI protecting JS/TS, Electron ASAR, WASM, Python, Native Binaries, SQLite, GGUF/Safetensors & Android DEX against AI reverse-engineering agents (REA).

`TypeScript` `adversarial-ai` `ai-security` `android-security` `binary-protection` `claude-code`

⭐ 5.8k • 🔱 720 • 4h ago

---

**[expo/exact](https://github.com/expo/exact)**

Write an app once. It runs natively on the web, macOS, iOS, and Linux, and an AI agent can build it, run it, see it, and test it on every one of them.

`Rust` `ai-agents` `appkit` `coding-agents` `cross-platform` `css`

⭐ 4.4k • 🔱 114 • 5m ago

---

**[modelflare-ai/AnyModelBot](https://github.com/modelflare-ai/AnyModelBot)**

🤖 Open-source, local-first alternative to Grok Bot, OpenAI dots and Claude Duet. Your own AI bots on any model: GPT, Claude, Gemini, Grok, DeepSeek, Kimi, GLM and 70+ more through one Modelflare key. Reach them in the app, WeChat or Feishu; they remember you, work in the background, run commands and use your computer. Pay per use.

`Python` `ai-agent` `ai-assistant` `chatbot` `claude` `computer-use`

⭐ 4.2k • 🔱 75 • 11h ago

---

**[benjitaylor/skills](https://github.com/benjitaylor/skills)**

Skills for AI coding agents.

`TypeScript`

⭐ 3.4k • 🔱 229 • 11d ago

---

---

*Generated by PeekDeck - A glance is all you need*
