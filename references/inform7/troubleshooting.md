# Inform 7: symptom → investigation → fix

Target Inform 10.1.2; [core](README.md), [source locations](sources.md).
These are diagnostic branches, not blanket replacements for built-in rules.

## Diagnose before patching

1. Reduce to one room, relevant objects/rules, and the shortest failing commands.
   Identify whether the failure is compilation, parsing, action handling, state,
   output, or interpreter capability.
2. In a testing build: `ACTIONS` reveals the action and success/failure; `RULES`
   traces applicable rules (`RULES ALL` is much noisier); `SHOWME object` reveals
   properties/whereabouts; `SCENES` and `RELATIONS` inspect those systems.
   These debug commands are not promised in a release build.
3. Consult the IDE Actions/Rules/Kinds/World/Scenes Index, then the named rule in
   installed Standard Rules or the responsible extension. The repository's
   capture runner uses `-no-index`; use an IDE scratch project when an Index is
   needed. Compiler logs and `auto.inf` remain in `prototype/build/EXAMPLE_ID/`.
4. Verify success **and** refusal, repeated use, synonyms, state afterward, and
   relevant barriers/NPCs. For parser work also test ambiguity and pronouns.
   Capture actual play; do not infer a transcript from compilation alone.

Official debugging: [WI 24.1](https://ganelson.github.io/inform-website/book/WI_24_1.html),
[24.3](https://ganelson.github.io/inform-website/book/WI_24_3.html).

## Common failure modes

| Symptom | Likely cause and useful fix | Read |
|---|---|---|
| English-looking sentence rejected | Wrong grammatical form/type, ambiguous name, or imperative at top level. Put executable phrases inside a rule; declare kinds/properties explicitly; shorten internal names. Inspect the first compiler problem before later ones. | [WI 2](https://ganelson.github.io/inform-website/book/WI_2_1.html), [11](https://ganelson.github.io/inform-website/book/WI_11_1.html) |
| Object vanishes / won't take / won't show in LOOK | Check holder, off-stage status, closed opaque containers, darkness, scenery/fixed status, and undescribed status. Scenery is normally fixed and omitted from room lists, not nonexistent. Undescribed does not mean invisible. | [WI 3](https://ganelson.github.io/inform-website/book/WI_3_1.html) |
| Displayed name cannot be typed | Printed name and vocabulary are separate. Add Understand synonyms; examine automatic source-name vocabulary and `privately-named`. | [WI 17.8](https://ganelson.github.io/inform-website/book/WI_17_8.html) |
| Wrong object/action chosen | Inspect ACTIONS and grammar before changing action rules. Give distinct vocabulary; use `Does the player mean` for preference. Do not use preference rules to compensate for missing grammar. | [WI 17.19](https://ganelson.github.io/inform-website/book/WI_17_19.html) |
| New verb still invokes old grammar | Adding an Understand line does not necessarily remove old meanings. If replacement is intended, use `Understand the command "..." as something new.` then define the grammar. Check aliases and special parser commands separately. | [WI 17.3](https://ganelson.github.io/inform-website/book/WI_17_3.html) |
| Remote noun recognized but action fails | Scope and touchability differ. `[any thing]` expands grammar reach, not physical access. Choose visible/touchable requirements deliberately; change reaching rules only for the intended mechanism. | [WI 12.17–12.19](https://ganelson.github.io/inform-website/book/WI_12_17.html) |
| Instead “works” but success history/After never fires | It normally ends the original action in failure and preempts action-specific Check/Carry out. Move normal mechanics into those stages or redirect explicitly. Earlier basic access rules still exist. | [WI 12.21](https://ganelson.github.io/inform-website/book/WI_12_21.html); [forum correction](https://intfiction.org/t/the-perils-of-instead/51796/2) |
| State changes but normal success message disappears | An After rule normally ends processing successfully. Add `continue the action;` when Report should follow; otherwise use After intentionally for replacement narration. | [WI 7.5](https://ganelson.github.io/inform-website/book/WI_7_5.html) |
| Duplicate reports / unexpected rule wins | Rules accumulate; specificity and explicit ordering matter, not just file position. Inspect Index/trace; name and narrowly replace/reorder the actual rule, or use an appropriate After rule. | [WI 19.4–19.6](https://ganelson.github.io/inform-website/book/WI_19_6.html) |
| `try silently` still prints | Only routine reporting is suppressed. Refusals and output in other stages can remain. Keep ordinary success prose in Report. | [WI 7.4](https://ganelson.github.io/inform-website/book/WI_7_4.html) |
| NPC does nothing / changes player's possessions | Player-only rule or hard-coded `player`; request refused by persuasion; failed NPC action has no suitable report. Use actor-aware rules and distinguish requests from scripted attempts. | [WI 12.11–12.14](https://ganelson.github.io/inform-website/book/WI_12_11.html) |
| Scene/timer repeats, fires late, or never starts | Scenes normally run once; conditions are checked at designated stages, not after every assignment. Separate one-time triggers from Every turn effects; inspect SCENES and end conditions. A failed in-world action can still consume a turn; parser rejection/out-of-world actions differ. | [WI 9](https://ganelson.github.io/inform-website/book/WI_9_1.html), [10](https://ganelson.github.io/inform-website/book/WI_10_1.html) |
| Text changes after “saving” it, or loops forever | Deferred substitutions retain live values; self-reference can recurse. Capture with `substituted form`; avoid state-changing say phrases and printing-name rules. | [WI 20.7](https://ganelson.github.io/inform-website/book/WI_20_7.html) |
| Table/list runtime error or wrong row | Missing lookup, blank entry, full table, out-of-range list index, or nested selection changed current row. Guard availability/bounds; preserve selected values before another lookup. PDF/HTML spacing is not source tabs. | [WI 16](https://ganelson.github.io/inform-website/book/WI_16_1.html), [21](https://ganelson.github.io/inform-website/book/WI_21_1.html) |
| Familiar action always refuses | Some standard actions deliberately have blocking checks until a game defines behavior. Find the exact named blocker, replace it narrowly, and supply the successful mechanics. Do not globally remove all Check rules. | [WI 12.9](https://ganelson.github.io/inform-website/book/WI_12_9.html), installed Standard Rules |
| Old example/extension won't compile | Identify its compiler era and dependencies before translating syntax. Low-level I6 inclusions, template replacements, response customization, and old `indexed text` code deserve particular scrutiny. Find a compatible release rather than silently mixing versions. | [Extensions and history](sources.md#guides-community-and-extensions) |
| UI differs from captured transcript | CheapGlk is a console interface, not the full graphical interpreter. Test status windows, sound, graphics, styles, and browser features in the intended interpreter. | [Project capture contract](../../prototype/README.md) |

## Project check commands

From the repository root, after changing a catalogued chapter example:

```powershell
uv run --project . python prototype/run.py --example SAMPLE-ID
uv run --project . python prototype/run.py
uv run --project . python prototype/run.py --check
```

Replace `SAMPLE-ID` with the real catalog ID. The first command captures one
example; the second refreshes generated outputs; the third checks them. The
capture protocol does not support replies to disambiguation prompts: use explicit
nouns for routine captures, and test clarification interactively when relevant.
