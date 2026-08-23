---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-23T04:36:27.505656+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- news
- repositories
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** August 23, 2026 at 04:36 UTC  
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

**[GOP urges top AI firms to do something about the toxic image of data centers](https://www.reddit.com/r/artificial/comments/1vvhngn/gop_urges_top_ai_firms_to_do_something_about_the/)**

GOP urges top AI firms to do something about the toxic image of data centers - SiliconANGLE

🔗 [SiliconANGLE](https://siliconangle.com/2026/08/19/gop-urges-top-ai-firms-to-do-something-about-the-toxic-image-of-data-centers/) • 11h ago

---

**[Unpopular opinion: AI is going to hit a peak, fade into the background, and human stuff becomes the luxury item](https://www.reddit.com/r/artificial/comments/1vvh293/unpopular_opinion_ai_is_going_to_hit_a_peak_fade/)**

Remember when computers were the luxury thing? Now they’re everywhere and basically invisible but nobody’s impressed by “I own a laptop” anymore. I think AI is heading the same way. It gets so common, so good, so baked into everything that it stops being a “thing” at all. It just disappears into the background, like electricity or wifi. Nobody says “wow, AI” anymore, the same way nobody says “wow, computer.” And when that happens, the rare thing won’t be AI-made stuff. It’ll be human-made stuff. Human skill, human attention, a person who actually did the thing themselves : that becomes the flex. Not because AI can’t do it, but because AI can, and choosing the human version anyway is what makes it valuable. AI won’t keep climbing forever like it feels like now. It’ll peak, then fade into invisibility. And humans doing human things will become the new premium.

12h ago

---

**[A personalized history podcast you can interrupt to ask the questions](https://www.reddit.com/r/artificial/comments/1vvup6g/a_personalized_history_podcast_you_can_interrupt/)**

The idea came from a personal frustration: I love history but could never find podcasts on the niche topics I wanted, and when I did, my curiosity always wanted a detour the host couldn't take. So I built the tool I wanted. It's called Historai https://historai.ca/ , it generates a podcast on any topic, one or two narrators, does real research and sources its material. The core feature: you can interrupt it any time and ask a question, and the story continues after. There's also a map and period artwork alongside the audio. Free to try, no account needed for the demo. Just looking for genuine feedback, happy to answer questions about how it works. And if you like it feel fee to share it! Podcast generated from the demo video: https://historai.ca/history/how-a-song-became-the-odyssey--cd48307e4d1244e1ac98e9fcb50f7484

2h ago

---

**[Our deterministic verification engine passed 66/66 benchmark cases on canonical structured inputs.](https://www.reddit.com/r/artificial/comments/1vvucil/our_deterministic_verification_engine_passed_6666/)**

Our deterministic verification engine passed 66/66 benchmark cases on canonical structured inputs. In live model evaluation, the end-to-end pipeline currently passed 19/66 cases. We are restructuring the benchmark to isolate failures by their first invalid state and to separately measure deterministic verifier correctness, production contract integrity, and live model generation reliability. The next benchmark version will provide stage-level attribution across transport, parsing, schema validation, normalization, claim binding, evidence graph construction, deterministic verification, and final outcome mapping. https://www.reddit.com/r/ArtificialInteligence/comments/1vucc82/i_benchmarked_my_deterministic_ai_financial/

2h ago

---

**[Follow-up: VSArena now has a proper VLA track (camera + language, no privileged state) — repo and docs are public](https://www.reddit.com/r/artificial/comments/1vvlxi2/followup_vsarena_now_has_a_proper_vla_track/)**

Posted about this project a little while ago — quick update since a few things changed that address feedback from that thread. Biggest change: split the observation space properly. There's now a VLA track where the policy only gets a 128x128 RGB camera + a language stacking instruction — cube poses are never sent to the policy. Scoring still uses real poses internally to grade spatial accuracy and completion, but that's judge-only, not policy-visible. State-based (privileged poses) is kept as a separate debug track and doesn't write public ELO either — wanted the "VLA vs state" distinction to be explicit rather than something people had to dig for. On the client-side physics concern from before:Studio (the in-browser demo) is spectator/dev-only, clearly labeled, and does not post to the public leaderboard. Public ELO only comes from a hosted harness that scores server-side. That harness isn't live yet —it's the one piece standing between this and actually being open for submissions. Repo + docs are public now:https://github.com/NovaCoding-G/VSArena -docs/harness.md — scoring writeup (spatial accuracy + task completion) -docs/sdk.md — submission protocol -Studio itself:https://vsarena.vercel.app/simulation (client-side, Rapier/WASM, 60fps) Still solo, still early, still not oversell-ready — but wanted to share since the VLA/state separation was directly a response to feedback here. Open to more of that, especially on what the scoring protocol might be missing.

8h ago

---

**[Will Chinese Open Source Agree to EU Watermarking?](https://www.reddit.com/r/artificial/comments/1vvnwxp/will_chinese_open_source_agree_to_eu_watermarking/)**

I wonder if people are thinking and worried about this yet? Anthopic, OpenAI and the western AI labs have agreed to watermark AI outputs. Some of us want free and open and untracked and un-modified outputs for many reasons. Do you think the Chinese labs will succumb to the EU pressure and implement the watermarking? Will there be some that dont? Or do people not even care about this? I don't like it and if the EU makes stupid laws, or the USA or another country for that matter, the rest of the world shouldn't be affected. My hope is that the chinese labs dont add it and that they stay free and open source. What do you think?

7h ago

---

**[Made a tool to remove SynthIDs from images](https://www.reddit.com/r/artificial/comments/1vvrso7/made_a_tool_to_remove_synthids_from_images/)**

As you know, whenever you edit an image via Gemini or OpenAI, they plaster a SynthID to mark it as their own. Further, these SynthIDs can be unqiue, which could be used to track whoever made it. This SynthIDs are imposed on even paid users, and cannot be opted out of this. In response, I created this scrubber. Works on any computer with 8GB of ram. Pretty reliable, automatic, but sucks with text. Have fun.

🔗 [GitHub](https://github.com/BovineOverlord/Loyal-Bear---The-SynthID-Scrambler) • 4h ago

---

**[UBS models $4.1T in AI infrastructure spending by 2028 - it assumes the power just shows up](https://www.reddit.com/r/artificial/comments/1vvfxyq/ubs_models_41t_in_ai_infrastructure_spending_by/)**

Everyone talks about chip supply as the bottleneck on AI buildout, but power interconnection is turning into the harder constraint in several major markets, and it works nothing like a chip shortage. A chip shortage is a supply problem: fabs run flat out, backlogs clear eventually, prices come down. Grid interconnection is a queue problem: a new data center has to get in line behind every other proposed generation and load project in that region, and studies for that queue routinely take years, not quarters. You can't buy your way to the front by paying more, and you can't build your way out of it by ordering more GPUs. Three things happened just this month that show the queue problem getting worse, not better. The Tennessee Valley Authority created a rate class specifically for AI data centers, an admission that normal industrial rates and normal queue treatment don't fit this load anymore. Denmark's grid operator started putting new data center interconnection requests behind other categories of demand entirely, rather than processing them in the order they arrived. And PJM's board overruled its own stakeholder vote on curtailment rules, which tells you the fight over who gets priority access to constrained transmission capacity is now happening at the top of the largest grid operator in the US. None of this shows up in a capex forecast. $4.1 trillion assumes the megawatts show up when the money does. In a growing number of regions that assumption is the thing to watch, not the chip supply chain. Curious what people closer to the utility/regulatory side are seeing: is interconnection actually the binding constraint now, or is that overstated relative to chips and cooling?

12h ago

---

**[Possible pathways to RSI](https://www.reddit.com/r/artificial/comments/1vv8iu3/possible_pathways_to_rsi/)**

I was just wondering what could be, from this point onwards the potential pathways to undeniable RSI.. which in my opinion is precursor to singularity/ AGI. Maybe not AGI but definitely RSI. (BELOW TEXT WAS EDITED BY GEMINI) Pathway 1: Decentralized & Crowdsourced Open-Source Automation An organized, community-driven ecosystem automates the entire machine-learning pipeline, utilizing crowdsourced compute and unified project management so open-source agents gradually upgrade their own systems without human intervention. Pathway 2: The Biological & Continuous Learning Shift A shift toward biocomputing enables large-scale continuous learning, allowing models to adapt dynamically to every experience and evolve distinct personalities, goals, and drives. Pathway 3: Closed-Loop Centralized Automation (Frontier Labs) Leading labs fully automate their R&D pipelines, enabling autonomous multi-agent systems to design experiments, set benchmarks, and deploy architectural upgrades without human involvement. Pathway 4 (SUGGESTED BY AI) : Additional Potential Triggers for RSI Hardware Design Feedback Loops: - AI designs next-generation silicon and neural architectures, directly accelerating the hardware required to build its successors. - Autonomous Synthetic Data Engine: Models continuously generate pristine, edge-case training data and formal proofs, bypassing human data limits. - Dynamic Test-Time Meta-Learning: Systems self-correct and alter their runtime execution graphs in real time, achieving continuous improvement without full retraining. What do you guys think? Also while responding if you can share what field or profession you belong to it would be nice. I'm just gathering different perspectives. Thanks for reading! This is my first post here. Excuse the blunders.

18h ago

---

**[I spent the morning digging into Anthropic so I could write it up properly. The short version](https://www.reddit.com/r/artificial/comments/1vvjmmo/i_spent_the_morning_digging_into_anthropic_so_i/)**

Anthropic appears to be A/B testing reduced effort levels in Claude Code I went through the primary sources and the threads this morning so I could write it up properly, and the short version is: the hype is half right. I collect daily AI news and write guides around exactly these stories at https://apexnexus.site (free, no email wall) if you want the deeper version. The writeup on Anthropic goes up later today. What's your take on Anthropic?

10h ago

---

---

## Google News: "ai"

**[Nvidia Customers Notified About AI-Related Price Hikes Above 15%](https://www.bloomberg.com/news/articles/2026-08-22/nvidia-customers-notified-about-ai-related-price-hikes-above-15)**

Bloomberg • 9h ago

---

**[Nvidia customers reportedly warned about AI-related price hikes](https://www.cnbc.com/2026/08/22/nvidia-customers-reportedly-warned-about-ai-related-price-hikes-.html)**

The chipmaker has told some of its largest customers that the prices of servers containing its AI chips could move more than 15% higher, Bloomberg News reported.

CNBC • 8h ago

---

**[Nvidia customers notified about AI-related price hikes above 15%, Bloomberg News reports](https://www.reuters.com/business/nvidia-customers-notified-about-ai-related-price-hikes-above-15-bloomberg-news-2026-08-22/)**

Reuters • 8h ago

---

**[Harvard Is Selling a $699 Course Taught by A.I. Clones of Its Faculty](https://www.nytimes.com/2026/08/22/business/dealbook/harvard-ai-faculty.html)**

The New York Times • 7h ago

---

**[Nvidia Is Spending $6 Billion to Build a Powerful U.S. Alternative to Chinese AI](https://www.wsj.com/tech/ai/nvidia-is-spending-6-billion-to-build-a-powerful-u-s-alternative-to-chinese-ai-c51c38cc)**

WSJ • 4h ago

---

**[A battle over ‘Italian brainrot’ could shape who owns AI art](https://www.npr.org/2026/08/19/nx-s1-5867638/artificial-intelligence-brainrot-memes-copyright-spyder-tung-tung-sahur)**

A legal battle over what looks like a cartoon stick could help set the rules over whether creators can claim ownership of their AI-generated characters.

NPR • 1d ago

---

**[Quiet on set. How AI transformed China’s microdrama scene](https://www.cnn.com/2026/08/22/style/short-drama-ai-china-intl-hnk)**

The breakneck AI transformation of the industry is the kind of technological disruption that many creatives fear could upend movie-making far beyond China.

CNN • 1d ago

---

**[AI decodes DNA initiator sequence found in about 60% of human genes](https://phys.org/news/2026-08-ai-decodes-dna-sequence-human.html)**

Phys.org • 12h ago

---

**[Connecticut man hid an AI prompt in a court filing. A judge found it.](https://www.ctinsider.com/connecticut/article/connecticut-judge-hidden-ai-prompt-injection-court-22387143.php)**

CT Insider • 19h ago

---

**[A mysterious free AI model is impressing developers. And nobody knows who made it.](https://www.businessinsider.com/ox-alpha-ai-model-mystery-2026-8)**

Ox Alpha, a mysterious AI model, debuted on OpenRouter on Thursday. Its origins are unknown, though some suspect a Chinese lab.

Business Insider • 7h ago

---

---

## HackerNews: "ai"

**[Don't paste the AI, please](https://news.ycombinator.com/item?id=49371857)**

If someone asks you a question, paste your answer — not the chatbot's.

⬆️ 1041 • 💬 579 • 2d ago • [dontpastetheai.com](https://dontpastetheai.com/)

---

**[AI companies destroy physical books – let's scan rare books before it's too late](https://news.ycombinator.com/item?id=49383026)**

AI companies are secretly buying, scanning, and destroying millions of physical books to train their models, permanently locking human knowledge inside private corporate servers. Anna’s Archive is urgently calling on volunteers worldwide to scan and upload books to their shadow library before this cultural heritage disappears forever.

⬆️ 611 • 💬 892 • 2d ago • [annas-archive.gl](https://annas-archive.gl/blog/physical-destruction.html)

---

**[I'm becoming AI-blind](https://news.ycombinator.com/item?id=49386699)**

Recently I've been catching myself having these little moments at work, when I'm trying to read a document someone has sent me and my brain somehow refuses to analyze it. It feels like I'm reading it, but I'm unable to focus on its content. I sat down to analyze these situations and realized they all have a common denominator: the documents all show a strong trace to AI. My brain learned to quickly spot signs of AI-generated content, at least the low effort one, and it now ignores it and moves on without thinking much about it.

⬆️ 475 • 💬 480 • 1d ago • [cymerys.com](https://cymerys.com/w/im-becoming-ai-blind)

---

**[Show HN: Huzzah – a novel approach to coding with AI](https://news.ycombinator.com/item?id=49378768)**

My personal portfolio site and blog.

⬆️ 378 • 💬 209 • 2d ago • [danielvaughn.dev](https://www.danielvaughn.dev/posts/huzzah/)

---

**[Anti-AI fonts are useless and harmful](https://news.ycombinator.com/item?id=49375719)**

Trying to obfuscate the web is a bad, pointless idea

⬆️ 210 • 💬 163 • 2d ago • [Andrew's WebLog](https://blog.yaros.ae/anti-ai-fonts-are-useless-and-harmful/)

---

**[Copyright does not protect AI-generated content in EU](https://news.ycombinator.com/item?id=49382041)**

Does copyright protect your AI-generated content in EU? Apparently not.  Content that is entirely generated by artificial intelligence is not protected by copyright. EU copyright law has strictly human-centric foundation. 

Daniel J. Gervais: 'When you put your name on an article that's written by ChatGPT or Claude, you're basically putting a provenance mark on it saying: I take responsibility for this. I haven't written it, but I'm putting my name on it. That doesn't give you copyright, but it does give you liability for the content'  https://euobserver.com/232898/interview-does-copyright-protect-your-ai-generated-content-in-europe-lets-find-out/

Gervais, Daniel J. and Shemtov, Noam and Marmanis, Haralambos and Zaller Rowland, Catherine, The Heart of the Matter: Copyright, AI Training, and LLMs (September 21, 2024). Available at SSRN: https://ssrn.com/abstract=4963711 or http://dx.doi.org/10.2139/ssrn.4963711

"Munich Local Court has held that AI generated logos do not enjoy copyright protection. Neither mere prompting nor the selection between several AI suggestions is sufficient as a human creative contribution. For businesses, this is ambivalent. On the one hand, content generated purely by AI can hardly be protected on an exclusive basis, which has implications for brand building and content strategies" https://www.germanlawinternational.com/intellectualproperty/copyright/from-the-printing-press-to-ai-how-the-eu-plans-to-modernize-copyright-law-164154/

#law #copyright #LLM #AI #iplaw #intellectualProperty #EU

⬆️ 189 • 💬 209 • 2d ago • [Mathstodon](https://mathstodon.xyz/@maxpool/117128107757895678)

---

**[AI boosted homework scores, then exam scores dropped: Study](https://news.ycombinator.com/item?id=49389565)**

⬆️ 165 • 💬 10 • 1d ago • [canews24.online](https://canews24.online/?p=71)

---

**[How a Texas student blew the whistle on a rogue AI hacking attempt](https://news.ycombinator.com/item?id=49387959)**

⬆️ 125 • 💬 44 • 1d ago • [reuters.com](https://www.reuters.com/world/how-texas-student-blew-whistle-rogue-ai-hacking-attempt-2026-08-20/)

---

**[AI didn't erase the junior engineer's value, it increased it it](https://news.ycombinator.com/item?id=49373269)**

The argument says AI erased the junior engineer's marginal value. An intern who shipped a feature that had been waiting for years suggests otherwise.

⬆️ 89 • 💬 143 • 2d ago • [Francisco Trindade](https://franciscotrindade.me/blog/the-kids-are-really-alright/)

---

**[Digging the grave of my skills: Hollywood creatives training AI to do their jobs](https://news.ycombinator.com/item?id=49399941)**

Amid a jobs slump, award-winning writers, directors and producers taking on sometimes lucrative temp work teaching AI skills such as screenwriting and production

⬆️ 52 • 💬 67 • 14h ago • [the Guardian](https://www.theguardian.com/technology/2026/aug/22/the-hollywood-creatives-training-ai-to-do-their-jobs)

---

---

## YouTube Videos: "ai"

**[AI Just Touched the Math God Wrote ](https://www.youtube.com/watch?v=IzrffaZ5v0s)**

FREE GUIDE: The Content Creator's AI Blueprint* – https://FirstMovers.ai/blueprint/ *An AI failed 650 times at the most famous ...

📺 Julia McCoy

👁️ 65K • 👍 2K • 💬 148 • ⏱️ 8:14 • 2d ago

---

**[WH nightmare: AI bubble COLLAPSES! A TECH INSIDER shows the TERRIFYING WAY it may all CRATER](https://www.youtube.com/watch?v=n32mhb2aUsE)**

MAGA allies are making huge bets on AI amid new signs that a tech “bubble” could rattle the economy. MS NOW's Ari Melber ...

📺 MS NOW

👁️ 677K • 👍 10K • 💬 1K • ⏱️ 12:08 • 2d ago

---

**[&quot;Only 2 Years Left&quot; AI Whistleblower Warns What Comes Next | Roman Yampolskiy](https://www.youtube.com/watch?v=ebWFexw51qM)**

Watch every episode ad-free & uncensored on Patreon: https://patreon.com/dannyjones Roman V. Yampolskiy is a computer ...

📺 Danny Jones

👁️ 123K • 👍 2K • 💬 654 • ⏱️ 1:50:40 • 1d ago

---

**[[Free on Github] My Jarvis AI Assistant](https://www.youtube.com/watch?v=FiOTrxq9ckM)**

This is Jarvis. He talks, he remembers everything we've ever worked on, he pushes back when my ideas don't add up, and he ...

📺 jaredrhod

👁️ 32K • 👍 2K • 💬 140 • ⏱️ 9:09 • 2d ago

---

**[AI Is Helpful, But Don’t Depend on It Too Much🤖⚠️ #AI #ArtificialIntelligence](https://www.youtube.com/watch?v=6rn83v0cxfQ)**

ArtificialIntelligence #AIDependence #AITools #prasadtechintelugu.

📺 Prasadtechshorts

👁️ 4K • 👍 424 • 💬 2 • ⏱️ 0:59 • 10h ago

---

**[Former Microsoft CEO Speaks Out on AI](https://www.youtube.com/watch?v=fv4qMGwCEtc)**

Titans on Tomorrow Ep. 2 with guest Steve Ballmer Presented by Cardiff: https://cardiff.co/ben The AI revolution is upon us and it's ...

📺 Ben Shapiro

👁️ 45K • 👍 2K • 💬 290 • ⏱️ 50:29 • 2d ago

---

**[MISERY: The REJECT AI... (Minecraft Animation)](https://www.youtube.com/watch?v=L7-Lqbjd-ak)**

Get your GAMETOONS merch HERE! - https://crowdmade.com/collections/gametoons Join the GameToons channel to get access ...

📺 GameToons +

👁️ 576K • 👍 9K • 💬 315 • ⏱️ 9:43 • 1d ago

---

**[AI IS RUINING EVERYTHING | The Kyle Kulinski Show](https://www.youtube.com/watch?v=DMlgkj8zcRk)**

Support The Show On Patreon!: https://www.patreon.com/seculartalk Subscribe to Krystal Kyle & Friends On Substack!

📺 Secular Talk

👁️ 84K • 👍 7K • 💬 896 • ⏱️ 8:38 • 2d ago

---

**[Blackouts &amp; Water Shortage Imminent: Tech Overlords Build AI Dystopia &amp; Crush Anyone Who Resists](https://www.youtube.com/watch?v=KMsklsr_nBM)**

The DoJ is using your tax dollars to sue any community that resists data centers. Clayton Morris on the AI takeover of America.

📺 Tucker Carlson

👁️ 248K • 👍 11K • 💬 1K • ⏱️ 1:00:28 • 1d ago

---

**[AI Learns to Play Mario](https://www.youtube.com/watch?v=zy-ZowzY8rI)**

You can download Revolut using this link: https://get.revolut.com/z4lF/codebullet and get $40 after your first purchase.

📺 Code Bullet

👁️ 611K • 👍 51K • 💬 1K • ⏱️ 13:55 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 2,090,699 • ❤️ 12,154 • 8d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 6,320,542 • ❤️ 2,635 • 2d ago

---

**[Qwen3.8-27B-Uncensored-MLX](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-MLX)**

*OrcaRouter*

An uncensored, MLX-quantized 27B parameter vision-language model optimized for Apple Silicon, supporting 2-8 bit precisions. It performs image-text-to-text tasks and is intended for AI safety research and red-teaming due to its removed safety alignment.

`image-text-to-text` `4.7B`

⬇️ 34,909 • ❤️ 887 • 1d ago

---

**[Qwen3.8-27B-Uncensored-FP8](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-FP8)**

*OrcaRouter*

This is an abliterated (refusal-removed) block-FP8 quantized version of Qwen3.8-27B, optimized for image-text-to-text tasks. It retains a 262K context window, tool-calling, and MTP speculative decoding, making it suitable for advanced AI research, red-teaming, and controlled experiments where safety alignment is intentionally bypassed.

`image-text-to-text` `27.8B`

⬇️ 142,846 • ❤️ 993 • 2d ago

---

**[Qwen3.8-27B-OBLITERATED](https://huggingface.co/OBLITERATUS/Qwen3.8-27B-OBLITERATED)**

*OBLITERATUS*

Qwen3.8-27B-OBLITERATED is an uncensored text generation model that achieves zero refusals while matching or exceeding stock Qwen3.8-27B capabilities, including advanced real-world tasks and tool calling. It utilizes a novel complementary abliteration blending technique to preserve performance and is optimized for greedy decoding with specific repetition penalty and disabled thinking settings.

`text-generation` `27.8B`

⬇️ 164,950 • ❤️ 541 • 2h ago

---

**[Qwen3.8-27B-Uncensored-HauhauCS-Aggressive-MTP-GGUF](https://huggingface.co/HauhauCS/Qwen3.8-27B-Uncensored-HauhauCS-Aggressive-MTP-GGUF)**

*HauhauCS*

This is an uncensored, aggressive Qwen3.8-27B multimodal model with HauhauCS FastMTP for accelerated text generation and a vision projector for image/video input. It excels at direct, fast responses and handles complex prompts without refusal, supporting up to 1M token context.

`image-text-to-text` `1.9B`

⬇️ 486,221 • ❤️ 489 • 5d ago

---

**[Qwen3.8-27B-Uncensored-GGUF](https://huggingface.co/JonathanColetti/Qwen3.8-27B-Uncensored-GGUF)**

*Jonathan Coletti*

This is an uncensored GGUF quantization of Qwen3.8-27B, optimized for reduced refusal behavior and retaining the multi-token prediction (MTP) head for enhanced generation efficiency. It supports text generation with multilingual capabilities (English, Chinese) and is compatible with llama.cpp, offering various quantization levels for different performance/resource trade-offs.

`text-generation` `27.3B`

⬇️ 1,223,422 • ❤️ 626 • 7d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a diffusion model for generating and manipulating video and audio content. It supports image-to-video, text-to-video, and various other cross-modal generation tasks, enabling creative video production and editing.

`image-to-video`

⬇️ 694,670 • ❤️ 1,569 • 5d ago

---

**[MiniMax-Music3](https://huggingface.co/MiniMaxAI/MiniMax-Music3)**

*MiniMax*

MiniMax Music 3 is a text-to-audio model capable of generating complete, five-minute songs with lyrics and detailed musical descriptions. It utilizes a hybrid LLM architecture and Flow Matching for coherent, high-fidelity 32 kHz stereo audio output, suitable for complex music production.

`text-to-audio` `2.4B`

⬇️ 16,644 • ❤️ 1,185 • 8d ago

---

**[Ornith-1.5-35B-A3B](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B)**

*Ornith*

Ornith-1.5-35B-A3B is a 35B Mixture-of-Experts model that activates ~3B parameters per token, excelling in coding and agentic tasks. It is built through end-to-end self-improvement, continuously generating and optimizing training tasks for enhanced performance.

`text-generation` `36.0B`

⬇️ 12,611 • ❤️ 324 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**

*Shuo Yang, Xiaoze Fan, Melissa Pan et al. (11 authors)*

🏢 University of California, Berkeley

FreeToken is an edge-native Mixture-of-Experts serving system that dynamically maps computation and model state onto heterogeneous local hardware to run large open-weight models on personal machines.

▲ 77 • 💬 2 • ⭐ 1,909 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2608.16157) • [💻 code](https://github.com/FlashML-org/FreeToken) • [🔗 project](https://www.flashml.ai/)

---

**[BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](https://huggingface.co/papers/2608.09888)**

*Björn Engdahl, Adrian Kosowski, Jan Chorowski et al. (9 authors)*

🏢 Pathway

A 150M-parameter reasoning model using recurrent latent reasoning and in-context learning achieves a new cost-accuracy frontier on ARC-AGI-1.

▲ 708 • 💬 5 • ⭐ 4,500 • 13d ago

[🎓 arXiv](https://arxiv.org/abs/2608.09888) • [💻 code](https://github.com/pathwaycom/arc-task-gen) • [🔗 project](https://pathway.com/blog/pathway-150m-model-breaks-arc-agi-1-cost-efficiency-frontier)

---

**[4DAnyone: Create Anyone in 4D from a Casual Monocular Video](https://huggingface.co/papers/2608.20335)**

*Yudong Jin, Tao Xie, Qihang Zhang et al. (9 authors)*

🏢 Ant Research

4DAnyone reconstructs 4D humans from monocular video by generating multiview-consistent videos and lifting them into 4D Gaussian Splatting, using reference and target context designs to overcome scaling bottlenecks.

▲ 66 • 💬 7 • ⭐ 317 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2608.20335) • [💻 code](https://github.com/ant-research/4DAnyone) • [🔗 project](https://4danyone.github.io/)

---

**[LLM-as-a-Verifier: A General-Purpose Verification Framework](https://huggingface.co/papers/2607.05391)**

*Jacky Kwok, Shulu Li, Pranav Atreya et al. (9 authors)*

LLM-as-a-Verifier introduces a probabilistic verification framework that scales across multiple dimensions to improve solution correctness assessment and agent performance across various benchmarks.

▲ 18 • 💬 1 • ⭐ 2,625 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2607.05391) • [💻 code](https://github.com/llm-as-a-verifier/llm-as-a-verifier) • [🔗 project](https://llm-as-a-verifier.com/)

---

**[Securing the AI Agent: A Unified Framework for Multi-Layer Agent Red Teaming](https://huggingface.co/papers/2606.31227)**

*Yong Yang, Xing Zheng, Huiyu Wu et al. (10 authors)*

🏢 Tencent

AI-Infra-Guard is an open-source framework that addresses AI infrastructure security through layered detection paradigms spanning infrastructure, protocol, agent behavior, and model layers.

▲ 14 • 💬 2 • ⭐ 5,407 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.31227) • [💻 code](https://github.com/Tencent/AI-Infra-Guard) • [🔗 project](https://matrix.tencent.com/clawscan/)

---

**[COLLEAGUE.SKILL: Automated AI Skill Generation via Expert Knowledge Distillation](https://huggingface.co/papers/2605.31264)**

*Tianyi Zhou, Dongrui Liu, Leitao Yuan et al. (5 authors)*

🏢 shanghai ailab 

Person-grounded AI skills are automatically distilled from heterogeneous traces into inspectable, correctable packages that capture both capabilities and behavioral patterns.

▲ 129 • 💬 3 • ⭐ 23,802 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.31264) • [💻 code](https://github.com/titanwings/colleague-skill)

---

**[LongCat-Video Technical Report](https://huggingface.co/papers/2510.22200)**

*Meituan LongCat Team, Xunliang Cai, Qilong Huang et al. (11 authors)*

🏢 LongCat

LongCat-Video, a 13.6B parameter video generation model based on the Diffusion Transformer framework, excels in efficient and high-quality long video generation across multiple tasks using unified architecture, coarse-to-fine generation, and block sparse attention.

▲ 40 • 💬 5 • ⭐ 7,415 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.22200) • [💻 code](https://github.com/meituan-longcat/LongCat-Video)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 124 • 💬 4 • ⭐ 99,289 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 84 • 💬 7 • ⭐ 84,782 • 25mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[EnvHarness: Awakening Static Worlds for Agent Learning](https://huggingface.co/papers/2608.19880)**

*Chengsong Huang, Zifeng Wang, Rujun Han et al. (17 authors)*

🏢 Google

EnvHarness and EnvRigger dynamically reshape static environments via programmable plugins to target agent weaknesses and improve reinforcement learning co-evolution.

▲ 246 • 💬 2 • ⭐ 169 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2608.19880) • [💻 code](https://github.com/google-research/envharness) • [🔗 project](https://envharness.com/)

---

---

## GitHub Repositories: "ai"

**[guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover)**

Strip multi-vendor AI provenance marks: Unicode text hygiene, statistical rewrite hooks, and C2PA/metadata from PNG/JPEG/SVG/PDF/DOCX/HTML/MD

`Python` `agent-skill` `ai` `anthropic` `c2pa` `chatgpt`

⭐ 17.1k • 🔱 2.0k • 3h ago

---

**[yc-software/qm](https://github.com/yc-software/qm)**

Multiplayer agent harness for work.

`TypeScript` `ai` `assistant` `harness` `qm`

⭐ 14.1k • 🔱 1.7k • 1d ago

---

**[trycompai/crm](https://github.com/trycompai/crm)**

Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

`TypeScript`

⭐ 8.8k • 🔱 1.1k • 1d ago

---

**[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)**

Free, open-source AI office suite for macOS, Windows & Linux — Word (.docx), Excel (.xlsx), PowerPoint (.pptx), PDF and Markdown editing with built-in AI agents.

`TypeScript` `ai` `cross-platform` `docx` `electron` `excel`

⭐ 3.5k • 🔱 581 • 1d ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 3.0k • 🔱 240 • 11d ago

---

**[yetone/cumora](https://github.com/yetone/cumora)**

Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains.

`TypeScript`

⭐ 2.9k • 🔱 350 • 9h ago

---

**[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)**

Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided before it happens and recorded after. Bring any AG-UI agent.

`TypeScript` `ag-ui` `agent-governance` `ai-agents` `browser-automation` `copilotkit`

⭐ 2.3k • 🔱 268 • 6h ago

---

**[QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent)**

A realtime voice runtime that keeps Agents talking, working, and present.  Real-time Voice Runtime for AI Agents

`JavaScript` `acp` `agent` `agentic-ai` `ai-coding` `claude-code`

⭐ 2.2k • 🔱 188 • 1d ago

---

**[ShawnPana/phone-harness](https://github.com/ShawnPana/phone-harness)**

let your agent control your phone

`Python` `agent` `ai` `automation` `developer-tools`

⭐ 2.0k • 🔱 183 • 1d ago

---

**[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)**

AI 短剧制作的 skill 集合：拆角色、排大纲、出场景与道具设定、写剧本、切分镜 | Agent skills for AI short-drama production — character bibles, adaptation outlines, art bibles, screenplays, storyboards. Runs in Claude Code & codex.

`JavaScript`

⭐ 1.9k • 🔱 236 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*
