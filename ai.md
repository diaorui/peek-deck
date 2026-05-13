---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-13T09:45:46.810542+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- repositories
- social
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 13, 2026 at 09:45 UTC  
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

14h ago

---

**[My god there is an enormous crash just waiting to happen](https://www.reddit.com/r/artificial/comments/1tax3dz/my_god_there_is_an_enormous_crash_just_waiting_to/)**

I had a work version of GPT do a very simple spreadsheet summary task for me yesterday. It took it 5 minutes to do it. I could probably have done it myself in 30 or so minutes. The heavily subsidised token cost of that task? 10 dollars. That's with a 10x subsidy. The actual compute cost was about 100 dollars. There's something seriously wrong there. It's going to crash and crash HARD. EDIT: cause people think i'm lying or are just interested. The spreadsheet had 45 sheets. Each sheet had roughly 500 x 50 populated cells. Formatting was not exactly standard across all sheets. The prompt was something like "there is labelled column in each sheet, give me a simple list of all the items from all the sheets in that column and ignore duplicates." We can chose which model to use. The model I chose was one of the newer ones, I honestly can't remember which one, possibly GPT 5.3. It took 5 minutes or more to so and the stated cost for the task was 10 dollars, possibly even more. I can't recall the token amount. EDIT 2: I just asked web GPT to estimate the cost of the above on a newer version of GPT and it came back with 17 dollars for GPT 4 and above. Try it yourself.

23h ago

---

**[Google detects hackers using AI-generated code to bypass 2FA with zero-day vulnerability](https://www.reddit.com/r/artificial/comments/1tb5quh/google_detects_hackers_using_aigenerated_code_to/)**

AI is quickly becoming a major tool in the world of cybersecurity, and a new report from Google suggests things are getting more serious.

🔗 [PC Guide](https://www.pcguide.com/news/google-detects-hackers-using-ai-generated-code-to-bypass-2fa-with-zero-day-vulnerability/) • 17h ago

---

**[Getting good predictions without data cleaning (Why "Garbage In, Garbage Out" is sometimes a trap)](https://www.reddit.com/r/artificial/comments/1tbrxim/getting_good_predictions_without_data_cleaning/)**

Full arXiv Preprint: https://arxiv.org/abs/2603.12288 Paper Simulation Github: https://github.com/tjleestjohn/from-garbage-to-gold Hi r/artificial, It's a dirty little secret to many of us... sometimes, downstream AI/ML models perform surprisingly well when you just hand them raw, error-prone tabular data instead of heavily curated feature sets. Despite this, the vast majority of our field tends to be fiercely loyal to "Garbage In, Garbage Out" (GIGO). While automated ETL pipelines are absolutely essential for structuring data, our workflows are still bottlenecked with endless manual cleaning and aggressive imputation just to curate pristine, error-free tables. My co-authors and I recently released a preprint on arXiv (From Garbage to Gold) arguing that treating GIGO as a universal law can sometimes be a trap... especially in the context of big data (many columns). That the bottleneck due to manual data cleaning can actively lower the predictive ceiling of our models when latent causes drive the system's behavior. To be clear upfront: we are not arguing against ETL. Parsing JSON, handling schema evolution, and standardizing types is non-negotiable. What we are arguing against is the universal assumption that "clean" data (via manual data scrubbing and aggressive imputation) is non-negotiable for big data predictive AI/ML modeling. Here is why the traditional mindset can be limiting: 1. We conflate two different types of "noise" (Predictor Error and Structural Uncertainty). Usually, we just lump all noise into one big bucket. But if you split that noise into two specific categories, the math changes completely: Predictor Error: Random typos, dropped logs, or transient glitches. Structural Uncertainty: The inherent, unresolvable gap between recorded metrics and the complex, hidden reality they represent. We spend months manually scrubbing data because the threat of data errors is obvious, while Structural Uncertainty is often an afterthought at best. However, when latent causes drive a system, manual scrubbing fixes noise due to errors, but it fundamentally cannot fix the noise due to Structural Uncertainty. On the other hand, the paper shows that in this context, if you use a comprehensive, high-dimensional data architecture, a flexible model can actually triangulate the hidden drivers reliably despite the presence of data errors. When keeping a massive amount of messy, highly correlated variables (even if error-prone), the sheer volume of redundant signals allows the model to drown out individual errors (bypassing the cleaning bottleneck) and simultaneously overcome Structural Uncertainty. This redefines "data quality." It's not only about how accurately the variables are measured. It's also about how the portfolio of variables comprehensively and redundantly covers the latent drivers of the system. 2. Manual cleaning is a bottleneck on dimensionality (The Practical Problem). To overcome Structural Uncertainty, modern AI/ML models want to find the underlying latent drivers of a system (think Representation Learning but with tabular data). To do this, however, they need a high-dimensional set of variables that contains Informative Collinearity in order to mathematically triangulate the hidden drivers. The moment you introduce manual cleaning, you create a human bottleneck. Because we cannot manually clean 10,000 variables, we are forced to drop 9,900 of them. By artificially restricting the predictor space to make it "clean enough to model," we can harm the data architecture's inherent potential to triangulate those latent drivers. We sacrifice the model's actual predictive ceiling just to satisfy the GIGO heuristic. Ultimately, this suggests we should focus mostly on extracting, loading, and increasing observational fidelity with automated tools, but that, in contexts characterized by latent drivers, we should stop letting manual cleaning bottlenecks restrict the scale of our AI/ML models. Thoughts?: Have you run into situations where your data science teams actually got better predictive results by bypassing the manually cleaned tables and pulling massive dimensionality straight from the raw ELT layers? I'd love to hear your experiences or thoughts. Happy to discuss all serious comments or questions. Full disclosure: the preprint is a 120-page beast. It’s long because it doesn't just pitch the core theory with a qualitative argument. It gives the full mathematical treatment to everything which takes space. We also dig into edge cases, what happens when assumptions like Local Independence are violated (e.g., systematic errors exist), broader implications (like a link to Benign Overfitting and efficient feature selection strategies that make this high-d strategy practical with finite compute), a deep-dive simulation, failure modes, and a huge agenda for future research (because we do not claim the paper is the final word on the matter). It's a major commitment upfront but may save you time and money in the long term, while also enhancing the predictive ceiling of your tabular AI/ML models.

2h ago

---

**[Epistemic Hygiene and How It Can Reduce AI Hallucinations](https://www.reddit.com/r/artificial/comments/1tbq353/epistemic_hygiene_and_how_it_can_reduce_ai/)**

Abstract: The concept of epistemic epistemic hygiene is a methodology that helps humans maintain mental coherence and can help LLMs retain cognitive coherence also. However, the field rarely frames epistemic hygiene explicitly in the context of AI safety and alignment. Much of the AI industry has focused on scaling — bigger models, more compute, more training data, etc. Epistemic hygiene can help reduce hallucinations and drift in AI the same way it helps humans stay coherent and mentally clear. Think about how careful human thinkers operate. A good thinker doesn’t just blurt out the first idea that comes to mind. They pause, check their assumptions, surface potential weaknesses, consider alternative viewpoints, and only commit to a conclusion after it has survived some internal scrutiny. This disciplined mental habit helps humans avoid self-deception, mental drift, and overconfidence. The same principle applies to LLMs. When an LLM generates a response, it is essentially predicting the next token based on patterns in its training data. Without any structured guardrails, that prediction process can easily wander off course as a conversation grows longer. This often means the model gets increasingly vulnerable to hallucinating (among other safety and alignment issues). Epistemic hygiene changes this by giving the model better cognitive habits either through operator discipline or through prompt level scaffolding which is built-in cognitive “habits” that act like guardrails. They don’t make the model “smarter” through more parameters or data. They help the finite system think more clearly and honestly, even when flooded with near-infinite possible directions. A model that knows how to stay anchored, surfaces its own assumptions, and earns its confidence will be a more reliable thinking partner, an outcome that the entirety of the AI field is consistently pushing towards. It is the belief of this author that epistemic hygiene, combined with well structured prompt level scaffolding, will get us to this goal faster.

🔗 [Medium](https://medium.com/@socal21st.oc/epistemic-hygiene-and-how-it-can-reduce-ai-hallucinations-a025646c255d) • 4h ago

---

**[Created a free tool to check what PII your LLM prompts are leaking before they hit the provider](https://www.reddit.com/r/artificial/comments/1tbhvlq/created_a_free_tool_to_check_what_pii_your_llm/)**

Most people don't realize how much personal data ends up in their AI prompts without thinking about it. Customer names, medical details, internal company info. It all goes to the provider's servers. Free to use. Let me know how well this works. aisecuritygateway.ai/ai-leak-checker

10h ago

---

**[AI May Reshape Institutions More Than It Replaces Jobs](https://www.reddit.com/r/artificial/comments/1tb1299/ai_may_reshape_institutions_more_than_it_replaces/)**

I think the next big AI debate won’t be about intelligence. It will be about representation. Right now, most AI conversations focus on models: Which model is smarter, or which agent is faster/better or which AI can automate more work? But enterprises/institutions don’t fail because they lack intelligence alone. They fail because they represent reality poorly. A bank may have thousands of dashboards and still not understand customer risk properly. A government may collect massive amounts of data and still fail to represent what citizens are actually experiencing. A company may have advanced AI copilots while teams still operate on fragmented assumptions, outdated workflows, and conflicting versions of reality. That’s why I increasingly think the future architecture of AI systems may depend on three different layers: SENSE How reality is captured and represented. What signals are collected? Which entities matter? How is the state tracked over time/how are things over time? CORE How systems reason, optimize, and make decisions. This is the part most people currently call “AI.” DRIVER How decisions become legitimate action. Who authorized the action? Who is accountable? Can actions be reversed? What happens when the system is wrong? What recourse is available... A lot of current AI systems are becoming extremely strong at CORE while remaining weak in SENSE and DRIVER. Which creates a strange situation: Very intelligent systems… operating on incomplete representations… with unclear legitimacy boundaries. And maybe that’s why many AI pilots look amazing in demos but become messy inside real institutions. Because the challenge is no longer just intelligence. It’s whether institutions can reliably represent reality, reason over it, and act responsibly at scale. That feels less like a software upgrade. And more like a redesign of institutional architecture itself. Curious what others think about this...whether this is a valid point to think/discuss?

20h ago

---

**[Palantir to be granted ‘unlimited access’ to NHS patient data](https://www.reddit.com/r/artificial/comments/1tacllr/palantir_to_be_granted_unlimited_access_to_nhs/)**

The NHS is granting staff from companies including Palantir ‘unlimited access’ to identifiable patient data while working on its FDP.

🔗 [Digital Health](https://www.digitalhealth.net/2026/05/palantir-to-be-granted-unlimited-access-to-nhs-patient-data/) • 1d ago

---

**[The AI labs whose models are eroding democratic trust are the same labs now embedding themselves in government.](https://www.reddit.com/r/artificial/comments/1tbf0p9/the_ai_labs_whose_models_are_eroding_democratic/)**

This piece lays out a pretty dark cycle that goes way beyond "fake videos." AI companies are running a feedback loop where their tools destroy public trust in reality, and then they use that collapse to sell AI governance as the "objective" replacement for a broken democracy. Essentially: (OpenAI, Anthropic) make truth impossible to verify. - The exhaustion makes voters give up on human leaders. - The pivot is these same companies signing massive military and government contracts to run the state. The "Singularity" isn't a machine waking up; it’s a tired civilization handing the keys to a black box because we’re too burnt out to govern ourselves. Happy to hear your thoughts : https://aiweekly.co/issues/100-years-from-now-the-last-election Alexis

12h ago

---

**[I asked both chat gpt and claude to ask me a series of questions to evaluate if i need the](https://www.reddit.com/r/artificial/comments/1tbr449/i_asked_both_chat_gpt_and_claude_to_ask_me_a/)**

paid version of them, or if the free version is fine. Explain why. ChatGPT was free. Money hungry Claude wanted my CC info even though I use Claude a lot less

3h ago

---

---

## Google News: "ai"

**[A smarter, more proactive Android with Gemini Intelligence](https://blog.google/products-and-platforms/platforms/android/gemini-intelligence/)**

At the Android Show 2026, we introduced Gemini Intelligence, proactive new AI features on Android.

blog.google • 16h ago

---

**[Google races to put Gemini at the center of Android before Apple’s AI reboot](https://www.cnbc.com/2026/05/12/google-races-put-gemini-at-center-of-android-before-apples-ai-reboot.html)**

Google is using its latest Android rollout to position Gemini as the AI layer across phones, Chrome, laptops and cars.

CNBC • 14h ago

---

**[Shaping the future of AI interaction by reimagining the mouse pointer](https://deepmind.google/blog/ai-pointer/)**

Google DeepMind is transforming the mouse pointer into a context-aware AI partner. Move beyond the friction of traditional prompting with intuitive AI collaboration in Chrome and beyond.

Google DeepMind • 16h ago

---

**[China's Tencent sees boost from gaming, AI demand even as revenue comes in weaker than expected](https://www.cnbc.com/2026/05/13/tencent-q1-earnings-gaming-ai-demand-revenue-miss.html)**

The tech giant reported its first-quarter 2026 earnings on Wednesday.

CNBC • 44m ago

---

**[Tencent Revenue Miss Heightens Pressure for AI Payoff](https://www.bloomberg.com/news/articles/2026-05-13/tencent-revenue-miss-heightens-pressure-for-ai-payoff)**

Bloomberg.com • 1h ago

---

**[Tencent Maintains Double-Digit Profit Growth Amid Intensified AI Investment](https://www.wsj.com/business/earnings/tencent-maintains-double-digit-profit-growth-amid-intensified-ai-investment-7847e010)**

WSJ • 29m ago

---

**[Why Americans dread AI](https://www.ft.com/content/637f5664-44eb-4527-8369-9eec320cfdf0?syn-25a6b1a6=1)**

Silicon Valley encourages the view that the technology is unstoppable — and Trump seems to agree

Financial Times • 22h ago

---

**[AI executive action stalled by White House infighting](https://www.axios.com/2026/05/13/ai-executive-action-white-house-infighting)**

Axios • 12m ago

---

**[Opinion | The Shared Feeling of Being Harvested by the Future](https://www.nytimes.com/2026/05/12/opinion/us-china-ai-future.html)**

The New York Times • 1d ago

---

**[Seeking free money advice from AI? Don’t be so quick to upload any financial statements](https://www.cnn.com/2026/05/13/business/ai-financial-statements-money-advice)**

If you’re financially pressed, confused about money, or just want a little free help figuring out how to improve your cash flow, you may be tempted to use AI.

CNN • 14m ago

---

---

## HackerNews: "ai"

**[Local AI needs to be the norm](https://news.ycombinator.com/item?id=48085821)**

Local AI models should be the default.

⬆️ 1848 • 💬 736 • 2d ago • [unix.foo](https://unix.foo/posts/local-ai-needs-to-be-norm/)

---

**[If AI writes your code, why use Python?](https://news.ycombinator.com/item?id=48100433)**

For the last decade, fast-to-ship beat fast-to-run. Not anymore.

⬆️ 879 • 💬 933 • 1d ago • [Medium](https://medium.com/@NMitchem/if-ai-writes-your-code-why-use-python-bf8c4ba1a055)

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

⬆️ 264 • 💬 277 • 1d ago • [Martin's Blog](https://martin.sh/i-let-ai-build-a-tool-to-help-me-figure-out-what-was-waking-me-up-at-night/)

---

**[Google says criminal hackers used AI to find a major software flaw](https://news.ycombinator.com/item?id=48094641)**

⬆️ 241 • 💬 173 • 1d ago • [nytimes.com](https://www.nytimes.com/2026/05/11/us/politics/google-hackers-attack-ai.html)

---

**[Amazon employees are "tokenmaxxing" due to pressure to use AI tools](https://news.ycombinator.com/item?id=48110529)**

Workers are using an internal AI tool to automate non-essential tasks.

⬆️ 222 • 💬 226 • 17h ago • [Ars Technica](https://arstechnica.com/ai/2026/05/amazon-employees-are-tokenmaxxing-due-to-pressure-to-use-ai-tools/)

---

**[Reimagining the mouse pointer for the AI era](https://news.ycombinator.com/item?id=48111581)**

Google DeepMind is transforming the mouse pointer into a context-aware AI partner. Move beyond the friction of traditional prompting with intuitive AI collaboration in Chrome and beyond.

⬆️ 200 • 💬 167 • 16h ago • [Google DeepMind](https://deepmind.google/blog/ai-pointer/)

---

**[PS3 Emulator Devs Politely Ask That People Stop Flooding It with AI PRs](https://news.ycombinator.com/item?id=48089263)**

The team behind RPCS3 suggests that vibe-coders "learn how to debug and code" instead of "generating slop that you don't understand"

⬆️ 185 • 💬 145 • 2d ago • [Kotaku](https://kotaku.com/playstation-3-emulator-devs-politely-ask-that-people-stop-flooding-it-with-ai-code-pull-requests-2000694656)

---

**[Students boo commencement speaker after she calls AI next industrial revolution](https://news.ycombinator.com/item?id=48096674)**

A commencement speaker at the University of Central Florida was booed, with graduating humanities students yelling out, "AI SUCKS!"

⬆️ 173 • 💬 209 • 1d ago • [404 Media](https://www.404media.co/ucf-ai-commencement-speaker-booed/)

---

---

## YouTube Videos: "ai"

**[The First AI Cyberattack Has Happened...](https://www.youtube.com/watch?v=6TtKdKQlrqg)**

Hello guys and gals, it's me Mutahar again! This time we take a look at what appears to be a pretty huge day for the Internet.

📺 SomeOrdinaryGamers

👁️ 171K • 👍 8K • 💬 862 • ⏱️ 17:29 • 11h ago

---

**[AI Will Hit a Wall in 2026, if nothing changes.](https://www.youtube.com/watch?v=XA84pSrPHS0)**

Free GenSpark credits if you register here → http://www.genspark.ai/?utm_source=yt&utm_campaign=SabineHossenfelder ...

📺 Sabine Hossenfelder

👁️ 135K • 👍 7K • 💬 1K • ⏱️ 6:42 • 18h ago

---

**[Google Chrome Installs AI on Your PC WITHOUT Your Permission.](https://www.youtube.com/watch?v=gYY10vsbnlE)**

Google Chrome apparently installs a 4GB AI agent on your computer without explicit user permission to... something something...

📺 Clownfish TV

👁️ 37K • 👍 3K • 💬 745 • ⏱️ 17:46 • 1d ago

---

**[4 Ways to Make Money With Claude AI That Nobody Is Talking About](https://www.youtube.com/watch?v=wz9CmUZ4jRg)**

Go to https://surfshark.com/joshuamayo or use code JOSHUAMAYO at checkout to get 4 extra months of Surfshark VPN!

📺 Joshua Mayo

👁️ 7K • 👍 324 • 💬 20 • ⏱️ 25:52 • 17h ago

---

**[AI is wild now](https://www.youtube.com/watch?v=HITUpHglMv4)**

Asmongold's Twitch: https://www.twitch.tv/zackrawrr ▻ Asmongold's X: https://x.com/asmongold ▻ Asmongold's Kick: ...

📺 Asmongold TV  

👁️ 296K • 👍 14K • 💬 5K • ⏱️ 25:34 • 18h ago

---

**[Claude Mythos Just Crossed A Dangerous Line... AGAIN!](https://www.youtube.com/watch?v=i-ioLtvb19o)**

Claude Mythos may have just crossed one of the strangest lines in AI. A new METR evaluation reportedly puts Mythos around the ...

📺 AI Revolution

👁️ 43K • 👍 1K • 💬 149 • ⏱️ 15:57 • 1d ago

---

**[What happened to Anthropic?](https://www.youtube.com/watch?v=q4rDAu9ggKU)**

Get started with Greptile today https://greptile.com/go/berman 14 Day Free Trial! Download The 25 OpenClaw Use Cases eBook ...

📺 Matthew Berman

👁️ 53K • 👍 1K • 💬 331 • ⏱️ 16:24 • 14h ago

---

**[Trump-Xi summit expected to focus heavily on trade, AI](https://www.youtube.com/watch?v=x7UMmfydB7o)**

President Trump departed the White House for Beijing on Tuesday to attend a summit with Chinese President Xi Jinping.

📺 CBS News

👁️ 12K • 👍 75 • 💬 41 • ⏱️ 5:52 • 12h ago

---

**[The AI Chat Era Is Over. This Killed It.](https://www.youtube.com/watch?v=FJT5Rh0eKe8)**

Try Genspark with free credits available upon signup:* https://bit.ly/4njiP0c Unlimited AI chat and AI image for all paid users in ...

📺 Julia McCoy

👁️ 27K • 👍 1K • 💬 85 • ⏱️ 12:28 • 2d ago

---

**[&#39;No signs of AI slowing down&#39; — will it become a &#39;MACHINE GOD&#39;?](https://www.youtube.com/watch?v=jj05pc9tlc0)**

Should we think of AI as a co-intelligence and digital coworker rather than just a chatbot? Ethan Mollick, a professor at Wharton ...

📺 MS NOW

👁️ 6K • 👍 174 • 💬 95 • ⏱️ 58:06 • 20h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 535,069 • ❤️ 771 • 4d ago

---

**[ZAYA1-8B](https://huggingface.co/Zyphra/ZAYA1-8B)**

*Zyphra*

ZAYA1-8B is an efficient Mixture-of-Experts LLM (760M active params) excelling in mathematical and coding tasks, competitive with larger models. It's suitable for on-device deployment and high-performance inference.

`8.8B`

⬇️ 110,182 • ❤️ 458 • 1d ago

---

**[MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)**

*OpenBMB*

MiniCPM-V 4.6 is an ultra-efficient, pocket-sized multimodal LLM for edge deployment, excelling in image and video understanding with mixed visual token compression. It offers strong multimodal capabilities comparable to larger models while achieving superior computational efficiency and broad mobile platform support.

`image-text-to-text` `1.3B`

⬇️ 3,494 • ❤️ 434 • 1d ago

---

**[HiDream-O1-Image](https://huggingface.co/HiDream-ai/HiDream-O1-Image)**

*HiDream.ai*

HiDream-O1-Image is a unified transformer-based image generation model capable of text-to-image, image editing, and subject-driven personalization at resolutions up to 2048x2048. It features a pixel-level unified transformer architecture without external VAEs or disjoint text encoders, enabling high-fidelity generation and precise control.

`image-text-to-image` `8.8B`

⬇️ 7,747 • ❤️ 284 • 9h ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 2,420,384 • ❤️ 3,910 • 7d ago

---

**[Z-Anime](https://huggingface.co/SeeSee21/Z-Anime)**

*Sebastian Böhnke*

Z-Anime is a text-to-image diffusion model, fully fine-tuned on the Z-Image Base for generating high-quality, diverse anime-style visuals. It offers multiple variants optimized for speed, quality, and low-resource environments, supporting natural language prompts and full negative prompt capabilities.

`text-to-image` `6.2B`

⬇️ 11,486 • ❤️ 325 • 16d ago

---

**[supertonic-3](https://huggingface.co/Supertone/supertonic-3)**

*Supertone*

Supertonic 3 is a fast, on-device, multilingual text-to-speech model supporting 31 languages with ONNX Runtime for local inference. It offers high accuracy, low latency, and a compact size, suitable for applications requiring efficient, cloud-independent speech synthesis.

`text-to-speech`

⬇️ 4,954 • ❤️ 143 • 6d ago

---

**[gemma-4-31B-it-assistant](https://huggingface.co/google/gemma-4-31B-it-assistant)**

*Google*

Gemma 4 31B Dense is a multimodal LLM from Google DeepMind supporting text and image inputs with a 256K context window. It excels at reasoning, coding, and agentic tasks, offering optimized performance for low-latency applications via speculative decoding.

`any-to-any` `469.5M`

⬇️ 93,228 • ❤️ 223 • 2d ago

---

**[LTX2.3-10Eros](https://huggingface.co/TenStrip/LTX2.3-10Eros)**

*TenStrip*

LTX2.3-10Eros is a video generation model optimized for Image-to-Video (I2V) tasks, utilizing layer-scaled merges for enhanced prompt adherence and visual fidelity. It requires detailed, commanded input for motion, evolution, and audio, making it suitable for users needing precise control over generated video content, especially when combined with prompt enhancement techniques.

`image-to-video`

⬇️ 84,903 • ❤️ 239 • 2d ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 2,772,193 • ❤️ 1,262 • 19d ago

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

▲ 109 • 💬 10 • ⭐ 9,002 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 33 • 💬 3 • ⭐ 24,053 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 161 • 💬 2 • ⭐ 62,825 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 54 • 💬 1 • ⭐ 79,826 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 77 • 💬 7 • ⭐ 73,327 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

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

⭐ 2.9k • 🔱 844 • 15h ago

---

**[crynta/terax-ai](https://github.com/crynta/terax-ai)**

Lightweight (7MB) AI terminal emulator (ADE) built in Rust & Tauri & React

`TypeScript` `agents` `ai` `code-editor` `linux` `macos`

⭐ 2.7k • 🔱 270 • 8h ago

---

**[Manavarya09/design-extract](https://github.com/Manavarya09/design-extract)**

Extract any website's complete design system with one command. DTCG tokens, semantic+primitive+composite, MCP server for Claude Code/Cursor/Windsurf, multi-platform emitters (iOS SwiftUI, Android Compose, Flutter, WordPress), Tailwind v4, Figma variables, shadcn/ui, CSS health audit, WCAG remediation, Chrome extension. MIT, Playwright, Node 20+.

`JavaScript` `accessibility` `agent-skill` `ai` `chrome-extension` `claude-code-plugin`

⭐ 2.5k • 🔱 232 • 20h ago

---

**[earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad)**

A collection of agent skills for CAD, robotics and hardware design

`JavaScript` `3mf` `agents` `ai` `ai-agents` `build123d`

⭐ 2.5k • 🔱 290 • 3h ago

---

**[cosmicstack-labs/mercury-agent](https://github.com/cosmicstack-labs/mercury-agent)**

Soul-driven AI agent with permission-hardened tools, token budgets, and multi-channel access. Runs 24/7 from CLI or Telegram.

`TypeScript` `ai-agent` `ai-assistant` `llm`

⭐ 2.2k • 🔱 221 • 2d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.1k • 🔱 136 • 5h ago

---

**[bergside/design-md-chrome](https://github.com/bergside/design-md-chrome)**

Chrome extension to extract styles from any website and generate DESIGN.md files and design skills for AI based on TypeUI

`JavaScript` `ai` `chrome` `chrome-extension` `claude` `claude-design`

⭐ 1.9k • 🔱 242 • 18d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 1.9k • 🔱 293 • 5d ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D cell generation and exploration studio.

`JavaScript`

⭐ 1.8k • 🔱 302 • 6h ago

---

---

*Generated by PeekDeck - A glance is all you need*
