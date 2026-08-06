![GitHub last commit](https://img.shields.io/github/last-commit/ValentinNikolaev/custom-php-analysis-tools)
![visitors](https://visitor-badge.laobi.icu/badge?page_id=ValentinNikolaev.custom-php-analysis-tools)

# Static analysis tools for PHP

A generated catalog of PHP static analysis, code quality, coding standards, metrics, refactoring, and hosted analysis tools.

Inspired by the pioneering [PHP Static Analysis Tools catalog by Exakat](https://github.com/exakat/php-static-analysis-tools) and its contributors.

Catalog metadata comes from `common/catalog/*.yaml`; Editors' Choice copy comes from `common/editor-choice-copy.yaml`. Run `python scripts/full_workflow.py` to refresh metadata and regenerate this file.

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

Category quotas and repository data select these active projects. A human or LLM writes the recommendation copy, followed by an editorial pass.

⭐ shows GitHub stars; 🥇, 🥈, and 🥉 mark the first three repository entries in each section.

<a id="editors-bug-finders"></a>

### Bug finders

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
| [Skylos](https://skylos.dev/)<br><sub>⭐ 482</sub> | Local pull-request checks for dead code, secrets, security defects, and quality regressions | The local-first scanner checks pull requests for dead code, secrets, security defects, and quality regressions. |

<a id="editors-coding-standards"></a>

### Coding standards

Linters and rule-enforcement tools for formatting, naming, documentation, and project-specific coding conventions.

| Tool | Recommended for | Why it stands out |
|---|---|---|
| [EasyCodingStandard](https://github.com/Symplify/EasyCodingStandard)<br><sub>🥇 ⭐ 1,619</sub> | Teams running PHP-CS-Fixer and PHP_CodeSniffer through one configuration | One PHP config runs both rule engines in parallel and supports prepared rule sets and gradual adoption. |
| [PHP Code Sniffer](https://github.com/PHPCSStandards/PHP_CodeSniffer)<br><sub>🥈 ⭐ 1,537</sub> | Projects enforcing published standards or detailed custom coding rules | An extensible sniff API supports established standards and project-specific rules. |

<a id="editors-architecture-rules"></a>

### Architecture rules

Ready-to-use tools that enforce dependency boundaries and architectural constraints in an application.

| Tool | Recommended for | Why it stands out |
|---|---|---|
| [Deptrac](https://github.com/sensiolabs-de/deptrac.git)<br><sub>🥇 ⭐ 2,983</sub> | Layered applications and modular monoliths that enforce dependency boundaries in CI | Dependency rules turn layer and module boundaries into repeatable CI checks. |
| [PHP Architecture Tester](https://phpat.dev)<br><sub>🥈 ⭐ 1,273</sub> | Teams that prefer to express architecture constraints as readable PHP tests | A fluent PHP API keeps architecture tests in the same language and workflow as application tests. |

<a id="editors-libraries-and-building-blocks"></a>

### Libraries and building blocks

Parsers, reflection libraries, and control-flow components for developers building custom analysis rules or tools.

| Tool | Recommended for | Why it stands out |
|---|---|---|
| [PHP Parser](https://github.com/nikic/PHP-Parser)<br><sub>🥇 ⭐ 17,451</sub> | Developers building analyzers, refactoring tools, formatters, or source transformations | A stable AST, traversal API, and code builder support many PHP analyzers and transformation tools. |

<a id="editors-fixers-and-refactoring"></a>

### Fixers and refactoring

Tools that automatically correct coding-standard violations, upgrade PHP syntax, or refactor existing code.

| Tool | Recommended for | Why it stands out |
|---|---|---|
| [PHP CS Fixer](https://github.com/FriendsOfPHP/PHP-CS-Fixer)<br><sub>🥇 ⭐ 13,545</sub> | Projects that automatically apply PHP formatting and coding-standard fixes | A broad fixer catalog and custom rule sets cover published standards and project-specific formatting. |
| [Rector](https://github.com/rectorphp/rector)<br><sub>🥈 ⭐ 10,396</sub> | Teams automating PHP upgrades, framework migrations, or repeatable refactoring | AST-based rules turn upgrade and refactoring recipes into reviewable code changes across a project. |

<a id="editors-metrics-and-architecture"></a>

### Metrics and architecture

Tools that measure complexity, coupling, dependencies, maintainability, churn, and other structural properties.

| Tool | Recommended for | Why it stands out |
|---|---|---|
| [PHPInsights](https://youtube.com/@nunomaduro?sub_confirmation=1)<br><sub>🥇 ⭐ 5,626</sub> | Teams that want a quick command-line overview of PHP code quality | A single console report summarizes several code-quality signals and can enforce thresholds in CI. |
| [PHP Metrics](https://github.com/Halleck45/PhpMetrics)<br><sub>🥈 ⭐ 2,605</sub> | Visual review of complexity, coupling, maintainability, and project structure | Browsable reports make complexity, coupling, and architecture metrics easier to inspect than raw output. |
| [PDepend](https://pdepend.org/)<br><sub>🥉 ⭐ 958</sub> | Detailed object-oriented design, dependency, complexity, and maintainability metrics | JDepend-inspired metrics quantify coupling, complexity, dependencies, and maintainability. |
| [PhpCodeArcheology](https://phpcodearcheology.github.io)<br><sub>⭐ 87</sub> | Architecture review using code metrics, dependency graphs, and Git churn | One analyzer combines 60+ metrics, dependency graphs, Git churn hotspots, and an MCP server. |

<a id="editors-specialized-tools"></a>

### Specialized tools

Wrappers, baseliners, multi-language engines, and focused analysis tools that do not fit the primary categories.

| Tool | Recommended for | Why it stands out |
|---|---|---|
| [Semgrep](https://semgrep.dev)<br><sub>🥇 ⭐ 16,123</sub> | Security teams writing custom checks for PHP and polyglot repositories | Source-like rules make custom bug and security checks quicker to write than compiler-style analyzers. |
| [Larastan](https://github.com/larastan/larastan)<br><sub>🥈 ⭐ 6,479</sub> | Laravel applications that need PHPStan to understand framework conventions | Laravel-specific type information covers containers, facades, Eloquent, and other framework conventions. |

<a id="complete-catalog"></a>

## Complete catalog

Repository tables are sorted by activity, then GitHub stars. Hosted services are sorted alphabetically.

⭐ shows GitHub stars; 🥇, 🥈, and 🥉 mark the first three repository entries in each section.

**Links:** &lt;/&gt; source code · 🌐 official website · 📦 package.

**Activity:** Active = updated within 90 days; Quiet = 90–182 days; Inactive = 183–364 days; Unknown = no repository activity data. Projects inactive for at least a year move to In Memoriam.

<a id="all-bug-finders"></a>

### Bug finders

Tools that inspect PHP code without running it to identify type errors, defects, dependency problems, and potential vulnerabilities.

| Tool | Best for | Status | Links |
|---|---|---|---|
| [PHP Stan](https://github.com/phpstan/phpstan)<br><sub>🥇 ⭐ 14,061</sub> | PHP Static Analysis Tool - discover bugs in your code without running it! | Active<br><sub>Aug 6, 2026 · [2.2.8](https://github.com/phpstan/phpstan/releases/tag/2.2.8)</sub> | [&lt;/&gt;](https://github.com/phpstan/phpstan "GitHub source") · [📦](https://packagist.org/packages/phpstan/phpstan "Packagist package") |
| [jscpd](https://github.com/kucherenko/jscpd)<br><sub>🥈 ⭐ 5,972</sub> | Copy/paste detector for programming source code, supports 223 formats. AI-ready with… | Active<br><sub>Aug 6, 2026 · [v5.0.14](https://github.com/kucherenko/jscpd/releases/tag/v5.0.14)</sub> | [&lt;/&gt;](https://github.com/kucherenko/jscpd "GitHub source") |
| [psalm](https://psalm.dev)<br><sub>🥉 ⭐ 5,875</sub> | A PHP static analysis tool for finding errors and security vulnerabilities in PHP… | Active<br><sub>Jul 13, 2026 · 6.16.1</sub> | [&lt;/&gt;](https://github.com/vimeo/psalm "GitHub source") · [🌐](https://psalm.dev "Official website") · [📦](https://packagist.org/packages/vimeo/psalm "Packagist package") |
| [Phan](https://github.com/etsy/phan)<br><sub>⭐ 5,619</sub> | Phan is a static analyzer for PHP. Phan prefers to avoid false-positives and attempts… | Active<br><sub>Jul 20, 2026 · [6.0.7](https://github.com/phan/phan/releases/tag/6.0.7)</sub> | [&lt;/&gt;](https://github.com/phan/phan "GitHub source") · [📦](https://packagist.org/packages/phan/phan "Packagist package") |
| [mago](http://mago.carthage.software/)<br><sub>⭐ 3,361</sub> | Mago is a toolchain for PHP that aims to provide a set of tools to help developers… | Active<br><sub>Aug 4, 2026 · 1.46.0</sub> | [&lt;/&gt;](https://github.com/carthage-software/mago "GitHub source") · [🌐](http://mago.carthage.software/ "Official website") · [📦](https://packagist.org/packages/carthage-software/mago "Packagist package") |
| [PHP Mess Detector](https://phpmd.org)<br><sub>⭐ 2,443</sub> | PHPMD is a spin-off project of PHP Depend and aims to be a PHP equivalent of the well… | Active<br><sub>Aug 2, 2026 · [2.15.0](https://github.com/phpmd/phpmd/releases/tag/2.15.0)</sub> | [&lt;/&gt;](https://github.com/phpmd/phpmd "GitHub source") · [🌐](https://phpmd.org "Official website") · [📦](https://packagist.org/packages/phpmd/phpmd "Packagist package") |
| [PHP Compatibility](http://techblog.wimgodden.be/tag/codesniffer/)<br><sub>⭐ 2,299</sub> | PHP Compatibility check for PHP_CodeSniffer | Active<br><sub>Aug 5, 2026 · 9.3.5</sub> | [&lt;/&gt;](https://github.com/PHPCompatibility/PHPCompatibility "GitHub source") · [🌐](http://techblog.wimgodden.be/tag/codesniffer/ "Official website") · [📦](https://packagist.org/packages/phpcompatibility/php-compatibility "Packagist package") |
| [composer-dependency-analyser](https://github.com/shipmonk-rnd/composer-dependency-analyser)<br><sub>⭐ 623</sub> | 🚀 Fast detection of composer dependency issues (unused dependencies, shadow… | Active<br><sub>Aug 4, 2026 · 1.8.4</sub> | [&lt;/&gt;](https://github.com/shipmonk-rnd/composer-dependency-analyser "GitHub source") · [📦](https://packagist.org/packages/shipmonk/composer-dependency-analyser "Packagist package") |
| [Skylos](https://skylos.dev/)<br><sub>⭐ 482</sub> | Local pull-request scanning for dead code and security issues | Active<br><sub>Aug 5, 2026</sub> | [&lt;/&gt;](https://github.com/duriantaco/skylos "GitHub source") · [🌐](https://skylos.dev/ "Official website") |
| [SonarPHP](https://github.com/SonarSource/sonar-php)<br><sub>⭐ 430</sub> | PHP analysis in SonarQube and SonarQube for IDE | Active<br><sub>Aug 4, 2026</sub> | [&lt;/&gt;](https://github.com/SonarSource/sonar-php "GitHub source") |
| [php-compat-info](https://llaville.github.io/php-compatinfo/7.2/)<br><sub>⭐ 380</sub> | Library that find out the minimum version and the extensions required for a piece of… | Active<br><sub>May 20, 2026</sub> | [&lt;/&gt;](https://github.com/llaville/php-compatinfo "GitHub source") · [🌐](https://llaville.github.io/php-compatinfo/7.2/ "Official website") |
| [PHP-Parallel-Lint](https://github.com/php-parallel-lint/PHP-Parallel-Lint)<br><sub>⭐ 356</sub> | This tool check syntax of PHP files faster than serial check with fancier output. | Active<br><sub>Jul 26, 2026 · v1.4.0</sub> | [&lt;/&gt;](https://github.com/php-parallel-lint/PHP-Parallel-Lint "GitHub source") · [📦](https://packagist.org/packages/php-parallel-lint/php-parallel-lint "Packagist package") |
| [phanalist](https://denzyldick.github.io/phanalist/)<br><sub>⭐ 161</sub> | Performant static analyzer for PHP, which is extremely easy to use. It helps you catch… | Active<br><sub>Aug 4, 2026 · v1.1.10</sub> | [&lt;/&gt;](https://github.com/denzyldick/phanalist "GitHub source") · [🌐](https://denzyldick.github.io/phanalist/ "Official website") · [📦](https://packagist.org/packages/denzyl/phanalist "Packagist package") |
| [AST Metrics](http://ast-metrics.dev)<br><sub>⭐ 151</sub> | See the invisible structure of your code. Multi-language code quality and architecture… | Active<br><sub>Jul 29, 2026</sub> | [&lt;/&gt;](https://github.com/ast-metrics/ast-metrics "GitHub source") · [🌐](http://ast-metrics.dev "Official website") |
| [Coverage Guard](https://github.com/shipmonk-rnd/coverage-guard)<br><sub>⭐ 56</sub> | 🧪 Enforce PHP code coverage in your CI. Not by percentage, but target core methods!… | Active<br><sub>Jul 17, 2026 · 1.1.0</sub> | [&lt;/&gt;](https://github.com/shipmonk-rnd/coverage-guard "GitHub source") · [📦](https://packagist.org/packages/shipmonk/coverage-guard "Packagist package") |
| [PHPDoctor](https://github.com/voku/PHPDoctor)<br><sub>⭐ 53</sub> | 🏥 PHPDoctor: Check files, full directories or strings for missing or bad PHPDoc types. | Active<br><sub>Jul 10, 2026 · 0.8.0</sub> | [&lt;/&gt;](https://github.com/voku/PHPDoctor "GitHub source") · [📦](https://packagist.org/packages/voku/phpdoctor "Packagist package") |
| [name-collision-detector](https://github.com/shipmonk-rnd/name-collision-detector)<br><sub>⭐ 35</sub> | Fast & simple tool to find class duplicates in your projects. | Active<br><sub>Jun 23, 2026 · 2.1.1</sub> | [&lt;/&gt;](https://github.com/shipmonk-rnd/name-collision-detector "GitHub source") · [📦](https://packagist.org/packages/shipmonk/name-collision-detector "Packagist package") |
| [PHP Analysis](https://github.com/cwi-swat/php-analysis)<br><sub>⭐ 29</sub> | PHP language analyses in Rascal | Active<br><sub>May 13, 2026 · [v1.1.0](https://github.com/cwi-swat/php-analysis/releases/tag/v1.1.0)</sub> | [&lt;/&gt;](https://github.com/cwi-swat/php-analysis "GitHub source") |
| [Composer-Unused](https://github.com/composer-unused/composer-unused)<br><sub>⭐ 1,684</sub> | Show unused composer dependencies by scanning your code | Quiet<br><sub>Apr 27, 2026 · 0.9.6</sub> | [&lt;/&gt;](https://github.com/composer-unused/composer-unused "GitHub source") · [📦](https://packagist.org/packages/icanhazstring/composer-unused "Packagist package") |
| [PHP Magic Number Detector](https://github.com/povils/phpmnd)<br><sub>⭐ 585</sub> | PHP Magic Number Detector | Quiet<br><sub>Feb 25, 2026 · [v3.6.1](https://github.com/povils/phpmnd/releases/tag/v3.6.1)</sub> | [&lt;/&gt;](https://github.com/povils/phpmnd "GitHub source") · [📦](https://packagist.org/packages/povils/phpmnd "Packagist package") |
| [PHP Static Type Checker](https://codeberg.org/Jumping-Beaver/PHP_Static_Type_Checker) | Static type checker for PHP relying on the php-ast PECL extension. Mirrored from… | Quiet<br><sub>Apr 8, 2026</sub> | [&lt;/&gt;](https://github.com/Jumping-Beaver/PHP_Static_Type_Checker "GitHub source") · <span title="Website unavailable">🌐×</span> |
| [noverify](https://github.com/VKCOM/noverify)<br><sub>⭐ 688</sub> | Pretty fast linter (code static analysis utility) for PHP | Inactive<br><sub>Jan 19, 2026 · v0.5.5</sub> | [&lt;/&gt;](https://github.com/VKCOM/noverify "GitHub source") · [📦](https://packagist.org/packages/vkcom/noverify "Packagist package") |
| [Progpilot](https://github.com/designsecurity/progpilot)<br><sub>⭐ 365</sub> | A static analysis tool for security | Inactive<br><sub>Aug 17, 2025 · v1.3.0</sub> | [&lt;/&gt;](https://github.com/designsecurity/progpilot "GitHub source") · [📦](https://packagist.org/packages/designsecurity/progpilot "Packagist package") |
| [Exakat](http://www.exakat.io/) | Smart static analysis | Unknown | [🌐](http://www.exakat.io/ "Official website") |
| [PHP Inspection](https://plugins.jetbrains.com/plugin/7622?pr=idea) | Static analysis plugin for PHPStorm | Unknown | [🌐](https://plugins.jetbrains.com/plugin/7622?pr=idea "Official website") |
| [SonarQube](http://www.sonarqube.org/) | An open platform to manage code quality. It covers PHP code | Unknown | [🌐](http://www.sonarqube.org/ "Official website") |

<a id="all-coding-standards"></a>

### Coding standards

Linters and rule-enforcement tools for formatting, naming, documentation, and project-specific coding conventions.

| Tool | Best for | Status | Links |
|---|---|---|---|
| [EasyCodingStandard](https://github.com/Symplify/EasyCodingStandard)<br><sub>🥇 ⭐ 1,619</sub> | ECS runs PHP-CS-Fixer and PHP_CodeSniffer as a single, parallel fast tool with zero… | Active<br><sub>Jul 22, 2026 · [13.2.15](https://github.com/ecsphp/ecs/releases/tag/13.2.15)</sub> | [&lt;/&gt;](https://github.com/ecsphp/ecs "GitHub source") |
| [PHP Code Sniffer](https://github.com/PHPCSStandards/PHP_CodeSniffer)<br><sub>🥈 ⭐ 1,537</sub> | PHP_CodeSniffer tokenizes PHP files and detects violations of a defined set of coding… | Active<br><sub>Aug 6, 2026 · 4.0.4</sub> | [&lt;/&gt;](https://github.com/PHPCSStandards/PHP_CodeSniffer "GitHub source") · [📦](https://packagist.org/packages/phpcsstandards/php_codesniffer "Packagist package") |
| [composer-normalize](https://github.com/ergebnis/composer-normalize)<br><sub>🥉 ⭐ 1,115</sub> | 🎵 Provides a composer plugin for normalizing composer.json. | Active<br><sub>Aug 2, 2026 · 2.52.0</sub> | [&lt;/&gt;](https://github.com/ergebnis/composer-normalize "GitHub source") · [📦](https://packagist.org/packages/ergebnis/composer-normalize "Packagist package") |
| [editorconfig-checker](https://editorconfig-checker.github.io/)<br><sub>⭐ 75</sub> | A tool to verify that your files are in harmony with your .editorconfig | Active<br><sub>May 28, 2026 · 10.7.0</sub> | [&lt;/&gt;](https://github.com/editorconfig-checker/editorconfig-checker.php "GitHub source") · [🌐](https://editorconfig-checker.github.io/ "Official website") · [📦](https://packagist.org/packages/editorconfig-checker/editorconfig-checker "Packagist package") |
| [TLint](https://github.com/tighten/tlint)<br><sub>⭐ 526</sub> | Tighten linter for Laravel conventions. | Quiet<br><sub>Apr 30, 2026 · v9.6.1</sub> | [&lt;/&gt;](https://github.com/tighten/tlint "GitHub source") · [📦](https://packagist.org/packages/tightenco/tlint "Packagist package") |
| [PHP Doc Check](https://github.com/NielsdeBlaauw/php-doc-check)<br><sub>⭐ 43</sub> | Uses complexity metrics to determine which functions need documentation. | Inactive<br><sub>Dec 16, 2025 · v0.4.1</sub> | [&lt;/&gt;](https://github.com/NielsdeBlaauw/php-doc-check "GitHub source") · [📦](https://packagist.org/packages/niels-de-blaauw/php-doc-check "Packagist package") |

<a id="all-architecture-rules"></a>

### Architecture rules

Ready-to-use tools that enforce dependency boundaries and architectural constraints in an application.

| Tool | Best for | Status | Links |
|---|---|---|---|
| [Deptrac](https://github.com/sensiolabs-de/deptrac.git)<br><sub>🥇 ⭐ 2,983</sub> | Keep your architecture clean. | Active<br><sub>Jul 23, 2026 · 4.7.1</sub> | [&lt;/&gt;](https://github.com/deptrac/deptrac "GitHub source") · [📦](https://packagist.org/packages/deptrac/deptrac "Packagist package") |
| [PHP Architecture Tester](https://phpat.dev)<br><sub>🥈 ⭐ 1,273</sub> | ✔️ PHP Architecture Tester - Easy architecture testing for PHP | Active<br><sub>Jul 30, 2026 · 0.12.4</sub> | [&lt;/&gt;](https://github.com/carlosas/phpat "GitHub source") · [🌐](https://phpat.dev "Official website") · [📦](https://packagist.org/packages/carlosas/phpat "Packagist package") |
| [PHPArkitect](https://github.com/phparkitect/arkitect)<br><sub>🥉 ⭐ 923</sub> | Put your architectural rules under test! | Active<br><sub>Jul 31, 2026 · 1.3.0</sub> | [&lt;/&gt;](https://github.com/phparkitect/arkitect "GitHub source") · [📦](https://packagist.org/packages/phparkitect/phparkitect "Packagist package") |

<a id="all-libraries-and-building-blocks"></a>

### Libraries and building blocks

Parsers, reflection libraries, and control-flow components for developers building custom analysis rules or tools.

| Tool | Best for | Status | Links |
|---|---|---|---|
| [PHP Parser](https://github.com/nikic/PHP-Parser)<br><sub>🥇 ⭐ 17,451</sub> | A PHP parser written in PHP | Active<br><sub>Jul 11, 2026 · v5.8.0</sub> | [&lt;/&gt;](https://github.com/nikic/PHP-Parser "GitHub source") · [📦](https://packagist.org/packages/nikic/php-parser "Packagist package") |
| [Better Reflection](https://github.com/Roave/BetterReflection)<br><sub>🥈 ⭐ 1,245</sub> | :crystal_ball: Better Reflection is a reflection API that aims to improve and provide… | Active<br><sub>Aug 2, 2026 · 6.72.0</sub> | [&lt;/&gt;](https://github.com/Roave/BetterReflection "GitHub source") · [📦](https://packagist.org/packages/roave/better-reflection "Packagist package") |
| [PHP-cfg](https://github.com/ircmaxell/php-cfg)<br><sub>🥉 ⭐ 246</sub> | A Control Flow Graph implementation in PHP | Active<br><sub>Aug 1, 2026 · V0.8.1</sub> | [&lt;/&gt;](https://github.com/ircmaxell/php-cfg "GitHub source") · [📦](https://packagist.org/packages/ircmaxell/php-cfg "Packagist package") |
| [Reflection](https://github.com/phpDocumentor/Reflection.git)<br><sub>⭐ 125</sub> | Reflection library to do Static Analysis for PHP Projects | Active<br><sub>Jul 30, 2026 · 7.0.0</sub> | [&lt;/&gt;](https://github.com/phpDocumentor/Reflection "GitHub source") · [📦](https://packagist.org/packages/phpdocumentor/reflection "Packagist package") |

<a id="all-fixers-and-refactoring"></a>

### Fixers and refactoring

Tools that automatically correct coding-standard violations, upgrade PHP syntax, or refactor existing code.

| Tool | Best for | Status | Links |
|---|---|---|---|
| [PHP CS Fixer](https://github.com/FriendsOfPHP/PHP-CS-Fixer)<br><sub>🥇 ⭐ 13,545</sub> | A tool to automatically fix PHP Coding Standards issues | Active<br><sub>Jul 31, 2026 · v3.95.18</sub> | [&lt;/&gt;](https://github.com/PHP-CS-Fixer/PHP-CS-Fixer "GitHub source") · [📦](https://packagist.org/packages/friendsofphp/php-cs-fixer "Packagist package") |
| [Rector](https://github.com/rectorphp/rector)<br><sub>🥈 ⭐ 10,396</sub> | Instant Upgrades and Automated Refactoring of any PHP 5.3+ code | Active<br><sub>Aug 5, 2026 · 2.6.1</sub> | [&lt;/&gt;](https://github.com/rectorphp/rector "GitHub source") · [📦](https://packagist.org/packages/rector/rector "Packagist package") |
| [Phpactor](https://github.com/phpactor/phpactor)<br><sub>🥉 ⭐ 1,908</sub> | Mainly a PHP Language Server with more features than you can shake a stick at | Active<br><sub>Aug 1, 2026 · 2026.07.22.0</sub> | [&lt;/&gt;](https://github.com/phpactor/phpactor "GitHub source") · [📦](https://packagist.org/packages/phpactor/phpactor "Packagist package") |
| [php-scoper](https://github.com/humbug/php-scoper)<br><sub>⭐ 806</sub> | 🔨 Prefixes all PHP namespaces in a file/directory to isolate the code bundled in PHARs. | Active<br><sub>Jul 6, 2026 · 0.18.19</sub> | [&lt;/&gt;](https://github.com/humbug/php-scoper "GitHub source") · [📦](https://packagist.org/packages/humbug/php-scoper "Packagist package") |
| [PHP Weaver](https://github.com/troelskn/phpweaver)<br><sub>⭐ 85</sub> | A combined runtime/static code-analysis tool, that can trace parameter types | Inactive<br><sub>Jan 28, 2026</sub> | [&lt;/&gt;](https://github.com/troelskn/phpweaver "GitHub source") |

<a id="all-metrics-and-architecture"></a>

### Metrics and architecture

Tools that measure complexity, coupling, dependencies, maintainability, churn, and other structural properties.

| Tool | Best for | Status | Links |
|---|---|---|---|
| [PHPInsights](https://youtube.com/@nunomaduro?sub_confirmation=1)<br><sub>🥇 ⭐ 5,626</sub> | 🔰 Instant PHP quality checks from your console | Active<br><sub>Aug 4, 2026 · v2.14.2</sub> | [&lt;/&gt;](https://github.com/nunomaduro/phpinsights "GitHub source") · [🌐](https://youtube.com/@nunomaduro?sub_confirmation=1 "Official website") · [📦](https://packagist.org/packages/nunomaduro/phpinsights "Packagist package") |
| [PHP Metrics](https://github.com/Halleck45/PhpMetrics)<br><sub>🥈 ⭐ 2,605</sub> | Beautiful and understandable static analysis tool for PHP | Active<br><sub>Aug 2, 2026 · 2.10.0</sub> | [&lt;/&gt;](https://github.com/phpmetrics/PhpMetrics "GitHub source") · [📦](https://packagist.org/packages/phpmetrics/phpmetrics "Packagist package") |
| [PDepend](https://pdepend.org/)<br><sub>🥉 ⭐ 958</sub> | Measuring PHP design quality and dependency structure | Active<br><sub>Aug 2, 2026 · 2.16.2</sub> | [&lt;/&gt;](https://github.com/pdepend/pdepend "GitHub source") · [🌐](https://pdepend.org/ "Official website") · [📦](https://packagist.org/packages/pdepend/pdepend "Packagist package") |
| [PhpCodeArcheology](https://phpcodearcheology.github.io)<br><sub>⭐ 87</sub> | PHP static analysis for architecture & maintainability — 60+ metrics, complexity… | Active<br><sub>Aug 1, 2026</sub> | [&lt;/&gt;](https://github.com/PhpCodeArcheology/PhpCodeArcheology "GitHub source") · [🌐](https://phpcodearcheology.github.io "Official website") |
| [PHP Semantic Versioning Checker](https://github.com/tomzx/php-semver-checker)<br><sub>⭐ 436</sub> | Compares two source sets and determines the appropriate semantic versioning to apply. | Quiet<br><sub>Feb 5, 2026 · v0.17.0</sub> | [&lt;/&gt;](https://github.com/tomzx/php-semver-checker "GitHub source") · [📦](https://packagist.org/packages/tomzx/php-semver-checker "Packagist package") |
| [churn-php](https://github.com/bmitch/churn-php)<br><sub>⭐ 1,376</sub> | Discover files in need of refactoring. | Inactive<br><sub>Dec 31, 2025 · 1.7.3</sub> | [&lt;/&gt;](https://github.com/bmitch/churn-php "GitHub source") · [📦](https://packagist.org/packages/bmitch/churn-php "Packagist package") |
| [dePHPend](https://github.com/mihaeu/dephpend)<br><sub>⭐ 532</sub> | Detect flaws in your architecture, before they drag you down into the depths of… | Inactive<br><sub>Jan 28, 2026 · 0.9.0</sub> | [&lt;/&gt;](https://github.com/mihaeu/dephpend "GitHub source") · [📦](https://packagist.org/packages/dephpend/dephpend "Packagist package") |
| [php-class-dependencies-analyzer](https://php-quality-tools.com/class-dependencies-analyzer/)<br><sub>⭐ 21</sub> | This tool allows you to monitor the dependencies and instability of your classes | Inactive<br><sub>Jan 6, 2026</sub> | [&lt;/&gt;](https://github.com/DeGraciaMathieu/php-class-dependencies-analyzer "GitHub source") · <span title="Website unavailable">🌐×</span> |

<a id="all-hosted-analysis-services"></a>

### Hosted analysis services

Web-based services that analyze repositories through hosted scans, dashboards, or CI integrations.

| Service | Best for | Delivery | Link |
|---|---|---|---|
| [Bliss](https://blissai.com/index.html) | Automatically reviews code in real-time and shows how much it's worth in lines of code | Hosted service | [🌐](https://blissai.com/index.html "Official website") |
| [Checkmarx](http://lp.checkmarx.com/php-code-analysis/) | Get a full PHP static security code analysis and prevent security vulnerabilities | Hosted service | <span title="Website unavailable">🌐×</span> |
| [Codacy](https://www.codacy.com/) | Codacy: Automated Code Review | Hosted service | [🌐](https://www.codacy.com/ "Official website") |
| [Code Climate](https://codeclimate.com) | Hosted static analysis for Ruby, PHP and JavaScript source code | Hosted service | [🌐](https://codeclimate.com "Official website") |
| [DeepSource](https://deepsource.com/directory/php) | Continuous PHP static analysis, SAST, and coverage reporting | Hosted repository analysis with pull-request integrations | [🌐](https://deepsource.com/directory/php "Official website") |
| [Insight](https://insight.sensiolabs.com/) | A SensioLabs tool to analyzes source code to find problems that degrade the overall… | Hosted service | <span title="Website unavailable">🌐×</span> |
| [Laravelshift](https://laravelshift.com/) | the automated way to upgrade Laravel applications. Upgrade Laravel applications all… | Hosted service | [🌐](https://laravelshift.com/ "Official website") |
| [Qodana for PHP](https://www.jetbrains.com/qodana/) | PhpStorm-grade PHP inspections and quality gates in CI | Cloud reports with native or Docker-based PHP linters | [🌐](https://www.jetbrains.com/qodana/ "Official website") |
| [RIPS](https://www.ripstech.com/) | The superior security software for PHP applications. Source code static analyser for… | Hosted service | [🌐](https://www.ripstech.com/ "Official website") |
| [Scrutinizer](https://scrutinizer-ci.com/) | Improve code quality and find bugs before they hit production with our continuous… | Hosted service | <span title="Website unavailable">🌐×</span> |
| [Semgrep AppSec Platform](https://semgrep.dev/products/semgrep-appsec-platform/) | Managed PHP security scans, triage, and policy enforcement | Hosted managed scans with SCM and CI integrations | [🌐](https://semgrep.dev/products/semgrep-appsec-platform/ "Official website") |
| [SideCI](https://sideci.com/) | CI for automated code review by code analysis | Hosted service | <span title="Website unavailable">🌐×</span> |
| [Snyk Code](https://snyk.io/product/snyk-code/) | Security-focused PHP static application security testing | Hosted dashboard with SCM, CLI, IDE, and CI integrations | [🌐](https://snyk.io/product/snyk-code/ "Official website") |
| [SonarQube Cloud](https://www.sonarsource.com/products/sonarqube/cloud/) | Hosted PHP quality gates, maintainability checks, and security analysis | Hosted dashboard with repository and CI integrations | [🌐](https://www.sonarsource.com/products/sonarqube/cloud/ "Official website") |

<a id="all-specialized-tools"></a>

### Specialized tools

Wrappers, baseliners, multi-language engines, and focused analysis tools that do not fit the primary categories.

| Tool | Best for | Status | Links |
|---|---|---|---|
| [Semgrep](https://semgrep.dev)<br><sub>🥇 ⭐ 16,123</sub> | Lightweight static analysis for many languages. Find bug variants with patterns that… | Active<br><sub>Aug 6, 2026</sub> | [&lt;/&gt;](https://github.com/semgrep/semgrep "GitHub source") · [🌐](https://semgrep.dev "Official website") |
| [Larastan](https://github.com/larastan/larastan)<br><sub>🥈 ⭐ 6,479</sub> | ⚗️ Adds code analysis to Laravel improving developer productivity and code quality. | Active<br><sub>Jul 30, 2026 · v3.10.0</sub> | [&lt;/&gt;](https://github.com/larastan/larastan "GitHub source") · [📦](https://packagist.org/packages/larastan/larastan "Packagist package") |
| [GrumPHP](https://github.com/phpro/grumphp)<br><sub>🥉 ⭐ 4,306</sub> | Running a project’s PHP quality tools before code is committed | Active<br><sub>Jul 22, 2026</sub> | [&lt;/&gt;](https://github.com/phpro/grumphp "GitHub source") · [📦](https://packagist.org/packages/phpro/grumphp "Packagist package") |
| [Opengrep](https://github.com/opengrep/opengrep)<br><sub>⭐ 2,879</sub> | 🔎 Static code analysis engine to find security issues in code. | Active<br><sub>Aug 5, 2026</sub> | [&lt;/&gt;](https://github.com/opengrep/opengrep "GitHub source") |
| [jakzal/phpqa](https://hub.docker.com/r/jakzal/phpqa/)<br><sub>⭐ 1,319</sub> | Running a ready-made PHP analysis toolchain in Docker | Active<br><sub>Aug 3, 2026</sub> | [&lt;/&gt;](https://github.com/jakzal/phpqa "GitHub source") · [🌐](https://hub.docker.com/r/jakzal/phpqa/ "Official website") |
| [Composer Require Checker](https://github.com/maglnet/ComposerRequireChecker)<br><sub>⭐ 1,006</sub> | A CLI tool to check whether a specific composer package uses imported symbols that… | Active<br><sub>Aug 5, 2026 · 4.24.0</sub> | [&lt;/&gt;](https://github.com/maglnet/ComposerRequireChecker "GitHub source") · [📦](https://packagist.org/packages/maglnet/composer-require-checker "Packagist package") |
| [PHP Parser](https://php-parser.glayzzle.com/)<br><sub>⭐ 563</sub> | :herb: NodeJS PHP Parser - extract AST or tokens | Active<br><sub>Aug 5, 2026</sub> | [&lt;/&gt;](https://github.com/glayzzle/php-parser "GitHub source") · [🌐](https://php-parser.glayzzle.com/ "Official website") |
| [aislop](https://scanaislop.com)<br><sub>⭐ 537</sub> | Detecting AI-code mistakes and quality regressions before merge | Active<br><sub>Aug 1, 2026</sub> | [&lt;/&gt;](https://github.com/scanaislop/aislop "GitHub source") · [🌐](https://scanaislop.com "Official website") |
| [Static Analysis Results Baseliner](https://github.com/DaveLiddament/sarb)<br><sub>⭐ 165</sub> | Static Analysis Results Baseliner | Active<br><sub>Jul 12, 2026 · 1.11.0</sub> | [&lt;/&gt;](https://github.com/DaveLiddament/sarb "GitHub source") · [📦](https://packagist.org/packages/dave-liddament/sarb "Packagist package") |
| [devbug](http://www.devbug.co.uk/) | Ongoing work on PHP Analysis in Rascal (PHP AiR) | Unknown | <span title="Website unavailable">🌐×</span> |
| [HHVM](http://hhvm.com/) | Hack Language from Facebook. Add a SCA until version 3.3.8, newer version doesn't have… | Unknown | [🌐](http://hhvm.com/ "Official website") |
| [PHPQA](https://edgedesigncz.github.io/phpqa/) | A Wrapper to a lot of PHP tools reported into a single HTML file | Unknown | [🌐](https://edgedesigncz.github.io/phpqa/ "Official website") |

<a id="in-memoriam"></a>

## 🕯️ In Memoriam — PHP analysis pioneers

These projects are no longer actively maintained, but their ideas, code, and communities made a lasting contribution to the PHP ecosystem. We preserve them here with gratitude and respect.

| Project | Contribution | Category | Last activity | Legacy resources |
|---|---|---|---|---|
| [🕯️ PHPLOC](https://github.com/sebastianbergmann/phploc) | A tool for quickly measuring the size of a PHP project. | Metrics and architecture | Apr 12, 2025 | [&lt;/&gt;](https://github.com/sebastianbergmann/phploc "GitHub source") · [📦](https://packagist.org/packages/phploc/phploc "Packagist package") |
| [🕯️ PHP Assumption](https://github.com/rskuipers/php-assumptions.git) | Tool to detect assumptions | Bug finders | Mar 22, 2025 | [&lt;/&gt;](https://github.com/rskuipers/php-assumptions "GitHub source") · [📦](https://packagist.org/packages/rskuipers/php-assumptions "Packagist package") |
| [🕯️ Coverage Checker](https://github.com/exussum12/coverageChecker) | Allows old code to use new standards | Specialized tools | Jun 25, 2024 | [&lt;/&gt;](https://github.com/exussum12/coverageChecker "GitHub source") · [📦](https://packagist.org/packages/exussum12/coverage-checker "Packagist package") |
| [🕯️ PHP Code Sniffer](https://github.com/squizlabs/PHP_CodeSniffer) | PHP_CodeSniffer tokenizes PHP files and detects violations of a defined set of coding standards. | Coding standards | Apr 1, 2024 | [&lt;/&gt;](https://github.com/squizlabs/PHP_CodeSniffer "GitHub source") |
| [🕯️ PHPCodeFixer](https://github.com/wapmorgan/PhpCodeFixer) | Analyzer of PHP code to search issues with deprecated functionality in newer interpreter versions. | Bug finders | Feb 14, 2024 | [&lt;/&gt;](https://github.com/wapmorgan/PhpDeprecationDetector "GitHub source") |
| [🕯️ PhpDependencyAnalysis](https://github.com/mamuz/PhpDependencyAnalysis) | Static code analysis to find violations in a dependency graph | Metrics and architecture | Dec 3, 2023 | [&lt;/&gt;](https://github.com/mamuz/PhpDependencyAnalysis "GitHub source") |
| [🕯️ PhpCodeAnalyzer](https://github.com/wapmorgan/PhpCodeAnalyzer.git) | Really, it's "php extensions usage analyzer". It scans codebase and analyzes which non-built-in php… | Bug finders | Jan 17, 2023 | [&lt;/&gt;](https://github.com/wapmorgan/PhpCodeAnalyzer "GitHub source") |
| [🕯️ PHPCPD](https://github.com/sebastianbergmann/phpcpd) | Copy/Paste Detector (CPD) for PHP code. | Bug finders | Jan 10, 2023 | [&lt;/&gt;](https://github.com/sebastianbergmann/phpcpd "GitHub source") · [📦](https://packagist.org/packages/sebastian/phpcpd "Packagist package") |
| [🕯️ PHP-malware-finder](https://github.com/nbs-system/php-malware-finder) | Detect potentially malicious PHP files | Bug finders | Feb 22, 2022 | [&lt;/&gt;](https://github.com/nbs-system/php-malware-finder "GitHub source") |
| [🕯️ PHP testability](https://github.com/edsonmedina/php_testability) | Analyses and reports testability issues of a php codebase | Bug finders | Jan 27, 2022 | [&lt;/&gt;](https://github.com/edsonmedina/php_testability "GitHub source") · [📦](https://packagist.org/packages/edsonmedina/php_testability "Packagist package") |
| [🕯️ PHP formatter](https://github.com/mmoreram/php-formatter) | PHP Formatter is a PHP developer friendly set of tools | Coding standards | Jun 24, 2021 | [&lt;/&gt;](https://github.com/mmoreram/php-formatter "GitHub source") · [📦](https://packagist.org/packages/mmoreram/php-formatter "Packagist package") |
| [🕯️ PHP-Parallel-Lint](https://github.com/JakubOnderka/PHP-Parallel-Lint) | This tool check syntax of PHP files faster than serial check with fancier output. | Bug finders | Mar 13, 2021 | [&lt;/&gt;](https://github.com/JakubOnderka/PHP-Parallel-Lint "GitHub source") · [📦](https://packagist.org/packages/jakub-onderka/php-parallel-lint "Packagist package") |
| [🕯️ phpdoc to typehint](https://github.com/dunglas/phpdoc-to-typehint) | Add scalar type hints and return types to existing PHP projects using PHPDoc annotations | Fixers and refactoring | Dec 28, 2020 | [&lt;/&gt;](https://github.com/dunglas/phpdoc-to-typehint "GitHub source") · [📦](https://packagist.org/packages/dunglas/phpdoc-to-typehint "Packagist package") |
| [🕯️ Pahout](https://github.com/wata727/pahout) | A pair programming partner for writing better PHP. Pahout means PHP mahout :elephant: | Coding standards | Jun 26, 2020 | [&lt;/&gt;](https://github.com/wata727/pahout "GitHub source") · [📦](https://packagist.org/packages/wata727/pahout "Packagist package") |
| [🕯️ PHP BackSlasher](https://github.com/nilportugues/php-backslasher) | [Git hook] Tool to add all PHP internal functions and constants to its namespace by adding backslash to them. | Fixers and refactoring | Apr 21, 2020 | [&lt;/&gt;](https://github.com/nilportugues/php-backslasher "GitHub source") · [📦](https://packagist.org/packages/nilportugues/php_backslasher "Packagist package") |
| [🕯️ Quality Analyzer](https://github.com/Qafoo/QualityAnalyzer.git) | Tool helping us to analyze software projects | Metrics and architecture | Dec 6, 2019 | [&lt;/&gt;](https://github.com/Qafoo/QualityAnalyzer "GitHub source") · [📦](https://packagist.org/packages/qafoo/quality-analyzer "Packagist package") |
| [🕯️ php7mar](https://github.com/Alexia/php7mar) | PHP 7 Migration Assistant Report (MAR) | Bug finders | May 28, 2019 | [&lt;/&gt;](https://github.com/Alexia/php7mar "GitHub source") · [📦](https://packagist.org/packages/alexia/php7mar "Packagist package") |
| [🕯️ Pfff](https://github.com/facebook/pfff) | Tools for code analysis, visualizations, or style-preserving source transformation. | Bug finders | Mar 27, 2019 | [&lt;/&gt;](https://github.com/facebookarchive/pfff "GitHub source") |
| [🕯️ Fixtro](https://github.com/karlosagudo/fixtro) | A QA static analysis code, with a different approach | Specialized tools | Mar 2, 2019 | [&lt;/&gt;](https://github.com/karlosagudo/fixtro "GitHub source") · [📦](https://packagist.org/packages/karlosagudo/fixtro "Packagist package") |
| [🕯️ PHP SA](https://github.com/ovr/phpsa) | Smart/Static Analyzer(sis) for PHP :bowtie::neckbeard: | Bug finders | Feb 27, 2019 | [&lt;/&gt;](https://github.com/ovr/phpsa "GitHub source") · [📦](https://packagist.org/packages/ovr/phpsa "Packagist package") |
| [🕯️ psecio:parse](https://github.com/psecio/parse.git) | Parse: A Static Security Scanner | Bug finders | Aug 7, 2018 | [&lt;/&gt;](https://github.com/psecio/parse "GitHub source") · [📦](https://packagist.org/packages/psecio/parse "Packagist package") |
| [🕯️ php-refactoring-browser](https://github.com/QafooLabs/php-refactoring-browser) | A command line refactoring tool for PHP | Fixers and refactoring | Nov 15, 2017 | [&lt;/&gt;](https://github.com/QafooLabs/php-refactoring-browser "GitHub source") · [📦](https://packagist.org/packages/qafoolabs/php-refactoring-browser "Packagist package") |
| [🕯️ Transphpile](https://github.com/jaytaph/Transphpile) | PHP 7 to PHP 5.6 Transpiler | Fixers and refactoring | Sep 2, 2017 | [&lt;/&gt;](https://github.com/jaytaph/Transphpile "GitHub source") |
| [🕯️ FunctionFQNReplacer](https://github.com/Roave/FunctionFQNReplacer) | provides a way to replace relative references of functions in function calls with absolute references | Fixers and refactoring | Jul 5, 2017 | [&lt;/&gt;](https://github.com/Roave/FunctionFQNReplacer "GitHub source") |
| [🕯️ PHP Manipulator](https://github.com/schmittjoh/php-manipulator) | Library for Analyzing and Modifying PHP Source Code | Specialized tools | Sep 27, 2014 | [&lt;/&gt;](https://github.com/schmittjoh/php-manipulator "GitHub source") · [📦](https://packagist.org/packages/jms/php-manipulator "Packagist package") |
