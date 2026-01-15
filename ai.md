---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-01-15T21:23:01.296076+00:00'
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

**Last Updated:** January 15, 2026 at 21:23 UTC  
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

**[Senate passes bill letting victims sue over Grok AI explicit images](https://www.reddit.com/r/artificial/comments/1qcpxzs/senate_passes_bill_letting_victims_sue_over_grok/)**

The US Senate backs new civil rights for victims of AI-generated sexual abuse as lawmakers confront misuse of Elon Musk's Grok chatbot on X.

🔗 [Interesting Engineering](https://interestingengineering.com/ai-robotics/us-senate-passes-grok-ai-explicit-images-bill) • 1d ago

---

**[Modern Android phones are powerful enough to run 16x AI Upscaling locally, yet most apps force you to the cloud. So I built an offline, GPU-accelerated alternative.](https://www.reddit.com/r/artificial/comments/1qdjvis/modern_android_phones_are_powerful_enough_to_run/)**

Hi everyone, I wanted to share a project I have been working on to bring high-quality super-resolution models directly to Android devices without relying on cloud processing. I have developed RendrFlow, a complete AI image utility belt designed to perform heavy processing entirely on-device. The Tech Stack (Under the Hood): Instead of relying on an internet connection, the app runs the inference locally. I have implemented a few specific features to manage the load: - Hardware Acceleration: You can toggle between CPU, GPU, and a specific "GPU Burst" mode to maximize throughput for heavier models. - The Models: It supports 2x, 4x, and even 16x Super-Resolution upscaling using High and Ultra quality models. - Privacy: Because there is no backend server, it works in Airplane mode. Your photos never leave your device. Full Feature List: I did not want it to just be a tech demo, so I added the utilities needed for a real workflow: - AI Upscaler: Clean up low-res images with up to 16x magnification. - Image Enhancer: A general fix-it mode for sharpening and de-blurring without changing resolution. - Smart Editor: Includes an offline AI Background Remover and a Magic Eraser to wipe unwanted objects. - Batch Converter: Select multiple images at once to convert between formats (JPEG, PNG, WEBP) or compile them into a PDF. - Resolution Control: Manually resize images to specific dimensions if you do not need AI upscaling. Why I need your help: Running 16x models on a phone is heavy. I am looking for feedback on how the "GPU Burst" mode handles heat management on different chipsets . https://play.google.com/store/apps/details?id=com.saif.example.imageupscaler

7h ago

---

**[Bandcamp bans purely AI-generated music from its platform](https://www.reddit.com/r/artificial/comments/1qd11nu/bandcamp_bans_purely_aigenerated_music_from_its/)**

Indie music store says it wants fans to have confidence music was largely made by humans.

🔗 [Ars Technica](https://arstechnica.com/ai/2026/01/bandcamp-bans-purely-ai-generated-music-from-its-platform/) • 23h ago

---

**[Why you are (probably) using coding agents wrong](https://www.reddit.com/r/artificial/comments/1qdubfv/why_you_are_probably_using_coding_agents_wrong/)**

Most people probably use coding agents wrong. There I said it again. They treat agents like smart, autonomous teammates/junior dev with their own volition and intuition and then wonder why the output is chaotic, inconsistent, or subtly/less subtly broken. An agent is not a “better ChatGPT.” The correct mental model when using agent to write your code is to be an orchestrator of its execution, not let it be independent thinker and expecting "here is a task based on custom domain and my own codebase, make it work". You have to define the structure, constraints, rules, and expectations. The agent just runs inside that box. ChatGPT, Gemini, etc. work alone because they come with heavy built-in guardrails and guidelines and are tuned for conversation and problem solving. Agents, on the other hand, touch all content they have zero idea about: your code, files, tools, side effects. They don’t magically inherit discipline or domain knowledge. They have to get that knowledge. If you don’t supply your own guardrails, standards, and explicit instructions, the agent will happily optimize for speed and hallucinate its way through your repo. Agents amplify intent. If your intent isn’t well-defined, they amplify chaos. What really worked best for me is this structure, for example: You have this task to extend customer login logic: [long wall of text that is probably JIRA task written by PM before having morning coffee] this is the point where most people hit enter and just wait for agent to do "magic", but there is more To complete this task, you have to do X and Y, in those location A and B etc. Before you start on this task use the file in root directory named guidelines.txt to figure how to write the code. And this is where the magic happens, in guidelines.txt you want: all your ins and outs of your domain, your workflow (simplified) where the meat of the app is located (models, views, infrastructure) the less obvious "gotchas" what the agent can touch what the agent must NEVER touch or only after manual approval This approach yielded best results for me and least "man, that is just wrong, what the hell"

1h ago

---

**[The rise of "Green AI" in 2026: Can we actually decouple AI growth from environmental damage?](https://www.reddit.com/r/artificial/comments/1qdm7np/the_rise_of_green_ai_in_2026_can_we_actually/)**

We all know that training massive LLMs consumes an incredible amount of power. But as we move further into 2026, the focus is shifting from pure accuracy to "Energy-to-Solution" metrics. I’ve spent some time researching how the industry is pivoting towards Green AI. There are some fascinating breakthroughs happening right now: Knowledge Distillation: Shrinking massive models to 1/10th their size without losing capability. Liquid Cooling: Data centers that recycle heat to warm nearby cities. Neuromorphic Chips: A massive jump in "Performance per Watt." I put together a deep dive into how these technologies are being used to actually help the planet (from smart grids to ocean-cleaning robots) rather than just draining its resources. Would love to hear your thoughts. Are we doing enough to make AI sustainable, or is the energy demand growing too fast for us to keep up? "I wrote a detailed analysis on this, let me know if anyone wants the link to read more."

6h ago

---

**[Accelerating Discovery: How the Materials Project Is Helping to Usher in the AI Revolution for Materials Science](https://www.reddit.com/r/artificial/comments/1qdr06k/accelerating_discovery_how_the_materials_project/)**

"In 2011, a small team at the Department of Energy’s Lawrence Berkeley National Laboratory (Berkeley Lab) launched what would become the world’s most-cited materials database. Today, the Materials Project serves over 650,000 users and has been cited more than 32,000 times — but its real impact may just be emerging. When renowned computational materials scientist Kristin Persson and her team first created the Materials Project, they envisioned an automated screening tool that could help researchers in industry and academia design new materials for batteries and other energy technologies at an accelerated pace. [...] “Machine learning is game-changing for materials discovery because it saves scientists from repeating the same process over and over while testing new chemicals and making new materials in the lab,” said Persson, the Materials Project Director and Co-Founder. “To be successful, machine learning programs need access to large amounts of high-quality, well-curated data. With its massive repository of curated data, the Materials Project is AI ready.” [...] Researchers are currently looking for new battery materials to more effectively store energy for the grid or for transportation, or new catalysts to help improve efficiencies in the chemical industry. But experimental data are available for fewer than one percent of compounds in open scientific literature, limiting our understanding of new materials and their properties. This is where data-driven materials science can help. “Accelerating materials discoveries is the key to unlocking new energy technologies,” Jain said. “What the Materials Project has enabled over the last decade is for researchers to get a sense of the properties of hundreds of thousands of materials by using high-fidelity computational simulations. That in turn has allowed them to design materials much more quickly as well as to develop machine-learning models that predict materials behavior for whatever application they’re interested in.” [...] The Microsoft Corp. has also used the Materials Project to train models for materials science, most recently to develop a tool called MatterGen, a generative model for inorganic materials design. Microsoft Azure Quantum developed a new battery electrolyte using data from the Materials Project. Other notable studies used the Materials Project to successfully design functional materials for promising new applications. In 2020, researchers from UC Santa Barbara, Argonne National Laboratory, and Berkeley Lab synthesized Mn1+xSb, a magnetic compound with promise for thermal cooling in electronics, automotive, aerospace, and energy applications. The researchers found the magnetocaloric material through a Materials Project screening of over 5,000 candidate compounds. In addition to accessing the vast database, the materials community can also contribute new data to the Materials Project through a platform called MPContribs. This allows national lab facilities, academic institutions, companies, and others who have generated large data sets on materials to share that data with the broader research community. Other community contributions have expanded coverage into previously unexplored areas through new material predictions and experimental validations. For example, Google Deepmind — Google’s artificial intelligence lab — used the Materials Project to train initial GNoME (graph networks for materials exploration) models to predict the total energy of a crystal, a key metric of a material’s stability. Through that work, which was published in the journal Nature in 2023, Google DeepMind contributed nearly 400,000 new compounds to the Materials Project, broadening the platform’s vast toolkit of material properties and simulations."

🔗 [Berkeley Lab News Center](https://newscenter.lbl.gov/2026/01/13/accelerating-discovery-how-the-materials-project-is-helping-to-usher-in-the-ai-revolution-for-materials-science/) • 3h ago

---

**[Gemini is winning](https://www.reddit.com/r/artificial/comments/1qd4mhv/gemini_is_winning/)**

Could Siri be the last piece of the puzzle?

🔗 [The Verge](https://www.theverge.com/ai-artificial-intelligence/861863/google-gemini-ai-race-winner) • 20h ago

---

**[Zhipu AI breaks US chip reliance with first major model trained on Huawei stack (GLM-Image)](https://www.reddit.com/r/artificial/comments/1qdbld2/zhipu_ai_breaks_us_chip_reliance_with_first_major/)**

Zhipu claims GLM-Image achieved industry-leading scores among open-source models for text rendering and Chinese character generation.

🔗 [South China Morning Post](https://www.scmp.com/tech/tech-war/article/3339869/zhipu-ai-breaks-us-chip-reliance-first-major-model-trained-huawei-stack) • 15h ago

---

**[Good courses/discussions about Gemini CLI](https://www.reddit.com/r/artificial/comments/1qd4hm6/good_coursesdiscussions_about_gemini_cli/)**

Hello everyone! I would like to ask if you guys know any good material about best practices, tips, tutorials, and other stuff related to Gemini CLI. I would like specially about context management and prompt engineering! Thank you guys, have a nice day!

20h ago

---

**[Google went from being "disrupted" by ChatGPT, to having the best LLM as well as rivalling Nvidia in hardware (TPUs). The narrative has changed](https://www.reddit.com/r/artificial/comments/1qcfcm6/google_went_from_being_disrupted_by_chatgpt_to/)**

The public narrative around Google has changed significantly over the past 1 year. (I say public, because people who were closely following google probably saw this coming). Since Google's revenue primarily comes from ads, LLMs eating up that market share questioned their future revenue potential. Then there was this whole saga of selling the Chrome browser. But they made a great comeback with the Gemini 3 and also TPUs being used for training it. Now the narrative is that Google is the best position company in the AI era.

🔗 [decodingthefutureresearch.substack.com](https://decodingthefutureresearch.substack.com/p/how-has-the-narrative-around-google) • 1d ago

---

---

## Google News: "ai"

**[A.I. Has Arrived in Gmail. Here’s What to Know.](https://www.nytimes.com/2026/01/15/technology/personaltech/gmail-gemini-ai-email-inbox.html)**

The New York Times • 11h ago

---

**[Apple sits out AI arms race to play kingmaker between Google and OpenAI](https://www.ft.com/content/8033b1bc-4ffe-47ed-baf0-5abea6a1322a)**

Multibillion-dollar deal to secure Gemini models reflects cautious approach to infrastructure spending

Financial Times • 16h ago

---

**[Apple lost the AI race — now the real challenge starts](https://www.theverge.com/tech/861957/google-apple-ai-deal-iphone-gemini)**

Paging smarter Siri.

The Verge • 2h ago

---

**[‘It’s AI blackface’: social media account hailed as the Aboriginal Steve Irwin is an AI character created in New Zealand](https://www.theguardian.com/australia-news/2026/jan/15/aboriginal-steve-irwin-ai-character-created-new-zealand)**

More than 180,000 people follow the Bush Legend’s accounts across Meta platforms, but its Aboriginal host is a work of digital fiction

The Guardian • 7h ago

---

**[TSMC’s Blockbuster Spending Plans, Results Herald Continued AI Boom](https://www.wsj.com/business/earnings/tsmc-ends-2025-with-a-bang-as-ai-keeps-boosting-profits-9f775b1e?gaa_at=eafs&gaa_n=AWEtsqfiTf_wv-keEj-jgRE8lTK-UFmccQk4_pUXquvsKAP311CPCzCSGylA&gaa_ts=69695686&gaa_sig=xWhdzNQFVqo4UCHi3jdqQq4BeOuVCesKBaWcjDI5HBjEyL4DmrrKcxm-GLRwxR_bUva_gwjV7h6uRtUs9cPeUA%3D%3D)**

The Wall Street Journal • 11h ago

---

**[TSMC delivers another record quarter as profit jumps 35% fueled by robust AI chip demand](https://www.cnbc.com/2026/01/15/tsmc-q4-profit-record-ai-chip-demand-nt1-trillion.html)**

TSMCy delivered another estimate-beating quarter, with profit up 35% from a year ago as advanced chip orders tied to AI continued to dominate its business.

CNBC • 15h ago

---

**[AI trade back on? The company behind chip leaders like Nvidia and AMD just raised its spending forecast](https://www.cnbc.com/2026/01/15/ai-trade-the-company-behind-chip-leaders-like-nvidia-raised-its-spending-forecast.html)**

Robust earnings results from chip manufacturing giant TSMC just gave a huge lift to the AI trade.

CNBC • 1h ago

---

**[AI as a life coach: experts share what works, what doesn’t and what to look out for](https://www.theguardian.com/wellness/2026/jan/15/ai-life-coach)**

It’s becoming more common for people to use AI chatbots for personal guidance – but this doesn’t come without risks

The Guardian • 4h ago

---

**[Children are at risk of forming romantic bonds with AI chatbots, experts warn](https://www.foxnews.com/politics/experts-warn-lawmakers-establish-guardrails-ai-chatbots-form-romantic-bonds-children)**

Congress hears alarming testimony about AI chatbots harming children's mental health, with experts warning of serious emotional risks and dangers.

Fox News • 1h ago

---

**[McKinsey tests AI chatbot in early stages of graduate recruitment](https://www.artificialintelligence-news.com/news/mckinsey-tests-ai-chatbot-in-early-stages-of-graduate-recruitment/)**

McKinsey has introduced an AI chatbot into early stages of graduate recruitment to help manage application volume.

AI News • 11h ago

---

---

## HackerNews: "ai"

**[AI generated music barred from Bandcamp](https://news.ycombinator.com/item?id=46605490)**

⬆️ 939 • 💬 714 • 2d ago • [old.reddit.com](https://old.reddit.com/r/BandCamp/comments/1qbw8ba/ai_generated_music_on_bandcamp/)

---

**[We can't have nice things because of AI scrapers](https://news.ycombinator.com/item?id=46608840)**

⬆️ 461 • 💬 257 • 1d ago • [blog.metabrainz.org](https://blog.metabrainz.org/2025/12/11/we-cant-have-nice-things-because-of-ai-scrapers/)

---

**[Signal leaders warn agentic AI is an insecure, unreliable surveillance risk](https://news.ycombinator.com/item?id=46605553)**

With agentic AI embedded at the OS level, databases storing entire digital lives accessible to malware, tasks whose reliability quickly breaks down at each step, and being opted-in without consent, Signal leadership is sounding the alarm for the industry to pull back until threats can be mitigated.

⬆️ 344 • 💬 102 • 2d ago • [Coywolf](https://coywolf.com/news/productivity/signal-president-and-vp-warn-agentic-ai-is-insecure-unreliable-and-a-surveillance-nightmare/)

---

**[To those who fired or didn't hire tech writers because of AI](https://news.ycombinator.com/item?id=46629474)**

Hey you,
Yes, you, who are thinking about not hiring a technical writer this year or, worse, erased one or more technical writing positions last year because of AI. You, who are buying into the promise of docs entirely authored by LLMs without expert oversight or guidance. You, who unloaded the weight of docs on your devs’ shoulders, as if it was a trivial chore.
You are making a big mistake. But you can still undo the damage.

⬆️ 304 • 💬 217 • 13h ago • [passo.uno](https://passo.uno/letter-those-who-fired-tech-writers-ai/)

---

**[The Influentists: AI hype without proof](https://news.ycombinator.com/item?id=46623195)**

Why we are losing technical rigor to social hype

⬆️ 243 • 💬 167 • 1d ago • [A journey into a wild pointer](https://carette.xyz/posts/influentists/)

---

**[Games Workshop bans staff from using AI](https://news.ycombinator.com/item?id=46607681)**

Warhammer maker Games Workshop has banned the use of AI in its content production and its design process, insisting that none of its senior managers are currently excited about the technology.

⬆️ 232 • 💬 125 • 2d ago • [IGN](https://www.ign.com/articles/warhammer-maker-games-workshop-bans-its-staff-from-using-ai-in-its-content-or-designs-says-none-of-its-senior-managers-are-currently-excited-about-the-tech)

---

**[Raspberry Pi's New AI Hat Adds 8GB of RAM for Local LLMs](https://news.ycombinator.com/item?id=46629682)**

Today Raspberry Pi launched their new $130 AI HAT+ 2 which includes a Hailo 10H and 8 GB of LPDDR4X RAM.
With that, the Hailo 10H is capable of running LLMs entirely standalone, freeing the Pi's CPU and system RAM for other tasks. The chip runs at a maximum of 3W, with 40 TOPS of INT8 NPU inference performance in addition to the equivalent 26 TOPS INT4 machine vision performance on the earlier AI HAT with Hailo 8.

⬆️ 231 • 💬 190 • 12h ago • [Jeff Geerling](https://www.jeffgeerling.com/blog/2026/raspberry-pi-ai-hat-2/)

---

**[Let's be honest, Generative AI isn't going all that well](https://news.ycombinator.com/item?id=46605587)**

⬆️ 228 • 💬 323 • 2d ago • [garymarcus.substack.com](https://garymarcus.substack.com/p/lets-be-honest-generative-ai-isnt)

---

**[Google removes AI health summaries](https://news.ycombinator.com/item?id=46595419)**

AI Overviews provided false liver test information experts called alarming.

⬆️ 225 • 💬 172 • 2d ago • [Ars Technica](https://arstechnica.com/ai/2026/01/google-removes-some-ai-health-summaries-after-investigation-finds-dangerous-flaws/)

---

**[Show HN: OSS AI agent that indexes and searches the Epstein files](https://news.ycombinator.com/item?id=46611348)**

Search the Epstein archive — an AI agent grounded in indexed emails, messages, and documents, powered by Nia

⬆️ 205 • 💬 95 • 1d ago • [epstein.trynia.ai](https://epstein.trynia.ai/)

---

---

## YouTube Videos: "ai"

**[Microsoft Shocks AI World: &quot;China AI Is Now Too Powerful&quot;](https://www.youtube.com/watch?v=vcUBUQOyzFI)**

Microsoft just issued a warning that reframes the AI race: outside the West, China is gaining fast through scale, affordability, and ...

📺 AI Revolution

👁️ 50K • 👍 1K • 💬 165 • ⏱️ 14:32 • 1d ago

---

**[The AI Endgame](https://www.youtube.com/watch?v=rqR7z2eHOBE)**

The tech oligarchs want to RETVRN. If you like my stuff, consider supporting me on Patreon, which will give you early access to ...

📺 Adam Something

👁️ 409K • 👍 35K • 💬 4K • ⏱️ 11:40 • 2d ago

---

**[Anthropic: Our AI just created a tool that can ‘automate all white collar work’, Me:](https://www.youtube.com/watch?v=wYs6HWZ2FdM)**

A new tool, with code written *only* by AI, has gone omega-viral: Claude Cowork. But is the hype justified? What do the stats say ...

📺 AI Explained

👁️ 61K • 👍 2K • 💬 342 • ⏱️ 19:03 • 1d ago

---

**[Google&#39;s Galileo AI Just KILLED $97/m Funnel Builder Platforms (Build Pro Sites FREE With Zero Code)](https://www.youtube.com/watch?v=G_f6nYdbp68)**

I put the AI tools I use for helping local businesses in one place https://www.pauljames.com/AIToolsTraining Follow on ...

📺 iampauljames

👁️ 8K • 👍 436 • 💬 89 • ⏱️ 8:44 • 1d ago

---

**[AI influencers are somehow even worse now](https://www.youtube.com/watch?v=G6lt6CfJMlw)**

bleh.

📺 D'Angelo

👁️ 134K • 👍 7K • 💬 531 • ⏱️ 26:29 • 1d ago

---

**[Which One is AI?](https://www.youtube.com/watch?v=1ttPxy5d1xg)**

ZoomPartner Which one do you think it is? So excited to host this Live Event with Zoom please sign up and tell your school so we ...

📺 Rebecca Zamolo

👁️ 807K • 👍 9K • 💬 362 • ⏱️ 0:23 • 2d ago

---

**[Nvidia CEO Brutally Mocked After Saying AI Criticism Is Bad For Society...](https://www.youtube.com/watch?v=gajL7fUfhVU)**

SOURCES 1: https://www.youtube.com/watch?v=jgCOnpTdAsE&t=771s 2: https://insider-gaming.com/microsoft-ceo-ai-slop/ 3: ...

📺 YongYea

👁️ 143K • 👍 9K • 💬 2K • ⏱️ 15:35 • 1d ago

---

**[‘OPPORTUNITIES?’: How AI could reshape the job market](https://www.youtube.com/watch?v=87jgPUHp0eY)**

Panelists Taylor Riggs, Kenny Polcari and Jason Chaffetz talk the impact of artificial intelligence on jobs and children on 'FOX ...

📺 Fox Business

👁️ 3K • 👍 57 • 💬 26 • ⏱️ 6:58 • 12h ago

---

**[Antigravity NEW Update is HUGE! Agent Skills, Subagents, AI Automation, and More!](https://www.youtube.com/watch?v=oRAeNVx2kqM)**

The latest Antigravity update brings Agent Skills, Subagents, AI Automation, and more, taking your agentic workflows to the next ...

📺 WorldofAI

👁️ 21K • 👍 608 • 💬 39 • ⏱️ 9:11 • 17h ago

---

**[I Sent AI the ICE Shooting Video and Let It DECIDE Who Was in the Wrong](https://www.youtube.com/watch?v=kR7ododCSyA)**

I'm sending AI the raw footage of the ICE shooting of Renee Nicole Good in Minneapolis and asking who it thinks was in the ...

📺 I Ask AI

👁️ 218K • 👍 17K • 💬 3K • ⏱️ 13:08 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-Image](https://huggingface.co/zai-org/GLM-Image)**

*Z.ai*

GLM-Image is a text-to-image model with a hybrid autoregressive + diffusion decoder architecture, excelling in text rendering and knowledge-intensive generation. It supports both text-to-image and image-to-image tasks including editing and style transfer.

`text-to-image`

⬇️ 2,442 • ❤️ 672 • 11h ago

---

**[Qwen-Image-Edit-2511-Multiple-Angles-LoRA](https://huggingface.co/fal/Qwen-Image-Edit-2511-Multiple-Angles-LoRA)**

*fal*

This LoRA fine-tunes Qwen-Image-Edit-2511 for precise multi-angle image generation, offering 96 camera poses (4 elevations, 8 azimuths, 3 distances) trained on Gaussian Splatting data for 3D consistency. It enables detailed control over camera viewpoints, including low-angle shots, for advanced image editing and content creation.

`image-to-image`

⬇️ 44,101 • ❤️ 680 • 8d ago

---

**[LTX-2](https://huggingface.co/Lightricks/LTX-2)**

*Lightricks*

LTX-2 is a DiT-based audio-video foundation model capable of generating synchronized video and audio from various inputs including images, text, and audio. It supports local execution and offers distilled and upscaler checkpoints for practical applications.

`image-to-video`

⬇️ 1,187,843 • ❤️ 1,040 • 1d ago

---

**[AgentCPM-Explore](https://huggingface.co/openbmb/AgentCPM-Explore)**

*OpenBMB*

AgentCPM-Explore is a 4B parameter agent foundation model excelling in long-horizon tasks across 8 benchmarks like GAIA and BrowserComp. It features over 100 rounds of continuous interaction, multi-source validation, and dynamic strategy adjustment for on-device deep research.

`text-generation` `4.0B`

⬇️ 315 • ❤️ 285 • 1d ago

---

**[LTXV2_comfy](https://huggingface.co/Kijai/LTXV2_comfy)**

*Jukka Seppänen*

LTXV2_comfy is a separated checkpoint model designed for ComfyUI, enabling an alternative method for loading LTX2 models. It is compatible with LTX2 GGUFs that include metadata, though it may require a specific PR for ComfyUI-GGUF nodes.

`18.9B`

⬇️ 41,095 • ❤️ 277 • 1d ago

---

**[Qwen3-VL-Embedding-8B](https://huggingface.co/Qwen/Qwen3-VL-Embedding-8B)**

*Qwen*

Qwen3-VL-Embedding-8B is a multimodal embedding model that generates high-dimensional vectors from text, images, and videos for tasks like retrieval and clustering. It supports over 30 languages and customizable embedding dimensions, enabling efficient cross-modal understanding and search.

`image-to-text` `8.1B`

⬇️ 31,008 • ❤️ 251 • 6d ago

---

**[Qwen3-VL-Embedding-2B](https://huggingface.co/Qwen/Qwen3-VL-Embedding-2B)**

*Qwen*

Qwen3-VL-Embedding-2B is a 2B parameter multimodal embedding model that generates high-dimensional vectors for text, images, and videos. It excels at cross-modal understanding and retrieval tasks, supporting over 30 languages and customizable embedding dimensions for flexible integration.

`image-to-text` `2.1B`

⬇️ 36,629 • ❤️ 230 • 6d ago

---

**[HyperCLOVAX-SEED-Think-32B](https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-32B)**

*HyperCLOVA X*

HyperCLOVAX-SEED-Think-32B is a 32B parameter vision-language model capable of multimodal understanding (text, image, video) with a 128K token context length. It excels at Korean-centric reasoning and offers an optional 'thinking mode' for deep, controllable analysis, making it suitable for complex agentic tasks and advanced multimodal QA.

`text-generation` `33.3B`

⬇️ 31,316 • ❤️ 384 • 9d ago

---

**[nemotron-speech-streaming-en-0.6b](https://huggingface.co/nvidia/nemotron-speech-streaming-en-0.6b)**

*NVIDIA*

Nemotron-Speech-Streaming-En-0.6b is a 600M parameter English ASR model featuring a cache-aware FastConformer-RNNT architecture for low-latency streaming and high-throughput batch processing. It supports dynamic chunk sizes, punctuation, and capitalization, making it ideal for real-time applications like voice assistants and live captioning.

`automatic-speech-recognition`

⬇️ 4,414 • ❤️ 382 • 9d ago

---

**[medgemma-1.5-4b-it](https://huggingface.co/google/medgemma-1.5-4b-it)**

*Google*

MedGemma 1.5 4B is a multimodal instruction-tuned model for medical text and image comprehension, capable of interpreting high-dimensional imaging (CT, MRI), whole-slide histopathology, longitudinal chest X-rays, and EHR data. It excels in generating text for healthcare applications like clinical reasoning and medical document understanding.

`image-text-to-text` `4.3B`

⬇️ 4,422 • ❤️ 198 • 23h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models](https://huggingface.co/papers/2601.07372)**

*Xin Cheng, Wangding Zeng, Damai Dai et al. (14 authors)*

Conditional memory via Engram module enhances Transformer models by enabling efficient knowledge lookup and improving reasoning capabilities through optimized sparsity allocation.

▲ 11 • 💬 1 • ⭐ 2,454 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2601.07372) • [💻 code](https://github.com/deepseek-ai/Engram)

---

**[MiroThinker: Pushing the Performance Boundaries of Open-Source Research Agents via Model, Context, and Interactive Scaling](https://huggingface.co/papers/2511.11793)**

*MiroMind Team, Song Bai, Lidong Bing et al. (54 authors)*

We present MiroThinker v1.0, an open-source research agent designed to advance tool-augmented reasoning and information-seeking capabilities. Unlike previous agents that only scale up model size or context length, MiroThinker explores interaction scaling at the model level, systematically training the model to handle deeper and more frequent agent-environment interactions as a third dimension of performance improvement. Unlike LLM test-time scaling, which operates in isolation and risks degradation with longer reasoning chains, interactive scaling leverages environment feedback and external information acquisition to correct errors and refine trajectories. Through reinforcement learning, the model achieves efficient interaction scaling: with a 256K context window, it can perform up to 600 tool calls per task, enabling sustained multi-turn reasoning and complex real-world research workflows. Across four representative benchmarks-GAIA, HLE, BrowseComp, and BrowseComp-ZH-the 72B variant achieves up to 81.9%, 37.7%, 47.1%, and 55.6% accuracy respectively, surpassing previous open-source agents and approaching commercial counterparts such as GPT-5-high. Our analysis reveals that MiroThinker benefits from interactive scaling consistently: research performance improves predictably as the model engages in deeper and more frequent agent-environment interactions, demonstrating that interaction depth exhibits scaling behaviors analogous to model size and context length. These findings establish interaction scaling as a third critical dimension for building next-generation open research agents, complementing model capacity and context windows.

▲ 182 • 💬 5 • ⭐ 4,955 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.11793) • [💻 code](https://github.com/MiroMindAI/MiroThinker) • [🔗 project](https://dr.miromind.ai/)

---

**[LTX-2: Efficient Joint Audio-Visual Foundation Model](https://huggingface.co/papers/2601.03233)**

*Yoav HaCohen, Benny Brazowski, Nisan Chiprut et al. (29 authors)*

LTX-2 is an open-source audiovisual diffusion model that generates synchronized video and audio content using a dual-stream transformer architecture with cross-modal attention and classifier-free guidance.

▲ 117 • 💬 3 • ⭐ 2,491 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2601.03233) • [💻 code](https://github.com/Lightricks/LTX-2) • [🔗 project](https://app.ltx.studio/ltx-2-playground/i2v)

---

**[SimpleMem: Efficient Lifelong Memory for LLM Agents](https://huggingface.co/papers/2601.02553)**

*Jiaqi Liu, Yaofeng Su, Peng Xia et al. (8 authors)*

To support reliable long-term interaction in complex environments, LLM agents require memory systems that efficiently manage historical experiences. Existing approaches either retain full interaction histories via passive context extension, leading to substantial redundancy, or rely on iterative reasoning to filter noise, incurring high token costs. To address this challenge, we introduce SimpleMem, an efficient memory framework based on semantic lossless compression. We propose a three-stage pipeline designed to maximize information density and token utilization: (1) Semantic Structured Compression, which applies entropy-aware filtering to distill unstructured interactions into compact, multi-view indexed memory units; (2) Recursive Memory Consolidation, an asynchronous process that integrates related units into higher-level abstract representations to reduce redundancy; and (3) Adaptive Query-Aware Retrieval, which dynamically adjusts retrieval scope based on query complexity to construct precise context efficiently. Experiments on benchmark datasets show that our method consistently outperforms baseline approaches in accuracy, retrieval efficiency, and inference cost, achieving an average F1 improvement of 26.4% while reducing inference-time token consumption by up to 30-fold, demonstrating a superior balance between performance and efficiency. Code is available at https://github.com/aiming-lab/SimpleMem.

▲ 27 • 💬 2 • ⭐ 1,107 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2601.02553) • [💻 code](https://github.com/aiming-lab/SimpleMem) • [🔗 project](https://aiming-lab.github.io/SimpleMem-Page/)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 133 • 💬 19 • ⭐ 50,145 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[Controlled Self-Evolution for Algorithmic Code Optimization](https://huggingface.co/papers/2601.07348)**

*Tu Hu, Ronghao Chen, Shuo Zhang et al. (12 authors)*

🏢 QuantaAlpha

Controlled Self-Evolution method improves code generation through diversified initialization, feedback-guided genetic evolution, and hierarchical memory to enhance exploration efficiency and solution quality.

▲ 92 • 💬 2 • ⭐ 61 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2601.07348) • [💻 code](https://github.com/QuantaAlpha/EvoControl)

---

**[Multi-Agent Software Development through Cross-Team Collaboration](https://huggingface.co/papers/2406.08979)**

*Zhuoyun Du, Chen Qian, Wei Liu et al. (8 authors)*

Cross-Team Collaboration improves software quality by enabling multiple LLM agent teams to propose and communicate decisions.

▲ 0 • 💬 0 • ⭐ 28,678 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2406.08979) • [💻 code](https://github.com/OpenBMB/ChatDev)

---

**[DeepResearchEval: An Automated Framework for Deep Research Task Construction and Agentic Evaluation](https://huggingface.co/papers/2601.09688)**

*Yibo Wang, Lei Wang, Yue Deng et al. (10 authors)*

🏢 Infinity Lab

DeepResearchEval presents an automated framework for creating complex research tasks and evaluating them through agent-based methods that adapt to task specifics and verify facts without relying on citations.

▲ 85 • 💬 1 • ⭐ 60 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2601.09688) • [💻 code](https://github.com/Infinity-AILab/DeepResearchEval)

---

**[LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models](https://huggingface.co/papers/2403.13372)**

*Yaowei Zheng, Richong Zhang, Junhao Zhang et al. (5 authors)*

LlamaFactory is a unified framework enabling efficient fine-tuning of large language models across various tasks using a web-based user interface.

▲ 176 • 💬 6 • ⭐ 65,809 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.13372) • [💻 code](https://github.com/hiyouga/LLaMA-Factory) • [🔗 project](https://huggingface.co/spaces/hiyouga/LLaMA-Board)

---

**[Scaling Large-Language-Model-based Multi-Agent Collaboration](https://huggingface.co/papers/2406.07155)**

*Chen Qian, Zihao Xie, Yifei Wang et al. (10 authors)*

Multi-agent collaboration networks enhance collective intelligence, outperforming baselines across various topologies and showing emergent abilities earlier than neural scaling laws suggest.

▲ 3 • 💬 0 • ⭐ 28,681 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2406.07155) • [💻 code](https://github.com/OpenBMB/ChatDev/tree/macnet) • [🔗 project](https://github.com/OpenBMB/ChatDev/tree/macnet)

---

---

## GitHub Repositories: "ai"

**[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)**

"DeepTutor: AI-Powered Personalized Learning Assistant"

`Python` `ai-agents` `ai-tutor` `deepresearch` `idea-generation` `interactive-learning`

⭐ 8.7k • 🔱 1.1k • 4h ago

---

**[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)**

Browser automation CLI for AI agents

`TypeScript`

⭐ 6.0k • 🔱 265 • 1d ago

---

**[snarktank/ralph](https://github.com/snarktank/ralph)**

Ralph is an autonomous AI agent loop that runs repeatedly until all PRD items are complete. 

`TypeScript`

⭐ 4.1k • 🔱 554 • 8d ago

---

**[vercel-labs/json-render](https://github.com/vercel-labs/json-render)**

AI → JSON → UI

`TypeScript`

⭐ 3.0k • 🔱 120 • 17h ago

---

**[nguyenphutrong/quotio](https://github.com/nguyenphutrong/quotio)**

Stop juggling AI accounts. Quotio is a beautiful native macOS menu bar app that unifies your Claude, Gemini, OpenAI, Qwen, and Antigravity subscriptions – with real-time quota tracking and smart auto-failover for AI coding tools like Claude Code, OpenCode, and Droid.

`Swift` `ai-tools` `developer-tools` `proxy` `quota-monitor`

⭐ 2.5k • 🔱 150 • 6h ago

---

**[journey-ad/gemini-watermark-remover](https://github.com/journey-ad/gemini-watermark-remover)**

A high-performance, 100% client-side tool for removing Gemini AI watermarks. Built with pure JavaScript, it leverages a mathematically precise Reverse Alpha Blending algorithm rather than unpredictable AI inpainting. / 基于 Javascript 的纯浏览器端 Gemini AI 图像无损去水印工具，使用数学精确的反向 Alpha 混合算法

`JavaScript`

⭐ 2.1k • 🔱 238 • 4d ago

---

**[ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)**

LLM驱动的 A 股智能分析器，多数据源行情 + 实时新闻 + Gemini 决策仪表盘 + 多渠道推送，零成本，纯白嫖，定时运行

`Python` `agent` `ai` `aigc` `gemini` `llm`

⭐ 1.9k • 🔱 1.6k • 7h ago

---

**[datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe)**

Learn vibe coding from 0 to 1 | 实战中从零学会 AI 编程｜产品思维、前后端开发

`JavaScript` `agent` `ai` `coding` `course` `gemini`

⭐ 1.6k • 🔱 133 • 9h ago

---

**[numman-ali/cc-mirror](https://github.com/numman-ali/cc-mirror)**

Create multiple isolated Claude Code variants with custom providers (Z.ai, MiniMax, OpenRouter, LiteLLM)

`TypeScript`

⭐ 1.4k • 🔱 118 • 3d ago

---

**[heilcheng/awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills)**

A curated list of skills, tools, tutorials, and capabilities for AI coding agents (Claude, Codex, Copilot, VS Code)

`agent-skills` `ai-agents` `ai-development` `anthropic` `automation`

⭐ 1.3k • 🔱 91 • 16d ago

---

---

*Generated by PeekDeck - A glance is all you need*
