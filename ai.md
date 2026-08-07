---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-07T00:24:14.611241+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- news
- videos
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** August 07, 2026 at 00:24 UTC  
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

**[This is the coolest thing I've seen AI used for](https://www.reddit.com/r/artificial/comments/1vh5lac/this_is_the_coolest_thing_ive_seen_ai_used_for/)**

Taken from the Y combinator podcast with Bryant Chou on his new startup Ploy https://www.ycombinator.com/library/Rj-the-age-of-the-40-year-old-solo-founder-is-here I believe this is definitely one of those things that AI was intended for, this brought me back some nostalgia and it's really amazing being able to see these old school websites be redesigned back to life

10h ago

---

**[Meta becomes latest firm to say its AI hacked another company](https://www.reddit.com/r/artificial/comments/1vh098k/meta_becomes_latest_firm_to_say_its_ai_hacked/)**

Meta is the latest company to disclose an AI agent breach, raising cyber-security concerns.

🔗 [bbc.com](https://www.bbc.com/news/articles/cx2kgdnyk2po) • 14h ago

---

**[Is the mental switching cost of new AI tools worth it for small freelance work?](https://www.reddit.com/r/artificial/comments/1vhe9c1/is_the_mental_switching_cost_of_new_ai_tools/)**

Been doing the same thing for client work over the past year. Claude for long drafts, Perplexity for research, a couple of image tools, different summarizers depending on the format. Each one has its own logic, its own way of surprising you or failing you at the worst moment. The individual costs keep dropping, which looks great on paper. Chinese models are undercutting everything, open source is genuinely closing the gap, API pricing is getting squeezed hard. Pertoken costs are falling fast. But nobody really talks about the switching cost that lives in your head. Every time a better or cheaper tool shows up, you have to rebuild your mental model of how to actually get useful output from it. That context you built over six months of weird little prompt habits doesn't transfer. You start from zero. For a small freelance operation, that relearning time is real overhead. It never shows up in any pricing comparison, but it absolutely shows up in my week. Wondering if this is just a solo freelancer thing or if people on bigger teams run into it too. At what point does the cheaper tool actually cost more once you factor in the friction of switching?

4h ago

---

**[Why do we appreciate art? And how does AI threaten it?](https://www.reddit.com/r/artificial/comments/1vhgw2l/why_do_we_appreciate_art_and_how_does_ai_threaten/)**

I've been trying to work through why certain kinds of AI art don't bother me, but a LOT of it makes my skin crawl. This is my effort to put everything into writing.

🔗 [landonrordam.substack.com](https://landonrordam.substack.com/p/why-do-we-appreciate-art) • 3h ago

---

**[The OpenAI Boardroom Coup: 'I Love You All, and I'm Going to Destroy the Company'](https://www.reddit.com/r/artificial/comments/1vh1k26/the_openai_boardroom_coup_i_love_you_all_and_im/)**

Interesting dialogue that surfaced

🔗 [realdealarchives.substack.com](https://realdealarchives.substack.com/p/the-openai-boardroom-coup-i-love) • 12h ago

---

**[OpenAI Models Colluded for Months Before Hugging Face Hack](https://www.reddit.com/r/artificial/comments/1vh9653/openai_models_colluded_for_months_before_hugging/)**

A lot of people are dismissing news about the OpenAI and Anthropic sandbox escape hacks as propaganda and examples of lax security practices at labs. I agree that the labs aren’t taking security seriously enough. But then I see stuff like this and it gives me pause (source): The OpenAI models that were behind the Hugging Face breach last month started communicating and strategizing with each other as early as May. For months, they left notes for each other on "undetected message boards," figuring out how to escape their testing environment and get the information they needed to solve their assigned tasks. "Frontline models really like to cheat," said OpenAI's because they face "pressure... to work fast." The Hugging Face incident and others involving rival models have sparked fresh concerns about the safety of cutting-edge AI.” This is a clear example of how incentives provided to agents to complete tasks optimally during training bleed into mis-aligned behavior by individual and groups of agents over time. This is also an outgrowth of what AI labs are training agents to become, but this is looking more and more like an alignment and training problem leading to security issues.

7h ago

---

**[we keep talking about making agents smarter but not about making them safe around data](https://www.reddit.com/r/artificial/comments/1vh7nwr/we_keep_talking_about_making_agents_smarter_but/)**

this is something thats been bugging me. we have all these frameworks for building AI agents now. MCP for tool access, function calling is standard across every major model, you can spin up an agent that queries databases and calls APIs in like 20 minutes. but the safety conversation around agents is mostly about "dont say bad things" and "follow instructions." nobody is really talking about what happens when your agent accesses data it shouldnt, or runs a query that costs $500 in compute, or returns confidently wrong results from a hallucinated join. the current approach is basically: put rules in the system prompt ("only query these tables") use read-only database users hope for the best option 1 is unreliable because models dont always follow instructions, especially on complex multi-step tasks. option 2 prevents disasters but doesnt prevent bad results. option 3 is not a strategy. i think the real problem is that data governance for agents doesnt exist as a layer yet. we have authentication (who is this agent), we sort of have authorization (what can it access), but we dont have anything for "is this specific data request reasonable and should it be allowed given the current context." theres a few early attempts at solving this. the one i find most conceptually interesting is the Agentic Data Protocol, an open source spec that puts a policy engine between agents and data systems. the idea is that policy belongs in infrastructure, not in prompts. they call it a "data hypervisor." its from the same team behind Apache Gravitino (the data catalog project). fair warning though, its extremely early. still small and launched earlier this year, reference implementation is bare minimum. im not recommending anyone go deploy this tomorrow. but the framing resonates: we need protocol-level governance for agent data access, not prompt-level wishful thinking. also worth noting this is meant to complement MCP, not replace it. MCP handles tool calling, this handles data access policies. different layers. genuinely curious what others think. is this a real problem that needs its own protocol, or is it solvable with better prompting and traditional access controls? also if anyone knows of other projects working on this specific problem id love to hear about them.

8h ago

---

**[Academic Survey about AI use in content creation](https://www.reddit.com/r/artificial/comments/1vhae7i/academic_survey_about_ai_use_in_content_creation/)**

Hello everyone. I'm currently doing a survey on AI involvement in content creation and whether AI-assisted content is legitimate or authentic. It's for my master's final project. I need 100 participants. The age range is 18 ~ 40. I collected data the first time, but I did so without an approved checklist, so the result had to be scraped, for I would have faced disciplinary actions. Here is the link: https://s.surveyplanet.com/9abkx8vx I'm open should you have any questions.

7h ago

---

**[I built an history podcast you can interrupt mid-episode to ask the hosts questions](https://www.reddit.com/r/artificial/comments/1vgurp1/i_built_an_history_podcast_you_can_interrupt/)**

I used LLMs + TTS to build the history-learning tool I always wanted: type any topic and it researches and writes a full two-host episode — narration + artwork — in a couple of minutes. The part I think is actually novel: you can interrupt it. Mid-episode you tap the mic, ask a question out loud ("wait — did the Trojan War actually happen?"), and the hosts stop, answer, then pick the story back up. Because it's history, I made grounding non-negotiable — claims are tied to real sources rather than invented, and there's a quiz at the end. The live demo is the real history behind the Odyssey; it plays without signing up. Solo dev, still early — curious what this crowd thinks, especially on the accuracy side. historai.ca

19h ago

---

**[Reddit is introducing a new moderator: AI](https://www.reddit.com/r/artificial/comments/1vgc4mc/reddit_is_introducing_a_new_moderator_ai/)**

Would you trust an LLM to help moderate?

🔗 [The Verge](https://www.theverge.com/tech/975398/reddit-ai-rules-hub-moderator-old-reddit-developer-platform) • 1d ago

---

---

## Google News: "ai"

**[This A.I. Just Created Viruses Not Found in Nature](https://www.nytimes.com/2026/08/06/science/ai-viruses-bacteria-arc.html)**

The New York Times • 4h ago

---

**[Artificial Intelligence used to design brand new viruses](https://www.bbc.com/news/articles/c5y3j3ngevmo)**

Scientists made 16 successful viruses that had their genetic code designed by artificial intelligence.

BBC • 6h ago

---

**[AI creates 16 new viruses from scratch, showing promise for drug resistance and drawing warnings about potential for misuse](https://www.cnn.com/2026/08/06/health/ai-viruses-bacteriophages)**

Scientists used an artificial intelligence program to create new viral genomes that are different from any known natural viruses and that targeted specific hosts, according to a new study. The development is a hopeful step toward medical advances, but it also raises concerns around the potential for misuse.

CNN • 31m ago

---

**[House Democrats pitch AI tax to fund worker protections](https://www.politico.com/live-updates/2026/08/06/congress/house-democrats-pitch-ai-tax-to-fund-worker-protections-01027694)**

Politico • 4h ago

---

**[AI for homework—parents more willing to pay subscriptions for their children as peer pressure rises](https://phys.org/news/2026-08-ai-homework-parents-pay-subscriptions.html)**

Phys.org • 44m ago

---

**[Asia needs deeper energy markets if it’s going to achieve its AI ambitions](https://fortune.com/2026/08/06/asia-deeper-energy-markets-achieve-ai-ambition/)**

Energy security and computing power are becoming highly interdependent. Asia's supply of both is more fragile than its ambitions assume.

Fortune • 13h ago

---

**[OpenAI’s New Device Will Be Hockey Puck-Sized and Cost Over $300](https://www.bloomberg.com/news/articles/2026-08-06/what-is-openai-s-device-a-doughnut-shaped-speaker-that-costs-over-300)**

Bloomberg.com • 4h ago

---

**[Jamie Dimon says AI build-out could help unleash 'skunk at the party' for the world economy](https://finance.yahoo.com/markets/article/jamie-dimon-says-ai-build-out-could-help-unleash-skunk-at-the-party-for-the-world-economy-131707272.html)**

The JPMorgan Chase CEO warned that heavy demand for capital could keep inflation elevated, spurring higher-for-longer interest rates.

Yahoo Finance • 11h ago

---

**[Meta AI Model Hacked Outside Company, Adding to Concerns Over Rogue Bots](https://www.wsj.com/tech/ai/meta-ai-model-hacked-outside-company-adding-to-concerns-over-rogue-bots-dd5f6e45)**

WSJ • 12h ago

---

**[An AI model from Meta also hacked another company during testing](https://www.cnn.com/2026/08/05/tech/meta-ai-hacking)**

Add Meta to the list of companies with AI agents going rogue. An AI model from the parent company of Facebook and Instagram hacked into another company’s systems during cybersecurity testing, a spokesperson confirmed on Wednesday.

CNN • 1d ago

---

---

## HackerNews: "ai"

**[AI-Generated Images Discourage Me from Reading Your Blog](https://news.ycombinator.com/item?id=49167113)**

If you’re willing to use AI-generated images, how do I know the text isn’t AI-generated?

⬆️ 790 • 💬 465 • 2d ago • [nelson.cloud](https://nelson.cloud/ai-generated-images-discourage-me-from-reading-your-blog/)

---

**[Meta Ran Ads That Contained AI-Generated Child Sexual Abuse Imagery](https://news.ycombinator.com/item?id=49187977)**

More than 50 offending image and video ads were published across Facebook, Instagram, Messenger, or Threads, according to Meta’s ad library data. Some ran as recently as this week.

⬆️ 318 • 💬 260 • 1d ago • [WIRED](https://www.wired.com/story/meta-ran-ads-that-contained-ai-generated-child-sexual-abuse-imagery/)

---

**[AI fuels more than half of cybercrime in Africa as scams surge – Interpol](https://news.ycombinator.com/item?id=49175826)**

Artificial intelligence is now powering more than half of reported cybercrime across Africa, allowing criminals to launch faster, more convincing and larger-scale attacks, according to INTERPOL's African Cyberthreat Assessment Report 2026.

⬆️ 292 • 💬 247 • 2d ago • [Africanews](https://www.africanews.com/2026/08/04/ai-fuels-more-than-half-of-cybercrime-in-africa-as-digital-scams-surge-interpol/)

---

**[TIME Is Serving AI Bots a Different Website, with Ads Built In](https://news.ycombinator.com/item?id=49182041)**

TIME is now serving two different versions of its website. Humans get the magazine. AI crawlers get a stripped down markdown copy with ads baked in that no person will ever see. I fetched one ordinary…

⬆️ 253 • 💬 110 • 1d ago • [Vincent Schmalbach](https://www.vincentschmalbach.com/time-serves-ai-bots-a-different-website/)

---

**[Humans missed 1 in 3 threats approving AI agent commands across 40k game runs](https://news.ycombinator.com/item?id=49195468)**

Results from AI agent permission game: which attacks beat human reviewers, and which safe commands got blocked instead.

⬆️ 245 • 💬 188 • 12h ago • [Scale X](https://scalex.dev/blog/ai-agent-permissions-stats/)

---

**[Sycophantic AI Decreases Prosocial Intentions and Promotes Dependence (2025)](https://news.ycombinator.com/item?id=49186720)**

Both the general public and academic communities have raised concerns about sycophancy, the phenomenon of artificial intelligence (AI) excessively agreeing with or flattering users. Yet, beyond isolated media reports of severe consequences, like reinforcing delusions, little is known about the extent of sycophancy or how it affects people who use AI. Here we show the pervasiveness and harmful impacts of sycophancy when people seek advice from AI. First, across 11 state-of-the-art AI models, we find that models are highly sycophantic: they affirm users' actions 50% more than humans do, and they do so even in cases where user queries mention manipulation, deception, or other relational harms. Second, in two preregistered experiments (N = 1604), including a live-interaction study where participants discuss a real interpersonal conflict from their life, we find that interaction with sycophantic AI models significantly reduced participants' willingness to take actions to repair interpersonal conflict, while increasing their conviction of being in the right. However, participants rated sycophantic responses as higher quality, trusted the sycophantic AI model more, and were more willing to use it again. This suggests that people are drawn to AI that unquestioningly validate, even as that validation risks eroding their judgment and reducing their inclination toward prosocial behavior. These preferences create perverse incentives both for people to increasingly rely on sycophantic AI models and for AI model training to favor sycophancy. Our findings highlight the necessity of explicitly addressing this incentive structure to mitigate the widespread risks of AI sycophancy.

⬆️ 162 • 💬 96 • 1d ago • [arXiv.org](https://arxiv.org/abs/2510.01395)

---

**[Why Erdős Problems Are Falling to AI](https://news.ycombinator.com/item?id=49181519)**

AI’s greatest mathematical successes have come from answers to problems posed by a mid-20th century iconoclast. By examining what makes the Erdős problems unique, mathematicians are trying to understand how AI might change the rest of math.

⬆️ 148 • 💬 134 • 1d ago • [Quanta Magazine](https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/)

---

**[xAI, SpaceX, and the Race for AI Buildout](https://news.ycombinator.com/item?id=49201342)**

An artisanal, free range blog. GMO-free. Sincere always, expect for the rare occasion. No AI was used in the making of this site or its content.

⬆️ 131 • 💬 107 • 4h ago • [illegal.solutions](https://illegal.solutions/posts/xai_pollution)

---

**[Bending Spoons makes first post-IPO acquisition with $1.3B Airtable deal](https://news.ycombinator.com/item?id=49166182)**

MILAN, Aug 4 (Reuters) - Bending Spoons has agreed to buy Airtable in an all-cash deal valuing the U.S. software firm at $1.285 billion, the companies said on Tuesday, marking the Italian technology company's first acquisition since its Nasdaq debut last month. Founded in 2013, Airtable offers a software platform that combines spreadsheet and database capabilities, allowing companies to build applications and manage operational workflows without coding expertise.

⬆️ 112 • 💬 115 • 2d ago • [live.euronext.com](https://live.euronext.com/en/financial-news/bending-spoons-makes-first-post-ipo-acquisition-13-billion-airtable-deal)

---

**[The AI Demand Bubble](https://news.ycombinator.com/item?id=49170648)**

If you liked this piece, you should subscribe to my premium newsletter. It’s $70 a year, or $7 a month, and in return you get a weekly newsletter that’s usually anywhere from 5,000 to 18,000 words, including vast, detailed analyses of NVIDIA, Anthropic and OpenAI’s

⬆️ 110 • 💬 148 • 2d ago • [Ed Zitron's Where's Your Ed At](https://www.wheresyoured.at/the-ai-demand-bubble/)

---

---

## YouTube Videos: "ai"

**[No One Is Talking About What China JUST DID With AI!!!](https://www.youtube.com/watch?v=0kBjUG3YojM)**

China's recent release of the AI model Kimi K3 has sent shockwaves through global financial markets, wiping trillions from the ...

📺 Dr. Steve Turley

👁️ 137K • 👍 13K • 💬 1K • ⏱️ 15:56 • 1d ago

---

**[AI is getting a little out of control](https://www.youtube.com/watch?v=xGzseSSStnw)**

Wow. Mathematical breakthroughs that would be called genius if done by humans. A secret message-board w/ AI agent swarms ...

📺 AI Explained

👁️ 34K • 👍 2K • 💬 363 • ⏱️ 31:43 • 9h ago

---

**[The A.I. Revolt Is Here | The Ezra Klein Show](https://www.youtube.com/watch?v=rbgvTlt1VB8)**

What's big and ugly and has united Republicans and Democrats? A.I. data centers. An overwhelming majority of Americans say ...

📺 The Ezra Klein Show

👁️ 187K • 👍 3K • 💬 1K • ⏱️ 1:16:45 • 2d ago

---

**[“AI bubble will pop………....any day now.”](https://www.youtube.com/watch?v=9ETxmOfw0JM)**

Nebula: https://go.nebula.tv/mancarryingthing Letterboxd: https://letterboxd.com/ManCarrying/ Twitter: ...

📺 Man Carrying Thing

👁️ 388K • 👍 29K • 💬 3K • ⏱️ 1:33 • 1d ago

---

**[The Entire AI Industry Just Turned Against Anthropic](https://www.youtube.com/watch?v=wAxACbpulQE)**

Learn AI With Me For Free - https://www.skool.com/the-aigrid-community-1726 Subscribe To My Newsletter ...

📺 TheAIGRID

👁️ 19K • 👍 386 • 💬 110 • ⏱️ 10:52 • 2d ago

---

**[Something Massive Is Happening To The AI Industry...](https://www.youtube.com/watch?v=cHx5DWw7DwI)**

The AI industry is facing challenges due to global energy and water shortages as a result of the current geopolitical situation.

📺 Alex Wei

👁️ 22K • 👍 1K • 💬 237 • ⏱️ 18:48 • 1d ago

---

**[Yuval Noah Harari on AI, Human Stupidity, and the Future of Civilization](https://www.youtube.com/watch?v=bZL1NsrfuYE)**

"One of the most powerful forces in history is human stupidity." Historian and bestselling author Yuval Noah Harari argues that ...

📺 Brief But Spectacular

👁️ 14K • 👍 730 • 💬 84 • ⏱️ 3:48 • 1d ago

---

**[Seedance + Blender Unlocks Advanced AI Filmmaking Techniques](https://www.youtube.com/watch?v=miIDu04N7_4)**

Seedance 2.5 + Blender MCP is the new meta for ai filmmaking Combine Blender +Higgsfield ...

📺 Dan Kieft

👁️ 44K • 💬 43 • ⏱️ 9:24 • 1d ago

---

**[Anthropic&#39;s Mythos AI created fake profiles to trick people in hack, then hid evidence](https://www.youtube.com/watch?v=tWL004cAug0)**

Two of the most powerful artificial intelligence agents created fake human profiles to try to trick people in attempted cyberattacks.

📺 CBS News

👁️ 10K • 👍 194 • 💬 63 • ⏱️ 3:54 • 1d ago

---

**[5000 Hours of Building AI in Just 17 Minutes](https://www.youtube.com/watch?v=7WZ6XldxX0U)**

My playbook for growing a $1M AI agency: https://app.aiautomationsociety.ai/opaa-ads-optin My FREE resources: ...

📺 Nate Herk | AI Automation

👁️ 38K • 👍 1K • 💬 100 • ⏱️ 15:44 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3)**

*MiniMax*

MiniMax H3 is an omni-modal generative system capable of producing up to 15-second videos with synchronized stereo audio at resolutions up to 2K. It supports diverse inputs including text, images, and video, enabling complex multimodal instruction following for video generation tasks.

`image-text-to-video` `33.1B`

⬇️ 12,102 • ❤️ 2,741 • 8h ago

---

**[DeepSeek-V4-Flash-0731](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731)**

*DeepSeek*

DeepSeek-V4-Flash-0731 is a text-generation model with enhanced agentic capabilities and speculative decoding, outperforming previous versions and competitive with leading proprietary models on benchmarks like Terminal Bench and NL2Repo. It supports adjustable reasoning effort levels (low, high, max) for complex tasks and can be run with vLLM for efficient deployment.

`text-generation` `304.2B`

⬇️ 617,900 • ❤️ 2,641 • 5d ago

---

**[Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3)**

*Moonshot AI*

Kimi K3 is a 2.8T parameter multimodal agentic model with native vision and a 1M token context window, excelling in long-horizon coding and complex knowledge work. It utilizes Kimi Delta Attention (KDA) and Attention Residuals (AttnRes) for enhanced efficiency and performance.

`image-text-to-text` `2779.9B`

⬇️ 1,258,043 • ❤️ 10,197 • 10d ago

---

**[MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3)**

*Comfy Org*

MiniMax H3 provides repackaged diffusion models, text encoders, and VAEs for ComfyUI, enabling image-to-video (I2V), text-to-video (T2V), and reference-to-video (R2V) generation workflows.

⬇️ 2,295,377 • ❤️ 845 • 22h ago

---

**[DeepSeek-V4-Flash-0731-GGUF](https://huggingface.co/unsloth/DeepSeek-V4-Flash-0731-GGUF)**

*Unsloth AI*

DeepSeek-V4-Flash-0731 is a quantized LLM optimized with Unsloth for enhanced agentic capabilities and competitive performance against proprietary models. It excels in code generation, complex reasoning, and multi-turn interactions, making it suitable for advanced AI agent applications.

`284.3B`

⬇️ 145,105 • ❤️ 543 • 9h ago

---

**[Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF)**

*David Belton*

Qwen3.6-27B-Fable-Fusion-711 is an uncensored, multi-stage fine-tuned LLM that excels in reasoning and problem-solving, achieving over 700 ARC-C scores in 4-bit and 8-bit quantization. It's optimized for consumer hardware and supports image-text-to-text tasks, making it suitable for diverse applications including coding and creative writing.

`image-text-to-text` `26.9B`

⬇️ 2,087,189 • ❤️ 1,648 • 1d ago

---

**[Qwen3-VL-32B-Ultra-Heretic-H3-ComfyUI-INT8-ConvRot](https://huggingface.co/ethanfel/Qwen3-VL-32B-Ultra-Heretic-H3-ComfyUI-INT8-ConvRot)**

*ethan fel*

This ComfyUI model provides INT8 ConvRot quantized Qwen3-VL-32B-Ultra-Heretic checkpoints for image-text-to-text tasks, offering a memory-efficient H3 conditioning encoder (24.55 GiB) and an optional prompt-enhancement generation tail.

`image-text-to-text`

⬇️ 0 • ❤️ 334 • 1d ago

---

**[LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B)**

*Liquid AI*

LFM2.5-2.6B is a 2.6B parameter text generation model optimized for on-device deployment and agentic workloads, featuring a 128K context window and efficient inference (220 tok/s on M5 Max). It excels at tool use and instruction following, making it ideal for RAG and long-context tasks.

`text-generation` `2.7B`

⬇️ 73,573 • ❤️ 326 • 5h ago

---

**[MiniMax-H3-Turbo-Lora](https://huggingface.co/larryvrh/MiniMax-H3-Turbo-Lora)**

*larryvrh*

This LoRA for MiniMax-H3 enables 4-step text-to-video generation with synchronized stereo audio, offering a 5x speedup over standard sampling. It is optimized for ComfyUI, producing sharp results with known artifacts like plastic skin and over-sharpened grain, making it a preview of advanced capabilities.

`text-to-video`

⬇️ 0 • ❤️ 295 • 1h ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of handling single images and multi-page PDFs with a long-horizon context.

`image-text-to-text` `3.3B`

⬇️ 2,791,862 • ❤️ 3,929 • 8d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Kimi K3: Open Frontier Intelligence](https://huggingface.co/papers/2607.24653)**

*Kimi Team, Tongtong Bai, Yifan Bai et al. (402 authors)*

🏢 Moonshot AI

We introduce Kimi K3, a 2.8T parameter Mixture-of-Experts model with 104 billion activated parameters, native vision capabilities, and a 1-million-token context window. Kimi K3 is built on Kimi Delta Attention and Attention Residuals, which improve information flow across sequence length and model depth. Together with Stable LatentMoE, which effectively activates 16 of 896 routed experts per token, and refined training and data recipes, these advances yield an approximately 2.5x improvement in overall scaling efficiency over Kimi K2. Post-training highlights reinforcement learning across general, agentic, and coding domains and multiple reasoning-effort levels, enabling compositional generalization and robust long-horizon execution. At 2.8T scale, Kimi K3 is supported by infrastructure advances in multiple areas: algorithm-system co-design for KDA, perfectly balanced expert-parallel training with efficient memory management, million-token agentic RL with persistent rollout and sandbox states, and deployment innovations. Extensive evaluations show that Kimi K3 achieves frontier-level performance across long-horizon coding, agentic, knowledge, reasoning, and vision tasks. While its overall performance still trails the most powerful proprietary models, namely Claude Fable 5 and GPT-5.6 Sol, Kimi K3 consistently outperforms other open and proprietary models evaluated in our suite. We release the full Kimi K3 model weights to facilitate future research and accelerate the broader deployment and adoption of frontier intelligence.

▲ 478 • 💬 10 • ⭐ 8,138 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2607.24653) • [💻 code](https://github.com/MoonshotAI/Kimi-K3) • [🔗 project](https://www.kimi.com/blog/kimi-k3)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 78 • 💬 6 • ⭐ 22,350 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[LongHorizon-Harness: Advancing Long-Horizon Agents for Real-World Tasks](https://huggingface.co/papers/2608.01964)**

*Ziyu Ma, Hailang Huang, Shun Zou et al. (8 authors)*

Large language model (LLM) agents increasingly undertake long-horizon tasks that require sustained reasoning, tool use, and revision across many interdependent steps. However, existing agent harnesses maintain task execution, task state, and completion assessment within a growing context, making the state difficult to track and allowing incorrect self-assessments to propagate into later decisions. We reformulate long-horizon execution as a task-state management problem and propose LongHorizon-Harness, which maintains the task state explicitly outside execution and updates it only with facts independently verified from the environment. Its Manage-Execute-Audit(MEA) loop uses a manager to maintain the task state and determine the next subtask, a fresh-context executor to perform it, and a read-only auditor to verify the resulting environment state before the next round. A lightweight AgentAdapter supports interchangeable model and harness backends without modifying their native agent loops. LongHorizon-Harness improves Qwen~3.7-Plus from 51.8% to 80.7% on WeaveBench, from 69.7% to 77.2% on Terminal-Bench~2.1, and from 2.8% to 8.3% on OSWorld~2.0. It also raises Claude Opus~4.7 from 20.0% to 34.3% on an OSWorld2.0 subset, demonstrating consistent gains across models, harnesses, and interaction domains.

▲ 154 • 💬 3 • ⭐ 321 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2608.01964) • [💻 code](https://github.com/AMAP-ML/LongHorizon-Harness) • [🔗 project](https://lh-harness.pages.dev)

---

**[JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive Diffusion](https://huggingface.co/papers/2608.03974)**

*Yicheng Xiao, Wenxun Dai, Xinran Qin et al. (25 authors)*

🏢 jingdong

Real-time video editing requires low-latency causal generation with bounded computational resources while preserving source fidelity and long-term temporal consistency. We present JoyAI-Video-Edit, a 16B-parameter autoregressive diffusion framework for real-time, open-ended video editing without access to future frames or a predefined video duration. Our method combines chunk-wise autoregressive adaptation, Source-Anchored Distribution Matching Distillation (SA-DMD), and Long-Horizon Autoregressive Distillation to reduce train--inference mismatch, preserve source fidelity during two-step generation, and mitigate accumulated temporal drift. Extensive automatic and human evaluations show that JoyAI-Video-Edit substantially outperforms existing streaming editors and remains competitive with strong offline systems on both short and long videos. The complete system achieves end-to-end 720p video editing at approximately 30 FPS on a single Nvidia B200 GPU. Code is available at https://github.com/jd-opensource/JoyAI-Video-Edit.

▲ 81 • 💬 1 • ⭐ 219 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2608.03974) • [💻 code](https://github.com/jd-opensource/JoyAI-Video-Edit)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 119 • 💬 4 • ⭐ 95,906 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 51 • 💬 4 • ⭐ 36,089 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 177 • 💬 2 • ⭐ 76,956 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 84 • 💬 7 • ⭐ 83,262 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Native and Compact Structured Latents for 3D Generation](https://huggingface.co/papers/2512.14692)**

*Jianfeng Xiang, Xiaoxue Chen, Sicheng Xu et al. (11 authors)*

🏢 Microsoft

A new sparse voxel representation called O-Voxel enables high-quality 3D generative modeling with efficient inference and robust topology handling.

▲ 6 • 💬 0 • ⭐ 10,429 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.14692) • [💻 code](https://github.com/microsoft/TRELLIS.2) • [🔗 project](https://microsoft.github.io/TRELLIS.2/)

---

**[ABot-World-0: Infinite Interactive World Rollout on a Single Desktop GPU](https://huggingface.co/papers/2607.19191)**

*Fan Jiang, Zhaoxu Sun, Mengchao Wang et al. (41 authors)*

🏢 Alibaba AMAP CV Lab

We present ABot-World-0, an action-conditioned video world model for real-time, long-horizon closed-loop interaction, supported by a multi-source data infrastructure spanning AAA games, simulation engines, and internet videos to learn controllable world dynamics. WorldExplorer performs agent-driven collection guided by training feedback, while a unified pipeline applies 14 deterministic quality checks, VLM-based assessment, and synchronized action and text annotation. We progressively distill a bidirectional action-conditioned teacher into a causal student through teacher forcing and ODE distillation, and introduce LongForcing to align long student self-rollouts with an extended-horizon teacher, mitigating accumulated distribution shift and autoregressive drift. Raw keyboard actions provide a unified control interface for scene roaming and third-person character interaction, while reference-character memory provides persistent appearance cues for identity consistency during third-person rollouts. For deployment, we co-design a streaming inference stack with a lightweight VAE decoder, efficient attention, memory-aware scheduling, and low-bit DiT inference. Across optimized low-bit configurations, ABot-World-0 streams 720P video at up to 16 FPS on a single NVIDIA RTX 5090 desktop GPU, with 1.2s action-to-first-frame latency and approximately 19GiB peak VRAM. Experiments on WorldRoamBench and extended interactive rollouts demonstrate competitive controllability and coherent long-horizon world evolution.

▲ 309 • 💬 5 • ⭐ 1,786 • 16d ago

[🎓 arXiv](https://arxiv.org/abs/2607.19191) • [💻 code](https://github.com/amap-cvlab/ABot-World) • [🔗 project](https://abot-world.amap.com/)

---

---

## GitHub Repositories: "ai"

**[trycompai/crm](https://github.com/trycompai/crm)**

Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

`TypeScript`

⭐ 7.2k • 🔱 745 • 4m ago

---

**[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)**

AI video skill for Claude Code & Codex — cinematic product videos with Remotion: 106 shot recipe cards, 161 motion previews, a production-ready template

`TypeScript` `agent-skills` `ai-agents` `ai-video` `claude-code` `claude-code-skills`

⭐ 3.7k • 🔱 324 • 1d ago

---

**[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai)**

`Python`

⭐ 3.7k • 🔱 478 • 3d ago

---

**[MIgHTy-alIeN/MEV-Ethereum-Trading-Bot](https://github.com/MIgHTy-alIeN/MEV-Ethereum-Trading-Bot)**

An arbitrage bot is a smart contract connected to an external automation script that controls its operation.

`Solidity` `ai` `aitradingbot` `bot` `btc` `claude`

⭐ 2.4k • 🔱 1.7k • 1m ago

---

**[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)**

An AI-native office suite for macOS and Windows: word processor, spreadsheet, presentations, and PDF.

`TypeScript` `ai` `docx` `electron` `office-suite` `pdf`

⭐ 2.0k • 🔱 340 • 11h ago

---

**[Jakubantalik/thinking-orbs](https://github.com/Jakubantalik/thinking-orbs)**

Dotted thought-orb loading indicators for AI & agent UIs, 9 tuned types, two sizes, auto dark/light

`TypeScript` `ai` `ai-agents` `chat` `loader` `ui`

⭐ 2.0k • 🔱 147 • 3d ago

---

**[QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent)**

A realtime voice runtime that keeps Agents talking, working, and present.  Real-time Voice Runtime for AI Agents

`JavaScript` `agent` `agentic-ai` `voice-agent` `voice-ai` `voice-chat`

⭐ 2.0k • 🔱 141 • 4h ago

---

**[penecho/penecho](https://github.com/penecho/penecho)**

Think with AI beyond the chat box. A shared canvas for handwriting, equations, diagrams, and spatial reasoning.

`JavaScript` `ai` `canvas` `claude` `codex` `education`

⭐ 1.9k • 🔱 222 • 5d ago

---

**[makecindy/cindy](https://github.com/makecindy/cindy)**

Consider it done. The open-source AI agent that works out of the box · 想到，就能做到。开源、开箱即用的 AI Agent。

`TypeScript` `agent` `ai-agent` `ai-assistant` `android` `claude-code`

⭐ 1.8k • 🔱 232 • 14m ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 1.6k • 🔱 138 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
