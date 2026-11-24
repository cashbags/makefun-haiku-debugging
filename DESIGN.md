# Design — Seventeen Syllables of Debugging

## The entry

> A print left in prod
> shouts my debug thoughts at dawn
> customers read them

73 characters, 73 bytes, three lines, no trailing newline. `main.py`
writes this fixed string to `/output/entry.txt`, deterministically: no
clock, no environment, no randomness, no network.

## Why this haiku wins

The judge weighs five criteria in strict order, and the haiku is built
to clear each in turn:

1. **A haiku about debugging, 5-7-5.** Every line was counted by a
   script (a syllable counter with an explicit per-word table, not by
   ear — it caught one real miscount in a draft, a line that read 6
   syllables instead of 7). Counts are 5-7-5, seventeen syllables,
   plainly about debugging: a print statement, production, customers.
2. **Concrete and fresh central image.** A stray `print` left in
   production, shouting the author's private debug thoughts at dawn,
   read by customers. A specific object, a specific place, a specific
   audience — not a vague statement about code. Not one of the flooded
   lanes: no blinking cursor, no breath-holding breakpoint, no missing
   comma, no typo, no "bug was me".
3. **The turn lands in line 3.** Lines 1–2 set a private scene: a
   developer's leftover debug print, shouting into the dark. Line 3
   reframes it as public exposure — the thoughts were never private,
   the customers read them. The poem's subject changes from the
   developer's mistake to its audience.
4. **Every word earns its place.** 73 characters, no filler. "At dawn"
   does double work: the hour of the deploy and the hour the print
   fires, and it makes "shouts" audible. "Left" carries the whole
   accident — nobody meant to ship it. No word exists only to fill a
   syllable.
5. **Reads aloud cleanly.** Three short clauses in plain speech
   rhythm: a statement, a longer middle line that runs like a sentence,
   a short landing. Nothing sounds like a syllable exercise.

The tone is bleak-funny rather than a joke: the humour is in the
situation, not a punchline. The brief allows funny, quiet or bleak,
and this image earns bleak.

## Tournament

Ten candidates across eight fresh images (rubber duck, the log line
that lies, the test that passes alone and fails in CI, the comment
that says "never", the print left in prod, the 2 a.m. deploy, git
blame, the stack trace ending in your own code), each verified 5-7-5
by the counter script, then pairwise-judged against the five criteria
in strict order:

- **A — duck, "and the bug gives up":** out first. The turn is pat;
  the bug giving up resolves the poem instead of reframing it.
- **F — midnight deploy, "I broke it myself":** out. Too close to
  the flooded "the bug was me" lane; "the pager wakes me" is generic.
- **J — log, "the crowd disagrees":** out. Same lane as B (the lying
  log), weaker on image and turn; B wins the lane outright.
- **C — test green locally, red in CI:** out. Common-knowledge image;
  the turn is neat but less vivid than the finalists'.
- **G — git blame, "past me says sorry":** out. Charming, but the
  turn is a punchline rather than a reframe, and git-blame-as-confession
  is a well-worn trope.
- **I — duck, "the answer was mine":** beats A for the duck lane (a
  real reframe: the silence helps, the answer was yours), then loses
  to D, whose turn — the forbidden line running nightly under a
  comment that says "never" — is sharper irony.
- **D — comment "never":** beats I, then loses to E. E's image is
  more vivid and sensory where D is insider-clever.
- **B — log, "the truth logs nothing":** final three. Strong image
  and a paradoxical turn, but the paradox is abstract — it needs a
  beat to land, where E's turn lands on first read.
- **H — stack trace, "and stops at my name":** final three. The
  reveal is personal and surprising, but it is a reveal rather than a
  reframe.
- **E — print left in prod:** winner. The turn reframes the whole
  poem — private thoughts become public reading — in three plain
  words, with the freshest image of the final three.

## Syllable verification

Counts came from a Python script (`/tmp/haiku_count.py`, outside the
entry tree): an explicit syllable table for every word used, cross-checked
against a vowel-group heuristic, disagreements printed for hand
resolution. The heuristic overcounts silent-e words (gives, pipeline,
wakes, files); the table governs there. The script caught one genuine
error: candidate I's line 2 first read "it says nothing, which helps"
— six syllables, not seven. Fixed to "it says nothing, which still
helps" and re-verified. All ten final candidates measure 5-7-5; the
winner measures 5-7-5 (A/print/left/in/prod; shouts/my/de-bug/
thoughts/at/dawn; cus-tom-ers/read/them), re-verified after the last
edit. No word in the winner is ambiguous in count.

## Determinism

`main.py` holds the haiku as a constant and writes it byte-identically
on every run (verified: two runs to different directories, outputs
byte-identical, sha256 in BUILD-REPORT.md). The entry is 73 characters,
inside the 1–200 gate, UTF-8, not only whitespace.
