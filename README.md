![GitHub last commit](https://img.shields.io/github/last-commit/ValentinNikolaev/custom-php-analysis-tools)
![visitors](https://visitor-badge.laobi.icu/badge?page_id=ValentinNikolaev.custom-php-analysis-tools)

# Static analysis tools for PHP

A generated catalog of PHP static analysis, code quality, coding standards, metrics, refactoring, and SaaS tools.

The source of truth is `common/catalog/*.yaml`. Run `python scripts/full_workflow.py` to refresh metadata and regenerate this file.

## Table of Contents

* [Bugs finders](#bugs-finders)
* [Coding standards](#coding-standards)
* [DIY](#diy)
* [Fixers](#fixers)
* [Metrics](#metrics)
* [SaaS](#saas)
* [Misc](#misc)

### Editors' Choice

##### Bugs finders

| Tool | Description | Stars | Updated | Latest | Links |
|---|---|---:|---|---|---|
| [PHP Stan](https://github.com/phpstan/phpstan) | PHP Static Analysis Tool - discover bugs in your code without running it! | 14,042 | 2026-07-25 | 2.2.5 | [GitHub](https://github.com/phpstan/phpstan)<br>[Packagist](https://packagist.org/packages/phpstan/phpstan) |
| [jscpd](https://github.com/kucherenko/jscpd) | Copy/paste detector for programming source code, supports 223 formats. AI-ready with token-efficient reporter, skill and MCP server. | 5,932 | 2026-07-24 | - | [GitHub](https://github.com/kucherenko/jscpd) |
| [psalm](https://psalm.dev) | A PHP static analysis tool for finding errors and security vulnerabilities in PHP applications | 5,869 | 2026-07-13 | 6.16.1 | [GitHub](https://github.com/vimeo/psalm)<br>[Packagist](https://packagist.org/packages/vimeo/psalm) |
| [Phan](https://github.com/etsy/phan) | Phan is a static analyzer for PHP. Phan prefers to avoid false-positives and attempts to prove incorrectness rather than correctness. | 5,619 | 2026-07-20 | 6.0.7 | [GitHub](https://github.com/phan/phan)<br>[Packagist](https://packagist.org/packages/phan/phan) |
| [mago](http://mago.carthage.software/) | Mago is a toolchain for PHP that aims to provide a set of tools to help developers write better code. | 3,329 | 2026-07-25 | 1.45.0 | [GitHub](https://github.com/carthage-software/mago)<br>[Packagist](https://packagist.org/packages/carthage-software/mago) |
| [PHP Mess Detector](https://phpmd.org) | PHPMD is a spin-off project of PHP Depend and aims to be a PHP equivalent of the well known Java tool PMD. PHPMD can be seen as an user friendly frontend application for the raw metrics stream measured by PHP Depend. | 2,443 | 2026-06-29 | 2.15.0 | [GitHub](https://github.com/phpmd/phpmd)<br>[Packagist](https://packagist.org/packages/phpmd/phpmd) |
| [Pfff](https://github.com/facebook/pfff) | Tools for code analysis, visualizations, or style-preserving source transformation. | 2,440 | 2019-03-27 | - | [GitHub](https://github.com/facebookarchive/pfff) |
| [PHPCPD](https://github.com/sebastianbergmann/phpcpd) | Copy/Paste Detector (CPD) for PHP code. | 2,211 | 2023-01-10 | v1.2 | [GitHub](https://github.com/sebastianbergmann/phpcpd)<br>[Packagist](https://packagist.org/packages/phpcpd-next/phpcpd) |
| [PHP Magic Number Detector](https://github.com/povils/phpmnd) | PHP Magic Number Detector | 585 | 2026-02-25 | v3.6.1 | [GitHub](https://github.com/povils/phpmnd)<br>[Packagist](https://packagist.org/packages/povils/phpmnd) |

##### Coding standards

| Tool | Description | Stars | Updated | Latest | Links |
|---|---|---:|---|---|---|
| [PHP Code Sniffer](https://github.com/squizlabs/PHP_CodeSniffer) | PHP_CodeSniffer tokenizes PHP files and detects violations of a defined set of coding standards. | 10,774 | 2024-04-01 | 4.0.1 | [GitHub](https://github.com/squizlabs/PHP_CodeSniffer)<br>[Packagist](https://packagist.org/packages/squizlabs/php_codesniffer) |
| [EasyCodingStandard](https://github.com/Symplify/EasyCodingStandard) | ECS runs PHP-CS-Fixer and PHP_CodeSniffer as a single, parallel fast tool with zero dependencies. Run on PHP 7.2+ | 1,618 | 2026-07-22 | - | [GitHub](https://github.com/ecsphp/ecs) |

##### DIY

| Tool | Description | Stars | Updated | Latest | Links |
|---|---|---:|---|---|---|
| [PHP Parser](https://github.com/nikic/PHP-Parser) | A PHP parser written in PHP | 17,452 | 2026-07-11 | v5.8.0 | [GitHub](https://github.com/nikic/PHP-Parser)<br>[Packagist](https://packagist.org/packages/nikic/php-parser) |

##### Fixers

| Tool | Description | Stars | Updated | Latest | Links |
|---|---|---:|---|---|---|
| [PHP CS Fixer](https://github.com/FriendsOfPHP/PHP-CS-Fixer) | A tool to automatically fix PHP Coding Standards issues | 13,547 | 2026-07-24 | v3.88.2 | [GitHub](https://github.com/PHP-CS-Fixer/PHP-CS-Fixer)<br>[Packagist](https://packagist.org/packages/composer-phar/php-cs-fixer) |
| [Rector](https://github.com/rectorphp/rector) | Instant Upgrades and Automated Refactoring of any PHP 5.3+ code | 10,380 | 2026-07-25 | 2.5.7 | [GitHub](https://github.com/rectorphp/rector)<br>[Packagist](https://packagist.org/packages/rector/rector) |

##### Metrics

| Tool | Description | Stars | Updated | Latest | Links |
|---|---|---:|---|---|---|
| [PHP Metrics](https://github.com/Halleck45/PhpMetrics) | Beautiful and understandable static analysis tool for PHP | 2,602 | 2026-07-22 | 2.10.0 | [GitHub](https://github.com/phpmetrics/PhpMetrics)<br>[Packagist](https://packagist.org/packages/phpmetrics/phpmetrics) |
| [PHPLOC](https://github.com/sebastianbergmann/phploc) | A tool for quickly measuring the size of a PHP project. | 2,344 | 2025-04-12 | 7.0.2 | [GitHub](https://github.com/sebastianbergmann/phploc)<br>[Packagist](https://packagist.org/packages/phploc/phploc) |
| [churn-php](https://github.com/bmitch/churn-php) | Discover files in need of refactoring. | 1,376 | 2025-12-31 | 1.7.3 | [GitHub](https://github.com/bmitch/churn-php)<br>[Packagist](https://packagist.org/packages/bmitch/churn-php) |
| [PhpDependencyAnalysis](https://github.com/mamuz/PhpDependencyAnalysis) | Static code analysis to find violations in a dependency graph | 575 | 2023-12-03 | v2.0.2 | [GitHub](https://github.com/mamuz/PhpDependencyAnalysis)<br>[Packagist](https://packagist.org/packages/agratushniy/php-dependency-analysis) |
| [dePHPend](https://github.com/mihaeu/dephpend) | Detect flaws in your architecture, before they drag you down into the depths of dependency hell ... | 533 | 2026-01-28 | - | [GitHub](https://github.com/mihaeu/dephpend)<br>[Packagist](https://packagist.org/packages/mihaeu/dephpend-tests) |
| [PHP Semantic Versioning Checker](https://github.com/tomzx/php-semver-checker) | Compares two source sets and determines the appropriate semantic versioning to apply. | 436 | 2026-02-05 | v0.17.0 | [GitHub](https://github.com/tomzx/php-semver-checker)<br>[Packagist](https://packagist.org/packages/tomzx/php-semver-checker) |

##### Misc

| Tool | Description | Stars | Updated | Latest | Links |
|---|---|---:|---|---|---|
| [Composer Require Checker](https://github.com/maglnet/ComposerRequireChecker) | A CLI tool to check whether a specific composer package uses imported symbols that aren't part of its direct composer dependencies | 1,005 | 2026-07-25 | 4.24.0 | [GitHub](https://github.com/maglnet/ComposerRequireChecker)<br>[Packagist](https://packagist.org/packages/maglnet/composer-require-checker) |
| [Coverage Checker](https://github.com/exussum12/coverageChecker) | Allows old code to use new standards | 176 | 2024-06-25 | 1.1.1 | [GitHub](https://github.com/exussum12/coverageChecker)<br>[Packagist](https://packagist.org/packages/exussum12/coverage-checker) |

### Whole list

##### Bugs finders

| Tool | Description | Stars | Updated | Latest | Links |
|---|---|---:|---|---|---|
| [PHP Stan](https://github.com/phpstan/phpstan) | PHP Static Analysis Tool - discover bugs in your code without running it! | 14,042 | 2026-07-25 | 2.2.5 | [GitHub](https://github.com/phpstan/phpstan)<br>[Packagist](https://packagist.org/packages/phpstan/phpstan) |
| [jscpd](https://github.com/kucherenko/jscpd) | Copy/paste detector for programming source code, supports 223 formats. AI-ready with token-efficient reporter, skill and MCP server. | 5,932 | 2026-07-24 | - | [GitHub](https://github.com/kucherenko/jscpd) |
| [psalm](https://psalm.dev) | A PHP static analysis tool for finding errors and security vulnerabilities in PHP applications | 5,869 | 2026-07-13 | 6.16.1 | [GitHub](https://github.com/vimeo/psalm)<br>[Packagist](https://packagist.org/packages/vimeo/psalm) |
| [Phan](https://github.com/etsy/phan) | Phan is a static analyzer for PHP. Phan prefers to avoid false-positives and attempts to prove incorrectness rather than correctness. | 5,619 | 2026-07-20 | 6.0.7 | [GitHub](https://github.com/phan/phan)<br>[Packagist](https://packagist.org/packages/phan/phan) |
| [mago](http://mago.carthage.software/) | Mago is a toolchain for PHP that aims to provide a set of tools to help developers write better code. | 3,329 | 2026-07-25 | 1.45.0 | [GitHub](https://github.com/carthage-software/mago)<br>[Packagist](https://packagist.org/packages/carthage-software/mago) |
| [PHP Mess Detector](https://phpmd.org) | PHPMD is a spin-off project of PHP Depend and aims to be a PHP equivalent of the well known Java tool PMD. PHPMD can be seen as an user friendly frontend application for the raw metrics stream measured by PHP Depend. | 2,443 | 2026-06-29 | 2.15.0 | [GitHub](https://github.com/phpmd/phpmd)<br>[Packagist](https://packagist.org/packages/phpmd/phpmd) |
| [Pfff](https://github.com/facebook/pfff) | Tools for code analysis, visualizations, or style-preserving source transformation. | 2,440 | 2019-03-27 | - | [GitHub](https://github.com/facebookarchive/pfff) |
| [PHPCPD](https://github.com/sebastianbergmann/phpcpd) | Copy/Paste Detector (CPD) for PHP code. | 2,211 | 2023-01-10 | v1.2 | [GitHub](https://github.com/sebastianbergmann/phpcpd)<br>[Packagist](https://packagist.org/packages/phpcpd-next/phpcpd) |
| [php7mar](https://github.com/Alexia/php7mar) | PHP 7 Migration Assistant Report (MAR) | 783 | 2019-05-28 | v0.2.0-beta | [GitHub](https://github.com/Alexia/php7mar)<br>[Packagist](https://packagist.org/packages/alexia/php7mar) |
| [PHP-Parallel-Lint](https://github.com/JakubOnderka/PHP-Parallel-Lint) | This tool check syntax of PHP files faster than serial check with fancier output. | 641 | 2021-03-13 | v1.0.0 | [GitHub](https://github.com/JakubOnderka/PHP-Parallel-Lint)<br>[Packagist](https://packagist.org/packages/jakub-onderka/php-parallel-lint) |
| [PHP SA](https://github.com/ovr/phpsa) | Smart/Static Analyzer(sis) for PHP :bowtie::neckbeard: | 635 | 2019-02-27 | 0.6.2 | [GitHub](https://github.com/ovr/phpsa)<br>[Packagist](https://packagist.org/packages/ovr/phpsa) |
| [PHP Magic Number Detector](https://github.com/povils/phpmnd) | PHP Magic Number Detector | 585 | 2026-02-25 | v3.6.1 | [GitHub](https://github.com/povils/phpmnd)<br>[Packagist](https://packagist.org/packages/povils/phpmnd) |
| [psecio:parse](https://github.com/psecio/parse.git) | Parse: A Static Security Scanner | 381 | 2018-08-07 | 0.8 | [GitHub](https://github.com/psecio/parse)<br>[Packagist](https://packagist.org/packages/psecio/parse) |
| [PHPCodeFixer](https://github.com/wapmorgan/PhpCodeFixer) | Analyzer of PHP code to search issues with deprecated functionality in newer interpreter versions. | 367 | 2024-02-14 | - | [GitHub](https://github.com/wapmorgan/PhpDeprecationDetector) |
| [PHP-malware-finder](https://github.com/nbs-system/php-malware-finder) | Detect potentially malicious PHP files | 342 | 2022-02-22 | - | [GitHub](https://github.com/nbs-system/php-malware-finder) |
| [PHP Assumption](https://github.com/rskuipers/php-assumptions.git) | Tool to detect assumptions | 164 | 2025-03-22 | 0.9.1 | [GitHub](https://github.com/rskuipers/php-assumptions)<br>[Packagist](https://packagist.org/packages/rskuipers/php-assumptions) |
| [PHP testability](https://github.com/edsonmedina/php_testability) | Analyses and reports testability issues of a php codebase | 130 | 2022-01-27 | - | [GitHub](https://github.com/edsonmedina/php_testability)<br>[Packagist](https://packagist.org/packages/edsonmedina/php_testability) |
| [PhpCodeAnalyzer](https://github.com/wapmorgan/PhpCodeAnalyzer.git) | Really, it's "php extensions usage analyzer". It scans codebase and analyzes which non-built-in php extensions used | 96 | 2023-01-17 | - | [GitHub](https://github.com/wapmorgan/PhpCodeAnalyzer) |
| [PHP Analysis](https://github.com/cwi-swat/php-analysis) | PHP language analyses in Rascal | 29 | 2026-05-13 | - | [GitHub](https://github.com/cwi-swat/php-analysis) |
| [Exakat](http://www.exakat.io/) | Smart static analysis | - | - | - | - |
| [PHP Inspection](https://plugins.jetbrains.com/plugin/7622?pr=idea) | Static analysis plugin for PHPStorm | - | - | - | - |
| [SonarQube](http://www.sonarqube.org/) | An open platform to manage code quality. It covers PHP code | - | - | - | - |

##### Coding standards

| Tool | Description | Stars | Updated | Latest | Links |
|---|---|---:|---|---|---|
| [PHP Code Sniffer](https://github.com/squizlabs/PHP_CodeSniffer) | PHP_CodeSniffer tokenizes PHP files and detects violations of a defined set of coding standards. | 10,774 | 2024-04-01 | 4.0.1 | [GitHub](https://github.com/squizlabs/PHP_CodeSniffer)<br>[Packagist](https://packagist.org/packages/squizlabs/php_codesniffer) |
| [EasyCodingStandard](https://github.com/Symplify/EasyCodingStandard) | ECS runs PHP-CS-Fixer and PHP_CodeSniffer as a single, parallel fast tool with zero dependencies. Run on PHP 7.2+ | 1,618 | 2026-07-22 | - | [GitHub](https://github.com/ecsphp/ecs) |
| [PHP formatter](https://github.com/mmoreram/php-formatter) | PHP Formatter is a PHP developer friendly set of tools | 168 | 2021-06-24 | v1.3.3 | [GitHub](https://github.com/mmoreram/php-formatter)<br>[Packagist](https://packagist.org/packages/mmoreram/php-formatter) |
| [Pahout](https://github.com/wata727/pahout) | A pair programming partner for writing better PHP. Pahout means PHP mahout :elephant: | 48 | 2020-06-26 | 0.7.0 | [GitHub](https://github.com/wata727/pahout)<br>[Packagist](https://packagist.org/packages/wata727/pahout) |

##### DIY

| Tool | Description | Stars | Updated | Latest | Links |
|---|---|---:|---|---|---|
| [PHP Parser](https://github.com/nikic/PHP-Parser) | A PHP parser written in PHP | 17,452 | 2026-07-11 | v5.8.0 | [GitHub](https://github.com/nikic/PHP-Parser)<br>[Packagist](https://packagist.org/packages/nikic/php-parser) |
| [Deptrac](https://github.com/sensiolabs-de/deptrac.git) | Keep your architecture clean. | 2,979 | 2026-07-23 | 4.7.1 | [GitHub](https://github.com/deptrac/deptrac)<br>[Packagist](https://packagist.org/packages/deptrac/deptrac) |
| [Better Reflection](https://github.com/Roave/BetterReflection) | :crystal_ball: Better Reflection is a reflection API that aims to improve and provide more features than PHP's built-in reflection API. | 1,245 | 2026-07-25 | 6.72.0 | [GitHub](https://github.com/Roave/BetterReflection)<br>[Packagist](https://packagist.org/packages/roave/better-reflection) |
| [PHP-cfg](https://github.com/ircmaxell/php-cfg) | A Control Flow Graph implementation in PHP | 247 | 2026-07-11 | V0.8.1 | [GitHub](https://github.com/ircmaxell/php-cfg)<br>[Packagist](https://packagist.org/packages/ircmaxell/php-cfg) |
| [Reflection](https://github.com/phpDocumentor/Reflection.git) | Reflection library to do Static Analysis for PHP Projects | 125 | 2026-07-06 | 7.0.0 | [GitHub](https://github.com/phpDocumentor/Reflection)<br>[Packagist](https://packagist.org/packages/phpdocumentor/reflection) |

##### Fixers

| Tool | Description | Stars | Updated | Latest | Links |
|---|---|---:|---|---|---|
| [PHP CS Fixer](https://github.com/FriendsOfPHP/PHP-CS-Fixer) | A tool to automatically fix PHP Coding Standards issues | 13,547 | 2026-07-24 | v3.88.2 | [GitHub](https://github.com/PHP-CS-Fixer/PHP-CS-Fixer)<br>[Packagist](https://packagist.org/packages/composer-phar/php-cs-fixer) |
| [Rector](https://github.com/rectorphp/rector) | Instant Upgrades and Automated Refactoring of any PHP 5.3+ code | 10,380 | 2026-07-25 | 2.5.7 | [GitHub](https://github.com/rectorphp/rector)<br>[Packagist](https://packagist.org/packages/rector/rector) |
| [php-refactoring-browser](https://github.com/QafooLabs/php-refactoring-browser) | A command line refactoring tool for PHP | 548 | 2017-11-15 | v0.1 | [GitHub](https://github.com/QafooLabs/php-refactoring-browser)<br>[Packagist](https://packagist.org/packages/qafoolabs/php-refactoring-browser) |
| [phpdoc to typehint](https://github.com/dunglas/phpdoc-to-typehint) | Add scalar type hints and return types to existing PHP projects using PHPDoc annotations | 225 | 2020-12-28 | v0.1.0 | [GitHub](https://github.com/dunglas/phpdoc-to-typehint)<br>[Packagist](https://packagist.org/packages/dunglas/phpdoc-to-typehint) |
| [Transphpile](https://github.com/jaytaph/Transphpile) | PHP 7 to PHP 5.6 Transpiler | 178 | 2017-09-02 | - | [GitHub](https://github.com/jaytaph/Transphpile) |
| [FunctionFQNReplacer](https://github.com/Roave/FunctionFQNReplacer) | provides a way to replace relative references of functions in function calls with absolute references | 158 | 2017-07-05 | - | [GitHub](https://github.com/Roave/FunctionFQNReplacer) |
| [PHP BackSlasher](https://github.com/nilportugues/php-backslasher) | [Git hook] Tool to add all PHP internal functions and constants to its namespace by adding backslash to them. | 88 | 2020-04-21 | 1.1.4 | [GitHub](https://github.com/nilportugues/php-backslasher)<br>[Packagist](https://packagist.org/packages/nilportugues/php_backslasher) |
| [PHP Weaver](https://github.com/troelskn/phpweaver) | A combined runtime/static code-analysis tool, that can trace parameter types | 85 | 2026-01-28 | - | [GitHub](https://github.com/troelskn/phpweaver) |

##### Metrics

| Tool | Description | Stars | Updated | Latest | Links |
|---|---|---:|---|---|---|
| [PHP Metrics](https://github.com/Halleck45/PhpMetrics) | Beautiful and understandable static analysis tool for PHP | 2,602 | 2026-07-22 | 2.10.0 | [GitHub](https://github.com/phpmetrics/PhpMetrics)<br>[Packagist](https://packagist.org/packages/phpmetrics/phpmetrics) |
| [PHPLOC](https://github.com/sebastianbergmann/phploc) | A tool for quickly measuring the size of a PHP project. | 2,344 | 2025-04-12 | 7.0.2 | [GitHub](https://github.com/sebastianbergmann/phploc)<br>[Packagist](https://packagist.org/packages/phploc/phploc) |
| [churn-php](https://github.com/bmitch/churn-php) | Discover files in need of refactoring. | 1,376 | 2025-12-31 | 1.7.3 | [GitHub](https://github.com/bmitch/churn-php)<br>[Packagist](https://packagist.org/packages/bmitch/churn-php) |
| [PhpDependencyAnalysis](https://github.com/mamuz/PhpDependencyAnalysis) | Static code analysis to find violations in a dependency graph | 575 | 2023-12-03 | v2.0.2 | [GitHub](https://github.com/mamuz/PhpDependencyAnalysis)<br>[Packagist](https://packagist.org/packages/agratushniy/php-dependency-analysis) |
| [dePHPend](https://github.com/mihaeu/dephpend) | Detect flaws in your architecture, before they drag you down into the depths of dependency hell ... | 533 | 2026-01-28 | - | [GitHub](https://github.com/mihaeu/dephpend)<br>[Packagist](https://packagist.org/packages/mihaeu/dephpend-tests) |
| [Quality Analyzer](https://github.com/Qafoo/QualityAnalyzer.git) | Tool helping us to analyze software projects | 490 | 2019-12-06 | - | [GitHub](https://github.com/Qafoo/QualityAnalyzer)<br>[Packagist](https://packagist.org/packages/qafoo/quality-analyzer) |
| [PHP Semantic Versioning Checker](https://github.com/tomzx/php-semver-checker) | Compares two source sets and determines the appropriate semantic versioning to apply. | 436 | 2026-02-05 | v0.17.0 | [GitHub](https://github.com/tomzx/php-semver-checker)<br>[Packagist](https://packagist.org/packages/tomzx/php-semver-checker) |

##### SaaS

| Tool | Description | Stars | Updated | Latest | Links |
|---|---|---:|---|---|---|
| [Bliss](https://blissai.com/index.html) | Automatically reviews code in real-time and shows how much it's worth in lines of code | - | - | - | - |
| [Checkmarx](http://lp.checkmarx.com/php-code-analysis/) | Get a full PHP static security code analysis and prevent security vulnerabilities | - | - | - | Site unavailable |
| [Codacy](https://www.codacy.com/) | Codacy: Automated Code Review | - | - | - | - |
| [Code Climate](https://codeclimate.com) | Hosted static analysis for Ruby, PHP and JavaScript source code | - | - | - | - |
| [Insight](https://insight.sensiolabs.com/) | A SensioLabs tool to analyzes source code to find problems that degrade the overall quality of your projects | - | - | - | Site unavailable |
| [Laravelshift](https://laravelshift.com/) | the automated way to upgrade Laravel applications. Upgrade Laravel applications all the way from Laravel 4.2 to the latest version of Laravel | - | - | - | - |
| [RIPS](https://www.ripstech.com/) | The superior security software for PHP applications. Source code static analyser for vulnerabilities | - | - | - | - |
| [Scrutinizer](https://scrutinizer-ci.com/) | Improve code quality and find bugs before they hit production with our continuous inspection platform | - | - | - | Site unavailable |
| [SideCI](https://sideci.com/) | CI for automated code review by code analysis | - | - | - | Site unavailable |

##### Misc

| Tool | Description | Stars | Updated | Latest | Links |
|---|---|---:|---|---|---|
| [Composer Require Checker](https://github.com/maglnet/ComposerRequireChecker) | A CLI tool to check whether a specific composer package uses imported symbols that aren't part of its direct composer dependencies | 1,005 | 2026-07-25 | 4.24.0 | [GitHub](https://github.com/maglnet/ComposerRequireChecker)<br>[Packagist](https://packagist.org/packages/maglnet/composer-require-checker) |
| [Coverage Checker](https://github.com/exussum12/coverageChecker) | Allows old code to use new standards | 176 | 2024-06-25 | 1.1.1 | [GitHub](https://github.com/exussum12/coverageChecker)<br>[Packagist](https://packagist.org/packages/exussum12/coverage-checker) |
| [PHP Manipulator](https://github.com/schmittjoh/php-manipulator) | Library for Analyzing and Modifying PHP Source Code | 105 | 2014-09-27 | - | [GitHub](https://github.com/schmittjoh/php-manipulator)<br>[Packagist](https://packagist.org/packages/jms/php-manipulator) |
| [Fixtro](https://github.com/karlosagudo/fixtro) | A QA static analysis code, with a different approach | 23 | 2019-03-02 | 1.0.11 | [GitHub](https://github.com/karlosagudo/fixtro)<br>[Packagist](https://packagist.org/packages/karlosagudo/fixtro) |
| [devbug](http://www.devbug.co.uk/) | Ongoing work on PHP Analysis in Rascal (PHP AiR) | - | - | - | Site unavailable |
| [HHVM](http://hhvm.com/) | Hack Language from Facebook. Add a SCA until version 3.3.8, newer version doesn't have anymore | - | - | - | - |
| [PHPQA](https://edgedesigncz.github.io/phpqa/) | A Wrapper to a lot of PHP tools reported into a single HTML file | - | - | - | - |
