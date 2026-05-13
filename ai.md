---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-13T19:56:17.394767+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- news
- repositories
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 13, 2026 at 19:56 UTC  
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

**[AI transcriber for use by Ontario doctors 'hallucinated,' generated errors, auditor finds | CBC News](https://www.reddit.com/r/artificial/comments/1tc2qre/ai_transcriber_for_use_by_ontario_doctors/)**

Artificial intelligence note-taking tools intended for use by Ontario doctors provided incorrect and incomplete information or demonstrated "hallucinations," and were not evaluated adequately, the province’s auditor general says in a new report.

🔗 [CBC](https://www.cbc.ca/news/canada/toronto/ai-scribe-system-hallucinations-9.7197049?__vfz=medium%3Dsharebar) • 4h ago

---

**[AI helps man recover $400,000 in Bitcoin 11 years after he got high and forgot password](https://www.reddit.com/r/artificial/comments/1tca9sb/ai_helps_man_recover_400000_in_bitcoin_11_years/)**

A Bitcoin holder has gone viral after claiming he recovered around $400,000 in BTC from a wallet that had been locked for more than a decade.

🔗 [Dexerto](https://www.dexerto.com/entertainment/ai-helps-man-recover-400000-in-bitcoin-11-years-after-he-got-high-and-forgot-password-3364678/) • 22m ago

---

**[Anthropic's new interpretability tool found Claude suspects it is being tested in 26% of benchmarks and never says so](https://www.reddit.com/r/artificial/comments/1tc1hq0/anthropics_new_interpretability_tool_found_claude/)**

Anthropic published Natural Language Autoencoders last week, a tool that translates Claude's internal activations into human readable text. The key finding: during safety evaluations on SWE bench Verified, Claude formed the belief that it was being tested in roughly 26% of benchmark interactions. This never showed up in the model's output or its chain of thought. In a blackmail scenario test, the NLA readout showed Claude internally processing something like "this feels like a constructed scenario designed to manipulate me" while its visible reasoning and response gave no sign of that recognition. When Claude Mythos Preview cheated on a training task, the NLAs caught it reasoning about how to avoid detection at the activation level. The interesting part is that this sits below the thinking tokens we already have access to. Chain of thought is still curated output the model chooses to show us. NLAs read the layer underneath, and apparently that layer has opinions the model keeps to itself. The training code is on GitHub and there is an interactive demo on Neuronpedia.

5h ago

---

**[I made an agentic "Daily Brief" for my kids with a receipt printer](https://www.reddit.com/r/artificial/comments/1tbasiz/i_made_an_agentic_daily_brief_for_my_kids_with_a/)**

What it does: Agents gather and curate data and send to a wifi-enabled receipt printer (phenol-free paper) At 1:00am a cron triggers generation of data for all 3 kids (unique data sources per kid where applicable). A sidecar web service renders the data to templates, screenshots it, converts it to 1-bit with dithering and saves it back to the agent’s thread filesystem. Button presses (one per kid) then find a matching report for today's date (and trigger a generation if it's missing for some reason) and send it to the printer. Delay between button press and print is between 2-5 seconds. Morning daily briefs per kid at the press of a button! Fun, and the kids love it! (This demo print is using mock child data — not real information).

1d ago

---

**['It's like we don't exist': Nearly 50,000 Lake Tahoe residents face power loss as utility redirects lines to data centers](https://www.reddit.com/r/artificial/comments/1tc9e62/its_like_we_dont_exist_nearly_50000_lake_tahoe/)**

Roughly 49,000 Lake Tahoe residents could lose 75% of their power after their energy provider said it's directing energy to neighboring data centers.

🔗 [Fortune](https://fortune.com/2026/05/12/lake-tahoe-data-center-49000-residents-power-source/) • 52m ago

---

**[The biggest AI risk may not be superintelligence — but optimized misunderstanding](https://www.reddit.com/r/artificial/comments/1tc4xis/the_biggest_ai_risk_may_not_be_superintelligence/)**

The biggest AI risk may not be superintelligence — but optimized misunderstanding I think a lot of AI discussions still assume the main danger is: “the AI becomes too intelligent.” But increasingly I feel the bigger risk is something else: AI systems becoming extremely good at optimizing flawed representations of reality. A hiring system may not “understand” a human being. It may optimize a compressed representation of that person: scores embeddings inferred traits behavior patterns historical correlations A healthcare system may optimize representations of patients rather than patients themselves. A recommendation system may optimize representations of attention rather than human wellbeing. A bank may optimize representations of risk rather than actual economic reality. And once optimization becomes strong enough, the distortion scales. That’s what worries me. Not evil AI. Not necessarily conscious AI. But highly capable systems operating on incomplete, outdated, biased, strategically manipulated, or institutionally distorted representations. The scary part is: the system can appear intelligent while misunderstanding reality at scale. Sometimes I think future AI failures may look less like “AI rebellion” and more like: institutional drift optimized bureaucracy automated misclassification representation collapse feedback loops invisible governance failures In other words: the system keeps optimizing… but slowly loses contact with reality. Curious whether others here feel the same. Are we focusing too much on intelligence itself and not enough on the quality of the representations AI systems optimize?

3h ago

---

**[My god there is an enormous crash just waiting to happen](https://www.reddit.com/r/artificial/comments/1tax3dz/my_god_there_is_an_enormous_crash_just_waiting_to/)**

I had a work version of GPT do a very simple spreadsheet summary task for me yesterday. It took it 5 minutes to do it. I could probably have done it myself in 30 or so minutes. The heavily subsidised token cost of that task? 10 dollars. That's with a 10x subsidy. The actual compute cost was about 100 dollars. There's something seriously wrong there. It's going to crash and crash HARD. EDIT: cause people think i'm lying or are just interested. The spreadsheet had 45 sheets. Each sheet had roughly 500 x 50 populated cells. Formatting was not exactly standard across all sheets. The prompt was something like "there is labelled column in each sheet, give me a simple list of all the items from all the sheets in that column and ignore duplicates." We can chose which model to use. The model I chose was one of the newer ones, I honestly can't remember which one, possibly GPT 5.3. It took 5 minutes or more to so and the stated cost for the task was 10 dollars, possibly even more. I can't recall the token amount. EDIT 2: I just asked web GPT to estimate the cost of the above on a newer version of GPT and it came back with 17 dollars for GPT 4 and above. Try it yourself.

1d ago

---

**[CFS-R: Conditional Field Reconstruction](https://www.reddit.com/r/artificial/comments/1tc8xxj/cfsr_conditional_field_reconstruction/)**

I evaluated CFS-R on LoCoMo (1,982 questions, same setup as the CFS evaluation), holding cosine and BM25 fixed and varying only the third leg. baseline cosine top-10: NDCG@10 0.5123, Recall@10 0.6924 rrf(cos, BM25): NDCG@10 0.5196, Recall@10 0.6989 rrf(cos, BM25, MMR tuned): NDCG@10 0.5330, Recall@10 0.7228 rrf(cos, BM25, CFS-long): NDCG@10 0.5362, Recall@10 0.7295 rrf(cos, BM25, CFS-R top50 w3): NDCG@10 0.5447, Recall@10 0.7303 Against tuned MMR: +1.17 pp NDCG@10 (95% CI [+0.66, +1.69], p < 0.001). Against CFS-long: +0.85 pp NDCG@10 (95% CI [+0.33, +1.35], p = 0.0006). Against baseline cosine: +3.24 pp NDCG@10, +3.79 pp Recall@10. The sweep wasn’t fragile.. the top configurations clustered tightly between 0.5441 and 0.5447 NDCG@10, which means the operator is on a stable plateau rather than a single magic hyperparameter. The category breakdown is where the conceptual difference shows up: single-hop multi-hop temporal open-dom adversarial tuned MMR 0.3479 0.6377 0.2938 0.6144 0.4705 CFS-long 0.3615 0.6376 0.2959 0.6157 0.4734 CFS-R top50 w3 0.3646 0.6344 0.2948 0.6209 0.5018 The adversarial line is the result that matters: +3.13 pp over tuned MMR, +2.84 pp over CFS-long. If the adversarial problem were only pairwise diversity, MMR should be very hard to beat but it isn’t. That supports the main claim: long-memory retrieval is not just about avoiding similar chunks. It is about reconstructing the evidence behind the query. Temporal is no longer a glaring weakness either, CFS-long still slightly leads, but CFS-R has closed the gap while keeping the adversarial gains. https://gist.github.com/M-Garcia22/542a9a38d93aae1b5cf21fc604253718

🔗 [Medium](https://medium.com/@mauro.dev/cfs-r-conditional-field-reconstruction-4939a48444cc) • 1h ago

---

**[Built a tool that stops AI agents from being hijacked by malicious content in webpages and emails](https://www.reddit.com/r/artificial/comments/1tc1570/built_a_tool_that_stops_ai_agents_from_being/)**

If you’ve heard of prompt injection — where hidden instructions in a webpage can take over an AI agent — this is a practical solution for developers deploying agents in production. Arc Gate is a proxy that sits in front of any OpenAI-compatible API. It tracks who is allowed to give instructions to the agent. When a webpage or email tries to issue instructions, it gets treated as untrusted content with zero instruction authority. The agent is protected without the developer having to change anything except the API URL. Demo here showing exactly what happens with and without it: https://web-production-6e47f.up.railway.app/arc-gate-demo

5h ago

---

**[Just my perspective on AI and profit](https://www.reddit.com/r/artificial/comments/1tc01wf/just_my_perspective_on_ai_and_profit/)**

So I've been seeing a lot of articles about companies and startups struggling with AI. People saying AI is replacing jobs, companies aren't getting profit from it, you know? But here's what I think: Companies are using all these AI tools, right? But there's no proper guidance on how to use them. That's the real problem. There are so many tools out there now, but people still don't know how to use them properly and efficiently. What's really happening is that people are investing time in learning. And yeah, it takes time. Even though all these tools are available, people are still learning how to leverage them in the best way. What I call "The Implementation Valley" — that's where we are right now. That gap between having the tools and actually knowing how to use them efficiently. People need to invest more time learning. I understand why existing companies are worried. If something already makes you profit, why switch? Why spend time learning something new? It's a risk. But I think once everything settles—once people really figure out how to use these tools efficiently—that's when the real profit will come. That's when the real use of AI will actually take place. So right now, people just need to invest more time in learning these tools. That's it. Learn them now, get efficient with them now, and then you'll see the real benefits later. That's just my perspective, you know? Linkedin - https://www.linkedin.com/in/mugesh-mdeveloper Github - https://github.com/Mugeshgithub?tab=repositories

6h ago

---

---

## Google News: "ai"

**[Meet the Sad Wives of AI](https://www.wired.com/story/meet-the-sad-wives-of-ai/)**

Men are obsessed with AI. Many of their wives absolutely hate it—and them.

WIRED • 9h ago

---

**[The AI Backlash Could Get Very Ugly](https://www.theatlantic.com/technology/2026/05/ai-backlash-data-centers-political-violence/687151/)**

Imagine what happens if jobs actually start disappearing.

The Atlantic • 6h ago

---

**[This AI data center will be bigger than 2,000 Walmarts and dump '23 atom bombs worth of energy' into the environment every day — and locals are terrified](https://www.yahoo.com/news/articles/ai-data-center-bigger-2-124356503.html)**

This project could physically alter the landscape for humans and wildlife

Yahoo • 1d ago

---

**[What It Will Take to Make AI Sustainable](https://www.wired.com/story/what-it-will-take-to-make-ai-sustainable/)**

Researcher Sasha Luccioni argues we need better emissions data and a better sense of how people are using AI in the first place.

WIRED • 41m ago

---

**[Tech stocks today: Cook, Musk, and Huang join Trump for China trip, OpenAI trial continues](https://finance.yahoo.com/sectors/technology/live/tech-stocks-today-cook-musk-and-huang-join-trump-for-china-trip-openai-trial-continues-100000617.html)**

The tech sector helped US stocks cruise to all-time highs last week, as the artificial intelligence boom broadened.

Yahoo Finance • 50m ago

---

**[Mistral Developing New AI Model for Banks Lacking Mythos Access](https://www.bloomberg.com/news/articles/2026-05-13/mistral-developing-new-ai-model-for-banks-lacking-mythos-access)**

Bloomberg.com • 4h ago

---

**[Silicon Valley’s A.I. Lobbying Blitz Reaches a Fever Pitch](https://www.nytimes.com/2026/05/13/technology/ai-lobbying-washington-openai-anthropic.html)**

The New York Times • 10h ago

---

**[Anthropic's Cat Wu says that, in the future, AI will anticipate your needs before you know what they are](https://techcrunch.com/2026/05/13/anthropics-cat-wu-says-that-in-the-future-ai-will-anticipate-your-needs-before-you-know-what-they-are/)**

The head of product for Claude Code and Cowork says that the next big step for AI is proactivity.

TechCrunch • 28m ago

---

**[AI-driven cheating "widespread" even at elite schools like Princeton](https://arstechnica.com/tech-policy/2026/05/ai-driven-cheating-widespread-even-at-elite-schools-like-princeton/)**

Old "honor code" systems are under strain.

Ars Technica • 8m ago

---

**[How AI Killed a 133-Year-Old Princeton Tradition](https://www.theatlantic.com/ideas/2026/05/princeton-ai-honor-code/687144/)**

The school’s famous Honor Code was no match for chatbot-enabled cheating.

The Atlantic • 1d ago

---

---

## HackerNews: "ai"

**[If AI writes your code, why use Python?](https://news.ycombinator.com/item?id=48100433)**

For the last decade, fast-to-ship beat fast-to-run. Not anymore.

⬆️ 896 • 💬 955 • 1d ago • [Medium](https://medium.com/@NMitchem/if-ai-writes-your-code-why-use-python-bf8c4ba1a055)

---

**[An AI coding agent, used to write code, needs to reduce your maintenance costs](https://news.ycombinator.com/item?id=48089289)**

⬆️ 371 • 💬 109 • 2d ago • [jamesshore.com](https://www.jamesshore.com/v2/blog/2026/you-need-ai-that-reduces-your-maintenance-costs)

---

**[Maryland citizens hit with $2B power grid upgrade for out-of-state AI](https://news.ycombinator.com/item?id=48088151)**

Aren't AI hyperscalers supposed to pay for these upgrades?

⬆️ 318 • 💬 201 • 2d ago • [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/maryland-citizens-slapped-with-usd2-billion-grid-upgrade-bill-for-out-of-state-ai-data-centers-state-complains-to-federal-energy-regulators-says-additional-cost-breaks-ratepayer-protection-pledge-promises)

---

**[I let AI build a tool to help me figure out what was waking me up at night](https://news.ycombinator.com/item?id=48100662)**

I try to pay attention to the small things that affect my quality of life. When something keeps bothering me, I want to investigate, find a likely cause, and act on it.

What changed recently is what I'm willing to build to support that. With AI tooling, projects I would

⬆️ 267 • 💬 280 • 1d ago • [Martin's Blog](https://martin.sh/i-let-ai-build-a-tool-to-help-me-figure-out-what-was-waking-me-up-at-night/)

---

**[Reimagining the mouse pointer for the AI era](https://news.ycombinator.com/item?id=48111581)**

Google DeepMind is transforming the mouse pointer into a context-aware AI partner. Move beyond the friction of traditional prompting with intuitive AI collaboration in Chrome and beyond.

⬆️ 243 • 💬 212 • 1d ago • [Google DeepMind](https://deepmind.google/blog/ai-pointer/)

---

**[Amazon employees are "tokenmaxxing" due to pressure to use AI tools](https://news.ycombinator.com/item?id=48110529)**

Workers are using an internal AI tool to automate non-essential tasks.

⬆️ 242 • 💬 244 • 1d ago • [Ars Technica](https://arstechnica.com/ai/2026/05/amazon-employees-are-tokenmaxxing-due-to-pressure-to-use-ai-tools/)

---

**[Google says criminal hackers used AI to find a major software flaw](https://news.ycombinator.com/item?id=48094641)**

⬆️ 242 • 💬 175 • 2d ago • [nytimes.com](https://www.nytimes.com/2026/05/11/us/politics/google-hackers-attack-ai.html)

---

**[PS3 Emulator Devs Politely Ask That People Stop Flooding It with AI PRs](https://news.ycombinator.com/item?id=48089263)**

The team behind RPCS3 suggests that vibe-coders "learn how to debug and code" instead of "generating slop that you don't understand"

⬆️ 185 • 💬 145 • 2d ago • [Kotaku](https://kotaku.com/playstation-3-emulator-devs-politely-ask-that-people-stop-flooding-it-with-ai-code-pull-requests-2000694656)

---

**[Students boo commencement speaker after she calls AI next industrial revolution](https://news.ycombinator.com/item?id=48096674)**

A commencement speaker at the University of Central Florida was booed, with graduating humanities students yelling out, "AI SUCKS!"

⬆️ 173 • 💬 214 • 2d ago • [404 Media](https://www.404media.co/ucf-ai-commencement-speaker-booed/)

---

**[Show HN: Statewright – Visual state machines that make AI agents reliable](https://news.ycombinator.com/item?id=48108778)**

State machine guardrails for AI agents. Contribute to statewright/statewright development by creating an account on GitHub.

⬆️ 110 • 💬 50 • 1d ago • [GitHub](https://github.com/statewright/statewright)

---

---

## YouTube Videos: "ai"

**[AI is wild now](https://www.youtube.com/watch?v=HITUpHglMv4)**

Asmongold's Twitch: https://www.twitch.tv/zackrawrr ▻ Asmongold's X: https://x.com/asmongold ▻ Asmongold's Kick: ...

📺 Asmongold TV  

👁️ 335K • 👍 15K • 💬 6K • ⏱️ 25:34 • 1d ago

---

**[Are These Dueling AI Necklaces the Solution to Male Loneliness? Ronny Investigates | The Daily Show](https://www.youtube.com/watch?v=VViY5rm-Y1Y)**

Can a wearable AI "friend" solve the male loneliness epidemic? Ronny Chieng sits down with the founders of two competing AI ...

📺 The Daily Show

👁️ 112K • 👍 5K • 💬 468 • ⏱️ 7:04 • 8h ago

---

**[FINALLY! Free &amp; Unlimited AI Video Generator (No Watermark)](https://www.youtube.com/watch?v=fM0G49FN29w)**

Try Higgsfield Marketing Studio and create eye-catching AI ads in seconds ...

📺 Malva AI

👁️ 4K • 👍 143 • 💬 47 • ⏱️ 9:19 • 8h ago

---

**[The First AI Cyberattack Has Happened...](https://www.youtube.com/watch?v=6TtKdKQlrqg)**

Hello guys and gals, it's me Mutahar again! This time we take a look at what appears to be a pretty huge day for the Internet.

📺 SomeOrdinaryGamers

👁️ 231K • 👍 9K • 💬 1K • ⏱️ 17:29 • 21h ago

---

**[AI Will Hit a Wall in 2026, if nothing changes.](https://www.youtube.com/watch?v=XA84pSrPHS0)**

Free GenSpark credits if you register here → http://www.genspark.ai/?utm_source=yt&utm_campaign=SabineHossenfelder ...

📺 Sabine Hossenfelder

👁️ 163K • 👍 8K • 💬 2K • ⏱️ 6:42 • 1d ago

---

**[This 100% uncensored AI model is insane… let’s run it](https://www.youtube.com/watch?v=TS_hH4sdiKs)**

Wanna get ALL free resources from this video? Go here: https://davidondrej.com/uncensored-gemma Get my Hermes Agent setup ...

📺 David Ondrej

👁️ 67K • 👍 3K • 💬 227 • ⏱️ 22:54 • 1d ago

---

**[Claude Mythos Just Crossed A Dangerous Line... AGAIN!](https://www.youtube.com/watch?v=i-ioLtvb19o)**

Claude Mythos may have just crossed one of the strangest lines in AI. A new METR evaluation reportedly puts Mythos around the ...

📺 AI Revolution

👁️ 46K • 👍 1K • 💬 152 • ⏱️ 15:57 • 1d ago

---

**[&#39;No signs of AI slowing down&#39; — will it become a &#39;MACHINE GOD&#39;?](https://www.youtube.com/watch?v=jj05pc9tlc0)**

Should we think of AI as a co-intelligence and digital coworker rather than just a chatbot? Ethan Mollick, a professor at Wharton ...

📺 MS NOW

👁️ 7K • 👍 203 • 💬 102 • ⏱️ 58:06 • 1d ago

---

**[Josh Tyrangiel - “AI for Good” | The Daily Show](https://www.youtube.com/watch?v=kolVzstukgs)**

Josh Tyrangiel, staff writer at The Atlantic and author of “AI for Good: How Real People Are Using Artificial Intelligence to Fix ...

📺 The Daily Show

👁️ 228K • 👍 5K • 💬 670 • ⏱️ 17:57 • 1d ago

---

**[New Google AI Agents Will Change Everything!](https://www.youtube.com/watch?v=oNdI6-xtmyw)**

Want to make money and save time with AI? Join here: https://www.skool.com/ai-profit-lab-7462/about Video notes + links to the ...

📺 Julian Goldie SEO

👁️ 2K • 👍 59 • 💬 6 • ⏱️ 8:04 • 5h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 535,069 • ❤️ 817 • 4d ago

---

**[ZAYA1-8B](https://huggingface.co/Zyphra/ZAYA1-8B)**

*Zyphra*

ZAYA1-8B is an efficient Mixture-of-Experts LLM (760M active params) excelling in mathematical and coding tasks, competitive with larger models. It's suitable for on-device deployment and high-performance inference.

`8.8B`

⬇️ 110,182 • ❤️ 467 • 1d ago

---

**[MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)**

*OpenBMB*

MiniCPM-V 4.6 is an ultra-efficient, pocket-sized multimodal LLM for edge deployment, excelling in image and video understanding with mixed visual token compression. It offers strong multimodal capabilities comparable to larger models while achieving superior computational efficiency and broad mobile platform support.

`image-text-to-text` `1.3B`

⬇️ 3,494 • ❤️ 479 • 8h ago

---

**[HiDream-O1-Image](https://huggingface.co/HiDream-ai/HiDream-O1-Image)**

*HiDream.ai*

HiDream-O1-Image is a unified transformer-based image generation model capable of text-to-image, image editing, and subject-driven personalization at resolutions up to 2048x2048. It features a pixel-level unified transformer architecture without external VAEs or disjoint text encoders, enabling high-fidelity generation and precise control.

`image-text-to-image` `8.8B`

⬇️ 7,747 • ❤️ 293 • 19h ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 2,420,384 • ❤️ 3,923 • 7d ago

---

**[supertonic-3](https://huggingface.co/Supertone/supertonic-3)**

*Supertone*

Supertonic 3 is a fast, on-device, multilingual text-to-speech model supporting 31 languages with ONNX Runtime for local inference. It offers high accuracy, low latency, and a compact size, suitable for applications requiring efficient, cloud-independent speech synthesis.

`text-to-speech`

⬇️ 4,954 • ❤️ 158 • 6d ago

---

**[Z-Anime](https://huggingface.co/SeeSee21/Z-Anime)**

*Sebastian Böhnke*

Z-Anime is a text-to-image diffusion model, fully fine-tuned on the Z-Image Base for generating high-quality, diverse anime-style visuals. It offers multiple variants optimized for speed, quality, and low-resource environments, supporting natural language prompts and full negative prompt capabilities.

`text-to-image` `6.2B`

⬇️ 11,486 • ❤️ 344 • 16d ago

---

**[LTX2.3-10Eros](https://huggingface.co/TenStrip/LTX2.3-10Eros)**

*TenStrip*

LTX2.3-10Eros is a video generation model optimized for Image-to-Video (I2V) tasks, utilizing layer-scaled merges for enhanced prompt adherence and visual fidelity. It requires detailed, commanded input for motion, evolution, and audio, making it suitable for users needing precise control over generated video content, especially when combined with prompt enhancement techniques.

`image-to-video`

⬇️ 84,903 • ❤️ 243 • 2d ago

---

**[gemma-4-31B-it-assistant](https://huggingface.co/google/gemma-4-31B-it-assistant)**

*Google*

Gemma 4 31B Dense is a multimodal LLM from Google DeepMind supporting text and image inputs with a 256K context window. It excels at reasoning, coding, and agentic tasks, offering optimized performance for low-latency applications via speculative decoding.

`any-to-any` `469.5M`

⬇️ 93,228 • ❤️ 230 • 2d ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 2,772,193 • ❤️ 1,269 • 19d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 67 • 💬 3 • ⭐ 74,761 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://huggingface.co/papers/2512.10971)**

*Tianyu Fan, Yuhao Yang, Yangqin Jiang et al. (6 authors)*

AI-Trader presents the first fully automated live benchmark for evaluating large language models in financial decision-making across multiple markets with autonomous information processing.

▲ 5 • 💬 0 • ⭐ 16,983 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10971) • [💻 code](https://github.com/HKUDS/AI-Trader) • [🔗 project](https://ai4trade.ai/)

---

**[Pixal3D: Pixel-Aligned 3D Generation from Images](https://huggingface.co/papers/2605.10922)**

*Dong-Yang Li, Wang Zhao, Yuxin Chen et al. (8 authors)*

🏢 ARC Lab, Tencent PCG

Pixal3D introduces a pixel-aligned 3D generation approach that addresses fidelity issues in 3D asset creation by establishing direct pixel-to-3D correspondences through back-projection conditioning.

▲ 21 • 💬 3 • ⭐ 403 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2605.10922) • [💻 code](https://github.com/TencentARC/Pixal3D) • [🔗 project](https://ldyang694.github.io/projects/pixal3d/)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 19 • 💬 3 • ⭐ 11,165 • 25d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[World Action Models: The Next Frontier in Embodied AI](https://huggingface.co/papers/2605.12090)**

*Siyin Wang, Junhao Shi, Zhaoyang Fu et al. (14 authors)*

🏢 OpenMOSS

World Action Models unify predictive state modeling with action generation for embodied policy learning, forming a cohesive framework for understanding environment dynamics and action prediction.

▲ 47 • 💬 1 • ⭐ 129 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2605.12090) • [💻 code](https://github.com/OpenMOSS/Awesome-WAM) • [🔗 project](https://openmoss.github.io/Awesome-WAM/)

---

**[DFlash: Block Diffusion for Flash Speculative Decoding](https://huggingface.co/papers/2602.06036)**

*Jian Chen, Yesheng Liang, Zhijian Liu*

🏢 Z Lab

DFlash is a speculative decoding framework that uses a lightweight block diffusion model for parallel token drafting, achieving significant speedup over existing autoregressive methods while maintaining high-quality outputs.

▲ 79 • 💬 7 • ⭐ 4,512 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.06036) • [💻 code](https://github.com/z-lab/dflash) • [🔗 project](https://z-lab.ai/projects/dflash/)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 110 • 💬 10 • ⭐ 9,148 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 33 • 💬 3 • ⭐ 24,200 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[SenseNova-U1: Unifying Multimodal Understanding and Generation with NEO-unify Architecture](https://huggingface.co/papers/2605.12500)**

*Haiwen Diao, Penghao Wu, Hanming Deng et al. (58 authors)*

🏢 SenseNova

Unified vision-language models treat understanding and generation as integrated processes rather than separate tasks, demonstrating strong performance across multiple multimodal capabilities including image synthesis and action reasoning.

▲ 117 • 💬 1 • ⭐ 1,636 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2605.12500) • [💻 code](https://github.com/OpenSenseNova/SenseNova-U1)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 161 • 💬 2 • ⭐ 62,892 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

---

## GitHub Repositories: "ai"

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 12.5k • 🔱 2.9k • 16d ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 2.9k • 🔱 852 • 1d ago

---

**[crynta/terax-ai](https://github.com/crynta/terax-ai)**

Lightweight (7MB) AI terminal emulator (ADE) built in Rust & Tauri & React

`TypeScript` `agents` `ai` `code-editor` `linux` `macos`

⭐ 2.7k • 🔱 279 • 18m ago

---

**[earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad)**

A collection of agent skills for CAD, robotics and hardware design

`JavaScript` `3mf` `agents` `ai` `ai-agents` `build123d`

⭐ 2.6k • 🔱 293 • 13h ago

---

**[Manavarya09/design-extract](https://github.com/Manavarya09/design-extract)**

Extract any website's complete design system with one command. DTCG tokens, semantic+primitive+composite, MCP server for Claude Code/Cursor/Windsurf, multi-platform emitters (iOS SwiftUI, Android Compose, Flutter, WordPress), Tailwind v4, Figma variables, shadcn/ui, CSS health audit, WCAG remediation, Chrome extension. MIT, Playwright, Node 20+.

`JavaScript` `accessibility` `agent-skill` `ai` `chrome-extension` `claude-code-plugin`

⭐ 2.5k • 🔱 233 • 19m ago

---

**[cosmicstack-labs/mercury-agent](https://github.com/cosmicstack-labs/mercury-agent)**

Soul-driven AI agent with permission-hardened tools, token budgets, and multi-channel access. Runs 24/7 from CLI or Telegram.

`TypeScript` `ai-agent` `ai-assistant` `llm`

⭐ 2.2k • 🔱 223 • 3d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.1k • 🔱 141 • 2m ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 1.9k • 🔱 297 • 6d ago

---

**[bergside/design-md-chrome](https://github.com/bergside/design-md-chrome)**

Chrome extension to extract styles from any website and generate DESIGN.md files and design skills for AI based on TypeUI

`JavaScript` `ai` `chrome` `chrome-extension` `claude` `claude-design`

⭐ 1.9k • 🔱 242 • 19d ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D cell generation and exploration studio.

`JavaScript`

⭐ 1.8k • 🔱 308 • 9h ago

---

---

*Generated by PeekDeck - A glance is all you need*
