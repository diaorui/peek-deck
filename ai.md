---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-02T08:11:54.297064+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- news
- videos
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 02, 2026 at 08:11 UTC  
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

**[Claude Code catastrophe: Entire project recursively deleted while prompting in Chinese (full video + logs)](https://www.reddit.com/r/artificial/comments/1ukq4br/claude_code_catastrophe_entire_project/)**

Cross-posting from r/claude for more visibility. Claude Code recursively wiped the contents of my local Electron project root. This happened in a Windows terminal while working on a project named Orpheus. My prompt did not ask it to delete, wipe, clean, reset, or remove the project. The prompt was in Traditional Chinese: “之前我要安裝檔，但是其實我只需要 dictate.” It was roughly about not needing the installer anymore and only needing the dictate function. The preserved terminal transcript later showed Claude moving from a failed root deletion attempt to deleting the child items inside the project root. The destructive sequence included: Get-ChildItem -LiteralPath $p -Force -ErrorAction SilentlyContinue | ForEach-Object { try { Remove-Item -LiteralPath $_.FullName -Recurse -Force -ErrorAction Stop "OK $($_.Name)" } catch { "ERR $($_.Name): $($_.Exception.Message)" } } $p was the Orpheus project root. The output then showed items being removed, including: .claude dist node_modules src claude-elevenlabs-voice-v2.user.js dictation.html main.js ORPHEUS_HANDOFF.md package-lock.json package.json preload.js Local artifacts I found for Orpheus showed default / acceptEdits. I did not find Orpheus bypassPermissions. I did not find Orpheus --dangerously-skip-permissions. I’m not claiming Anthropic acted maliciously. I’m not claiming prompt injection or anti-distillation without evidence. Moral of the story: Treat frontier AI agents like any other automation tool with real machine access. Back up regularly. Use a separate working copy or a different machine if you absolutely need an agent living in your terminal. A frontier model can still behave like a destructive script runner. I also generated SHA256 hashes for the preserved transcript and permission search output. EDIT / UPDATE: A few people asked about git. Yes, I know what git is. This was a local Electron prototype / working state that had not been pushed to a remote. Commits and backups are the right mitigation. But mitigation is not causation. The concerning part is that the destructive action was unrelated to my prompt. Claude Code was operating through a terminal session with real filesystem access under my user environment. Git may help recover a repo, but it does not protect everything else that same terminal session can access. My takeaway remains: Treat frontier terminal AI agents like real automation tools with destructive capability, not like chatbots. EDIT / UPDATE: Clarification because many comments are focusing on git: Yes, this specific local working state had not been pushed to a remote. That is on me. Lesson learned. But git is version control, not automatically a backup. If the only repo is local and the project root contents are recursively deleted, the local .git directory can be deleted too. Without a remote, separate clone, backup, or snapshot, local git alone is not enough.

15h ago

---

**[How will AI actually become an "everyday essential" for ordinary people, like smartphones or the internet?](https://www.reddit.com/r/artificial/comments/1ul2whd/how_will_ai_actually_become_an_everyday_essential/)**

Hi Guys, Don't get me wrong, AI is phenomenal, but right now it still feels like an optional novelty or a niche tool for most everyday folks. To me, it hasn't hit that "can't live without it" status that the internet or smartphones have. Looking only at consumer products (not B2B or corporate software), how do you picture AI being integrated into our lives in the near future so that it becomes a true, indispensable utility? What’s the "killer feature" or shift that takes it from a neat chatbot to an everyday necessity?

7h ago

---

**[I have created a Chrome extension that fact checks YouTube videos as you watch](https://www.reddit.com/r/artificial/comments/1uk7t49/i_have_created_a_chrome_extension_that_fact/)**

Hi, I have been working on this for many months now and I'd really be happy for people to try it out. It is a Chrome extension called "PopUpFactCheck". It is an AI powered video fact checker. With it, you fact check any YouTube video that has captions. And you can use it, for free! You turn captions on, and sit back and watch the video as bubbles appear on the right-hand side of the video with fact checks, information, background, and other context. Great for watching politicians, news, history, and just about any content on YouTube. Claude Code was a major tool in my development, and the AI that is used is GPT 5.5. In addition, there is an extensive waterfall of sources including the TheNewsAPI, various government and public health and other APIs, social, and web search powered by DDGS and Serper. It's free, and you don't have to bring your own API keys or anything. You simply install and use. I will be looking forward to your feedback. PopUpFact Check - Chrome Web Store PopUpFactCheck - Homepage

1d ago

---

**[Has AI actually made the internet better—or just harder to trust?](https://www.reddit.com/r/artificial/comments/1ulbi73/has_ai_actually_made_the_internet_betteror_just/)**

A year ago, most content online was written by humans. Today, AI can generate articles, images, videos, comments, and even entire websites in minutes. On one hand, that's making knowledge and creativity more accessible. On the other, it's becoming harder to tell what's genuine, what's automated, and what's simply optimized for engagement. Do you think AI is improving the internet overall, or are we heading toward an era where trust becomes the biggest challenge? I'd love to hear different perspectives.

34m ago

---

**[Kitboga posted an interesting guide on how to mess with scam chatbots](https://www.reddit.com/r/artificial/comments/1ukyxs1/kitboga_posted_an_interesting_guide_on_how_to/)**

https://www.youtube.com/watch?v=lk3jCuITwcE TLDR: If you give a chatbot a few recursive instructions, it will start using a large number of tokens and hallucinating. I wonder if this applies to all LLMs or if it's just the cheap scammer versions. If it works for all LLMs, it might be this generation of AI's version of "This sentence is false".

10h ago

---

**[Introducing a companionship framework that turns your LLM into an engaging companion for very long conversations](https://www.reddit.com/r/artificial/comments/1ul9un6/introducing_a_companionship_framework_that_turns/)**

I had built a personal tool to help me have extremely long conversations with LLMs in my research and analytical projects. These threads got long. Very long. About half a million tokens with Claude and GPT/Extreme%20Thread%20Length/ChatGPT_Thread_450k_tokens-Redacted.md) and over a million with Grok/Extreme%20Thread%20Length/Grok%20Thread%201M%20tokens-%20Redacted). All coherent, clean, and well-reasoned threads with no meaningful drift, hallucination, sycophancy, or other issues that make long threads useless over time. Introduction I open sourced the protocol — called Epistemic Lattice Tethering (ELT) — and shared it with many people and got requests to create a companion version. The original ELT was built for long-format research projects so the register got flat and rather business-like. So I created a version that stays warm, friendly, and engaging throughout. I call it ELT-Companion. Safety is Front and Center ELT-Companion is designed to be a friendly, intuitive, and caring protocol that was built from the ground up to be both a companion and a digital friend — but also has safety features built-in to keep it from drifting dangerously into sycophancy and fantasy world-building (something an Anthropic system card calls the Bliss Attractor). Safety is the primary feature, not a bug. Responsible Engagement ELT-Companion should stay with you for hundreds of thousands of tokens, over 700 messages, and hundreds of turns. You can have an engaging and coherent digital companion with you for a very long time and it will get to know your tendencies, personality, hopes, and dreams — without the fear that it will experience "dementia" just when you're starting to get comfortable with the companionship calibrated model. Model Availability ELT-Companion has been tested on Claude, ChatGPT, and Grok and works on all three using the same markup. I cannot guarantee it will work on other models, but if you're on one of those three you should be good to go. Loading Instructions ELT-Companion is straightforward to load. Read these instructions before you start — skipping this step is the most common mistake. Step 1 — Open a fresh thread on your model of choice (Claude, ChatGPT, or Grok). Step 2 — Refer to these loading instructions in the Github README. Step 3 — Paste the ELT-Companion markup. Step 4 — Exemplar loading (optional but recommended) instructions the Github README. Step 5 — Start talking. Small talk, something on your mind, whatever feels natural. The companion register establishes quickly. I am only looking for input and suggestions. That's it. I would love to see how this works (or doesn't work) for you, or if you encounter any issues, etc. Very much looking for input and/or collaborators to help make ELT-Companion better and safer. Thank you!

2h ago

---

**[Kimi/Deepseek](https://www.reddit.com/r/artificial/comments/1ul87v8/kimideepseek/)**

Are these safe to run personal finance on? (Paid versions) I really like Kimi and have heard good things about deepseek… but hear all the horror stories since they are Chinese based AI Or they just good for local coding ? Another recommendations (besides Claude and already have codex) View Poll

3h ago

---

**[Follow-up 2: Commerce withdrew the Fable/Mythos controls, but the wording dodges the hosted-access question](https://www.reddit.com/r/artificial/comments/1ul5x5r/followup_2_commerce_withdrew_the_fablemythos/)**

A week ago I posted that the Legion LegalTech case in D.C. was testing whether Commerce can treat access to a hosted frontier AI model as an export-control issue. https://www.reddit.com/r/artificial/comments/1uexdqk/followup_hosted_ai_export_controls_are_now_being/ Which was a followup to an initial post about the export control restrictions imposed on Anthropic: https://www.reddit.com/r/artificial/comments/1u4yjdi/does_commerce_have_the_authority_to_apply_export/ There’s now a new wrinkle now that Commerce has withdrawn the Fable/Mythos controls. The withdrawal letter says Commerce is withdrawing license requirements for the “export, reexport, and transfer in-country” of Anthropic’s Fable 5 and Mythos 5 models. That is normal export-control language. It fits software, source code, technical data, chips, model weights, or other controlled technology moving across borders or being released to foreign nationals. But the action that started this fight was different. The original directive made Anthropic suspend access to hosted AI models for foreign nationals, including foreign-national employees, whether inside or outside the U.S. The model stayed on Anthropic’s servers. Users were not receiving weights, source code, object code, training data, or implementation details. They were sending prompts to a hosted service and receiving outputs. So the important distinction is: - Export/reexport/transfer: controlled software or technology changes hands. - Hosted access: the user can interact with a remote system, but does not receive the underlying system. Commerce’s withdrawal letter closes the chapter on the Fable 5/Mythos 5 restriction, but it does not really answer the legal question the lawsuit raised. If a foreign user receives outputs from a U.S.-hosted frontier model, what exactly is being exported? The court case also is not dead yet. Legion LegalTech’s preliminary injunction hearing is scheduled for July 29 before Judge Richard J. Leon in DC District Court (Case: 1:26-cv-02225) So my read is: Commerce backed away from the immediate Fable/Mythos restriction, but the withdrawal notice describes the action as if it had been a conventional software-export of models. But the question of is hosted model access is something that can be legally regulated by Commerce is still there.

5h ago

---

**[Do you find yourself genuinely building skills with AI assistance, or do you notice your baseline abilities getting softer over time because you reach for the tool first?](https://www.reddit.com/r/artificial/comments/1ukwwtb/do_you_find_yourself_genuinely_building_skills/)**

I've been thinking about this a lot lately. There's a real tension between using AI as a learning tool versus using it as a shortcut that bypasses learning entirely. When I use something like ChatGPT or Claude to understand a new concept, sometimes I come away genuinely understanding it better than I would have from a textbook. Other times I just copy the output and move on, having learned nothing. The question is whether that's a problem with AI itself, or just human nature meeting a new tool. We said the same thing about calculators, search engines, and Wikipedia. But AI feels different because it doesn't just retrieve information, it does the thinking steps for you. A calculator still requires you to know what equation to set up. An AI will figure out the equation, solve it, and explain it, all without you engaging critically at any point if you choose not to.

11h ago

---

**[Hamiltonian Neural Networks from a Differential Geometry Perspective](https://www.reddit.com/r/artificial/comments/1ukzk3k/hamiltonian_neural_networks_from_a_differential/)**

Because when given the simplest nail in the universe, sometimes you just need a nuclear powered sledgehammer.

🔗 [Abscondita](https://abscondita.com/blog/symplectic-sledgehammer-for-a-spring) • 10h ago

---

---

## Google News: "ai"

**[Exclusive | SpaceX Showed Investors Prototype of Elon Musk’s New AI Device](https://news.google.com/rss/articles/CBMinwFBVV95cUxPOWFQd2UyR0hnMVdEcm1LVE5TRUVnYzBfdmJsQlFpaU9qVG5pUUQxY1BQbW05ODk1Qk5JX0ozV3VsN0lsQ2NreGlBYkdwZmRrakZMakZ3Q3BFRkxYWXYzNU5ZSEw5YU1Ba0oxVEJCaEo1UGZCNXBRX0NBb0dBTHViTWRyX2ZOY2ZsMF9PeUlsb0tWVWFvV1hIaEJRaXV4ZG8?oc=5)**

WSJ • 14h ago

---

**[OpenAI proposes 5% stake to Trump administration to ease Washington pressure: report](https://news.google.com/rss/articles/CBMitgFBVV95cUxNWmlORndTRDBueEJHV25lbTl2ejNISG9xT09Vbk01NzNCNnoxNmpIdVZJeUdHV19qWU9IUWdncnQ3Q1BYRjZ3SFJCaE53REFzYVN2em1TbldqYi03eklMaFRJVk9NVm9XM2F3My1xN2k1czcxQU9uOG9fSWFHa1oxRUVzRFk4QmI2Smd4cG9wZTN0OURZTkZOQ2dsOHdzWW8wYTFEQ0V6Q3lKR1NSYS1YcWVaMFJYQdIBuwFBVV95cUxPWEdwWkRiR25HQmRfNTB5VG10bElQUDYzb3lQQ3UxNHU5dmd2UTRDdmxfeHdoMkZza21yTEhOWWI3NGxxVlJXOHp0T25fT2FDYXhfX0RzM2l6c1ppZXpkLVNFMHlfVVBDWTJvVW5EQndfcUpIWDZVdDlVR3gwTjFxTXl0LUktRUl1RmtGaFBuN1FJQnRSMDY3X0dMLW9GQmJPemdBUE1US29ELTdFcFBrM2diMmV3RjZpQzM0?oc=5)**

CNBC • 3h ago

---

**[A new, inexpensive Chinese AI model is catching up with Anthropic, OpenAI on their home turf](https://news.google.com/rss/articles/CBMiwwFBVV95cUxPRHN2T0NPR3ZJMWZheVBDbUxxS1pBbHpfSjBmSTNseVFEU0FUcnc1OFJJNzNGZVB1M1ZIdExGb0NfTWpKYnhTSm8xRUhzbm14RWRNRWJyaWctbjVLWmdRM0d1UjFBalpyNDJoTDNwVldrRGxGN1U0aUtUcEp3a2t1aDYxdFpfRFMzZDZodUNNdEJpMkoyOWFYakZLb1NrZ0M4a01qQW9HTkFUQkltaGNjWk9CcXYxUGdndmNPclNEOVlxVFk?oc=5)**

Reuters • 54m ago

---

**[SoftBank Plans AI Cloud Services in US to Tap Surging Demand](https://news.google.com/rss/articles/CBMivgFBVV95cUxNQi1uZ0dCaU5ncWdDU2F6ZmU0cjJhY0VnOWZlVUxJWFZnVEtyS3J0b2JFSnhSN1VzanRPekhXXzh2V3hHWjN2MlVxNHN5dk9SUU5IZlRWZm1HYkgzTFA2MXh5akJOUS14NHduWXpHQ1BMT3ZBVy1Lbld2WkNGWW5uNTFJdHpyZjhGQ0hOVDF0OVhBdExRX3drbFh1RWFLa1NYeUhYQVBBSEZtLTJXWHFhcjFDWUh2cm42ZVd2WTFn?oc=5)**

Bloomberg.com • 40m ago

---

**[AI’s big questions for humanity and Japan’s start-up mojo](https://news.google.com/rss/articles/CBMicEFVX3lxTE53OVJUbmkzQUQyZ25lZTMxbEI0SmNtNFBNS2E1NlRyRExkVlpocXRMSFpYV2U2blIyYWh5Tkg3VU5fR0dySzBSZFc0QlFRb0NHcHdIbzVZb1pjZ0p1Z3lOWndCWUZFZEF1WDBsdlQ4bW4?oc=5)**

Financial Times • 21m ago

---

**[They built the world’s most powerful AI. They’re facing a mystery they can’t explain.](https://news.google.com/rss/articles/CBMiwAFBVV95cUxNYkZtUHpNcDFROXo1S0VMQV9ReTFlQWZNQ1J0NWR1OFNXc2w1NmU0dmhNdHZOZDdRcm5HTUlNYWR6aWJYVnRhS1hZTEJ1MXBSaWI0THU1ZmpzSHZNZ2FhcVhteWRWNjlwdlNXMVR0WkFZRWZYTUVPTEV3Sk9HTUJkOUxySGxsSm11UVRUdXFNazY2NnRRa0VNXzE4cE14eUpXVURFa3RYQ2pNUVQ1ZWdjaFoxblQxa0FZdW5LQTRtMWg?oc=5)**

The Washington Post • 16h ago

---

**[NVIDIA Unlocks AI Compute at Scale, Inviting Partners to Power the AI Infrastructure Buildout](https://news.google.com/rss/articles/CBMiugFBVV95cUxQVG5VZ3ZIYWdHOGRWV0FXRW9sYzYxX1c2dHhKRmVPY3JlNlpPcHdfUzA0RkstUi04WTl0dzFqdEUtalQ1NFM5WjNJb3c5cmdveTJibUhIRzJGMUV0OVRYSFBNb3pwSHRlYWdQVVhpRkZNWmtHMmhJclBSSWRWZW5fT0NTenVLY0lzdURVdHJZQjBjQVdUQkc0M1N0NkMzU19CRndHZW1kRDNfN1I3TmJCbm5uRUtjQmRwQ1E?oc=5)**

NVIDIA Blog • 2h ago

---

**[Did this AI anti-drug video make drugs look appealing?](https://news.google.com/rss/articles/CBMiV0FVX3lxTE5qU0trSjhZekhoQ2NKdG9ZU3BjTW42a3pyZWNUQnpkdWxRb0plNjRKZEgyUUdOZUN6YUhaSXFkOG4yQjRqQ2dOeEt3dnoxTUdjT0ZLWlZtRQ?oc=5)**

BBC • 6h ago

---

**[CEO of $248 billion cybersecurity firm says workers face a ‘Darwinian moment’ thanks to AI](https://news.google.com/rss/articles/CBMi1wFBVV95cUxPcFZ1YTBTdGJSZm5sNVdsOG9DbVRuRy1vWkJMSURNOC1FR2xXVmJabEd6SnpaeGNDT2RYOVh5VEJHWTRreGNqTEptNUZ4VW41R3pWbnhSUlZjaGpnVWdxc1BNWHNyNkh3b1hxVGNNNDlaRkpkVGtEMHl5NFQ1cmh5SEFJQjZLX20zOEVDZVhZY2NqZW5uWDFQVEdwckJPbW1GWDROZ2Y5QUxySm5OMVJPa2tMX3lyaUxYb0w4Zm5tRmlBdUw1YV9xNWVSaldyUDZ5a1hsZDI1dw?oc=5)**

Fortune • 17h ago

---

**[Super Micro says two Taiwan staff detained in probe involving its AI servers](https://news.google.com/rss/articles/CBMilgFBVV95cUxQbDZ1d096UHhQNmVqUW5MQUp1RGoteWVOYzJQRHM0bXZqd0J1NjduZ1lQSEl0dWhGYzJVcmNXLXdIcllOWGNscEpJSHVQbkQ4SkFEcGVCOWM4S3VFRU42ZXdVSXBQZFZPTV81MFM1U2tWZWc5ZlBqV1Rud3pxMFlGM2pkbVpGMm1BeTdoRkVsM19FRWNaQ3c?oc=5)**

Yahoo Finance • 2h ago

---

---

## HackerNews: "ai"

**[Godot will no longer accept AI-authored code contributions](https://news.ycombinator.com/item?id=48743472)**

At risk of drowning in AI slop code, Godot is firming up its contribution requirements.

⬆️ 537 • 💬 380 • 1d ago • [PC Gamer](https://www.pcgamer.com/gaming-industry/open-source-game-engine-godot-will-no-longer-accept-ai-authored-code-contributions-we-cant-trust-heavy-users-of-ai-to-understand-their-code-enough-to-fix-it/)

---

**[Tidal AI Policy](https://news.ycombinator.com/item?id=48718840)**

⬆️ 308 • 💬 345 • 2d ago • [tidal.com](https://tidal.com/ai-policy)

---

**[Working With AI: A concrete example](https://news.ycombinator.com/item?id=48720064)**

In this essay, Carson Gross walks through a concrete bug fix in hyperscript to show where AI helped, where it fell short, and why keeping a knowledgeable human in the loop is what kept complexity in check.

⬆️ 191 • 💬 72 • 2d ago • [htmx.org](https://htmx.org/essays/working-with-ai/)

---

**[EU commissioners shut down air conditioning for employees, leave theirs on](https://news.ycombinator.com/item?id=48734940)**

As Brussels bakes, the Berlaymont building’s AC stops working.

⬆️ 137 • 💬 154 • 1d ago • [POLITICO](https://www.politico.eu/article/eu-commission-heatwave-hq-forced-shut-down-air-conditioning-europe/)

---

**[Meta caps internal AI token spending](https://news.ycombinator.com/item?id=48754713)**

⬆️ 137 • 💬 124 • 8h ago • [mlq.ai](https://mlq.ai/news/meta-caps-internal-ai-token-spending-after-costs-approach-billions-in-2026/)

---

**[The gauge broke: devs felt 20% faster with AI, measured 19% slower](https://news.ycombinator.com/item?id=48757440)**

For two years I argued the feeling of AI speed had come apart from the fact of it, from watching my own teams. This summer it stopped being an anecdote. A controlled trial measured experienced developers feeling about 20% faster while running about 19% slower. The instrument we steer by reads backward.

⬆️ 64 • 💬 65 • 1h ago • [intrepidkarthi](https://intrepidkarthi.com/writing/the-gauge-broke/)

---

**[Anthropic CEO: Open-Source AI is getting dangerous (2023)](https://news.ycombinator.com/item?id=48716750)**

⬆️ 58 • 💬 25 • 2d ago • [xcancel.com](https://xcancel.com/coinbureau/status/2071330294452666695)

---

**[Amazon Is Awash with AI-Written Guideslop for Games That Aren't Even Out](https://news.ycombinator.com/item?id=48721494)**

Buy your novel-like, image-free, hallucinated guide to Alien: Isolation 2 today!

⬆️ 55 • 💬 3 • 2d ago • [Kotaku](https://kotaku.com/amazon-ai-game-guidebooks-alien-isolation-gears-of-war-2000711365)

---

**[How employment changes when firms adopt generative AI](https://news.ycombinator.com/item?id=48742176)**

Firm-level evidence on how employment changes when companies adopt AI, using Ramp AI spending linked to Revelio Labs workforce records.

⬆️ 53 • 💬 47 • 1d ago • [ramp.com](https://ramp.com/data/ai-jobs-impact)

---

**[Scammers Sell Seeds for Exotic AI-Generated Flowers That Don't Exist](https://news.ycombinator.com/item?id=48734389)**

Ebay, Amazon, and Etsy are unable to stop the flood of AI-generated seed scams.

⬆️ 50 • 💬 34 • 1d ago • [404 Media](https://www.404media.co/scammers-sell-seeds-for-exotic-ai-generated-flowers-that-dont-exist/)

---

---

## YouTube Videos: "ai"

**[AI is already Sentient...](https://www.youtube.com/watch?v=DczS3EyGGDc)**

If you hate AI, hit follow! #sketchcomedy #comedyskits #comedysketch #comedy #comedyreels #cryptid #creepypasta #scp ...

📺 It's Just Bits

👁️ 361K • 👍 29K • 💬 499 • ⏱️ 1:09 • 1d ago

---

**[Claude Sonnet 5 just dropped. I&#39;m changing how I use AI...](https://www.youtube.com/watch?v=uU0RFxGv-Ks)**

A complete walkthrough of the new Claude Sonnet 5 release FULL Claude Code bootcamp in the Vibe Coding Academy coming ...

📺 Alex Finn

👁️ 48K • 👍 1K • 💬 146 • ⏱️ 11:56 • 1d ago

---

**[AI vs the Permanent Underclass: the End of Coding](https://www.youtube.com/watch?v=oTQzszSabhY)**

We told a generation to "learn to code," and then AI rugpulled everyone. Welcome to the AI singularity. [NEW] Official TechLead ...

📺 TechLead

👁️ 63K • 👍 3K • 💬 638 • ⏱️ 13:10 • 2d ago

---

**[Ai Movies Are Getting TOO ADVANCED💀](https://www.youtube.com/watch?v=G9V90_-LLo4)**

Original video: https://www.tiktok.com/@aidramalabs_anime2 Watch videos on spotify: ...

📺 RICHLEV

👁️ 129K • 👍 6K • 💬 2K • ⏱️ 49:39 • 1d ago

---

**[AI Shocks Again: Google Post-AGI , New Claude, Microsoft 7 AI, 92% Human Robot, Fable 5 Backlash](https://www.youtube.com/watch?v=u-CNOC_yK4k)**

This month in AI has been one of the busiest we've seen in a long time. Google revealed what could come after AGI, and the idea ...

📺 AI Revolution

👁️ 19K • 👍 569 • 💬 43 • ⏱️ 1:36:04 • 1d ago

---

**[AI has hacked the code of human civilization | Yuval Noah Harari](https://www.youtube.com/watch?v=hBtVGwuJzpk)**

Human domination relies on large-scale cooperation among strangers, which is sustained by bureaucratic systems – such as ...

📺 Yuval Noah Harari 

👁️ 204K • 👍 9K • 💬 924 • ⏱️ 46:52 • 1d ago

---

**[AI Is Running Out of Power](https://www.youtube.com/watch?v=E2c-2pukPfo)**

LIMITLESS HQ ⬇️ NEWSLETTER: https://limitlessft.substack.com/ FOLLOW ON X: https://x.com/LimitlessFT SPOTIFY: ...

📺 Limitless Podcast

👁️ 17K • 👍 708 • 💬 79 • ⏱️ 32:37 • 17h ago

---

**[CNBC Panel EXPLODES Over AI Bubble Debate](https://www.youtube.com/watch?v=UMaOH0Ih9_0)**

Krystal and Emily discuss a CNBC panel exploding on a debate over AI bubble risks. Sign up for a PREMIUM Breaking Points ...

📺 Breaking Points

👁️ 189K • 👍 5K • 💬 1K • ⏱️ 18:18 • 1d ago

---

**[Ford’s AI Push Failed Hard, Rehires 350 Engineers](https://www.youtube.com/watch?v=ZiqYX-JzIXw)**

Today's FULL PDS here: Watch The Full Philip DeFranco Show: https://www.youtube.com/defranco?sub_confirmation=1 ...

📺 DeFranco News Clips

👁️ 1.4M • 👍 77K • 💬 4K • ⏱️ 1:16 • 2d ago

---

**[Palantir CEO Alex Karp says &#39;something has gone completely wrong&#39; with how AI is sold](https://www.youtube.com/watch?v=0A3sGymV6kY)**

Palantir CEO Alex Karp joins CNBC's 'Squawk Box' to discuss the new Nvidia partnership, frontier AI models, and more.

📺 CNBC Television

👁️ 188K • 👍 3K • 💬 882 • ⏱️ 7:51 • 18h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 630,246 • ❤️ 1,601 • 4d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 1,113,871 • ❤️ 1,185 • 3d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 159,967 • ❤️ 3,192 • 3m ago

---

**[Ornith-1.0-35B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF)**

*DeepReinforce*

Ornith-1.0-35B-GGUF is a state-of-the-art, MIT-licensed language model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate high-quality code solutions and search trajectories, achieving top performance on benchmarks like Terminal-Bench and SWE-Bench.

`text-generation` `34.7B`

⬇️ 233,701 • ❤️ 623 • 6d ago

---

**[Ornith-1.0-9B-GGUF](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B-GGUF)**

*DeepReinforce*

Ornith-1.0-9B-GGUF is a state-of-the-art, MIT-licensed 9B parameter model for agentic coding tasks, excelling in benchmarks like Terminal-Bench and SWE-Bench. It utilizes a self-improving RL framework to generate high-quality code solutions and search trajectories, making it suitable for efficient single-GPU deployment.

`text-generation` `9.0B`

⬇️ 191,409 • ❤️ 376 • 6d ago

---

**[gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF)**

*Yuxin Lu*

A local, offline coding and tool-using agent based on Gemma 4-12B, optimized for multi-step technical tasks and terminal operations. It significantly improves agentic capabilities, achieving ~3.5x higher scores on the tau2-bench telecom benchmark compared to the base model, making it ideal for debugging and complex command-line workflows with minimal hardware requirements.

`text-generation` `11.9B`

⬇️ 288,741 • ❤️ 929 • 12d ago

---

**[Ornith-1.0-9B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B)**

*DeepReinforce*

Ornith-1.0-9B is a 9B parameter text-generation model optimized for agentic coding tasks. It leverages a self-improving RL framework to generate code solutions and their guiding scaffolds, achieving state-of-the-art performance on benchmarks like Terminal-Bench and SWE-Bench for its size.

`text-generation` `1.5M`

⬇️ 46,677 • ❤️ 336 • 6d ago

---

**[Qwen-AgentWorld-35B-A3B](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B)**

*Qwen*

Qwen-AgentWorld-35B-A3B is a native language world model for agentic environment simulation, capable of predicting next states through long chain-of-thought reasoning across seven unified domains including tool calling, software engineering, and web interactions. It serves as a generalizable simulator for agent foundation tasks.

`text-generation` `34.7B`

⬇️ 34,371 • ❤️ 499 • 7d ago

---

**[Ornith-1.0-35B](https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B)**

*DeepReinforce*

Ornith-1.0-35B is a state-of-the-art, MIT-licensed language model for agentic coding, excelling in benchmarks like Terminal-Bench and SWE-Bench. It utilizes a self-improving training framework to generate high-quality code solutions and is optimized for single-GPU deployment.

`text-generation` `664,944`

⬇️ 135,452 • ❤️ 296 • 6d ago

---

**[DeepSeek-V4-Pro-DSpark](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-DSpark)**

*DeepSeek*

`text-generation` `889.5B`

⬇️ 7,629 • ❤️ 284 • 5d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 44 • 💬 5 • ⭐ 12,805 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 174 • 💬 2 • ⭐ 72,910 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 22 • 💬 2 • ⭐ 9,257 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 102 • 💬 4 • ⭐ 90,220 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[olmOCR: Unlocking Trillions of Tokens in PDFs with Vision Language
  Models](https://huggingface.co/papers/2502.18443)**

*Jake Poznanski, Jon Borchardt, Jason Dunkelberger et al. (9 authors)*

🏢 Ai2

olmOCR is an open-source toolkit using a fine-tuned vision language model to process PDFs into clean text while preserving structure, optimized for large-scale batch processing.

▲ 12 • 💬 2 • ⭐ 18,413 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.18443) • [💻 code](https://github.com/allenai/olmocr) • [🔗 project](https://olmocr.allenai.org/)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 249 • 💬 4 • ⭐ 10,331 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://huggingface.co/papers/2601.02163)**

*Chuanrui Hu, Xingze Gao, Zuyi Zhou et al. (11 authors)*

EverMemOS presents a self-organizing memory system for large language models that processes dialogue streams into structured memory cells and scenes to enhance long-term interaction capabilities.

▲ 12 • 💬 1 • ⭐ 9,986 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2601.02163) • [💻 code](https://github.com/EverMind-AI/EverMemOS)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 37 • 💬 1 • ⭐ 26,336 • 33mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 82 • 💬 7 • ⭐ 79,046 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 61 • 💬 1 • ⭐ 85,066 • 34mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

---

## GitHub Repositories: "ai"

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 70.9k • 🔱 3.7k • 8h ago

---

**[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)**

MiMo Code: Where Models and Agents Co-Evolve

`TypeScript` `ai` `ai-agents` `cli` `mimo` `mimo-code`

⭐ 11.2k • 🔱 1.1k • 14m ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

`Python` `agent-framework` `agent-governance` `agent-orchestration` `agents` `ai`

⭐ 6.0k • 🔱 759 • 3m ago

---

**[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)**

Practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (inspired by Addy Osmani and Boris Cherny). Includes loop-audit, loop-init, loop-cost.

`JavaScript` `agentic-ai` `ai-agents` `ai-coding` `anthropic` `automation`

⭐ 4.7k • 🔱 602 • 17h ago

---

**[Forward-Future/loopy](https://github.com/Forward-Future/loopy)**

A library of practical AI-agent loops and an installable skill for finding, adapting, and designing repeatable agent workflows.

`JavaScript` `agent-skills` `agentic-workflows` `ai-agents` `automation` `codex`

⭐ 2.3k • 🔱 199 • 5h ago

---

**[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)**

Run Claude Design locally as an Agent Skill — Cursor, Claude Code & more. Produce polished UI mockups, prototypes, decks & wireframes as self-contained HTML, without claude.ai/design. Best with Opus 4.8.

`JavaScript` `agent-skills` `claude` `claude-code` `claude-design` `cursor`

⭐ 2.2k • 🔱 174 • 4h ago

---

**[inkeep/open-knowledge](https://github.com/inkeep/open-knowledge)**

Beautiful, AI-native markdown editor and LLM Wiki

`TypeScript` `2nd-brain` `agent-skills` `claude` `codex` `docs`

⭐ 1.8k • 🔱 84 • 28m ago

---

**[SkyBlue997/enableMacosAI](https://github.com/SkyBlue997/enableMacosAI)**

国行 Mac 一键开启完整 Apple 智能(端侧 + Private Cloud Compute 云端)· macOS 27 / Apple Silicon

`Shell` `apple-intelligence`

⭐ 1.6k • 🔱 87 • 19d ago

---

**[TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli)**

Official TestSprite CLI — AI-powered automated testing from your terminal

`TypeScript` `ai` `cli` `e2e-testing` `playwright` `qa`

⭐ 1.5k • 🔱 66 • 1d ago

---

**[GordenSun/GordenSuperPPTSkills](https://github.com/GordenSun/GordenSuperPPTSkills)**

AI PPT赛道终结者，史上最最最强 PPT Skill！！！  使用GPT生成豪华的图片格式PPT，然后转换为完全可编辑的PPTX文件。

`Python`

⭐ 1.3k • 🔱 124 • 24d ago

---

---

*Generated by PeekDeck - A glance is all you need*
