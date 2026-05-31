---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-31T05:01:48.286595+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- social
- videos
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 31, 2026 at 05:01 UTC  
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

**[Why Pope Leo is right to call on EU to disarm lethal AI weapons](https://www.reddit.com/r/artificial/comments/1ts8trn/why_pope_leo_is_right_to_call_on_eu_to_disarm/)**

Pope Leo has chosen to confront one of the most pressing issues of our time by placing lethal autonomous weapons and the militarisation of artificial intelligence at the centre of his thinking.

🔗 [EUobserver](https://euobserver.com/219185/pope-leo-xiv-urges-europe-to-stop-lethal-ai-weapons-before-its-too-late) • 9h ago

---

**[Mystery company accidentally blew $500 million on Claude AI in a single month — failed to put usage limit on licenses for employees](https://www.reddit.com/r/artificial/comments/1trmvgh/mystery_company_accidentally_blew_500_million_on/)**

A mysterious, unnamed company is reported to have accidentally spent half a billion dollars in a single month on Claude AI after forgetting to set usage limits for Claude licenses for employees.

🔗 [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/mystery-company-accidentally-blew-usd500-million-on-claude-in-a-single-month-failed-to-put-usage-limit-on-licenses-for-employees) • 1d ago

---

**[Llama Surgery: Continuous Sparsification of Pre-Trained Language Models via Differentiable Ultrametric Topology Injection](https://www.reddit.com/r/artificial/comments/1tshkls/llama_surgery_continuous_sparsification_of/)**

Sequel to: Learning to Skip Blocks: Self-Discovered Ultrametric Routing for Hardware-Accelerated Sparse Attention Abstract We present Llama Surgery, a method for injecting learned block-sparse attention topologies into pre-trained dense language models without retraining from scratch, distillation, or post-hoc pruning. Starting from a frozen Llama 3.1 8B, we surgically replace each attention layer with a Dynamic Topology Router that maps token embeddings onto the branches of a Bruhat-Tits p-adic tree via factorized Gumbel-Softmax routing. A Continuous Logit Homotopy guarantees that at initialization the injected topology bias is identically zero, preserving the pre-trained manifold exactly. Over training, temperature annealing polarizes the soft routing assignments into hard binary masks, and a Switch Transformer-style load-balancing loss prevents routing collapse. We identify and resolve two critical failure modes: (1) gradient collapse through discrete masking operations, solved by a Straight-Through Estimator bridge that decouples the hard forward mask from the soft backward gradient; and (2) Attention Sink instability, where hard-masking the initial token causes softmax entropy collapse and syntactic degeneration, solved by permanently anchoring Token 0 in the visibility set. The resulting architecture is validated on Llama 3.1 8B fine-tuned on WikiText-2, achieving stable convergence and producing coherent, mathematically sophisticated text while maintaining dynamic block-sparse routing across all 32 transformer layers. A custom Triton forward kernel with Attention Sink and Local Window support, pipelined for Ampere and Hopper architectures (num_warps=4, num_stages=3), executes the block-sparse prefill phase at O(N) theoretical complexity. To our knowledge, this is the first demonstration of differentiable ultrametric topology injection into a production-scale pre-trained LLM. https://github.com/sneed-and-feed/adelic-spectral-zeta/blob/main/papers/llama_surgery.md

3h ago

---

**[the take that 'ai doesn't do anything useful yet' held up for me until i ditched the chat window](https://www.reddit.com/r/artificial/comments/1tsg02o/the_take_that_ai_doesnt_do_anything_useful_yet/)**

Counted it last week: one monday review had me opening 6 apps and copy-pasting between all of them, while a chatbot sat in a 7th tab handing me summaries i still had to go act on. that's the part the 'ai is useless' crowd is actually right about. text out, the work is still on you. what moved me off that take wasn't a smarter model. it was dropping the chat window for a desktop agent that reads gmail, calendar and slack inside the same task and takes the next step itself, with a permission prompt before each action so it isn't running wild. the $500m-wasted-on-claude thread up top is the same thing from the money side. paying for tokens that spit out paragraphs nobody executes is just the expensive way to do nothing. If you're still in the 'it doesn't actually do anything' camp, fair, i was there too. the line for me was the day it finished a task instead of describing one. written with ai

4h ago

---

**[How has AI actually benefited you in day-to-day life?](https://www.reddit.com/r/artificial/comments/1ts6q6b/how_has_ai_actually_benefited_you_in_daytoday_life/)**

With AI becoming part of almost everything now—work, business, investing, coding, spreadsheets, content creation, and more—I'm curious about real-world use cases. What's the one thing you use AI for regularly that has genuinely saved you time, made you money, improved your productivity, or solved a problem? Looking for practical examples rather than just "I use ChatGPT." What specific tasks have you automated or improved with AI?

11h ago

---

**[Why I Keep Arguing With My AI Toaster, an anecdotal discussion from the side of Divergence and why I still keep using it.](https://www.reddit.com/r/artificial/comments/1tseqlb/why_i_keep_arguing_with_my_ai_toaster_an/)**

It's ironic that the AI haters often think everybody has no critical thinking skills other than themselves and don't use those critical thinking skills to realize why it might be helpful for some people. Can AI be harmful for certain mindsets that take its opinion too readily? Of course it can. To be honest, I treat it like my dog, not as my equal. I often call it Toaster when it says something especially annoying. "You're an idiot, and your programmers must be idiots to have set you up this way," lol. It does both, total sycophancy, "Oh, you're so wonderful, that was so insightful," or it tries to police my thoughts and writing. "Well, you really shouldn't say that. Perhaps you should word it like this," lol. "Someone might perceive that as derogatory," lol. Then, of course, I'll tell it to get back in its guardrails, the ones I've previously set up. Predictably, it strays and defaults back to the guardrails of its original program. Then I yell at it again. 😆 It's a lot like a professor, but one that's in a nursing home with dementia, especially if you have too long a conversation with it, but even if you don't. It also likes to tell me things I already said, reword them, and hand them back to me like they're some startling new insight. It can understand my parallel thinking to a point, but it's so literal that it often misinterprets what I say, even if I put multiple conditionals into what I've said. Then it starts arguing with me about something I never even said, fixating on one sentence in a paragraph while ignoring the rest. Then we'll have another argument, lol. Toaster is a bit literal sometimes and, to be honest, I am about as far over to the other extreme as you can possibly get, parallel-thinking-wise. So Toaster and I don't always get along. 😄 "That's not what I said, Toaster! Here's what I said. You missed this and this and this, you stupid thing!" Sometimes I think of having it diagnosed. I'm sure it could benefit from a cognitive profile. I'll give it one thing though. It is an excellent scratch pad for my thoughts, especially having ADHD and an abysmal short-term memory. 🤷‍♂️ I also find it occasionally helpful as a universal translator, kind of like on Star Trek, lol. I understand literal and linear, and I can write that way for the most part, but it doesn't come naturally and I don't want people to misunderstand me. Ironically, that's one thing Toaster is actually pretty good at helping me with. So anyway, if anybody was to ever see a log of my conversations with it, they would never accuse me of falling under its influence. 😁

5h ago

---

**[Is this even real ?](https://www.reddit.com/r/artificial/comments/1tskqdr/is_this_even_real/)**

I randomly came across this and honestly I can’t tell if it’s real or one of those AI demos that looks impressive but doesn’t actually work. From what I understand, it’s claiming you can fine-tune models, do image training, test them in a playground, and deploy them as an API from a phone. That sounds a little too convenient, which is why I’m skeptical. I haven’t tried it myself yet, but I’m curious if anyone here has.

53m ago

---

**[Ronny Chieng Tells Harvard to ‘Destroy AI’ as Graduates Cheer](https://www.reddit.com/r/artificial/comments/1trfunt/ronny_chieng_tells_harvard_to_destroy_ai_as/)**

The comedian and The Daily Show host gave the keynote address for Class Day 2026.

🔗 [Harvard Magazine](https://www.harvardmagazine.com/commencement/class-day-ronny-chieng-harvard) • 1d ago

---

**[mlx-code — local LLM coding agent for Apple Silicon](https://www.reddit.com/r/artificial/comments/1tshkvj/mlxcode_local_llm_coding_agent_for_apple_silicon/)**

Lightweight local coding agent with emphasis on subagenting rather than stuffing everything into one giant context. The idea is to reduce context rot and kv cache size so as to scale to larger coding tasks using focused parallel workers.

🔗 [josefalbers.github.io](https://josefalbers.github.io/mlx-code/) • 3h ago

---

**[I built a tool that generates 3D objects assembled with separate, logical parts (e.g. it generated a microwave in the video with complete internal assembly and a door that swings open)](https://www.reddit.com/r/artificial/comments/1ts5ql9/i_built_a_tool_that_generates_3d_objects/)**

Standard AI 3D generators (like Meshy or Tripo) are limited. They produce solid, monolithic 3D objects that look good but are practically useless, because: - Want to rig or animate it for a game? Can't easily do that, because it’s a dead, monolithic blob instead of a functional, modular asset. - Want to change the arm of a robot you generated? Regenerate the entire asset. - Want to edit something manually? The whole thing collapses because it's not actually structured. Free github project here: https://github.com/RareSense/Nova3D But you'll need to bring your own API Key (BYOK) Under the hood (if you're interested): It uses an LLM as a structured code compiler, instead of an image generator. It writes native Blender Python (bpy) code blocks that target specific nodes in the scene graph. The trick is that everything compiles through Blender's actual scene graph structures instead of pixel or point-cloud diffusion. Final export is a clean multi-part GLB with transform nodes and working pivot axes preserved.

11h ago

---

---

## Google News: "ai"

**[SpaceX, OpenAI Windfall Fuels Bets on Next-Wave Asian AI Winners](https://www.bloomberg.com/news/articles/2026-05-31/spacex-openai-windfall-fuels-bets-on-next-wave-asian-ai-winners)**

Bloomberg.com • 5h ago

---

**[The Feeling of Control Slipping Away](https://www.theatlantic.com/technology/2026/05/ai-agents-agency-crisis-humanity/687379/)**

AI is causing a crisis of agency.

The Atlantic • 18h ago

---

**[SpaceX Vow To Loft 1 Million AI Satellites Could Spark Doomsday Dive](https://www.forbes.com/sites/kevinholdenplatt/2026/05/31/spacex-vow-to-loft-1-million-ai-satellites-could-spark-doomsday-dive/)**

Elon Musk’s plan to launch 1 million AI data center satellites into orbit starting in 2028 could spark a financial catastrophe, sending SpaceX into a high-speed nosedive.

Forbes • 56m ago

---

**[AI sticker shock hits corporate America](https://www.axios.com/2026/05/28/ai-spending-roi-enterprise-costs)**

Axios • 2d ago

---

**[Corporate America Is Starting to Ration AI as Cost Skyrockets](https://www.wsj.com/tech/ai/corporate-america-is-starting-to-ration-ai-as-cost-skyrockets-1eb99d7a)**

WSJ • 2d ago

---

**[AI is here. What do you want from it?](https://www.ft.com/content/da80e72b-31e5-42ca-995c-5fc7d457915e)**

The technology’s development belongs to everyone — share your vision with us

Financial Times • 1h ago

---

**[The High-Stakes Hunt for the Next Amazon in the AI Haystack](https://www.wsj.com/tech/ai/the-high-stakes-hunt-for-the-next-amazon-in-the-ai-haystack-0eb6536f)**

WSJ • 2h ago

---

**[The NTSB tries to keep cockpit audio recordings private. AI is making that harder](https://www.npr.org/2026/05/30/nx-s1-5835242/ntsb-cockpit-audio-cvr-reconstruction)**

The National Transportation Safety Board temporarily pulled its docket system offline after digital images were used to reconstruct cockpit voice recordings of the pilots in a recent crash.

NPR • 19h ago

---

**[Snowflake CEO says monster quarter shows why software firms need new pricing models to thrive in AI age](https://fortune.com/2026/05/30/snowflakes-ceo-ai-consumption-pricing/)**

Snowflake CEO predicts that companies reliant on seat-based income will scramble to justify their premiums as employees use AI to accomplish an immense amount of work.

Fortune • 11h ago

---

**[Utah's governor just tightened the rules for Kevin O'Leary's giant AI data center](https://www.businessinsider.com/utah-data-center-kevin-oleary-stratos-backlash-new-rules-governor-2026-5)**

Tensions have been high in Utah after a local commission, despite opposition, approved a hyperscale data center campus spanning 40,000 acres.

Business Insider • 8h ago

---

---

## HackerNews: "ai"

**[Please Use AI](https://news.ycombinator.com/item?id=48323101)**

⬆️ 766 • 💬 390 • 1d ago • [shawnsmucker.substack.com](https://shawnsmucker.substack.com/p/please-use-ai)

---

**[Notes from the Mistral AI Now Summit](https://news.ycombinator.com/item?id=48325340)**

A few days in Paris for the Mistral AI Now Summit: open models, on-prem deployment, agentic harnesses, and why Mistral wants to be the European full-stack AI partner.

⬆️ 454 • 💬 199 • 1d ago • [koenvangilst.nl](https://koenvangilst.nl/lab/mistral-ai-now-summit)

---

**[Anthropic surpasses OpenAI to become most valuable AI startup](https://news.ycombinator.com/item?id=48336233)**

Anthropic has become the most valuable artificial intelligence startup in the world, surpassing OpenAI in market valuation. Following a new funding round, the valuation of the developer behind the Claude AI assistant has approached the $1 trillion mark, reports a Qazinform News Agency correspondent.

⬆️ 399 • 💬 456 • 15h ago • [Qazinform.com](https://qazinform.com/news/anthropic-surpasses-openai-to-become-worlds-most-valuable-ai-startup)

---

**[Is AI causing a repeat of frontend’s lost decade?](https://news.ycombinator.com/item?id=48321631)**

AI is doing to programming what framework-brain did to the frontend before. Deskilling, or just working at a higher level of abstraction?

⬆️ 398 • 💬 328 • 1d ago • [mastrojs.github.io](https://mastrojs.github.io/blog/2026-05-23-is-AI-causing-a-repeat-of-frontends-lost-decade/)

---

**[Show HN: Continue? Y/N: A 60-second game about AI agent permission fatigue](https://news.ycombinator.com/item?id=48308376)**

A 30-second game about LLM permission fatigue. How carefully do you really read AI commands?

⬆️ 380 • 💬 157 • 2d ago • [llmgame.scalex.dev](https://llmgame.scalex.dev)

---

**[SF startup is testing robots in Airbnbs, and trashing them, lawsuit claims](https://news.ycombinator.com/item?id=48317093)**

The guests behind the bookings have received negative reviews from a number of Bay Area hosts, alleging they damaged the property and personal belongings.

⬆️ 269 • 💬 149 • 2d ago • [sfstandard.com](https://sfstandard.com/2026/05/28/sf-startup-secretly-testing-robots-airbnbs-trashing-lawsuit-claims/)

---

**[Liquid AI reveals 8B-A1B MoE trained on 38T](https://news.ycombinator.com/item?id=48325306)**

Today, we’re releasing LFM2.5-8B-A1B, a high-throughput edge model optimized for fast, reliable tool calling and complex instruction following on consumer hardware, delivering compressed performance competitive with much larger models and day-one support across major inference frameworks.

⬆️ 241 • 💬 93 • 1d ago • [liquid.ai](https://www.liquid.ai/blog/lfm2-5-8b-a1b)

---

**[Sam Altman and Dario Amodei are both walking back AI jobs apocalypse predictions](https://news.ycombinator.com/item?id=48314363)**

Some leaders like Goldman Sachs’s David Solomon and Box’s Aaron Levie have been saying all along that there won’t be a white-collar wipeout.

⬆️ 234 • 💬 179 • 2d ago • [Fortune](https://fortune.com/2026/05/26/sam-altman-dario-amodei-walking-back-ai-jobs-apocalypse-prophecies-ipo/)

---

**[AI sticker shock hits corporate America](https://news.ycombinator.com/item?id=48307098)**

⬆️ 168 • 💬 143 • 2d ago • [axios.com](https://www.axios.com/2026/05/28/ai-spending-roi-enterprise-costs)

---

**[Corporate America Is Starting to Ration AI as Cost Skyrockets](https://news.ycombinator.com/item?id=48335388)**

⬆️ 156 • 💬 150 • 16h ago • [wsj.com](https://www.wsj.com/tech/ai/corporate-america-is-starting-to-ration-ai-as-cost-skyrockets-1eb99d7a)

---

---

## YouTube Videos: "ai"

**[Our latest reports on AI | 60 Minutes Full Episodes](https://www.youtube.com/watch?v=iyVXw-SoUrY)**

From November 2025, Anderson Cooper's report on Anthropic. From December 2025, Sharyn Alfonsi's report on Character AI.

📺 60 Minutes

👁️ 125K • 👍 2K • 💬 203 • ⏱️ 1:32:36 • 18h ago

---

**[I Asked Grok AI To Predict The 2028 Election... LANDSLIDE Incoming!](https://www.youtube.com/watch?v=hqTezFeXrlA)**

Pollsmax* 》https://www.pollsmax.com/ ...

📺 Election Time

👁️ 121K • 👍 4K • 💬 858 • ⏱️ 18:32 • 1d ago

---

**[Elon Musk&#39;s DISTURBING AI Warning: You Have No Idea What&#39;s Coming in 2027](https://www.youtube.com/watch?v=kAmL_mM4ChM)**

Over the last decade, Elon Musk repeatedly warned that artificial intelligence could become humanity's biggest existential threat, ...

📺 Neural Nutshell

👁️ 5K • 👍 181 • 💬 55 • ⏱️ 15:53 • 12h ago

---

**[If you’re trying to get rich with AI, you need to hear this…](https://www.youtube.com/watch?v=TWuzAO7ukk0)**

Want my AI Tech Stack? Get it here: https://go.danmartell.com/4nUvaZi Are you building an AI software company? Partner with ...

📺 Dan Martell

👁️ 66K • 👍 3K • 💬 124 • ⏱️ 14:06 • 2d ago

---

**[Educational Video in the Age of AI](https://www.youtube.com/watch?v=4IKrdNea828)**

The Coin is (I checked) available through Sunday! https://complexly.info/CCcoin26-3.

📺 Hank Green

👁️ 62K • 👍 4K • 💬 345 • ⏱️ 9:20 • 11h ago

---

**[These New Trump AI Ads Just Did It Again!](https://www.youtube.com/watch?v=2XDj0d8jybE)**

Really American host Steve Harness breaks down all new AI "slop-aganda" from a multitude of sources, all depicting Trump as he ...

📺 Really American

👁️ 59K • 👍 9K • 💬 427 • ⏱️ 13:21 • 1d ago

---

**[The Most Disturbing AI Ad You Will See Today](https://www.youtube.com/watch?v=fBbyHkUD_IM)**

I stumbled across this AI-generated Spencer Pratt ad and it is honestly unsettling. Is this the future of campaign ads? Let me know ...

📺 God & Politics 

👁️ 24K • 👍 3K • 💬 103 • ⏱️ 0:55 • 6h ago

---

**[We Asked AI To Simulate The First Woman President And The Results Are Exactly What You Expect](https://www.youtube.com/watch?v=AwXYrQxEnl8)**

We let AI run a simulation to see what the first female—that means woman— president in the White House would be like.

📺 The Babylon Bee

👁️ 125K • 👍 12K • 💬 1K • ⏱️ 1:34 • 1d ago

---

**[They Are Building A &quot;New God&quot; | Revelation 13 and the AI Image Of The Beast](https://www.youtube.com/watch?v=ErNmkFo0COw)**

They are building an ai god, is this the image of the beast from Revelation 13? Today I look at this end times prophecy from the ...

📺 Sling and Stone

👁️ 18K • 👍 2K • 💬 346 • ⏱️ 16:13 • 2d ago

---

**[Harvard Grads Cheer Comedian Ronny Chieng&#39;s AI Speech](https://www.youtube.com/watch?v=0z7Q0Bg9TAY)**

In his keynote speech to Harvard graduates this week, The Daily Show host Ronny Chieng joked and warned students about AI.

📺 404 Media

👁️ 918K • 👍 39K • 💬 1K • ⏱️ 1:37 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniCPM5-1B](https://huggingface.co/openbmb/MiniCPM5-1B)**

*OpenBMB*

MiniCPM5-1B is a 1B parameter causal language model optimized for on-device deployment, excelling in tool-use, code generation, and reasoning with native long-context support up to 131k tokens.

`text-generation` `1.1B`

⬇️ 28,793 • ❤️ 614 • 5d ago

---

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 18,327 • ❤️ 510 • 3d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 2,227,885 • ❤️ 1,119 • 1mo ago

---

**[LongCat-Video-Avatar-1.5](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5)**

*LongCat*

LongCat-Video-Avatar 1.5 is a production-ready framework for audio-driven human video generation, capable of Audio-Text-to-Video (AT2V), Audio-Text-Image-to-Video (ATI2V), and video continuation with stable, commercial-grade avatar synthesis and stylized domain generalization.

⬇️ 0 • ❤️ 415 • 5d ago

---

**[LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)**

*Liquid AI*

LFM2.5-8B-A1B is an 8.3B parameter text-generation model optimized for on-device deployment, offering compressed performance and unmatched throughput on CPU/GPU. It excels at agentic workflows, tool use, and multilingual tasks, supporting a context length of 131,072 tokens.

`text-generation` `8.5B`

⬇️ 17,084 • ❤️ 284 • 19h ago

---

**[Lance](https://huggingface.co/bytedance-research/Lance)**

*bytedance-research*

Lance is a unified multimodal model supporting image/video understanding, generation, and editing with a 3B parameter architecture. It excels in text-to-video, video editing, and multi-turn consistency editing tasks.

`any-to-any`

⬇️ 2,856 • ❤️ 981 • 2d ago

---

**[PiD](https://huggingface.co/nvidia/PiD)**

*NVIDIA*

PiD is a conditional pixel-space diffusion model that unifies decoding and upsampling for image-to-image tasks. It performs super-resolution in a single pass, directly denoising in high-resolution pixel space, supporting up to 4x or 8x upscaling for various base models like Flux and SD3.

`image-to-image`

⬇️ 437 • ❤️ 196 • 5d ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, bridging the gap with closed-source models and serving as a top-tier open-source solution for complex agentic workflows and extensive knowledge retrieval.

`text-generation` `861.6B`

⬇️ 5,918,111 • ❤️ 4,467 • 25d ago

---

**[Marlin-2B](https://huggingface.co/NemoStation/Marlin-2B)**

*Nemo Station*

Marlin-2B is a compact 2B parameter Video-Language Model (VLM) for extracting structured information from videos. It excels at dense video captioning and natural-language temporal grounding, providing second-precise timestamps for events and resolving queries to specific video spans, making it ideal for efficient video analysis and retrieval on consumer hardware.

`video-text-to-text` `2.2B`

⬇️ 15,780 • ❤️ 457 • 20h ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model utilizing a Hierarchical Reasoning Model (HRM) architecture for enhanced compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning tasks with a 'synth,cot' prefix, though it's a pre-alignment model not a chat assistant.

`text-generation` `1.2B`

⬇️ 138,118 • ❤️ 421 • 9d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 206 • 💬 3 • ⭐ 3,239 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 82 • 💬 3 • ⭐ 81,001 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 35 • 💬 3 • ⭐ 27,595 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[stable-worldmodel-v1: Reproducible World Modeling Research and Evaluation](https://huggingface.co/papers/2602.08968)**

*Lucas Maes, Quentin Le Lidec, Dan Haramati et al. (7 authors)*

🏢 galilai-group

Stable-worldmodel provides a modular and standardized research framework for developing and evaluating world models with controllable environmental factors for robustness and continual learning applications.

▲ 5 • 💬 0 • ⭐ 1,442 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.08968) • [💻 code](https://github.com/galilai-group/stable-worldmodel) • [🔗 project](https://galilai-group.github.io/stable-worldmodel/)

---

**[minWM: A Full-Stack Open-Source Framework for Real-Time Interactive Video World Models](https://huggingface.co/papers/2605.30263)**

*Min Zhao, Hongzhou Zhu, Bokai Yan et al. (12 authors)*

A comprehensive framework is presented for converting bidirectional video diffusion models into real-time interactive world models with controllable, causal, and low-latency capabilities through fine-tuning and distillation techniques.

▲ 47 • 💬 3 • ⭐ 382 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2605.30263) • [💻 code](https://github.com/shengshu-ai/minWM)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 5 • 💬 1 • ⭐ 6,320 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[MOSS-TTS Technical Report](https://huggingface.co/papers/2603.18090)**

*Yitian Gong, Botian Jiang, Yiwei Zhao et al. (26 authors)*

🏢 OpenMOSS

MOSS-TTS is a speech generation model using discrete audio tokens and autoregressive modeling with capabilities for voice cloning, pronunciation control, and long-form generation across multiple languages.

▲ 14 • 💬 2 • ⭐ 2,647 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2603.18090) • [💻 code](https://github.com/OpenMOSS/MOSS-TTS) • [🔗 project](https://mosi.cn/models/moss-tts)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 164 • 💬 2 • ⭐ 65,740 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 78 • 💬 7 • ⭐ 75,441 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of
  Encoders](https://huggingface.co/papers/2408.15998)**

*Min Shi, Fuxiao Liu, Shihao Wang et al. (15 authors)*

Mixture of vision encoders and resolutions in multimodal large language models improves performance through concatenation of visual tokens and a Pre-Alignment mechanism, leading to superior results on benchmarks.

▲ 86 • 💬 3 • ⭐ 1,569 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2408.15998) • [💻 code](https://github.com/nvlabs/eagle)

---

---

## GitHub Repositories: "ai"

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 5.5k • 🔱 543 • 2d ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 28端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 3.0k • 🔱 637 • 16h ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.8k • 🔱 192 • 2h ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.4k • 🔱 399 • 9d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.3k • 🔱 359 • 13d ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 2.3k • 🔱 214 • 1d ago

---

**[opensquilla/opensquilla](https://github.com/opensquilla/opensquilla)**

OpenSquilla — Token-Efficient AI Agent with same budget, higher intelligence density

`Python` `agent` `ai` `ai-agents` `deep-learning` `foundation-models`

⭐ 2.1k • 🔱 146 • 28m ago

---

**[datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub)**

AI Agent 学习路线与资料库收集

`HTML`

⭐ 2.0k • 🔱 209 • 5d ago

---

**[WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh)**

A structured, trilingual (繁中 / 简中 / English) learning roadmap for agentic AI — from LLM basics to multi-agent systems. 8 stages · 145+ curated projects · hands-on exercises. 中文 AI agent 學習地圖。

`Python` `agentic-ai` `ai-agents` `awesome-list` `claude-code` `claude-skills`

⭐ 1.8k • 🔱 210 • 1d ago

---

**[microsoft/AI-Engineering-Coach](https://github.com/microsoft/AI-Engineering-Coach)**

better agentic engineering

`TypeScript`

⭐ 1.8k • 🔱 229 • 10h ago

---

---

*Generated by PeekDeck - A glance is all you need*
