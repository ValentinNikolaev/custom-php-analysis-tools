# Static analysis tools for PHP

This file is generated from `common/catalog/*.yaml` by `scripts/generate_editor_choice.py`.
Selection is deterministic and limited to alive projects only. Repositories require at least 500 GitHub stars, then eligible projects are ranked by category quota, stars, repository freshness, and archive signals.
A human or LLM writes the recommendations and reasons in `common/editor-choice-copy.yaml`, followed by an editorial pass. Generation fails when a selected tool lacks either field.
⭐ shows GitHub stars; 🥇, 🥈, and 🥉 mark the first three entries in each section.

## Bug finders

Tools that inspect PHP code without running it to identify type errors, defects, dependency problems, and potential vulnerabilities.

| Tool | Recommended for | Why it stands out |
|---|---|---|
| [PHP Stan](https://github.com/phpstan/phpstan)<br><sub>🥇 ⭐ 14,061</sub> | PHP applications that need configurable type-safety checks and framework extensions | Extensions add framework-specific types, while baselines and rule levels support gradual adoption. |
| [jscpd](https://github.com/kucherenko/jscpd)<br><sub>🥈 ⭐ 5,972</sub> | Polyglot repositories that need duplicate-code checks across PHP and other file formats | One CLI detects copy-paste across 223 formats and provides CI, token-efficient, and MCP reporting options. |
| [psalm](https://psalm.dev)<br><sub>🥉 ⭐ 5,875</sub> | Projects needing advanced type modelling, taint analysis, and security checks | Psalm combines an expressive type system with taint analysis for application and security defects. |
| [Phan](https://github.com/etsy/phan)<br><sub>⭐ 5,619</sub> | Teams that want AST-based PHP analysis designed to limit false positives | Phan uses php-ast and tries to prove incorrectness, an approach designed to reduce false positives. |
| [mago](http://mago.carthage.software/)<br><sub>⭐ 3,361</sub> | Teams that want a Rust-based PHP linter, formatter, and static analyzer | Mago combines customizable linting, static analysis, automatic fixes, formatting, and AST visualization. |
| [PHP Mess Detector](https://phpmd.org)<br><sub>⭐ 2,443</sub> | Finding complexity, naming, unused-code, and design problems with configurable rules | PHPMD turns PDepend metrics into configurable rules for complexity, naming, and maintainability problems. |
| [PHP Compatibility](http://techblog.wimgodden.be/tag/codesniffer/)<br><sub>⭐ 2,299</sub> | Libraries and applications that must support specific PHP version ranges | Dedicated PHP_CodeSniffer rules detect syntax and API usage that conflicts with a target PHP version. |
| [composer-dependency-analyser](https://github.com/shipmonk-rnd/composer-dependency-analyser)<br><sub>⭐ 623</sub> | Composer projects checking for unused, shadow, and misplaced dependencies | Separate checks identify unused, shadow, and misplaced Composer dependencies. |

## Coding standards

Linters and rule-enforcement tools for formatting, naming, documentation, and project-specific coding conventions.

| Tool | Recommended for | Why it stands out |
|---|---|---|
| [EasyCodingStandard](https://github.com/Symplify/EasyCodingStandard)<br><sub>🥇 ⭐ 1,619</sub> | Teams running PHP-CS-Fixer and PHP_CodeSniffer through one configuration | One PHP config runs both rule engines in parallel and supports prepared rule sets and gradual adoption. |
| [PHP Code Sniffer](https://github.com/PHPCSStandards/PHP_CodeSniffer)<br><sub>🥈 ⭐ 1,537</sub> | Projects enforcing published standards or detailed custom coding rules | An extensible sniff API supports established standards and project-specific rules. |

## Architecture rules

Ready-to-use tools that enforce dependency boundaries and architectural constraints in an application.

| Tool | Recommended for | Why it stands out |
|---|---|---|
| [Deptrac](https://github.com/sensiolabs-de/deptrac.git)<br><sub>🥇 ⭐ 2,983</sub> | Layered applications and modular monoliths that enforce dependency boundaries in CI | Dependency rules turn layer and module boundaries into repeatable CI checks. |
| [PHP Architecture Tester](https://phpat.dev)<br><sub>🥈 ⭐ 1,273</sub> | Teams that prefer to express architecture constraints as readable PHP tests | A fluent PHP API keeps architecture tests in the same language and workflow as application tests. |

## Libraries and building blocks

Parsers, reflection libraries, and control-flow components for developers building custom analysis rules or tools.

| Tool | Recommended for | Why it stands out |
|---|---|---|
| [PHP Parser](https://github.com/nikic/PHP-Parser)<br><sub>🥇 ⭐ 17,451</sub> | Developers building analyzers, refactoring tools, formatters, or source transformations | A stable AST, traversal API, and code builder support many PHP analyzers and transformation tools. |

## Fixers and refactoring

Tools that automatically correct coding-standard violations, upgrade PHP syntax, or refactor existing code.

| Tool | Recommended for | Why it stands out |
|---|---|---|
| [PHP CS Fixer](https://github.com/FriendsOfPHP/PHP-CS-Fixer)<br><sub>🥇 ⭐ 13,545</sub> | Projects that automatically apply PHP formatting and coding-standard fixes | A broad fixer catalog and custom rule sets cover published standards and project-specific formatting. |
| [Rector](https://github.com/rectorphp/rector)<br><sub>🥈 ⭐ 10,396</sub> | Teams automating PHP upgrades, framework migrations, or repeatable refactoring | AST-based rules turn upgrade and refactoring recipes into reviewable code changes across a project. |

## Metrics and architecture

Tools that measure complexity, coupling, dependencies, maintainability, churn, and other structural properties.

| Tool | Recommended for | Why it stands out |
|---|---|---|
| [PHPInsights](https://youtube.com/@nunomaduro?sub_confirmation=1)<br><sub>🥇 ⭐ 5,626</sub> | Teams that want a quick command-line overview of PHP code quality | A single console report summarizes several code-quality signals and can enforce thresholds in CI. |
| [PHP Metrics](https://github.com/Halleck45/PhpMetrics)<br><sub>🥈 ⭐ 2,605</sub> | Visual review of complexity, coupling, maintainability, and project structure | Browsable reports make complexity, coupling, and architecture metrics easier to inspect than raw output. |
| [PDepend](https://pdepend.org/)<br><sub>🥉 ⭐ 958</sub> | Detailed object-oriented design, dependency, complexity, and maintainability metrics | JDepend-inspired metrics quantify coupling, complexity, dependencies, and maintainability. |

## Specialized tools

Wrappers, baseliners, multi-language engines, and focused analysis tools that do not fit the primary categories.

| Tool | Recommended for | Why it stands out |
|---|---|---|
| [Semgrep](https://semgrep.dev)<br><sub>🥇 ⭐ 16,123</sub> | Security teams writing custom checks for PHP and polyglot repositories | Source-like rules make custom bug and security checks quicker to write than compiler-style analyzers. |
| [Larastan](https://github.com/larastan/larastan)<br><sub>🥈 ⭐ 6,479</sub> | Laravel applications that need PHPStan to understand framework conventions | Laravel-specific type information covers containers, facades, Eloquent, and other framework conventions. |
