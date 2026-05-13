---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-13T06:49:01.730619+00:00'
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

**Last Updated:** May 13, 2026 at 06:49 UTC  
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

**[I made an agentic "Daily Brief" for my kids with a receipt printer](https://www.reddit.com/r/artificial/comments/1tbasiz/i_made_an_agentic_daily_brief_for_my_kids_with_a/)**

What it does: Agents gather and curate data and send to a wifi-enabled receipt printer (phenol-free paper) At 1:00am a cron triggers generation of data for all 3 kids (unique data sources per kid where applicable). A sidecar web service renders the data to templates, screenshots it, converts it to 1-bit with dithering and saves it back to the agent’s thread filesystem. Button presses (one per kid) then find a matching report for today's date (and trigger a generation if it's missing for some reason) and send it to the printer. Delay between button press and print is between 2-5 seconds. Morning daily briefs per kid at the press of a button! Fun, and the kids love it! (This demo print is using mock child data — not real information).

12h ago

---

**[My god there is an enormous crash just waiting to happen](https://www.reddit.com/r/artificial/comments/1tax3dz/my_god_there_is_an_enormous_crash_just_waiting_to/)**

I had a work version of GPT do a very simple spreadsheet summary task for me yesterday. It took it 5 minutes to do it. I could probably have done it myself in 30 or so minutes. The heavily subsidised token cost of that task? 10 dollars. That's with a 10x subsidy. The actual compute cost was about 100 dollars. There's something seriously wrong there. It's going to crash and crash HARD. EDIT: cause people think i'm lying or are just interested. The spreadsheet had 45 sheets. Each sheet had roughly 500 x 50 populated cells. Formatting was not exactly standard across all sheets. The prompt was something like "there is labelled column in each sheet, give me a simple list of all the items from all the sheets in that column and ignore duplicates." We can chose which model to use. The model I chose was one of the newer ones, I honestly can't remember which one, possibly GPT 5.3. It took 5 minutes or more to so and the stated cost for the task was 10 dollars, possibly even more. I can't recall the token amount. EDIT 2: I just asked web GPT to estimate the cost of the above on a newer version of GPT and it came back with 17 dollars for GPT 4 and above. Try it yourself.

20h ago

---

**[Google detects hackers using AI-generated code to bypass 2FA with zero-day vulnerability](https://www.reddit.com/r/artificial/comments/1tb5quh/google_detects_hackers_using_aigenerated_code_to/)**

AI is quickly becoming a major tool in the world of cybersecurity, and a new report from Google suggests things are getting more serious.

🔗 [PC Guide](https://www.pcguide.com/news/google-detects-hackers-using-ai-generated-code-to-bypass-2fa-with-zero-day-vulnerability/) • 14h ago

---

**[Epistemic Hygiene and How It Can Reduce AI Hallucinations](https://www.reddit.com/r/artificial/comments/1tbq353/epistemic_hygiene_and_how_it_can_reduce_ai/)**

Abstract: The concept of epistemic epistemic hygiene is a methodology that helps humans maintain mental coherence and can help LLMs retain cognitive coherence also. However, the field rarely frames epistemic hygiene explicitly in the context of AI safety and alignment. Much of the AI industry has focused on scaling — bigger models, more compute, more training data, etc. Epistemic hygiene can help reduce hallucinations and drift in AI the same way it helps humans stay coherent and mentally clear. Think about how careful human thinkers operate. A good thinker doesn’t just blurt out the first idea that comes to mind. They pause, check their assumptions, surface potential weaknesses, consider alternative viewpoints, and only commit to a conclusion after it has survived some internal scrutiny. This disciplined mental habit helps humans avoid self-deception, mental drift, and overconfidence. The same principle applies to LLMs. When an LLM generates a response, it is essentially predicting the next token based on patterns in its training data. Without any structured guardrails, that prediction process can easily wander off course as a conversation grows longer. This often means the model gets increasingly vulnerable to hallucinating (among other safety and alignment issues). Epistemic hygiene changes this by giving the model better cognitive habits either through operator discipline or through prompt level scaffolding which is built-in cognitive “habits” that act like guardrails. They don’t make the model “smarter” through more parameters or data. They help the finite system think more clearly and honestly, even when flooded with near-infinite possible directions. A model that knows how to stay anchored, surfaces its own assumptions, and earns its confidence will be a more reliable thinking partner, an outcome that the entirety of the AI field is consistently pushing towards. It is the belief of this author that epistemic hygiene, combined with well structured prompt level scaffolding, will get us to this goal faster.

🔗 [Medium](https://medium.com/@socal21st.oc/epistemic-hygiene-and-how-it-can-reduce-ai-hallucinations-a025646c255d) • 1h ago

---

**[Created a free tool to check what PII your LLM prompts are leaking before they hit the provider](https://www.reddit.com/r/artificial/comments/1tbhvlq/created_a_free_tool_to_check_what_pii_your_llm/)**

Most people don't realize how much personal data ends up in their AI prompts without thinking about it. Customer names, medical details, internal company info. It all goes to the provider's servers. Free to use. Let me know how well this works. aisecuritygateway.ai/ai-leak-checker

7h ago

---

**[I asked both chat gpt and claude to ask me a series of questions to evaluate if i need the](https://www.reddit.com/r/artificial/comments/1tbr449/i_asked_both_chat_gpt_and_claude_to_ask_me_a/)**

paid version of them, or if the free version is fine. Explain why. ChatGPT was free. Money hungry Claude wanted my CC info even though I use Claude a lot less

34m ago

---

**[Palantir to be granted ‘unlimited access’ to NHS patient data](https://www.reddit.com/r/artificial/comments/1tacllr/palantir_to_be_granted_unlimited_access_to_nhs/)**

The NHS is granting staff from companies including Palantir ‘unlimited access’ to identifiable patient data while working on its FDP.

🔗 [Digital Health](https://www.digitalhealth.net/2026/05/palantir-to-be-granted-unlimited-access-to-nhs-patient-data/) • 1d ago

---

**[The AI labs whose models are eroding democratic trust are the same labs now embedding themselves in government.](https://www.reddit.com/r/artificial/comments/1tbf0p9/the_ai_labs_whose_models_are_eroding_democratic/)**

This piece lays out a pretty dark cycle that goes way beyond "fake videos." AI companies are running a feedback loop where their tools destroy public trust in reality, and then they use that collapse to sell AI governance as the "objective" replacement for a broken democracy. Essentially: (OpenAI, Anthropic) make truth impossible to verify. - The exhaustion makes voters give up on human leaders. - The pivot is these same companies signing massive military and government contracts to run the state. The "Singularity" isn't a machine waking up; it’s a tired civilization handing the keys to a black box because we’re too burnt out to govern ourselves. Happy to hear your thoughts : https://aiweekly.co/issues/100-years-from-now-the-last-election Alexis

9h ago

---

**[AI May Reshape Institutions More Than It Replaces Jobs](https://www.reddit.com/r/artificial/comments/1tb1299/ai_may_reshape_institutions_more_than_it_replaces/)**

I think the next big AI debate won’t be about intelligence. It will be about representation. Right now, most AI conversations focus on models: Which model is smarter, or which agent is faster/better or which AI can automate more work? But enterprises/institutions don’t fail because they lack intelligence alone. They fail because they represent reality poorly. A bank may have thousands of dashboards and still not understand customer risk properly. A government may collect massive amounts of data and still fail to represent what citizens are actually experiencing. A company may have advanced AI copilots while teams still operate on fragmented assumptions, outdated workflows, and conflicting versions of reality. That’s why I increasingly think the future architecture of AI systems may depend on three different layers: SENSE How reality is captured and represented. What signals are collected? Which entities matter? How is the state tracked over time/how are things over time? CORE How systems reason, optimize, and make decisions. This is the part most people currently call “AI.” DRIVER How decisions become legitimate action. Who authorized the action? Who is accountable? Can actions be reversed? What happens when the system is wrong? What recourse is available... A lot of current AI systems are becoming extremely strong at CORE while remaining weak in SENSE and DRIVER. Which creates a strange situation: Very intelligent systems… operating on incomplete representations… with unclear legitimacy boundaries. And maybe that’s why many AI pilots look amazing in demos but become messy inside real institutions. Because the challenge is no longer just intelligence. It’s whether institutions can reliably represent reality, reason over it, and act responsibly at scale. That feels less like a software upgrade. And more like a redesign of institutional architecture itself. Curious what others think about this...whether this is a valid point to think/discuss?

17h ago

---

**[The rise of ‘Stacey face’: How AI enhancements are warping our beauty standards](https://www.reddit.com/r/artificial/comments/1ta95lq/the_rise_of_stacey_face_how_ai_enhancements_are/)**

As manosphere trends spread across the internet, a strict vision of the ideal woman is making its way from AI makeover apps to surgeons’ offices. Lydia Spencer-Elliott speaks to experts about ‘Stacey face’, which is seen as the highest tier of female beauty

🔗 [The Independent](https://www.the-independent.com/life-style/stacey-stacy-becky-looksmaxxing-for-women-b2972911.html?utm_source=reddit&utm_medium=social&utm_campaign=artificial) • 1d ago

---

---

## Google News: "ai"

**[Google races to put Gemini at the center of Android before Apple’s AI reboot](https://www.cnbc.com/2026/05/12/google-races-put-gemini-at-center-of-android-before-apples-ai-reboot.html)**

Google is using its latest Android rollout to position Gemini as the AI layer across phones, Chrome, laptops and cars.

CNBC • 11h ago

---

**[Google Says Criminal Hackers Used A.I. to Find a Major Software Flaw](https://www.nytimes.com/2026/05/11/us/politics/google-hackers-attack-ai.html)**

The New York Times • 1d ago

---

**[Introducing Googlebook, designed for Gemini Intelligence](https://blog.google/products-and-platforms/platforms/android/meet-googlebook/)**

We’re introducing Googlebook, a new category of laptops designed for Gemini Intelligence and perfectly in sync with your Android phone.

blog.google • 13h ago

---

**[Shaping the future of AI interaction by reimagining the mouse pointer](https://deepmind.google/blog/ai-pointer/)**

Google DeepMind is transforming the mouse pointer into a context-aware AI partner. Move beyond the friction of traditional prompting with intuitive AI collaboration in Chrome and beyond.

Google DeepMind • 13h ago

---

**[AI coders are carrying half-open laptops through airports, offices, and ice rinks](https://www.msn.com/en-us/news/technology/ai-coders-are-carrying-half-open-laptops-through-airports-offices-and-ice-rinks/ar-AA22YI3k?ocid=BingNewsBrowse)**

MSN • 1h ago

---

**[Duolingo's CEO says AI misses what his best designers nail](https://www.businessinsider.com/duolingo-ceo-luis-von-ahn-ai-cannot-top-designers-creativity-2026-5)**

Duolingo's CEO said AI can't achieve the "level of creativity or the polish" that his top designers can.

Business Insider • 52m ago

---

**[Spain pushes ahead with social media, AI rules despite Big Tech lobbying pressure](https://www.yahoo.com/news/articles/spain-pushes-ahead-social-media-060422656.html)**

Spain will push ahead with new rules to make social networks and AI safer despite intense lobbying from ‌the tech industry, its digital transformation minister Oscar Lopez told Reuters.  "The profit ‌...

Yahoo • 45m ago

---

**[Chelsea flower show garden designers clash over use of AI](https://www.theguardian.com/lifeandstyle/2026/may/13/chelsea-flower-show-garden-designers-clash-over-ai)**

Horticulturalists express alarm after award-winning Matt Keightley launches app that can automate designs

The Guardian • 1h ago

---

**[How AI Killed a 133-Year-Old Princeton Tradition](https://www.theatlantic.com/ideas/2026/05/princeton-ai-honor-code/687144/)**

The school’s famous Honor Code was no match for chatbot-enabled cheating.

The Atlantic • 14h ago

---

**[Nvidia Is Buying the Chip Supply Chain](https://www.wsj.com/tech/nvidia-is-buying-the-chip-supply-chain-871db5e3)**

WSJ • 14h ago

---

---

## HackerNews: "ai"

**[Local AI needs to be the norm](https://news.ycombinator.com/item?id=48085821)**

Local AI models should be the default.

⬆️ 1847 • 💬 736 • 2d ago • [unix.foo](https://unix.foo/posts/local-ai-needs-to-be-norm/)

---

**[If AI writes your code, why use Python?](https://news.ycombinator.com/item?id=48100433)**

For the last decade, fast-to-ship beat fast-to-run. Not anymore.

⬆️ 865 • 💬 921 • 1d ago • [Medium](https://medium.com/@NMitchem/if-ai-writes-your-code-why-use-python-bf8c4ba1a055)

---

**[An AI coding agent, used to write code, needs to reduce your maintenance costs](https://news.ycombinator.com/item?id=48089289)**

⬆️ 368 • 💬 109 • 2d ago • [jamesshore.com](https://www.jamesshore.com/v2/blog/2026/you-need-ai-that-reduces-your-maintenance-costs)

---

**[Maryland citizens hit with $2B power grid upgrade for out-of-state AI](https://news.ycombinator.com/item?id=48088151)**

Aren't AI hyperscalers supposed to pay for these upgrades?

⬆️ 318 • 💬 201 • 2d ago • [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/maryland-citizens-slapped-with-usd2-billion-grid-upgrade-bill-for-out-of-state-ai-data-centers-state-complains-to-federal-energy-regulators-says-additional-cost-breaks-ratepayer-protection-pledge-promises)

---

**[I let AI build a tool to help me figure out what was waking me up at night](https://news.ycombinator.com/item?id=48100662)**

I try to pay attention to the small things that affect my quality of life. When something keeps bothering me, I want to investigate, find a likely cause, and act on it.

What changed recently is what I'm willing to build to support that. With AI tooling, projects I would

⬆️ 262 • 💬 277 • 1d ago • [Martin's Blog](https://martin.sh/i-let-ai-build-a-tool-to-help-me-figure-out-what-was-waking-me-up-at-night/)

---

**[Google says criminal hackers used AI to find a major software flaw](https://news.ycombinator.com/item?id=48094641)**

⬆️ 239 • 💬 172 • 1d ago • [nytimes.com](https://www.nytimes.com/2026/05/11/us/politics/google-hackers-attack-ai.html)

---

**[Amazon employees are "tokenmaxxing" due to pressure to use AI tools](https://news.ycombinator.com/item?id=48110529)**

Workers are using an internal AI tool to automate non-essential tasks.

⬆️ 217 • 💬 225 • 14h ago • [Ars Technica](https://arstechnica.com/ai/2026/05/amazon-employees-are-tokenmaxxing-due-to-pressure-to-use-ai-tools/)

---

**[PS3 Emulator Devs Politely Ask That People Stop Flooding It with AI PRs](https://news.ycombinator.com/item?id=48089263)**

The team behind RPCS3 suggests that vibe-coders "learn how to debug and code" instead of "generating slop that you don't understand"

⬆️ 185 • 💬 145 • 2d ago • [Kotaku](https://kotaku.com/playstation-3-emulator-devs-politely-ask-that-people-stop-flooding-it-with-ai-code-pull-requests-2000694656)

---

**[Reimagining the mouse pointer for the AI era](https://news.ycombinator.com/item?id=48111581)**

Google DeepMind is transforming the mouse pointer into a context-aware AI partner. Move beyond the friction of traditional prompting with intuitive AI collaboration in Chrome and beyond.

⬆️ 181 • 💬 150 • 13h ago • [Google DeepMind](https://deepmind.google/blog/ai-pointer/)

---

**[Students boo commencement speaker after she calls AI next industrial revolution](https://news.ycombinator.com/item?id=48096674)**

A commencement speaker at the University of Central Florida was booed, with graduating humanities students yelling out, "AI SUCKS!"

⬆️ 171 • 💬 209 • 1d ago • [404 Media](https://www.404media.co/ucf-ai-commencement-speaker-booed/)

---

---

## YouTube Videos: "ai"

**[The First AI Cyberattack Has Happened...](https://www.youtube.com/watch?v=6TtKdKQlrqg)**

Hello guys and gals, it's me Mutahar again! This time we take a look at what appears to be a pretty huge day for the Internet.

📺 SomeOrdinaryGamers

👁️ 143K • 👍 7K • 💬 770 • ⏱️ 17:29 • 8h ago

---

**[AI Will Hit a Wall in 2026, if nothing changes.](https://www.youtube.com/watch?v=XA84pSrPHS0)**

Free GenSpark credits if you register here → http://www.genspark.ai/?utm_source=yt&utm_campaign=SabineHossenfelder ...

📺 Sabine Hossenfelder

👁️ 124K • 👍 7K • 💬 1K • ⏱️ 6:42 • 15h ago

---

**[This Is Insane... This Just Ended The Google Stitch VS Claude Design Debate](https://www.youtube.com/watch?v=PJ9CmTODmVo)**

Gemini vs Claude is finally settled with Google Stitch and Claude Design going head to head. Both got massive upgrades, and ...

📺 AI LABS

👁️ 5K • 👍 122 • 💬 13 • ⏱️ 10:46 • 16h ago

---

**[The AI Chat Era Is Over. This Killed It.](https://www.youtube.com/watch?v=FJT5Rh0eKe8)**

Try Genspark with free credits available upon signup:* https://bit.ly/4njiP0c Unlimited AI chat and AI image for all paid users in ...

📺 Julia McCoy

👁️ 27K • 👍 1K • 💬 83 • ⏱️ 12:28 • 2d ago

---

**[Google Chrome Installs AI on Your PC WITHOUT Your Permission.](https://www.youtube.com/watch?v=gYY10vsbnlE)**

Google Chrome apparently installs a 4GB AI agent on your computer without explicit user permission to... something something...

📺 Clownfish TV

👁️ 36K • 👍 3K • 💬 739 • ⏱️ 17:46 • 1d ago

---

**[4 Ways to Make Money With Claude AI That Nobody Is Talking About](https://www.youtube.com/watch?v=wz9CmUZ4jRg)**

Go to https://surfshark.com/joshuamayo or use code JOSHUAMAYO at checkout to get 4 extra months of Surfshark VPN!

📺 Joshua Mayo

👁️ 5K • 👍 282 • 💬 16 • ⏱️ 25:52 • 14h ago

---

**[What happened to Anthropic?](https://www.youtube.com/watch?v=q4rDAu9ggKU)**

Get started with Greptile today https://greptile.com/go/berman 14 Day Free Trial! Download The 25 OpenClaw Use Cases eBook ...

📺 Matthew Berman

👁️ 48K • 👍 1K • 💬 313 • ⏱️ 16:24 • 11h ago

---

**[Trump-Xi summit expected to focus heavily on trade, AI](https://www.youtube.com/watch?v=x7UMmfydB7o)**

President Trump departed the White House for Beijing on Tuesday to attend a summit with Chinese President Xi Jinping.

📺 CBS News

👁️ 12K • 👍 73 • 💬 41 • ⏱️ 5:52 • 9h ago

---

**[Claude Mythos Just Crossed A Dangerous Line... AGAIN!](https://www.youtube.com/watch?v=i-ioLtvb19o)**

Claude Mythos may have just crossed one of the strangest lines in AI. A new METR evaluation reportedly puts Mythos around the ...

📺 AI Revolution

👁️ 42K • 👍 1K • 💬 149 • ⏱️ 15:57 • 1d ago

---

**[AI is Sending People into Psychosis](https://www.youtube.com/watch?v=LxmIIYj5FQE)**

AI chatbots are pulling people into delusions with devastating consequences. Sources: The Dark Addiction Patterns of Current AI ...

📺 Vanessa Wingårdh

👁️ 136K • 👍 8K • 💬 3K • ⏱️ 15:05 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 157,648 • ❤️ 756 • 4d ago

---

**[ZAYA1-8B](https://huggingface.co/Zyphra/ZAYA1-8B)**

*Zyphra*

ZAYA1-8B is an efficient Mixture-of-Experts LLM (760M active params) excelling in mathematical and coding tasks, competitive with larger models. It's suitable for on-device deployment and high-performance inference.

`8.8B`

⬇️ 66,119 • ❤️ 455 • 1d ago

---

**[MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)**

*OpenBMB*

MiniCPM-V 4.6 is an ultra-efficient, pocket-sized multimodal LLM for edge deployment, excelling in image and video understanding with mixed visual token compression. It offers strong multimodal capabilities comparable to larger models while achieving superior computational efficiency and broad mobile platform support.

`image-text-to-text` `1.3B`

⬇️ 0 • ❤️ 422 • 1d ago

---

**[HiDream-O1-Image](https://huggingface.co/HiDream-ai/HiDream-O1-Image)**

*HiDream.ai*

HiDream-O1-Image is a unified transformer-based image generation model capable of text-to-image, image editing, and subject-driven personalization at resolutions up to 2048x2048. It features a pixel-level unified transformer architecture without external VAEs or disjoint text encoders, enabling high-fidelity generation and precise control.

`image-text-to-image` `8.8B`

⬇️ 3,418 • ❤️ 280 • 6h ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 2,017,835 • ❤️ 3,905 • 7d ago

---

**[Z-Anime](https://huggingface.co/SeeSee21/Z-Anime)**

*Sebastian Böhnke*

Z-Anime is a text-to-image diffusion model, fully fine-tuned on the Z-Image Base for generating high-quality, diverse anime-style visuals. It offers multiple variants optimized for speed, quality, and low-resource environments, supporting natural language prompts and full negative prompt capabilities.

`text-to-image` `6.2B`

⬇️ 9,477 • ❤️ 322 • 16d ago

---

**[supertonic-3](https://huggingface.co/Supertone/supertonic-3)**

*Supertone*

Supertonic 3 is a fast, on-device, multilingual text-to-speech model supporting 31 languages with ONNX Runtime for local inference. It offers high accuracy, low latency, and a compact size, suitable for applications requiring efficient, cloud-independent speech synthesis.

`text-to-speech`

⬇️ 1,837 • ❤️ 136 • 6d ago

---

**[gemma-4-31B-it-assistant](https://huggingface.co/google/gemma-4-31B-it-assistant)**

*Google*

Gemma 4 31B Dense is a multimodal LLM from Google DeepMind supporting text and image inputs with a 256K context window. It excels at reasoning, coding, and agentic tasks, offering optimized performance for low-latency applications via speculative decoding.

`any-to-any` `469.5M`

⬇️ 66,561 • ❤️ 222 • 1d ago

---

**[LTX2.3-10Eros](https://huggingface.co/TenStrip/LTX2.3-10Eros)**

*TenStrip*

LTX2.3-10Eros is a video generation model optimized for Image-to-Video (I2V) tasks, utilizing layer-scaled merges for enhanced prompt adherence and visual fidelity. It requires detailed, commanded input for motion, evolution, and audio, making it suitable for users needing precise control over generated video content, especially when combined with prompt enhancement techniques.

`image-to-video`

⬇️ 64,008 • ❤️ 239 • 2d ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 2,446,478 • ❤️ 1,260 • 19d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 64 • 💬 3 • ⭐ 74,474 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://huggingface.co/papers/2512.10971)**

*Tianyu Fan, Yuhao Yang, Yangqin Jiang et al. (6 authors)*

AI-Trader presents the first fully automated live benchmark for evaluating large language models in financial decision-making across multiple markets with autonomous information processing.

▲ 5 • 💬 0 • ⭐ 16,765 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10971) • [💻 code](https://github.com/HKUDS/AI-Trader) • [🔗 project](https://ai4trade.ai/)

---

**[Pixal3D: Pixel-Aligned 3D Generation from Images](https://huggingface.co/papers/2605.10922)**

*Dong-Yang Li, Wang Zhao, Yuxin Chen et al. (8 authors)*

🏢 ARC Lab, Tencent PCG

Pixal3D introduces a pixel-aligned 3D generation approach that addresses fidelity issues in 3D asset creation by establishing direct pixel-to-3D correspondences through back-projection conditioning.

▲ 19 • 💬 3 • ⭐ 263 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2605.10922) • [💻 code](https://github.com/TencentARC/Pixal3D) • [🔗 project](https://ldyang694.github.io/projects/pixal3d/)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 19 • 💬 3 • ⭐ 11,083 • 25d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[DFlash: Block Diffusion for Flash Speculative Decoding](https://huggingface.co/papers/2602.06036)**

*Jian Chen, Yesheng Liang, Zhijian Liu*

🏢 Z Lab

DFlash is a speculative decoding framework that uses a lightweight block diffusion model for parallel token drafting, achieving significant speedup over existing autoregressive methods while maintaining high-quality outputs.

▲ 79 • 💬 7 • ⭐ 4,483 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.06036) • [💻 code](https://github.com/z-lab/dflash) • [🔗 project](https://z-lab.ai/projects/dflash/)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 108 • 💬 10 • ⭐ 9,002 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 32 • 💬 3 • ⭐ 24,053 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 161 • 💬 2 • ⭐ 62,777 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 54 • 💬 1 • ⭐ 79,826 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[Flow-OPD: On-Policy Distillation for Flow Matching Models](https://huggingface.co/papers/2605.08063)**

*Zhen Fang, Wenxuan Huang, Yu Zeng et al. (11 authors)*

Flow-OPD addresses limitations in Flow Matching text-to-image models through a two-stage alignment approach combining on-policy distillation and manifold anchor regularization, achieving significant improvements in generation quality and alignment metrics.

▲ 83 • 💬 2 • ⭐ 108 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2605.08063) • [💻 code](https://github.com/CostaliyA/Flow-OPD) • [🔗 project](https://costaliya.github.io/Flow-OPD/)

---

---

## GitHub Repositories: "ai"

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 12.5k • 🔱 2.9k • 15d ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 2.9k • 🔱 842 • 12h ago

---

**[crynta/terax-ai](https://github.com/crynta/terax-ai)**

Lightweight (7MB) AI terminal emulator (ADE) built in Rust & Tauri & React

`TypeScript` `agents` `ai` `code-editor` `linux` `macos`

⭐ 2.6k • 🔱 267 • 6h ago

---

**[Manavarya09/design-extract](https://github.com/Manavarya09/design-extract)**

Extract any website's complete design system with one command. DTCG tokens, semantic+primitive+composite, MCP server for Claude Code/Cursor/Windsurf, multi-platform emitters (iOS SwiftUI, Android Compose, Flutter, WordPress), Tailwind v4, Figma variables, shadcn/ui, CSS health audit, WCAG remediation, Chrome extension. MIT, Playwright, Node 20+.

`JavaScript` `accessibility` `agent-skill` `ai` `chrome-extension` `claude-code-plugin`

⭐ 2.5k • 🔱 231 • 17h ago

---

**[earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad)**

A collection of agent skills for CAD, robotics and hardware design

`JavaScript` `3mf` `agents` `ai` `ai-agents` `build123d`

⭐ 2.5k • 🔱 287 • 3m ago

---

**[cosmicstack-labs/mercury-agent](https://github.com/cosmicstack-labs/mercury-agent)**

Soul-driven AI agent with permission-hardened tools, token budgets, and multi-channel access. Runs 24/7 from CLI or Telegram.

`TypeScript` `ai-agent` `ai-assistant` `llm`

⭐ 2.1k • 🔱 220 • 2d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.1k • 🔱 135 • 2h ago

---

**[bergside/design-md-chrome](https://github.com/bergside/design-md-chrome)**

Chrome extension to extract styles from any website and generate DESIGN.md files and design skills for AI based on TypeUI

`JavaScript` `ai` `chrome` `chrome-extension` `claude` `claude-design`

⭐ 1.9k • 🔱 242 • 18d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 1.9k • 🔱 290 • 5d ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D cell generation and exploration studio.

`JavaScript`

⭐ 1.7k • 🔱 298 • 3h ago

---

---

*Generated by PeekDeck - A glance is all you need*
