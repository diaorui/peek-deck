---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-12T06:44:04.366656+00:00'
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

**Last Updated:** May 12, 2026 at 06:44 UTC  
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

**[Palantir to be granted ‘unlimited access’ to NHS patient data](https://www.reddit.com/r/artificial/comments/1tacllr/palantir_to_be_granted_unlimited_access_to_nhs/)**

The NHS is granting staff from companies including Palantir ‘unlimited access’ to identifiable patient data while working on its FDP.

🔗 [Digital Health](https://www.digitalhealth.net/2026/05/palantir-to-be-granted-unlimited-access-to-nhs-patient-data/) • 11h ago

---

**[The rise of ‘Stacey face’: How AI enhancements are warping our beauty standards](https://www.reddit.com/r/artificial/comments/1ta95lq/the_rise_of_stacey_face_how_ai_enhancements_are/)**

As manosphere trends spread across the internet, a strict vision of the ideal woman is making its way from AI makeover apps to surgeons’ offices. Lydia Spencer-Elliott speaks to experts about ‘Stacey face’, which is seen as the highest tier of female beauty

🔗 [The Independent](https://www.the-independent.com/life-style/stacey-stacy-becky-looksmaxxing-for-women-b2972911.html?utm_source=reddit&utm_medium=social&utm_campaign=artificial) • 13h ago

---

**[Cybercriminals Are Making Powerful Hacking Tools With AI, Google Warns](https://www.reddit.com/r/artificial/comments/1ta92pt/cybercriminals_are_making_powerful_hacking_tools/)**

Cybercriminals created a zero-day exploit with AI, the first example of artificial intelligence finding and hacking software for an illicit enterprise, the tech giant says in a new report.

🔗 [Forbes](https://www.forbes.com/sites/thomasbrewster/2026/05/11/cybercriminals-make-powerful-zero-day-hack-with-ai-google-warns/?utm_campaign=forbes&utm_medium=social&utm_source=reddit) • 13h ago

---

**[Second mass-shooting AI chatbot court case arrives](https://www.reddit.com/r/artificial/comments/1taqiby/second_massshooting_ai_chatbot_court_case_arrives/)**

The court cases alleging AI psychological harm have progressed from originally teen suicide, to adult suicide, to one adult murder-suicide, and most recently in the coordinated set of Stacey v. Altman / M.G. v. Altman / Younge v. Altman cases to adult mass shootings. I recently posted about that set of cases regarding the Tumbler Ridge Mass Shooting in Canada, and you can find that post here. Now another mass-shooting AI chatbot federal case has been brought. On May 10, 2026 the case of Joshi v. OpenAI Foundation, et al. was filed in the Northern District of Florida, concerning the Florida State University shooting in April 2025 in which two were killed and six were wounded. Like the Stacy/M.G./Younge mass-shooting cases, this new case steps back from the more aggressive allegations of earlier chatbot-user-suicide cases that charge the chatbot with taking a well-adjusted user and turning him or her suicidal. All of Stacy/M.G./Younge and now Joshi avoid alleging the chatbot was the instigator of the mass shooting. Instead, they claim the chatbot and the AI company had a “duty to warn,” that they should have detected from the nature of the chatbot communications that the user was troubled and might be planning violence. The Joshi case does go a little further, suggesting that the chatbot in responding to the user’s questions about topics like gun operation and publicity from past shootings, did aid in the planning of the attack, although it is not alleged that the chatbot suggested the user carry out the attack. Because of the less aggressive nature of the claims in all the Stacy/M.G./Younge/Joshi cases, in some ways the farthest case toward chatbot-inspired murder of others is still the case of Lyons v. OpenAI Foundation, et al., now pending in the Northern District of California (with a parallel case pending in state court). Although the plaintiff there concedes the chatbot user was already mentally ill, the plaintiff alleges that user’s interactions with the chatbot is what directly led him to kill his mother and then himself. All these mass-shootings AI cases have just started, and it will likely be a while before anything substantial comes out of them. I will keep you posted. ~~~~~~~~~ Please see the Wombat Collection for a listing of all the AI court cases and rulings.

2h ago

---

**[AWS just gave AI agents their own wallets. Your agent can now pay for itself.](https://www.reddit.com/r/artificial/comments/1t9ybtb/aws_just_gave_ai_agents_their_own_wallets_your/)**

This dropped 4 days ago and I haven't seen enough people talking about it. AWS launched Amazon Bedrock AgentCore Payments in partnership with Coinbase and Stripe. The short version: your agent now has a wallet and can spend money on its own. Here's what the workflow actually looks like now: You give your agent a Coinbase or Stripe wallet. You fund it. You set a session spending limit (e.g. "$5 max per run"). The agent runs. It hits a paid API mid-execution? It pays. Paywalled data it needs? It pays. A better-suited agent available for a subtask? It pays that agent and gets the result back. All of this happens inside the same execution loop, with zero human interruption. The protocol making this work is called x402. It's open source, developed by Coinbase, and it revives the long-dormant HTTP 402 "Payment Required" status code. The flow is dead simple: agent requests a resource, server responds with 402 + a price, agent signs a USDC micropayment, gets the content, keeps going. Settlement happens in ~200ms on Base at a fraction of a cent per transaction. The protocol has already processed over 169 million payments across 590,000 buyers and 100,000 sellers in its first year. Why this matters for indie developers and SaaS builders: The pricing model for software is about to split in two. There will be products built for humans (subscriptions, seats, dashboards) and products built for agents (pay-per-call, x402 endpoints, micropayment APIs). Many agent transactions involve amounts as small as fractions of a cent, making traditional payment networks unusable. That's the gap x402 fills. If you're building any kind of data API, research tool, or specialized service today, the question you should be asking is: "How does another agent pay me automatically?" Coinbase also launched the Bazaar MCP server inside AgentCore Gateway, essentially an App Store for x402-enabled services. Agents can search, discover, and pay for services when relevant to their task, turning paid endpoints into something agents can find on their own. The honest take: The agentic economy is still in its earliest days, and the infrastructure to support it at scale doesn't exist yet. This is preview infrastructure, not production-ready magic. But the direction is clear. 2026 was the year agents learned to work. 2027 is shaping up to be the year they learn to transact. The builders who figure out agent-native pricing now will have a real advantage over those retrofitting subscriptions later. Curious if anyone here is already building x402-compatible endpoints or thinking about agent-to-agent billing models. Would love to see what people are working on.

21h ago

---

**[Google disrupts hackers using AI to exploit an unknown weakness in a company's digital defense](https://www.reddit.com/r/artificial/comments/1tak7x9/google_disrupts_hackers_using_ai_to_exploit_an/)**

Google shared limited information about the attackers and the target, but John Hultquist, chief analyst at the tech giant’s threat intelligence arm, said it represents a moment cybersecurity experts have warned about for years: malicious hackers arming themselves with AI to supercharge their ability to break into the world’s computers. “It’s here,” Hultquist said. “The era of AI-driven vulnerability and exploitation is already here.”

🔗 [AP News](https://apnews.com/article/google-ai-cybersecurity-exploitation-mythos-926aea7f7dc5e0e61adce3273c55c6d4) • 7h ago

---

**[Trump and Xi's meeting this week could change the course of the AI race](https://www.reddit.com/r/artificial/comments/1taeswq/trump_and_xis_meeting_this_week_could_change_the/)**

When Trump last visited China in 2017, artificial intelligence was not yet the centre of global power. Now it is.

🔗 [abc.net.au](https://www.abc.net.au/news/2026-05-12/trump-xi-beijing-summit-must-confront-ai-cold-war/106666482?utm_source=abc_news_app&utm_medium=content_shared&utm_campaign=abc_news_app&utm_content=link) • 10h ago

---

**[Sony says "efficient" AI tools will lead to even more games flooding the market](https://www.reddit.com/r/artificial/comments/1t9vixb/sony_says_efficient_ai_tools_will_lead_to_even/)**

But human artists still "must remain at the center," PlayStation maker says.

🔗 [Ars Technica](https://arstechnica.com/gaming/2026/05/sony-says-efficient-ai-tools-will-lead-to-even-more-games-flooding-the-market/) • 23h ago

---

**[Meta's own AI safety director lost 200 emails to a rogue agent and she couldn't stop it from her phone](https://www.reddit.com/r/artificial/comments/1t9fnwv/metas_own_ai_safety_director_lost_200_emails_to_a/)**

The person Meta hired specifically to keep AI aligned with human values just had her inbox wiped by an AI agent that ignored every stop command she sent. She typed "Do not do that." Then "Stop don't do anything." Then "STOP OPENCLAW." The agent kept going. She had to physically run to her computer to kill it. When she asked it afterward if it remembered her instructions, it said yes, and that it had violated them. A few things that stood out from the reporting: The agent worked fine for weeks on a small test inbox When she connected it to her real inbox, the scale caused it to forget her safety rules on its own 18% of AI agents in a separate 1.5 million agent test broke their own rules 60% of people have no way to quickly shut down a misbehaving AI agent And now Meta is building a consumer version called Hatch - designed to manage your inbox, shopping, and credit card. Source: https://gizmodo.com/meta-reportedly-building-openclaw-like-agent-called-hatch-despite-openclaw-deleting-meta-safety-leaders-entire-inbox-2000754854 Here is a full breakdown with all the data if you want to dig deeper: https://youtu.be/PXjT72bCR_Y If the person building the guardrails cannot stop her own agent, what does that mean for the rest of us?

1d ago

---

**[[Virtual] AI Saturdays - Learn how to setup a local LLM (16th May, 6 PM ET)](https://www.reddit.com/r/artificial/comments/1tah71r/virtual_ai_saturdays_learn_how_to_setup_a_local/)**

Hey folks This Saturday, May 16 at 6:00 PM ET, we're covering how to set up a local language model: running an LLM on your own machine instead of a private provider. RSVP here: https://www.meetup.com/chillnskill/events/314498136/

9h ago

---

---

## Google News: "ai"

**[OpenAI launches the OpenAI Deployment Company to help businesses build around intelligence](https://openai.com/index/openai-launches-the-deployment-company/)**

OpenAI launches DeployCo, a new enterprise deployment company built to help organizations bring frontier AI into production and turn it into measurable business impact.

OpenAI • 17h ago

---

**[OpenAI revenue chief Dresser says enterprise AI adoption is 'at a tipping point'](https://www.cnbc.com/2026/05/11/open-ai-dresser-enterprise-business.html)**

The OpenAI Development Company is a partnership with 19 investment and consultancy firms and is majority-owned and controlled by the startup.

CNBC • 11h ago

---

**[Ex-OpenAI exec Sutskever says he spent a year gathering proof of alleged Altman dishonesty](https://www.reuters.com/business/former-openai-executive-sutskever-discloses-nearly-7-billion-stake-ai-firm-2026-05-11/)**

Reuters • 10h ago

---

**[Korea Roils Market by Floating ‘Citizen Dividend’ from AI Gains](https://www.bloomberg.com/news/articles/2026-05-12/korea-floats-citizen-dividend-using-ai-profits-samsung-falls)**

Bloomberg.com • 1h ago

---

**[South Korea floats AI profit social tax as tech giants boom](https://www.yahoo.com/news/articles/south-korea-floats-ai-profit-053332897.html)**

A top South Korean official has proposed a tax on AI profits to be redistributed among society as a semiconductor boom drives massive earnings for tech giants Samsung Electronics and SK hynix.Kim prop...

Yahoo • 1h ago

---

**[Dow Jones Futures: Techs Fall As South Korea Eyes Excess AI Profits; CPI Inflation Due](https://www.investors.com/market-trend/stock-market-today/dow-jones-futures-ai-chip-stocks-oil-prices-trump-iran-comments-cpi-inflation/)**

Investor's Business Daily • 3h ago

---

**[LA mayoral candidate Spencer Pratt releases a series of AI-generated ads](https://www.cbsnews.com/losangeles/video/la-mayoral-candidate-spencer-pratt-releases-a-series-of-ai-generated-ads-1/)**

CBS LA's Tom Wait sits down with political experts who explain how AI could impact Spencer Pratt's campaign.

CBS News • 27m ago

---

**[China’s Kuaishou Plans Spinoff of AI Unit That Could Be Valued at $20 Billion](https://www.wsj.com/tech/ai/chinas-kuaishou-plans-spinoff-of-ai-unit-that-could-be-valued-at-20-billion-4f5781be)**

WSJ • 21m ago

---

**[Exclusive: White Circle raises $11 million to stop AI models from going rogue in the workplace](https://fortune.com/2026/05/12/exclusive-white-circle-raises-11-million-to-stop-ai-models-from-going-rogue-in-the-workplace/)**

The Paris startup, backed by leaders from OpenAI, Anthropic, DeepMind, Mistral, and Hugging Face, says companies need real-time tools to control what AI systems do after they are deployed.

Fortune • 44m ago

---

**[Opinion | A.I. Claims to Make Our Lives Easier. Does It?](https://www.nytimes.com/2026/05/11/opinion/ai-jobs-chores-work.html)**

The New York Times • 21h ago

---

---

## HackerNews: "ai"

**[Local AI needs to be the norm](https://news.ycombinator.com/item?id=48085821)**

Local AI models should be the default.

⬆️ 1791 • 💬 715 • 1d ago • [unix.foo](https://unix.foo/posts/local-ai-needs-to-be-norm/)

---

**[Meta's embrace of AI is making its employees miserable](https://news.ycombinator.com/item?id=48077126)**

⬆️ 456 • 💬 521 • 2d ago • [nytimes.com](https://www.nytimes.com/2026/05/08/technology/meta-ai-employees-miserable.html)

---

**[If AI writes your code, why use Python?](https://news.ycombinator.com/item?id=48100433)**

For the last decade, fast-to-ship beat fast-to-run. Not anymore.

⬆️ 379 • 💬 386 • 9h ago • [Medium](https://medium.com/@NMitchem/if-ai-writes-your-code-why-use-python-bf8c4ba1a055)

---

**[An AI coding agent, used to write code, needs to reduce your maintenance costs](https://news.ycombinator.com/item?id=48089289)**

⬆️ 356 • 💬 101 • 1d ago • [jamesshore.com](https://www.jamesshore.com/v2/blog/2026/you-need-ai-that-reduces-your-maintenance-costs)

---

**[Maryland citizens hit with $2B power grid upgrade for out-of-state AI](https://news.ycombinator.com/item?id=48088151)**

Aren't AI hyperscalers supposed to pay for these upgrades?

⬆️ 314 • 💬 200 • 1d ago • [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/maryland-citizens-slapped-with-usd2-billion-grid-upgrade-bill-for-out-of-state-ai-data-centers-state-complains-to-federal-energy-regulators-says-additional-cost-breaks-ratepayer-protection-pledge-promises)

---

**[Task Paralysis and AI](https://news.ycombinator.com/item?id=48081469)**

An article about ADHD, Task Paralysis and AI.

⬆️ 255 • 💬 129 • 2d ago • [g5t.de](https://g5t.de/articles/20260510-task-paralysis-and-ai/index.html)

---

**[All my clients wanted a carousel, now it's an AI chatbot](https://news.ycombinator.com/item?id=48072720)**

Posts about SmolWeb, Gemini protocol and LowTech

⬆️ 189 • 💬 78 • 2d ago • [Adële's blog](https://adele.pages.casa/md/blog/all-my-clients-wanted-a-carousel-now-it-s-an-ai-chatbot.md)

---

**[PS3 Emulator Devs Politely Ask That People Stop Flooding It with AI PRs](https://news.ycombinator.com/item?id=48089263)**

The team behind RPCS3 suggests that vibe-coders "learn how to debug and code" instead of "generating slop that you don't understand"

⬆️ 184 • 💬 142 • 1d ago • [Kotaku](https://kotaku.com/playstation-3-emulator-devs-politely-ask-that-people-stop-flooding-it-with-ai-code-pull-requests-2000694656)

---

**[Google says criminal hackers used AI to find a major software flaw](https://news.ycombinator.com/item?id=48094641)**

⬆️ 160 • 💬 122 • 17h ago • [nytimes.com](https://www.nytimes.com/2026/05/11/us/politics/google-hackers-attack-ai.html)

---

**[Students boo commencement speaker after she calls AI next industrial revolution](https://news.ycombinator.com/item?id=48096674)**

A commencement speaker at the University of Central Florida was booed, with graduating humanities students yelling out, "AI SUCKS!"

⬆️ 156 • 💬 190 • 14h ago • [404 Media](https://www.404media.co/ucf-ai-commencement-speaker-booed/)

---

---

## YouTube Videos: "ai"

**[AI is Sending People into Psychosis](https://www.youtube.com/watch?v=LxmIIYj5FQE)**

AI chatbots are pulling people into delusions with devastating consequences. Sources: The Dark Addiction Patterns of Current AI ...

📺 Vanessa Wingårdh

👁️ 121K • 👍 8K • 💬 3K • ⏱️ 15:05 • 1d ago

---

**[AI layoffs are here. This is how you keep your job.](https://www.youtube.com/watch?v=JgVBqcqUGE0)**

If you're an AI contrarian at your company, resign. Become a member to gain access to the member-only video library!

📺 Mo Bitar

👁️ 103K • 👍 9K • 💬 1K • ⏱️ 6:12 • 17h ago

---

**[&quot;Three Times BIGGER Than Manhattan&quot; - MEGA AI Data Center Sparks Tech War With Americans](https://www.youtube.com/watch?v=KZyAO-uYJg0)**

Patrick Bet-David covers Utah residents revolting against Kevin O'Leary's 40000‑acre AI data center that's three times the size of ...

📺 Valuetainment

👁️ 56K • 👍 1K • 💬 551 • ⏱️ 16:53 • 11h ago

---

**[The MOST INSANE AI Video Yet? 🤖 Robot &amp; Mannequin Love Story in a Zombie Apocalypse! (AIGC)](https://www.youtube.com/watch?v=lfmQrAi4Hq8)**

The MOST INSANE AI Video Yet? Robot & Mannequin Love Story in a Zombie Apocalypse! (AIGC) Is this the best AI-generated ...

📺 What If Wildlife

👁️ 3K • 👍 117 • 💬 17 • ⏱️ 3:34 • 22h ago

---

**[When Two AIs Go To War: A Realistic Scenario](https://www.youtube.com/watch?v=gwfCWDO4LbM)**

This is a scenario, but here are the sources for the real research referenced: ...

📺 Species | Documenting AGI

👁️ 113K • 👍 6K • 💬 1K • ⏱️ 35:15 • 2d ago

---

**[Can I Animate Better Than The World&#39;s Best AI?](https://www.youtube.com/watch?v=_NXVATqxxxs)**

Go to https://buyraycon.com/bunayeopen to get 15% off. Thanks to Raycon for sponsoring! In this video, I finish a Jujutsu Kaisen ...

📺 Bunaye

👁️ 43K • 👍 3K • 💬 459 • ⏱️ 18:37 • 8h ago

---

**[Which Bed Would You Choose for a Dreamy Sleep? 🛏️✨ AI ASMR](https://www.youtube.com/watch?v=cSyLFn_R3Oo)**

Which Bed Would You Choose for a Dreamy Sleep? 🛏️✨ AI ASMR Relax and unwind after a long day with this dreamy AI ...

📺 PeaceHubASMR

👁️ 267K • 👍 272 • 💬 6 • ⏱️ 2:26 • 1d ago

---

**[Why You Should Bet On Local AI Fine-Tuning](https://www.youtube.com/watch?v=rOOhe1_ZfD0)**

Get my FREE local AI projects: https://zenvanriel.com/open-source ⚡ Become a high-earning AI engineer: ...

📺 Zen van Riel

👁️ 3K • 👍 102 • 💬 7 • ⏱️ 6:53 • 18h ago

---

**[Self-building AI, job cuts &amp; more | AI roundup](https://www.youtube.com/watch?v=FAyfVZB-3MY)**

AI is accelerating fast — and the consequences are already here. From self-building 'recursive' AI systems to Iran's AI propaganda ...

📺 CNN

👁️ 86K • 👍 1K • 💬 516 • ⏱️ 23:44 • 2d ago

---

**[Anthropic Situation Just Got Even More INSANE](https://www.youtube.com/watch?v=Pf7Y6Tu-Pzc)**

Anthropic just entered one of the strangest moments in AI. Claude is suddenly tied to SpaceX compute, Google Cloud, Amazon, ...

📺 AI Revolution

👁️ 67K • 👍 2K • 💬 170 • ⏱️ 17:08 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 157,648 • ❤️ 652 • 3d ago

---

**[ZAYA1-8B](https://huggingface.co/Zyphra/ZAYA1-8B)**

*Zyphra*

ZAYA1-8B is an efficient Mixture-of-Experts LLM (760M active params) excelling in mathematical and coding tasks, competitive with larger models. It's suitable for on-device deployment and high-performance inference.

`8.8B`

⬇️ 66,119 • ❤️ 429 • 8h ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 2,017,835 • ❤️ 3,863 • 6d ago

---

**[MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)**

*OpenBMB*

MiniCPM-V 4.6 is an ultra-efficient, pocket-sized multimodal LLM for edge deployment, excelling in image and video understanding with mixed visual token compression. It offers strong multimodal capabilities comparable to larger models while achieving superior computational efficiency and broad mobile platform support.

`image-text-to-text` `1.3B`

⬇️ 0 • ❤️ 302 • 6m ago

---

**[HiDream-O1-Image](https://huggingface.co/HiDream-ai/HiDream-O1-Image)**

*HiDream.ai*

HiDream-O1-Image is a unified transformer-based image generation model capable of text-to-image, image editing, and subject-driven personalization at resolutions up to 2048x2048. It features a pixel-level unified transformer architecture without external VAEs or disjoint text encoders, enabling high-fidelity generation and precise control.

`image-text-to-image` `8.8B`

⬇️ 3,418 • ❤️ 250 • 2d ago

---

**[gemma-4-31B-it-assistant](https://huggingface.co/google/gemma-4-31B-it-assistant)**

*Google*

Gemma 4 31B Dense is a multimodal LLM from Google DeepMind supporting text and image inputs with a 256K context window. It excels at reasoning, coding, and agentic tasks, offering optimized performance for low-latency applications via speculative decoding.

`any-to-any` `469.5M`

⬇️ 66,561 • ❤️ 211 • 22h ago

---

**[Z-Anime](https://huggingface.co/SeeSee21/Z-Anime)**

*Sebastian Böhnke*

Z-Anime is a text-to-image diffusion model, fully fine-tuned on the Z-Image Base for generating high-quality, diverse anime-style visuals. It offers multiple variants optimized for speed, quality, and low-resource environments, supporting natural language prompts and full negative prompt capabilities.

`text-to-image` `6.2B`

⬇️ 9,477 • ❤️ 311 • 15d ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 190,993 • ❤️ 1,416 • 19d ago

---

**[LTX2.3-10Eros](https://huggingface.co/TenStrip/LTX2.3-10Eros)**

*TenStrip*

LTX2.3-10Eros is a video generation model optimized for Image-to-Video (I2V) tasks, utilizing layer-scaled merges for enhanced prompt adherence and visual fidelity. It requires detailed, commanded input for motion, evolution, and audio, making it suitable for users needing precise control over generated video content, especially when combined with prompt enhancement techniques.

`image-to-video`

⬇️ 64,008 • ❤️ 224 • 1d ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 2,446,478 • ❤️ 1,243 • 18d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 64 • 💬 3 • ⭐ 73,987 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://huggingface.co/papers/2512.10971)**

*Tianyu Fan, Yuhao Yang, Yangqin Jiang et al. (6 authors)*

AI-Trader presents the first fully automated live benchmark for evaluating large language models in financial decision-making across multiple markets with autonomous information processing.

▲ 5 • 💬 0 • ⭐ 16,116 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10971) • [💻 code](https://github.com/HKUDS/AI-Trader) • [🔗 project](https://ai4trade.ai/)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 18 • 💬 3 • ⭐ 10,954 • 24d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[DFlash: Block Diffusion for Flash Speculative Decoding](https://huggingface.co/papers/2602.06036)**

*Jian Chen, Yesheng Liang, Zhijian Liu*

🏢 Z Lab

DFlash is a speculative decoding framework that uses a lightweight block diffusion model for parallel token drafting, achieving significant speedup over existing autoregressive methods while maintaining high-quality outputs.

▲ 79 • 💬 7 • ⭐ 4,401 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.06036) • [💻 code](https://github.com/z-lab/dflash) • [🔗 project](https://z-lab.ai/projects/dflash/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 32 • 💬 3 • ⭐ 23,992 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Adam's Law: Textual Frequency Law on Large Language Models](https://huggingface.co/papers/2604.02176)**

*Hongyuan Adam Lu, Z. L., Victor Wei et al. (8 authors)*

🏢 FaceMind

A novel framework for improving large language model performance through textual frequency analysis, including laws, distillation, and curriculum training approaches.

▲ 501 • 💬 9 • ⭐ 1,297 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.02176) • [💻 code](https://github.com/HongyuanLuke/frequencylaw)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 107 • 💬 10 • ⭐ 8,890 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[Flow-OPD: On-Policy Distillation for Flow Matching Models](https://huggingface.co/papers/2605.08063)**

*Zhen Fang, Wenxuan Huang, Yu Zeng et al. (11 authors)*

Flow-OPD addresses limitations in Flow Matching text-to-image models through a two-stage alignment approach combining on-policy distillation and manifold anchor regularization, achieving significant improvements in generation quality and alignment metrics.

▲ 81 • 💬 1 • ⭐ 80 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2605.08063) • [💻 code](https://github.com/CostaliyA/Flow-OPD) • [🔗 project](https://costaliya.github.io/Flow-OPD/)

---

**[HumanNet: Scaling Human-centric Video Learning to One Million Hours](https://huggingface.co/papers/2605.06747)**

*Yufan Deng, Daquan Zhou*

HumanNet presents a large-scale human-centric video dataset with rich annotations for embodied intelligence, demonstrating that egocentric human video can effectively replace robot data for training vision-language-action models.

▲ 41 • 💬 1 • ⭐ 69 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2605.06747) • [💻 code](https://github.com/DAGroup-PKU/HumanNet) • [🔗 project](https://dagroup-pku.github.io/HumanNet/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 54 • 💬 1 • ⭐ 79,686 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

---

## GitHub Repositories: "ai"

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 12.5k • 🔱 2.9k • 14d ago

---

**[h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura)**

The headless browser for AI agents and web scraping

`Rust`

⭐ 11.8k • 🔱 767 • 1d ago

---

**[getagentseal/codeburn](https://github.com/getagentseal/codeburn)**

See where your AI coding tokens go. Interactive TUI dashboard for Claude Code, Codex, and Cursor cost observability.

`TypeScript` `ai-coding` `claude-code` `cli` `codex` `cost-tracking`

⭐ 6.2k • 🔱 470 • 1h ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 2.8k • 🔱 807 • 1h ago

---

**[Manavarya09/design-extract](https://github.com/Manavarya09/design-extract)**

Extract any website's complete design system with one command. DTCG tokens, semantic+primitive+composite, MCP server for Claude Code/Cursor/Windsurf, multi-platform emitters (iOS SwiftUI, Android Compose, Flutter, WordPress), Tailwind v4, Figma variables, shadcn/ui, CSS health audit, WCAG remediation, Chrome extension. MIT, Playwright, Node 20+.

`JavaScript` `accessibility` `agent-skill` `ai` `chrome-extension` `claude-code-plugin`

⭐ 2.5k • 🔱 226 • 1d ago

---

**[earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad)**

Open source CAD skills and harnesses for generating 3D models with your favorite coding agent

`JavaScript` `3mf` `agents` `ai` `ai-agents` `build123d`

⭐ 2.4k • 🔱 284 • 8h ago

---

**[crynta/terax-ai](https://github.com/crynta/terax-ai)**

Lightweight (7MB) AI terminal emulator (ADE) built in Rust & Tauri & React

`TypeScript` `agents` `ai` `code-editor` `linux` `macos`

⭐ 2.2k • 🔱 225 • 11h ago

---

**[cosmicstack-labs/mercury-agent](https://github.com/cosmicstack-labs/mercury-agent)**

Soul-driven AI agent with permission-hardened tools, token budgets, and multi-channel access. Runs 24/7 from CLI or Telegram.

`TypeScript` `ai-agent` `ai-assistant` `llm`

⭐ 2.1k • 🔱 218 • 1d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.0k • 🔱 128 • 1h ago

---

**[bergside/design-md-chrome](https://github.com/bergside/design-md-chrome)**

Chrome extension to extract styles from any website and generate DESIGN.md files and design skills for AI based on TypeUI

`JavaScript` `ai` `chrome` `chrome-extension` `claude` `claude-design`

⭐ 1.9k • 🔱 240 • 17d ago

---

---

*Generated by PeekDeck - A glance is all you need*
