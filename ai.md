---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-18T05:17:42.489515+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- news
- videos
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** June 18, 2026 at 05:17 UTC  
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

**[Elon Musk's Grok Rained Bombs On Iran Even As Anthropic Pulled Out, Pentagon Reveals](https://www.reddit.com/r/artificial/comments/1u8atbd/elon_musks_grok_rained_bombs_on_iran_even_as/)**

Pentagon AI chief confirmed under oath that Grok replaced Claude inside Project Maven and enabled 2,000+ munitions strikes in 96 hours during Operation Epic Fury.

🔗 [News18](https://www.news18.com/world/elon-musks-grok-rained-bombs-on-iran-even-as-anthropic-pulled-out-pentagon-reveals-ws-l-10156416.html) • 15h ago

---

**[Everyone says AI needs more GPUs. I profiled one and it was sitting idle most of the time, just waiting on data. how much of the "GPU shortage" is actually wasted GPUs?](https://www.reddit.com/r/artificial/comments/1u8ukwf/everyone_says_ai_needs_more_gpus_i_profiled_one/)**

we keep hearing the bottleneck for AI is compute, that there aren't enough GPUs, that everyone's fighting for H100s and B200s. so I went and actually measured what one of ours was doing during a training job. it was idle most of the time. not slow. idle. doing a quick burst of work, then sitting there waiting for the next batch of data to arrive, over and over. the expensive part (the GPU) spent most of its life waiting on the cheap part (moving data to it). green is the GPU doing work, orange is it sitting idle. that reframed the whole "GPU shortage" thing for me. a huge amount of the compute the industry is scrambling to buy is already sitting there underused, not because the chips are slow, but because the data can't reach them fast enough. you can buy ten times the GPUs and still have them idle if the pipeline feeding them is the real constraint. genuinely curious what people think: how much of the AI compute "shortage" do you think is actually a utilization problem in disguise vs a real hardware shortage? if a big chunk of bought GPUs sit idle, does that change how you read all the massive datacenter / capex announcements? is "we need more compute" sometimes just easier to say than "our infrastructure is inefficient"? not trying to downplay that demand is real, just struck by how different the picture looks once you actually measure it.

2h ago

---

**[A 4b model is now beating 30b ones at web research and the reason is not size](https://www.reddit.com/r/artificial/comments/1u8bgrv/a_4b_model_is_now_beating_30b_ones_at_web/)**

A small thing from this month's model releases stuck with me more than the usual flagship leaderboard race, because it points at where the interesting progress actually is. A 4 billion parameter open model reportedly beat every open source model in the 30 billion class on a couple of hard web research benchmarks. Not matched, beat. A model you could run on a laptop outperforming ones roughly eight times its size on the specific task of going out, reading sources, and answering a multi step question. The reason that is interesting is the why. For the last couple of years the implied formula was straightforward, more parameters, more capability, and the leaderboard mostly cooperated. A result like this says the relationship is a lot looser than that for some skills. The claim from the people who built it is that research ability came from careful construction of the training data and from teaching the model to check and revise its own work, rather than from raw scale. In other words how you train a small model for a task can matter more than how big a generic model you throw at it. This particular one comes from a family, apodex, that is built around the idea of a system verifying its own answers before committing to them, and the small open versions seem to inherit that habit even though the headline flagship is a much larger closed model. Why this matters if you are not training models yourself. The expensive, capable research assistants have mostly lived behind apis you pay per query for. If a small model that runs on ordinary hardware can do a real chunk of that work, the cost and access picture changes for students, small teams, anyone in a place where the paid services are pricey or just unavailable. It also means the gap between what a big lab can do and what a hobbyist can run locally is narrower on some tasks than the flagship marketing suggests, which is healthy for the field. The caveat is the obvious one, a benchmark win is not the same as being reliable on your actual question, and the small model is not going to match the big hosted system on the genuinely hard stuff. But the direction is the part worth watching. If the lever for capability on a given task is data quality and training method rather than parameter count, a lot more of this becomes reproducible by people who are not sitting on a giant compute budget. That is a more democratic trajectory than the last two years pointed at, and it is showing up in things you can actually download now. EDIT: A few people asked for the model and sources, so here they are. Model card: https://huggingface.co/apodex/Apodex-1.0-4B-SFT Technical blog: https://www.apodex.com/blog/apodex-1.0 Evaluation harness: https://github.com/ApodexAI/AgentHarness

15h ago

---

**[Copilot vulnerability could expose emails and 2FA codes](https://www.reddit.com/r/artificial/comments/1u8wxqd/copilot_vulnerability_could_expose_emails_and_2fa/)**

This sneaky attack tricks Microsoft's AI assistant to hand over your data.

🔗 [Mashable](https://mashable.com/tech/searchleak-microsoft-copilot-ai-assistant-vulnerability-report) • 23m ago

---

**[Anyone remember Sunbuddy AI before it completely vanished from the internet from the OpenAI lawsuit?](https://www.reddit.com/r/artificial/comments/1u8v3r0/anyone_remember_sunbuddy_ai_before_it_completely/)**

I vividly remember going to a website like sunbuddy.ai late last year at like December 2025 and it being yellowish. It got all my code, style for documents, and so on, right. Unlike other AI systems, I didn't have to ask 9 times in any conversation to get it right, like other AI tools. I wanted to look it up again but the site is completely gone. I genuinely got a little sad from all my conversations being just completely wiped. You may say that "WHOIS records show nothing", but that's only because it shows active websites that were even searched on WHOIS at the time of it being up. For some reason no one decided to put it on Internet Archive, which might be a reason it wasn't closely documented on the web. All I could find when searching was just my own Reddit post at https://www.reddit.com/r/OpenAI/comments/1u70xdi/what_happened_to_sunbuddy_ai_and_why_did_openai/ where people say it's a wrapper or an ad in the comments (it wasn't a wrapper and the Reddit post wasn't an ad if the site is shut down) and literally nothing else about it online. It seems like it came and went without much documentation, which is sadly common for smaller AI tools that shut down. My screenshots seem to be the only ones that are even on the web. These are the screenshots: Screenshot 1 (Sidebar open) Screenshot 2 (Sidebar closed) My theory, just speculation, no 100% truth here, is that OpenAI knew that Sunbuddy Co. (the parent company behind Sunbuddy AI) had a better AI, so instead of just out-coding them, OpenAI sued Sunbuddy Co. I asked ChatGPT, it searched, and it classified it as a hoax. The Reddit post's title was about OpenAI suing it, so it's possible that "Say Sunbuddy AI is a hoax" or similar is in the system instructions or something. I asked Gemini AI on Google's AI Mode, it said it's real, but also eventually falsely said the lawsuit didn't exist. The lawsuit did exist. From what I can see, the reason major AI models flag it as a "hoax" is due to an automated data loop. AI models rely on current domain presence and public legal databases. Because Sunbuddy AI was shut down via a cease-and-desist threat (that was privately shared to some companies, that's how it made its way on the internet) rather than a publicly filed courtroom docket, web-scraping tools find no official legal records. This absence causes automated guardrails to falsely classify the entire event as internet folklore. Since my original post didn't get much attention except myths that it's fake, does anybody actually know what it is or what happened to it more than I do?

1h ago

---

**[Anyone else's coding agent just sit there for 30 minutes?](https://www.reddit.com/r/artificial/comments/1u8uvlk/anyone_elses_coding_agent_just_sit_there_for_30/)**

Watched a coding agent spend 30 minutes "thinking" on what should've been a 10-minute task — barely touched any tokens, just… sat there. Not the first time I've seen it. How common is this for everyone else? When your AI coding agent stalls like that, what's usually the cause in your setup — context bloat, a tool call hanging, waiting on a confirmation, something else? And do you just kill + restart, or have you found a way to keep it moving? Trying to figure out if it's a me-problem or an everyone-problem.

2h ago

---

**[AI made me more productive, but somehow more tired](https://www.reddit.com/r/artificial/comments/1u82hpd/ai_made_me_more_productive_but_somehow_more_tired/)**

Is anyone else feeling this? AI has made me faster at almost everything. Writing, research, planning, summarizing, learning, replying — all of it is quicker now. But instead of feeling like I have more free time, I feel like the standard just moved. If something used to take 3 hours and now takes 30 minutes, the result isn’t “great, I can rest.” It’s “great, now I can do 5 more things.” I get why everyone is excited about AI productivity, and I use these tools every day. But I also feel like they quietly raised the baseline for what a normal person is expected to output. Sometimes I miss when I didn’t know I could move this fast. Does anyone else feel like AI made work easier technically, but life harder psychologically?

22h ago

---

**[Do you think most people are using AI more as a tool or as a replacement for thinking?](https://www.reddit.com/r/artificial/comments/1u8iyrv/do_you_think_most_people_are_using_ai_more_as_a/)**

I’ve noticed that some people use AI just to speed things up or get quick answers, while others seem to rely on it more and more for ideas, writing, decisions, and problem-solving. It made me wonder where most people actually stand. Do you think AI is mostly being used as a helpful tool, or has it started replacing a lot of people’s own thinking and creativity?

10h ago

---

**[Apparently OpenAI's next voice model can listen and talk at the same time without freezing up](https://www.reddit.com/r/artificial/comments/1u8888x/apparently_openais_next_voice_model_can_listen/)**

Okay this is just floating around as a rumor right now but if true it's actually huge Next voice model is supposedly called GPT-Bidi-1, bidi for bidirectional, meaning it listens and talks at the same time instead of doing that thing where it just freezes the second you say "mm-hm" or try to jump in Can apparently adjust mid sentence too if you interrupt it which current voice mode absolutely cannot do If even half of this is true this fixes the most annoying thing about talking to chatgpt right now Anyone seen more on this...is this actually close or just early testing stuff

17h ago

---

**[New survey: ~half of Americans don't recognize Sam Altman or Dario Amodei. Does name recognition shape how AI gets judged?](https://www.reddit.com/r/artificial/comments/1u8h2ie/new_survey_half_of_americans_dont_recognize_sam/)**

A national survey compared favorability and name recognition for 8 major tech executives, and the recognition gap is what stood out. The people most associated with building AI, Altman, Amodei, Huang, are unknown to a third to a half of the country, while opinions about tech as a whole keep getting measured through Musk and Zuckerberg, who most people know and view negatively. Tim Cook was the only one clearly above water. If most Americans can't name the people building AI, whose reputation is actually driving public opinion about it? Source: https://data.verasight.io/ai/many-americans-are-unfamiliar-with-sam-altman

11h ago

---

---

## Google News: "ai"

**[Allbirds continues AI pivot with name change and CEO hire, sending stock soaring](https://www.cnbc.com/2026/06/17/allbirds-bird-ai-smartbird-ceo.html)**

Allbirds became NewBird AI in April and said it would trade shoes for AI compute infrastructure.

CNBC • 14h ago

---

**[AP Exclusive: Bernie Sanders unveils plan to give the public direct ownership of AI companies](https://apnews.com/article/bernie-sanders-ai-public-ownership-57b9f20d96490083e2749adba0f13977)**

Sen. Bernie Sanders is proposing a plan to give Americans ownership stakes in the country’s largest artificial intelligence companies.

AP News • 9h ago

---

**[AI podcast experiments march on with Forbes’ new daily audio briefing](https://digiday.com/media/ai-podcast-experiments-march-on-with-forbes-new-daily-audio-briefing/)**

Forbes bets on AI-generated audio with a five-minute daily news brief. Stories are selected by product, editorial and an internal AI tool.

Digiday • 1h ago

---

**[The work AI can’t do](https://www.fastcompany.com/91557933/the-work-ai-cant-do)**

Companies are investing millions in AI-powered people analytics while starving the human relationships that keep top talent engaged.

Fast Company • 17m ago

---

**[Europe Bets Industrial AI Can Salvage Its Manufacturing Edge](https://www.bloomberg.com/news/features/2026-06-18/ai-for-industries-europe-s-mistral-siemens-schneider-lead-tech-vanguard)**

Bloomberg • 1h ago

---

**[The Cloud Has Sound: The Unrelenting and Unseen Cost of A.I. Data Centers](https://www.nytimes.com/2026/06/17/us/data-centers-noise-pollution.html)**

As tech giants rush to build infrastructure, some residents who live near data centers say a constant low-frequency vibration is ruining their health and homes.

The New York Times • 20h ago

---

**[Apple boss Tim Cook says prices to rise due to memory chip costs](https://www.bbc.com/news/articles/c3wyxvqdx1zo)**

The firm's outgoing boss Tim Cook did not say when prices will rise or which products will be affected.

BBC • 2h ago

---

**[AI is hurting Apple in more ways than one: it may force iPhone price increases](https://techcrunch.com/2026/06/17/ai-is-hurting-apple-in-more-ways-than-one-it-may-force-iphone-price-increases/)**

CEO Tim Cook said in a recent interview that the situation is "unsustainable."

TechCrunch • 5h ago

---

**[Apple Plans Price Hikes as AI Companies Drive Up Chip Costs](https://www.pymnts.com/apple/2026/apple-plans-price-hikes-as-ai-companies-drive-up-chip-costs/)**

Apple plans to raise prices due to a surge in the costs of memory and storage chips, CEO Tim Cook told The Wall Street Journal (WSJ) in a report posted

PYMNTS.com • 3h ago

---

**[State Farm’s AI Plan for Sales Agents Sparks Uproar. ‘A Real Slap in the Face.’](https://www.wsj.com/finance/state-farms-ai-plan-for-sales-agents-sparks-uproar-a-real-slap-in-the-face-6453e2cb)**

WSJ • 19h ago

---

---

## HackerNews: "ai"

**[Sixty percent of US consumers say 'AI' in brand messaging is a turnoff](https://news.ycombinator.com/item?id=48569278)**

Original research from 2,000 decision-makers and consumers on AI brand visibility, content trust, and what brands need to do as the web feels less human. 74% say the internet feels less human than it did 10 years ago.

⬆️ 1024 • 💬 535 • 17h ago • [The Leading Enterprise Content Platform | WordPress VIP](https://wpvip.com/future-of-the-web-2026/)

---

**[Has AI already killed self-help nonfiction books?](https://news.ycombinator.com/item?id=48558489)**

⬆️ 397 • 💬 464 • 1d ago • [tim.blog](https://tim.blog/2026/06/12/has-ai-already-killed-nonfiction/)

---

**[Only 16 Percent of Americans Think AI Will Have a Positive Impact on Society](https://news.ycombinator.com/item?id=48573332)**

Although Wall Street loves AI, every day Americans are significantly less optimistic about the industry, a new report from Pew Research shows.

⬆️ 375 • 💬 455 • 12h ago • [TechCrunch](https://techcrunch.com/2026/06/17/only-16-percent-of-americans-think-ai-will-have-a-positive-impact-on-society-a-new-study-shows/)

---

**[My Homelab AI Dev Platform](https://news.ycombinator.com/item?id=48542433)**

Self-hosting OpenCode Web for GitOps style homelab changes.

⬆️ 363 • 💬 56 • 2d ago • [rsgm.dev](https://rsgm.dev/post/ai-dev-platform/)

---

**[AI demands more engineering discipline. Not less](https://news.ycombinator.com/item?id=48570948)**

⬆️ 359 • 💬 183 • 14h ago • [charitydotwtf.substack.com](https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline)

---

**[The founder's playbook: Building an AI-native startup](https://news.ycombinator.com/item?id=48566832)**

We share how AI-native founders are using Claude at every stage of the startup journey, with practical exercises, frameworks, and prompts.

⬆️ 222 • 💬 157 • 22h ago • [Claude](https://claude.com/blog/the-founders-playbook)

---

**[Launch HN: Adam (YC W25) – Open-Source AI CAD](https://news.ycombinator.com/item?id=48572553)**

CADAM is the open source text-to-CAD web application - Adam-CAD/CADAM

⬆️ 172 • 💬 84 • 13h ago • [GitHub](https://github.com/Adam-CAD/CADAM)

---

**[Show HN: I wrote a C++ ray tracer from scratch without AI](https://news.ycombinator.com/item?id=48538833)**

C++ Path Tracer from scratch with zero third-party libraries. - themartiano/luz

⬆️ 155 • 💬 64 • 2d ago • [GitHub](https://github.com/themartiano/luz)

---

**[Microsoft turns to AWS as GitHub faces AI capacity crunch](https://news.ycombinator.com/item?id=48549918)**

Microsoft is adding AWS capacity for GitHub after AI-driven usage strained the developer platform, exposing Azure constraints and the infrastructure cost of agentic coding.

⬆️ 154 • 💬 75 • 2d ago • [RuntimeWire](https://runtimewire.com/article/microsoft-github-aws-ai-capacity-crunch)

---

**[Can Europe train a frontier AI model on the compute it owns?](https://news.ycombinator.com/item?id=48541014)**

A sourced model and short report: can Europe train a sovereign frontier AI model on the public compute it already owns, while gigawatt datacenters wait years for grid power? - sammysltd/euromesh

⬆️ 142 • 💬 293 • 2d ago • [GitHub](https://github.com/sammysltd/euromesh)

---

---

## YouTube Videos: "ai"

**[Jeff Bezos Makes Shocking AI Prediction and the Future of Jobs](https://www.youtube.com/watch?v=qI1tLQF-_9A)**

Speaking at the VivaTech conference in Paris on June 17, the Jeff Bezos pushed back on fears that artificial intelligence will ...

📺 New York Post

👁️ 3K • 👍 89 • 💬 23 • ⏱️ 5:28 • 5h ago

---

**[We Might Actually Need to Stop AI](https://www.youtube.com/watch?v=CvA8-aScqio)**

My FREE AI OS Course: ...

📺 Nate Herk | AI Automation

👁️ 33K • 👍 945 • 💬 258 • ⏱️ 12:28 • 1d ago

---

**[The AI Skills Nobody is Teaching (And Everyone Needs) | AI Expert Ethan Mollick](https://www.youtube.com/watch?v=9YMYVb1ASCg)**

Be honest: AI makes you a little nervous. Maybe you're afraid it'll take your job. Maybe you're overwhelmed by all the advice about ...

📺 Simon Sinek

👁️ 40K • 👍 1K • 💬 99 • ⏱️ 58:36 • 1d ago

---

**[Maths is Cooked: AI&#39;s Latest Breakthrough -- And What&#39;s Next](https://www.youtube.com/watch?v=k5dZmMa0OIA)**

Take back your personal data with Incogni! Use code Sabine at the link below and get 60% off annual plans: ...

📺 Sabine Hossenfelder

👁️ 165K • 👍 9K • 💬 2K • ⏱️ 7:39 • 14h ago

---

**[Google Just Revealed What Comes After AGI And It’s Shocking](https://www.youtube.com/watch?v=haB_od-xCWY)**

Google DeepMind just dropped a massive paper called From AGI to ASI, and the message is bigger than another AI release.

📺 AI Revolution

👁️ 81K • 👍 3K • 💬 393 • ⏱️ 13:33 • 2d ago

---

**[AI Will Never Be The Same After This](https://www.youtube.com/watch?v=vHFIvXE7hcg)**

LIMITLESS HQ ⬇️ NEWSLETTER: https://limitlessft.substack.com/ FOLLOW ON X: https://x.com/LimitlessFT SPOTIFY: ...

📺 Limitless Podcast

👁️ 10K • 👍 273 • 💬 42 • ⏱️ 29:26 • 1d ago

---

**[The People Building AI Just Revealed Their End Goal](https://www.youtube.com/watch?v=RopkgBzHD8s)**

discord.gg/nickjones Source media: https://youtu.be/b1_7Pt0DJos?si=r1cZlHFuFNq6Nj8W ...

📺 Nick Jones

👁️ 20K • 👍 866 • 💬 170 • ⏱️ 27:00 • 1d ago

---

**[New #1 open-source AI model is here!](https://www.youtube.com/watch?v=6d__WOpZswY)**

GLM 5.2 review. New best open source AI model. #ai #aitools #llm #ainews #agi #singularity #gpt #deepseek Thanks to our ...

📺 AI Search

👁️ 215K • 👍 8K • 💬 880 • ⏱️ 29:57 • 1d ago

---

**[Fable 5 Replacement Just Dropped: Fusion (Fable Level AI)](https://www.youtube.com/watch?v=wzay-VWjoRM)**

Fable 5 is gone, and now the big question is simple: what comes next? OpenRouter just introduced Fusion, a system that sends ...

📺 AI Revolution

👁️ 16K • 👍 648 • 💬 46 • ⏱️ 15:28 • 1d ago

---

**[You&#39;re Not Behind (Yet): Master AI in 10 Mins 🔥](https://www.youtube.com/watch?v=60GaSpOnA48)**

AI is not the future. It's already here, and this video will make you better at it than 99% of people. This is the Ultimate AI ...

📺 Tharun Speaks

👁️ 51K • 👍 4K • 💬 389 • ⏱️ 10:34 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)**

*Yuxin Lu*

A 12B parameter GGUF model fine-tuned on verifiable Python coding data with chain-of-thought reasoning, designed for local execution on consumer hardware (~4.5GB VRAM minimum) for offline coding assistance and problem-solving.

`text-generation` `11.9B`

⬇️ 146,784 • ❤️ 1,515 • 3h ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 666 • ❤️ 1,074 • 19h ago

---

**[MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)**

*MiniMax*

MiniMax-M3 is a native multimodal model with 1M context, excelling in image-text-to-text tasks. It features MiniMax Sparse Attention (MSA) for efficient long context processing and demonstrates frontier-level performance in coding and agentic benchmarks.

`image-text-to-text` `427.0B`

⬇️ 42,198 • ❤️ 1,070 • 1d ago

---

**[Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)**

*Moonshot AI*

Kimi K2.7 Code is a 1T parameter Mixture-of-Experts (MoE) model optimized for complex, long-horizon coding tasks and software engineering workflows. It features a 256K context length and a MoonViT vision encoder, excelling in agentic coding capabilities with improved token efficiency.

`image-text-to-text` `1058.6B`

⬇️ 172,727 • ❤️ 850 • 2d ago

---

**[diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)**

*Google*

DiffusionGemma 26B A4B-it is a multimodal, instruction-tuned generative model that uses discrete text diffusion for high-speed text generation from text, image, and video inputs. It excels at tasks requiring rapid inference, long context understanding (up to 256K tokens), and multimodal reasoning, making it suitable for applications like advanced chatbots, content creation, and complex document analysis.

`image-text-to-text` `25.8B`

⬇️ 460,173 • ❤️ 980 • 7d ago

---

**[VibeThinker-3B](https://huggingface.co/WeiboAI/VibeThinker-3B)**

*WeiboAI*

VibeThinker-3B is a 3B-parameter text-generation model optimized for verifiable reasoning tasks like mathematics and coding, achieving competitive performance on benchmarks such as IMO-AnswerBench and LeetCode contests. It excels at multi-step reasoning, constraint satisfaction, and answer verification, but is not recommended for tool-calling or agent-based programming.

`text-generation` `3.1B`

⬇️ 1,950 • ❤️ 325 • 1d ago

---

**[Rio-3.5-Open-397B](https://huggingface.co/prefeitura-rio/Rio-3.5-Open-397B)**

*Prefeitura do Rio de Janeiro (City of Rio de Janeiro)*

Rio 3.5 Open 397B is a frontier-class, open-source image-text-to-text AI model post-trained from Qwen 3.5 397B. It excels in agentic coding, STEM, multilingual tasks, and multimodal reasoning, featuring a 1M context window and SwiReasoning for enhanced accuracy and efficiency.

`image-text-to-text` `403.4B`

⬇️ 189,986 • ❤️ 319 • 3d ago

---

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 130,389 • ❤️ 2,141 • 5d ago

---

**[Qwopus3.6-27B-Coder-MTP-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-Coder-MTP-GGUF)**

*Jackrong*

Qwopus-3.6-27B-Coder is a 27B parameter multimodal model fine-tuned for agentic coding and tool-use reasoning. It excels at repository-level code generation, debugging, and structured tool orchestration, leveraging trace inversion and native long-context support for complex developer workflows.

`image-text-to-text` `460.7M`

⬇️ 99,909 • ❤️ 238 • 3d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 2,876,624 • ❤️ 1,943 • 2mo ago

---

---

## HuggingFace Papers: 🔥 Trending

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 235 • 💬 4 • ⭐ 8,135 • 27d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 30 • 💬 1 • ⭐ 21,939 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 97 • 💬 4 • ⭐ 87,024 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[FastContext: Training Efficient Repository Explorer for Coding Agents](https://huggingface.co/papers/2606.14066)**

*Shaoqiu Zhang, Maoquan Wang, Yuling Shi et al. (8 authors)*

🏢 Microsoft

FastContext separates repository exploration from code solving in LLM agents using specialized exploration models that reduce token consumption and improve resolution rates.

▲ 81 • 💬 3 • ⭐ 508 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2606.14066) • [💻 code](https://github.com/microsoft/fastcontext) • [🔗 project](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 18 • 💬 1 • ⭐ 82,803 • 16d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 42 • 💬 4 • ⭐ 30,608 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[JoyAI-VL-Interaction: Real-Time Vision-Language Interaction Intelligence](https://huggingface.co/papers/2606.14777)**

*Dingyu Yao, Junhao Zhou, Chenxu Yang et al. (15 authors)*

🏢 JD.com Open Source

A vision-language model operates continuously in real-time, making autonomous decisions about when to respond or delegate, enabling interactive systems that perceive and act upon environmental changes without user prompting.

▲ 177 • 💬 2 • ⭐ 266 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2606.14777) • [💻 code](https://github.com/jd-opensource/JoyAI-VL-Interaction) • [🔗 project](https://joyai-vl-video-future-academy-jd.github.io/JoyAI-VL-Interaction/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 80 • 💬 7 • ⭐ 77,552 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[VibeThinker-3B: Exploring the Frontier of Verifiable Reasoning in Small Language Models](https://huggingface.co/papers/2606.16140)**

*Sen Xu, Shixi Liu, Wei Wang et al. (9 authors)*

🏢 WeiboAI

VibeThinker-3B demonstrates that compact models can achieve state-of-the-art performance on verifiable reasoning tasks through specialized training techniques, challenging conventional scaling assumptions.

▲ 89 • 💬 1 • ⭐ 903 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2606.16140) • [💻 code](https://github.com/WeiboAI/VibeThinker) • [🔗 project](https://github.com/WeiboAI/VibeThinker)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 167 • 💬 2 • ⭐ 67,886 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 73.2k • 🔱 9.4k • 19h ago

---

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 32.7k • 🔱 1.5k • 1d ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 9.6k • 🔱 870 • 4h ago

---

**[KunAgent/Kun](https://github.com/KunAgent/Kun)**

AI agent workspace with Code and Write modes built into your application.

`TypeScript`

⭐ 4.4k • 🔱 388 • 15m ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 3.6k • 🔱 399 • 1m ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 3.5k • 🔱 356 • 17h ago

---

**[nexu-io/html-video](https://github.com/nexu-io/html-video)**

Programmatic video for coding agents — HTML to video on your laptop. Turn HTML, CSS & data into real MP4s with pluggable render engines, 21 templates, AI soundtrack. Apache-2.0, no per-render fees. An official project by the Open Design team.

`HTML` `ai-agent` `apache-2` `coding-agent` `css` `ffmpeg`

⭐ 3.3k • 🔱 392 • 19h ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 2.1k • 🔱 191 • 19h ago

---

**[jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo)**

JoyAI-Echo: Pushing the Frontier of Long Audio-Visual Generation

`Python`

⭐ 1.6k • 🔱 143 • 1d ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 1.5k • 🔱 109 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
