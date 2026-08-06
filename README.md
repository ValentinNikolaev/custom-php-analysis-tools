![GitHub last commit](https://img.shields.io/github/last-commit/ValentinNikolaev/custom-php-analysis-tools)
![visitors](https://visitor-badge.laobi.icu/badge?page_id=ValentinNikolaev.custom-php-analysis-tools)

# Static analysis tools for PHP

A generated catalog of PHP static analysis, code quality, coding standards, metrics, refactoring, and hosted analysis tools.

Inspired by the pioneering [PHP Static Analysis Tools catalog by Exakat](https://github.com/exakat/php-static-analysis-tools) and its contributors.

The source of truth is `common/catalog/*.yaml`. Run `python scripts/full_workflow.py` to refresh metadata and regenerate this file.

To review and import newly listed active projects from Exakat, run `python scripts/full_workflow.py --import-exakat`.

## Table of contents

- [Editors' Choice](#editors-choice)
- [Complete catalog](#complete-catalog)
  - [Bug finders](#all-bug-finders)
  - [Coding standards](#all-coding-standards)
  - [Architecture rules](#all-architecture-rules)
  - [Libraries and building blocks](#all-libraries-and-building-blocks)
  - [Fixers and refactoring](#all-fixers-and-refactoring)
  - [Metrics and architecture](#all-metrics-and-architecture)
  - [Hosted analysis services](#all-hosted-analysis-services)
  - [Specialized tools](#all-specialized-tools)
- [In Memoriam](#in-memoriam)

<a id="editors-choice"></a>

## Editors' Choice

A decision-oriented shortlist of active projects selected by category, adoption, repository freshness, and archive signals.

<a id="editors-bug-finders"></a>

### Bug finders

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

<a id="editors-coding-standards"></a>

### Coding standards

Linters and rule-enforcement tools for formatting, naming, documentation, and project-specific coding conventions.

| Tool | Recommended for | Why it stands out |
|---|---|---|
| [EasyCodingStandard](https://github.com/Symplify/EasyCodingStandard)<br><sub>★ 1,619</sub> | ECS runs PHP-CS-Fixer and PHP_CodeSniffer as a single, parallel fast tool with zero dependencies. Run on PHP… | High adoption and recent maintenance: ★ 1,619; updated Jul 22, 2026. |
| [PHP Code Sniffer](https://github.com/PHPCSStandards/PHP_CodeSniffer)<br><sub>★ 1,537</sub> | PHP_CodeSniffer tokenizes PHP files and detects violations of a defined set of coding standards. | High adoption and recent maintenance: ★ 1,537; updated Aug 6, 2026. |

<a id="editors-architecture-rules"></a>

### Architecture rules

Ready-to-use tools that enforce dependency boundaries and architectural constraints in an application.

| Tool | Recommended for | Why it stands out |
|---|---|---|
| [Deptrac](https://github.com/sensiolabs-de/deptrac.git)<br><sub>★ 2,983</sub> | Keep your architecture clean. | High adoption and recent maintenance: ★ 2,983; updated Jul 23, 2026. |
| [PHP Architecture Tester](https://phpat.dev)<br><sub>★ 1,273</sub> | ✔️ PHP Architecture Tester - Easy architecture testing for PHP | High adoption and recent maintenance: ★ 1,273; updated Jul 30, 2026. |

<a id="editors-libraries-and-building-blocks"></a>

### Libraries and building blocks

Parsers, reflection libraries, and control-flow components for developers building custom analysis rules or tools.

| Tool | Recommended for | Why it stands out |
|---|---|---|
| [PHP Parser](https://github.com/nikic/PHP-Parser)<br><sub>★ 17,451</sub> | A PHP parser written in PHP | High adoption and recent maintenance: ★ 17,451; updated Jul 11, 2026. |

<a id="editors-fixers-and-refactoring"></a>

### Fixers and refactoring

Tools that automatically correct coding-standard violations, upgrade PHP syntax, or refactor existing code.

| Tool | Recommended for | Why it stands out |
|---|---|---|
| [PHP CS Fixer](https://github.com/FriendsOfPHP/PHP-CS-Fixer)<br><sub>★ 13,545</sub> | A tool to automatically fix PHP Coding Standards issues | High adoption and recent maintenance: ★ 13,545; updated Jul 31, 2026. |
| [Rector](https://github.com/rectorphp/rector)<br><sub>★ 10,396</sub> | Instant Upgrades and Automated Refactoring of any PHP 5.3+ code | High adoption and recent maintenance: ★ 10,396; updated Aug 5, 2026. |

<a id="editors-metrics-and-architecture"></a>

### Metrics and architecture

Tools that measure complexity, coupling, dependencies, maintainability, churn, and other structural properties.

| Tool | Recommended for | Why it stands out |
|---|---|---|
| [PHPInsights](https://youtube.com/@nunomaduro?sub_confirmation=1)<br><sub>★ 5,626</sub> | 🔰 Instant PHP quality checks from your console | High adoption and recent maintenance: ★ 5,626; updated Aug 4, 2026. |
| [PHP Metrics](https://github.com/Halleck45/PhpMetrics)<br><sub>★ 2,605</sub> | Beautiful and understandable static analysis tool for PHP | High adoption and recent maintenance: ★ 2,605; updated Aug 2, 2026. |
| [PDepend](https://pdepend.org/)<br><sub>★ 958</sub> | Measuring PHP design quality and dependency structure | Active community and recent maintenance: ★ 958; updated Aug 2, 2026. |
| [PhpCodeArcheology](https://phpcodearcheology.github.io)<br><sub>★ 87</sub> | PHP static analysis for architecture & maintainability — 60+ metrics, complexity analysis, dependency… | Recently maintained; updated Aug 1, 2026. |

<a id="editors-specialized-tools"></a>

### Specialized tools

Wrappers, baseliners, multi-language engines, and focused analysis tools that do not fit the primary categories.

| Tool | Recommended for | Why it stands out |
|---|---|---|
| [Semgrep](https://semgrep.dev)<br><sub>★ 16,123</sub> | Lightweight static analysis for many languages. Find bug variants with patterns that look like source code. | High adoption and recent maintenance: ★ 16,123; updated Aug 6, 2026. |
| [Larastan](https://github.com/larastan/larastan)<br><sub>★ 6,479</sub> | ⚗️ Adds code analysis to Laravel improving developer productivity and code quality. | High adoption and recent maintenance: ★ 6,479; updated Jul 30, 2026. |

<a id="complete-catalog"></a>

## Complete catalog

Repository tables are sorted by activity, then GitHub stars. Hosted services are sorted alphabetically.

**Activity:** Active = updated within 90 days; Quiet = 90–182 days; Inactive = 183–364 days; Unknown = no repository activity data. Projects inactive for at least a year move to In Memoriam.

<a id="all-bug-finders"></a>

### Bug finders

Tools that inspect PHP code without running it to identify type errors, defects, dependency problems, and potential vulnerabilities.

| Tool | What it does | Activity | Latest | Resources |
|---|---|---|---|---|
| [PHP Stan](https://github.com/phpstan/phpstan)<br><sub>★ 14,061</sub> | PHP Static Analysis Tool - discover bugs in your code without running it! | Active · Aug 6, 2026 | [2.2.8](https://github.com/phpstan/phpstan/releases/tag/2.2.8) | [GitHub](https://github.com/phpstan/phpstan) · [Packagist](https://packagist.org/packages/phpstan/phpstan) |
| [jscpd](https://github.com/kucherenko/jscpd)<br><sub>★ 5,972</sub> | Copy/paste detector for programming source code, supports 223 formats. AI-ready with token-efficient… | Active · Aug 6, 2026 | [v5.0.14](https://github.com/kucherenko/jscpd/releases/tag/v5.0.14) | [GitHub](https://github.com/kucherenko/jscpd) |
| [psalm](https://psalm.dev)<br><sub>★ 5,875</sub> | A PHP static analysis tool for finding errors and security vulnerabilities in PHP applications | Active · Jul 13, 2026 | 6.16.1 | [GitHub](https://github.com/vimeo/psalm) · [Packagist](https://packagist.org/packages/vimeo/psalm) |
| [Phan](https://github.com/etsy/phan)<br><sub>★ 5,619</sub> | Phan is a static analyzer for PHP. Phan prefers to avoid false-positives and attempts to prove incorrectness… | Active · Jul 20, 2026 | [6.0.7](https://github.com/phan/phan/releases/tag/6.0.7) | [GitHub](https://github.com/phan/phan) · [Packagist](https://packagist.org/packages/phan/phan) |
| [mago](http://mago.carthage.software/)<br><sub>★ 3,361</sub> | Mago is a toolchain for PHP that aims to provide a set of tools to help developers write better code. | Active · Aug 4, 2026 | 1.46.0 | [GitHub](https://github.com/carthage-software/mago) · [Packagist](https://packagist.org/packages/carthage-software/mago) |
| [PHP Mess Detector](https://phpmd.org)<br><sub>★ 2,443</sub> | PHPMD is a spin-off project of PHP Depend and aims to be a PHP equivalent of the well known Java tool PMD… | Active · Aug 2, 2026 | [2.15.0](https://github.com/phpmd/phpmd/releases/tag/2.15.0) | [GitHub](https://github.com/phpmd/phpmd) · [Packagist](https://packagist.org/packages/phpmd/phpmd) |
| [PHP Compatibility](http://techblog.wimgodden.be/tag/codesniffer/)<br><sub>★ 2,299</sub> | PHP Compatibility check for PHP_CodeSniffer | Active · Aug 5, 2026 | 9.3.5 | [GitHub](https://github.com/PHPCompatibility/PHPCompatibility) · [Packagist](https://packagist.org/packages/phpcompatibility/php-compatibility) |
| [composer-dependency-analyser](https://github.com/shipmonk-rnd/composer-dependency-analyser)<br><sub>★ 623</sub> | 🚀 Fast detection of composer dependency issues (unused dependencies, shadow dependencies, misplaced… | Active · Aug 4, 2026 | 1.8.4 | [GitHub](https://github.com/shipmonk-rnd/composer-dependency-analyser) · [Packagist](https://packagist.org/packages/shipmonk/composer-dependency-analyser) |
| [Skylos](https://skylos.dev/)<br><sub>★ 482</sub> | Local pull-request scanning for dead code and security issues | Active · Aug 5, 2026 | — | [GitHub](https://github.com/duriantaco/skylos) |
| [SonarPHP](https://github.com/SonarSource/sonar-php)<br><sub>★ 430</sub> | PHP analysis in SonarQube and SonarQube for IDE | Active · Aug 4, 2026 | — | [GitHub](https://github.com/SonarSource/sonar-php) |
| [php-compat-info](https://llaville.github.io/php-compatinfo/7.2/)<br><sub>★ 380</sub> | Library that find out the minimum version and the extensions required for a piece of code to run | Active · May 20, 2026 | — | [GitHub](https://github.com/llaville/php-compatinfo) |
| [PHP-Parallel-Lint](https://github.com/php-parallel-lint/PHP-Parallel-Lint)<br><sub>★ 356</sub> | This tool check syntax of PHP files faster than serial check with fancier output. | Active · Jul 26, 2026 | v1.4.0 | [GitHub](https://github.com/php-parallel-lint/PHP-Parallel-Lint) · [Packagist](https://packagist.org/packages/php-parallel-lint/php-parallel-lint) |
| [phanalist](https://denzyldick.github.io/phanalist/)<br><sub>★ 161</sub> | Performant static analyzer for PHP, which is extremely easy to use. It helps you catch common mistakes in… | Active · Aug 4, 2026 | v1.1.10 | [GitHub](https://github.com/denzyldick/phanalist) · [Packagist](https://packagist.org/packages/denzyl/phanalist) |
| [AST Metrics](http://ast-metrics.dev)<br><sub>★ 151</sub> | See the invisible structure of your code. Multi-language code quality and architecture analyzer (Go, PHP… | Active · Jul 29, 2026 | — | [GitHub](https://github.com/ast-metrics/ast-metrics) |
| [Coverage Guard](https://github.com/shipmonk-rnd/coverage-guard)<br><sub>★ 56</sub> | 🧪 Enforce PHP code coverage in your CI. Not by percentage, but target core methods! Allows you to start… | Active · Jul 17, 2026 | 1.1.0 | [GitHub](https://github.com/shipmonk-rnd/coverage-guard) · [Packagist](https://packagist.org/packages/shipmonk/coverage-guard) |
| [PHPDoctor](https://github.com/voku/PHPDoctor)<br><sub>★ 53</sub> | 🏥 PHPDoctor: Check files, full directories or strings for missing or bad PHPDoc types. | Active · Jul 10, 2026 | 0.8.0 | [GitHub](https://github.com/voku/PHPDoctor) · [Packagist](https://packagist.org/packages/voku/phpdoctor) |
| [name-collision-detector](https://github.com/shipmonk-rnd/name-collision-detector)<br><sub>★ 35</sub> | Fast & simple tool to find class duplicates in your projects. | Active · Jun 23, 2026 | 2.1.1 | [GitHub](https://github.com/shipmonk-rnd/name-collision-detector) · [Packagist](https://packagist.org/packages/shipmonk/name-collision-detector) |
| [PHP Analysis](https://github.com/cwi-swat/php-analysis)<br><sub>★ 29</sub> | PHP language analyses in Rascal | Active · May 13, 2026 | [v1.1.0](https://github.com/cwi-swat/php-analysis/releases/tag/v1.1.0) | [GitHub](https://github.com/cwi-swat/php-analysis) |
| [Composer-Unused](https://github.com/composer-unused/composer-unused)<br><sub>★ 1,684</sub> | Show unused composer dependencies by scanning your code | Quiet · Apr 27, 2026 | 0.9.6 | [GitHub](https://github.com/composer-unused/composer-unused) · [Packagist](https://packagist.org/packages/icanhazstring/composer-unused) |
| [PHP Magic Number Detector](https://github.com/povils/phpmnd)<br><sub>★ 585</sub> | PHP Magic Number Detector | Quiet · Feb 25, 2026 | [v3.6.1](https://github.com/povils/phpmnd/releases/tag/v3.6.1) | [GitHub](https://github.com/povils/phpmnd) · [Packagist](https://packagist.org/packages/povils/phpmnd) |
| [PHP Static Type Checker](https://codeberg.org/Jumping-Beaver/PHP_Static_Type_Checker) | Static type checker for PHP relying on the php-ast PECL extension. Mirrored from Codeberg.org | Quiet · Apr 8, 2026 | — | [GitHub](https://github.com/Jumping-Beaver/PHP_Static_Type_Checker) · Website unavailable |
| [noverify](https://github.com/VKCOM/noverify)<br><sub>★ 688</sub> | Pretty fast linter (code static analysis utility) for PHP | Inactive · Jan 19, 2026 | v0.5.5 | [GitHub](https://github.com/VKCOM/noverify) · [Packagist](https://packagist.org/packages/vkcom/noverify) |
| [Progpilot](https://github.com/designsecurity/progpilot)<br><sub>★ 365</sub> | A static analysis tool for security | Inactive · Aug 17, 2025 | v1.3.0 | [GitHub](https://github.com/designsecurity/progpilot) · [Packagist](https://packagist.org/packages/designsecurity/progpilot) |
| [Exakat](http://www.exakat.io/) | Smart static analysis | Unknown | — | — |
| [PHP Inspection](https://plugins.jetbrains.com/plugin/7622?pr=idea) | Static analysis plugin for PHPStorm | Unknown | — | — |
| [SonarQube](http://www.sonarqube.org/) | An open platform to manage code quality. It covers PHP code | Unknown | — | — |

<a id="all-coding-standards"></a>

### Coding standards

Linters and rule-enforcement tools for formatting, naming, documentation, and project-specific coding conventions.

| Tool | What it does | Activity | Latest | Resources |
|---|---|---|---|---|
| [EasyCodingStandard](https://github.com/Symplify/EasyCodingStandard)<br><sub>★ 1,619</sub> | ECS runs PHP-CS-Fixer and PHP_CodeSniffer as a single, parallel fast tool with zero dependencies. Run on PHP… | Active · Jul 22, 2026 | [13.2.15](https://github.com/ecsphp/ecs/releases/tag/13.2.15) | [GitHub](https://github.com/ecsphp/ecs) |
| [PHP Code Sniffer](https://github.com/PHPCSStandards/PHP_CodeSniffer)<br><sub>★ 1,537</sub> | PHP_CodeSniffer tokenizes PHP files and detects violations of a defined set of coding standards. | Active · Aug 6, 2026 | 4.0.4 | [GitHub](https://github.com/PHPCSStandards/PHP_CodeSniffer) · [Packagist](https://packagist.org/packages/phpcsstandards/php_codesniffer) |
| [composer-normalize](https://github.com/ergebnis/composer-normalize)<br><sub>★ 1,115</sub> | 🎵 Provides a composer plugin for normalizing composer.json. | Active · Aug 2, 2026 | 2.52.0 | [GitHub](https://github.com/ergebnis/composer-normalize) · [Packagist](https://packagist.org/packages/ergebnis/composer-normalize) |
| [editorconfig-checker](https://editorconfig-checker.github.io/)<br><sub>★ 75</sub> | A tool to verify that your files are in harmony with your .editorconfig | Active · May 28, 2026 | 10.7.0 | [GitHub](https://github.com/editorconfig-checker/editorconfig-checker.php) · [Packagist](https://packagist.org/packages/editorconfig-checker/editorconfig-checker) |
| [TLint](https://github.com/tighten/tlint)<br><sub>★ 526</sub> | Tighten linter for Laravel conventions. | Quiet · Apr 30, 2026 | v9.6.1 | [GitHub](https://github.com/tighten/tlint) · [Packagist](https://packagist.org/packages/tightenco/tlint) |
| [PHP Doc Check](https://github.com/NielsdeBlaauw/php-doc-check)<br><sub>★ 43</sub> | Uses complexity metrics to determine which functions need documentation. | Inactive · Dec 16, 2025 | v0.4.1 | [GitHub](https://github.com/NielsdeBlaauw/php-doc-check) · [Packagist](https://packagist.org/packages/niels-de-blaauw/php-doc-check) |

<a id="all-architecture-rules"></a>

### Architecture rules

Ready-to-use tools that enforce dependency boundaries and architectural constraints in an application.

| Tool | What it does | Activity | Latest | Resources |
|---|---|---|---|---|
| [Deptrac](https://github.com/sensiolabs-de/deptrac.git)<br><sub>★ 2,983</sub> | Keep your architecture clean. | Active · Jul 23, 2026 | 4.7.1 | [GitHub](https://github.com/deptrac/deptrac) · [Packagist](https://packagist.org/packages/deptrac/deptrac) |
| [PHP Architecture Tester](https://phpat.dev)<br><sub>★ 1,273</sub> | ✔️ PHP Architecture Tester - Easy architecture testing for PHP | Active · Jul 30, 2026 | 0.12.4 | [GitHub](https://github.com/carlosas/phpat) · [Packagist](https://packagist.org/packages/carlosas/phpat) |
| [PHPArkitect](https://github.com/phparkitect/arkitect)<br><sub>★ 923</sub> | Put your architectural rules under test! | Active · Jul 31, 2026 | 1.3.0 | [GitHub](https://github.com/phparkitect/arkitect) · [Packagist](https://packagist.org/packages/phparkitect/phparkitect) |

<a id="all-libraries-and-building-blocks"></a>

### Libraries and building blocks

Parsers, reflection libraries, and control-flow components for developers building custom analysis rules or tools.

| Tool | What it does | Activity | Latest | Resources |
|---|---|---|---|---|
| [PHP Parser](https://github.com/nikic/PHP-Parser)<br><sub>★ 17,451</sub> | A PHP parser written in PHP | Active · Jul 11, 2026 | v5.8.0 | [GitHub](https://github.com/nikic/PHP-Parser) · [Packagist](https://packagist.org/packages/nikic/php-parser) |
| [Better Reflection](https://github.com/Roave/BetterReflection)<br><sub>★ 1,245</sub> | :crystal_ball: Better Reflection is a reflection API that aims to improve and provide more features than… | Active · Aug 2, 2026 | 6.72.0 | [GitHub](https://github.com/Roave/BetterReflection) · [Packagist](https://packagist.org/packages/roave/better-reflection) |
| [PHP-cfg](https://github.com/ircmaxell/php-cfg)<br><sub>★ 246</sub> | A Control Flow Graph implementation in PHP | Active · Aug 1, 2026 | V0.8.1 | [GitHub](https://github.com/ircmaxell/php-cfg) · [Packagist](https://packagist.org/packages/ircmaxell/php-cfg) |
| [Reflection](https://github.com/phpDocumentor/Reflection.git)<br><sub>★ 125</sub> | Reflection library to do Static Analysis for PHP Projects | Active · Jul 30, 2026 | 7.0.0 | [GitHub](https://github.com/phpDocumentor/Reflection) · [Packagist](https://packagist.org/packages/phpdocumentor/reflection) |

<a id="all-fixers-and-refactoring"></a>

### Fixers and refactoring

Tools that automatically correct coding-standard violations, upgrade PHP syntax, or refactor existing code.

| Tool | What it does | Activity | Latest | Resources |
|---|---|---|---|---|
| [PHP CS Fixer](https://github.com/FriendsOfPHP/PHP-CS-Fixer)<br><sub>★ 13,545</sub> | A tool to automatically fix PHP Coding Standards issues | Active · Jul 31, 2026 | v3.95.18 | [GitHub](https://github.com/PHP-CS-Fixer/PHP-CS-Fixer) · [Packagist](https://packagist.org/packages/friendsofphp/php-cs-fixer) |
| [Rector](https://github.com/rectorphp/rector)<br><sub>★ 10,396</sub> | Instant Upgrades and Automated Refactoring of any PHP 5.3+ code | Active · Aug 5, 2026 | 2.6.1 | [GitHub](https://github.com/rectorphp/rector) · [Packagist](https://packagist.org/packages/rector/rector) |
| [Phpactor](https://github.com/phpactor/phpactor)<br><sub>★ 1,908</sub> | Mainly a PHP Language Server with more features than you can shake a stick at | Active · Aug 1, 2026 | 2026.07.22.0 | [GitHub](https://github.com/phpactor/phpactor) · [Packagist](https://packagist.org/packages/phpactor/phpactor) |
| [php-scoper](https://github.com/humbug/php-scoper)<br><sub>★ 806</sub> | 🔨 Prefixes all PHP namespaces in a file/directory to isolate the code bundled in PHARs. | Active · Jul 6, 2026 | 0.18.19 | [GitHub](https://github.com/humbug/php-scoper) · [Packagist](https://packagist.org/packages/humbug/php-scoper) |
| [PHP Weaver](https://github.com/troelskn/phpweaver)<br><sub>★ 85</sub> | A combined runtime/static code-analysis tool, that can trace parameter types | Inactive · Jan 28, 2026 | — | [GitHub](https://github.com/troelskn/phpweaver) |

<a id="all-metrics-and-architecture"></a>

### Metrics and architecture

Tools that measure complexity, coupling, dependencies, maintainability, churn, and other structural properties.

| Tool | What it does | Activity | Latest | Resources |
|---|---|---|---|---|
| [PHPInsights](https://youtube.com/@nunomaduro?sub_confirmation=1)<br><sub>★ 5,626</sub> | 🔰 Instant PHP quality checks from your console | Active · Aug 4, 2026 | v2.14.2 | [GitHub](https://github.com/nunomaduro/phpinsights) · [Packagist](https://packagist.org/packages/nunomaduro/phpinsights) |
| [PHP Metrics](https://github.com/Halleck45/PhpMetrics)<br><sub>★ 2,605</sub> | Beautiful and understandable static analysis tool for PHP | Active · Aug 2, 2026 | 2.10.0 | [GitHub](https://github.com/phpmetrics/PhpMetrics) · [Packagist](https://packagist.org/packages/phpmetrics/phpmetrics) |
| [PDepend](https://pdepend.org/)<br><sub>★ 958</sub> | Measuring PHP design quality and dependency structure | Active · Aug 2, 2026 | 2.16.2 | [GitHub](https://github.com/pdepend/pdepend) · [Packagist](https://packagist.org/packages/pdepend/pdepend) |
| [PhpCodeArcheology](https://phpcodearcheology.github.io)<br><sub>★ 87</sub> | PHP static analysis for architecture & maintainability — 60+ metrics, complexity analysis, dependency… | Active · Aug 1, 2026 | — | [GitHub](https://github.com/PhpCodeArcheology/PhpCodeArcheology) |
| [PHP Semantic Versioning Checker](https://github.com/tomzx/php-semver-checker)<br><sub>★ 436</sub> | Compares two source sets and determines the appropriate semantic versioning to apply. | Quiet · Feb 5, 2026 | v0.17.0 | [GitHub](https://github.com/tomzx/php-semver-checker) · [Packagist](https://packagist.org/packages/tomzx/php-semver-checker) |
| [churn-php](https://github.com/bmitch/churn-php)<br><sub>★ 1,376</sub> | Discover files in need of refactoring. | Inactive · Dec 31, 2025 | 1.7.3 | [GitHub](https://github.com/bmitch/churn-php) · [Packagist](https://packagist.org/packages/bmitch/churn-php) |
| [dePHPend](https://github.com/mihaeu/dephpend)<br><sub>★ 532</sub> | Detect flaws in your architecture, before they drag you down into the depths of dependency hell ... | Inactive · Jan 28, 2026 | 0.9.0 | [GitHub](https://github.com/mihaeu/dephpend) · [Packagist](https://packagist.org/packages/dephpend/dephpend) |
| [php-class-dependencies-analyzer](https://php-quality-tools.com/class-dependencies-analyzer/)<br><sub>★ 21</sub> | This tool allows you to monitor the dependencies and instability of your classes | Inactive · Jan 6, 2026 | — | [GitHub](https://github.com/DeGraciaMathieu/php-class-dependencies-analyzer) · Website unavailable |

<a id="all-hosted-analysis-services"></a>

### Hosted analysis services

Web-based services that analyze repositories through hosted scans, dashboards, or CI integrations.

| Service | Best for | Delivery | Website status |
|---|---|---|---|
| [Bliss](https://blissai.com/index.html) | Automatically reviews code in real-time and shows how much it's worth in lines of code | Hosted service | Website available |
| [Checkmarx](http://lp.checkmarx.com/php-code-analysis/) | Get a full PHP static security code analysis and prevent security vulnerabilities | Hosted service | Website unavailable |
| [Codacy](https://www.codacy.com/) | Codacy: Automated Code Review | Hosted service | Website available |
| [Code Climate](https://codeclimate.com) | Hosted static analysis for Ruby, PHP and JavaScript source code | Hosted service | Website available |
| [DeepSource](https://deepsource.com/directory/php) | Continuous PHP static analysis, SAST, and coverage reporting | Hosted repository analysis with pull-request integrations | Website available |
| [Insight](https://insight.sensiolabs.com/) | A SensioLabs tool to analyzes source code to find problems that degrade the overall quality of your projects | Hosted service | Website unavailable |
| [Laravelshift](https://laravelshift.com/) | the automated way to upgrade Laravel applications. Upgrade Laravel applications all the way from Laravel 4.2… | Hosted service | Website available |
| [Qodana for PHP](https://www.jetbrains.com/qodana/) | PhpStorm-grade PHP inspections and quality gates in CI | Cloud reports with native or Docker-based PHP linters | Website available |
| [RIPS](https://www.ripstech.com/) | The superior security software for PHP applications. Source code static analyser for vulnerabilities | Hosted service | Website available |
| [Scrutinizer](https://scrutinizer-ci.com/) | Improve code quality and find bugs before they hit production with our continuous inspection platform | Hosted service | Website unavailable |
| [Semgrep AppSec Platform](https://semgrep.dev/products/semgrep-appsec-platform/) | Managed PHP security scans, triage, and policy enforcement | Hosted managed scans with SCM and CI integrations | Website available |
| [SideCI](https://sideci.com/) | CI for automated code review by code analysis | Hosted service | Website unavailable |
| [Snyk Code](https://snyk.io/product/snyk-code/) | Security-focused PHP static application security testing | Hosted dashboard with SCM, CLI, IDE, and CI integrations | Website available |
| [SonarQube Cloud](https://www.sonarsource.com/products/sonarqube/cloud/) | Hosted PHP quality gates, maintainability checks, and security analysis | Hosted dashboard with repository and CI integrations | Website available |

<a id="all-specialized-tools"></a>

### Specialized tools

Wrappers, baseliners, multi-language engines, and focused analysis tools that do not fit the primary categories.

| Tool | What it does | Activity | Latest | Resources |
|---|---|---|---|---|
| [Semgrep](https://semgrep.dev)<br><sub>★ 16,123</sub> | Lightweight static analysis for many languages. Find bug variants with patterns that look like source code. | Active · Aug 6, 2026 | — | [GitHub](https://github.com/semgrep/semgrep) |
| [Larastan](https://github.com/larastan/larastan)<br><sub>★ 6,479</sub> | ⚗️ Adds code analysis to Laravel improving developer productivity and code quality. | Active · Jul 30, 2026 | v3.10.0 | [GitHub](https://github.com/larastan/larastan) · [Packagist](https://packagist.org/packages/larastan/larastan) |
| [GrumPHP](https://github.com/phpro/grumphp)<br><sub>★ 4,306</sub> | Running a project’s PHP quality tools before code is committed | Active · Jul 22, 2026 | — | [GitHub](https://github.com/phpro/grumphp) · [Packagist](https://packagist.org/packages/phpro/grumphp) |
| [Opengrep](https://github.com/opengrep/opengrep)<br><sub>★ 2,879</sub> | 🔎 Static code analysis engine to find security issues in code. | Active · Aug 5, 2026 | — | [GitHub](https://github.com/opengrep/opengrep) |
| [jakzal/phpqa](https://hub.docker.com/r/jakzal/phpqa/)<br><sub>★ 1,319</sub> | Running a ready-made PHP analysis toolchain in Docker | Active · Aug 3, 2026 | — | [GitHub](https://github.com/jakzal/phpqa) |
| [Composer Require Checker](https://github.com/maglnet/ComposerRequireChecker)<br><sub>★ 1,006</sub> | A CLI tool to check whether a specific composer package uses imported symbols that aren't part of its direct… | Active · Aug 5, 2026 | 4.24.0 | [GitHub](https://github.com/maglnet/ComposerRequireChecker) · [Packagist](https://packagist.org/packages/maglnet/composer-require-checker) |
| [PHP Parser](https://php-parser.glayzzle.com/)<br><sub>★ 563</sub> | :herb: NodeJS PHP Parser - extract AST or tokens | Active · Aug 5, 2026 | — | [GitHub](https://github.com/glayzzle/php-parser) |
| [aislop](https://scanaislop.com)<br><sub>★ 537</sub> | Detecting AI-code mistakes and quality regressions before merge | Active · Aug 1, 2026 | — | [GitHub](https://github.com/scanaislop/aislop) |
| [Static Analysis Results Baseliner](https://github.com/DaveLiddament/sarb)<br><sub>★ 165</sub> | Static Analysis Results Baseliner | Active · Jul 12, 2026 | 1.11.0 | [GitHub](https://github.com/DaveLiddament/sarb) · [Packagist](https://packagist.org/packages/dave-liddament/sarb) |
| [devbug](http://www.devbug.co.uk/) | Ongoing work on PHP Analysis in Rascal (PHP AiR) | Unknown | — | Website unavailable |
| [HHVM](http://hhvm.com/) | Hack Language from Facebook. Add a SCA until version 3.3.8, newer version doesn't have anymore | Unknown | — | — |
| [PHPQA](https://edgedesigncz.github.io/phpqa/) | A Wrapper to a lot of PHP tools reported into a single HTML file | Unknown | — | — |

<a id="in-memoriam"></a>

## 🕯️ In Memoriam — PHP analysis pioneers

These projects are no longer actively maintained, but their ideas, code, and communities made a lasting contribution to the PHP ecosystem. We preserve them here with gratitude and respect.

| Project | Contribution | Category | Last activity | Legacy resources |
|---|---|---|---|---|
| [🕯️ PHPLOC](https://github.com/sebastianbergmann/phploc) | A tool for quickly measuring the size of a PHP project. | Metrics and architecture | Apr 12, 2025 | [GitHub](https://github.com/sebastianbergmann/phploc) · [Packagist](https://packagist.org/packages/phploc/phploc) |
| [🕯️ PHP Assumption](https://github.com/rskuipers/php-assumptions.git) | Tool to detect assumptions | Bug finders | Mar 22, 2025 | [GitHub](https://github.com/rskuipers/php-assumptions) · [Packagist](https://packagist.org/packages/rskuipers/php-assumptions) |
| [🕯️ Coverage Checker](https://github.com/exussum12/coverageChecker) | Allows old code to use new standards | Specialized tools | Jun 25, 2024 | [GitHub](https://github.com/exussum12/coverageChecker) · [Packagist](https://packagist.org/packages/exussum12/coverage-checker) |
| [🕯️ PHP Code Sniffer](https://github.com/squizlabs/PHP_CodeSniffer) | PHP_CodeSniffer tokenizes PHP files and detects violations of a defined set of coding standards. | Coding standards | Apr 1, 2024 | [GitHub](https://github.com/squizlabs/PHP_CodeSniffer) |
| [🕯️ PHPCodeFixer](https://github.com/wapmorgan/PhpCodeFixer) | Analyzer of PHP code to search issues with deprecated functionality in newer interpreter versions. | Bug finders | Feb 14, 2024 | [GitHub](https://github.com/wapmorgan/PhpDeprecationDetector) |
| [🕯️ PhpDependencyAnalysis](https://github.com/mamuz/PhpDependencyAnalysis) | Static code analysis to find violations in a dependency graph | Metrics and architecture | Dec 3, 2023 | [GitHub](https://github.com/mamuz/PhpDependencyAnalysis) |
| [🕯️ PhpCodeAnalyzer](https://github.com/wapmorgan/PhpCodeAnalyzer.git) | Really, it's "php extensions usage analyzer". It scans codebase and analyzes which non-built-in php… | Bug finders | Jan 17, 2023 | [GitHub](https://github.com/wapmorgan/PhpCodeAnalyzer) |
| [🕯️ PHPCPD](https://github.com/sebastianbergmann/phpcpd) | Copy/Paste Detector (CPD) for PHP code. | Bug finders | Jan 10, 2023 | [GitHub](https://github.com/sebastianbergmann/phpcpd) · [Packagist](https://packagist.org/packages/sebastian/phpcpd) |
| [🕯️ PHP-malware-finder](https://github.com/nbs-system/php-malware-finder) | Detect potentially malicious PHP files | Bug finders | Feb 22, 2022 | [GitHub](https://github.com/nbs-system/php-malware-finder) |
| [🕯️ PHP testability](https://github.com/edsonmedina/php_testability) | Analyses and reports testability issues of a php codebase | Bug finders | Jan 27, 2022 | [GitHub](https://github.com/edsonmedina/php_testability) · [Packagist](https://packagist.org/packages/edsonmedina/php_testability) |
| [🕯️ PHP formatter](https://github.com/mmoreram/php-formatter) | PHP Formatter is a PHP developer friendly set of tools | Coding standards | Jun 24, 2021 | [GitHub](https://github.com/mmoreram/php-formatter) · [Packagist](https://packagist.org/packages/mmoreram/php-formatter) |
| [🕯️ PHP-Parallel-Lint](https://github.com/JakubOnderka/PHP-Parallel-Lint) | This tool check syntax of PHP files faster than serial check with fancier output. | Bug finders | Mar 13, 2021 | [GitHub](https://github.com/JakubOnderka/PHP-Parallel-Lint) · [Packagist](https://packagist.org/packages/jakub-onderka/php-parallel-lint) |
| [🕯️ phpdoc to typehint](https://github.com/dunglas/phpdoc-to-typehint) | Add scalar type hints and return types to existing PHP projects using PHPDoc annotations | Fixers and refactoring | Dec 28, 2020 | [GitHub](https://github.com/dunglas/phpdoc-to-typehint) · [Packagist](https://packagist.org/packages/dunglas/phpdoc-to-typehint) |
| [🕯️ Pahout](https://github.com/wata727/pahout) | A pair programming partner for writing better PHP. Pahout means PHP mahout :elephant: | Coding standards | Jun 26, 2020 | [GitHub](https://github.com/wata727/pahout) · [Packagist](https://packagist.org/packages/wata727/pahout) |
| [🕯️ PHP BackSlasher](https://github.com/nilportugues/php-backslasher) | [Git hook] Tool to add all PHP internal functions and constants to its namespace by adding backslash to them. | Fixers and refactoring | Apr 21, 2020 | [GitHub](https://github.com/nilportugues/php-backslasher) · [Packagist](https://packagist.org/packages/nilportugues/php_backslasher) |
| [🕯️ Quality Analyzer](https://github.com/Qafoo/QualityAnalyzer.git) | Tool helping us to analyze software projects | Metrics and architecture | Dec 6, 2019 | [GitHub](https://github.com/Qafoo/QualityAnalyzer) · [Packagist](https://packagist.org/packages/qafoo/quality-analyzer) |
| [🕯️ php7mar](https://github.com/Alexia/php7mar) | PHP 7 Migration Assistant Report (MAR) | Bug finders | May 28, 2019 | [GitHub](https://github.com/Alexia/php7mar) · [Packagist](https://packagist.org/packages/alexia/php7mar) |
| [🕯️ Pfff](https://github.com/facebook/pfff) | Tools for code analysis, visualizations, or style-preserving source transformation. | Bug finders | Mar 27, 2019 | [GitHub](https://github.com/facebookarchive/pfff) |
| [🕯️ Fixtro](https://github.com/karlosagudo/fixtro) | A QA static analysis code, with a different approach | Specialized tools | Mar 2, 2019 | [GitHub](https://github.com/karlosagudo/fixtro) · [Packagist](https://packagist.org/packages/karlosagudo/fixtro) |
| [🕯️ PHP SA](https://github.com/ovr/phpsa) | Smart/Static Analyzer(sis) for PHP :bowtie::neckbeard: | Bug finders | Feb 27, 2019 | [GitHub](https://github.com/ovr/phpsa) · [Packagist](https://packagist.org/packages/ovr/phpsa) |
| [🕯️ psecio:parse](https://github.com/psecio/parse.git) | Parse: A Static Security Scanner | Bug finders | Aug 7, 2018 | [GitHub](https://github.com/psecio/parse) · [Packagist](https://packagist.org/packages/psecio/parse) |
| [🕯️ php-refactoring-browser](https://github.com/QafooLabs/php-refactoring-browser) | A command line refactoring tool for PHP | Fixers and refactoring | Nov 15, 2017 | [GitHub](https://github.com/QafooLabs/php-refactoring-browser) · [Packagist](https://packagist.org/packages/qafoolabs/php-refactoring-browser) |
| [🕯️ Transphpile](https://github.com/jaytaph/Transphpile) | PHP 7 to PHP 5.6 Transpiler | Fixers and refactoring | Sep 2, 2017 | [GitHub](https://github.com/jaytaph/Transphpile) |
| [🕯️ FunctionFQNReplacer](https://github.com/Roave/FunctionFQNReplacer) | provides a way to replace relative references of functions in function calls with absolute references | Fixers and refactoring | Jul 5, 2017 | [GitHub](https://github.com/Roave/FunctionFQNReplacer) |
| [🕯️ PHP Manipulator](https://github.com/schmittjoh/php-manipulator) | Library for Analyzing and Modifying PHP Source Code | Specialized tools | Sep 27, 2014 | [GitHub](https://github.com/schmittjoh/php-manipulator) · [Packagist](https://packagist.org/packages/jms/php-manipulator) |
