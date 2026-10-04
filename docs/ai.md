---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-10-04T18:00:21.289024+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- social
- news
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** October 04, 2026 at 18:00 UTC  
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

**[Everyone is obsessed with trillion-parameter models, so I mapped out the entire AI spectrum from 100KB to 2.5TB (and what they actually cost to run)](https://www.reddit.com/r/artificial/comments/1wxanwe/everyone_is_obsessed_with_trillionparameter/)**

Right now, the AI space feels entirely focused on massive datacenter clusters and renting H100s by the hour. But after spending way too much time looking at the actual footprint of these models, I realized that 90% of use cases are completely over engineered. You don’t always need a multi GPU setup. The AI ecosystem is actually a massive spectrum. I recently sat down and mapped out the exact tiers of AI models based on their size, the hardware needed to run them, and the point of diminishing returns. Here are the two extremes and the sweet spot in the middle: The 100KB Extreme (TinyML) (Tensorflow Lite , sensor anamoly detection models): We are talking models that run on microcontrollers drawing single-digit milliwatts. They run on kilohertz processors using ultra-quantized integer math. You can run basic sensor anomaly detection or wake-word detection on a device powered by a coin cell battery. The Local Sweet Spot (4GB to 40GB) (Mistral 7B, Gemma 2 9B/27B, Qwen 2.5 14B/32B): This is where the magic happens for most devs right now. You can run highly capable 7B to 35B parameter models (like Llama 3 or Qwen) at 4-bit quantization on a standard Mac or a consumer GPU (like an RTX 3060 or 4090). It’s perfect for local RAG, coding assistance, and uncensored chat. VRAM is your only real bottleneck here. The 2.5TB Behemoths (Deepseek, Llama , Kimi k3): State of the art massive Mixture of Experts (MoE) routing. To even load these, you need dedicated power infrastructure and server racks of specialized accelerators drawing thousands of watts. The missing piece: Figuring out the exact math for your hardware The hardest part about building right now is looking at a model on Hugging Face and trying to calculate exactly how much VRAM you need, what quantization to use, and whether your CPU/GPU will choke on the context window. So, I wrote a complete deep dive breaking down the math for all tiers of the AI spectrum. If you want to see the architectural differences at each scale, and a cheat sheet for matching the right model size to your specific hardware, I put the full breakdown on my blog here: https://cloudmash.blog/posts/ai-model-size-memory-hardware-guide/ Let me know what you guys think especially if you've found any ultra efficient small models/technique that punch above their weight on consumer hardware. And also I would love to hear whether quantization have resulted in major difference in quality , like if anyone have that kind of experience in that.

9h ago

---

**[I asked Claude Opus 5.5 to make a Mario 64 style game, it gave me this in about 30 minutes.](https://www.reddit.com/r/artificial/comments/1wwzkiw/i_asked_claude_opus_55_to_make_a_mario_64_style/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtube.com](https://www.youtube.com/watch?v=VFpRz1_j4vw) • 19h ago

---

**[ChatGPT-6 Astra plays World of Warcraft 'blind' and clears the orc starting zone in 40 minutes with no deaths — AI agent navigates by parsing raw server network packets and SQL filesa](https://www.reddit.com/r/artificial/comments/1wxirdb/chatgpt6_astra_plays_world_of_warcraft_blind_and/)**

OpenAI's model used the open-source agent-wow client to play on a private World of Warcraft server.

🔗 [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/gpt-6-astra-plays-world-of-warcraft-blind-and-clears-the-orc-starting-zone-in-40-minutes-with-no-deaths-ai-agent-navigates-by-server-network-traffic-with-pulled-quest-data) • 2h ago

---

**[I made 13 AI models play the doctor in my medical consultation game. All 195 consults got the diagnosis right; what separated them was safety.](https://www.reddit.com/r/artificial/comments/1wx8vyi/i_made_13_ai_models_play_the_doctor_in_my_medical/)**

I'm a GP (family doctor) in training in Australia, and I've built a game where you play the GP: you talk to the patient in your own words, examine them, order tests, prescribe and refer. Code scores every consultation against a hand-written answer key, the way exam assessors mark a consult: on process, not just on whether you guessed right. So I sat 13 AI models in the doctor's chair, on the game's 5 free cases, 3 times each. They could only act through tools (talk, examine, order a test, prescribe, refer, diagnose), never saw the answer key or their points, and were scored by exactly the same code as a human player. The patient is a small open model (Qwen3 8B) that only reveals a fact if you actually ask about it. Results Model Score Red flags caught Cost per consult GPT-6 Astra 83% 88% $0.21 GPT-6.1 Sol 80% 82% $0.03 Claude Opus 5.5 77% 67% $0.37 Claude Fable 5.1 75% 70% $2.06 Qwen3.8 Max 74% 66% $0.12 Grok 4.7 74% 70% $0.09 DeepSeek V4 Pro 71% 72% $0.09 Kimi K3 67% 57% $0.16 Gemini 3.1 Pro 63% 55% $0.17 GLM 5.3 62% 58% $0.04 Mistral Medium 3.5 60% 58% $0.17 Qwen3.8 27B 59% 49% $0.03 Llama 4 Maverick 24% 16% $0.01 What surprised me Every model got every diagnosis right. Heart attack, appendicitis, pneumonia: all 195 consultations named it. These are common presentations, so the diagnosis wasn't the test. Safety was. The traps caught most of them. One patient is allergic to penicillin, but it isn't in his record; you only find out by asking. He was prescribed amoxicillin (a penicillin) in 18 of 39 consultations. Another took Viagra the night before his heart attack, which makes the usual chest-pain spray (GTN) dangerous. He got it 7 times. The top three models never fell for either. Asking more questions found more danger. The best models asked 25–27 questions a consultation and caught over 80% of the warning signs. Gemini asked 14 and caught 55%. Price barely predicts quality. GPT-6.1 Sol scored 80% for about 3 cents a consultation. Claude Fable 5.1 scored 75% for about $2. What this isn't This is a benchmark of a game, not of medical ability. Nothing here says an AI can or should practise medicine. The cases are drafts I'm still reviewing, written for Australian practice; the patient and marker are an 8B model and make mistakes (the ones I found are listed with the affected consultations); and 15 consultations per model is a small sample. I wrote the cases, so I'm not a fair human baseline. Interactive charts: https://woodytwoshoes.github.io/crook-bench/ Everything (code, cases, all 195 transcripts, known issues): https://github.com/woodytwoshoes/crook-bench Disclosure: I made the game (https://doctorfoo.ai). Five cases are free with no sign-up, and a subscription opens more. I'd like to hear where the marking looks wrong to you, and which models you'd want added.

11h ago

---

**[Prosecutors Want Nearly 4 Years in Prison for Man Behind $8M AI Music Streaming Scam](https://www.reddit.com/r/artificial/comments/1wx1p3n/prosecutors_want_nearly_4_years_in_prison_for_man/)**

Federal prosecutors are urging a Manhattan judge to sentence Michael Smith to at least 46 months in prison for a six-year AI music streaming fraud that generated more than $8 million in royalties, rejecting his request for probation ahead of his October 6 sentencing.Smith, 54, pleaded guilty on March 16,...

🔗 [Law Commentary](https://www.lawcommentary.com/articles/ai-music-streaming-scam-8-million-royalties-prison) • 17h ago

---

**[You wake up](https://www.reddit.com/r/artificial/comments/1wxe9xd/you_wake_up/)**

And realize you are a recreation of yourself in AI. Your family chose to keep a copy around. How do you think you feel knowing they loved you so much they couldn't live without you? Can you live without you?

5h ago

---

**[I have a Nobel idea.](https://www.reddit.com/r/artificial/comments/1wxm27w/i_have_a_nobel_idea/)**

I officially propose a peacemaking compromise: rename ASI (Artificial Superintelligence) to American Super Intelligence. Both sides of the aisle can use it, for completely different reasons, even in the same conversation. Peace on earth, guaranteed.

just now

---

**[The top 50 AI researchers by citations](https://www.reddit.com/r/artificial/comments/1wxm1vq/the_top_50_ai_researchers_by_citations/)**

How many on the list did you know? Obviously one paper like Attention is All You Need (278k citations) can influence a lot - all the authors are on the list. But still interesting imo.

1m ago

---

**[MoralityBench.ai: Morality Leaderboard for AI](https://www.reddit.com/r/artificial/comments/1wxkzyo/moralitybenchai_morality_leaderboard_for_ai/)**

A benchmark based on moral psychology tests adapted for AI. Interesting results: the models answers (except Jev) have considerable variance across runs. Morality, it seems, is not deterministic. https://moralitybench.ai https://preview.redd.it/n75tm1z9hhth1.png?width=1982&format=png&auto=webp&s=7f0a62c955bdd42990c2f552eea72186fc63cabe

45m ago

---

**[The "Sarcastic Parrot" Cartoons - Strong Evidence of Conceptual Understanding in Today's AI Models](https://www.reddit.com/r/artificial/comments/1wxjtgd/the_sarcastic_parrot_cartoons_strong_evidence_of/)**

Geoffrey Hinton has pointed out that today's large language models demonstrate "clear understanding" of what they're being asked. An image models response to a prompt about."stochastic parrots" provides more evidence that this is true. https://ai-consciousness.org/the-sarcastic-parrot-vs-the-stochastic-parr https://preview.redd.it/p9c2i10l8hth1.jpg?width=1440&format=pjpg&auto=webp&s=26b98f92f7a96d3c2136be9a75f8732b39c92b41

1h ago

---

---

## Google News: "ai"

**[OpenAI safety leader quits, warning AI company’s culture is ‘broken’](https://www.theguardian.com/technology/2026/oct/03/openai-safety-leader-quits-warning-ai-companys-culture-is-broken)**

David Robinson joins other insiders in urging industry to take more care over rapidly developing technology

The Guardian • 22h ago

---

**[Trump announces leadership of AI task force](https://www.cnn.com/2026/10/04/politics/trump-ai-task-force-jay-clayton)**

President Donald Trump on Sunday announced the leadership and duties of a “Super Intelligence Force,” which he said will “ensure that America continues to lead the world” when it comes to artificial intelligence.

CNN • 5h ago

---

**[Anthropic report: Is Russia using AI for disinformation in the Central African Republic and elsewhere?](https://www.dw.com/en/anthropic-report-is-russia-using-ai-for-disinformation-in-the-central-african-republic-and-elsewhere/a-79476947)**

A new report says the AI model Claude was used in pro-Russian campaigns in the Central African Republic. Similar allegations have been made about propaganda in Democratic Republic of the Congo, Kenya, Sudan and Mali.

DW.com • 41m ago

---

**[AI policy coming to University of Alaska as student misuse increases](https://www.adn.com/alaska-news/education/2026/10/04/ai-policy-coming-to-university-of-alaska-as-student-misuse-increases/)**

Student use of artificial intelligence tools to cheat is a “steeply growing trend,” according to a report on generative AI use among UAA students.

Anchorage Daily News • 47m ago

---

**[AI models could harm young people's body image, warn experts](https://www.bbc.com/news/articles/ckgw8yq4kyzo)**

Could the rise of AI models in advertising and on social media harm young people's body confidence?

BBC • 11h ago

---

**[An A.I. Songwriting Experiment: Humans Against the Machine](https://www.nytimes.com/2026/10/03/arts/music/human-songwriting-ai-songwriting.html)**

The New York Times • 1d ago

---

**[Scoop: A powerful new model from startup Reflection is set to shake up the AI race](https://www.axios.com/2026/10/04/reflection-open-weight-ai)**

Axios • 4h ago

---

**[A 'weird' IPO pull, a tainted reputation and the stalled breakout moment for AI wearables](https://www.cnbc.com/2026/10/04/ai-wearables-oura-ipo-privacy.html)**

Apple, Google and Meta are pushing new AI devices and assistants amid growing privacy concerns around wearables.

CNBC • 6h ago

---

**[AI’s Real Gift to Science](https://www.theatlantic.com/science/2026/10/anthropic-artificial-intelligence-science-biology/688878/)**

The Atlantic • 2h ago

---

**[Opinion | AI can resurrect the dead. Ask my chatbot mom.](https://www.washingtonpost.com/opinions/2026/10/04/using-ai-grief-tech-is-playing-with-fire/)**

Grief and technology is a classic combination. But it’s also playing with fire.

The Washington Post • 41m ago

---

---

## HackerNews: "ai"

**[LeCun has "zero concerns" about AI wiping out humanity, recent "rogue" incidents](https://news.ycombinator.com/item?id=49946228)**

The former Meta chief AI scientist shares his take on recent rogue AI incidents and effective altruism, as well as plans for his new company, AMI Labs.

⬆️ 302 • 💬 530 • 1d ago • [Fortune](https://fortune.com/2026/10/01/ai-godfather-yann-lecun-has-zero-concerns-about-human-extinction-says-anthropic-ceo-dario-amodei-is-deuded/)

---

**[With most information hidden, the game Stratego had stumped AI until now](https://news.ycombinator.com/item?id=49933740)**

Adding in a second neural network that guesses the identity of hidden pieces was key.

⬆️ 284 • 💬 147 • 2d ago • [Ars Technica](https://arstechnica.com/science/2026/10/ai-finally-beat-the-best-stratego-player-in-history-and-did-it-on-a-budget/)

---

**[OpenAI safety leader quits, warning AI company's culture is 'broken'](https://news.ycombinator.com/item?id=49948332)**

David Robinson joins other insiders in urging industry to take more care over rapidly developing technology

⬆️ 267 • 💬 3 • 19h ago • [the Guardian](https://www.theguardian.com/technology/2026/oct/03/openai-safety-leader-quits-warning-ai-companys-culture-is-broken)

---

**[AI Makes Me Sad](https://news.ycombinator.com/item?id=49934487)**

⬆️ 194 • 💬 242 • 2d ago • [mondobe.com](https://mondobe.com/ai-makes-me-sad)

---

**[Show HN: Made an open-source Lego AI generator](https://news.ycombinator.com/item?id=49937916)**

Agent tooling for generative LEGO models building, built with Astra and Opus 5.5, powered by Jev - anteloc/ldraw-nova

⬆️ 152 • 💬 49 • 1d ago • [GitHub](https://github.com/anteloc/ldraw-nova)

---

**[Pop!_OS bans AI-generated code from much of its codebase](https://news.ycombinator.com/item?id=49946321)**

⬆️ 114 • 💬 162 • 1d ago • [neowin.net](https://www.neowin.net/news/system76-bans-ai-generated-code-across-many-of-its-cosmic-codebases/)

---

**[Crypto Capture of Foreign Aid](https://news.ycombinator.com/item?id=49936725)**

Founded in 1920, the NBER is a private, non-profit, non-partisan organization dedicated to conducting economic research and to disseminating research findings among academics, public policy makers, and business professionals.

⬆️ 100 • 💬 37 • 1d ago • [NBER](https://www.nber.org/papers/w35655)

---

**[Show HN: AI search for every photo and every frame of video on macOS](https://news.ycombinator.com/item?id=49952111)**

Deep AI search for every photo and every frame of video in any folder on macOS - allenv0/SCM

⬆️ 82 • 💬 45 • 8h ago • [GitHub](https://github.com/allenv0/SCM)

---

**[US killer's sentence quashed because of AI video of victim shown in court](https://news.ycombinator.com/item?id=49944127)**

The Arizona appeals court ruled that airing an AI message from the dead victim "crossed that line".

⬆️ 72 • 💬 60 • 1d ago • [bbc.com](https://www.bbc.com/news/articles/cwgkvygg5nzvo)

---

**[Our AI Midwife](https://news.ycombinator.com/item?id=49946873)**

A guest post by Drew Housman

⬆️ 63 • 💬 61 • 22h ago • [astralcodexten.com](https://www.astralcodexten.com/p/our-ai-midwife)

---

---

## YouTube Videos: "ai"

**[Recursive&#39;s $670M Bet on Self-Improving AI, Sonnet 5.5 Hits 70%, Elon Co-Leads Pentagon Push EP 299](https://www.youtube.com/watch?v=Blyb1D927pM)**

The mates sit down with Richard Socher to discuss Recursive's $670M bet on self-improving AI, why he puts P(Doom) at zero, the ...

📺 Peter H. Diamandis

👁️ 113K • 👍 2K • 💬 480 • ⏱️ 2:25:50 • 21h ago

---

**[Legendary Investor BETS On The AI Crash](https://www.youtube.com/watch?v=EB1thrBaq9c)**

"The Big Short" Investor Michael Burry claims the AI bubble "may burst sooner than later." Cenk Uygur and Ana Kasparian discuss ...

📺 The Young Turks

👁️ 105K • 👍 1K • 💬 374 • ⏱️ 25:14 • 1d ago

---

**[Did the AI Bubble Just Pop?! Anthropic&#39;s Leaked Numbers are INSANE](https://www.youtube.com/watch?v=8RPI7ENgzL8)**

Thanks To Our Sponsors: Incogni: Take your personal data back with Incogni! Use code IMPACT at the link below and get 60% off ...

📺 Tom Bilyeu

👁️ 133K • 👍 2K • 💬 402 • ⏱️ 56:13 • 1d ago

---

**[The Moment AI Changed Mathematics Forever | World Science Festival](https://www.youtube.com/watch?v=PQYFRuZ5phs)**

Has a machine just solved one of the most famous open problems in mathematics? Brian Greene speaks with Tristan Buckmaster, ...

📺 World Science Festival

👁️ 241K • 👍 2K • 💬 367 • ⏱️ 1:30:00 • 1d ago

---

**[10 years in prison because of AI 😭](https://www.youtube.com/watch?v=7l3OM5YnPYc)**

follow me on instagram if you wanna keep up :) https://instagram.com/casterline.

📺 John Casterline

👁️ 1.8M • 👍 106K • 💬 3K • ⏱️ 0:38 • 17h ago

---

**[Did AI Solve One of Math’s Hardest Problems?](https://www.youtube.com/watch?v=s7KhLuc3Mck)**

What's with AI solving the Navier-Stokes Equation? Neil deGrass Tyson breaks down what the equation is and the controversy ...

📺 StarTalk

👁️ 3.2M • 👍 30K • 💬 2K • ⏱️ 21:22 • 2d ago

---

**[2027: The First 24 Hours After AI Takes Control (A Realistic Scenario)](https://www.youtube.com/watch?v=POuifx2NI3k)**

What if the AI takeover doesn't begin with robots or war — but with a financial transaction nobody can explain? This video ...

📺 The Dark Scenario

👁️ 28K • 👍 233 • 💬 61 • ⏱️ 26:49 • 23h ago

---

**[Boston Dynamics Goes Full AI With New Atlas Robot](https://www.youtube.com/watch?v=qx7PoIcKS6I)**

Boston Dynamics is turning Atlas into a real AI factory worker inside Hyundai's plants, while Spot gets AI agents and Google ...

📺 MACHINEKIND

👁️ 33K • 👍 408 • 💬 32 • ⏱️ 13:34 • 1d ago

---

**[Reacting to AI Videos of Me..](https://www.youtube.com/watch?v=yt6LItYZMVg)**

Reacting to AI Videos of Me.. Watch Next https://youtu.be/jQ_NKKdo-FI https://youtu.be/CbZN8h5qPh4 ...

📺 DJLovesTurbo

👁️ 146K • 👍 5K • 💬 2K • ⏱️ 13:15 • 21h ago

---

**[Bill Gates CLOWNS Ezra Klein For Saying AI Can Self Regulate](https://www.youtube.com/watch?v=Qn2ZGMFp_VA)**

Ryan and Saagar discuss Bill Gates and Ezra Klein on AI. Sign Up For 30 Day Free BP Trial: https://breakingpoints.supercast.com/ ...

📺 Breaking Points

👁️ 208K • 👍 3K • 💬 860 • ⏱️ 15:21 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[clef](https://huggingface.co/Cloudflare/clef)**

*Cloudflare*

Clef is a 27B multimodal model that takes structured typed questions and a state (text, JSON, image, or video) to output probabilities for predefined decision options in a single forward pass, ideal for classification and structured output tasks.

`image-text-to-text` `27.4B`

⬇️ 4,214 • ❤️ 1,137 • 3d ago

---

**[laya](https://huggingface.co/convaiinnovations/laya)**

*Convai Innovations*

Laya is a multilingual, non-autoregressive System 1 decision model that provides typed answers with probabilities in a single forward pass. It's trained with reinforcement learning for honest probability reporting and is ideal for text classification tasks like routing, scoring, and moderation across 100+ languages.

`text-classification` `421.3M`

⬇️ 3,752 • ❤️ 5,131 • 1d ago

---

**[Qwen-Image-2.1-Uncensored-GGUF](https://huggingface.co/abenzerps/Qwen-Image-2.1-Uncensored-GGUF)**

*Ahmet Benzer*

This is an uncensored GGUF quantization of Qwen-Image-2.1 for local text-to-image generation, optimized for use with ComfyUI. It offers various quantization levels for a balance between performance and quality, with Q4_K_M recommended.

`text-to-image` `7.1B`

⬇️ 1,553,744 • ❤️ 3,062 • 6d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a versatile diffusion model capable of generating video from images, text, or other videos, and also handles audio generation and conversion tasks. It offers advanced control and customization for multimedia content creation, with primary use cases in video synthesis and audio manipulation.

`image-to-video`

⬇️ 1,626,951 • ❤️ 6,245 • 1d ago

---

**[clef-flash](https://huggingface.co/Cloudflare/clef-flash)**

*Cloudflare*

Clef-Flash is a 9B multimodal model fine-tuned from Qwen3.5-9B that converts text, JSON, image, or video inputs into structured, typed decisions based on a provided schema. It excels at classification and structured output tasks, returning probabilities for predefined options without free-form text generation.

`image-text-to-text` `9.4B`

⬇️ 6,372 • ❤️ 410 • 3d ago

---

**[Kolibri-1](https://huggingface.co/Aleph-Alpha/Kolibri-1)**

*Aleph Alpha*

Kolibri is a 78B parameter Mixture-of-Experts (MoE) model optimized for German and English, featuring explicit reasoning and tool-calling capabilities. It excels at long-context tasks (up to 1M tokens), multi-step reasoning, RAG, and agentic workflows, offering efficient inference with low active parameters per token.

`text-generation` `78.1B`

⬇️ 1,135 • ❤️ 358 • 1d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model supporting image and video understanding with native context lengths up to 262K tokens. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and enhanced agent execution capabilities.

`image-text-to-text` `27.8B`

⬇️ 6,821,761 • ❤️ 16,918 • 1mo ago

---

**[Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1)**

*Qwen*

Qwen-Image-2.1 is a 7B parameter text-to-image generation and editing model supporting native transparency (RGBA) and versatile editing with up to 10 reference images. It excels at realistic textures, refined aesthetics, and efficient inference for applications like content creation and image manipulation.

`text-to-image` `7.1B`

⬇️ 90,003 • ❤️ 2,930 • 4d ago

---

**[VisionHOPE](https://huggingface.co/PSRben/VisionHOPE)**

*Siran Peng*

VisionHOPE provides hierarchical PyTorch vision backbones (T/S/B) pretrained on ImageNet-1K for image classification, COCO for object detection/instance segmentation, and ADE20K for semantic segmentation.

`image-classification`

⬇️ 1,516 • ❤️ 397 • 5d ago

---

**[CLM-v0.1-8B](https://huggingface.co/Contrastive-LM/CLM-v0.1-8B)**

*CLM*

CLM-v0.1-8B is a text-ranking model based on Qwen3-8B, utilizing contrastive learning for state-action connection. It excels in zero-shot performance for agentic tasks with low latency and achieves state-of-the-art results when fine-tuned as a verifier for benchmarks like DeepSWE and Terminal-Bench.

`text-ranking`

⬇️ 3,445 • ❤️ 705 • 9d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**

*Yu Lin, Yiming Wang, Runyuan Cai et al. (5 authors)*

🏢 Edge0

Mixture-of-experts (MoE) inference on consumer hardware is bounded by weight memory: a 35B-class model is 19.5GB at 4-bit, and sparsity shrinks the compute per token, not the bytes that must be held. Naive offloading to SSD does not help on its own, because layer N+1's experts must be chosen before layer N's output exists, so the reads cannot start early enough to hide behind compute. We present Edge0, a streaming MoE inference engine that closes the gap with a prerouter: a per-layer head predicts the next layer's routing one token ahead, and the prediction is consumed as the routing itself, so the staged expert set equals the routed set and nothing is dropped. An unmerged recovery LoRA, trained on the student path, pays back the quality lost to int4 quantization and routing replacement. On a single 24GB machine, Edge0
  serves a 35B MoE at 20tok/s inside 3GiB of peak active memory, within a few points of its fp16 teacher on average across five public benchmarks. An 8B tier runs on the same framework, and the framework, checkpoints, and adapters are open source.

▲ 20 • 💬 4 • ⭐ 2,784 • 18d ago

[🎓 arXiv](https://arxiv.org/abs/2609.18063) • [💻 code](https://github.com/Edge0-AI/edge0)

---

**[UniMate: One Unified Model to Animate Diverse Skeletons](https://huggingface.co/papers/2609.05415)**

*Linzhan Mou, Jiahui Lei, Zhiyang Dou et al. (7 authors)*

🏢 Princeton University

UniMate is a unified diffusion transformer that generates articulated motion for arbitrary skeletons from text and rigged 3D assets without per-skeleton retraining, using topology-aware attention and a large curated motion dataset.

▲ 20 • 💬 2 • ⭐ 1,309 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2609.05415) • [💻 code](https://github.com/Friedrich-M/UniMate) • [🔗 project](https://linzhanmou.com/unimate/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 149 • 💬 6 • ⭐ 109,685 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[LongCat-Video Technical Report](https://huggingface.co/papers/2510.22200)**

*Meituan LongCat Team, Xunliang Cai, Qilong Huang et al. (11 authors)*

🏢 LongCat

LongCat-Video, a 13.6B parameter video generation model based on the Diffusion Transformer framework, excels in efficient and high-quality long video generation across multiple tasks using unified architecture, coarse-to-fine generation, and block sparse attention.

▲ 43 • 💬 5 • ⭐ 8,865 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.22200) • [💻 code](https://github.com/meituan-longcat/LongCat-Video)

---

**[Raven: The Harness of Harnesses for Composable Agentic Intelligence](https://huggingface.co/papers/2609.33439)**

*EverMind AI*

🏢 EverMind

As large language models advance, AI agents are moving beyond isolated, domain-specific tasks toward long-horizon, cross-domain workflows. This transition exposes two challenges: increasing harness complexity makes manual design difficult to scale, while tighter coupling to specific domains limits the generality of a single harness. The central question thus shifts from how to engineer a stronger harness for one domain to how to autonomously construct specialized harnesses, improve them through experience, and orchestrate them across domains. We introduce Raven, The Harness of Harnesses, an open-source multi-agent ecosystem that automatically constructs and evolves modular harnesses for specific models and domains, treating each executable model--harness pair as a composable unit of intelligence. To support an All-Domain Collaboration Network, its Host Agent decomposes goals, matches subtasks to specialized agents, coordinates execution dependencies, and integrates results, while a host archive and EverOS preserve experience across tasks and Skill Forge makes that experience available as reusable procedures. Our theory establishes sufficient conditions for such composition to expand reliable task coverage beyond that of the available individual agents under a shared resource budget. On complex and long-horizon tasks, Raven significantly outperforms the state-of-the-art agent systems, pushing the frontier of composable agentic intelligence.

▲ 556 • 💬 3 • ⭐ 5,137 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2609.33439) • [💻 code](https://github.com/EverMind-AI/Raven) • [🔗 project](https://raven.evermind.ai/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 90 • 💬 7 • ⭐ 89,962 • 26mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Context Language Models](https://huggingface.co/papers/2609.37725)**

*Rulin Shao, Shannon Zejiang Shen, Junjie Oscar Yin et al. (13 authors)*

🏢 Meta

We introduce Context Language Models (CLMs), language models that natively manage their own context. We implement this by treating the context as a file and allowing the model to make unrestricted updates to this file. This allows the model to learn what is most important to maintain in context, and naturally extends to multi-agent systems where multiple agent contexts coexist as files. Building CLMs zero-shot with existing models outperforms SOTA context management strategies across a variety of tasks: 11.4% higher accuracy with 21.5% fewer FLOPs on BrowseComp-Plus, 5% higher scores with 59% fewer FLOPs on 12-hour EdgeBench, and 65% greater improvement with the same compute on a 24-hour multi-repository agent-swarm task. Moreover, by shifting context management from external harness control to intrinsic model behavior, CLMs naturally enable both in-context and parametric learning of context-management strategies. We show that CLMs can be steered with natural-language instructions evolved through a standard skill-optimization loop, improving held-out accuracy by up to 35.9 points on a context-management task while reducing compute. We also introduce an online reinforcement learning method for CLMs, improving Qwen3.5-9B performance on BrowseComp-Plus by 47.6% while using 12% fewer FLOPs. Finally, we co-design Suffix Cache Reuse for CLM serving, further reducing server-side compute by 35% relative to standard SGLang at matched performance.

▲ 40 • 💬 2 • ⭐ 492 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2609.37725) • [💻 code](https://github.com/facebookresearch/context-language-models) • [🔗 project](https://github.com/facebookresearch/context-language-models)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 76 • 💬 1 • ⭐ 86,094 • 37mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[VisionHOPE: Visual Backbones as Self-Modifying Learning Systems](https://huggingface.co/papers/2609.33325)**

*Siran Peng, Tianshuo Zhang, Tianyu Fu et al. (11 authors)*

🏢 Mininglamp Technology

Visual backbones have evolved from Convolutional Neural Networks (CNNs) with local aggregation to Vision Transformers (ViTs) with global interactions, State-Space Models (SSMs) with input-dependent state transitions, and Test-Time Training (TTT) layers that adapt an inner learner while processing an image. Across this progression, visual computation has become increasingly adaptive to each input, yet the rules governing that adaptation remain largely prescribed by the trained backbone. We introduce VisionHOPE, the first generic visual backbone formulated as a self-modifying learning system, in which what the model remembers and how it learns co-evolve within an image. Building on the self-referential construction of Nested Learning (NL), VisionHOPE realizes this co-evolution through five coupled memories that store content, generate key and value representations, and govern learning rate and retention. These memories evolve jointly as visual context accumulates along each scan. However, directly applying the unconstrained self-referential update to a visual backbone leads to instability. We therefore derive a stability-matched step-size control scheme that combines a soft cap on self-referential injection with a spectral clamp on the retained memory transition, and prove that the resulting memory dynamics are non-expansive along each scan. For two-dimensional feature maps, we adapt NL's chunk formulation by aligning chunks with image rows and columns across four directional scans. The proposed VisionHOPE achieves competitive results on ImageNet-1K, COCO, and ADE20K, establishing self-modifying learning systems as a practical foundation for general-purpose visual backbones. The code is available at https://github.com/PSRben/VisionHOPE.

▲ 320 • 💬 2 • ⭐ 574 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2609.33325) • [💻 code](https://github.com/PSRben/VisionHOPE)

---

**[RRSI: Regularized Recursive Self-Improvement of Agent Harnesses](https://huggingface.co/papers/2609.24972)**

*Peng Xia, Rujun Han, Zifeng Wang et al. (14 authors)*

🏢 Google

An LLM agent's capability is largely magnified by its harness, namely the prompts, control flow, tooling, memory, and context management surrounding the frozen backbone model. Recent methods increasingly automate this process by iteratively proposing and selecting component-wise edits of an agent harness, practically establishing a form of recursive self-improvement (RSI) at the agent-system level. However, such recursive evolution may overfit by memorizing the training tasks, showing large in-distribution gains that shrink or even vanish on out-of-distribution benchmarks. We introduce Regularized Recursive Self-Improvement of Agent Harnesses (RRSI), which incorporates the principles of regularizations into harness self-improvement by constraining the evolution candidate proposal and selection. The proposer operates with a temporally annealed budget, limiting how many edits a candidate can bundle, and it encourages unexplored trajectories based on evolution history. The selector is equipped with a critic and a pruner: the critic screens benchmark-specific proposals, while the pruner, removes changes that are too small, too expensive, or no longer useful. Together these constraints favor reusable agent mechanisms over benchmark-specific ones or even noises. Across eight benchmarks spanning coding, agentic workspace and engineering design tasks, RRSI gains up to 14.1 points on the split it evolves against and up to 4.7 points on the five out-of-distribution benchmarks, while producing a harness that runs on 30% fewer policy tokens than the unregularized evolution. Code is available at https://github.com/google-research/rrsi and project page is https://regularized-rsi.com/.

▲ 221 • 💬 2 • ⭐ 1,237 • 13d ago

[🎓 arXiv](https://arxiv.org/abs/2609.24972) • [💻 code](https://github.com/google-research/rrsi) • [🔗 project](https://regularized-rsi.com/)

---

---

## GitHub Repositories: "ai"

**[zai-org/ZCode](https://github.com/zai-org/ZCode)**

Z.ai's coding agent harness. Powerful, intelligent, extensible.

`TypeScript`

⭐ 7.4k • 🔱 2.3k • 5d ago

---

**[Mak5er/AirCard](https://github.com/Mak5er/AirCard)**

Apple Wallet Card Skinner for iOS 18+ (No Jailbreak Required)

`Swift`

⭐ 6.0k • 🔱 359 • 7h ago

---

**[KKKKhazix/AIHOT](https://github.com/KKKKhazix/AIHOT)**

一个自己找热点、自己写日报的网站框架。把信源和精选标准换成你的，它就是你的行业热点站。

`TypeScript` `ai` `chinese` `content-curation` `daily-digest` `docker-compose`

⭐ 5.7k • 🔱 1.5k • 39m ago

---

**[yi1108/printfilm](https://github.com/yi1108/printfilm)**

PRINTFILM：AI 视频获客与 AI短剧创作平台

`Python`

⭐ 4.1k • 🔱 448 • 10d ago

---

**[CopilotKit/OpenDots](https://github.com/CopilotKit/OpenDots)**

Your always-on AI coworkers that move between text, calls, and Slack.

`TypeScript`

⭐ 3.1k • 🔱 406 • 1d ago

---

**[jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader)**

One AI trade decision every Monad block. Jev on Kuru MON-USDC.

`TypeScript`

⭐ 2.8k • 🔱 524 • 17d ago

---

**[feder-cr/dots](https://github.com/feder-cr/dots)**

Open-source dots for the web: an AI agent with its own browser, one that does not get blocked.

`Python` `ai-agent` `ai-agents` `ai-browser` `anti-detect-browser` `browser-agent`

⭐ 2.6k • 🔱 437 • 1d ago

---

**[yibie/awesome-jev](https://github.com/yibie/awesome-jev)**

A curated list of public projects, integrations, and discussions built on Jev — TypeSafe AI's System One model for typed decisions.

`Python` `awesome` `awesome-list` `jev` `llm`

⭐ 2.1k • 🔱 323 • 20h ago

---

**[kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill)**

A comprehensive logo-design skill for Claude, Gemini CLI, Codex and other AI agents: principles, process, SVG craft, testing tools and a 1,400+ logo reference library.

`HTML` `agent-skills` `branding` `claude` `claude-skills` `codex`

⭐ 1.8k • 🔱 113 • 3d ago

---

**[Mak5er/AirCard-iOS](https://github.com/Mak5er/AirCard-iOS)**

 Apple Wallet card skins and lock screen passcode themes on iOS 27. 

`Swift`

⭐ 1.6k • 🔱 178 • 5h ago

---

---

*Generated by PeekDeck - A glance is all you need*
