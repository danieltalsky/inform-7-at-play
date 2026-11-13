# Inform 7 language and capability map

Independent of any tutorial outline. Use this to recognize what Inform can
express and to assess the scope of an explanation. Target: 10.1.2; **WI** is the
official language manual, **RB** its companion implementation cookbook.
[Core](README.md) · [Local/online source map](sources.md).

## Coverage inventory

Each row is a family of capabilities, not a requirement that every discussion
teach every item. Chapter links also expose their section-level contents.

| Area | Concepts an agent should know exist | Official entry |
|---|---|---|
| Source language | Assertions versus instructions; sentence structure, punctuation, comments, headings, source naming and ambiguity; compiler problems and Index. | [WI 2](https://ganelson.github.io/inform-website/book/WI_2_1.html) |
| World model | Rooms, directions, map connections, doors, regions, things, people/animals, containers, supporters, parts, backdrops, devices, clothing; light, openness, locking, portability, scenery; player and containment tree. | [WI 3](https://ganelson.github.io/inform-website/book/WI_3_1.html) |
| Type and property system | Kinds/subkinds/instances; value kinds; either/or and value properties; defaults versus constraints; object-valued properties and `nothing`; typed variables. | [WI 4](https://ganelson.github.io/inform-website/book/WI_4_1.html), [22](https://ganelson.github.io/inform-website/book/WI_22_1.html) |
| Descriptions as queries | Adjectives, Definition rules, conditions, quantification, counting, descriptions of objects versus text descriptions; selecting and iterating matching values. | [WI 6](https://ganelson.github.io/inform-website/book/WI_6_1.html) |
| State and control flow | `now`, `let`, varying values, mutation/movement/removal, tests/branches, loops, temporary names, random selection, direct model changes versus actions. | [WI 8](https://ganelson.github.io/inform-website/book/WI_8_1.html), [11](https://ganelson.github.io/inform-website/book/WI_11_1.html) |
| Actions | Built-in actions, patterns, noun/second noun, redirection, Check/Carry out/Report and Before/Instead/After, success/history, implicit actions, action variables, stored actions, actor support, persuasion, accessibility/visibility, out-of-world actions. | [WI 7](https://ganelson.github.io/inform-website/book/WI_7_1.html), [12](https://ganelson.github.io/inform-website/book/WI_12_1.html) |
| Parsing | Command/action distinction, synonyms and replacement grammar, grammar tokens, topics, values, multiple objects, custom tokens, conditional/property/relation vocabulary, pronouns, disambiguation preferences, mistakes, precedence. | [WI 17](https://ganelson.github.io/inform-website/book/WI_17_1.html) |
| Time and narrative state | Startup, turns/time of day, scheduled events, past conditions, repeated actions; scenes, overlaps, recurrence, multiple endings, scene-dependent rules. | [WI 9](https://ganelson.github.io/inform-website/book/WI_9_1.html), [10](https://ganelson.github.io/inform-website/book/WI_10_1.html) |
| Phrases and higher abstraction | Parameterized instructions, predicates and value-returning phrases, type checking, phrase options, phrase values, generic kinds, applying functions to values/lists. | [WI 11](https://ganelson.github.io/inform-website/book/WI_11_1.html), [22](https://ganelson.github.io/inform-website/book/WI_22_1.html) |
| Relations | One/many cardinalities, symmetric/reciprocal and equivalence relations, condition-defined relations, verbs/prepositions, indirect relations and routes, relations involving values. | [WI 13](https://ganelson.github.io/inform-website/book/WI_13_1.html) |
| Rulebooks | Named rules, applicability/specificity/ordering, explicit listing/replacement, basis and variables, default outcomes, success/failure/no outcome, named outcomes/value-producing rulebooks, follow versus abide by. | [WI 19](https://ganelson.github.io/inform-website/book/WI_19_1.html) |
| Activities | Extensible Before/For/After hooks, contextual `while` conditions, activity variables; name/list/room-description printing, reading commands and parser messages. Distinct from actions. | [WI 18](https://ganelson.github.io/inform-website/book/WI_18_1.html) |
| Prose and responses | Descriptions/initial appearances, substitutions and alternatives, text lists, paragraph control, articles/plurals, adaptive tense/viewpoint/agreement, named library responses; deferred versus substituted text. | [WI 5](https://ganelson.github.io/inform-website/book/WI_5_1.html), [14](https://ganelson.github.io/inform-website/book/WI_14_1.html), [20](https://ganelson.github.io/inform-website/book/WI_20_1.html) |
| Data and mathematics | Numbers/real numbers, arithmetic, equations, units; tables with typed columns/blank rows/lookups/sorting/continuations/topics; typed lists, bounds, membership and transformations; text matching, regex and replacement. | [WI 15](https://ganelson.github.io/inform-website/book/WI_15_1.html), [16](https://ganelson.github.io/inform-website/book/WI_16_1.html), [20](https://ganelson.github.io/inform-website/book/WI_20_1.html), [21](https://ganelson.github.io/inform-website/book/WI_21_1.html) |
| Media and persistence | Figures, sounds, external files and table/text data; Glulx/Z-machine/interpreter differences; Glk capabilities and extensions for richer interfaces. | [WI 23](https://ganelson.github.io/inform-website/book/WI_23_1.html) |
| Testing and distribution | Test scripts, debug verbs, Index/Skein/transcripts, deterministic randomness, release builds, metadata, cover art, websites/interpreters, source release, bibliographic information. | [WI 24](https://ganelson.github.io/inform-website/book/WI_24_1.html), [25](https://ganelson.github.io/inform-website/book/WI_25_1.html), [26](https://ganelson.github.io/inform-website/book/WI_26_1.html) |
| Extensions and internals | Include/version/dependency/documentation conventions; Standard Rules and language extensions; low-level I6/Inter kits and compiler tooling. Advanced escape hatches require version-specific evidence. | [WI 27](https://ganelson.github.io/inform-website/book/WI_27_1.html), [kits](https://ganelson.github.io/inform/inbuild/M-agtk.html) |

## What is a library/design pattern rather than a language primitive?

Conversation systems, goals/planning, inventories with weight/volume, liquids,
ropes, money, combat, hint systems, navigation aids, and procedural prose often
combine primitives or extensions. Do not invent a built-in facility because its
English name sounds plausible. The [Recipe Book contents](https://ganelson.github.io/inform-website/book/RB_1_1.html)
route these implementation questions: place (3), time/plot (4), viewpoint (5),
commands (6), other characters/conversation (7), vehicles/furniture (8), props
(9), physics (10), out-of-world effects (11), presentation/media (12), testing
and publishing (13).

## Using this map for “what's missing?”

Establish the passage's promise and intended reader first. Compare it with the
relevant capability family and its dependencies. Report omissions as:

- **Needed for correctness:** missing distinction, prerequisite, failure case,
  or state change that makes the explanation misleading.
- **Useful next step:** a likely follow-up use case or generalization worth a
  small example.
- **Advanced pointer:** acknowledge the capability and link onward; do not turn
  a focused passage into a chapter on the whole language.

For example, reviewing actions suggests checking grammar versus action, stage
choice, successful state change versus narration, failure/repetition, and actor
assumptions. Stored actions and action variables may merit only a pointer. A
missing language feature is not automatically missing teaching material.
