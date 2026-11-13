# Inform 7: compact working reference

Target: **Inform 10.1.2**, Glulx; researched 2026-11-12 against the installed
official manuals/Standard Rules and the official website. This is an agent's
working memory, not a replacement manual. **WI** = *Writing with Inform*;
**RB** = *Inform Recipe Book*. [Source map and local paths](sources.md).

Read this file first. For a coverage review use [scope](scope.md); for a bug use
[troubleshooting](troubleshooting.md). Open only the needed deeper reference.

## Model and syntax

- Inform is a typed, rule-based language with English-like syntax, not arbitrary
  English. Top-level assertions establish the initial model; imperative phrases
  run inside rules/phrases. `The hatch is open.` initializes; `now the hatch is
  open;` changes state; `if the hatch is open:` tests it. `let` introduces a local;
  `... is a number that varies` declares mutable global state. [WI 8](https://ganelson.github.io/inform-website/book/WI_8_1.html)
- A **kind** groups objects/values and supplies properties/defaults. A named object
  is an instance. `usually` supplies an overridable default; do not confuse it
  with `always`/`never` constraints. Prefer a kind plus shared rules over many
  nearly identical object rules. [WI 4](https://ganelson.github.io/inform-website/book/WI_4_1.html)
- Containers hold things **in** them; supporters hold things **on** them; parts
  are attached; people carry/wear things. `holder` is immediate; `location` and
  `enclosed by` answer different, broader whereabouts questions. `now`/`move`
  changes the model directly; `try` attempts an action with its rules. An unplaced
  thing can exist off-stage. [WI 8.7–8.17](https://ganelson.github.io/inform-website/book/WI_8_7.html)
- Prefer explicit nouns when `it`, `here`, or abbreviated source names might bind
  unexpectedly. Use straight quotes, consistent block indentation, semicolons
  between phrases, and a final period. Tables require actual tab separators.

## Actions: the central design decision

A **command** is player input; grammar maps it to an **action**; rulebooks implement
that action. A new command can invoke an existing action. A new action needs no
grammar if used only through `try`. [WI 17.1](https://ganelson.github.io/inform-website/book/WI_17_1.html)

For an ordinary player action, the useful outline is:

`parser → Before → basic light/access/carrying checks → Instead → Check → Carry out → After → Report`

This omits internal stages and NPC request handling. Consult the actual
[processing diagram](https://ganelson.github.io/inform-website/book/WI_12_2.html)
and installed Standard Rules for exact sequencing.

| Stage | Use | Normal fall-through |
|---|---|---|
| Before | Preparation or redirection | Continues |
| Instead | Replace/refuse this particular attempt | Ends original action in failure |
| Check | Preconditions; `say "Reason." instead;` rejects | Continues if not stopped |
| Carry out | State changes constituting success | Continues |
| After | Specific successful aftermath or replacement narration | Ends successfully, skipping Report |
| Report | Normal success narration | Continues through applicable reports |

Use `continue the action;` in an After rule when ordinary reporting should follow.
An Instead rule can also continue explicitly. Adding a rule does not delete
existing ones. For general mechanics, separate Check/Carry out/Report; for one
exception, a narrow Instead or After is often appropriate.
[WI 12.9](https://ganelson.github.io/inform-website/book/WI_12_9.html),
[12.21](https://ganelson.github.io/inform-website/book/WI_12_21.html),
[7.5](https://ganelson.github.io/inform-website/book/WI_7_5.html).

### Small complete pattern

Original example; the toolchain and playback verification are recorded in
[sources](sources.md#verification). `tune` implicitly takes a reachable instrument;
trying again fails without changing state. NPC support is intentionally absent.

```inform7
"Tuning Bench"

The Workshop is a room.
An instrument is a kind of thing.
An instrument can be tuned or untuned.
An instrument is usually untuned.
The copper bell is an instrument in the Workshop.
The wooden peg is a thing in the Workshop.

Tuning is an action applying to one carried thing.
Understand "tune [something]" as tuning.

Check tuning:
	if the noun is not an instrument:
		say "Only instruments need tuning." instead;
	if the noun is tuned:
		say "It is already tuned." instead.

Carry out tuning:
	now the noun is tuned.

Report tuning:
	say "You tune [the noun]."

Test me with "tune bell / tune bell / tune peg / inventory".
```

Carrying requirements run before Check: even the rejected peg is implicitly
taken. Use a touchable action plus deliberate acquisition logic if that is unwanted.

`try` can fail: inspect the resulting state before continuing dependent work.
`try silently` suppresses Report, not all output from checks, After rules, or
Carry out rules. Nested actions do not independently advance a full game turn.
[WI 7.4](https://ganelson.github.io/inform-website/book/WI_7_4.html)

For NPCs, distinguish a player **request** (persuasion) from a scripted action.
Ordinary author-written action rules often apply only to the player; explicitly
use `someone`/`an actor` where appropriate, operate on `actor`, and consider
awareness and unsuccessful-attempt reporting.
[WI 12.3–12.14](https://ganelson.github.io/inform-website/book/WI_12_11.html)

## Parser, names, and scope

Source identifier, printed name, and parser vocabulary are separate. Changing
`printed name` does not add synonyms. `Understand "chime" as the copper bell.`
adds vocabulary; `privately-named` suppresses automatic vocabulary from the source
name. Proper/plural naming and articles are presentation choices, not identity.
[WI 17.8](https://ganelson.github.io/inform-website/book/WI_17_8.html)

`[something]` normally resolves an in-scope thing; `[any thing]` broadens noun
selection. Neither automatically changes reachability. `one thing` in an action
declaration defaults to touchable; `one carried thing` adds carrying requirements
and may cause implicit taking. `one visible thing` is **not a universal visibility
guard**, especially for programmatic `try`; grammar scope and `requiring light`
are separate. [WI 12.17](https://ganelson.github.io/inform-website/book/WI_12_17.html)

Use conditional/property-based Understand rules for changing names and
`Does the player mean` to prefer among plausible parses. It cannot make an
unrecognized word valid or an absent thing reachable. `[text]` supplies a topic,
not an object. [WI 17](https://ganelson.github.io/inform-website/book/WI_17_1.html)

## Abstraction and state

| Need | Tool and caution | Reference |
|---|---|---|
| Reusable computation | Typed `To ...`, `To decide whether ...`, `To decide what ...`; return with `decide on`. Keep predicates free of side effects. | [WI 11](https://ganelson.github.io/inform-website/book/WI_11_1.html) |
| Query a class of objects | Descriptions, adjectives, `Definition:`, `repeat with ... running through ...`; distinguish description from a text description property. | [WI 6](https://ganelson.github.io/inform-website/book/WI_6_1.html) |
| Links between entities | Relations; select one/many cardinality and symmetry deliberately. Relation verbs are not player commands. | [WI 13](https://ganelson.github.io/inform-website/book/WI_13_1.html) |
| Structured records | Tables; typed columns, selected rows, explicit blanks. Row selection is mutable context; preserve values before a nested lookup. | [WI 16](https://ganelson.github.io/inform-website/book/WI_16_1.html) |
| Ordered collection | Typed lists; entries are indexed from 1. Check emptiness/bounds before selecting. | [WI 21](https://ganelson.github.io/inform-website/book/WI_21_1.html) |
| Extensible policy | Named rules/rulebooks; specificity affects order. Success/failure stops traversal; “no outcome” continues. `rule failed` is not the negation of `rule succeeded`. | [WI 19.6](https://ganelson.github.io/inform-website/book/WI_19_6.html), [19.11](https://ganelson.github.io/inform-website/book/WI_19_11.html) |
| Presentation hook | Activities have Before/For/After rules; For supplies the implementation. Activities are not actions and do not imply turns. | [WI 18](https://ganelson.github.io/inform-website/book/WI_18_1.html) |
| Plot phase | Scenes have explicit start/end conditions; they can overlap, normally happen once, and need `recurring` to repeat. | [WI 10](https://ganelson.github.io/inform-website/book/WI_10_1.html) |

Text containing substitutions can remain deferred; use `the substituted form of`
to capture a snapshot. Self-referential deferred text can recurse forever. Keep
printing names/descriptions free of game-state changes: printing and comparison
can evaluate text in unexpected contexts.
[WI 20.7](https://ganelson.github.io/inform-website/book/WI_20_7.html)

Use a minimal story and a short command sequence to resolve uncertainty. Inspect
`ACTIONS`, `RULES`, `SHOWME`, and the IDE Index before adding compensating rules.
[Troubleshooting workflow](troubleshooting.md#diagnose-before-patching).
