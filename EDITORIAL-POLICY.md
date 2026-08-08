# Editorial policy

The PHP Analysis Tools Catalog is maintainer-curated, with community
contributions welcome. This policy describes what belongs in the catalog, how
claims are verified, and how recommendations are made.

## Scope

The catalog covers tools that inspect, transform, measure, or enforce qualities
of PHP source code, plus closely related building blocks and hosted services.
Every current entry must provide a concrete PHP use case.

Included artifact types are:

- standalone analyzers and linters;
- coding-standard rulesets and analyzer extensions;
- architecture, compatibility, security, dependency, and metrics tools;
- automated formatters, fixers, and refactoring tools;
- parsers and libraries used to build PHP analysis tooling;
- orchestration tools whose primary purpose is running PHP quality checks; and
- hosted products with documented PHP analysis support.

General CI setup actions, hook managers, unrelated CMS plugins, generic catalogs,
and repositories that merely mention PHP are excluded. Testing and coverage
tools may appear as `adjacent` only when their catalog record clearly explains
the boundary.

## Inclusion evidence

A current entry needs:

1. an official public project or product page;
2. evidence of a real PHP-analysis capability;
3. enough documentation for a user to evaluate or install it;
4. a factual description, a specific benefit, a meaningful limitation, and at
   least one primary source; and
5. a recorded editorial review date.

Stars and downloads are supporting signals, never standalone requirements.
Young or specialized projects may be included when their distinct value and
maintenance evidence are clear. Experimental tools must be labelled as such.

## Taxonomy

The broad `category` is used for navigation. Independent fields describe the
kind of artifact (`artifact_type`), tasks (`use_cases`), supported ecosystems,
capabilities, license, pricing, installation, and supported PHP versions.
Extensions and rulesets are not presented as independent analyzer engines.

## Lifecycle and successors

Repository activity and product availability are separate signals. A quiet,
stable tool is not automatically retired after a fixed number of days.

`catalog_status: historical` is an explicit editorial decision based on
archival, discontinued product support, loss of the documented PHP capability,
or a verified successor. Historical entries remain in In Memoriam. Forks,
renames, acquisitions, and successor projects use `successor_of` and
`supersedes` relations where known.

## Editors' Choice

Editors' Choice is a small manually approved shortlist, not an automatic stars
ranking and not a fixed quota per category. A selection should:

- solve a common or especially important PHP use case;
- be relevant to supported PHP versions today;
- have usable documentation and a credible maintenance path;
- offer a distinct reason to choose it over nearby alternatives; and
- have a specific recommendation and rationale in the editorial copy file.

Membership changes require a reviewed pull request. The reviewer should record
why an entry was added, replaced, or removed.

## Sources and review dates

Prefer official repositories, documentation, release notes, package metadata,
and vendor announcements. Third-party catalogs are useful discovery sources but
should not be the sole evidence for a current product claim. Automated upstream
descriptions are stored separately from editorial conclusions when both exist.

Each entry's `reviewed_at` represents a human review of editorial claims.
Automated metadata timestamps represent fetch freshness and must not be used as
a substitute. Public cards should expose supporting evidence and review dates.

## Commercial products and conflicts

Open-source and hosted products may both be listed, but licensing, pricing, and
local/cloud delivery must be labelled accurately. Sponsorship, payment, vendor
affiliation, or contributor affiliation cannot buy inclusion or an Editors'
Choice position. Contributors must disclose relevant affiliations in proposals.

The maintainer makes final editorial decisions and documents material changes
through repository history. Corrections and appeals are welcome through the
public issue forms.
