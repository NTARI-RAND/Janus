# Contributing

This repository carries the official JFA document, its translations, and the
conformance suite that binds the prose to the invariant registry. Two rules
govern every change: **sign your commits off**, and **keep the suite green**.

## Amendments go into the document

Propose a change by editing the document and opening a pull request. The diff
is the proposal, and the board approves or rejects it in review. Do not add
proposal files or version-documentation alongside the standard — git history is
the version record, and a parallel proposal document starts drifting from the
text it describes the moment it is merged.

Text that is settled goes into the document. Anything still unsettled goes into
[OPEN-QUESTIONS.md](OPEN-QUESTIONS.md) as a numbered entry carrying a
`**Status:**` line and an `**Inherits:**` line, in the style of the entries
already there. Update the count in that file's opening paragraph when you add
one. This split is not cosmetic: merging a document edit makes the text
normative, so a question that is still open cannot ride in on it.

## Sign-off (DCO)

Every commit needs a `Signed-off-by` trailer. The DCO check requires the name
and email in that trailer to match the commit author exactly, so let git add it
rather than typing it by hand:

```
git commit -s
```

If the check fails on an existing branch, add the trailer to every commit and
force-push:

```
git rebase HEAD~<n> --signoff
git push --force-with-lease
```

## The conformance suite

```
python jfa-conformance-suite.py                 # check the document
python jfa-conformance-suite.py --list          # print the invariant registry
python jfa-conformance-suite.py --explain REC_witness_minimum
python jfa-conformance-suite.py --bindings ../Cloudy   # report which delegated
                                                       # invariants a repo binds
```

Exit code 0 when every executed check passes, 1 otherwise. It runs on every
pull request as the **Conformance** check and takes well under a second.

Run the CLI regression tests locally with
`python -m unittest -v test_jfa_conformance_suite`.

To catch failures before you push, install the hook once in your clone:

```
git config core.hooksPath .githooks
```

That is a convenience, not a gate — hooks are not distributed with the
repository, and `git push --no-verify` skips them. The pull request check is
what actually holds.

### Compare two fixture runs for a delegated test

Choose one Go `TestInvariant_` function in an implementation checkout. Use a
valid fixture and a synthetic fixture that violates the cited invariant.
Generate both reports yourself in your own checkout. Reports attached to a pull
request do not establish what ran. Use [Go 1.20 or later](https://go.dev/doc/go1.20),
which emits the required package start event.

Run the same function in the same package and checkout for both fixtures,
preferably with an existing fixture selector. For example, if the test reads
the `FIXTURE` environment variable, run these commands from its package in a
POSIX shell (for example, Git Bash on Windows):

```sh
FIXTURE=/path/to/valid.fixture go test -json -count=1 -run '^TestInvariant_REC_public_chain_Example$' . > /tmp/jfa-valid.json
FIXTURE=/path/to/violating.fixture go test -json -count=1 -run '^TestInvariant_REC_public_chain_Example$' . > /tmp/jfa-violating.json
```

In PowerShell 7, set `$env:FIXTURE` before each `go test` invocation and
redirect its output to a writable path such as `$env:TEMP/jfa-valid.json` or
`$env:TEMP/jfa-violating.json`. Reports must be UTF-8, with or without a BOM.
Windows PowerShell 5.1 writes UTF-16 with `>`, so use PowerShell 7 or Git Bash.

The second Go command should fail on the invariant assertion. From the Janus
checkout, compare the recorded runs and check that failure for the intended
assertion:

```sh
python check-binding-fixtures.py --repo /path/to/implementation \
  --test TestInvariant_REC_public_chain_Example \
  --expect 'expected a single shared head' \
  /tmp/jfa-valid.json /tmp/jfa-violating.json
```

The command reports the citation separately from the two recorded outcomes.
It checks both report package names against the cited test file's directory
and the closest enclosing `go.mod` within the implementation checkout. If the
name is cited in multiple files, use `--path path/to/record_test.go` relative to
`--repo` to select the file that was built with your Go configuration.

Under each FAIL result, the command prints output attributed to the selected
test and its subtests. The optional `--expect` takes a Python regular expression
that must match that output when the violating run fails. Use an assertion
specific to the invariant. Without `--expect`, inspect the failure yourself
before treating a passing/failing pair as evidence.

It returns 0 for a passing valid fixture and a failing violating fixture,
1 for a completed pair with other outcomes, or 2 for inconclusive evidence
such as a skipped test, missing citation, unknown or mismatched package, or
incomplete report. A failure that does not match `--expect` is also inconclusive.
The result describes one test and two supplied runs.
Reviewers still interpret the failure and assess the implementation in its
own repository. Both this command and the document checker read files only.
The Go runs happen in the implementation checkout.

Run the fixture-report regression tests with
`python -m unittest -v test_binding_fixtures`. These tests require Go 1.20 or
later on PATH and generate reports from synthetic fixtures. The hosted
**Conformance** check runs the document suite. It skips this command and its
regression tests.

### What the suite constrains

Edits to the document fail the suite if they:

- drop, repeat or reorder the nine required level-two sections. Additional
  level-two sections are fine. Use `##` or underline the title with hyphens.
- add a `###` heading inside one of the five layer sections. Each must carry
  exactly Protocol Tier, Orchestrator Tier and Frontend Tier, in that order.
  Put new prose in the body of an existing tier. Headings inside fenced code
  examples do not count as sections or tiers.
- leave *The Lines That Cannot Be Crossed* with any count but twelve.
- remove or reword a registered anchor phrase. Twenty-five invariants are
  anchored to the sections that carry them; run `--list` to see them, and
  prefer appending to rewriting.
- name a product. The document is product-agnostic.
- introduce an email address other than the organizational footer's.

## Translations

The English document is authoritative; translations are for reach, not
interpretation. The suite checks the English document only. If you amend it,
say in the pull request whether the translations should be updated before the
change is adopted or after.
