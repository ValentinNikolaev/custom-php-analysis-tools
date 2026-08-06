![GitHub last commit](https://img.shields.io/github/last-commit/ValentinNikolaev/custom-php-analysis-tools)
![visitors](https://visitor-badge.laobi.icu/badge?page_id=ValentinNikolaev.custom-php-analysis-tools)

# Static analysis tools for PHP

A generated catalog of PHP static analysis, code quality, coding standards, metrics, refactoring, and SaaS tools.

Inspired by the pioneering [PHP Static Analysis Tools catalog by Exakat](https://github.com/exakat/php-static-analysis-tools) and its contributors.

The source of truth is `common/catalog/*.yaml`. Run `python scripts/full_workflow.py` to refresh metadata and regenerate this file.

To review and import newly listed active projects from Exakat, run `python scripts/full_workflow.py --import-exakat`.

## Table of Contents

* [Bugs finders](#bugs-finders)
* [Coding standards](#coding-standards)
* [DIY](#diy)
* [Fixers](#fixers)
* [Metrics](#metrics)
* [SaaS](#saas)
* [Misc](#misc)
* [In Memoriam](#in-memoriam)

### Editors' Choice

##### Bugs finders

| Tool | Description | Status | ⭐ Stars | Updated | Latest release | Links |
|---|---|---|---:|---|---|---|
| [PHP Stan](https://github.com/phpstan/phpstan) | PHP Static Analysis Tool - discover bugs in your code without running it! | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 14,061 | 2026-08-06 | [**2.2.8**](https://github.com/phpstan/phpstan/releases/tag/2.2.8) | [GitHub](https://github.com/phpstan/phpstan)<br>[Packagist](https://packagist.org/packages/phpstan/phpstan) |
| [jscpd](https://github.com/kucherenko/jscpd) | Copy/paste detector for programming source code, supports 223 formats. AI-ready with token-efficient reporter, skill and MCP server. | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 5,972 | 2026-08-06 | [**Release v5.0.14**](https://github.com/kucherenko/jscpd/releases/tag/v5.0.14) | [GitHub](https://github.com/kucherenko/jscpd) |
| [psalm](https://psalm.dev) | A PHP static analysis tool for finding errors and security vulnerabilities in PHP applications | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 5,875 | 2026-07-13 | 6.16.1 | [GitHub](https://github.com/vimeo/psalm)<br>[Packagist](https://packagist.org/packages/vimeo/psalm) |
| [Phan](https://github.com/etsy/phan) | Phan is a static analyzer for PHP. Phan prefers to avoid false-positives and attempts to prove incorrectness rather than correctness. | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 5,619 | 2026-07-20 | [**6.0.7**](https://github.com/phan/phan/releases/tag/6.0.7) | [GitHub](https://github.com/phan/phan)<br>[Packagist](https://packagist.org/packages/phan/phan) |
| [mago](http://mago.carthage.software/) | Mago is a toolchain for PHP that aims to provide a set of tools to help developers write better code. | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 3,361 | 2026-08-04 | 1.46.0 | [GitHub](https://github.com/carthage-software/mago)<br>[Packagist](https://packagist.org/packages/carthage-software/mago) |
| [PHP Mess Detector](https://phpmd.org) | PHPMD is a spin-off project of PHP Depend and aims to be a PHP equivalent of the well known Java tool PMD. PHPMD can be seen as an user friendly frontend application for the raw metrics stream measured by PHP Depend. | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 2,443 | 2026-08-02 | [**PHPMD 2.15.0**](https://github.com/phpmd/phpmd/releases/tag/2.15.0) | [GitHub](https://github.com/phpmd/phpmd)<br>[Packagist](https://packagist.org/packages/phpmd/phpmd) |
| [PHP Compatibility](http://techblog.wimgodden.be/tag/codesniffer/) | PHP Compatibility check for PHP_CodeSniffer | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 2,299 | 2026-08-05 | 9.3.5 | [GitHub](https://github.com/PHPCompatibility/PHPCompatibility)<br>[Packagist](https://packagist.org/packages/phpcompatibility/php-compatibility) |
| [composer-dependency-analyser](https://github.com/shipmonk-rnd/composer-dependency-analyser) | 🚀 Fast detection of composer dependency issues (unused dependencies, shadow dependencies, misplaced dependencies) | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 623 | 2026-08-04 | 1.8.4 | [GitHub](https://github.com/shipmonk-rnd/composer-dependency-analyser)<br>[Packagist](https://packagist.org/packages/shipmonk/composer-dependency-analyser) |
| [php-compat-info](https://llaville.github.io/php-compatinfo/7.2/) | Library that find out the minimum version and the extensions required for a piece of code to run | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 380 | 2026-05-20 | - | [GitHub](https://github.com/llaville/php-compatinfo) |

##### Coding standards

| Tool | Description | Status | ⭐ Stars | Updated | Latest release | Links |
|---|---|---|---:|---|---|---|
| [EasyCodingStandard](https://github.com/Symplify/EasyCodingStandard) | ECS runs PHP-CS-Fixer and PHP_CodeSniffer as a single, parallel fast tool with zero dependencies. Run on PHP 7.2+ | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 1,619 | 2026-07-22 | [**Released ECS 13.2.15**](https://github.com/ecsphp/ecs/releases/tag/13.2.15) | [GitHub](https://github.com/ecsphp/ecs) |
| [PHP Code Sniffer](https://github.com/PHPCSStandards/PHP_CodeSniffer) | PHP_CodeSniffer tokenizes PHP files and detects violations of a defined set of coding standards. | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 1,537 | 2026-08-06 | 4.0.4 | [GitHub](https://github.com/PHPCSStandards/PHP_CodeSniffer)<br>[Packagist](https://packagist.org/packages/phpcsstandards/php_codesniffer) |

##### DIY

| Tool | Description | Status | ⭐ Stars | Updated | Latest release | Links |
|---|---|---|---:|---|---|---|
| [PHP Parser](https://github.com/nikic/PHP-Parser) | A PHP parser written in PHP | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 17,451 | 2026-07-11 | v5.8.0 | [GitHub](https://github.com/nikic/PHP-Parser)<br>[Packagist](https://packagist.org/packages/nikic/php-parser) |

##### Fixers

| Tool | Description | Status | ⭐ Stars | Updated | Latest release | Links |
|---|---|---|---:|---|---|---|
| [PHP CS Fixer](https://github.com/FriendsOfPHP/PHP-CS-Fixer) | A tool to automatically fix PHP Coding Standards issues | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 13,545 | 2026-07-31 | v3.95.18 | [GitHub](https://github.com/PHP-CS-Fixer/PHP-CS-Fixer)<br>[Packagist](https://packagist.org/packages/friendsofphp/php-cs-fixer) |
| [Rector](https://github.com/rectorphp/rector) | Instant Upgrades and Automated Refactoring of any PHP 5.3+ code | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 10,396 | 2026-08-05 | 2.6.1 | [GitHub](https://github.com/rectorphp/rector)<br>[Packagist](https://packagist.org/packages/rector/rector) |

##### Metrics

| Tool | Description | Status | ⭐ Stars | Updated | Latest release | Links |
|---|---|---|---:|---|---|---|
| [PHPInsights](https://youtube.com/@nunomaduro?sub_confirmation=1) | 🔰 Instant PHP quality checks from your console | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 5,626 | 2026-08-04 | v2.14.2 | [GitHub](https://github.com/nunomaduro/phpinsights)<br>[Packagist](https://packagist.org/packages/nunomaduro/phpinsights) |
| [PHP Metrics](https://github.com/Halleck45/PhpMetrics) | Beautiful and understandable static analysis tool for PHP | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 2,605 | 2026-08-02 | 2.10.0 | [GitHub](https://github.com/phpmetrics/PhpMetrics)<br>[Packagist](https://packagist.org/packages/phpmetrics/phpmetrics) |
| [PhpCodeArcheology](https://phpcodearcheology.github.io) | PHP static analysis for architecture & maintainability — 60+ metrics, complexity analysis, dependency graphs, git churn hotspots, and AI-ready MCP server. Alternative to PHPMetrics. | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 87 | 2026-08-01 | - | [GitHub](https://github.com/PhpCodeArcheology/PhpCodeArcheology) |

##### Misc

| Tool | Description | Status | ⭐ Stars | Updated | Latest release | Links |
|---|---|---|---:|---|---|---|
| [Semgrep](https://semgrep.dev) | Lightweight static analysis for many languages. Find bug variants with patterns that look like source code. | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 16,123 | 2026-08-06 | - | [GitHub](https://github.com/semgrep/semgrep) |
| [Larastan](https://github.com/larastan/larastan) | ⚗️ Adds code analysis to Laravel improving developer productivity and code quality. | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 6,479 | 2026-07-30 | v3.10.0 | [GitHub](https://github.com/larastan/larastan)<br>[Packagist](https://packagist.org/packages/larastan/larastan) |

### Whole list

##### Bugs finders

| Tool | Description | Status | ⭐ Stars | Updated | Latest release | Links |
|---|---|---|---:|---|---|---|
| [PHP Stan](https://github.com/phpstan/phpstan) | PHP Static Analysis Tool - discover bugs in your code without running it! | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 14,061 | 2026-08-06 | [**2.2.8**](https://github.com/phpstan/phpstan/releases/tag/2.2.8) | [GitHub](https://github.com/phpstan/phpstan)<br>[Packagist](https://packagist.org/packages/phpstan/phpstan) |
| [jscpd](https://github.com/kucherenko/jscpd) | Copy/paste detector for programming source code, supports 223 formats. AI-ready with token-efficient reporter, skill and MCP server. | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 5,972 | 2026-08-06 | [**Release v5.0.14**](https://github.com/kucherenko/jscpd/releases/tag/v5.0.14) | [GitHub](https://github.com/kucherenko/jscpd) |
| [psalm](https://psalm.dev) | A PHP static analysis tool for finding errors and security vulnerabilities in PHP applications | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 5,875 | 2026-07-13 | 6.16.1 | [GitHub](https://github.com/vimeo/psalm)<br>[Packagist](https://packagist.org/packages/vimeo/psalm) |
| [Phan](https://github.com/etsy/phan) | Phan is a static analyzer for PHP. Phan prefers to avoid false-positives and attempts to prove incorrectness rather than correctness. | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 5,619 | 2026-07-20 | [**6.0.7**](https://github.com/phan/phan/releases/tag/6.0.7) | [GitHub](https://github.com/phan/phan)<br>[Packagist](https://packagist.org/packages/phan/phan) |
| [mago](http://mago.carthage.software/) | Mago is a toolchain for PHP that aims to provide a set of tools to help developers write better code. | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 3,361 | 2026-08-04 | 1.46.0 | [GitHub](https://github.com/carthage-software/mago)<br>[Packagist](https://packagist.org/packages/carthage-software/mago) |
| [PHP Mess Detector](https://phpmd.org) | PHPMD is a spin-off project of PHP Depend and aims to be a PHP equivalent of the well known Java tool PMD. PHPMD can be seen as an user friendly frontend application for the raw metrics stream measured by PHP Depend. | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 2,443 | 2026-08-02 | [**PHPMD 2.15.0**](https://github.com/phpmd/phpmd/releases/tag/2.15.0) | [GitHub](https://github.com/phpmd/phpmd)<br>[Packagist](https://packagist.org/packages/phpmd/phpmd) |
| [PHP Compatibility](http://techblog.wimgodden.be/tag/codesniffer/) | PHP Compatibility check for PHP_CodeSniffer | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 2,299 | 2026-08-05 | 9.3.5 | [GitHub](https://github.com/PHPCompatibility/PHPCompatibility)<br>[Packagist](https://packagist.org/packages/phpcompatibility/php-compatibility) |
| [composer-dependency-analyser](https://github.com/shipmonk-rnd/composer-dependency-analyser) | 🚀 Fast detection of composer dependency issues (unused dependencies, shadow dependencies, misplaced dependencies) | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 623 | 2026-08-04 | 1.8.4 | [GitHub](https://github.com/shipmonk-rnd/composer-dependency-analyser)<br>[Packagist](https://packagist.org/packages/shipmonk/composer-dependency-analyser) |
| [php-compat-info](https://llaville.github.io/php-compatinfo/7.2/) | Library that find out the minimum version and the extensions required for a piece of code to run | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 380 | 2026-05-20 | - | [GitHub](https://github.com/llaville/php-compatinfo) |
| [PHP-Parallel-Lint](https://github.com/php-parallel-lint/PHP-Parallel-Lint) | This tool check syntax of PHP files faster than serial check with fancier output. | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 356 | 2026-07-26 | v1.4.0 | [GitHub](https://github.com/php-parallel-lint/PHP-Parallel-Lint)<br>[Packagist](https://packagist.org/packages/php-parallel-lint/php-parallel-lint) |
| [phanalist](https://denzyldick.github.io/phanalist/) | Performant static analyzer for PHP, which is extremely easy to use. It helps you catch common mistakes in your PHP code. | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 161 | 2026-08-04 | v1.1.10 | [GitHub](https://github.com/denzyldick/phanalist)<br>[Packagist](https://packagist.org/packages/denzyl/phanalist) |
| [AST Metrics](http://ast-metrics.dev) | See the   invisible structure of your code. Multi-language code quality and architecture analyzer (Go,   PHP, Python, Rust...) | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 151 | 2026-07-29 | - | [GitHub](https://github.com/ast-metrics/ast-metrics) |
| [Coverage Guard](https://github.com/shipmonk-rnd/coverage-guard) | 🧪 Enforce PHP code coverage in your CI. Not by percentage, but target core methods! Allows you to start enforcing coverage for new code only!   Also contains tooling to merge and convert PHPUnit coverage files. | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 56 | 2026-07-17 | 1.1.0 | [GitHub](https://github.com/shipmonk-rnd/coverage-guard)<br>[Packagist](https://packagist.org/packages/shipmonk/coverage-guard) |
| [PHPDoctor](https://github.com/voku/PHPDoctor) | 🏥 PHPDoctor: Check files, full directories or strings for missing or bad PHPDoc types. | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 53 | 2026-07-10 | 0.8.0 | [GitHub](https://github.com/voku/PHPDoctor)<br>[Packagist](https://packagist.org/packages/voku/phpdoctor) |
| [name-collision-detector](https://github.com/shipmonk-rnd/name-collision-detector) | Fast & simple tool to find class duplicates in your projects. | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 35 | 2026-06-23 | 2.1.1 | [GitHub](https://github.com/shipmonk-rnd/name-collision-detector)<br>[Packagist](https://packagist.org/packages/shipmonk/name-collision-detector) |
| [PHP Analysis](https://github.com/cwi-swat/php-analysis) | PHP language analyses in Rascal | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 29 | 2026-05-13 | [**PHP 7.1 Support**](https://github.com/cwi-swat/php-analysis/releases/tag/v1.1.0) | [GitHub](https://github.com/cwi-swat/php-analysis) |
| [Composer-Unused](https://github.com/composer-unused/composer-unused) | Show unused composer dependencies by scanning your code | ![Dying](https://img.shields.io/badge/status-dying-yellow) | 1,684 | 2026-04-27 | 0.9.6 | [GitHub](https://github.com/composer-unused/composer-unused)<br>[Packagist](https://packagist.org/packages/icanhazstring/composer-unused) |
| [PHP Magic Number Detector](https://github.com/povils/phpmnd) | PHP Magic Number Detector | ![Dying](https://img.shields.io/badge/status-dying-yellow) | 585 | 2026-02-25 | [**PHPMND 3.6.1**](https://github.com/povils/phpmnd/releases/tag/v3.6.1) | [GitHub](https://github.com/povils/phpmnd)<br>[Packagist](https://packagist.org/packages/povils/phpmnd) |
| [PHP Static Type Checker](https://codeberg.org/Jumping-Beaver/PHP_Static_Type_Checker) | Static type checker for PHP relying on the php-ast PECL extension. Mirrored from Codeberg.org | ![Dying](https://img.shields.io/badge/status-dying-yellow) | - | 2026-04-08 | - | [GitHub](https://github.com/Jumping-Beaver/PHP_Static_Type_Checker)<br>Site unavailable |
| [noverify](https://github.com/VKCOM/noverify) | Pretty fast linter (code static analysis utility) for PHP | ![Almost dead](https://img.shields.io/badge/status-almost_dead-orange) | 688 | 2026-01-19 | v0.5.5 | [GitHub](https://github.com/VKCOM/noverify)<br>[Packagist](https://packagist.org/packages/vkcom/noverify) |
| [Progpilot](https://github.com/designsecurity/progpilot) | A static analysis tool for security | ![Almost dead](https://img.shields.io/badge/status-almost_dead-orange) | 365 | 2025-08-17 | v1.3.0 | [GitHub](https://github.com/designsecurity/progpilot)<br>[Packagist](https://packagist.org/packages/designsecurity/progpilot) |
| [Exakat](http://www.exakat.io/) | Smart static analysis | ![Unknown](https://img.shields.io/badge/status-unknown-lightgrey) | - | - | - | - |
| [PHP Inspection](https://plugins.jetbrains.com/plugin/7622?pr=idea) | Static analysis plugin for PHPStorm | ![Unknown](https://img.shields.io/badge/status-unknown-lightgrey) | - | - | - | - |
| [SonarQube](http://www.sonarqube.org/) | An open platform to manage code quality. It covers PHP code | ![Unknown](https://img.shields.io/badge/status-unknown-lightgrey) | - | - | - | - |

##### Coding standards

| Tool | Description | Status | ⭐ Stars | Updated | Latest release | Links |
|---|---|---|---:|---|---|---|
| [EasyCodingStandard](https://github.com/Symplify/EasyCodingStandard) | ECS runs PHP-CS-Fixer and PHP_CodeSniffer as a single, parallel fast tool with zero dependencies. Run on PHP 7.2+ | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 1,619 | 2026-07-22 | [**Released ECS 13.2.15**](https://github.com/ecsphp/ecs/releases/tag/13.2.15) | [GitHub](https://github.com/ecsphp/ecs) |
| [PHP Code Sniffer](https://github.com/PHPCSStandards/PHP_CodeSniffer) | PHP_CodeSniffer tokenizes PHP files and detects violations of a defined set of coding standards. | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 1,537 | 2026-08-06 | 4.0.4 | [GitHub](https://github.com/PHPCSStandards/PHP_CodeSniffer)<br>[Packagist](https://packagist.org/packages/phpcsstandards/php_codesniffer) |
| [composer-normalize](https://github.com/ergebnis/composer-normalize) | 🎵 Provides a composer plugin for normalizing composer.json. | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 1,115 | 2026-08-02 | 2.52.0 | [GitHub](https://github.com/ergebnis/composer-normalize)<br>[Packagist](https://packagist.org/packages/ergebnis/composer-normalize) |
| [PHPArkitect](https://github.com/phparkitect/arkitect) | Put your architectural rules under test! | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 923 | 2026-07-31 | 1.3.0 | [GitHub](https://github.com/phparkitect/arkitect)<br>[Packagist](https://packagist.org/packages/phparkitect/phparkitect) |
| [editorconfig-checker](https://editorconfig-checker.github.io/) | A tool to verify that your files are in harmony with your .editorconfig | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 75 | 2026-05-28 | 10.7.0 | [GitHub](https://github.com/editorconfig-checker/editorconfig-checker.php)<br>[Packagist](https://packagist.org/packages/editorconfig-checker/editorconfig-checker) |
| [TLint](https://github.com/tighten/tlint) | Tighten linter for Laravel conventions. | ![Dying](https://img.shields.io/badge/status-dying-yellow) | 526 | 2026-04-30 | v9.6.1 | [GitHub](https://github.com/tighten/tlint)<br>[Packagist](https://packagist.org/packages/tightenco/tlint) |
| [PHP Doc Check](https://github.com/NielsdeBlaauw/php-doc-check) | Uses complexity metrics to determine which functions need documentation. | ![Almost dead](https://img.shields.io/badge/status-almost_dead-orange) | 43 | 2025-12-16 | v0.4.1 | [GitHub](https://github.com/NielsdeBlaauw/php-doc-check)<br>[Packagist](https://packagist.org/packages/niels-de-blaauw/php-doc-check) |

##### DIY

| Tool | Description | Status | ⭐ Stars | Updated | Latest release | Links |
|---|---|---|---:|---|---|---|
| [PHP Parser](https://github.com/nikic/PHP-Parser) | A PHP parser written in PHP | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 17,451 | 2026-07-11 | v5.8.0 | [GitHub](https://github.com/nikic/PHP-Parser)<br>[Packagist](https://packagist.org/packages/nikic/php-parser) |
| [Deptrac](https://github.com/sensiolabs-de/deptrac.git) | Keep your architecture clean. | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 2,983 | 2026-07-23 | 4.7.1 | [GitHub](https://github.com/deptrac/deptrac)<br>[Packagist](https://packagist.org/packages/deptrac/deptrac) |
| [PHP Architecture Tester](https://phpat.dev) | ✔️ PHP Architecture Tester - Easy architecture testing for PHP | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 1,273 | 2026-07-30 | 0.12.4 | [GitHub](https://github.com/carlosas/phpat)<br>[Packagist](https://packagist.org/packages/carlosas/phpat) |
| [Better Reflection](https://github.com/Roave/BetterReflection) | :crystal_ball: Better Reflection is a reflection API that aims to improve and provide more features than PHP's built-in reflection API. | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 1,245 | 2026-08-02 | 6.72.0 | [GitHub](https://github.com/Roave/BetterReflection)<br>[Packagist](https://packagist.org/packages/roave/better-reflection) |
| [PHP-cfg](https://github.com/ircmaxell/php-cfg) | A Control Flow Graph implementation in PHP | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 246 | 2026-08-01 | V0.8.1 | [GitHub](https://github.com/ircmaxell/php-cfg)<br>[Packagist](https://packagist.org/packages/ircmaxell/php-cfg) |
| [Reflection](https://github.com/phpDocumentor/Reflection.git) | Reflection library to do Static Analysis for PHP Projects | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 125 | 2026-07-30 | 7.0.0 | [GitHub](https://github.com/phpDocumentor/Reflection)<br>[Packagist](https://packagist.org/packages/phpdocumentor/reflection) |

##### Fixers

| Tool | Description | Status | ⭐ Stars | Updated | Latest release | Links |
|---|---|---|---:|---|---|---|
| [PHP CS Fixer](https://github.com/FriendsOfPHP/PHP-CS-Fixer) | A tool to automatically fix PHP Coding Standards issues | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 13,545 | 2026-07-31 | v3.95.18 | [GitHub](https://github.com/PHP-CS-Fixer/PHP-CS-Fixer)<br>[Packagist](https://packagist.org/packages/friendsofphp/php-cs-fixer) |
| [Rector](https://github.com/rectorphp/rector) | Instant Upgrades and Automated Refactoring of any PHP 5.3+ code | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 10,396 | 2026-08-05 | 2.6.1 | [GitHub](https://github.com/rectorphp/rector)<br>[Packagist](https://packagist.org/packages/rector/rector) |
| [Phpactor](https://github.com/phpactor/phpactor) | Mainly a PHP Language Server with more features than you can shake a stick at | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 1,908 | 2026-08-01 | 2026.07.22.0 | [GitHub](https://github.com/phpactor/phpactor)<br>[Packagist](https://packagist.org/packages/phpactor/phpactor) |
| [php-scoper](https://github.com/humbug/php-scoper) | 🔨 Prefixes all PHP namespaces in a file/directory to isolate the code bundled in PHARs. | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 806 | 2026-07-06 | 0.18.19 | [GitHub](https://github.com/humbug/php-scoper)<br>[Packagist](https://packagist.org/packages/humbug/php-scoper) |
| [PHP Weaver](https://github.com/troelskn/phpweaver) | A combined runtime/static code-analysis tool, that can trace parameter types | ![Almost dead](https://img.shields.io/badge/status-almost_dead-orange) | 85 | 2026-01-28 | - | [GitHub](https://github.com/troelskn/phpweaver) |

##### Metrics

| Tool | Description | Status | ⭐ Stars | Updated | Latest release | Links |
|---|---|---|---:|---|---|---|
| [PHPInsights](https://youtube.com/@nunomaduro?sub_confirmation=1) | 🔰 Instant PHP quality checks from your console | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 5,626 | 2026-08-04 | v2.14.2 | [GitHub](https://github.com/nunomaduro/phpinsights)<br>[Packagist](https://packagist.org/packages/nunomaduro/phpinsights) |
| [PHP Metrics](https://github.com/Halleck45/PhpMetrics) | Beautiful and understandable static analysis tool for PHP | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 2,605 | 2026-08-02 | 2.10.0 | [GitHub](https://github.com/phpmetrics/PhpMetrics)<br>[Packagist](https://packagist.org/packages/phpmetrics/phpmetrics) |
| [PhpCodeArcheology](https://phpcodearcheology.github.io) | PHP static analysis for architecture & maintainability — 60+ metrics, complexity analysis, dependency graphs, git churn hotspots, and AI-ready MCP server. Alternative to PHPMetrics. | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 87 | 2026-08-01 | - | [GitHub](https://github.com/PhpCodeArcheology/PhpCodeArcheology) |
| [PHP Semantic Versioning Checker](https://github.com/tomzx/php-semver-checker) | Compares two source sets and determines the appropriate semantic versioning to apply. | ![Dying](https://img.shields.io/badge/status-dying-yellow) | 436 | 2026-02-05 | v0.17.0 | [GitHub](https://github.com/tomzx/php-semver-checker)<br>[Packagist](https://packagist.org/packages/tomzx/php-semver-checker) |
| [churn-php](https://github.com/bmitch/churn-php) | Discover files in need of refactoring. | ![Almost dead](https://img.shields.io/badge/status-almost_dead-orange) | 1,376 | 2025-12-31 | 1.7.3 | [GitHub](https://github.com/bmitch/churn-php)<br>[Packagist](https://packagist.org/packages/bmitch/churn-php) |
| [dePHPend](https://github.com/mihaeu/dephpend) | Detect flaws in your architecture, before they drag you down into the depths of dependency hell ... | ![Almost dead](https://img.shields.io/badge/status-almost_dead-orange) | 532 | 2026-01-28 | 0.9.0 | [GitHub](https://github.com/mihaeu/dephpend)<br>[Packagist](https://packagist.org/packages/dephpend/dephpend) |
| [php-class-dependencies-analyzer](https://php-quality-tools.com/class-dependencies-analyzer/) | This tool allows you to monitor the dependencies and instability of your classes | ![Almost dead](https://img.shields.io/badge/status-almost_dead-orange) | 21 | 2026-01-06 | - | [GitHub](https://github.com/DeGraciaMathieu/php-class-dependencies-analyzer) |

##### SaaS

| Tool | Description | Status | ⭐ Stars | Updated | Latest release | Links |
|---|---|---|---:|---|---|---|
| [Bliss](https://blissai.com/index.html) | Automatically reviews code in real-time and shows how much it's worth in lines of code | ![Unknown](https://img.shields.io/badge/status-unknown-lightgrey) | - | - | - | - |
| [Checkmarx](http://lp.checkmarx.com/php-code-analysis/) | Get a full PHP static security code analysis and prevent security vulnerabilities | ![Unknown](https://img.shields.io/badge/status-unknown-lightgrey) | - | - | - | Site unavailable |
| [Codacy](https://www.codacy.com/) | Codacy: Automated Code Review | ![Unknown](https://img.shields.io/badge/status-unknown-lightgrey) | - | - | - | - |
| [Code Climate](https://codeclimate.com) | Hosted static analysis for Ruby, PHP and JavaScript source code | ![Unknown](https://img.shields.io/badge/status-unknown-lightgrey) | - | - | - | - |
| [Insight](https://insight.sensiolabs.com/) | A SensioLabs tool to analyzes source code to find problems that degrade the overall quality of your projects | ![Unknown](https://img.shields.io/badge/status-unknown-lightgrey) | - | - | - | Site unavailable |
| [Laravelshift](https://laravelshift.com/) | the automated way to upgrade Laravel applications. Upgrade Laravel applications all the way from Laravel 4.2 to the latest version of Laravel | ![Unknown](https://img.shields.io/badge/status-unknown-lightgrey) | - | - | - | - |
| [RIPS](https://www.ripstech.com/) | The superior security software for PHP applications. Source code static analyser for vulnerabilities | ![Unknown](https://img.shields.io/badge/status-unknown-lightgrey) | - | - | - | - |
| [Scrutinizer](https://scrutinizer-ci.com/) | Improve code quality and find bugs before they hit production with our continuous inspection platform | ![Unknown](https://img.shields.io/badge/status-unknown-lightgrey) | - | - | - | - |
| [SideCI](https://sideci.com/) | CI for automated code review by code analysis | ![Unknown](https://img.shields.io/badge/status-unknown-lightgrey) | - | - | - | Site unavailable |

##### Misc

| Tool | Description | Status | ⭐ Stars | Updated | Latest release | Links |
|---|---|---|---:|---|---|---|
| [Semgrep](https://semgrep.dev) | Lightweight static analysis for many languages. Find bug variants with patterns that look like source code. | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 16,123 | 2026-08-06 | - | [GitHub](https://github.com/semgrep/semgrep) |
| [Larastan](https://github.com/larastan/larastan) | ⚗️ Adds code analysis to Laravel improving developer productivity and code quality. | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 6,479 | 2026-07-30 | v3.10.0 | [GitHub](https://github.com/larastan/larastan)<br>[Packagist](https://packagist.org/packages/larastan/larastan) |
| [Opengrep](https://github.com/opengrep/opengrep) | 🔎 Static code analysis engine to find security issues in code. | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 2,879 | 2026-08-05 | - | [GitHub](https://github.com/opengrep/opengrep) |
| [Composer Require Checker](https://github.com/maglnet/ComposerRequireChecker) | A CLI tool to check whether a specific composer package uses imported symbols that aren't part of its direct composer dependencies | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 1,006 | 2026-08-05 | 4.24.0 | [GitHub](https://github.com/maglnet/ComposerRequireChecker)<br>[Packagist](https://packagist.org/packages/maglnet/composer-require-checker) |
| [PHP Parser](https://php-parser.glayzzle.com/) | :herb: NodeJS PHP Parser - extract AST or tokens | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 563 | 2026-08-05 | - | [GitHub](https://github.com/glayzzle/php-parser) |
| [Static Analysis Results Baseliner](https://github.com/DaveLiddament/sarb) | Static Analysis Results Baseliner | ![Alive](https://img.shields.io/badge/status-alive-brightgreen) | 165 | 2026-07-12 | 1.11.0 | [GitHub](https://github.com/DaveLiddament/sarb)<br>[Packagist](https://packagist.org/packages/dave-liddament/sarb) |
| [devbug](http://www.devbug.co.uk/) | Ongoing work on PHP Analysis in Rascal (PHP AiR) | ![Unknown](https://img.shields.io/badge/status-unknown-lightgrey) | - | - | - | Site unavailable |
| [HHVM](http://hhvm.com/) | Hack Language from Facebook. Add a SCA until version 3.3.8, newer version doesn't have anymore | ![Unknown](https://img.shields.io/badge/status-unknown-lightgrey) | - | - | - | - |
| [PHPQA](https://edgedesigncz.github.io/phpqa/) | A Wrapper to a lot of PHP tools reported into a single HTML file | ![Unknown](https://img.shields.io/badge/status-unknown-lightgrey) | - | - | - | - |

<a id="in-memoriam"></a>

## 🕯️ In Memoriam — PHP Analysis Pioneers

These projects are no longer actively maintained, but their ideas, code, and communities made a lasting contribution to the PHP ecosystem. We preserve them here with gratitude and respect.

| Project | Contribution | Category | Last activity | Legacy links |
|---|---|---|---|---|
| [🕯️ PHPLOC](https://github.com/sebastianbergmann/phploc) | A tool for quickly measuring the size of a PHP project. | Metrics | 2025-04-12 | [Source](https://github.com/sebastianbergmann/phploc)<br>[Packagist](https://packagist.org/packages/phploc/phploc) |
| [🕯️ PHP Assumption](https://github.com/rskuipers/php-assumptions.git) | Tool to detect assumptions | Bugs finders | 2025-03-22 | [Source](https://github.com/rskuipers/php-assumptions)<br>[Packagist](https://packagist.org/packages/rskuipers/php-assumptions) |
| [🕯️ Coverage Checker](https://github.com/exussum12/coverageChecker) | Allows old code to use new standards | Misc | 2024-06-25 | [Source](https://github.com/exussum12/coverageChecker)<br>[Packagist](https://packagist.org/packages/exussum12/coverage-checker) |
| [🕯️ PHP Code Sniffer](https://github.com/squizlabs/PHP_CodeSniffer) | PHP_CodeSniffer tokenizes PHP files and detects violations of a defined set of coding standards. | Coding standards | 2024-04-01 | [Source](https://github.com/squizlabs/PHP_CodeSniffer) |
| [🕯️ PHPCodeFixer](https://github.com/wapmorgan/PhpCodeFixer) | Analyzer of PHP code to search issues with deprecated functionality in newer interpreter versions. | Bugs finders | 2024-02-14 | [Source](https://github.com/wapmorgan/PhpDeprecationDetector) |
| [🕯️ PhpDependencyAnalysis](https://github.com/mamuz/PhpDependencyAnalysis) | Static code analysis to find violations in a dependency graph | Metrics | 2023-12-03 | [Source](https://github.com/mamuz/PhpDependencyAnalysis) |
| [🕯️ PhpCodeAnalyzer](https://github.com/wapmorgan/PhpCodeAnalyzer.git) | Really, it's "php extensions usage analyzer". It scans codebase and analyzes which non-built-in php extensions used | Bugs finders | 2023-01-17 | [Source](https://github.com/wapmorgan/PhpCodeAnalyzer) |
| [🕯️ PHPCPD](https://github.com/sebastianbergmann/phpcpd) | Copy/Paste Detector (CPD) for PHP code. | Bugs finders | 2023-01-10 | [Source](https://github.com/sebastianbergmann/phpcpd)<br>[Packagist](https://packagist.org/packages/sebastian/phpcpd) |
| [🕯️ PHP-malware-finder](https://github.com/nbs-system/php-malware-finder) | Detect potentially malicious PHP files | Bugs finders | 2022-02-22 | [Source](https://github.com/nbs-system/php-malware-finder) |
| [🕯️ PHP testability](https://github.com/edsonmedina/php_testability) | Analyses and reports testability issues of a php codebase | Bugs finders | 2022-01-27 | [Source](https://github.com/edsonmedina/php_testability)<br>[Packagist](https://packagist.org/packages/edsonmedina/php_testability) |
| [🕯️ PHP formatter](https://github.com/mmoreram/php-formatter) | PHP Formatter is a PHP developer friendly set of tools | Coding standards | 2021-06-24 | [Source](https://github.com/mmoreram/php-formatter)<br>[Packagist](https://packagist.org/packages/mmoreram/php-formatter) |
| [🕯️ PHP-Parallel-Lint](https://github.com/JakubOnderka/PHP-Parallel-Lint) | This tool check syntax of PHP files faster than serial check with fancier output. | Bugs finders | 2021-03-13 | [Source](https://github.com/JakubOnderka/PHP-Parallel-Lint)<br>[Packagist](https://packagist.org/packages/jakub-onderka/php-parallel-lint) |
| [🕯️ phpdoc to typehint](https://github.com/dunglas/phpdoc-to-typehint) | Add scalar type hints and return types to existing PHP projects using PHPDoc annotations | Fixers | 2020-12-28 | [Source](https://github.com/dunglas/phpdoc-to-typehint)<br>[Packagist](https://packagist.org/packages/dunglas/phpdoc-to-typehint) |
| [🕯️ Pahout](https://github.com/wata727/pahout) | A pair programming partner for writing better PHP. Pahout means PHP mahout :elephant: | Coding standards | 2020-06-26 | [Source](https://github.com/wata727/pahout)<br>[Packagist](https://packagist.org/packages/wata727/pahout) |
| [🕯️ PHP BackSlasher](https://github.com/nilportugues/php-backslasher) | [Git hook] Tool to add all PHP internal functions and constants to its namespace by adding backslash to them. | Fixers | 2020-04-21 | [Source](https://github.com/nilportugues/php-backslasher)<br>[Packagist](https://packagist.org/packages/nilportugues/php_backslasher) |
| [🕯️ Quality Analyzer](https://github.com/Qafoo/QualityAnalyzer.git) | Tool helping us to analyze software projects | Metrics | 2019-12-06 | [Source](https://github.com/Qafoo/QualityAnalyzer)<br>[Packagist](https://packagist.org/packages/qafoo/quality-analyzer) |
| [🕯️ php7mar](https://github.com/Alexia/php7mar) | PHP 7 Migration Assistant Report (MAR) | Bugs finders | 2019-05-28 | [Source](https://github.com/Alexia/php7mar)<br>[Packagist](https://packagist.org/packages/alexia/php7mar) |
| [🕯️ Pfff](https://github.com/facebook/pfff) | Tools for code analysis, visualizations, or style-preserving source transformation. | Bugs finders | 2019-03-27 | [Source](https://github.com/facebookarchive/pfff) |
| [🕯️ Fixtro](https://github.com/karlosagudo/fixtro) | A QA static analysis code, with a different approach | Misc | 2019-03-02 | [Source](https://github.com/karlosagudo/fixtro)<br>[Packagist](https://packagist.org/packages/karlosagudo/fixtro) |
| [🕯️ PHP SA](https://github.com/ovr/phpsa) | Smart/Static Analyzer(sis) for PHP :bowtie::neckbeard: | Bugs finders | 2019-02-27 | [Source](https://github.com/ovr/phpsa)<br>[Packagist](https://packagist.org/packages/ovr/phpsa) |
| [🕯️ psecio:parse](https://github.com/psecio/parse.git) | Parse: A Static Security Scanner | Bugs finders | 2018-08-07 | [Source](https://github.com/psecio/parse)<br>[Packagist](https://packagist.org/packages/psecio/parse) |
| [🕯️ php-refactoring-browser](https://github.com/QafooLabs/php-refactoring-browser) | A command line refactoring tool for PHP | Fixers | 2017-11-15 | [Source](https://github.com/QafooLabs/php-refactoring-browser)<br>[Packagist](https://packagist.org/packages/qafoolabs/php-refactoring-browser) |
| [🕯️ Transphpile](https://github.com/jaytaph/Transphpile) | PHP 7 to PHP 5.6 Transpiler | Fixers | 2017-09-02 | [Source](https://github.com/jaytaph/Transphpile) |
| [🕯️ FunctionFQNReplacer](https://github.com/Roave/FunctionFQNReplacer) | provides a way to replace relative references of functions in function calls with absolute references | Fixers | 2017-07-05 | [Source](https://github.com/Roave/FunctionFQNReplacer) |
| [🕯️ PHP Manipulator](https://github.com/schmittjoh/php-manipulator) | Library for Analyzing and Modifying PHP Source Code | Misc | 2014-09-27 | [Source](https://github.com/schmittjoh/php-manipulator)<br>[Packagist](https://packagist.org/packages/jms/php-manipulator) |
