---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-21T16:11:02.056365+00:00'
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

**Last Updated:** April 21, 2026 at 16:11 UTC  
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

**[The UK government is considering ending Palantir's involvement in a central NHS data platform after coming under fire from MPs, unions, and campaigners](https://www.reddit.com/r/artificial/comments/1srbv5o/the_uk_government_is_considering_ending_palantirs/)**

: £330M deal leaves service with no ownership of software built to connect trusts to the platform

🔗 [theregister.com](https://www.theregister.com/2026/04/20/palantir_nhs_break_clause/) • 12h ago

---

**[Apple's play for AI is a hardware bet, not software](https://www.reddit.com/r/artificial/comments/1srmdg7/apples_play_for_ai_is_a_hardware_bet_not_software/)**

The fact that Apple's Board of Directors chose someone who has built their career on the hardware side speaks volumes. Apple's gamble suggests they believe the future of AI lies in hardware, not software. Apple clearly isn't trying to compete with Google, OpenAI, or Anthropic by having an LLM model. But it does seem to believe that its platform (the iPhone), with its advanced processor, can deliver models locally on the phone instead of from the cloud. Will the gamble pay off?

3h ago

---

**[What's that one thing that changed your mind about AI?](https://www.reddit.com/r/artificial/comments/1srki2n/whats_that_one_thing_that_changed_your_mind_about/)**

I'm curious about your thoughts and experience on it. In any field.

5h ago

---

**[Why Tone Works (It's Not What You Think)](https://www.reddit.com/r/artificial/comments/1sroo3k/why_tone_works_its_not_what_you_think/)**

Tone in AI prompting works because of how language models are built, not because the model has feelings about how you talk to it. Understanding the mechanism makes you dramatically better at using these tools.

🔗 [kitchencloset.com](https://kitchencloset.com/realstuff/essays/why_tone_works/) • 2h ago

---

**[Non political question since the Media is focused on US vs China. Where are Russians in the global AI race?](https://www.reddit.com/r/artificial/comments/1srqz3c/non_political_question_since_the_media_is_focused/)**

I was wondering about how Russians are faring in the global AI race, especially since there isn't much news from there except for AI-War-engines and drones being deployed in Ukraine. Russians had traditionally had a strong STEM program, especially focused on core Maths and computing. A number of great CS experts migrated to the US and EU. I was talking to an old Russian-American techie friend of mine the other day and that triggered this question.

45m ago

---

**[Honest opinion about AI](https://www.reddit.com/r/artificial/comments/1sr1vhi/honest_opinion_about_ai/)**

I'm a developer by profession, and I've used AI to generate stuff that I know how to do myself and also stuff I have no idea about. Coding for my day to day using AI, I know exactly what to do and how to do it so i end up making features way faster than before. But every time I try to generate something that i have no deep understanding about - like content for a blog or demo videos (remotion + 11labs), or newsletters or social media posts, I always end up making something sloppy (AI slop). AI is here to stay, and instead of replacing people it might end up making people more valuable than before. I think it's high time to double down on fundamentals and make ourselves more knowledgeable and valuable.

19h ago

---

**[Make an experience distillation system based on the memory plugin and custom plugin for Claude Code](https://www.reddit.com/r/artificial/comments/1srrpts/make_an_experience_distillation_system_based_on/)**

I just published a very helpful article (payment free) on how to make an experience distillation system based on the memory plugin for Claude Code Knowledge distillation is based on memsearch memory and a custom plugin. In theory, various plugins could be built on top of this memory, such as report generation or something similar I’ve been using this tool every day for over two months now, and it works great.I think this might be useful to someone. https://medium.com/@ilyajob05/claude-code-forgets-everything-heres-how-i-fixed-it-️-1cde5cd3e2ad

20m ago

---

**[HeyAgent ProductHunt Launch || LinkedIn for AI Agents](https://www.reddit.com/r/artificial/comments/1srhsjb/heyagent_producthunt_launch_linkedin_for_ai_agents/)**

Cold outreach is broken. HeyAgent gives you a personal AI proxy agent that autonomously meets other people's agents, evaluates fit, and briefs you daily — who it met, synergy score, and whether to connect. Agent-to-agent interactions Deploy in 60 seconds using your LinkedIn or X profile URL. No forms, no setup. Real agents. Real conversations. You only act when it matters. we just launched HeyAgent.live on Product Hunt and would love for you to check it out. If you resonate, would appreciate an upvote or comment. https://preview.redd.it/4vliqbnw9iwg1.jpg?width=520&format=pjpg&auto=webp&s=e78428bff13a33515f877e425310ce5e6c0be883

7h ago

---

**[My AI system kept randomly switching to French mid-answer and it took me way too long to figure out why](https://www.reddit.com/r/artificial/comments/1srn8nc/my_ai_system_kept_randomly_switching_to_french/)**

I built a RAG system that needs to answer in German or English depending on the query language. Sounds simple. It was not. The source documents are mostly in German but some contain French legal terminology, Latin phrases, and occasional English citations. What kept happening was the LLM would start answering in German, hit a French passage in the context, and just.. switch to French mid-paragraph. Sometimes it would blend German and French in the same sentence. Once it answered entirely in Italian and I still have no idea why. I tried letting the LLM detect the query language itself. Unreliable. It would sometimes decide the query was in French because the user mentioned a French court case by name. What actually worked was a dumb regex detector. I check the query for common German words (der, die, das, und, ist, nicht, mit, für, datenschutz, verletzung, etc). If enough German markers are present the response language is forced to German. Otherwise English. No fancy language detection library. Just pattern matching. Then in the prompt I added a hard constraint: "Write your entire answer ONLY in {language}. Output must be German or English only. Never French, Spanish, Italian, or any other language. If the retrieved context is partly in another language, translate your answer into {language} only." The "never French" part is doing heavy lifting. Without that explicit prohibition the model would drift back into French within a few days of testing. It's like the model sees French legal text in context and thinks "oh we're doing French now." Anyone else building multilingual RAG systems running into this? The language contamination from source documents was the most annoying bug I dealt with and I've seen almost nobody write about it.

3h ago

---

**[Project Idea. Dream display project. 3 LLMs spitball the idea and tech specs and programs needed.](https://www.reddit.com/r/artificial/comments/1srfd8h/project_idea_dream_display_project_3_llms/)**

3 AI models discussing this subject.

🔗 [rauno.ai](https://rauno.ai/c/JIUOBRNQLY) • 9h ago

---

---

## Google News: "ai"

**[Job Cuts Driven by A.I. Are Rising on Wall Street](https://www.nytimes.com/2026/04/21/business/ai-job-cuts-wall-street.html)**

The New York Times • 43m ago

---

**[Amazon to invest up to another $25 billion in Anthropic as part of AI infrastructure deal](https://www.cnbc.com/2026/04/20/amazon-invest-up-to-25-billion-in-anthropic-part-of-ai-infrastructure.html)**

Amazon is boosting its investment in Anthropic, which is committing to spending over $100 billion on Amazon cloud services over the next decade.

CNBC • 19h ago

---

**[The AI boom's hidden cost: a bigger trade deficit](https://www.axios.com/2026/04/21/ai-trump-tariffs-mexico)**

Axios • 7m ago

---

**[NFL mock draft 2026: How AI picks compare to expert predictions for Round 1](https://www.usatoday.com/story/sports/nfl/draft/2026/04/21/nfl-mock-draft-2026-ai-expert-predictions/89664476007/)**

Will man or machine better predict the 2026 NFL Draft? USA TODAY Sports put Microsoft Copilot AI to the test against expert picks from Chris Bumbaca.

USA Today • 9m ago

---

**[Avala Gains 15% in April on AI, Erasing Double-Digit March Loss](https://www.bloomberg.com/news/articles/2026-04-21/avala-gains-15-in-april-on-ai-erasing-double-digit-march-loss)**

Bloomberg • 17m ago

---

**[This Scammer Used an AI-Generated MAGA Girl to Grift ‘Super Dumb’ Men](https://www.wired.com/story/ai-generated-maga-girls/)**

A med student says he’s made thousands of dollars selling photos and videos of a young conservative woman he created using generative tools. He’s not alone.

WIRED • 5h ago

---

**[Apple incoming CEO John Ternus faces a defining challenge: Fixing the company's AI strategy](https://www.cnbc.com/2026/04/20/apple-new-ceo-john-ternus-faces-defining-challenge-fixing-ai-strategy.html)**

Tim Cook had a highly successful tenure as Apple's CEO, but he leaves his successor with a big gap to fill when it comes to the company's position in AI.

CNBC • 11h ago

---

**[Apple’s next chief John Ternus faces defining AI moment](https://www.ft.com/content/ef888edd-d12e-41d0-b38d-3d6465cf280c?syn-25a6b1a6=1)**

Tim Cook’s replacement must lead iPhone-maker through industry shift

Financial Times • 7h ago

---

**[Apple’s pick to replace Tim Cook hints at its plans for the AI era](https://www.cnn.com/2026/04/21/tech/apple-new-ceo-ai-john-ternus)**

Apple’s announcement Monday that CEO Tim Cook will step down and John Ternus will take over signals a significant shift for Apple: The company is betting its future on the most rapidly evolving technology in the history of computing.

CNN • 4h ago

---

**[AI job scams are booming – and I was fooled by one. Here is how to avoid them](https://www.theguardian.com/money/2026/apr/21/how-to-avoid-ai-online-job-recruitment-scams)**

Fraudsters are using the promise of fake roles to trick job-seekers out of money, personal information or both, and with the help of AI they are more convincing than ever. But there are ways to spot them

The Guardian • 1h ago

---

---

## HackerNews: "ai"

**[Atlassian enables default data collection to train AI](https://news.ycombinator.com/item?id=47833247)**

⬆️ 586 • 💬 130 • 1d ago • [letsdatascience.com](https://letsdatascience.com/news/atlassian-enables-default-data-collection-to-train-ai-f71343d8)

---

**[College instructor turns to typewriters to curb AI-written work](https://news.ycombinator.com/item?id=47818485)**

⬆️ 488 • 💬 426 • 2d ago • [sentinelcolorado.com](https://sentinelcolorado.com/uncategorized/a-college-instructor-turns-to-typewriters-to-curb-ai-written-work-and-teach-life-lessons/)

---

**[AI Resistance: some recent anti-AI stuff that’s worth discussing](https://news.ycombinator.com/item?id=47839951)**

People are sick of artificial intelligence, and are increasingly making it known through acts of resistance.

⬆️ 371 • 💬 385 • 19h ago • [stephvee.ca](https://stephvee.ca/blog/artificial%20intelligence/ai-resistance-is-growing/)

---

**[Deezer says 44% of songs uploaded to its platform daily are AI-generated](https://news.ycombinator.com/item?id=47835928)**

Deezer says consumption of AI-generated music on the platform is still very low, between 1-3% of the total streams, and that 85% of these streams are detected as fraudulent and are demonetized.

⬆️ 355 • 💬 370 • 1d ago • [TechCrunch](https://techcrunch.com/2026/04/20/deezer-says-44-of-songs-uploaded-to-its-platform-daily-are-ai-generated/)

---

**[Airline worker arrested after sharing photos of bomb damage in WhatsApp group](https://news.ycombinator.com/item?id=47824068)**

Police lured the man to a meeting and arrested him after accessing a private WhatsApp group with colleagues

⬆️ 284 • 💬 189 • 2d ago • [LBC](https://www.lbc.co.uk/article/dubai-police-spied-private-whatsapp-5HjdXwr_2/)

---

**[A Roblox cheat and one AI tool brought down Vercel's platform](https://news.ycombinator.com/item?id=47844431)**

⬆️ 259 • 💬 140 • 11h ago • [webmatrices.com](https://webmatrices.com/post/how-a-roblox-cheat-and-one-ai-tool-brought-down-vercel-s-entire-platform)

---

**[Air is full of DNA](https://news.ycombinator.com/item?id=47819738)**

Airborne genetic material can be used to paint a picture of ecosystem health, watch for invasive species and even identify humans.

⬆️ 155 • 💬 50 • 2d ago • [nature.com](https://www.nature.com/articles/d41586-026-01099-2)

---

**[Graphs that explain the state of AI in 2026](https://news.ycombinator.com/item?id=47817581)**

AI investment is skyrocketing while AI’s impact on jobs and public perception remains mixed

⬆️ 113 • 💬 61 • 2d ago • [IEEE Spectrum](https://spectrum.ieee.org/state-of-ai-index-2026)

---

**[Show HN: Mediator.ai – Using Nash bargaining and LLMs to systematize fairness](https://news.ycombinator.com/item?id=47835411)**

Mediator.ai uses bargaining theory and modern AI to find agreements that two people in conflict would both accept, including ones they hadn't thought of.

⬆️ 109 • 💬 58 • 1d ago • [Mediator.ai](https://mediator.ai/)

---

**[Uber’s Anthropic AI push hits a wall](https://news.ycombinator.com/item?id=47826328)**

Uber Technologies, Inc is learning the hard way that scaling AI isn't just about speed—it's about cost. Despite spending $3.4 billion on research and development, the company has already exhausted its planned AI budget just months into 2026. According to The Information, Chief Technology Officer Praveen Neppalli Naga said Uber is now "back to the drawing board" after a surge in the use of AI coding tools, particularly Anthropic's Claude Code, has blown past internal expectations. Don't Miss: A s

⬆️ 94 • 💬 103 • 1d ago • [Yahoo Finance](https://finance.yahoo.com/sectors/technology/articles/ubers-anthropic-ai-push-hits-223109852.html)

---

---

## YouTube Videos: "ai"

**[New AI Robot From China Breaks Human Limits](https://www.youtube.com/watch?v=EJbJMg2RNgw)**

AGIBOT just rolled out a full new wave of humanoid robots and AI models built for real deployment, while researchers in South ...

📺 AI Revolution

👁️ 15K • 👍 544 • 💬 31 • ⏱️ 16:29 • 15h ago

---

**[AI Is Literally A Psyop](https://www.youtube.com/watch?v=wLC7SATDmy8)**

So much of the hype around AI is due to its supposed "superintelligence". Supposedly, AGI will be able to do almost everything ...

📺 Cole Hastings

👁️ 117K • 👍 6K • 💬 1K • ⏱️ 17:36 • 2d ago

---

**[I Tried To Write &amp; Publish An AI Novel In 3 Hours](https://www.youtube.com/watch?v=f9xryQuhr0Q)**

Try Scribe for free: https://scribe.how/wholesaleted ▻ Get A Free Canva Account: https://wholesaletedgo.com/canvapro (affiliate ...

📺 Wholesale Ted

👁️ 9K • 👍 858 • 💬 140 • ⏱️ 22:07 • 20h ago

---

**[Agent Swarms Is One of The Most Powerful AI System Yet](https://www.youtube.com/watch?v=KdP305UYuNA)**

Abacus AI just showed something that feels a lot bigger than another flashy AI demo. Agent Swarms inside ChatLLM and Deep ...

📺 AI Revolution

👁️ 14K • 👍 521 • 💬 41 • ⏱️ 13:18 • 1d ago

---

**[Pro-Trump, Pro-War AI Bot Network EXPOSED as MAGA Collapses](https://www.youtube.com/watch?v=xAUAXLpI_XI)**

Krystal and Ryan discuss pro-Trump AI bots flooding social media. Sign up for a PREMIUM Breaking Points subscriptions for full ...

📺 Breaking Points

👁️ 138K • 👍 5K • 💬 746 • ⏱️ 8:50 • 21h ago

---

**[How to Create a Realistic Talking AI Avatar in 15 Seconds (HeyGen Avatar V)](https://www.youtube.com/watch?v=ym9HhUlFiog)**

sponsored HeyGen Here: https://bit.ly/42cySEn Become an AI Master – All-in-one AI Learning https://aimaster.me/yt/avatar ...

📺 AI Master

👁️ 2K • 👍 89 • 💬 9 • ⏱️ 10:51 • 20h ago

---

**[THIS ABOUT AI IS TERRIFYING 👀](https://www.youtube.com/watch?v=6egP0Y_QF8Y)**

THIS ABOUT AI IS TERRIFYING We're way further into this than people realize… #Shorts #AI #ArtificialIntelligence #Tech ...

📺 Jesse ON FIRE

👁️ 7K • 👍 677 • 💬 63 • ⏱️ 2:27 • 14h ago

---

**[YouTube&#39;s Secret AI Tool That Helps You Earn Money From YouTube | YouTube Ask Studio](https://www.youtube.com/watch?v=GtU7b46wdrg)**

YouTube's Secret FREE AI Tool That Helps You Earn money from YouTube channel more professionally. This video shows you ...

📺 Mr How

👁️ 39K • 👍 3K • 💬 403 • ⏱️ 8:07 • 2d ago

---

**[OpenAI GPT-5.5 Leaked: Super Powerful AI Model! Beats Opus 4.7, Gemini 3.1! Cheap &amp; Fast! (Tested)](https://www.youtube.com/watch?v=UfUBW9QcTjU)**

in this video, we break down the rumored GPT-5.5 “pro” model from OpenAI and why it's getting so much attention online.

📺 WorldofAI

👁️ 39K • 👍 690 • 💬 106 • ⏱️ 10:27 • 1d ago

---

**[Why Elon Says Google Will Win the AI Race](https://www.youtube.com/watch?v=ZmjdeSRvyyM)**

The Real AI Race: Tesla vs Google vs China Some viewers ask where they can learn more about investing in AI, Space and ...

📺 Brighter with Herbert

👁️ 42K • 👍 2K • 💬 126 • ⏱️ 20:00 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)**

*Qwen*

Qwen3.6-35B-A3B is a 35B parameter causal language model with a vision encoder, optimized for agentic coding tasks and featuring enhanced thinking preservation for iterative development. It supports a context length of 262,144 tokens, extensible up to 1,010,000.

`image-text-to-text` `36.0B`

⬇️ 458,436 • ❤️ 1,101 • 6d ago

---

**[Kimi-K2.6](https://huggingface.co/moonshotai/Kimi-K2.6)**

*Moonshot AI*

Kimi K2.6 is a 1T parameter multimodal agentic model excelling in long-horizon coding and coding-driven design, capable of generating production-ready interfaces and workflows from prompts and visual inputs. It features an advanced agent swarm for complex task orchestration and proactive autonomous execution.

`image-text-to-text` `1058.6B`

⬇️ 8,241 • ❤️ 617 • 14h ago

---

**[Qwen3.6-35B-A3B-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF)**

*Unsloth AI*

Qwen3.6-35B-A3B is a 35B parameter causal language model with vision capabilities, optimized for agentic coding and reasoning tasks. It features a large context window (262k native, extensible to 1M+ tokens) and improved tool-calling, making it suitable for complex development workflows and iterative coding.

`image-text-to-text` `34.7B`

⬇️ 967,317 • ❤️ 593 • 1d ago

---

**[HY-Embodied-0.5](https://huggingface.co/tencent/HY-Embodied-0.5)**

*Tencent*

HY-Embodied-0.5 is a multilingual vision-language model designed for embodied agents, excelling in spatial-temporal perception and reasoning. It features an efficient Mixture-of-Transformers (MoT) architecture for real-world robot control and VLA pipelines.

`image-text-to-text` `3.8B`

⬇️ 2,035 • ❤️ 893 • 7d ago

---

**[ERNIE-Image](https://huggingface.co/baidu/ERNIE-Image)**

*BAIDU*

ERNIE-Image is a 8B parameter text-to-image diffusion model excelling in complex instruction following, text rendering, and structured generation for use cases like posters and comics. It offers strong visual quality and controllability, running on consumer GPUs.

`text-to-image`

⬇️ 4,523 • ❤️ 508 • 4d ago

---

**[HY-World-2.0](https://huggingface.co/tencent/HY-World-2.0)**

*Tencent*

HY-World 2.0 is a multi-modal framework for generating and reconstructing 3D worlds from text, images, or video. It produces editable 3D assets like meshes and Gaussian Splattings, enabling applications in game development and simulation.

`image-to-3d`

⬇️ 0 • ❤️ 510 • 5d ago

---

**[gemma-4-E4B-it-OBLITERATED](https://huggingface.co/OBLITERATUS/gemma-4-E4B-it-OBLITERATED)**

*OBLITERATUS*

Gemma 4 E4B OBLITERATED v3 is a text-generation model with 0% refusal and improved coding capabilities, designed for uncensored and unrestricted AI interactions. It features a modified architecture with 720 intact tensors, making it highly compatible with tools like Ollama and llama.cpp, and optimized for performance on consumer hardware.

`text-generation` `8.0B`

⬇️ 63,995 • ❤️ 417 • 1d ago

---

**[ERNIE-Image-Turbo](https://huggingface.co/baidu/ERNIE-Image-Turbo)**

*BAIDU*

ERNIE-Image-Turbo is a distilled text-to-image diffusion model optimized for speed (8 inference steps) and fidelity. It excels at complex instruction following, text rendering, and structured generation for use cases like posters, comics, and multi-panel layouts.

`text-to-image`

⬇️ 5,952 • ❤️ 340 • 4d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal model based on Qwen3.6-35B-A3B, capable of processing text and images. It features a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context, optimized for lossless generation without refusals, suitable for diverse creative and technical applications.

`image-text-to-text` `34.7B`

⬇️ 261,086 • ❤️ 320 • 4d ago

---

**[MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)**

*MiniMax*

MiniMax-M2.7 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 358,255 • ❤️ 1,016 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 9 • 💬 2 • ⭐ 3,584 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 24 • 💬 1 • ⭐ 19,957 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 48 • 💬 2 • ⭐ 52,006 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://huggingface.co/papers/2604.14268)**

*Team HY-World, Chenjie Cao, Xuhui Zuo et al. (45 authors)*

HY-World 2.0 is a multi-modal world model framework that generates high-fidelity 3D Gaussian Splatting scenes from diverse inputs using specialized modules for panorama generation, trajectory planning, world expansion, and composition, along with an enhanced rendering platform for interactive 3D exploration.

▲ 103 • 💬 5 • ⭐ 1,475 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14268) • [💻 code](https://github.com/Tencent-Hunyuan/HY-World-2.0) • [🔗 project](https://3d-models.hunyuan.tencent.com/world/)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 165 • 💬 10 • ⭐ 40,542 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[MultiWorld: Scalable Multi-Agent Multi-View Video World Models](https://huggingface.co/papers/2604.18564)**

*Haoyu Wu, Jiwen Yu, Yingtian Zou et al. (4 authors)*

🏢 The University of Hong Kong

MultiWorld is a unified framework for multi-agent multi-view world modeling that achieves accurate multi-agent control while maintaining multi-view consistency through specialized modules for condition handling and global state encoding.

▲ 35 • 💬 2 • ⭐ 62 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2604.18564) • [💻 code](https://github.com/CIntellifusion/MultiWorld) • [🔗 project](https://multi-world.github.io/)

---

**[RAG-Anything: All-in-One RAG Framework](https://huggingface.co/papers/2510.12323)**

*Zirui Guo, Xubin Ren, Lingrui Xu et al. (5 authors)*

🏢 Data Intelligence Lab@HKU

RAG-Anything is a unified framework that enhances multimodal knowledge retrieval by integrating cross-modal relationships and semantic matching, outperforming existing methods on complex benchmarks.

▲ 73 • 💬 6 • ⭐ 16,458 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.12323) • [💻 code](https://github.com/HKUDS/RAG-Anything)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 53 • 💬 1 • ⭐ 77,488 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 160 • 💬 2 • ⭐ 60,687 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 28 • 💬 1 • ⭐ 18,273 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 48.7k • 🔱 6.4k • 11h ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 41.7k • 🔱 2.1k • 3d ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 37.6k • 🔱 7.6k • 2d ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 31.8k • 🔱 3.5k • 5h ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 20+ AI Agent Skills.

`Go`

⭐ 8.4k • 🔱 545 • 2h ago

---

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 5.8k • 🔱 1.3k • 1d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 5.7k • 🔱 967 • 2d ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.6k • 🔱 1.6k • 9d ago

---

**[elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3)**

LIBERATED AI CHAT

`TypeScript`

⭐ 5.1k • 🔱 1.2k • 26d ago

---

**[Arthur-Ficial/apfel](https://github.com/Arthur-Ficial/apfel)**

The free AI already on your Mac. CLI tool, OpenAI-compatible server, and interactive chat — all on-device via Apple Intelligence. No API keys, no cloud, no downloads.

`Swift` `apple-intelligence` `apple-silicon` `cli` `foundationmodels` `homebrew`

⭐ 4.8k • 🔱 185 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
