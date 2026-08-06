# Static analysis tools for PHP

This file is generated from `common/catalog/*.yaml` by `scripts/generate_editor_choice.py`.
Selection is deterministic and limited to alive projects only, then ranked by category quota, stars, repository freshness, and archive signals.

## Bug finders

Tools that inspect PHP code without running it to identify type errors, defects, dependency problems, and potential vulnerabilities.

| Tool | Recommended for | Why it stands out |
|---|---|---|
| [PHP Stan](https://github.com/phpstan/phpstan)<br><sub>★ 14,061</sub> | PHP Static Analysis Tool - discover bugs in your code without running it! | High adoption and recent maintenance: ★ 14,061; updated Aug 6, 2026. |
| [jscpd](https://github.com/kucherenko/jscpd)<br><sub>★ 5,972</sub> | Copy/paste detector for programming source code, supports 223 formats. AI-ready with token-efficient… | High adoption and recent maintenance: ★ 5,972; updated Aug 6, 2026. |
| [psalm](https://psalm.dev)<br><sub>★ 5,875</sub> | A PHP static analysis tool for finding errors and security vulnerabilities in PHP applications | High adoption and recent maintenance: ★ 5,875; updated Jul 13, 2026. |
| [Phan](https://github.com/etsy/phan)<br><sub>★ 5,619</sub> | Phan is a static analyzer for PHP. Phan prefers to avoid false-positives and attempts to prove incorrectness… | High adoption and recent maintenance: ★ 5,619; updated Jul 20, 2026. |
| [mago](http://mago.carthage.software/)<br><sub>★ 3,361</sub> | Mago is a toolchain for PHP that aims to provide a set of tools to help developers write better code. | High adoption and recent maintenance: ★ 3,361; updated Aug 4, 2026. |
| [PHP Mess Detector](https://phpmd.org)<br><sub>★ 2,443</sub> | PHPMD is a spin-off project of PHP Depend and aims to be a PHP equivalent of the well known Java tool PMD… | High adoption and recent maintenance: ★ 2,443; updated Aug 2, 2026. |
| [PHP Compatibility](http://techblog.wimgodden.be/tag/codesniffer/)<br><sub>★ 2,299</sub> | PHP Compatibility check for PHP_CodeSniffer | High adoption and recent maintenance: ★ 2,299; updated Aug 5, 2026. |
| [composer-dependency-analyser](https://github.com/shipmonk-rnd/composer-dependency-analyser)<br><sub>★ 623</sub> | 🚀 Fast detection of composer dependency issues (unused dependencies, shadow dependencies, misplaced… | Active community and recent maintenance: ★ 623; updated Aug 4, 2026. |
| [Skylos](https://skylos.dev/)<br><sub>★ 482</sub> | Local pull-request scanning for dead code and security issues | Active community and recent maintenance: ★ 482; updated Aug 5, 2026. |

## Coding standards

Linters and rule-enforcement tools for formatting, naming, documentation, and project-specific coding conventions.

| Tool | Recommended for | Why it stands out |
|---|---|---|
| [EasyCodingStandard](https://github.com/Symplify/EasyCodingStandard)<br><sub>★ 1,619</sub> | ECS runs PHP-CS-Fixer and PHP_CodeSniffer as a single, parallel fast tool with zero dependencies. Run on PHP… | High adoption and recent maintenance: ★ 1,619; updated Jul 22, 2026. |
| [PHP Code Sniffer](https://github.com/PHPCSStandards/PHP_CodeSniffer)<br><sub>★ 1,537</sub> | PHP_CodeSniffer tokenizes PHP files and detects violations of a defined set of coding standards. | High adoption and recent maintenance: ★ 1,537; updated Aug 6, 2026. |

## Architecture rules

Ready-to-use tools that enforce dependency boundaries and architectural constraints in an application.

| Tool | Recommended for | Why it stands out |
|---|---|---|
| [Deptrac](https://github.com/sensiolabs-de/deptrac.git)<br><sub>★ 2,983</sub> | Keep your architecture clean. | High adoption and recent maintenance: ★ 2,983; updated Jul 23, 2026. |
| [PHP Architecture Tester](https://phpat.dev)<br><sub>★ 1,273</sub> | ✔️ PHP Architecture Tester - Easy architecture testing for PHP | High adoption and recent maintenance: ★ 1,273; updated Jul 30, 2026. |

## Libraries and building blocks

Parsers, reflection libraries, and control-flow components for developers building custom analysis rules or tools.

| Tool | Recommended for | Why it stands out |
|---|---|---|
| [PHP Parser](https://github.com/nikic/PHP-Parser)<br><sub>★ 17,451</sub> | A PHP parser written in PHP | High adoption and recent maintenance: ★ 17,451; updated Jul 11, 2026. |

## Fixers and refactoring

Tools that automatically correct coding-standard violations, upgrade PHP syntax, or refactor existing code.

| Tool | Recommended for | Why it stands out |
|---|---|---|
| [PHP CS Fixer](https://github.com/FriendsOfPHP/PHP-CS-Fixer)<br><sub>★ 13,545</sub> | A tool to automatically fix PHP Coding Standards issues | High adoption and recent maintenance: ★ 13,545; updated Jul 31, 2026. |
| [Rector](https://github.com/rectorphp/rector)<br><sub>★ 10,396</sub> | Instant Upgrades and Automated Refactoring of any PHP 5.3+ code | High adoption and recent maintenance: ★ 10,396; updated Aug 5, 2026. |

## Metrics and architecture

Tools that measure complexity, coupling, dependencies, maintainability, churn, and other structural properties.

| Tool | Recommended for | Why it stands out |
|---|---|---|
| [PHPInsights](https://youtube.com/@nunomaduro?sub_confirmation=1)<br><sub>★ 5,626</sub> | 🔰 Instant PHP quality checks from your console | High adoption and recent maintenance: ★ 5,626; updated Aug 4, 2026. |
| [PHP Metrics](https://github.com/Halleck45/PhpMetrics)<br><sub>★ 2,605</sub> | Beautiful and understandable static analysis tool for PHP | High adoption and recent maintenance: ★ 2,605; updated Aug 2, 2026. |
| [PDepend](https://pdepend.org/)<br><sub>★ 958</sub> | Measuring PHP design quality and dependency structure | Active community and recent maintenance: ★ 958; updated Aug 2, 2026. |
| [PhpCodeArcheology](https://phpcodearcheology.github.io)<br><sub>★ 87</sub> | PHP static analysis for architecture & maintainability — 60+ metrics, complexity analysis, dependency… | Recently maintained; updated Aug 1, 2026. |

## Specialized tools

Wrappers, baseliners, multi-language engines, and focused analysis tools that do not fit the primary categories.

| Tool | Recommended for | Why it stands out |
|---|---|---|
| [Semgrep](https://semgrep.dev)<br><sub>★ 16,123</sub> | Lightweight static analysis for many languages. Find bug variants with patterns that look like source code. | High adoption and recent maintenance: ★ 16,123; updated Aug 6, 2026. |
| [Larastan](https://github.com/larastan/larastan)<br><sub>★ 6,479</sub> | ⚗️ Adds code analysis to Laravel improving developer productivity and code quality. | High adoption and recent maintenance: ★ 6,479; updated Jul 30, 2026. |
