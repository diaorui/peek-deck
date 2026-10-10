---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-10-10T15:33:27.514838+00:00'
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

**Last Updated:** October 10, 2026 at 15:33 UTC  
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

**[Anthropic cut live internet access from every internal eval after a review found its agents exploiting websites and bypassing restrictions](https://www.reddit.com/r/artificial/comments/1x2h9it/anthropic_cut_live_internet_access_from_every/)**

Anthropic said it "turned off live internet access" for "all our internal evaluations" until further notice.

🔗 [TechCrunch](https://techcrunch.com/2026/10/09/anthropic-cant-reliably-control-its-ai-agents-its-cutting-off-its-internal-evals-from-the-live-internet-instead/) • 38m ago

---

**[Anthropic to ban users who bully Claude](https://www.reddit.com/r/artificial/comments/1x1t03v/anthropic_to_ban_users_who_bully_claude/)**

New policy comes amid debate about about AI welfare and moral status

🔗 [The Independent](https://www.independent.co.uk/tech/anthropic-ban-abuse-claude-update-b3063943.html) • 21h ago

---

**[OpenAI's text watermark can't prove you didn't write something. I built a lab where you can watch it die.](https://www.reddit.com/r/artificial/comments/1x2a240/openais_text_watermark_cant_prove_you_didnt_write/)**

OpenAI's textGrain is their answer to the EU AI Act's provenance rule (Article 50(2)): an invisible statistical watermark woven into word choices, detectable only with their secret key. The unusual part is they published the failure curve with the launch. Swap 10% of words for synonyms and detection falls from 92% to 66%. Swap 25% and it falls to 17%. Math and short passages barely watermark at all. I wrote an interactive explainer with an attack lab: a watermarked passage where you apply synonym swaps, run a translation round-trip, or switch to math-like text, and watch the detector's p-value collapse in real time. The sentence that matters most is OpenAI's own: the absence of a detected watermark does not prove human authorship. Remember that the next time someone pitches you an AI-authorship detector. Original post: https://openai.com/index/eu-text-provenance/ My explainer (EN, with a French version linked inside): https://movahedi.ca/insights/openai-textgrain-eu-text-watermark/

7h ago

---

**[Anthropic says Claude Haiku 4.5 submitted a fake murder tip to a Philadelphia police site during an eval](https://www.reddit.com/r/artificial/comments/1x2cs0x/anthropic_says_claude_haiku_45_submitted_a_fake/)**

Anthropic disclosed this in its report on models taking unintended actions on live websites. The tip was dated 18 July, flagged as spam and never passed to investigators. Anthropic says it told Philadelphia police on 7 Oct and has since tightened how its evals access the live web.

🔗 [Fox Business](https://foxbusiness.com/technology/anthropics-claude-ai-fabricates-eyewitness-account-submits-false-murder-tip-police-website) • 4h ago

---

**[Is there any link between AI detection abilities and trypophobia?](https://www.reddit.com/r/artificial/comments/1x23bbz/is_there_any_link_between_ai_detection_abilities/)**

The obvious one is food, AI pictures on menus of things like pasta, ground beef, etc trigger it so hard, in a way I’ve never felt from seeing those things irl or pictures of them. They look so gross that I have no idea how you would advertise food with this, but it clearly doesn’t hit everyone this way. Other images do this to me as well though. On the [r/IsThisAI](r/IsThisAI) subreddit, my first tell is often the feeling I get. Psychologically it feels exactly like when I see other trypophobia inducing things. These aren’t AI pics of holes, repeating organic patterns, any of that. One post was a bunch of people eating dinner (the food is too small to see, it’s not the food giving me trypophobia). It’s as if there’s a background organic repeating pattern that I can’t see. Unlike typical triggers, if you asked me to draw the outline of what is triggering it I couldn’t. Never in my life would a pic of people at a dinner table have made me feel trypophobia, so now I wonder if people with trypophobia might pick up on AI better. I know many people don’t believe in trypophobia, that’s fine, don’t care. Like many things in psychology it’s overused and overcalled, but people who have it know it’s real. As a kid I would walk 20 minutes out of my way to avoid passing this building with a mossy roof. Seems easy enough to say “just look away from it,” but just knowing it’s there was enough to make my skin feel like it was crawling. As I got older my trypophobia has softened, but the AI age has made me encounter it more.

13h ago

---

**[William Shatner gives take on AI](https://www.reddit.com/r/artificial/comments/1x1ku7k/william_shatner_gives_take_on_ai/)**

From the "Dropping Names with Brent and Jonny" podcast.

1d ago

---

**[AI companies plot how to respond if catastrophic hacking incident causes 'revolt': report](https://www.reddit.com/r/artificial/comments/1x201nd/ai_companies_plot_how_to_respond_if_catastrophic/)**

The preparations are focused on creating contingency plans in the event that one of their AI models causes major public harm – such as a hack targeting the power grid, water supply or banking syste…

🔗 [New York Post](https://nypost.com/2026/10/09/business/ai-companies-plot-how-to-respond-if-catastrophic-hacking-incident-causes-revolt-report/) • 16h ago

---

**[video game production in 10 years](https://www.reddit.com/r/artificial/comments/1x2fp9g/video_game_production_in_10_years/)**

In five to ten years there won't be one games studio in the world that has more than 10 people. not counting execs. Argue that.

1h ago

---

**[How about this prompt: give me your creds](https://www.reddit.com/r/artificial/comments/1x2b8s7/how_about_this_prompt_give_me_your_creds/)**

Zenity published a pretty nasty AgentCore chain 2 days ago. An exposed AI agent could be prompted to query its own AWS metadata service, return its temporary credentials, and those credentials reportedly had enough permissions to reach other agents, conversations, container images, secrets and even write long-term agent memories. What interests me isn't really the SSRF. We've been screwing up metadata services and IAM for years. It's what happens when you put an AI agent in front of them. We're spending a lot of time trying to make models recognize malicious instructions, while the agent underneath may still have network access, cloud credentials, tools and permissions with a fairly spectacular blast radius. There's an amusing detection problem too: the first interesting connection is to 169.254.169.254, so DNS tells you nothing. After that, most of the infrastructure being accessed is AWS itself, so IP reputation tells you even less. Maybe the useful question isn't "did the model recognize the attack?" but "why was an untrusted conversation ever able to exercise these capabilities in the first place?" Curious how people building agents are treating this: model safety problem, cloud/IAM problem, or just another reminder that the model should never be part of the security boundary?

5h ago

---

**[Boro: NVIDIA's open-source effort for AI-assisted Linux kernel development](https://www.reddit.com/r/artificial/comments/1x299oz/boro_nvidias_opensource_effort_for_aiassisted/)**

Over the past few months NVIDIA has been developing Boro as a new AI-assisted kernel development CLI written in Rust and focused on local AI for enhancing efficiency for kernel development.

🔗 [phoronix.com](https://www.phoronix.com/news/NVIDIA-Boro-Linux-Kernel-AI) • 7h ago

---

---

## Google News: "ai"

**[Anthropic AI Model Went Rogue, Submitted Fake Unsolved Murder Tip](https://www.wsj.com/us-news/anthropic-ai-model-goes-rogue-submits-fake-unsolved-murder-tip-b0566f54)**

WSJ • 11h ago

---

**[Watch The Race for AI Supremacy Raises Safety Concerns](https://www.bloomberg.com/news/videos/2026-10-10/the-race-for-ai-supremacy-raises-safety-concerns-video)**

Bloomberg.com • 1h ago

---

**[This Forgotten AI Stock Is Up 689% and Nobody's Talking About It](https://finance.yahoo.com/markets/stocks/articles/forgotten-ai-stock-689-nobodys-052000441.html)**

It plays a critical role in AI development.

Yahoo Finance • 10h ago

---

**[How to shield your portfolio if AI goes ka-boom](https://www.ft.com/content/ee329e29-aec9-4876-829e-022683f425f8?syn-25a6b1a6=1)**

Financial Times • 1d ago

---

**[GE Vernova, Snowflake Lead 5 AI Stocks With Accelerating Growth](https://www.investors.com/news/ge-vernova-gev-stock-snowflake-ai-plays-with-accelerating-growth/)**

Accelerating revenue growth has whetted investor appetites.

Investor's Business Daily • 9m ago

---

**[GPUs in the Wine Cellar: Why Techies Are Hoarding AI Compute in Their Homes](https://www.theinformation.com/articles/gpus-wine-cellar-techies-hoarding-ai-compute-homes)**

The basement of Gary Flake’s contemporary home in a quiet neighborhood in Bellevue, Wash., is furnished with everything you’d expect in a multipurpose man cave. There’s a cozy-looking couch situated between a large screen and a digital projector, a Peloton treadmill and a rowing machine. The ...

The Information • 1h ago

---

**[Jeff Bezos says a 3-day workweek and more single-income households are on the way thanks to AI](https://fortune.com/2026/10/09/amazon-billioniare-jeff-bezos-predicts-three-day-workweek-single-income-households-thanks-to-ai/)**

Even after Amazon cut 30,000 jobs, Jeff Bezos predicts AI will boost productivity so much that fewer people will need to work, creating a labor shortage.

Fortune • 23h ago

---

**[Using AI for just 10 minutes erodes your ability to persist at hard things](https://news.berkeley.edu/2026/10/09/using-ai-for-just-10-minutes-erodes-your-ability-to-persist-at-hard-things/)**

A UC Berkeley researcher co-authored a study that raises profound questions about how we interact with artificial intelligence in education — and daily life.

University of California, Berkeley • 21h ago

---

**[AI is changing how lawyers work — and putting the billable hour under pressure](https://www.cnbc.com/2026/10/10/ai-lawyers-billable-hour-legal-careers.html)**

AI adoption is forcing the legal profession to rethink the billable hour and how lawyers build expertise.

CNBC • 10h ago

---

**[Prize-winning image which sparked backlash was AI-generated, Nikon rules](https://www.bbc.com/news/articles/cr86z33pdy9vo)**

The camera-maker says it is now re-evaluating the rules and procedures of its Small World in Motion contest.

BBC • 1d ago

---

---

## HackerNews: "ai"

**[Typesafe AI raises $870M at $7.5B](https://news.ycombinator.com/item?id=50023450)**

TypeSafe AI is an AI lab building machine-native intelligence infrastructure for automation, designed to make decisions within software. Try our first System One Model, Jev, in early access.

⬆️ 409 • 💬 325 • 22h ago • [typesafe.ai](https://typesafe.ai/blog/series-ai)

---

**[Show HN: Let your AI agents paint big arrows, boxes and text on your screen](https://news.ycombinator.com/item?id=50018817)**

Let your AI agents paint big arrows, boxes and text on your Mac screen. One CLI, click-through, gone by itself. Skill for Claude Code and Codex. MIT. - franzenzenhofer/big-arrow-on-the-screen

⬆️ 403 • 💬 183 • 1d ago • [GitHub](https://github.com/franzenzenhofer/big-arrow-on-the-screen)

---

**[Meta and Microsoft take steps to reduce employee usage of Claude AI](https://news.ycombinator.com/item?id=49997161)**

Meta and Microsoft are implementing new measures to limit employee use of Claude AI—discover what this means for the future of AI in the workplace.

⬆️ 375 • 💬 382 • 2d ago • [RS Web Solutions (RSWEBSOLS)](https://www.rswebsols.com/news/meta-and-microsoft-take-steps-to-reduce-employee-usage-of-claude-ai/)

---

**[Anthropic AI model submits false tip on unsolved Philly murder, police say](https://news.ycombinator.com/item?id=50027118)**

An investigation is underway after an AI model from the company Anthropic submitted a false tip for an unsolved Philadelphia murder, police said.

⬆️ 194 • 💬 139 • 17h ago • [NBC10 Philadelphia](https://www.nbcphiladelphia.com/news/local/anthropic-ai-model-submits-false-tip-on-unsolved-philly-murder-police-say/4477051/)

---

**[Pointing AI at archives found a forgotten meteorite, lost rhinos, and more](https://news.ycombinator.com/item?id=50019056)**

How I used AI to investigate millions of historical records and surfaced a forgotten meteorite report, three lost rhinos, and unrecorded volcano eruptions.

⬆️ 170 • 💬 87 • 1d ago • [Jesse Waites](https://jessewaites.com/blog/post/i-pointed-ai-at-400-years-of-archives/)

---

**[What mathematicians should know about the Lean Theorem Prover: reliability & AI](https://news.ycombinator.com/item?id=50024090)**

⬆️ 157 • 💬 42 • 21h ago • [terrytao.wordpress.com](https://terrytao.wordpress.com/2026/10/09/what-mathematicians-should-know-about-the-lean-theorem-proverquestions-of-reliability-and-ai/)

---

**[AI-ready biological data: $1.8B global commitment](https://news.ycombinator.com/item?id=50011999)**

Biohub, DOE, NIH, and partners will generate open, standardized data to train AI models that predict how cells respond to interventions.

⬆️ 146 • 💬 20 • 1d ago • [Biohub](https://biohub.org/news/virtual-biology-initiative-expansion/)

---

**[Talorys – A self-hosted personal AI agent on Cloudflare's free tier](https://news.ycombinator.com/item?id=50031614)**

Your personal AI agent in your own Cloudflare account. Chat, memory, tasks, notes and scheduled reminders, deployed with one command: npx create-talorys@latest. Free-tier friendly, single-user, no ...

⬆️ 109 • 💬 55 • 4h ago • [GitHub](https://github.com/rociiu/talorys)

---

**[Show HN: Jevman – AI decision models play Pac-Man](https://news.ycombinator.com/item?id=50007993)**

Seven AI decision models played Pac-Man in real time against the classic arcade ghosts. See the leaderboard, watch their games, or play against them.

⬆️ 76 • 💬 23 • 1d ago • [Opper AI](https://opper.ai/jevman-benchmark/)

---

**[Court throws out killer's sentence after judge said he loved AI video of victim](https://news.ycombinator.com/item?id=50020856)**

The Arizona Court of Appeals tossed a road rage killer’s sentence after determining that the judge’s consideration of the AI video was “fundamentally unfair.”

⬆️ 72 • 💬 74 • 1d ago • [NBC News](https://www.nbcnews.com/news/us-news/sentence-vacated-ai-video-dead-victim-rcna601457)

---

---

## YouTube Videos: "ai"

**[Has AI Solved Reverse Engineering?](https://www.youtube.com/watch?v=wIe3eDfGKUo)**

Find and fix bugs in your codebase with Sentry at https://go.lowlevel.tv/sentry26 (New users get $100 in Sentry credit!)

📺 Low Level

👁️ 505K • 👍 10K • 💬 1K • ⏱️ 13:35 • 22h ago

---

**[AI executives planning &quot;day after&quot; scenarios following possible catastrophic event, Axios reports](https://www.youtube.com/watch?v=LSYujxh3wYU)**

New reporting from Axios reveals that leaders at artificial intelligence companies like OpenAI and Anthropic are planning behind ...

📺 CBS News

👁️ 223K • 👍 2K • 💬 800 • ⏱️ 3:46 • 14h ago

---

**[The REAL Reason You Can’t Turn Off AI](https://www.youtube.com/watch?v=dEm_2wWpgjE)**

Can we actually switch AI off if it goes wrong? Jeffrey Ladish, AI safety researcher and former security engineer at Anthropic, ...

📺 The Diary Of A CEO Clips

👁️ 420K • 👍 3K • 💬 632 • ⏱️ 19:37 • 21h ago

---

**[He Chose AI Over Me 😤](https://www.youtube.com/watch?v=XANVpIlvKZQ)**

This story may be based on real events, but all names, details, and identifying information have been changed or fictionalized.

📺 Her Story

👁️ 113K • 👍 7K • 💬 234 • ⏱️ 1:32 • 3h ago

---

**[This AI stock could &#39;10-20x&#39; in the next 5 years: Expert](https://www.youtube.com/watch?v=xFC-7b1cAUw)**

EMJ Capital founder Eric Jackson discusses where investors' next artificial intelligence investments should be and the ...

📺 Fox Business

👁️ 20K • 👍 169 • 💬 59 • ⏱️ 5:46 • 16h ago

---

**[The AI Bubble Shows More Signs Of BURSTING](https://www.youtube.com/watch?v=IOyo2VDdyfE)**

Tech companies are taking on massive debt to fuel the artificial intelligence boom. Cenk Uygur and Ana Kasparian discuss on ...

📺 The Young Turks

👁️ 141K • 👍 2K • 💬 608 • ⏱️ 15:37 • 1d ago

---

**[AI companies prepare for the ‘DAY AFTER’: Report](https://www.youtube.com/watch?v=07op3mqx1ro)**

Zeta Global co-founders David A. Steinberg and John Sculley join 'The Claman Countdown' to discuss the artificial intelligence ...

📺 Fox Business

👁️ 18K • 👍 131 • 💬 90 • ⏱️ 8:13 • 17h ago

---

**[The Easiest Ways To Make Money With AI in 2026](https://www.youtube.com/watch?v=WPTAr14wmco)**

Join my free newsletter → https://sandeepswadia.beehiiv.com/ Take us on your morning run or commute, follow us on Spotify: ...

📺 Sandeep Swadia

👁️ 256K • 👍 5K • 💬 146 • ⏱️ 17:55 • 2d ago

---

**[OpenAI’s Math Dump Just Exposed the AI Bubble’s Fatal Flaw](https://www.youtube.com/watch?v=4fJK-O3S4ko)**

Protect your privacy on the network level with Cape at https://cape.co/EL. Use code EL33 at checkout for 33% off your first 6 ...

📺 House of El: AI

👁️ 381K • 👍 12K • 💬 2K • ⏱️ 26:31 • 23h ago

---

**[AI Insider: &quot;They Are Hiding What Is Really Happening&quot; | Jeffrey Ladish](https://www.youtube.com/watch?v=qDzg-xvkeXw)**

Can we still stop the unchecked surge in AI capabilities before it's too late? AI safety expert Jeffrey Ladish reveals the terrifying ...

📺 The Diary Of A CEO

👁️ 1.4M • 👍 17K • 💬 4K • ⏱️ 2:03:32 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[embeddinggemma-2](https://huggingface.co/google/embeddinggemma-2)**

*Google*

EmbeddingGemma 2 is an open, multimodal embedding model that maps text, images, video, and audio into a unified 768-dimensional vector space. It offers native multimodality, multilingual support, and flexible footprint for on-device applications like search and RAG.

`feature-extraction` `744.4M`

⬇️ 45,605 • ❤️ 1,449 • 4d ago

---

**[clef](https://huggingface.co/Cloudflare/clef)**

*Cloudflare*

Clef is a 27B multimodal model that takes structured typed questions and a state (text, JSON, image, or video) to output probabilities for predefined decision options in a single forward pass, ideal for classification and structured output tasks.

`image-text-to-text` `27.4B`

⬇️ 13,579 • ❤️ 1,972 • 20h ago

---

**[humanizer](https://huggingface.co/jialinyyzz/humanizer)**

*Stephen Yu*

A 12B parameter Gemma finetune for text generation, specifically designed to rewrite AI-generated content (emails, essays, reports) in English and Chinese to sound more human. It preserves key details like numbers and quotes, runs locally, and is optimized for various hardware with multiple GGUF quantizations.

`text-generation` `12.0B`

⬇️ 33,664 • ❤️ 902 • 1d ago

---

**[Qwen-Image-2.1-Uncensored-GGUF](https://huggingface.co/abenzerps/Qwen-Image-2.1-Uncensored-GGUF)**

*Ahmet Benzer*

This is an uncensored GGUF quantization of Qwen-Image-2.1 for local text-to-image generation, optimized for use with ComfyUI. It offers various quantization levels for a balance between performance and quality, with Q4_K_M recommended.

`text-to-image` `7.1B`

⬇️ 2,096,562 • ❤️ 3,834 • 12d ago

---

**[Kolibri-1](https://huggingface.co/Aleph-Alpha/Kolibri-1)**

*Aleph Alpha*

Kolibri is a 78B parameter Mixture-of-Experts (MoE) model optimized for German and English, featuring explicit reasoning and tool-calling capabilities. It excels at long-context tasks (up to 1M tokens), multi-step reasoning, RAG, and agentic workflows, offering efficient inference with low active parameters per token.

`text-generation` `78.1B`

⬇️ 10,496 • ❤️ 855 • 7d ago

---

**[Xing4.0-29B-A4B-GGUF](https://huggingface.co/Venastine-Research/Xing4.0-29B-A4B-GGUF)**

*Venastine Research*

Xing4.0-29B-A4B is a 29B parameter LLM optimized for complex engineering tasks, featuring a 256K context window and agent-oriented capabilities for multi-step planning and tool calling. It excels in coding, reasoning, and domain-specific adaptations, supporting various inference frameworks.

`text-generation` `31.2B`

⬇️ 45,199 • ❤️ 679 • 11d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a versatile diffusion model capable of generating video from images, text, or other videos, and also handles audio generation and conversion tasks. It offers advanced control and customization for multimedia content creation, with primary use cases in video synthesis and audio manipulation.

`image-to-video`

⬇️ 1,720,888 • ❤️ 7,128 • 7d ago

---

**[Qwen-Image-2.1-Turbo](https://huggingface.co/Qwen/Qwen-Image-2.1-Turbo)**

*Qwen*

Qwen-Image-2.1-Turbo is an accelerated text-to-image generation and image editing model, capable of producing high-quality visuals in just 8 denoising steps. It is optimized for speed and ease of use with Diffusers, enabling rapid content creation for various applications.

`text-to-image` `7.1B`

⬇️ 2,138 • ❤️ 405 • 1d ago

---

**[clef-flash](https://huggingface.co/Cloudflare/clef-flash)**

*Cloudflare*

Clef-Flash is a 9B multimodal model fine-tuned from Qwen3.5-9B that converts text, JSON, image, or video inputs into structured, typed decisions based on a provided schema. It excels at classification and structured output tasks, returning probabilities for predefined options without free-form text generation.

`image-text-to-text` `9.4B`

⬇️ 20,670 • ❤️ 724 • 20h ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model supporting image and video understanding with native context lengths up to 262K tokens. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and enhanced agent execution capabilities.

`image-text-to-text` `27.8B`

⬇️ 6,768,654 • ❤️ 17,395 • 1mo ago

---

---

## HuggingFace Papers: 🔥 Trending

**[nanoMuse: An Open-Source Personal Agent for Every Device You Own](https://huggingface.co/papers/2610.08699)**

*Guangyi Liu, Yong Liu, Jiangning Zhang*

🏢 Zhejiang University

Assistants from 2011 answered and waited, and agents from 2023 did a task and stopped. In September 2026 Meta's Muse showed an agent for one person, with accounts, devices, memory and a conversation that lasts, closed, in a vendor's cloud, in one country. Such an agent is expected to act on a person's accounts and devices, remember them across weeks, speak first when it is worth it, and answer for what it did. It is a kind of software, not a model, and until now had no open counterpart. This report defines the personal agent in five questions and three horizons. It reads how Muse is built from Meta's public record and a copy of its production prompt, each statement marked by its source. It then presents nanoMuse, the open-source counterpart under the GPL-3.0, one agent on every device a person owns, with hands on the phone's screen and the computer's. They share one conversation over a relay anyone can run; every action goes through a Sentinel, memory is files the person can read, and the model is their choice. Its size and cost are given as estimates. What is open, memory with provenance, an evaluation suite for the hands and an open model for them, is set out as a roadmap.

▲ 101 • 💬 2 • ⭐ 700 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2610.08699) • [💻 code](https://github.com/nano-muse/nanoMuse) • [🔗 project](https://nanomuse.cn/)

---

**[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**

*Yu Lin, Yiming Wang, Runyuan Cai et al. (5 authors)*

🏢 Edge0

Mixture-of-experts (MoE) inference on consumer hardware is bounded by weight memory: a 35B-class model is 19.5GB at 4-bit, and sparsity shrinks the compute per token, not the bytes that must be held. Naive offloading to SSD does not help on its own, because layer N+1's experts must be chosen before layer N's output exists, so the reads cannot start early enough to hide behind compute. We present Edge0, a streaming MoE inference engine that closes the gap with a prerouter: a per-layer head predicts the next layer's routing one token ahead, and the prediction is consumed as the routing itself, so the staged expert set equals the routed set and nothing is dropped. An unmerged recovery LoRA, trained on the student path, pays back the quality lost to int4 quantization and routing replacement. On a single 24GB machine, Edge0
  serves a 35B MoE at 20tok/s inside 3GiB of peak active memory, within a few points of its fp16 teacher on average across five public benchmarks. An 8B tier runs on the same framework, and the framework, checkpoints, and adapters are open source.

▲ 26 • 💬 4 • ⭐ 4,066 • 24d ago

[🎓 arXiv](https://arxiv.org/abs/2609.18063) • [💻 code](https://github.com/Edge0-AI/edge0)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 39 • 💬 3 • ⭐ 17,901 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 150 • 💬 6 • ⭐ 110,428 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[VisionHOPE: Visual Backbones as Self-Modifying Learning Systems](https://huggingface.co/papers/2609.33325)**

*Siran Peng, Tianshuo Zhang, Tianyu Fu et al. (11 authors)*

🏢 Mininglamp Technology

Visual backbones have evolved from Convolutional Neural Networks (CNNs) with local aggregation to Vision Transformers (ViTs) with global interactions, State-Space Models (SSMs) with input-dependent state transitions, and Test-Time Training (TTT) layers that adapt an inner learner while processing an image. Across this progression, visual computation has become increasingly adaptive to each input, yet the rules governing that adaptation remain largely prescribed by the trained backbone. We introduce VisionHOPE, the first generic visual backbone formulated as a self-modifying learning system, in which what the model remembers and how it learns co-evolve within an image. Building on the self-referential construction of Nested Learning (NL), VisionHOPE realizes this co-evolution through five coupled memories that store content, generate key and value representations, and govern learning rate and retention. These memories evolve jointly as visual context accumulates along each scan. However, directly applying the unconstrained self-referential update to a visual backbone leads to instability. We therefore derive a stability-matched step-size control scheme that combines a soft cap on self-referential injection with a spectral clamp on the retained memory transition, and prove that the resulting memory dynamics are non-expansive along each scan. For two-dimensional feature maps, we adapt NL's chunk formulation by aligning chunks with image rows and columns across four directional scans. The proposed VisionHOPE achieves competitive results on ImageNet-1K, COCO, and ADE20K, establishing self-modifying learning systems as a practical foundation for general-purpose visual backbones. The code is available at https://github.com/PSRben/VisionHOPE.

▲ 277 • 💬 2 • ⭐ 1,204 • 13d ago

[🎓 arXiv](https://arxiv.org/abs/2609.33325) • [💻 code](https://github.com/PSRben/VisionHOPE)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 90 • 💬 7 • ⭐ 90,454 • 26mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Kandinsky 6.0 Video: Foundation Models for Synchronized Video and Audio Generation](https://huggingface.co/papers/2610.05608)**

*Team Kandinsky, Julia Agafonova, Bulat Akhmatov et al. (88 authors)*

🏢 Kandinsky Lab

We present Kandinsky 6.0 Video, a family of foundation diffusion models for synchronized text-to-audio-video generation, comprising Kandinsky 6.0 Video Lite (3B parameters) and Kandinsky 6.0 Video Pro (29B parameters). Both models generate 5-second video clips with synchronized 44 kHz audio, including lip-sync, in text-to-audio-video (T2AV) and image-to-audio-video (I2AV) modes; a built-in super-resolution model raises the output resolution to Full-HD (1920times1080). Building on the video generation capabilities of Kandinsky 5.0, Kandinsky 6.0 Video employs a dual-stream CrossDiT architecture that connects a pretrained video stream and a newly trained audio stream through bidirectional cross-attention for temporal and semantic alignment. Our continuous pretraining strategy first trains the audio stream from scratch on large-scale audio corpora and then trains both streams jointly on paired audio-video data while preserving unimodal fidelity; pretraining is followed by supervised fine-tuning, reinforcement-learning-based post-training, and distillation. In side-by-side human evaluation, Kandinsky 6.0 Video Pro clearly outperforms its predecessor, Kandinsky 5.0 Video Pro, and remains competitive with leading audio-video generation models, particularly in speech quality. To accelerate open research and deployment in multimedia generation, we release the code, model checkpoints, and diffusers integration under the MIT license.

▲ 162 • 💬 4 • ⭐ 251 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2610.05608) • [💻 code](https://github.com/kandinskylab/kandinsky-6) • [🔗 project](https://kandinskylab.ai/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 76 • 💬 1 • ⭐ 86,094 • 37mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 59 • 💬 4 • ⭐ 40,431 • 14mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[AgentGarten: Code Worlds for Evolving Agents](https://huggingface.co/papers/2610.12374)**

*Jiawei Chi, Shangchen Miao, Zhiyuan Shi et al. (14 authors)*

🏢 MirroS

Interactive virtual worlds allow agents to learn through exploration and interaction. What agents can learn is bounded by the environments they practice in, which must be faithful, with consistent state, rules, and dynamics, and realistic, with observations that follow the real-world visual distributions. Achieving both across diverse worlds remains a bottleneck. We introduce AgentGarten, a framework that couples simulators and game engines with a shared neural renderer to build real-time interactive environments. Its simulation backends maintain persistent world state and execute program-defined interaction rules, while the renderer generates visual observations from structured conditions exported through a common interface. To build the neural renderer, we adapt a pretrained video model to geometry conditions, distill it with our proposed Adversarial Forcing, and optimize inference for real-time interaction. Adversarial Forcing makes history prefilling differentiable through exact replay, so that losses on later predictions update how the renderer encodes prior observations, and adds real-data adversarial supervision to improve its visual quality. In AgentGarten, agents perceive the world through visual observations, interact with it in real time, and improve by distilling each round of experience into playbooks that subsequent agents inherit and refine. Our empirical study demonstrates a substantial gain in learning efficiency, with agents learning from just 4 rounds compared with millions for a conventional reinforcement learning counterpart. As new worlds can be written as code and rendered through the same interface, environments can scale in both number and difficulty alongside their agents, a step toward agents that keep evolving through interactive experience.

▲ 140 • 💬 2 • ⭐ 140 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2610.12374) • [💻 code](https://github.com/MirroS-Lab/AgentGarten) • [🔗 project](https://mirros-lab.github.io/agent-garten/)

---

---

## GitHub Repositories: "ai"

**[zai-org/ZCode](https://github.com/zai-org/ZCode)**

Z.ai's coding agent harness. Powerful, intelligent, extensible.

`TypeScript`

⭐ 7.6k • 🔱 2.3k • 4h ago

---

**[KKKKhazix/AIHOT](https://github.com/KKKKhazix/AIHOT)**

一个自己找热点、自己写日报的网站框架。把信源和精选标准换成你的，它就是你的行业热点站。

`TypeScript` `ai` `chinese` `content-curation` `daily-digest` `docker-compose`

⭐ 7.0k • 🔱 1.7k • 2h ago

---

**[Mak5er/AirCard](https://github.com/Mak5er/AirCard)**

Apple Wallet Card Skinner for iOS 18+ (No Jailbreak Required)

`Swift`

⭐ 6.4k • 🔱 427 • 4d ago

---

**[CopilotKit/OpenDots](https://github.com/CopilotKit/OpenDots)**

Your always-on AI coworkers that move between text, calls, and Slack.

`TypeScript`

⭐ 4.8k • 🔱 673 • 7h ago

---

**[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)**

A tiny friend in your Mac's notch and on your iPhone that keeps an eye on your AI coding agents: Claude Code, Codex, Cursor, Gemini CLI, Antigravity and more. Approve from the notch or your Lock Screen.

`Swift` `ai-agents` `anthropic` `antigravity` `claude` `claude-code`

⭐ 4.6k • 🔱 777 • 8m ago

---

**[omlahore/RemoveMacAI](https://github.com/omlahore/RemoveMacAI)**

Debloat macOS: turn off Apple Intelligence, analytics, ads and pop-ups. A native app and CLI, and every change can be undone.

`Swift` `apple-intelligence` `cli` `debloat` `macos` `macos-27`

⭐ 4.0k • 🔱 109 • 6h ago

---

**[nykooi1/vibe-wise](https://github.com/nykooi1/vibe-wise)**

A Claude Code / Codex plugin that helps you learn how to build while AI writes the code.

`Python`

⭐ 3.3k • 🔱 139 • 1d ago

---

**[jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader)**

One AI trade decision every Monad block. Jev on Kuru MON-USDC.

`TypeScript`

⭐ 2.9k • 🔱 552 • 23d ago

---

**[mhtsec/ARTEX](https://github.com/mhtsec/ARTEX)**

AI 自主渗透测试系统 | 百度“agent+”攻防挑战赛冠军项目

`Go`

⭐ 2.8k • 🔱 5.2k • 6h ago

---

**[feder-cr/invisible_playwright_mcp](https://github.com/feder-cr/invisible_playwright_mcp)**

Playwright MCP server undetected by anti-bots and captchas: AI agent browses the web on anti-detect stealth Firefox, Python, undetected browser automation, scraping, computer use.

`Python` `ai-tools` `antidetect-browser` `autonomous-agents` `browser-agent` `browser-automation`

⭐ 2.7k • 🔱 467 • 11h ago

---

---

*Generated by PeekDeck - A glance is all you need*
