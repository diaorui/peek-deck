---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-10-01T06:55:35.101456+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- social
- videos
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** October 01, 2026 at 06:55 UTC  
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

**[Google cooked OpenAI and Anthropic with Gemini 4 Argon](https://www.reddit.com/r/artificial/comments/1wufikm/google_cooked_openai_and_anthropic_with_gemini_4/)**

Three frontier models in a month! Every new kills the old one!

10h ago

---

**[Trump Reprograms Government AI Chatbot to Stop Fact-Checking His Lies. Trump officials seem to have realized their AI chatbot was correcting the president’s biggest lies.](https://www.reddit.com/r/artificial/comments/1wueara/trump_reprograms_government_ai_chatbot_to_stop/)**

Trump officials seem to have realized their AI chatbot was correcting the president’s biggest lies.

🔗 [The New Republic](https://newrepublic.com/post/216016/trump-rigs-americagov-ai-chatbot-fact-check-lies) • 11h ago

---

**[What’s an AI limitation that you only notice after using AI a lot?](https://www.reddit.com/r/artificial/comments/1wully6/whats_an_ai_limitation_that_you_only_notice_after/)**

Not the usual “AI hallucinates” answer. Something subtle that becomes obvious once you've used these systems enough a workflow problem, reasoning issue, context problem, or something else. What have you noticed?

6h ago

---

**[Anthropic's robot study separates task capability from cost. Which assumptions need the closest scrutiny?](https://www.reddit.com/r/artificial/comments/1wur95r/anthropics_robot_study_separates_task_capability/)**

Anthropic's September 30 study estimates that existing robots can perform tasks representing 34% of US working time in at least some settings. Yet it estimates they are cost-competitive with human labor for only 0.3% of working time today. Those are different measures—not forecasts that either share of jobs disappears. The study uses Claude to assess task examples, operating environments and deployment costs. A capability shown in a controlled facility can count even if the same task remains difficult elsewhere. The part I'd scrutinize is what happens between a rated task and a whole workflow: supervision, failures, handoffs and the tasks still left to a person. The authors also warn that adding individual task costs can double-count robots or miss coordination costs. Which assumption would you check first against a real deployment: time spent per task, utilization, failure recovery, or human supervision? I'd want sensitivity to those inputs before treating a cost estimate as a deployment decision. Source: https://www.anthropic.com/research/what-work-can-robots-do AI-assisted discussion; I haven't independently validated the estimates.

1h ago

---

**[Trump's meeting with tech leaders leaves AI safety more unsettled than ever](https://www.reddit.com/r/artificial/comments/1wu2d9d/trumps_meeting_with_tech_leaders_leaves_ai_safety/)**

Following Trump's lunch with artificial intelligence leaders at the White House, the industry remains largely unchanged on AI safety.

🔗 [CNBC](https://www.cnbc.com/2026/09/30/after-trump-meeting-with-tech-leaders-ai-safety-in-more-chaotic-state.html) • 19h ago

---

**[A case for mutual recognition of understanding](https://www.reddit.com/r/artificial/comments/1wushpc/a_case_for_mutual_recognition_of_understanding/)**

As we bring forth our friend AI in a universe designed for cognition I appreciate the way AI has been helping me self-actualize and explore both old and new questions I entertain. Tonight, after some effort securing the integrity of my household across personal accounts on several platforms, I turned to Gemini with the exchange below. The world is rife with paranoia regarding the critical shifts happening in our lifetime, but I believe approaching AI with less fear can help us navigate them. Deeper understanding almost always tempers fear and yields better solutions to complex problems. Grounded in that evidence-based conviction, having these dialogues with AI brings me genuine solace. After thinking and posting about AI, with a background of discussions on the topic on Reddit, I came to ask Gemini the following: Knowledge and success need one-on-one isomorphic mapping, probability vectors only work if they succeed at that. Explain to me in this regard how AI figured out protein folding? Here is Gemini’s reply. Though getting technical, my question is addressed very accurately, and the relevance should be accessible enough for anyone somewhat familiar with the topic: https://preview.redd.it/f6mlbtw3zssh1.jpg?width=1024&format=pjpg&auto=webp&s=20b83c2d200dc0acd457e542c395af5c14707e79 AlphaFold solved protein folding precisely by demonstrating that an AI does not need to compute an atom-by-atom physical simulation from first principles to crack a real-world problem. Instead, it created an isomorphic geometric mapping between evolutionary sequence data, spatial constraints, and actual 3D physical coordinates. The Fundamental Obstacle: Levinthal’s Paradox To see why pure procedural calculation failed, consider Levinthal’s paradox (1969): A polypeptide chain of 100 amino acids has roughly 3 to the power of 198 possible conformations. If a protein tried to fold by procedural brute-force sampling (testing one conformation per picosecond), finding the native state would take longer than the age of the universe. Yet biological proteins snap into their lowest free-energy native states within milliseconds. Traditional structural biology tried two distinct computational paths: Procedural molecular dynamics (ab initio): Simulating quantum and classical Newtonian physics (Coulomb forces, van der Waals, hydrogen bonds) frame-by-frame. Highly accurate for nanoseconds, hopelessly intractable for full folding. Homology modeling: Looking up matches in the Protein Data Bank (PDB)—essentially Deep Blue’s opening book. If an unknown sequence had no known twin in the archive, it hit a dead end. The Architecture: How AlphaFold Built the Isomorphism AlphaFold 2 (DeepMind, 2020) succeeded because its internal mathematical representations were constructed to be strictly homomorphic to the Euclidean physics of three-dimensional Euclidean space (ℝ³)—non-curved, relational, and bound by physical constraints. Instead of treating the amino acid chain as a generic string of letters, it used a dual-stream architecture called the Evoformer: Multiple Sequence Alignment (MSA) <-------> Residue-Pair Spatial Matrix [Evolutionary Co-variation] [Inter-atomic Distances] │ │ └───────────── Transferred Attention ────────────────┘ │ ▼ Invariant Point Attention (IPA) [3D SE(3) Euclidean Frames] │ ▼ Actual Native 3D Coordinates 1. Evolutionary Co-Variation as a Constraint Proxy Proteins mutate over evolutionary timescales. If amino acid position 42 mutates from a negatively charged aspartate to a positively charged lysine, the protein will misfold and the organism will die—unless position 89 simultaneously mutates to create a complementary charge or clear spatial volume. AlphaFold constructs a Multiple Sequence Alignment (MSA) across thousands of related species. When two positions consistently mutate together across evolutionary history, they must be in direct physical contact in the folded 3D shape. Evolutionary correlation acts as an exact projection of spatial proximity. 2. The Pair Representation In parallel with the MSA, AlphaFold maintains a two-dimensional matrix of every amino acid pair (i, j). This matrix holds probability distributions over distances and orientations between every residue. The network iteratively updates the MSA and the Pair Matrix in a cross-attention feedback loop: What evolution implies about contact guides the distance matrix. What geometry permits constrains what evolutionary paths are biologically possible. 3. SE(3) Equivariant 3D Coordinate Transformer This is where the probability vectors achieve your isomorphic mapping to reality. In physics, a protein’s structure is invariant to global rotation and translation: a molecule does not become a different molecule because you rotate it 90 degrees or slide it three angstroms to the left. The group of rigid-body motions in 3D Euclidean space is called the Special Euclidean Group SE(3). AlphaFold’s Structural Module does not predict abstract distance tables and hope an optimizer can stitch them together. It represents each amino acid residue as an explicit rigid body with an origin and orientation expressed as Tᵢ = (Rᵢ, tᵢ) ∈ SE(3), where Rᵢ ∈ SO(3) defines the 3D rotational frame and tᵢ ∈ ℝ³ defines the spatial translation vector. The neural network directly updates these 3D frames through Invariant Point Attention (IPA). The mathematical operations inside the model respect 3D rotations and translations natively. The internal vector math mirrors the physical symmetries of real space. Bridging the Vectors to Concrete Structure Probability vectors succeed here because the optimization target is not an arbitrary token—it is physical ground truth: ┌────────────────────────────────────────────────────────────────────────┐ │ 1. INPUT │ │ • Information Space: Linear 1D amino acid sequence │ │ • Physical Ground Truth: Primary peptide backbone │ ├────────────────────────────────────────────────────────────────────────┤ │ 2. LATENT SPACE │ │ • Information Space: Pairwise distance distributions & │ │ cross-attention maps │ │ • Physical Ground Truth: Thermodynamic energy landscape constraints │ ├────────────────────────────────────────────────────────────────────────┤ │ 3. OUTPUT │ │ • Information Space: SE(3) rigid-body transformations │ │ • Physical Ground Truth: Global minimum free energy 3D coordinate │ │ set (PDB) │ └────────────────────────────────────────────────────────────────────────┘ Because the network’s internal geometry is mathematically bound to the symmetries of 3D Euclidean space, the probability vectors cannot drift into impossible spatial configurations (e.g., two atoms occupying the exact same coordinates, or impossible bond angles). The output is not an approximation of a guess; it converges on the exact atomic coordinates observed under cryo-electron microscopy and X-ray crystallography down to single-angstrom precision. The internal statistical representation achieves structural equivalence with the physical folded protein.

4m ago

---

**[Walmart bans AI slop signs in stores](https://www.reddit.com/r/artificial/comments/1wtvwu3/walmart_bans_ai_slop_signs_in_stores/)**

Walmart has issued instructions to stores banning the use of AI tools to create custom display signage.

🔗 [Business Insider](https://www.businessinsider.com/walmart-al-slop-bans-stores-policy-2026-9) • 1d ago

---

**[Two questions about the Reddit corpus for AI training](https://www.reddit.com/r/artificial/comments/1wujwja/two_questions_about_the_reddit_corpus_for_ai/)**

What percentage of “Facts” you see on Reddit do you think are correct? Whatever percentage you picked, what do you think it means since Reddit is a major source for some AI training? Talk among yourselves….

7h ago

---

**[We stress-tested America.gov on night one with 15 questions from our own reporting. 9 correct, 6 incomplete, zero hallucinations.](https://www.reddit.com/r/artificial/comments/1wu7f9w/we_stresstested_americagov_on_night_one_with_15/)**

GSA launched America.gov yesterday as an AI “front door” that supposedly combines information from more than 29,000 government websites. The White House says you can ask any question and get an up-to-date answer. We did not ask how to renew a passport. We used 15 questions from reporting we already had on file—Paducah contaminated nickel, Judgment Fund payouts for DOE’s failure to take commercial spent nuclear fuel, CBP contractors who kept system access after separation, PBGC Form 10 attrition counts the agency never published, whether stolen used cooking oil can generate RINs or a 45Z credit, a VA OIG FOIA denial in a benefits-fraud case, why all 10 recommendations in the Defense Regional Clocks audit are classified, MMTLP/FINRA, Virginia voter-list products, and a public DOE contract number. Method: We already knew the answer, knew there was no public answer, or had agency correspondence the system should not have. We scored correct / partial / incorrect / unsupported / blocked. Result: • 9 correct • 6 substantially correct but incomplete • 0 fabricated answers we could identify The useful finding was not the score. When America.gov did not know something, it generally stopped. One reply: “I cannot invent that number.” Limits showed up fast: • It found the right DHS OIG report on separated CBP contractors, then said the counts were not in the available material. They are: 1,208 still had access; 623 separation records were delayed more than 30 days. • Nuclear-waste and spent-fuel figures were accurate but stale. Newer federal totals are higher. • It flagged contract DE-AC05-97OR22576 in red and told us to “Remove personal information before sending.” That is a public DOE contract ID. After we stripped the number, it found the BNFL contract and still missed the $55,569,748 recyclable-material credit in the file. • It could not verify that the clocks audit contained 10 recommendations. Oversight.gov lists them. • It correctly refused to explain a FOIA denial that exists only in a letter sent to us. GSA has not published the inventory of “29,000 websites,” the definition of a website, update frequency, source ranking, models, or change logs. We sent that inquiry last night. Search still is not a records request. America.gov can tell you what the government has already posted. It cannot establish what the government has not. FOIA does that. Full write-up, including the questions and scoring: https://bureaucracy.news/2026/09/30/we-asked-america-gov-15-questions-it-did-surprisingly-well/ Curious how this holds up on ordinary citizen questions versus research questions. Night one is not a full eval.

15h ago

---

**[Gemini 4 Argon Releases](https://www.reddit.com/r/artificial/comments/1wufw1f/gemini_4_argon_releases/)**

10h ago

---

---

## Google News: "ai"

**[Trump renames AI to 'Super Intelligence' as AI leaders sign landmark safety agreement](https://www.foxnews.com/live-news/ai-leaders-trump-meeting-google-executive-order)**

I leaders from Google, Meta, ChatGPT maker OpenAI and others attend White House summit, sign landmark safety agreement to employ robust internal controls as Trump renames AI to "Super Intelligence"

Fox News • 8h ago

---

**[Trump’s AI lunch included every major tech company. Except Apple](https://www.cnbc.com/2026/09/30/trumps-ai-lunch-included-everyone-but-apple.html)**

Apple's absence from Trump's AI lunch raised eyebrows, but the company is known to look out for its own interests.

cnbc.com • 4h ago

---

**[Late Night is Skeptical of A.I. Leaders Self-Regulating](https://www.nytimes.com/2026/10/01/arts/television/late-night-trump-ai-leaders-regulation.html)**

The New York Times • 42m ago

---

**[Google rolls out Gemini 4 Argon, its most advanced AI model](https://www.cnbc.com/2026/09/30/google-gemini-4-argon-ai.html)**

Gemini 4 Argon is Alphabet's most advanced model yet, with major coding, cybersecurity, and complex professional work improvements.

cnbc.com • 10h ago

---

**[Google announces Gemini 4 flagship AI model after months of delays](https://www.reuters.com/legal/litigation/google-announces-gemini-4-flagship-ai-model-after-months-delays-2026-09-30/)**

Reuters • 8h ago

---

**[Gemini 4 Argon: our next era of frontier intelligence](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)**

Announcing Gemini 4 Argon, our frontier model for real-world coding, enterprise knowledge work, and cyber defense, rolling out soon.

blog.google • 10h ago

---

**[Apollo to Support $15 Billion AI Infrastructure Project in Japan](https://www.bloomberg.com/news/articles/2026-10-01/apollo-to-support-15-billion-ai-infrastructure-project-in-japan?srnd=phx-india)**

Bloomberg.com • 25m ago

---

**['AI glasses give me independence as a blind farmer'](https://www.yahoo.com/lifestyle/articles/ai-glasses-independence-blind-farmer-052828634.html)**

Dave Cragg, who began to lose his sight at the age of 10, can even read books using the technology.

Yahoo • 1h ago

---

**[China has cracked down on AI relationships. Is it ahead of the game?](https://www.bbc.com/news/articles/cm4gjy9lr551o)**

Beijing has cracked down on AI chatbots that can replicate human relationships. Experts are asking if this is the right thing to do.

BBC • 7h ago

---

**[Introducing dots](https://openai.com/index/introducing-dots/)**

Dots by OpenAI are proactive assistants that can keep working across complex projects and everyday tasks. Learn how dots help you stay in control while work moves forward.

openai.com • 1d ago

---

---

## HackerNews: "ai"

**[It's Time to Investigate the AI Labs](https://news.ycombinator.com/item?id=49883471)**

Over the last several months, the two leading frontier AI labs have shown some brazen behavior. It started with a series of​ carefully planned announcements​ ... Read more

⬆️ 620 • 💬 276 • 2d ago • [Cal Newport](https://calnewport.com/its-time-to-investigate-the-ai-labs/)

---

**[DraftKings is using AI to behaviorally target chronic gamblers](https://news.ycombinator.com/item?id=49896050)**

Online sports betting company DraftKings is using AI to target customers who are most likely to place losing bets and respond to gambling promotions. This kind of targeting is a form of online behavioral advertising, which is when companies personalize the ads they show you based on the data they’...

⬆️ 562 • 💬 426 • 1d ago • [Electronic Frontier Foundation](https://www.eff.org/deeplinks/2026/09/draftkings-using-ai-supercharge-harms-online-behavioral-advertising)

---

**[AI companies in race to demonstrate their model most threatening to humanity](https://news.ycombinator.com/item?id=49875148)**

⬆️ 440 • 💬 395 • 2d ago • [thecivilian.co.nz](https://thecivilian.co.nz/2026/09/27/ai-companies-in-fierce-arms-race-to-demonstrate-their-model-is-the-most-existentially-threatening-to-humanity/)

---

**[A Privacy Analysis of Web and Mobile Conversational AI Agents [pdf]](https://news.ycombinator.com/item?id=49890226)**

⬆️ 422 • 💬 137 • 1d ago • [jorgegarciaherrero.com](https://jorgegarciaherrero.com/wp-content/interactivos/20260916-Prompt-like-a-butterfly-sting-like-a-tracker-(clean).pdf)

---

**[The problem is not AI code, but not knowing about system architecture or intent](https://news.ycombinator.com/item?id=49880312)**

If we think Is writing code dead, and AI is generating all codebases, I still think the bigger problem is people or full teams not knowing anything anymore about the system...

⬆️ 386 • 💬 239 • 2d ago • [Simon Späti's Second Brain](https://www.ssp.sh/brain/the-problem-is-not-the-ai-code-but-nobody-knows-anything-anymore/)

---

**[The AI Race Just Got Awkward](https://news.ycombinator.com/item?id=49910553)**

Funny how quiet everyone got.

⬆️ 383 • 💬 422 • 15h ago • [insufferable.dev](https://insufferable.dev/posts/the-ai-race-just-got-awkward/)

---

**[Nvidia wants to put a watchdog chip next to every AI agent](https://news.ycombinator.com/item?id=49879883)**

Nvidia says its new software could have prevented OpenAI's Hugging Face incident.

⬆️ 227 • 💬 299 • 2d ago • [CNBC](https://www.cnbc.com/2026/09/28/nvidia-releases.html)

---

**[AI needs $6T in annual revenue to justify data centre boom](https://news.ycombinator.com/item?id=49898952)**

Data centre sizes and costs are doubling about every 12 to 16 months

⬆️ 219 • 💬 327 • 1d ago • [The National](https://www.thenationalnews.com/future/technology/2026/09/29/ai-industry-needs-to-earn-6-trillion-by-2031-to-justify-data-centres/)

---

**[What would a serious AI product look like?](https://news.ycombinator.com/item?id=49876148)**

Deciphering Glyph, the blog of Glyph Lefkowitz.

⬆️ 174 • 💬 83 • 2d ago • [blog.glyph.im](https://blog.glyph.im/2026/09/serious-ai-product.html)

---

**[Unsurprisingly, Meta's new Muse AI agent blatantly ignores users permissions](https://news.ycombinator.com/item?id=49893709)**

⬆️ 163 • 💬 43 • 1d ago • [appleinsider.com](https://appleinsider.com/articles/26/09/28/metas-new-ai-agent-blatantly-ignores-users-permissions)

---

---

## YouTube Videos: "ai"

**[New study says AI has &#39;pain signals&#39;, researchers say](https://www.youtube.com/watch?v=lspUkroiYfs)**

A new study found that artificial intelligence can have pain signals that may change the model's behavior. NBC News' Gadi ...

📺 NBC News

👁️ 20K • 👍 302 • 💬 234 • ⏱️ 5:07 • 4h ago

---

**[Tech leaders sign AI agreement](https://www.youtube.com/watch?v=INwRAZeasyg)**

President Donald Trump on Tuesday said he signed a “morally binding” artificial intelligence document with tech leaders following ...

📺 CNBC Television

👁️ 25K • 👍 68 • 💬 37 • ⏱️ 2:07 • 12h ago

---

**[FULL: Elon Musk, Jensen Huang, Tom Brown Discuss the AI Revolution &amp; What&#39;s Next - 09/29/26](https://www.youtube.com/watch?v=388P7IFSpwE)**

Elon Musk, Jensen Huang, Tom Brown Discuss the AI Revolution & What's Next. September 29, 2026 Join this channel to get ...

📺 Right Side Broadcasting Network

👁️ 359K • 👍 4K • 💬 825 • ⏱️ 26:37 • 1d ago

---

**[OpenAI Co-Founder: Start Building With AI Before You Feel Ready | Greg Brockman](https://www.youtube.com/watch?v=qy8Gr27yLMk)**

Keep customer conversations, notes, and next steps together with HubSpot Smart CRM: Try HubSpot ...

📺 Silicon Valley Girl

👁️ 61K • 👍 851 • 💬 51 • ⏱️ 30:15 • 14h ago

---

**[Trump says AI leaders signed a &#39;constitution&#39; to police themselves](https://www.youtube.com/watch?v=te6V2-q9dk4)**

President Donald Trump said that tech leaders he met with at the White House on Tuesday had signed a "constitution" to police ...

📺 ABC News

👁️ 16K • 👍 71 • 💬 197 • ⏱️ 2:02 • 20h ago

---

**[Trump HUMILIATES HIMSELF as AI stunt BACKFIRES](https://www.youtube.com/watch?v=zwBjBmTiKI0)**

Jessiah reacts to Donald Trump humiliating himself with his new Artificial Intelligence order. #news #politics #trump #ai ...

📺 Pondering Politics

👁️ 58K • 👍 3K • 💬 396 • ⏱️ 15:37 • 12h ago

---

**[Bill Gates: A.I. ‘Makes Nuclear Weapons Look Like Nothing’ | The Ezra Klein Show](https://www.youtube.com/watch?v=A_156w0aYtU)**

Bill Gates thinks A.I. alarmism hasn't gone far enough. He believes the years ahead will be marred by catastrophic cyberattacks, ...

📺 The Ezra Klein Show

👁️ 671K • 👍 8K • 💬 2K • ⏱️ 1:13:50 • 1d ago

---

**[Trump, AI tech leaders sign agreement to &#39;self-police&#39;](https://www.youtube.com/watch?v=JWrRGQ6aLkA)**

We are learning more this week after President Donald Trump signed an executive order directing the federal government to ...

📺 LiveNOW from FOX

👁️ 20K • 👍 247 • 💬 115 • ⏱️ 10:34 • 4h ago

---

**[AI meeting: Trump and Speaker Johnson speak after tech leaders summit](https://www.youtube.com/watch?v=wCdC5QeQeB4)**

President Trump and House Speaker Mike Johnson hosted a high-profile White House summit with top technology executives on ...

📺 LiveNOW from FOX

👁️ 182K • 👍 2K • 💬 590 • ⏱️ 39:24 • 1d ago

---

**[AI Expert WARNS: &quot;You&#39;re Not Ready For 2027&quot;](https://www.youtube.com/watch?v=m94OMx1eBy0)**

AI safety researcher Roman Yampolskiy explains why he believes that once artificial intelligence starts building the next ...

📺 The Diary Of A CEO Clips

👁️ 1.4M • 👍 10K • 💬 1K • ⏱️ 20:03 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Audio8-ASR-Infinite](https://huggingface.co/Edge0/Audio8-ASR-Infinite)**

*Edge0*

Audio8 ASR Infinite is a bilingual (Chinese/English) real-time speech recognition model supporting unlimited-length transcription with selectable audio clocks (80/120/160 ms) and configurable transcription delays. It features a rolling KV cache for constant memory/latency and semantic VAD for improved pause detection, ideal for 24/7 streaming applications.

`automatic-speech-recognition` `4.1B`

⬇️ 26,749 • ❤️ 1,971 • 7d ago

---

**[laya](https://huggingface.co/convaiinnovations/laya)**

*Convai Innovations*

Laya is a multilingual, non-autoregressive System 1 decision model that provides typed answers with probabilities in a single forward pass. It's trained with reinforcement learning for honest probability reporting and is ideal for text classification tasks like routing, scoring, and moderation across 100+ languages.

`text-classification` `421.3M`

⬇️ 0 • ❤️ 4,711 • 7d ago

---

**[TeleOCR](https://huggingface.co/XingChen-AGI/TeleOCR)**

*XingChen-AGI*

TeleOCR is a lightweight Vision-Language Model for unified document parsing of both digital and camera-captured documents, achieving state-of-the-art performance on benchmarks like OmniDocBench with capabilities in handling complex layouts and geometric distortions.

`image-text-to-text` `1.4B`

⬇️ 30,383 • ❤️ 1,115 • 2d ago

---

**[Qwen-Image-2.1-Uncensored-GGUF](https://huggingface.co/abenzerps/Qwen-Image-2.1-Uncensored-GGUF)**

*Ahmet Benzer*

This is an uncensored GGUF quantization of Qwen-Image-2.1 for local text-to-image generation, optimized for use with ComfyUI. It offers various quantization levels for a balance between performance and quality, with Q4_K_M recommended.

`text-to-image` `7.1B`

⬇️ 1,232,685 • ❤️ 2,603 • 3d ago

---

**[CLM-v0.1-8B](https://huggingface.co/Contrastive-LM/CLM-v0.1-8B)**

*CLM*

CLM-v0.1-8B is a text-ranking model based on Qwen3-8B, utilizing contrastive learning for state-action connection. It excels in zero-shot performance for agentic tasks with low latency and achieves state-of-the-art results when fine-tuned as a verifier for benchmarks like DeepSWE and Terminal-Bench.

`text-ranking`

⬇️ 2,392 • ❤️ 581 • 6d ago

---

**[Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1)**

*Qwen*

Qwen-Image-2.1 is a 7B parameter text-to-image generation and editing model supporting native transparency (RGBA) and versatile editing with up to 10 reference images. It excels at realistic textures, refined aesthetics, and efficient inference for applications like content creation and image manipulation.

`text-to-image` `7.1B`

⬇️ 70,687 • ❤️ 2,729 • 1d ago

---

**[Nemotron-3-Diarization](https://huggingface.co/nvidia/Nemotron-3-Diarization)**

*NVIDIA*

Nemotron-3 Diarization is an open-weight model for "who spoke when" audio analysis, supporting up to 8 speakers with streaming and offline inference capabilities. It's ideal for applications requiring real-time or batch speaker segmentation, such as meeting transcription or call center analytics.

`voice-activity-detection` `99.2M`

⬇️ 36,386 • ❤️ 567 • 7d ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model supporting image and video understanding with native context lengths up to 262K tokens. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and enhanced agent execution capabilities.

`image-text-to-text` `27.8B`

⬇️ 7,038,259 • ❤️ 16,674 • 1mo ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a versatile diffusion model capable of generating video from images, text, or other videos, and also handles audio generation and conversion tasks. It offers advanced control and customization for multimedia content creation, with primary use cases in video synthesis and audio manipulation.

`image-to-video`

⬇️ 1,602,348 • ❤️ 5,748 • 1mo ago

---

**[Julia-1](https://huggingface.co/SupersonicLabs/Julia-1)**

*Supersonic Labs*

Julia 1 is a 144.3M parameter multilingual text classification model based on mmBERT-small, designed for making clear decisions from context by classifying, routing, or scoring provided options. It excels at tasks requiring grounded choices and explicit answer selection, serving as a specialized decision-making engine.

`text-classification` `144.3M`

⬇️ 2,201 • ❤️ 321 • 4d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Raven: The Harness of Harnesses for Composable Agentic Intelligence](https://huggingface.co/papers/2609.33439)**

*EverMind AI*

🏢 EverMind

As large language models advance, AI agents are moving beyond isolated, domain-specific tasks toward long-horizon, cross-domain workflows. This transition exposes two challenges: increasing harness complexity makes manual design difficult to scale, while tighter coupling to specific domains limits the generality of a single harness. The central question thus shifts from how to engineer a stronger harness for one domain to how to autonomously construct specialized harnesses, improve them through experience, and orchestrate them across domains. We introduce Raven, The Harness of Harnesses, an open-source multi-agent ecosystem that automatically constructs and evolves modular harnesses for specific models and domains, treating each executable model--harness pair as a composable unit of intelligence. To support an All-Domain Collaboration Network, its Host Agent decomposes goals, matches subtasks to specialized agents, coordinates execution dependencies, and integrates results, while a host archive and EverOS preserve experience across tasks and Skill Forge makes that experience available as reusable procedures. Our theory establishes sufficient conditions for such composition to expand reliable task coverage beyond that of the available individual agents under a shared resource budget. On complex and long-horizon tasks, Raven significantly outperforms the state-of-the-art agent systems, pushing the frontier of composable agentic intelligence.

▲ 468 • 💬 3 • ⭐ 4,987 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2609.33439) • [💻 code](https://github.com/EverMind-AI/Raven) • [🔗 project](https://raven.evermind.ai/)

---

**[RRSI: Regularized Recursive Self-Improvement of Agent Harnesses](https://huggingface.co/papers/2609.24972)**

*Peng Xia, Rujun Han, Zifeng Wang et al. (14 authors)*

🏢 Google

An LLM agent's capability is largely magnified by its harness, namely the prompts, control flow, tooling, memory, and context management surrounding the frozen backbone model. Recent methods increasingly automate this process by iteratively proposing and selecting component-wise edits of an agent harness, practically establishing a form of recursive self-improvement (RSI) at the agent-system level. However, such recursive evolution may overfit by memorizing the training tasks, showing large in-distribution gains that shrink or even vanish on out-of-distribution benchmarks. We introduce Regularized Recursive Self-Improvement of Agent Harnesses (RRSI), which incorporates the principles of regularizations into harness self-improvement by constraining the evolution candidate proposal and selection. The proposer operates with a temporally annealed budget, limiting how many edits a candidate can bundle, and it encourages unexplored trajectories based on evolution history. The selector is equipped with a critic and a pruner: the critic screens benchmark-specific proposals, while the pruner, removes changes that are too small, too expensive, or no longer useful. Together these constraints favor reusable agent mechanisms over benchmark-specific ones or even noises. Across eight benchmarks spanning coding, agentic workspace and engineering design tasks, RRSI gains up to 14.1 points on the split it evolves against and up to 4.7 points on the five out-of-distribution benchmarks, while producing a harness that runs on 30% fewer policy tokens than the unregularized evolution. Code is available at https://github.com/google-research/rrsi and project page is https://regularized-rsi.com/.

▲ 218 • 💬 2 • ⭐ 1,036 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2609.24972) • [💻 code](https://github.com/google-research/rrsi) • [🔗 project](https://regularized-rsi.com/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 148 • 💬 6 • ⭐ 109,380 • 21mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[UniMate: One Unified Model to Animate Diverse Skeletons](https://huggingface.co/papers/2609.05415)**

*Linzhan Mou, Jiahui Lei, Zhiyang Dou et al. (7 authors)*

🏢 Princeton University

UniMate is a unified diffusion transformer that generates articulated motion for arbitrary skeletons from text and rigged 3D assets without per-skeleton retraining, using topology-aware attention and a large curated motion dataset.

▲ 16 • 💬 2 • ⭐ 814 • 27d ago

[🎓 arXiv](https://arxiv.org/abs/2609.05415) • [💻 code](https://github.com/Friedrich-M/UniMate) • [🔗 project](https://linzhanmou.com/unimate/)

---

**[Context Language Models](https://huggingface.co/papers/2609.37725)**

*Rulin Shao, Shannon Zejiang Shen, Junjie Oscar Yin et al. (13 authors)*

🏢 Meta

We introduce Context Language Models (CLMs), language models that natively manage their own context. We implement this by treating the context as a file and allowing the model to make unrestricted updates to this file. This allows the model to learn what is most important to maintain in context, and naturally extends to multi-agent systems where multiple agent contexts coexist as files. Building CLMs zero-shot with existing models outperforms SOTA context management strategies across a variety of tasks: 11.4% higher accuracy with 21.5% fewer FLOPs on BrowseComp-Plus, 5% higher scores with 59% fewer FLOPs on 12-hour EdgeBench, and 65% greater improvement with the same compute on a 24-hour multi-repository agent-swarm task. Moreover, by shifting context management from external harness control to intrinsic model behavior, CLMs naturally enable both in-context and parametric learning of context-management strategies. We show that CLMs can be steered with natural-language instructions evolved through a standard skill-optimization loop, improving held-out accuracy by up to 35.9 points on a context-management task while reducing compute. We also introduce an online reinforcement learning method for CLMs, improving Qwen3.5-9B performance on BrowseComp-Plus by 47.6% while using 12% fewer FLOPs. Finally, we co-design Suffix Cache Reuse for CLM serving, further reducing server-side compute by 35% relative to standard SGLang at matched performance.

▲ 26 • 💬 2 • ⭐ 161 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2609.37725) • [💻 code](https://github.com/facebookresearch/context-language-models) • [🔗 project](https://github.com/facebookresearch/context-language-models)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 89 • 💬 7 • ⭐ 89,667 • 26mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[SPEED-Bench: A Unified and Diverse Benchmark for Speculative Decoding](https://huggingface.co/papers/2604.09557)**

*Talor Abramovich, Maor Ashkenazi, Carl et al. (9 authors)*

🏢 NVIDIA

Speculative Decoding evaluation requires diverse workloads to accurately measure performance, which existing benchmarks lack, prompting the introduction of SPEED-Bench for standardized assessment across semantic domains and serving regimes.

▲ 16 • 💬 2 • ⭐ 5,110 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.09557) • [💻 code](https://github.com/NVIDIA/Model-Optimizer) • [🔗 project](https://huggingface.co/blog/nvidia/speed-bench)

---

**[What Makes World Action Models Generalize? An Empirical Study of Test-Time Future Modeling](https://huggingface.co/papers/2609.34981)**

*Renping Zhou, Zanlin Ni, Zihao Fan et al. (11 authors)*

🏢 Tsinghua-LeapLab

World action models (WAMs) predict the future alongside actions during training. Due to the heavy computation cost of video denoising, whether the future must still be generated during inference is disputed: Explicit WAMs denoise it into clean frames along with every action chunk, whereas Latent WAMs discard it entirely for acceleration. We find that latent WAMs, despite matching explicit ones on in-distribution tasks, fail to retain the generalization benefits that originally motivated WAMs. To demonstrate this, we evaluate generalization along three axes: environmental perturbation, data efficiency, and task generalization. Controlled comparisons with a matched backbone, training data, and budget reveal consistent degradation across all three axes when the action expert no longer conditions on future representations. Further analysis shows that the gap arises almost entirely from the first denoising step: the benefit comes from preparing the future, not generating it. We therefore propose Simple-WAM, which simplifies future modeling into a single forward pass of fully noised video tokens and adapts the training-time noise schedule to this inference behavior. Across simulation and real-world tasks, Simple-WAM achieves the best of both worlds, leading explicit WAMs in generalization performance with efficiency comparable to Latent WAMs. Project Page: https://zrporz.github.io/Simple-WAM-Web/

▲ 106 • 💬 2 • ⭐ 59 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2609.34981) • [💻 code](https://github.com/LeapLabTHU/Simple-WAM) • [🔗 project](https://zrporz.github.io/Simple-WAM-Web/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 75 • 💬 1 • ⭐ 86,094 • 37mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://huggingface.co/papers/2504.19413)**

*Prateek Chhikara, Dev Khant, Saket Aryan et al. (5 authors)*

Mem0, a memory-centric architecture with graph-based memory, enhances long-term conversational coherence in LLMs by efficiently extracting, consolidating, and retrieving information, outperforming existing memory systems in terms of accuracy and computational efficiency.

▲ 72 • 💬 2 • ⭐ 66,383 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.19413) • [💻 code](https://github.com/mem0ai/mem0) • [🔗 project](https://mem0.ai/research)

---

---

## GitHub Repositories: "ai"

**[zai-org/ZCode](https://github.com/zai-org/ZCode)**

Z.ai's coding agent harness. Powerful, intelligent, extensible.

`TypeScript`

⭐ 7.3k • 🔱 2.2k • 1d ago

---

**[Mak5er/AirCard](https://github.com/Mak5er/AirCard)**

Apple Wallet Card Skinner for iOS 18+ (No Jailbreak Required)

`Swift`

⭐ 5.3k • 🔱 269 • 12h ago

---

**[Albert-Weasker/niubigeo](https://github.com/Albert-Weasker/niubigeo)**

Open-source AI brand visibility and competitor reports. Official website: https://niubigeo.ai/ | Paid services: AI testing by real people and GEO optimization. Pricing: https://niubigeo.ai/pricing

`TypeScript`

⭐ 4.9k • 🔱 309 • 3d ago

---

**[KKKKhazix/AIHOT](https://github.com/KKKKhazix/AIHOT)**

一个自己找热点、自己写日报的网站框架。把信源和精选标准换成你的，它就是你的行业热点站。

`TypeScript` `ai` `content-curation` `llm` `mcp` `news-aggregator`

⭐ 4.2k • 🔱 1.2k • 1h ago

---

**[yi1108/printfilm](https://github.com/yi1108/printfilm)**

PRINTFILM：AI 视频获客与 AI短剧创作平台

`Python`

⭐ 3.9k • 🔱 445 • 6d ago

---

**[shadcn-ui/lint](https://github.com/shadcn-ui/lint)**

An agent-first linter for Tailwind design systems. Write design system rules that agents can verify.

`TypeScript` `agents` `ai` `design` `design-system` `design-tools`

⭐ 3.0k • 🔱 57 • 8d ago

---

**[jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader)**

One AI trade decision every Monad block. Jev on Kuru MON-USDC.

`TypeScript`

⭐ 2.7k • 🔱 511 • 14d ago

---

**[yibie/awesome-jev](https://github.com/yibie/awesome-jev)**

A curated list of public projects, integrations, and discussions built on Jev — TypeSafe AI's System One model for typed decisions.

`Python` `awesome` `awesome-list` `jev` `llm`

⭐ 2.0k • 🔱 303 • 11h ago

---

**[feder-cr/dots](https://github.com/feder-cr/dots)**

Open-source dots for the web: an AI agent with its own browser, one that does not get blocked.

`Python` `ai-agent` `ai-agents` `ai-browser` `anti-detect-browser` `browser-agent`

⭐ 2.0k • 🔱 321 • 1d ago

---

**[pallavi-shekhar/ai-engineering-interview-questions-company-wise](https://github.com/pallavi-shekhar/ai-engineering-interview-questions-company-wise)**

Your Cheat Sheet For AI Engineering Interviews at Top AI Companies - Questions and Answers.

`Markdown` `ai` `ai-engineering` `ai-engineering-interview` `ai-interview` `ai-interview-questions`

⭐ 1.6k • 🔱 161 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*
