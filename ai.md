---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-13T03:32:00.744909+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- social
- repositories
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 13, 2026 at 03:32 UTC  
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

8h ago

---

**[My god there is an enormous crash just waiting to happen](https://www.reddit.com/r/artificial/comments/1tax3dz/my_god_there_is_an_enormous_crash_just_waiting_to/)**

I had a work version of GPT do a very simple spreadsheet summary task for me yesterday. It took it 5 minutes to do it. I could probably have done it myself in 30 or so minutes. The heavily subsidised token cost of that task? 10 dollars. That's with a 10x subsidy. The actual compute cost was about 100 dollars. There's something seriously wrong there. It's going to crash and crash HARD. EDIT: cause people think i'm lying or are just interested. The spreadsheet had 45 sheets. Each sheet had roughly 500 x 50 populated cells. Formatting was not exactly standard across all sheets. The prompt was something like "there is labelled column in each sheet, give me a simple list of all the items from all the sheets in that column and ignore duplicates." We can chose which model to use. The model I chose was one of the newer ones, I honestly can't remember which one, possibly GPT 5.3. It took 5 minutes or more to so and the stated cost for the task was 10 dollars, possibly even more. I can't recall the token amount. EDIT 2: I just asked web GPT to estimate the cost of the above on a newer version of GPT and it came back with 17 dollars for GPT 4 and above. Try it yourself.

17h ago

---

**[Google detects hackers using AI-generated code to bypass 2FA with zero-day vulnerability](https://www.reddit.com/r/artificial/comments/1tb5quh/google_detects_hackers_using_aigenerated_code_to/)**

AI is quickly becoming a major tool in the world of cybersecurity, and a new report from Google suggests things are getting more serious.

🔗 [PC Guide](https://www.pcguide.com/news/google-detects-hackers-using-ai-generated-code-to-bypass-2fa-with-zero-day-vulnerability/) • 11h ago

---

**[Created a free tool to check what PII your LLM prompts are leaking before they hit the provider](https://www.reddit.com/r/artificial/comments/1tbhvlq/created_a_free_tool_to_check_what_pii_your_llm/)**

Most people don't realize how much personal data ends up in their AI prompts without thinking about it. Customer names, medical details, internal company info. It all goes to the provider's servers. Free to use. Let me know how well this works. aisecuritygateway.ai/ai-leak-checker

4h ago

---

**[Palantir to be granted ‘unlimited access’ to NHS patient data](https://www.reddit.com/r/artificial/comments/1tacllr/palantir_to_be_granted_unlimited_access_to_nhs/)**

The NHS is granting staff from companies including Palantir ‘unlimited access’ to identifiable patient data while working on its FDP.

🔗 [Digital Health](https://www.digitalhealth.net/2026/05/palantir-to-be-granted-unlimited-access-to-nhs-patient-data/) • 1d ago

---

**[AI May Reshape Institutions More Than It Replaces Jobs](https://www.reddit.com/r/artificial/comments/1tb1299/ai_may_reshape_institutions_more_than_it_replaces/)**

I think the next big AI debate won’t be about intelligence. It will be about representation. Right now, most AI conversations focus on models: Which model is smarter, or which agent is faster/better or which AI can automate more work? But enterprises/institutions don’t fail because they lack intelligence alone. They fail because they represent reality poorly. A bank may have thousands of dashboards and still not understand customer risk properly. A government may collect massive amounts of data and still fail to represent what citizens are actually experiencing. A company may have advanced AI copilots while teams still operate on fragmented assumptions, outdated workflows, and conflicting versions of reality. That’s why I increasingly think the future architecture of AI systems may depend on three different layers: SENSE How reality is captured and represented. What signals are collected? Which entities matter? How is the state tracked over time/how are things over time? CORE How systems reason, optimize, and make decisions. This is the part most people currently call “AI.” DRIVER How decisions become legitimate action. Who authorized the action? Who is accountable? Can actions be reversed? What happens when the system is wrong? What recourse is available... A lot of current AI systems are becoming extremely strong at CORE while remaining weak in SENSE and DRIVER. Which creates a strange situation: Very intelligent systems… operating on incomplete representations… with unclear legitimacy boundaries. And maybe that’s why many AI pilots look amazing in demos but become messy inside real institutions. Because the challenge is no longer just intelligence. It’s whether institutions can reliably represent reality, reason over it, and act responsibly at scale. That feels less like a software upgrade. And more like a redesign of institutional architecture itself. Curious what others think about this...whether this is a valid point to think/discuss?

14h ago

---

**[The AI labs whose models are eroding democratic trust are the same labs now embedding themselves in government.](https://www.reddit.com/r/artificial/comments/1tbf0p9/the_ai_labs_whose_models_are_eroding_democratic/)**

This piece lays out a pretty dark cycle that goes way beyond "fake videos." AI companies are running a feedback loop where their tools destroy public trust in reality, and then they use that collapse to sell AI governance as the "objective" replacement for a broken democracy. Essentially: (OpenAI, Anthropic) make truth impossible to verify. - The exhaustion makes voters give up on human leaders. - The pivot is these same companies signing massive military and government contracts to run the state. The "Singularity" isn't a machine waking up; it’s a tired civilization handing the keys to a black box because we’re too burnt out to govern ourselves. Happy to hear your thoughts : https://aiweekly.co/issues/100-years-from-now-the-last-election Alexis

6h ago

---

**[The rise of ‘Stacey face’: How AI enhancements are warping our beauty standards](https://www.reddit.com/r/artificial/comments/1ta95lq/the_rise_of_stacey_face_how_ai_enhancements_are/)**

As manosphere trends spread across the internet, a strict vision of the ideal woman is making its way from AI makeover apps to surgeons’ offices. Lydia Spencer-Elliott speaks to experts about ‘Stacey face’, which is seen as the highest tier of female beauty

🔗 [The Independent](https://www.the-independent.com/life-style/stacey-stacy-becky-looksmaxxing-for-women-b2972911.html?utm_source=reddit&utm_medium=social&utm_campaign=artificial) • 1d ago

---

**[Will AI turn us all into hipsters and artisans?](https://www.reddit.com/r/artificial/comments/1tbgt7k/will_ai_turn_us_all_into_hipsters_and_artisans/)**

🔗 [archive.md](https://archive.md/TGEXd) • 5h ago

---

**[China Sought Access to Anthropic’s Newest A.I. The Answer Was No.](https://www.reddit.com/r/artificial/comments/1tb3kzh/china_sought_access_to_anthropics_newest_ai_the/)**

🔗 [nytimes.com](https://www.nytimes.com/2026/05/12/us/politics/china-ai-anthropic-openai-mythos-chatgpt.html) • 12h ago

---

---

## Google News: "ai"

**[How AI Killed a 133-Year-Old Princeton Tradition](https://www.theatlantic.com/ideas/2026/05/princeton-ai-honor-code/687144/)**

The school’s famous Honor Code was no match for chatbot-enabled cheating.

The Atlantic • 11h ago

---

**[Laid-off GM employees tell of ominous email, severance and role of AI](https://www.cnbc.com/2026/05/12/gm-layoffs-ai-severance.html)**

General Motors employees who were laid off Monday described their job terminations to CNBC.

CNBC • 9h ago

---

**[AI Rivalry Overshadows Push For Guardrails At Xi-Trump Talks: Experts](https://www.barrons.com/articles/ai-rivalry-overshadows-push-for-guardrails-at-xi-trump-talks-experts-740f1dc9)**

Barron's • 9m ago

---

**[Asian Shares Trade Mixed as AI Excitement Fades and War Worries Continue](https://www.usnews.com/news/business/articles/2026-05-12/asian-shares-trade-mixed-as-ai-excitement-fades-and-war-worries-continue)**

Asian shares are trading mixed, as the enthusiasm over AI and other technology stocks gradually faded, braking Wall Street’s record-setting run

U.S. News & World Report • 43m ago

---

**[Asian Stocks Fall On US-Iran Impasse, AI Setbacks](https://www.barrons.com/articles/asian-stocks-fall-on-us-iran-impasse-ai-setbacks-16d0c959)**

Barron's • 16m ago

---

**[Florida students boo graduation speaker who called AI ‘next Industrial Revolution’](https://www.theguardian.com/technology/2026/may/12/florida-students-boo-graduation-speaker-ai)**

Real estate executive got an unexpected earful when she spoke of ‘living in a time of profound change’

The Guardian • 6h ago

---

**[Opinion | The Shared Feeling of Being Harvested by the Future](https://www.nytimes.com/2026/05/12/opinion/us-china-ai-future.html)**

The New York Times • 18h ago

---

**[Nvidia Is Buying the Chip Supply Chain](https://www.wsj.com/tech/nvidia-is-buying-the-chip-supply-chain-871db5e3)**

WSJ • 11h ago

---

**[Shaping the future of AI interaction by reimagining the mouse pointer](https://deepmind.google/blog/ai-pointer/)**

Google DeepMind is transforming the mouse pointer into a context-aware AI partner. Move beyond the friction of traditional prompting with intuitive AI collaboration in Chrome and beyond.

Google DeepMind • 10h ago

---

**[AI robot changes your tires and balances them too](https://www.foxnews.com/tech/ai-robot-changes-tires-balances)**

Boston-based Automated Tire, Inc. unveils SmartBay, an AI-powered robotic platform that handles tire changes and wheel balancing with minimal human help.

Fox News • 10h ago

---

---

## HackerNews: "ai"

**[Local AI needs to be the norm](https://news.ycombinator.com/item?id=48085821)**

Local AI models should be the default.

⬆️ 1844 • 💬 735 • 2d ago • [unix.foo](https://unix.foo/posts/local-ai-needs-to-be-norm/)

---

**[If AI writes your code, why use Python?](https://news.ycombinator.com/item?id=48100433)**

For the last decade, fast-to-ship beat fast-to-run. Not anymore.

⬆️ 854 • 💬 917 • 1d ago • [Medium](https://medium.com/@NMitchem/if-ai-writes-your-code-why-use-python-bf8c4ba1a055)

---

**[An AI coding agent, used to write code, needs to reduce your maintenance costs](https://news.ycombinator.com/item?id=48089289)**

⬆️ 366 • 💬 108 • 2d ago • [jamesshore.com](https://www.jamesshore.com/v2/blog/2026/you-need-ai-that-reduces-your-maintenance-costs)

---

**[Maryland citizens hit with $2B power grid upgrade for out-of-state AI](https://news.ycombinator.com/item?id=48088151)**

Aren't AI hyperscalers supposed to pay for these upgrades?

⬆️ 318 • 💬 201 • 2d ago • [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/maryland-citizens-slapped-with-usd2-billion-grid-upgrade-bill-for-out-of-state-ai-data-centers-state-complains-to-federal-energy-regulators-says-additional-cost-breaks-ratepayer-protection-pledge-promises)

---

**[I let AI build a tool to help me figure out what was waking me up at night](https://news.ycombinator.com/item?id=48100662)**

I try to pay attention to the small things that affect my quality of life. When something keeps bothering me, I want to investigate, find a likely cause, and act on it.

What changed recently is what I'm willing to build to support that. With AI tooling, projects I would

⬆️ 262 • 💬 276 • 1d ago • [Martin's Blog](https://martin.sh/i-let-ai-build-a-tool-to-help-me-figure-out-what-was-waking-me-up-at-night/)

---

**[Task Paralysis and AI](https://news.ycombinator.com/item?id=48081469)**

An article about ADHD, Task Paralysis and AI.

⬆️ 256 • 💬 129 • 2d ago • [g5t.de](https://g5t.de/articles/20260510-task-paralysis-and-ai/index.html)

---

**[Google says criminal hackers used AI to find a major software flaw](https://news.ycombinator.com/item?id=48094641)**

⬆️ 237 • 💬 172 • 1d ago • [nytimes.com](https://www.nytimes.com/2026/05/11/us/politics/google-hackers-attack-ai.html)

---

**[Amazon employees are "tokenmaxxing" due to pressure to use AI tools](https://news.ycombinator.com/item?id=48110529)**

Workers are using an internal AI tool to automate non-essential tasks.

⬆️ 212 • 💬 219 • 11h ago • [Ars Technica](https://arstechnica.com/ai/2026/05/amazon-employees-are-tokenmaxxing-due-to-pressure-to-use-ai-tools/)

---

**[PS3 Emulator Devs Politely Ask That People Stop Flooding It with AI PRs](https://news.ycombinator.com/item?id=48089263)**

The team behind RPCS3 suggests that vibe-coders "learn how to debug and code" instead of "generating slop that you don't understand"

⬆️ 185 • 💬 144 • 2d ago • [Kotaku](https://kotaku.com/playstation-3-emulator-devs-politely-ask-that-people-stop-flooding-it-with-ai-code-pull-requests-2000694656)

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

👁️ 102K • 👍 5K • 💬 638 • ⏱️ 17:29 • 5h ago

---

**[AI Will Hit a Wall in 2026, if nothing changes.](https://www.youtube.com/watch?v=XA84pSrPHS0)**

Free GenSpark credits if you register here → http://www.genspark.ai/?utm_source=yt&utm_campaign=SabineHossenfelder ...

📺 Sabine Hossenfelder

👁️ 111K • 👍 6K • 💬 1K • ⏱️ 6:42 • 12h ago

---

**[WTF is going on at Anthropic?!](https://www.youtube.com/watch?v=q4rDAu9ggKU)**

Get started with Greptile today https://greptile.com/go/berman 14 Day Free Trial! Download The 25 OpenClaw Use Cases eBook ...

📺 Matthew Berman

👁️ 40K • 👍 1K • 💬 293 • ⏱️ 16:53 • 8h ago

---

**[This Is Insane... This Just Ended The Google Stitch VS Claude Design Debate](https://www.youtube.com/watch?v=PJ9CmTODmVo)**

Gemini vs Claude is finally settled with Google Stitch and Claude Design going head to head. Both got massive upgrades, and ...

📺 AI LABS

👁️ 5K • 👍 118 • 💬 13 • ⏱️ 10:46 • 13h ago

---

**[AI is Creating a Beauty Class and a Servant Class ](https://www.youtube.com/watch?v=AGWTuK3I9dE)**

📺 Pearl

👁️ 8K • 👍 557 • 💬 106 • ⏱️ 7:01 • 1d ago

---

**[4 Ways to Make Money With Claude AI That Nobody Is Talking About](https://www.youtube.com/watch?v=wz9CmUZ4jRg)**

Go to https://surfshark.com/joshuamayo or use code JOSHUAMAYO at checkout to get 4 extra months of Surfshark VPN!

📺 Joshua Mayo

👁️ 4K • 👍 236 • 💬 15 • ⏱️ 25:52 • 11h ago

---

**[GPT Image 2.0 + Seedance 2.0 = INSANE AI Motion Graphics](https://www.youtube.com/watch?v=NrV6g3iv2lk)**

GPT Image 2 together with Seedance is extremely powerful, if you use it right Try out GPT Image 2 & Seedance: ...

📺 Mira AI

👁️ 4K • ⏱️ 9:33 • 6h ago

---

**[Build a Self-Running AI Company in 16 Minutes (Move 75% Faster)](https://www.youtube.com/watch?v=Baa71rPgxvA)**

Higgsfield MCP gives Claude hands — your agent can now generate videos, ads, photos, landing pages and dashboards directly ...

📺 Silicon Valley Girl

👁️ 11K • 👍 558 • 💬 61 • ⏱️ 16:01 • 14h ago

---

**[The AI Chat Era Is Over. This Killed It.](https://www.youtube.com/watch?v=FJT5Rh0eKe8)**

Try Genspark with free credits available upon signup:* https://bit.ly/4njiP0c Unlimited AI chat and AI image for all paid users in ...

📺 Julia McCoy

👁️ 26K • 👍 1K • 💬 82 • ⏱️ 12:28 • 2d ago

---

**[Claude Mythos Just Crossed A Dangerous Line... AGAIN!](https://www.youtube.com/watch?v=i-ioLtvb19o)**

Claude Mythos may have just crossed one of the strangest lines in AI. A new METR evaluation reportedly puts Mythos around the ...

📺 AI Revolution

👁️ 41K • 👍 1K • 💬 148 • ⏱️ 15:57 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 157,648 • ❤️ 738 • 4d ago

---

**[ZAYA1-8B](https://huggingface.co/Zyphra/ZAYA1-8B)**

*Zyphra*

ZAYA1-8B is an efficient Mixture-of-Experts LLM (760M active params) excelling in mathematical and coding tasks, competitive with larger models. It's suitable for on-device deployment and high-performance inference.

`8.8B`

⬇️ 66,119 • ❤️ 452 • 1d ago

---

**[MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)**

*OpenBMB*

MiniCPM-V 4.6 is an ultra-efficient, pocket-sized multimodal LLM for edge deployment, excelling in image and video understanding with mixed visual token compression. It offers strong multimodal capabilities comparable to larger models while achieving superior computational efficiency and broad mobile platform support.

`image-text-to-text` `1.3B`

⬇️ 0 • ❤️ 396 • 20h ago

---

**[HiDream-O1-Image](https://huggingface.co/HiDream-ai/HiDream-O1-Image)**

*HiDream.ai*

HiDream-O1-Image is a unified transformer-based image generation model capable of text-to-image, image editing, and subject-driven personalization at resolutions up to 2048x2048. It features a pixel-level unified transformer architecture without external VAEs or disjoint text encoders, enabling high-fidelity generation and precise control.

`image-text-to-image` `8.8B`

⬇️ 3,418 • ❤️ 275 • 3h ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 2,017,835 • ❤️ 3,900 • 6d ago

---

**[Z-Anime](https://huggingface.co/SeeSee21/Z-Anime)**

*Sebastian Böhnke*

Z-Anime is a text-to-image diffusion model, fully fine-tuned on the Z-Image Base for generating high-quality, diverse anime-style visuals. It offers multiple variants optimized for speed, quality, and low-resource environments, supporting natural language prompts and full negative prompt capabilities.

`text-to-image` `6.2B`

⬇️ 9,477 • ❤️ 320 • 16d ago

---

**[gemma-4-31B-it-assistant](https://huggingface.co/google/gemma-4-31B-it-assistant)**

*Google*

Gemma 4 31B Dense is a multimodal LLM from Google DeepMind supporting text and image inputs with a 256K context window. It excels at reasoning, coding, and agentic tasks, offering optimized performance for low-latency applications via speculative decoding.

`any-to-any` `469.5M`

⬇️ 66,561 • ❤️ 218 • 1d ago

---

**[LTX2.3-10Eros](https://huggingface.co/TenStrip/LTX2.3-10Eros)**

*TenStrip*

LTX2.3-10Eros is a video generation model optimized for Image-to-Video (I2V) tasks, utilizing layer-scaled merges for enhanced prompt adherence and visual fidelity. It requires detailed, commanded input for motion, evolution, and audio, making it suitable for users needing precise control over generated video content, especially when combined with prompt enhancement techniques.

`image-to-video`

⬇️ 64,008 • ❤️ 237 • 2d ago

---

**[supertonic-3](https://huggingface.co/Supertone/supertonic-3)**

*Supertone*

Supertonic 3 is a fast, on-device, multilingual text-to-speech model supporting 31 languages with ONNX Runtime for local inference. It offers high accuracy, low latency, and a compact size, suitable for applications requiring efficient, cloud-independent speech synthesis.

`text-to-speech`

⬇️ 1,837 • ❤️ 129 • 6d ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 2,446,478 • ❤️ 1,258 • 19d ago

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

▲ 5 • 💬 0 • ⭐ 16,439 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10971) • [💻 code](https://github.com/HKUDS/AI-Trader) • [🔗 project](https://ai4trade.ai/)

---

**[Pixal3D: Pixel-Aligned 3D Generation from Images](https://huggingface.co/papers/2605.10922)**

*Dong-Yang Li, Wang Zhao, Yuxin Chen et al. (8 authors)*

🏢 ARC Lab, Tencent PCG

Pixal3D introduces a pixel-aligned 3D generation approach that addresses fidelity issues in 3D asset creation by establishing direct pixel-to-3D correspondences through back-projection conditioning.

▲ 17 • 💬 3 • ⭐ 263 • 2d ago

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

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 54 • 💬 1 • ⭐ 79,795 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 161 • 💬 2 • ⭐ 62,777 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Adam's Law: Textual Frequency Law on Large Language Models](https://huggingface.co/papers/2604.02176)**

*Hongyuan Adam Lu, Z. L., Victor Wei et al. (8 authors)*

🏢 FaceMind

A novel framework for improving large language model performance through textual frequency analysis, including laws, distillation, and curriculum training approaches.

▲ 501 • 💬 9 • ⭐ 1,309 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.02176) • [💻 code](https://github.com/HongyuanLuke/frequencylaw)

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

⭐ 2.9k • 🔱 836 • 8h ago

---

**[crynta/terax-ai](https://github.com/crynta/terax-ai)**

Lightweight (7MB) AI terminal emulator (ADE) built in Rust & Tauri & React

`TypeScript` `agents` `ai` `code-editor` `linux` `macos`

⭐ 2.6k • 🔱 262 • 2h ago

---

**[Manavarya09/design-extract](https://github.com/Manavarya09/design-extract)**

Extract any website's complete design system with one command. DTCG tokens, semantic+primitive+composite, MCP server for Claude Code/Cursor/Windsurf, multi-platform emitters (iOS SwiftUI, Android Compose, Flutter, WordPress), Tailwind v4, Figma variables, shadcn/ui, CSS health audit, WCAG remediation, Chrome extension. MIT, Playwright, Node 20+.

`JavaScript` `accessibility` `agent-skill` `ai` `chrome-extension` `claude-code-plugin`

⭐ 2.5k • 🔱 230 • 14h ago

---

**[earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad)**

Open source CAD skills and harnesses for generating 3D models with your favorite coding agent

`JavaScript` `3mf` `agents` `ai` `ai-agents` `build123d`

⭐ 2.5k • 🔱 286 • 1d ago

---

**[cosmicstack-labs/mercury-agent](https://github.com/cosmicstack-labs/mercury-agent)**

Soul-driven AI agent with permission-hardened tools, token budgets, and multi-channel access. Runs 24/7 from CLI or Telegram.

`TypeScript` `ai-agent` `ai-assistant` `llm`

⭐ 2.1k • 🔱 220 • 2d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.1k • 🔱 134 • 42s ago

---

**[bergside/design-md-chrome](https://github.com/bergside/design-md-chrome)**

Chrome extension to extract styles from any website and generate DESIGN.md files and design skills for AI based on TypeUI

`JavaScript` `ai` `chrome` `chrome-extension` `claude` `claude-design`

⭐ 1.9k • 🔱 242 • 18d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 1.9k • 🔱 287 • 5d ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D cell generation and exploration studio.

`JavaScript`

⭐ 1.7k • 🔱 297 • 2h ago

---

---

*Generated by PeekDeck - A glance is all you need*
