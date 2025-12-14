---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2025-12-14T14:00:52.383278+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- repositories
- social
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** December 14, 2025 at 14:00 UTC  
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

**[Exploring a more direct way to edit AI images after getting frustrated myself](https://www.reddit.com/r/artificial/comments/1pmc0h3/exploring_a_more_direct_way_to_edit_ai_images/)**

A lot of AI image tools are powerful, but they rely heavily on long, precise prompts. That works, but it also creates friction when you just want to change one small thing. I ran into this problem enough times that I started experimenting with a different interaction for myself. Instead of re-writing prompts, I tried pointing at the exact area in the image and describing the change in a few words. It made me wonder if spatial guidance can sometimes work better than text alone. I am curious how people here think about human in the loop interfaces like this. When does pointing beat prompting?

2h ago

---

**[Fei-Fei Li, a Stanford professor and CEO of AI startup World Labs, known as the 'Godmother of AI' says degrees are less important in hiring than how quickly you can ‘superpower yourself’ with new tools](https://www.reddit.com/r/artificial/comments/1plx3ah/feifei_li_a_stanford_professor_and_ceo_of_ai/)**

Instead, she looks to hire software engineers with AI fluency to her startup that aims to revolutionize the tech.

🔗 [Fortune](https://fortune.com/2025/12/12/fei-fei-li-stanford-professor-godmother-ai-college-degrees-skills-talent-ceo/) • 16h ago

---

**[Meta is pivoting away from open source AI to money-making AI](https://www.reddit.com/r/artificial/comments/1plnzz7/meta_is_pivoting_away_from_open_source_ai_to/)**

🔗 [bloomberg.com](https://www.bloomberg.com/news/articles/2025-12-10/inside-meta-s-pivot-from-open-source-to-money-making-ai-model) • 22h ago

---

**[AI is NOT the problem. The 1% billionaires who control them are. Their never-ending quest for power and more IS THE PROBLEM. Stop blaming the puppets and start blaming the puppeteers.](https://www.reddit.com/r/artificial/comments/1plxp93/ai_is_not_the_problem_the_1_billionaires_who/)**

15h ago

---

**[Sick of uploading sensitive PDFs to ChatGPT? I built a fully offline "Second Brain" using Llama 3 + Python (No API keys needed)](https://www.reddit.com/r/artificial/comments/1pmas1w/sick_of_uploading_sensitive_pdfs_to_chatgpt_i/)**

Hi everyone, I love LLMs for summarizing documents, but I work with some sensitive data (contracts/personal finance) that I strictly refuse to upload to the cloud. I realized many people are stuck between "not using AI" or "giving away their data". So, I built a simple, local RAG (Retrieval-Augmented Generation) pipeline that runs 100% offline on my MacBook. The Stack (Free & Open Source): Engine: Ollama (Running Llama 3 8b) Glue: Python + LangChain Memory: ChromaDB (Vector Store) It’s surprisingly fast. It ingests a PDF, chunks it, creates embeddings locally, and then I can chat with it without a single byte leaving my WiFi. I made a video tutorial walking through the setup and the code. (Note: Audio is Spanish, but code/subtitles are universal): 📺 https://youtu.be/sj1yzbXVXM0?si=s5mXfGto9cSL8GkW 💻 https://gist.github.com/JoaquinRuiz/e92bbf50be2dffd078b57febb3d961b2 Are you guys using any specific local UI for this, or do you stick to CLI/Scripts like me?

3h ago

---

**[Google Translate now lets you hear real-time translations in your headphones](https://www.reddit.com/r/artificial/comments/1pm09b8/google_translate_now_lets_you_hear_realtime/)**

The real-time headphone translations experience keeps each speaker’s tone, emphasis, and cadence intact, so it’s easier to follow the conversation and tell who’s saying what.

🔗 [TechCrunch](https://techcrunch.com/2025/12/12/google-translate-now-lets-you-hear-real-time-translations-in-your-headphones/) • 13h ago

---

**[AI Agent Outperforms Human Hackers in Stanford Cybersecurity Experiment](https://www.reddit.com/r/artificial/comments/1pm2lfg/ai_agent_outperforms_human_hackers_in_stanford/)**

An artificial intelligence agent has shown it can do what even seasoned cybersecurity professionals sometimes miss. In a controlled experiment at Stanford

🔗 [LearnGupt](https://scienceclock.com/ai-agent-beats-human-hackers-in-stanford-cybersecurity-experiment/) • 11h ago

---

**[One-Minute Daily AI News 12/14/2025](https://www.reddit.com/r/artificial/comments/1pm8i0t/oneminute_daily_ai_news_12142025/)**

Time’s 2025 Person of the Year: The architects of AI.[1] AI data center boom could be bad news for other infrastructure projects.[2] Google Translate brings real-time speech translations to any headphones.[3] OpenAI has Released the ‘circuit-sparsity’: A Set of Open Tools for Connecting Weight Sparse Models and Dense Baselines through Activation Bridges.[4] Sources: [1] https://www.reuters.com/business/media-telecom/architects-ai-named-times-person-year-2025-12-11/ [2] https://techcrunch.com/2025/12/13/ai-data-center-boom-could-be-bad-news-for-other-infrastructure-projects/ [3] https://www.theverge.com/news/843483/google-translate-live-speech-translations-headphones [4] https://www.marktechpost.com/2025/12/13/openai-has-released-the-circuit-sparsity-a-set-of-open-tools-for-connecting-weight-sparse-models-and-dense-baselines-through-activation-bridges/

6h ago

---

**[Built a pipeline for training HRM-sMOE LLMs](https://www.reddit.com/r/artificial/comments/1pm3e0v/built_a_pipeline_for_training_hrmsmoe_llms/)**

just as the title says, ive built a pipeline for building HRM & HRM-sMOE LLMs. However, i only have dual RTX 2080TIs and training is painfully slow. Currently working on training a model through the tinystories dataset and then will be running eval tests. Ill update when i can with more information. If you want to check it out here it is: https://github.com/Wulfic/AI-OS

11h ago

---

**[Sam Altman Got What He Wanted](https://www.reddit.com/r/artificial/comments/1plowm2/sam_altman_got_what_he_wanted/)**

For now

🔗 [The Atlantic](https://www.theatlantic.com/technology/2025/12/trump-ai-executive-order/685243/?utm_source=reddit&utm_medium=social&utm_campaign=the-atlantic&utm_content=edit-promo) • 21h ago

---

---

## Google News: "ai"

**[Jamie Dimon says soft skills like emotional intelligence and communication are vital as AI eliminates roles](https://fortune.com/2025/12/14/jamie-dimon-soft-skills-emotional-intelligence-communication-ai-eliminates-roles/)**

Dimon added that people who possess soft skills will have "plenty of jobs."

Fortune • 4h ago

---

**[The View From Inside the AI Bubble](https://www.theatlantic.com/technology/2025/12/neurips-ai-bubble-agi/685250/)**

Secret parties, lavish buffets, and talks of annihilation at one of the largest AI-research conferences

The Atlantic • 2h ago

---

**[It's beginning to look a lot like (AI) Christmas](https://www.axios.com/2025/12/14/ai-christmas-nativity-visuals-sermons-jesus)**

Axios • 1h ago

---

**[How Trump’s tech advisers overcame a MAGA rebellion over AI](https://www.washingtonpost.com/politics/2025/12/14/trump-ai-executive-order-divisions/)**

The Washington Post • 59m ago

---

**[Working with AI can be even more efficient with this all-in-one platform](https://mashable.com/article/dec-14-1minai-advanced-business-plan-lifetime-subscription)**

Experience the next level of AI efficiency.

Mashable • 4h ago

---

**[Trump signs executive order blocking states from enforcing their own regulations around AI](https://edition.cnn.com/2025/12/11/tech/ai-trump-states-executive-order)**

President Donald Trump on Thursday signed an executive order that blocks states from enforcing their own regulations around artificial intelligence and instead aims to create a “single national framework” for AI.

CNN • 2d ago

---

**[Experts urge caution as Trump’s big bill incentivizes AI in healthcare](https://www.theguardian.com/us-news/2025/dec/14/trump-healthcare-ai)**

Analysts say benefits could be felt in under-resourced rural hospitals but warn against AI as a cost-cutting measure

The Guardian • 1h ago

---

**[He created Grand Theft Auto. Now he's back with a novel about an AI that hijacks your mind](https://www.bbc.com/news/articles/c2epm9z9kkvo)**

A Better Paradise is a dystopian vision of the near future in which an AI-led computer game goes rogue.

BBC • 13h ago

---

**[For the First Time, AI Analyzes Language as Well as a Human Expert](https://www.wired.com/story/in-a-first-ai-models-analyze-language-as-well-as-a-human-expert/)**

If language is what makes us human, what does it mean now that large language models have gained “metalinguistic” abilities?

WIRED • 7h ago

---

**[Meet My Top 5 Artificial Intelligence (AI) Stocks for 2026](https://finance.yahoo.com/news/meet-top-5-artificial-intelligence-203000061.html)**

The AI computing market is a great place to invest.

Yahoo Finance • 17h ago

---

---

## HackerNews: "ai"

**[macOS 26.2 enables fast AI clusters with RDMA over Thunderbolt](https://news.ycombinator.com/item?id=46248644)**

Update your apps to use new features, and test your apps against API changes.

⬆️ 523 • 💬 280 • 1d ago • [Apple Developer Documentation](https://developer.apple.com/documentation/macos-release-notes/macos-26_2-release-notes#RDMA-over-Thunderbolt)

---

**[Ask HN: How can I get better at using AI for programming?](https://news.ycombinator.com/item?id=46255285)**

⬆️ 377 • 💬 379 • 22h ago

---

**[Disney making $1B investment in OpenAI, will allow characters on Sora AI](https://news.ycombinator.com/item?id=46231585)**

Disney is investing in OpenAI and has licensed its iconic characters like Mickey Mouse, Ariel and Iron Man to be used in the Sora AI video generator.

⬆️ 325 • 💬 2 • 2d ago • [CNBC](https://www.cnbc.com/2025/12/11/disney-openai-sora-characters-video.html)

---

**[Guarding My Git Forge Against AI Scrapers](https://news.ycombinator.com/item?id=46241849)**

A summary of the techniques in place to protect my git forge

⬆️ 170 • 💬 122 • 2d ago • [VulpineCitrus](https://vulpinecitrus.info/blog/guarding-git-forge-ai-scrapers/)

---

**[Using secondary school maths to demystify AI](https://news.ycombinator.com/item?id=46245731)**

Educators can show in secondary school maths that AI systems don’t think, making maths more interesting while teaching core concepts of AI.

⬆️ 129 • 💬 241 • 1d ago • [Raspberry Pi Foundation](https://www.raspberrypi.org/blog/secondary-school-maths-showing-that-ai-systems-dont-think/)

---

**[A Developer Accidentally Found CSAM in AI Data. Google Banned Him for It](https://news.ycombinator.com/item?id=46233067)**

Mark Russo reported the dataset to all the right organizations, but still couldn't get into his accounts for months.

⬆️ 119 • 💬 93 • 2d ago • [404 Media](https://www.404media.co/a-developer-accidentally-found-csam-in-ai-data-google-banned-him-for-it/)

---

**[If a Meta AI model can read a brain-wide signal, why wouldn't the brain?](https://news.ycombinator.com/item?id=46260106)**

In 2023, Meta researchers were able to decode images in thoughts from the brain's magnetic fields. What if that's how the brain coordinates it's own global state?

⬆️ 113 • 💬 66 • 12h ago • [1393](https://1393.xyz/writing/if-a-meta-ai-model-can-read-a-brain-wide-signal-why-wouldnt-the-brain)

---

**[New Kindle feature uses AI to answer questions about books](https://news.ycombinator.com/item?id=46248417)**

The new feature, called Ask this Book, is already drawing controversy and unanswered questions.

⬆️ 82 • 💬 128 • 1d ago • [Reactor](https://reactormag.com/new-kindle-feature-ai-answer-questions-books-authors/)

---

**[Purdue University approves new AI requirement for all undergrads](https://news.ycombinator.com/item?id=46257939)**

⬆️ 62 • 💬 55 • 17h ago • [forbes.com](https://www.forbes.com/sites/michaeltnietzel/2025/12/13/purdue-university-approves-new-ai-requirement-for-all-undergrads/)

---

**[AI is bringing old nuclear plants out of retirement](https://news.ycombinator.com/item?id=46254276)**

The White House has promised to quadruple nuclear power by 2050.

⬆️ 51 • 💬 66 • 1d ago • [wbur.org](https://www.wbur.org/hereandnow/2025/12/09/nuclear-power-ai)

---

---

## YouTube Videos: "ai"

**[Our 2025 Reports on Artificial Intelligence | 60 Minutes Full Episodes](https://www.youtube.com/watch?v=KpOcUrPdx-4)**

From November, Anderson Cooper's report on why Anthropic's CEO spends so much time warning of AI's potential dangers.

📺 60 Minutes

👁️ 213K • 👍 4K • 💬 562 • ⏱️ 1:21:07 • 1d ago

---

**[🇮🇳 India vs 🇵🇰 Pakistan | Epic AI Boxing Fight 🔥  #ai #trendingshorts #ytshorts #india  #pakistan](https://www.youtube.com/watch?v=MezlC1MtgMk)**

Dog V/S Dog – AI Generated Epic Fight Is AI generated Shorts video mein aap dekhenge ek zabardast aur intense fight ...

📺 ZX_SONU_EDITDZ

👁️ 3K • 💬 8 • ⏱️ 0:47 • 13h ago

---

**[OpenAI was dead… Then GPT-5.2 dropped](https://www.youtube.com/watch?v=rEvEXQvo-F8)**

Deploying on Railway feels like magic. Get $20 in free credits to try it out - https://railway.com/?referralCode=fireship Sam Altman ...

📺 Fireship

👁️ 353K • 👍 15K • 💬 836 • ⏱️ 4:01 • 1d ago

---

**[AI News: Deepseek Controversy, GPT-5.2, OpenAI x Disney, Meta Closed-Source and more!](https://www.youtube.com/watch?v=IHwt6UxiKOw)**

Try Greptile for free for 14 days! https://greptile.com/go/berman Download The Subtle Art of Not Being Replaced ...

📺 Matthew Berman

👁️ 41K • 👍 1K • 💬 258 • ⏱️ 15:01 • 1d ago

---

**[Why the AI Bubble Is Actually a $60T Black Hole](https://www.youtube.com/watch?v=21e5GZF3yx0)**

Start earning interest in gold: https://Monetary-Metals.com/GEN ----------------------- 🗞️ Sign up to our free newsletter to get smarter ...

📺 GEN

👁️ 64K • 👍 4K • 💬 662 • ⏱️ 22:33 • 1d ago

---

**[Glenn Beck&#39;s Idiot Contest With Ai George Washington](https://www.youtube.com/watch?v=0ABgUZtXzkI)**

Watch the Majority Report live Monday–Friday at 12pm EST on YouTube OR via daily podcast at http://www.Majority.fm The ...

📺 The Majority Report w/ Sam Seder

👁️ 70K • 👍 2K • 💬 609 • ⏱️ 12:51 • 1d ago

---

**[Paris’s AI Barber Pod 3.0 Will Blow Your Mind! 🤯 Next-Level Haircut ✅](https://www.youtube.com/watch?v=zA4FbVEC3lc)**

Paris's AI Barber Pod 3.0 is next-level insanity! ✂️ Get a flawless haircut in seconds, thanks to futuristic tech you won't believe ...

📺 Smart Tales

👁️ 20K • 👍 145 • ⏱️ 0:08 • 17h ago

---

**[AI Is Ruining Christmas...](https://www.youtube.com/watch?v=FKyzEFE50S0)**

The YouTube algorithm is now full of AI generated Christmas videos... Merry SLOPmas!! You know what's NOT AI slop? Skywork!

📺 Steve Terreberry

👁️ 112K • 👍 9K • 💬 1K • ⏱️ 16:45 • 14h ago

---

**[REACTING TO AI VIDEOS ABOUT ME..](https://www.youtube.com/watch?v=HGB-kBc9W5w)**

I Released My Own ROBLOX GAME! (Dump) https://www.roblox.com/games/98868317791094/DUMP-ALPHA 100k ROBUX ...

📺 CaylusBlox

👁️ 496K • 👍 11K • 💬 2K • ⏱️ 13:43 • 2d ago

---

**[Which Dream Bed Would You Choose? 🛏️✨ Ultimate Oddly Satisfying AI ASMR](https://www.youtube.com/watch?v=RxCG7MSt0pk)**

Join Impossible AIs and unlock exclusive perks! ✨ @ImpossibleAIs-c9z Drift into pure comfort—AI-crafted relaxing beds designed ...

📺 Impossible AIs

👁️ 124K • 👍 455 • 💬 13 • ⏱️ 8:26 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)**

*Tongyi-MAI*

Z-Image-Turbo is a highly efficient text-to-image diffusion transformer model with 6B parameters, achieving sub-second inference on H800 GPUs with 8 NFEs. It excels at photorealistic generation, bilingual text rendering (English/Chinese), and instruction adherence, fitting within 16GB VRAM.

`text-to-image`

⬇️ 277,583 • ❤️ 2,678 • 5d ago

---

**[VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B)**

*Microsoft*

VibeVoice-Realtime-0.5B is a lightweight, real-time text-to-speech model with ~300ms latency, supporting streaming input for robust long-form generation, ideal for live narration and LLM integration.

`text-to-speech` `1.0B`

⬇️ 130,627 • ❤️ 813 • 1d ago

---

**[GLM-4.6V-Flash](https://huggingface.co/zai-org/GLM-4.6V-Flash)**

*Z.ai*

GLM-4.6V-Flash is a lightweight multimodal model for image-text-to-text tasks, featuring native function calling for vision-driven tool use and interleaved content generation. It excels at multimodal document understanding, frontend replication, and low-latency applications.

`image-text-to-text` `10.3B`

⬇️ 67,698 • ❤️ 404 • 4d ago

---

**[Devstral-Small-2-24B-Instruct-2512](https://huggingface.co/mistralai/Devstral-Small-2-24B-Instruct-2512)**

*Mistral AI_*

Devstral Small 2 24B Instruct 2512 is a lightweight, agentic LLM for software engineering tasks, excelling at codebase exploration and multi-file editing with a 256k context window and FP8 precision. It is ideal for AI code assistants and agentic coding use cases, capable of running locally on consumer hardware.

`24.0B`

⬇️ 15,778 • ❤️ 323 • 2d ago

---

**[GLM-4.6V](https://huggingface.co/zai-org/GLM-4.6V)**

*Z.ai*

GLM-4.6V is a versatile multimodal model supporting image-text-to-text tasks, featuring native function calling for vision-driven tool use, interleaved content generation, and advanced multimodal document understanding with a 128k context window. It's suitable for complex business scenarios requiring perception-to-action capabilities.

`image-text-to-text` `107.7B`

⬇️ 3,369 • ❤️ 296 • 5d ago

---

**[AutoGLM-Phone-9B](https://huggingface.co/zai-org/AutoGLM-Phone-9B)**

*Z.ai*

AutoGLM-Phone-9B is a vision-language model for mobile intelligent assistance, enabling automated smartphone operations via ADB by understanding UI elements and executing natural language commands for task completion.

`image-text-to-text` `934,400`

⬇️ 35,747 • ❤️ 272 • 5d ago

---

**[GLM-ASR-Nano-2512](https://huggingface.co/zai-org/GLM-ASR-Nano-2512)**

*Z.ai*

GLM-ASR-Nano-2512 is a 1.5B parameter speech recognition model excelling in low-volume and dialectal (Cantonese) speech, outperforming Whisper V3 on benchmarks with a 4.10 average error rate. It's ideal for noisy environments and diverse linguistic use cases.

`automatic-speech-recognition` `2.3B`

⬇️ 5,553 • ❤️ 194 • 2d ago

---

**[Devstral-2-123B-Instruct-2512](https://huggingface.co/mistralai/Devstral-2-123B-Instruct-2512)**

*Mistral AI_*

Devstral 2 123B Instruct is an FP8 agentic LLM optimized for software engineering tasks, excelling in codebase exploration, multi-file editing, and powering SWE agents with a 256k context window.

`125.0B`

⬇️ 4,725 • ❤️ 193 • 2d ago

---

**[Apriel-1.6-15b-Thinker](https://huggingface.co/ServiceNow-AI/Apriel-1.6-15b-Thinker)**

*ServiceNow-AI*

Apriel-1.6-15B-Thinker is a cost-efficient multimodal reasoning model that excels at image-text-to-text tasks, achieving frontier performance with reduced token usage. It's suitable for enterprise use cases like function calling and instruction following, fitting on a single GPU.

`image-text-to-text` `14.9B`

⬇️ 1,276 • ❤️ 183 • 4d ago

---

**[GLM-TTS](https://huggingface.co/zai-org/GLM-TTS)**

*Z.ai*

GLM-TTS is a controllable, zero-shot text-to-speech system that uses a two-stage LLM and Flow Matching architecture, enhanced by multi-reward reinforcement learning for expressive emotion control and high-quality synthesis. It supports voice cloning from short prompts and streaming inference for interactive applications.

`text-to-speech`

⬇️ 0 • ❤️ 173 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 128 • 💬 6 • ⭐ 17,804 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[Z-Image: An Efficient Image Generation Foundation Model with Single-Stream Diffusion Transformer](https://huggingface.co/papers/2511.22699)**

*Z-Image Team, Huanqia Cai, Sihan Cao et al. (21 authors)*

🏢 Tongyi-MAI

Z-Image, a 6B-parameter Scalable Single-Stream Diffusion Transformer (S3-DiT) model, achieves high-performance image generation with reduced computational cost, offering sub-second inference and compatibility with consumer hardware.

▲ 192 • 💬 4 • ⭐ 6,814 • 17d ago

[🎓 arXiv](https://arxiv.org/abs/2511.22699) • [💻 code](https://github.com/Tongyi-MAI/Z-Image) • [🔗 project](https://tongyi-mai.github.io/Z-Image-blog/)

---

**[Decoupled DMD: CFG Augmentation as the Spear, Distribution Matching as the Shield](https://huggingface.co/papers/2511.22677)**

*Dongyang Liu, Peng Gao, David Liu et al. (11 authors)*

🏢 Tongyi-MAI

The study reveals that in text-to-image generation, CFG Augmentation is the primary driver of few-step distillation in Distribution Matching Distillation (DMD), while the distribution matching term acts as a regularizer.

▲ 24 • 💬 2 • ⭐ 6,817 • 17d ago

[🎓 arXiv](https://arxiv.org/abs/2511.22677) • [💻 code](https://github.com/Tongyi-MAI/Z-Image/tree/main) • [🔗 project](https://tongyi-mai.github.io/Z-Image-blog/)

---

**[The Well: a Large-Scale Collection of Diverse Physics Simulations for
  Machine Learning](https://huggingface.co/papers/2412.00568)**

*Ruben Ohana, Michael McCabe, Lucas Meyer et al. (26 authors)*

A large-scale dataset collection, The Well, provides diverse numerical simulations for benchmarking machine learning models in physical systems simulation.

▲ 23 • 💬 2 • ⭐ 1,514 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.00568) • [💻 code](https://github.com/PolymathicAI/the_well)

---

**[Wan-Move: Motion-controllable Video Generation via Latent Trajectory Guidance](https://huggingface.co/papers/2512.08765)**

*Ruihang Chu, Yefei He, Zhekai Chen et al. (13 authors)*

🏢 TongyiLab

Wan-Move enhances motion control in video generative models by integrating motion-aware features into latent space, enabling high-quality and scalable video synthesis.

▲ 121 • 💬 3 • ⭐ 327 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2512.08765) • [💻 code](https://github.com/ali-vilab/Wan-Move) • [🔗 project](https://wan-move.github.io/)

---

**[OmniFlatten: An End-to-end GPT Model for Seamless Voice Conversation](https://huggingface.co/papers/2410.17799)**

*Qinglin Zhang, Luyao Cheng, Chong Deng et al. (9 authors)*

A novel GPT-based model, OmniFlatten, enables real-time natural full-duplex spoken dialogue through a multi-stage post-training technique that integrates speech and text without altering the original model's architecture.

▲ 6 • 💬 1 • ⭐ 51,061 • 13mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.17799) • [💻 code](https://github.com/karpathy/nanogpt)

---

**[DeepCode: Open Agentic Coding](https://huggingface.co/papers/2512.07921)**

*Zongwei Li, Zhonghang Li, Zirui Guo et al. (5 authors)*

DeepCode, a fully autonomous framework, addresses the challenges of document-to-codebase synthesis by optimizing information flow through source compression, structured indexing, knowledge injection, and error correction, achieving state-of-the-art performance and surpassing human experts.

▲ 19 • 💬 2 • ⭐ 11,981 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2512.07921) • [💻 code](https://github.com/HKUDS/DeepCode)

---

**[SAM 3: Segment Anything with Concepts](https://huggingface.co/papers/2511.16719)**

*Nicolas Carion, Laura Gustafson, Yuan-Ting Hu et al. (38 authors)*

🏢 AI at Meta

Segment Anything Model 3 achieves state-of-the-art performance in promptable concept segmentation and tracking by leveraging a unified model architecture with decoupled recognition and localization.

▲ 112 • 💬 4 • ⭐ 5,792 • 24d ago

[🎓 arXiv](https://arxiv.org/abs/2511.16719) • [💻 code](https://github.com/facebookresearch/sam3) • [🔗 project](https://ai.meta.com/sam3/)

---

**[Visionary: The World Model Carrier Built on WebGPU-Powered Gaussian Splatting Platform](https://huggingface.co/papers/2512.08478)**

*Yuning Gong, Yifei Liu, Yifan Zhan et al. (24 authors)*

Visionary is an open web-native platform enabling real-time rendering of 3D Gaussian Splatting and meshes with efficient GPU-based inference, supporting dynamic content and generative models.

▲ 72 • 💬 4 • ⭐ 297 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2512.08478) • [💻 code](https://github.com/Visionary-Laboratory/visionary) • [🔗 project](https://visionary-laboratory.github.io/visionary/)

---

**[Live Avatar: Streaming Real-time Audio-Driven Avatar Generation with Infinite Length](https://huggingface.co/papers/2512.04677)**

*Yubo Huang, Hailong Guo, Fangtai Wu et al. (11 authors)*

🏢 Quark

Live Avatar uses a 14-billion-parameter diffusion model with Timestep-forcing Pipeline Parallelism and Rolling Sink Frame Mechanism to achieve real-time, high-fidelity avatar generation.

▲ 166 • 💬 4 • ⭐ 945 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2512.04677) • [💻 code](https://github.com/Alibaba-Quark/LiveAvatar) • [🔗 project](https://liveavatar.github.io/)

---

---

## GitHub Repositories: "ai"

**[zai-org/Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM)**

An Open Phone Agent Model & Framework. Unlocking the AI Phone for Everyone

`Python` `agent` `phone-use-agent`

⭐ 14.2k • 🔱 2.2k • 5h ago

---

**[Anionex/banana-slides](https://github.com/Anionex/banana-slides)**

一个基于nano banana pro🍌的原生AI PPT生成应用，迈向真正的＂Vibe PPT＂; 支持上传任意模板图片；上传任意素材&智能解析；一句话/大纲/页面描述自动生成PPT；口头修改指定区域、一键导出 - An AI-native PPT generator based on nano banana pro🍌

`Python` `ai-ppt-maker` `ai-slide-builder` `ai-slides` `llm` `nanobananapro`

⭐ 2.7k • 🔱 306 • 2h ago

---

**[glidea/banana-prompt-quicker](https://github.com/glidea/banana-prompt-quicker)**

🍌Awesome Prompts; Nano Banana；Banana Pro; Gemini；AI Studio；Prompt Quickly[正在开发 Sidebar 高级功能，敬请期待]

`JavaScript` `banana` `gemini` `prompt`

⭐ 1.7k • 🔱 137 • 5d ago

---

**[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)**

An AI SKILL that provide design intelligence for building professional UI/UX multiple platforms

`Python` `ai-skills` `antigravity` `claude` `claude-code` `command-line`

⭐ 1.2k • 🔱 308 • 8d ago

---

**[repplus/rep](https://github.com/repplus/rep)**

rep+ — Burp-style HTTP Repeater for Chrome DevTools with built‑in AI to explain requests and suggest attacks

`JavaScript` `css` `html` `javascript` `markdown`

⭐ 1.1k • 🔱 135 • 2d ago

---

**[Norsico/Video-Materials-AutoGEN-Workstation](https://github.com/Norsico/Video-Materials-AutoGEN-Workstation)**

一个集内容策划、AI文案自动生成、TTS 批量自动配音、(AI)图片素材合成、ASR自动提取语言字幕脚本、AI自由创作于一体的(短视频)生成工作站。方便管理每期的视频项目。

`Python`

⭐ 1.1k • 🔱 217 • 14d ago

---

**[AnandChowdhary/continuous-claude](https://github.com/AnandChowdhary/continuous-claude)**

🔂 Run Claude Code in a continuous loop, autonomously creating PRs, waiting for checks, and merging

`Shell` `ai` `ai-agents` `claude` `claude-code` `continuous-ai`

⭐ 951 • 🔱 67 • 5d ago

---

**[Hugo-Dz/spritefusion-pixel-snapper](https://github.com/Hugo-Dz/spritefusion-pixel-snapper)**

A tool to snap pixels to a perfect grid. Designed to fix messy and inconsistent pixel art generated by AI.

`Rust` `game-development` `gamedev` `image-processing` `pixel-art`

⭐ 891 • 🔱 23 • 6d ago

---

**[Ryandonofrio3/osgrep](https://github.com/Ryandonofrio3/osgrep)**

Open Source Semantic Search for your AI Agent

`TypeScript` `colbert` `embeddings` `grep` `grep-search`

⭐ 861 • 🔱 49 • 8h ago

---

**[firecrawl/open-scouts](https://github.com/firecrawl/open-scouts)**

  AI-powered web monitoring platform. Create automated scouts that search the web and send email alerts when they find what you're looking for. 

`TypeScript` `ai-agents` `alerts` `automation` `email-notifications` `firecrawl`

⭐ 692 • 🔱 100 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*
