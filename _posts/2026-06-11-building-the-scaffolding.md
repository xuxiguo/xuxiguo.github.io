---
title: "Building the Scaffolding: What Actually Makes an AI Agent Smart"
date: 2026-06-11
categories: ["AI Agents", "Research Notes"]
description: "The model is not the moat. A tour of the scaffolding around an AI agent — MCP, Skills, sub-agents, and hooks — and how these four parts compose into a system that can do real research."
---

Give two researchers the same model — the very same Claude or GPT, the same weights, the same raw intelligence — and you can get wildly different results. One ends up with a chatbot that drafts emails. The other ends up with a system that reaches into a financial database, cleans the data, runs the regression, formats the table to journal style, and drafts the paragraph describing the result. Same engine. Completely different machine.

The difference is not the model. It is everything built around the model. People who build these systems have a couple of words for it — the *scaffolding* the model works from, and the *harness* that runs it<sup>[[8]](#ref8)</sup> — and I have become convinced this layer is where the real skill of working with AI now lives.

There is a line I keep coming back to: everyone can drive a Ferrari, but not everyone can race in Formula 1. The car matters, of course. But at the top, everyone has a comparable car. What separates the winners is the team around it — the pit crew, the telemetry, the race strategy, the thousand small decisions that turn raw horsepower into a result. AI is arriving at the same place. The frontier models are extraordinary and increasingly similar to one another. The edge is moving to the scaffolding.

This is a companion to an earlier post, where I told the story of how a chatbot grew hands and became an agent. Here I want to open the agent up and look at the parts inside.

---

## The Engine Is Not the Car

A frontier model is a magnificent engine. But an engine bolted to a stand, revving in a workshop, does not take you anywhere. To go somewhere you need a chassis and wheels, a steering column, a fuel line, brakes. The scaffolding is all of that: the structure that turns raw capability into something that can do a real job — safely, and the same way every time.

<figure>
  <img src="/assets/img/blog/scaffold-fig1-stack.png"
       alt="A three-tier pyramid. Bottom (widest), labeled Table Stakes: Tools — everyone has ChatGPT, Claude, Gemini. Middle, labeled The Differentiator: Scaffolding — Skills, Subagents, MCP, Hooks. Top (narrowest), labeled Your Human Edge: Judgment — the right questions plus human oversight. Caption quote: Everyone can drive a Ferrari. Not everyone can race F1."
       class="img-fluid" style="max-width:100%; border-radius:4px;">
  <figcaption class="figure-caption text-center mt-2">
    <strong>Figure 1.</strong> The tools are table stakes — everyone has access to similar models. The scaffolding is the differentiator. And your own judgment sits on top, where the real edge lives.
  </figcaption>
</figure>

In agent terms, the scaffolding comes down to four needs. The agent needs **reach** — a way to touch the tools and data that live outside it. It needs **consistency** — a memory of how you like things done, so it does not improvise differently every time. It needs **scale** — a way to divide a big job so it does not collapse under its own weight. And it needs **safety** — automatic rules for the things you cannot afford to have go wrong. Four components map onto those four needs, and the rest of this post is a tour of them: MCP, Skills, sub-agents, and hooks.

It is worth pausing on why this is the part that matters. The models themselves are becoming something close to a commodity — powerful, broadly available, and similar across providers. When Goldman Sachs's CEO said AI can now draft "95% of an IPO prospectus" in minutes, the striking part was not the 95%; it was that the remaining 5% — the judgment, the compliance, the responsibility — is where all the value concentrates.<sup>[[1]](#ref1)</sup> And when Anthropic reported that its model uncovered more than 500 high-severity software vulnerabilities that human experts had missed for years, that capability lived in the same kind of model anyone can rent.<sup>[[2]](#ref2)</sup> The moat is not the engine. It is the validated, well-designed scaffold built around it for a specific job.

So let me walk through the four parts.

---

## Reach: MCP, a USB-C Port for AI

A model on its own is sealed off from your data. It cannot see your database, your files, or your reference library. The first job of the scaffolding is to give it reach.

The old way to do this was painful. Every tool needed its own custom integration, hand-built and brittle. If you had five models and five data sources, you faced something like twenty-five separate connectors to write and maintain. It did not scale.

In November 2024, Anthropic introduced the Model Context Protocol — MCP — to solve exactly this.<sup>[[3]](#ref3)</sup> The official description is the one I find clearest: MCP is "a USB-C port for AI applications."<sup>[[4]](#ref4)</sup> Before USB-C, every device needed its own special cable; after it, one standard port connects to almost anything. MCP does the same for AI. You build one connector — an "MCP server" — for a tool, and any MCP-aware agent can plug into it. Someone builds the server once; everyone benefits.

<figure>
  <img src="/assets/img/blog/scaffold-fig2-mcp-hub.png"
       alt="A hub-and-spoke diagram. At the center, an AI agent surrounded by a ring labeled MCP. Spokes connect out to six tools: WRDS database, SEC EDGAR filings, Zotero library, Stata engine, local files, and Google Scholar."
       class="img-fluid" style="max-width:100%; border-radius:4px;">
  <figcaption class="figure-caption text-center mt-2">
    <strong>Figure 2.</strong> MCP turns a tangle of one-off integrations into a single port. Build a connector once, and the agent can reach WRDS, EDGAR, Zotero, Stata, your files, and more.
  </figcaption>
</figure>

For my own research, this is the difference between an assistant that can only talk and one that can actually fetch. Through MCP servers, the same agent can pull a sample from WRDS, read filings from SEC EDGAR, look up references in Zotero, hand a regression to Stata, and read and write files on my machine — all through one common protocol. An MCP server can expose three kinds of things to the agent: *tools* it can call, *resources* it can read, and *prompts* it can reuse. The agent does not need to know how any of them are built. It just needs the port.

If you take one idea from this section, make it this: MCP is reach. It is how the brain gets its arms long enough to touch the rest of your world.

---

## Consistency: Skills, a Recipe Card the Agent Never Loses

Reach lets the agent act. But action without consistency is its own problem. Ask a capable model to do the same task twice and it may do it two different ways — winsorizing at different thresholds, formatting a table differently, labeling variables by its own logic rather than yours. For research, where reproducibility is the whole game, that drift is unacceptable.

This is what Skills are for. A Skill is, quite literally, a folder of instructions that teaches the agent how *you* want a task done. At its center is a single file — `SKILL.md` — written in plain language: a name, a short description, and the step-by-step method. Anthropic released Skills as an open standard in October 2025, and the format is deliberately simple enough that anyone can write one.<sup>[[5]](#ref5)</sup>

The clever part is how Skills manage the agent's attention, through something called *progressive disclosure*.

<figure>
  <img src="/assets/img/blog/scaffold-fig3-skills.png"
       alt="Three stacked layers showing progressive disclosure. Layer 1, always loaded: name plus description, about 30 tokens — Claude reads just this to know when the skill applies. Layer 2, loaded when relevant: the full SKILL.md instructions. Layer 3, opened only as needed: scripts, templates, and reference files, which can be megabytes."
       class="img-fluid" style="max-width:100%; border-radius:4px;">
  <figcaption class="figure-caption text-center mt-2">
    <strong>Figure 3.</strong> Progressive disclosure. The agent reads only a one-line description until a task matches; then it opens the full instructions; then the bundled files, only if a step needs them. A skill can be enormous yet cost almost nothing until it is used.
  </figcaption>
</figure>

Here is the idea. The agent does not load the whole skill all the time. It keeps only a one-line description in view — just enough to know *when* the skill applies. The moment a task matches, it opens the full `SKILL.md`. And only if a particular step calls for it does the agent reach for the bundled scripts, templates, or reference files, which can be huge. The result is that a skill can carry an enormous amount of expertise while costing almost nothing until the exact moment it is needed.

In practice, a Skill is how I stop repeating myself. Instead of telling the agent "winsorize at the 1st and 99th percentile and cluster standard errors by firm" on every single task, I write it down once. From then on, the instruction loads fresh every time, and the work comes back the way my lab actually does it. MCP gives the agent reach; Skills give it consistency.

---

## Scale: Sub-agents, a Company Instead of a Genius

There is a hard limit hiding inside every model: the context window. Everything the agent is currently working with — your messages, the files it has opened, the code it has run, the outputs it has seen — has to fit inside a single window of attention, on the order of a couple hundred pages' worth of text. When the window fills, the oldest material falls out the back.<sup>[[6]](#ref6)</sup>

This produces a failure mode I have come to call the forgetting problem. An agent can be perfect through steps one, two, and three of a long task, and then, around step forty, quietly lose track of what the variables meant or what you originally asked. It is not a bug. It is a structural constraint, the agent's version of short-term memory running out.

One agent, in other words, cannot build a skyscraper. It cannot hold every role of a large project in one mind at once. But we have known how to solve this for a very long time — not in software, in human organizations. We specialize and delegate.

<figure>
  <img src="/assets/img/blog/scaffold-fig4-orchestration.png"
       alt="An orchestration diagram. At the top, a conductor labeled You plus Conductor with clean context that sees only summaries. Below, four specialist agents — Data, Analysis, Writing, Review — each with its own fresh context window. Arrows show the conductor delegating one job down to each and each returning a summary up."
       class="img-fluid" style="max-width:100%; border-radius:4px;">
  <figcaption class="figure-caption text-center mt-2">
    <strong>Figure 4.</strong> Instead of one overloaded agent, build a company. A conductor delegates a single job to each specialist; each works in its own fresh context window and returns a clean summary. The messy raw work never clogs the conductor's mind.
  </figcaption>
</figure>

So instead of one super-agent, you build a small company. A conductor agent takes the big goal and hands each piece to a specialist sub-agent: one to extract the data, one to run the analysis, one to draft the writing, one to review. Each specialist gets its own fresh context window, does one job, and returns a short, clean summary. The conductor only ever sees the summaries — never the thousands of lines of raw work — so its own context stays uncluttered no matter how large the overall project grows.

This is how I now run serious projects: as something closer to a research-paper factory than a single conversation. I talk to a handful of conductors; they manage a larger crew of specialists below them. The dead ends, the failed runs, the messy intermediate data — all of it stays sealed inside the specialist that produced it. Only the clean result flows up. MCP gives reach, Skills give consistency, and sub-agents give scale.

---

## Safety: Hooks, Smoke Detectors for Your Agent

There is one more problem, and it is the one that should make you cautious about handing an agent the keys.

Think of a ship navigating by dead reckoning. A compass that is off by half a degree feels fine for an hour and lands you on the wrong continent after three days. Language models work by approximation, and when you chain fifty steps together, small errors can compound. An agent can do something subtly wrong at step forty-seven — silently drop part of a sample, overwrite a file, run a command it should not — and you may not notice until much later. You cannot rely on the agent to remember every rule every time, any more than you would rely on yourself to.

So you do not rely on memory. You wire the rules into the harness itself, with hooks.

<figure>
  <img src="/assets/img/blog/scaffold-fig5-hooks.png"
       alt="A horizontal lifecycle track with four points: user prompt, before a tool runs, after a tool runs, and before it stops. At three of the points, a hook fires automatically — block a dangerous delete before a tool runs, auto-format the code after a tool runs, and run the tests before the agent stops."
       class="img-fluid" style="max-width:100%; border-radius:4px;">
  <figcaption class="figure-caption text-center mt-2">
    <strong>Figure 5.</strong> A hook is a rule that fires automatically at a fixed point in the agent's lifecycle — before a tool runs, after it runs, or before it finishes. You write the rule once; the harness enforces it every single time.
  </figcaption>
</figure>

A hook is a rule that fires automatically at a specific point in the agent's lifecycle.<sup>[[7]](#ref7)</sup> Before a tool runs, after it runs, before the agent is allowed to stop — at each of these moments you can attach a rule that runs without anyone asking for it. Block any command that looks like a dangerous delete. Automatically format every table the moment it is written. Refuse to let the agent declare victory until the tests pass. The crucial property is that hooks are deterministic: they are not polite suggestions the model might forget under load, they are guardrails the system enforces every time. Smoke detectors, not reminders.

This is also where the human belongs. The discipline I try to keep is a simple rhythm — human sets the direction, the AI executes, the human validates, the AI refines. Each human checkpoint is a place to catch the half-degree error before it becomes a wrong continent. Hooks automate the rules you can write down; your own review covers the judgment you cannot.

---

## How the Parts Compose

These four are not independent gadgets. They are layers that stack, each covering a different weakness of a raw model.

| Component | What it gives the agent | Everyday analogy | A research example |
|---|---|---|---|
| **MCP** | **Reach** — one open protocol to connect external tools and data | A USB-C port | Pull a sample from WRDS; read filings from EDGAR |
| **Skill** | **Consistency** — reusable instructions, loaded the same way every time | A recipe card | "Winsorize at the 1st and 99th percentile," every time |
| **Sub-agent** | **Scale** — a specialist with its own fresh context window | Hiring a teammate | A data-cleaning agent returns a tidy summary |
| **Hook** | **Safety** — a rule that fires automatically at a fixed point | A smoke detector | Auto-format every table; block a dangerous delete |

Put them together around a capable model and you have something genuinely useful: an agent that can reach your real tools, do the work your way, scale across a big project without losing the thread, and stay inside the rules that matter — while you supervise the handful of decisions that actually require a human. That last clause is not a footnote. The whole point of the scaffolding is to free your attention for the judgment only you can supply.

---

## The Edge Is the Design

Step back, and the picture is the pyramid from the start. At the base are the tools — table stakes, because everyone has access to similar models. In the middle is the scaffolding — the differentiator, because this is where design actually happens. And at the top is judgment — your edge, because deciding which problem is worth solving and whether an answer can be trusted is still irreducibly human.

I find this genuinely hopeful, especially for students and early-career researchers. The scaffolding is learnable. It is mostly open, mostly cheap, and mostly a matter of design rather than resources. You do not need to train a model or raise a billion dollars. You need to learn to think like the CEO of a small company of agents — to decide what to delegate, how to keep the work consistent, and where to stand guard. A first-year PhD student with well-designed scaffolding can now do what used to take a lab full of people.

And you do not have to build it all at once. Start small. Write one Skill for a task you repeat constantly. Connect one tool through MCP. Add one hook for a mistake you never want to see again. Each piece compounds. Before long you are not chatting with an AI; you are directing one.

Everyone can drive a Ferrari. The interesting question — the one worth getting good at — is how you build the team around it. The tools are extraordinary and getting better every month. What we build with them, and how carefully, is still the human part. That is exactly where I would want it to be.

---

## References

<ol>
  <li id="ref1">Business Insider. <a href="https://www.businessinsider.com/goldman-sachs-ceo-david-solomon-ai-ipo-investment-bank-analyst-2025-1" target="_blank">"Goldman Sachs CEO David Solomon on AI drafting 95% of an IPO prospectus." January 2025.</a></li>
  <li id="ref2">The Hacker News. <a href="https://thehackernews.com/2026/02/claude-opus-46-finds-500-high-severity.html" target="_blank">"Claude finds 500+ high-severity vulnerabilities across open-source projects." February 2026.</a> See also Anthropic, <a href="https://www.anthropic.com/news/claude-code-security" target="_blank">"Making frontier cybersecurity capabilities available."</a></li>
  <li id="ref3">Anthropic. <a href="https://www.anthropic.com/news/model-context-protocol" target="_blank">"Introducing the Model Context Protocol." November 2024.</a></li>
  <li id="ref4">Model Context Protocol. <a href="https://modelcontextprotocol.io/docs/getting-started/intro" target="_blank">"What is the Model Context Protocol (MCP)?"</a></li>
  <li id="ref5">Anthropic. <a href="https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills" target="_blank">"Equipping agents for the real world with Agent Skills." October 2025.</a></li>
  <li id="ref6">Anthropic. <a href="https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents" target="_blank">"Effective context engineering for AI agents." September 2025.</a></li>
  <li id="ref7">Claude Code Documentation. <a href="https://code.claude.com/docs/en/hooks" target="_blank">"Hooks reference."</a> See also Anthropic, <a href="https://www.anthropic.com/research/building-effective-agents" target="_blank">"Building Effective Agents." December 2024.</a></li>
  <li id="ref8">Hugging Face. <a href="https://huggingface.co/blog/agent-glossary" target="_blank">"Harness, Scaffold, and the AI Agent Terms Worth Getting Right." 2026.</a></li>
</ol>
