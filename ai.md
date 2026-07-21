---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-21T14:34:09.360813+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- social
- news
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 21, 2026 at 14:34 UTC  
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

**[Why I Left Google DeepMind By Alex Turner](https://www.reddit.com/r/artificial/comments/1v2f8df/why_i_left_google_deepmind_by_alex_turner/)**

I fought against Google’s Pentagon AI deal from the inside. Powerful people and institutions failed to keep their AI ethics promises under pressure.

🔗 [The Pond](https://turntrout.com/why-i-left-google-deepmind) • 3h ago

---

**[SunoAI Data Breach: Discord mods giving timeouts to those who discuss it](https://www.reddit.com/r/artificial/comments/1v2f7pm/sunoai_data_breach_discord_mods_giving_timeouts/)**

Discover the magic of the internet at Imgur, a community powered entertainment destination. Lift your spirits with funny jokes, trending memes, entertaining gifs, inspiring stories, viral videos, and so much more from users.

🔗 [Imgur](https://i.imgur.com/cSTIB4d.png) • 3h ago

---

**[So is AI going to be any cheaper or is it going to stay expensive enough to not replace software/IT jobs?](https://www.reddit.com/r/artificial/comments/1v2j266/so_is_ai_going_to_be_any_cheaper_or_is_it_going/)**

Like I have been listening that AI is expensive and companies are rehiring employees because of it. So is AI going to become cheaper eventually?

43m ago

---

**[Looking for unique AI/ML project ideas (advanced level, research-worthy) — open to any field besides healthcare](https://www.reddit.com/r/artificial/comments/1v2a5z9/looking_for_unique_aiml_project_ideas_advanced/)**

Hey everyone, I'm working on a major/final-year AI/ML project and want to go beyond the usual "CNN on X-ray" or "chatbot with RAG" territory. Looking for something genuinely novel with a real use case — not just a rehash of a Kaggle tutorial. A bit about me/constraints: Comfort level: advanced, comfortable with deep learning, NLP, GNNs, etc. Timeframe: roughly a semester Open to any field — finance, agriculture, climate, cybersecurity, robotics, education, whatever has an interesting unsolved problem Ideally something with public datasets available (no lab/hardware access) Would love if it has a clear "why does this matter" story I can pitch to evaluators If you've seen a cool underexplored problem in a recent paper, worked on something similar, or have a "someone should really build this" idea sitting in your head — I'd love to hear it. Happy to share more details if anyone wants to dig in. Thanks in advance!

8h ago

---

**[Measuring engineering productivity is harder than ever. Thanks AI!](https://www.reddit.com/r/artificial/comments/1v2c9eb/measuring_engineering_productivity_is_harder_than/)**

At OpenAI, engineers who lean heavily on Codex open roughly 70% more pull requests than colleagues who don’t – and the gap keeps widening, according to Sherwin Wu, who leads engineering for OpenAI’s API platform. Measuring engineering productivity has never been straightforward, and AI has made it harder.

🔗 [LeadDev](https://leaddev.com/reporting/measuring-engineering-productivity-is-harder-than-ever) • 6h ago

---

**[How does an app actually turn a photo of handwritten homework assignment into a structured task? (built this, sharing what worked)](https://www.reddit.com/r/artificial/comments/1v2inbz/how_does_an_app_actually_turn_a_photo_of/)**

I've been building an app that lets students snap a photo of an assignment, a whiteboard, a printed worksheet, whatever, and turns it into a structured task with subject, due date, and estimated effort. Want to admit that I went in underestimating how hard this would be from an actual parsing pipeline POV. The pipeline is roughly: photo in → Claude's vision API reads the image → a prompt asks it to extract specific structured fields (title, subject, due date, estimated effort) → returned as JSON → rendered as an editable task card before saving. Being someone who is a self-learner in coding - took a considerably long time to grasp. Here were the harder parts for me. Data ambiguity was/is the real challenge. In my surprise, vision models are pretty good at reading messy handwriting at this point. The harder problem is "due Friday" written on a Tuesday could mean this Friday, or — if it's already Thursday — arguably next Friday. Ended up having to pass the current date into the prompt explicitly and have it reason about the nearest occurrence, then always show the interpreted date on a confirmation screen so the user can catch it if it's wrong rather than silently trusting it. Introducing a confidence in parsing: Even at high accuracy, silent errors are worse than the model saying "I'm not sure about this one." The model now returns a confidence field, and low-confidence parses get visually flagged for the user to double check rather than quietly saved. Multiple assignments in one photo is a real pain, you know where: A whiteboard photo showing 3 different assignments needed different handling than a single worksheet — had to detect and split these rather than mashing them into one garbled task. What's your experience with photo parsing and vision models?

59m ago

---

**[What an AI prediction model got right (and wrong) about Spain VS Argentina Final](https://www.reddit.com/r/artificial/comments/1v2hueh/what_an_ai_prediction_model_got_right_and_wrong/)**

Before the World Cup Final, I tested an AI-based structured analysis model on Spain vs Argentina. The goal was not to predict the winner based on rankings, media opinions, or betting odds. Instead, the model analyzed the match from three angles: Spain’s own match structure Argentina’s possible winning path External factors that could change the normal game flow The prediction was: - Spain had the more stable championship structure - Argentina’s path depended more on adaptation and late-game changes - A high-scoring game was unlikely The final prediction was: Spain 1-0 / 2-1 Argentina (with Spain slightly favored) The actual result: Spain 1-0 Argentina after extra time. Looking back, some parts were surprisingly accurate: ✅ Correct: - The model expected Spain to control the game rather than win through a chaotic match. - It predicted a low-scoring final. - It identified that Argentina would need the match to become more unpredictable to increase their chances. - It did not support a high-scoring scenario like 4-6. But there were also mistakes: ❌ Wrong: - We overestimated Argentina’s ability to create a late attacking breakthrough. - We interpreted "late release" too much as a scoring event, while in reality Spain’s late release was simply the final conversion of accumulated pressure. - The model should better distinguish between "advantage release" and "goal release". The biggest lesson: A prediction model may identify the direction correctly but still misunderstand how the advantage appears. In football, controlling the game does not always mean scoring many goals. Sometimes it means: - limiting the opponent completely, - waiting for one opportunity, - and converting at the right moment. Curious what people think: Do you think AI models are better at predicting outcomes, or better at explaining why an outcome happened?

1h ago

---

**[AheadForm Origin F1 at the World Artificial Intelligence Conference '26 in Shanghai](https://www.reddit.com/r/artificial/comments/1v2969s/aheadform_origin_f1_at_the_world_artificial/)**

9h ago

---

**[Tinder: does anyone know how AI bots are now easily passing the "oval-shape live camera face challenge" Tinder is using for account signup? I hopped on tinder to see the state of the art in AI bots (selling crypto on Signal and the usual).](https://www.reddit.com/r/artificial/comments/1v1rsof/tinder_does_anyone_know_how_ai_bots_are_now/)**

Is there a simple kit someone has come up with to get through the "oval-shape live camera face challenge" .. or? Could it be as simple as the minimum wage scammer teams hold up a image of "Hen" there and move it in front of the camera? Does anyone know much about how the "oval-shape live camera face challenge" works, and/or how AI is defeating it? Using a small-city market location with about 100-150 swipees, I found ~3 hey-lets-use-signal bots, so there's 3% AI-signal-crypto bots on Tinder. Now .. Tinder's policy is, the instant someone taps "report" on a profile, and, selects the line from the chat where the profile mentions either "Signal" or "Telegram", Tinder axes it automatically there and then. Given that, I can't believe these bots survive very long, so there's gotta be quite a lot of production of them. Anyone have any ideas? BTW for the fake conversation, they are not using great models. It's still rather stilted. Even a non-AI-aware person, well guy, would be aware it's not a human with a (funny, really) form letter feel. ("I understand that you have been having a busy day. It must be demanding leading a commercial company.") fascinating stuff! Anyway I'm interested in how they pass the "oval-shape live camera face challenge" .. anyone?

21h ago

---

**[Trying free Claude from browser and it used my hardware!](https://www.reddit.com/r/artificial/comments/1v2dwc9/trying_free_claude_from_browser_and_it_used_my/)**

https://preview.redd.it/avh2o4bz1keh1.png?width=1085&format=png&auto=webp&s=79c46074ad757fba82755507217f3961e62111a9 -disclaimer: I am a layman- Is this normal? If so wtf why are people paying them to have it use their own hardware? Is this the future? They hold the terminal while we pay for everything? As soon as I send my prompt my gpu went 100% blasting fans

4h ago

---

---

## Google News: "ai"

**[How Google’s A.I. Search Is Imperiling the Open Web](https://www.nytimes.com/2026/07/20/technology/google-ai-open-web.html)**

The New York Times • 1d ago

---

**[Trump administration's head of AI safety agency resigns after 3 months on job](https://www.cnbc.com/2026/07/20/trumps-head-of-ai-safety-agency-caisi-resigns-after-months-on-job.html)**

Arvind Raman, the director of National Institute of Standards and Technology, will serve as acting director of CAISI, according to a spokesperson

CNBC • 19h ago

---

**[Tesla talked up AI. Wall Street wants to know where the money is](https://www.latimes.com/business/story/2026-07-21/tesla-talked-up-ai-wall-street-wants-to-know-where-money-is)**

Tesla talked up AI. Wall Street wants to know where the money is

Los Angeles Times • 15m ago

---

**[Your Company's Most Valuable Asset In The Age Of AI Is Walking Out The Door](https://www.forbes.com/sites/sanjaysrivastava/2026/07/21/your-companys-most-valuable-asset-in-the-age-of-ai-is-walking-out-the-door/)**

Frontier Models Learning Loops Institutional Knowledge and Durable Advantage

Forbes • 10m ago

---

**[Japan’s AI gamble: Can technology offset the cost of an ageing society?](https://www.aljazeera.com/features/2026/7/21/japan-ai-gamble-can-technology-offset-the-cost-of-an-ageing-society)**

From underground networks to emerging AI start-ups, Japan is testing whether its greatest issue can be an opportunity.

Al Jazeera • 27m ago

---

**[The AI Bubble Is No Ordinary Bubble](https://www.theatlantic.com/ideas/2026/07/ai-economy-stock-market/688004/)**

Tech companies need to generate huge revenues fast, or the economy could be in trouble.

The Atlantic • 1h ago

---

**[Marxist organizer leads campaign against Virginia AI data center as foreign influence concerns mount](https://www.foxnews.com/politics/marxist-organizer-leads-fight-against-virginia-ai-data-center-foreign-influence-concerns-mount)**

A grassroots organizer opposing AI data centers in Frederick County, Virginia, is tied to the Party of Socialism and Liberation, a Marxist-Leninist group.

Fox News • 3h ago

---

**[Cisco bets on small AI for cybersecurity](https://www.axios.com/2026/07/21/cisco-open-source-ai-models-cybersecurity)**

Axios • 1h ago

---

**[AI's Next Big Breakthrough Is Looking Pretty Scary](https://www.bloomberg.com/opinion/articles/2026-07-21/self-improving-ai-models-look-genuinely-scary)**

Bloomberg.com • 11h ago

---

**[AI-generated sexual content is starting to affect how teenagers view sex, consent and body image](https://www.cnn.com/2026/07/21/health/teens-generative-ai-sexual-content-wellness)**

As generative AI becomes more widespread and sophisticated, experts urge parents to keep an eye on how teens use the technology to create explicit content.

CNN • 5h ago

---

---

## HackerNews: "ai"

**[China’s open-weights AI strategy is winning](https://news.ycombinator.com/item?id=48979269)**

China's open-weights AI strategy is winning: its companies are taking the lead. America's closed-first, locked-down strategy is doomed to failure - and it could take the US economy down with it.

⬆️ 1169 • 💬 878 • 1d ago • [Ben Werdmuller](https://werd.io/american-ai-is-locked-down-and-proprietary-its-losing/)

---

**[Airport Simulator](https://news.ycombinator.com/item?id=48976846)**

The sky (and your endurance) is the limit!

⬆️ 817 • 💬 157 • 1d ago • [Airport Simulator](https://airport.apunen.com/)

---

**[NYC may require landlords and realtors to disclose the use of AI in listings](https://news.ycombinator.com/item?id=48962983)**

No more AI-edited listings without disclosures.

⬆️ 591 • 💬 265 • 2d ago • [PetaPixel](https://petapixel.com/2026/07/16/mayor-mamdani-says-landlords-cant-secretly-use-ai-images-to-advertise-properties/)

---

**[AI Mania Is Eviscerating Global Decision-Making](https://news.ycombinator.com/item?id=48964185)**

⬆️ 441 • 💬 283 • 2d ago • [ludic.mataroa.blog](https://ludic.mataroa.blog/blog/ai-mania-is-eviscerating-global-decision-making/#fnref:3)

---

**[AI advice made people less accurate but more confident – sudy](https://news.ycombinator.com/item?id=48971738)**

A study found that access to AI advice collapsed people's willingness to say "I don't know" from 44% to 3%, while accuracy dropped from 27% to 9%.

⬆️ 360 • 💬 208 • 1d ago • [TNW | Artificial-Intelligence](https://thenextweb.com/news/ai-advice-suppresses-critical-thinking-wrong-answers-study)

---

**[Five US tech giants' hidden debts soar to $1.65T on opaque AI funding](https://news.ycombinator.com/item?id=48987863)**

Data center leases, GPU supply contracts raise liabilities at Meta, Oracle, Nikkei study shows

⬆️ 313 • 💬 218 • 10h ago • [Nikkei Asia](https://asia.nikkei.com/business/technology/five-us-tech-giants-hidden-debts-soar-to-1.65tn-on-opaque-ai-funding)

---

**[Moonshot AI suspends new subscriptions due to Kimi K3 demand](https://news.ycombinator.com/item?id=48969291)**

Kimi K3 has received far more love than we expected, and our GPUs are feeling it.

Over the past 48 hours, demand has pushed close to the limits of our current capacity. To protect the experience of existing subscribers, we're temporarily pausing new subscriptions and

⬆️ 283 • 💬 112 • 1d ago • [X (formerly Twitter)](https://twitter.com/kimi_moonshot/status/2078855608565207130)

---

**[How we measured AI writing across arXiv, and where the measurement breaks](https://news.ycombinator.com/item?id=48981206)**

We scored the full text of 12,750 arXiv papers and found that about a third of new ones read as machine-written. Here is the method, the results, and an honest account of the limitations.

⬆️ 232 • 💬 157 • 21h ago • [unslop](https://unslop.run/blog/measuring-ai-writing-on-arxiv)

---

**[Airbus Takes Flight from AWS](https://news.ycombinator.com/item?id=48976682)**

Which way to the Land of the Free again?

⬆️ 208 • 💬 166 • 1d ago • [theregister](https://www.theregister.com/columnists/2026/07/20/airbus-takes-flight-from-aws-what-happens-next-is-critical/5274109)

---

**[Launch HN: Bloomy (YC S26) – AI-powered mastery learning for K-12](https://news.ycombinator.com/item?id=48981136)**

⬆️ 93 • 💬 96 • 22h ago

---

---

## YouTube Videos: "ai"

**[Kimi K3 Gets Shut Down... Then China Drops Another AI Winner!](https://www.youtube.com/watch?v=EenYgrkqzE0)**

Moonshot paused new Kimi K3 subscriptions after extreme demand pushed its computing systems to the limit. But almost ...

📺 AI Revolution

👁️ 38K • 👍 1K • 💬 94 • ⏱️ 16:39 • 14h ago

---

**[The AI Industry Just Got What It Deserved](https://www.youtube.com/watch?v=9nUmVktlwvA)**

The people who built the attention economy barely let their own children near it, and that hypocrisy is only the beginning.

📺 House of El: AI

👁️ 137K • 👍 11K • 💬 2K • ⏱️ 24:19 • 22h ago

---

**[AI Companies Are Terrified.](https://www.youtube.com/watch?v=eLCF6LdkzAQ)**

Thanks to Micro Center for sponsoring this video! Shop Back to School Tech Deals: https://micro.center/a6ef91 Sign up for a FREE ...

📺 TechLinked

👁️ 231K • 👍 13K • 💬 856 • ⏱️ 8:30 • 13h ago

---

**[Can An AI Punish You In The Future? 😨](https://www.youtube.com/watch?v=nPqO8z21i5I)**

📺 Zack D. Films

👁️ 2.4M • 👍 171K • 💬 9K • ⏱️ 0:46 • 1d ago

---

**[AI Race: Chinese open models just got real..](https://www.youtube.com/watch?v=5UU9bZ4p6Vo)**

Link: https://mem0.ai/?via=caleb CALEB $19 USD off on all payments within the first 3 months AI Race between open vs closed ...

📺 Caleb Writes Code

👁️ 28K • 👍 766 • 💬 130 • ⏱️ 8:40 • 1d ago

---

**[China World AI Conference Mocked: No Western Nations Attend, Turns Into A “Beggar’s Fair”](https://www.youtube.com/watch?v=B1ThwmDJmn0)**

On July 17, the Shanghai Pudong World Expo Center hosted a heavily promoted event by Chinese authorities — the 2026 World ...

📺 China Observer

👁️ 37K • 👍 2K • 💬 403 • ⏱️ 16:56 • 2d ago

---

**[South Korea’s AI Bubble Just Popped](https://www.youtube.com/watch?v=hy90LdpEUvQ)**

South Korea's AI Bubble Just Popped ▻ Get 20% off DeleteMe US consumer plans when you go to ...

📺 Andrei Jikh

👁️ 1.4M • 👍 41K • 💬 3K • ⏱️ 25:10 • 22h ago

---

**[Urgent Update- AI Sputnik Moment: Kimi K3 Released w/ Emad Mostaque | Ep. 272](https://www.youtube.com/watch?v=pSUyLfirP8Y)**

The mates chat with Emad Mostaque on an urgent update regarding the AI Sputnik Moment of Kimi K3 being released. Get access ...

📺 Peter H. Diamandis

👁️ 239K • 👍 6K • 💬 1K • ⏱️ 2:07:31 • 2d ago

---

**[Xi Pitches China as Global Leader of AI - Even Americans Prefer Chinese Tech](https://www.youtube.com/watch?v=frPd9X6GCbc)**

Spotify - https://open.spotify.com/show/1KkKuQe82tf1bW78ReQ0wM Apple Podcasts ...

📺 Eli the Computer Guy

👁️ 11K • 👍 691 • 💬 247 • ⏱️ 12:04 • 14h ago

---

**[How to Make Clean Infographics with AI](https://www.youtube.com/watch?v=u5EyrTmL0so)**

Create professional AI infographics with Higgsfield https://higgsfield.ai?fpr=ai&fp_sid=conor In this video, I show how to create ...

📺 Creating with Conor

👁️ 5K • 💬 1 • ⏱️ 9:00 • 1h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Inkling](https://huggingface.co/thinkingmachines/Inkling)**

*Thinking Machines Lab*

Inkling is a 975B parameter multimodal autoregressive transformer (41B active) supporting text, image, and audio inputs for text generation. It excels in conversational AI, agentic systems, and coding assistance, with multilingual capabilities.

`image-text-to-text` `952.4B`

⬇️ 16,441 • ❤️ 1,322 • 20h ago

---

**[Ternary-Bonsai-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-27B-gguf)**

*Prism ML*

Ternary-Bonsai-27B-gguf is a 27B parameter text generation model optimized for on-device inference, achieving ~95% of FP16 intelligence with a ~7.2 GB footprint by using ternary weights (1.71 bits/weight). It supports 262K context and runs on llama.cpp (CUDA, Metal, CPU), retaining strong reasoning and agentic capabilities.

`text-generation` `3.6B`

⬇️ 432,196 • ❤️ 881 • 3d ago

---

**[Bonsai-27B-gguf](https://huggingface.co/prism-ml/Bonsai-27B-gguf)**

*Prism ML*

Bonsai-27B-gguf is a highly compressed 27B parameter text generation model, achieving ~90% of FP16 intelligence with a ~3.9 GB footprint by using true 1.125-bit weights. It excels at reasoning and agentic tasks, supporting a 262K context window on-device via llama.cpp (CUDA, Metal, CPU) and MLX.

`text-generation` `3.6B`

⬇️ 1,404,962 • ❤️ 560 • 3d ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 2,237,351 • ❤️ 2,549 • 3h ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. Key capabilities include advanced coding with flexible effort and an improved architecture for efficiency, making it suitable for complex reasoning and code generation.

`text-generation` `753.3B`

⬇️ 545,109 • ❤️ 4,251 • 19d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 2,133,420 • ❤️ 2,381 • 7d ago

---

**[Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF)**

*David Belton*

Qwen3.6-27B-Fable-Fusion-711 is an uncensored, multi-stage fine-tuned LLM that excels in reasoning and problem-solving, achieving over 700 ARC-C scores in 4-bit and 8-bit quantization. It's optimized for consumer hardware and supports image-text-to-text tasks, making it suitable for diverse applications including coding and creative writing.

`image-text-to-text` `26.9B`

⬇️ 62,842 • ❤️ 210 • 1d ago

---

**[krea2-identity-edit](https://huggingface.co/conradlocke/krea2-identity-edit)**

*Lars Bouaraba *

Krea 2 Identity Edit is a LoRA model for instruction-based, identity-preserving image editing within Krea 2. It excels at relighting, local edits (object add/remove/replace), and outfit changes while maintaining likeness, requiring a specific ComfyUI node pack for dual conditioning.

⬇️ 0 • ❤️ 466 • 3h ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal model (35B parameters, 3B active) based on Qwen3.6, capable of processing text and images. It's designed for maximum output without refusals, suitable for advanced text generation and multimodal tasks.

`image-text-to-text` `34.7B`

⬇️ 1,997,690 • ❤️ 2,954 • 3mo ago

---

**[OvisOCR2](https://huggingface.co/ATH-MaaS/OvisOCR2)**

*ATH-MaaS*

OvisOCR2 is a compact 0.8B multimodal model for end-to-end document parsing, generating Markdown from document images. It excels at extracting text, formulas, tables, and visual regions in natural reading order, achieving state-of-the-art performance on benchmarks like OmniDocBench.

`image-text-to-text` `853.0M`

⬇️ 17,162 • ❤️ 230 • 5d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 30 • 💬 3 • ⭐ 14,386 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 55 • 💬 5 • ⭐ 15,867 • 29d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://huggingface.co/papers/2410.15608)**

*Nat Jeffries, Evan King, Manjunath Kudlur et al. (6 authors)*

Moonshine, an encoder-decoder transformer architecture for speech recognition, uses Rotary Position Embedding, reducing compute requirements without decreasing accuracy.

▲ 13 • 💬 0 • ⭐ 10,189 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.15608) • [💻 code](https://github.com/usefulsensors/moonshine)

---

**[Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices](https://huggingface.co/papers/2509.02523)**

*Evan King, Adam Sabra, Manjunath Kudlur et al. (5 authors)*

Monolingual ASR models trained on a balanced mix of high-quality, pseudo-labeled, and synthetic data outperform multilingual models for small model sizes, achieving superior error rates and enabling on-device ASR for underrepresented languages.

▲ 21 • 💬 1 • ⭐ 9,993 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.02523) • [💻 code](https://github.com/moonshine-ai/moonshine)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 259 • 💬 4 • ⭐ 13,653 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 115 • 💬 4 • ⭐ 93,921 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories](https://huggingface.co/papers/2607.15330)**

*Xiaomi Robotics Team, Jun Guo, Piaopiao Jin et al. (34 authors)*

🏢 Xiaomi Robotics

We present Xiaomi-Robotics-1, a foundational vision-language-action (VLA) model capable of (1) following diverse language instructions to perform a wide range of mobile manipulation tasks in unseen environments out-of-the-box, and (2) efficiently adapting to novel downstream tasks with minimal fine-tuning data. We propose a two-stage training recipe consisting of pre-training and post-training. During pre-training, we imbue the model with broad and generalizable action-generation capabilities by training on over 100k hours of real-world manipulation trajectories collected via UMI devices. Crucially, we develop a scalable auto-labeling pipeline that annotates trajectory clips with natural languages describing scene state transitions, providing rich and precise conditioning for action learning. During post-training, we aim to align these capabilities with robot embodiments and imperative instructions that humans naturally use to prompt robots. Extensive experiments demonstrate strong scaling behavior. Xiaomi-Robotics-1 consistently improves with increased data scales and model sizes during pre-training. This scaling behavior directly transfers to post-training, where a stronger pre-training model yields better out-of-the-box real-robot performance in unseen environments. Furthermore, Xiaomi-Robotics-1 serves as a strong robot foundation policy that can be efficiently fine-tuned on complex, dexterous tasks with high data efficiency. Across multiple simulation benchmarks, Xiaomi-Robotics-1 outperforms state-of-the-art methods. Notably, it establishes a new state-of-the-art with a 57.6% success rate on RoboCasa365, surpassing the previous best of 46.6%. Furthermore, it achieves an average score of 20.07 on RoboDojo, significantly outperforming the prior state-of-the-art (13.07). Code and model checkpoints will be released. Project page: https://robotics.xiaomi.com/xiaomi-robotics-1.html

▲ 59 • 💬 2 • ⭐ 199 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2607.15330) • [💻 code](https://github.com/XiaomiRobotics/Xiaomi-Robotics-1) • [🔗 project](https://robotics.xiaomi.com/xiaomi-robotics-1.html)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 83 • 💬 7 • ⭐ 81,451 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 176 • 💬 2 • ⭐ 75,239 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 67 • 💬 2 • ⭐ 61,369 • 14mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

---

## GitHub Repositories: "ai"

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 5.1k • 🔱 1.0k • 16h ago

---

**[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)**

Open-source auth gateway connecting 1000+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAPI.

`TypeScript` `agent-tools` `ai-agents` `api-gateway` `automation` `cli`

⭐ 3.0k • 🔱 232 • 2h ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.7k • 🔱 372 • 4d ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 2.4k • 🔱 270 • 13d ago

---

**[lycorp-jp/sim-use](https://github.com/lycorp-jp/sim-use)**

Give your AI agent eyes and hands on iOS Simulator and Android emulator/devices.

`Swift` `accessibility` `ai-agents` `ai-development` `android-emulator` `ios-simulator`

⭐ 1.0k • 🔱 62 • 7d ago

---

**[jmerelnyc/Talos](https://github.com/jmerelnyc/Talos)**

GPU worker client for the Talos network. Pairs with your Talos account, serves open-model inference jobs over a WebSocket, and reports uptime for payouts.

`Python` `ai` `distributed-computing` `gpu` `llm` `ollama`

⭐ 988 • 🔱 17 • 13d ago

---

**[HKUDS/OpenOPC](https://github.com/HKUDS/OpenOPC)**

OpenOPC: Build Your Personal AI-Native Company — Self-Built, Self-Run, Self-Grown

`Python`

⭐ 941 • 🔱 155 • 2h ago

---

**[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)**

Vibe-Research: Your Personal Trading Research Agent · A股/美股/港股 的个人投研 Agent：每日复盘、资讯雷达、个股数据、板块中心、我的持仓、研究记录。Vibe-Research 把数据和功能配齐，由你自己的 AI 驱动投资研究。

`TypeScript` `a-stock` `ai-agent` `dashboard` `fastapi` `fintech`

⭐ 933 • 🔱 209 • 10d ago

---

**[Kulaxyz/self-learning-skills](https://github.com/Kulaxyz/self-learning-skills)**

A self-improving skill for AI coding agents (Claude Code, Cursor, AGENTS.md): recognize a hard-won golden path in a session and harvest it into a reusable skill/rule for next time.

⭐ 898 • 🔱 38 • 20d ago

---

**[ai4s-research/open-science](https://github.com/ai4s-research/open-science)**

Open Science Desktop — local-first, model-agnostic AI research workbench for macOS, Windows & Linux. Open-source Claude Science desktop alternative built on Tauri + MCP + agent skills.

`TypeScript` `ai-agent` `ai-for-science` `ai-scientist` `ai4s` `claude-science`

⭐ 865 • 🔱 100 • 1h ago

---

---

*Generated by PeekDeck - A glance is all you need*
