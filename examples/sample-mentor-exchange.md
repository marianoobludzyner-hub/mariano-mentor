# Worked example: Mariano Mentor, grounded in the sample context

With [`sample-context/`](sample-context/) loaded as a Claude Project's knowledge, here is how the mentor grounds its answer in the specific numbers and situation rather than generic advice.

**Founder asks:** "Should I hire a second CSM to help catch renewal risk earlier?"

**Mariano Mentor:**

Not yet, and here's why the numbers say so before the org chart does.

The question: if you already suspect "at risk" has no real definition at Northwind, what's kept you from writing that definition down before now?

Where this sits: P1, reactive mindset and missing mandate, underneath P2 (renewals that surprise). It maps to SHIFT letter S, Signal, not letter T, headcount. Your `numbers.md` shows churn around 15% against an implied 93% NRR, but every figure is a founder estimate, not a tracked number. You don't have a visibility problem you can fix by adding a person, you have a measurement problem, and a second CSM inherits the exact same blind spot the first one has: nobody has defined what an early warning signal actually looks like at Northwind.

A second hire before that definition exists means two people reacting instead of one. Systems before people: the constraint isn't headcount, it's that "at risk" has no operational definition yet.

The move: before you write the job post, have your current CSM pull the last 4 renewals (including the one that was missed) and write down, account by account, what was true 60 days before each one that nobody flagged. That list is the start of your actual health signal, not a hire. Once that pattern exists on paper, whether you need a second CSM becomes a much easier question, and probably a cheaper one to answer.

---

Reproduce this: load the 5 files in [`sample-context/`](sample-context/) into a Claude Project alongside the [Mariano Mentor](../mentor/SKILL.md) skill, and ask the same question.
