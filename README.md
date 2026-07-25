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

* [jscpd](https://github.com/kucherenko/jscpd) - Copy/paste detector for programming source code, supports 223 formats. AI-ready with token-efficient reporter, skill and MCP server. (5,932 stars; updated 2026-07-24; [repo](https://github.com/kucherenko/jscpd))
* [mago](http://mago.carthage.software/) - Mago is a toolchain for PHP that aims to provide a set of tools to help developers write better code. (3,329 stars; updated 2026-07-25; latest 1.45.0; [repo](https://github.com/carthage-software/mago); [packagist](https://packagist.org/packages/carthage-software/mago))
* [Pfff](https://github.com/facebook/pfff) - Tools for code analysis, visualizations, or style-preserving source transformation. (2,440 stars; updated 2019-03-27; [repo](https://github.com/facebookarchive/pfff))
* [Phan](https://github.com/etsy/phan) - Phan is a static analyzer for PHP. Phan prefers to avoid false-positives and attempts to prove incorrectness rather than correctness. (5,619 stars; updated 2026-07-20; latest 6.0.7; [repo](https://github.com/phan/phan); [packagist](https://packagist.org/packages/phan/phan))
* [PHP Magic Number Detector](https://github.com/povils/phpmnd) - PHP Magic Number Detector (585 stars; updated 2026-02-25; latest v3.6.1; [repo](https://github.com/povils/phpmnd); [packagist](https://packagist.org/packages/povils/phpmnd))
* [PHP Mess Detector](https://phpmd.org) - PHPMD is a spin-off project of PHP Depend and aims to be a PHP equivalent of the well known Java tool PMD. PHPMD can be seen as an user friendly frontend application for the raw metrics stream measured by PHP Depend. (2,443 stars; updated 2026-06-29; latest 2.15.0; [repo](https://github.com/phpmd/phpmd); [packagist](https://packagist.org/packages/phpmd/phpmd))
* [PHP Stan](https://github.com/phpstan/phpstan) - PHP Static Analysis Tool - discover bugs in your code without running it! (14,042 stars; updated 2026-07-25; latest 2.2.5; [repo](https://github.com/phpstan/phpstan); [packagist](https://packagist.org/packages/phpstan/phpstan))
* [PHPCPD](https://github.com/sebastianbergmann/phpcpd) - Copy/Paste Detector (CPD) for PHP code. (2,211 stars; updated 2023-01-10; latest v1.2; [repo](https://github.com/sebastianbergmann/phpcpd); [packagist](https://packagist.org/packages/phpcpd-next/phpcpd))
* [psalm](https://psalm.dev) - A PHP static analysis tool for finding errors and security vulnerabilities in PHP applications (5,869 stars; updated 2026-07-13; latest 6.16.1; [repo](https://github.com/vimeo/psalm); [packagist](https://packagist.org/packages/vimeo/psalm))

##### Coding standards

* [EasyCodingStandard](https://github.com/Symplify/EasyCodingStandard) - ECS runs PHP-CS-Fixer and PHP_CodeSniffer as a single, parallel fast tool with zero dependencies. Run on PHP 7.2+ (1,618 stars; updated 2026-07-22; [repo](https://github.com/ecsphp/ecs))
* [PHP Code Sniffer](https://github.com/squizlabs/PHP_CodeSniffer) - PHP_CodeSniffer tokenizes PHP files and detects violations of a defined set of coding standards. (10,774 stars; updated 2024-04-01; latest 4.0.1; [repo](https://github.com/squizlabs/PHP_CodeSniffer); [packagist](https://packagist.org/packages/squizlabs/php_codesniffer))

##### DIY

* [PHP Parser](https://github.com/nikic/PHP-Parser) - A PHP parser written in PHP (17,452 stars; updated 2026-07-11; latest v5.8.0; [repo](https://github.com/nikic/PHP-Parser); [packagist](https://packagist.org/packages/nikic/php-parser))

##### Fixers

* [PHP CS Fixer](https://github.com/FriendsOfPHP/PHP-CS-Fixer) - A tool to automatically fix PHP Coding Standards issues (13,547 stars; updated 2026-07-24; latest v3.88.2; [repo](https://github.com/PHP-CS-Fixer/PHP-CS-Fixer); [packagist](https://packagist.org/packages/composer-phar/php-cs-fixer))
* [Rector](https://github.com/rectorphp/rector) - Instant Upgrades and Automated Refactoring of any PHP 5.3+ code (10,380 stars; updated 2026-07-25; latest 2.5.7; [repo](https://github.com/rectorphp/rector); [packagist](https://packagist.org/packages/rector/rector))

##### Metrics

* [churn-php](https://github.com/bmitch/churn-php) - Discover files in need of refactoring. (1,376 stars; updated 2025-12-31; latest 1.7.3; [repo](https://github.com/bmitch/churn-php); [packagist](https://packagist.org/packages/bmitch/churn-php))
* [dePHPend](https://github.com/mihaeu/dephpend) - Detect flaws in your architecture, before they drag you down into the depths of dependency hell ... (533 stars; updated 2026-01-28; [repo](https://github.com/mihaeu/dephpend); [packagist](https://packagist.org/packages/mihaeu/dephpend-tests))
* [PHP Metrics](https://github.com/Halleck45/PhpMetrics) - Beautiful and understandable static analysis tool for PHP (2,602 stars; updated 2026-07-22; latest 2.10.0; [repo](https://github.com/phpmetrics/PhpMetrics); [packagist](https://packagist.org/packages/phpmetrics/phpmetrics))
* [PHP Semantic Versioning Checker](https://github.com/tomzx/php-semver-checker) - Compares two source sets and determines the appropriate semantic versioning to apply. (436 stars; updated 2026-02-05; latest v0.17.0; [repo](https://github.com/tomzx/php-semver-checker); [packagist](https://packagist.org/packages/tomzx/php-semver-checker))
* [PhpDependencyAnalysis](https://github.com/mamuz/PhpDependencyAnalysis) - Static code analysis to find violations in a dependency graph (575 stars; updated 2023-12-03; latest v2.0.2; [repo](https://github.com/mamuz/PhpDependencyAnalysis); [packagist](https://packagist.org/packages/agratushniy/php-dependency-analysis))
* [PHPLOC](https://github.com/sebastianbergmann/phploc) - A tool for quickly measuring the size of a PHP project. (2,344 stars; updated 2025-04-12; latest 7.0.2; [repo](https://github.com/sebastianbergmann/phploc); [packagist](https://packagist.org/packages/phploc/phploc))

##### Misc

* [Composer Require Checker](https://github.com/maglnet/ComposerRequireChecker) - A CLI tool to check whether a specific composer package uses imported symbols that aren't part of its direct composer dependencies (1,005 stars; updated 2026-07-25; latest 4.24.0; [repo](https://github.com/maglnet/ComposerRequireChecker); [packagist](https://packagist.org/packages/maglnet/composer-require-checker))
* [Coverage Checker](https://github.com/exussum12/coverageChecker) - Allows old code to use new standards (176 stars; updated 2024-06-25; latest 1.1.1; [repo](https://github.com/exussum12/coverageChecker); [packagist](https://packagist.org/packages/exussum12/coverage-checker))

### Whole list

##### Bugs finders

* [Exakat](http://www.exakat.io/) - Smart static analysis
* [jscpd](https://github.com/kucherenko/jscpd) - Copy/paste detector for programming source code, supports 223 formats. AI-ready with token-efficient reporter, skill and MCP server. (5,932 stars; updated 2026-07-24; [repo](https://github.com/kucherenko/jscpd))
* [mago](http://mago.carthage.software/) - Mago is a toolchain for PHP that aims to provide a set of tools to help developers write better code. (3,329 stars; updated 2026-07-25; latest 1.45.0; [repo](https://github.com/carthage-software/mago); [packagist](https://packagist.org/packages/carthage-software/mago))
* [Pfff](https://github.com/facebook/pfff) - Tools for code analysis, visualizations, or style-preserving source transformation. (2,440 stars; updated 2019-03-27; [repo](https://github.com/facebookarchive/pfff))
* [Phan](https://github.com/etsy/phan) - Phan is a static analyzer for PHP. Phan prefers to avoid false-positives and attempts to prove incorrectness rather than correctness. (5,619 stars; updated 2026-07-20; latest 6.0.7; [repo](https://github.com/phan/phan); [packagist](https://packagist.org/packages/phan/phan))
* [PHP Analysis](https://github.com/cwi-swat/php-analysis) - PHP language analyses in Rascal (29 stars; updated 2026-05-13; [repo](https://github.com/cwi-swat/php-analysis))
* [PHP Assumption](https://github.com/rskuipers/php-assumptions.git) - Tool to detect assumptions (164 stars; updated 2025-03-22; latest 0.9.1; [repo](https://github.com/rskuipers/php-assumptions); [packagist](https://packagist.org/packages/rskuipers/php-assumptions))
* [PHP Inspection](https://plugins.jetbrains.com/plugin/7622?pr=idea) - Static analysis plugin for PHPStorm
* [PHP Magic Number Detector](https://github.com/povils/phpmnd) - PHP Magic Number Detector (585 stars; updated 2026-02-25; latest v3.6.1; [repo](https://github.com/povils/phpmnd); [packagist](https://packagist.org/packages/povils/phpmnd))
* [PHP Mess Detector](https://phpmd.org) - PHPMD is a spin-off project of PHP Depend and aims to be a PHP equivalent of the well known Java tool PMD. PHPMD can be seen as an user friendly frontend application for the raw metrics stream measured by PHP Depend. (2,443 stars; updated 2026-06-29; latest 2.15.0; [repo](https://github.com/phpmd/phpmd); [packagist](https://packagist.org/packages/phpmd/phpmd))
* [PHP SA](https://github.com/ovr/phpsa) - Smart/Static Analyzer(sis) for PHP :bowtie::neckbeard: (635 stars; updated 2019-02-27; latest 0.6.2; [repo](https://github.com/ovr/phpsa); [packagist](https://packagist.org/packages/ovr/phpsa))
* [PHP Stan](https://github.com/phpstan/phpstan) - PHP Static Analysis Tool - discover bugs in your code without running it! (14,042 stars; updated 2026-07-25; latest 2.2.5; [repo](https://github.com/phpstan/phpstan); [packagist](https://packagist.org/packages/phpstan/phpstan))
* [PHP testability](https://github.com/edsonmedina/php_testability) - Analyses and reports testability issues of a php codebase (130 stars; updated 2022-01-27; [repo](https://github.com/edsonmedina/php_testability); [packagist](https://packagist.org/packages/edsonmedina/php_testability))
* [PHP-malware-finder](https://github.com/nbs-system/php-malware-finder) - Detect potentially malicious PHP files (342 stars; updated 2022-02-22; [repo](https://github.com/nbs-system/php-malware-finder))
* [PHP-Parallel-Lint](https://github.com/JakubOnderka/PHP-Parallel-Lint) - This tool check syntax of PHP files faster than serial check with fancier output. (641 stars; updated 2021-03-13; latest v1.0.0; [repo](https://github.com/JakubOnderka/PHP-Parallel-Lint); [packagist](https://packagist.org/packages/jakub-onderka/php-parallel-lint))
* [php7mar](https://github.com/Alexia/php7mar) - PHP 7 Migration Assistant Report (MAR) (783 stars; updated 2019-05-28; latest v0.2.0-beta; [repo](https://github.com/Alexia/php7mar); [packagist](https://packagist.org/packages/alexia/php7mar))
* [PhpCodeAnalyzer](https://github.com/wapmorgan/PhpCodeAnalyzer.git) - Really, it's "php extensions usage analyzer". It scans codebase and analyzes which non-built-in php extensions used (96 stars; updated 2023-01-17; [repo](https://github.com/wapmorgan/PhpCodeAnalyzer))
* [PHPCodeFixer](https://github.com/wapmorgan/PhpCodeFixer) - Analyzer of PHP code to search issues with deprecated functionality in newer interpreter versions. (367 stars; updated 2024-02-14; [repo](https://github.com/wapmorgan/PhpDeprecationDetector))
* [PHPCPD](https://github.com/sebastianbergmann/phpcpd) - Copy/Paste Detector (CPD) for PHP code. (2,211 stars; updated 2023-01-10; latest v1.2; [repo](https://github.com/sebastianbergmann/phpcpd); [packagist](https://packagist.org/packages/phpcpd-next/phpcpd))
* [psalm](https://psalm.dev) - A PHP static analysis tool for finding errors and security vulnerabilities in PHP applications (5,869 stars; updated 2026-07-13; latest 6.16.1; [repo](https://github.com/vimeo/psalm); [packagist](https://packagist.org/packages/vimeo/psalm))
* [psecio:parse](https://github.com/psecio/parse.git) - Parse: A Static Security Scanner (381 stars; updated 2018-08-07; latest 0.8; [repo](https://github.com/psecio/parse); [packagist](https://packagist.org/packages/psecio/parse))
* [SonarQube](http://www.sonarqube.org/) - An open platform to manage code quality. It covers PHP code

##### Coding standards

* [EasyCodingStandard](https://github.com/Symplify/EasyCodingStandard) - ECS runs PHP-CS-Fixer and PHP_CodeSniffer as a single, parallel fast tool with zero dependencies. Run on PHP 7.2+ (1,618 stars; updated 2026-07-22; [repo](https://github.com/ecsphp/ecs))
* [Pahout](https://github.com/wata727/pahout) - A pair programming partner for writing better PHP. Pahout means PHP mahout :elephant: (48 stars; updated 2020-06-26; latest 0.7.0; [repo](https://github.com/wata727/pahout); [packagist](https://packagist.org/packages/wata727/pahout))
* [PHP Code Sniffer](https://github.com/squizlabs/PHP_CodeSniffer) - PHP_CodeSniffer tokenizes PHP files and detects violations of a defined set of coding standards. (10,774 stars; updated 2024-04-01; latest 4.0.1; [repo](https://github.com/squizlabs/PHP_CodeSniffer); [packagist](https://packagist.org/packages/squizlabs/php_codesniffer))
* [PHP formatter](https://github.com/mmoreram/php-formatter) - PHP Formatter is a PHP developer friendly set of tools (168 stars; updated 2021-06-24; latest v1.3.3; [repo](https://github.com/mmoreram/php-formatter); [packagist](https://packagist.org/packages/mmoreram/php-formatter))

##### DIY

* [Better Reflection](https://github.com/Roave/BetterReflection) - :crystal_ball: Better Reflection is a reflection API that aims to improve and provide more features than PHP's built-in reflection API. (1,245 stars; updated 2026-07-25; latest 6.72.0; [repo](https://github.com/Roave/BetterReflection); [packagist](https://packagist.org/packages/roave/better-reflection))
* [Deptrac](https://github.com/sensiolabs-de/deptrac.git) - Keep your architecture clean. (2,979 stars; updated 2026-07-23; latest 4.7.1; [repo](https://github.com/deptrac/deptrac); [packagist](https://packagist.org/packages/deptrac/deptrac))
* [PHP Parser](https://github.com/nikic/PHP-Parser) - A PHP parser written in PHP (17,452 stars; updated 2026-07-11; latest v5.8.0; [repo](https://github.com/nikic/PHP-Parser); [packagist](https://packagist.org/packages/nikic/php-parser))
* [PHP-cfg](https://github.com/ircmaxell/php-cfg) - A Control Flow Graph implementation in PHP (247 stars; updated 2026-07-11; latest V0.8.1; [repo](https://github.com/ircmaxell/php-cfg); [packagist](https://packagist.org/packages/ircmaxell/php-cfg))
* [Reflection](https://github.com/phpDocumentor/Reflection.git) - Reflection library to do Static Analysis for PHP Projects (125 stars; updated 2026-07-06; latest 7.0.0; [repo](https://github.com/phpDocumentor/Reflection); [packagist](https://packagist.org/packages/phpdocumentor/reflection))

##### Fixers

* [FunctionFQNReplacer](https://github.com/Roave/FunctionFQNReplacer) - provides a way to replace relative references of functions in function calls with absolute references (158 stars; updated 2017-07-05; [repo](https://github.com/Roave/FunctionFQNReplacer))
* [PHP BackSlasher](https://github.com/nilportugues/php-backslasher) - [Git hook] Tool to add all PHP internal functions and constants to its namespace by adding backslash to them. (88 stars; updated 2020-04-21; latest 1.1.4; [repo](https://github.com/nilportugues/php-backslasher); [packagist](https://packagist.org/packages/nilportugues/php_backslasher))
* [PHP CS Fixer](https://github.com/FriendsOfPHP/PHP-CS-Fixer) - A tool to automatically fix PHP Coding Standards issues (13,547 stars; updated 2026-07-24; latest v3.88.2; [repo](https://github.com/PHP-CS-Fixer/PHP-CS-Fixer); [packagist](https://packagist.org/packages/composer-phar/php-cs-fixer))
* [PHP Weaver](https://github.com/troelskn/phpweaver) - A combined runtime/static code-analysis tool, that can trace parameter types (85 stars; updated 2026-01-28; [repo](https://github.com/troelskn/phpweaver))
* [php-refactoring-browser](https://github.com/QafooLabs/php-refactoring-browser) - A command line refactoring tool for PHP (548 stars; updated 2017-11-15; latest v0.1; [repo](https://github.com/QafooLabs/php-refactoring-browser); [packagist](https://packagist.org/packages/qafoolabs/php-refactoring-browser))
* [phpdoc to typehint](https://github.com/dunglas/phpdoc-to-typehint) - Add scalar type hints and return types to existing PHP projects using PHPDoc annotations (225 stars; updated 2020-12-28; latest v0.1.0; [repo](https://github.com/dunglas/phpdoc-to-typehint); [packagist](https://packagist.org/packages/dunglas/phpdoc-to-typehint))
* [Rector](https://github.com/rectorphp/rector) - Instant Upgrades and Automated Refactoring of any PHP 5.3+ code (10,380 stars; updated 2026-07-25; latest 2.5.7; [repo](https://github.com/rectorphp/rector); [packagist](https://packagist.org/packages/rector/rector))
* [Transphpile](https://github.com/jaytaph/Transphpile) - PHP 7 to PHP 5.6 Transpiler (178 stars; updated 2017-09-02; [repo](https://github.com/jaytaph/Transphpile))

##### Metrics

* [churn-php](https://github.com/bmitch/churn-php) - Discover files in need of refactoring. (1,376 stars; updated 2025-12-31; latest 1.7.3; [repo](https://github.com/bmitch/churn-php); [packagist](https://packagist.org/packages/bmitch/churn-php))
* [dePHPend](https://github.com/mihaeu/dephpend) - Detect flaws in your architecture, before they drag you down into the depths of dependency hell ... (533 stars; updated 2026-01-28; [repo](https://github.com/mihaeu/dephpend); [packagist](https://packagist.org/packages/mihaeu/dephpend-tests))
* [PHP Metrics](https://github.com/Halleck45/PhpMetrics) - Beautiful and understandable static analysis tool for PHP (2,602 stars; updated 2026-07-22; latest 2.10.0; [repo](https://github.com/phpmetrics/PhpMetrics); [packagist](https://packagist.org/packages/phpmetrics/phpmetrics))
* [PHP Semantic Versioning Checker](https://github.com/tomzx/php-semver-checker) - Compares two source sets and determines the appropriate semantic versioning to apply. (436 stars; updated 2026-02-05; latest v0.17.0; [repo](https://github.com/tomzx/php-semver-checker); [packagist](https://packagist.org/packages/tomzx/php-semver-checker))
* [PhpDependencyAnalysis](https://github.com/mamuz/PhpDependencyAnalysis) - Static code analysis to find violations in a dependency graph (575 stars; updated 2023-12-03; latest v2.0.2; [repo](https://github.com/mamuz/PhpDependencyAnalysis); [packagist](https://packagist.org/packages/agratushniy/php-dependency-analysis))
* [PHPLOC](https://github.com/sebastianbergmann/phploc) - A tool for quickly measuring the size of a PHP project. (2,344 stars; updated 2025-04-12; latest 7.0.2; [repo](https://github.com/sebastianbergmann/phploc); [packagist](https://packagist.org/packages/phploc/phploc))
* [Quality Analyzer](https://github.com/Qafoo/QualityAnalyzer.git) - Tool helping us to analyze software projects (490 stars; updated 2019-12-06; [repo](https://github.com/Qafoo/QualityAnalyzer); [packagist](https://packagist.org/packages/qafoo/quality-analyzer))

##### SaaS

* [Bliss](https://blissai.com/index.html) - Automatically reviews code in real-time and shows how much it's worth in lines of code
* [Checkmarx](http://lp.checkmarx.com/php-code-analysis/) - Get a full PHP static security code analysis and prevent security vulnerabilities (site unavailable)
* [Codacy](https://www.codacy.com/) - Codacy: Automated Code Review
* [Code Climate](https://codeclimate.com) - Hosted static analysis for Ruby, PHP and JavaScript source code
* [Insight](https://insight.sensiolabs.com/) - A SensioLabs tool to analyzes source code to find problems that degrade the overall quality of your projects (site unavailable)
* [Laravelshift](https://laravelshift.com/) - the automated way to upgrade Laravel applications. Upgrade Laravel applications all the way from Laravel 4.2 to the latest version of Laravel
* [RIPS](https://www.ripstech.com/) - The superior security software for PHP applications. Source code static analyser for vulnerabilities
* [Scrutinizer](https://scrutinizer-ci.com/) - Improve code quality and find bugs before they hit production with our continuous inspection platform (site unavailable)
* [SideCI](https://sideci.com/) - CI for automated code review by code analysis (site unavailable)

##### Misc

* [Composer Require Checker](https://github.com/maglnet/ComposerRequireChecker) - A CLI tool to check whether a specific composer package uses imported symbols that aren't part of its direct composer dependencies (1,005 stars; updated 2026-07-25; latest 4.24.0; [repo](https://github.com/maglnet/ComposerRequireChecker); [packagist](https://packagist.org/packages/maglnet/composer-require-checker))
* [Coverage Checker](https://github.com/exussum12/coverageChecker) - Allows old code to use new standards (176 stars; updated 2024-06-25; latest 1.1.1; [repo](https://github.com/exussum12/coverageChecker); [packagist](https://packagist.org/packages/exussum12/coverage-checker))
* [devbug](http://www.devbug.co.uk/) - Ongoing work on PHP Analysis in Rascal (PHP AiR) (site unavailable)
* [Fixtro](https://github.com/karlosagudo/fixtro) - A QA static analysis code, with a different approach (23 stars; updated 2019-03-02; latest 1.0.11; [repo](https://github.com/karlosagudo/fixtro); [packagist](https://packagist.org/packages/karlosagudo/fixtro))
* [HHVM](http://hhvm.com/) - Hack Language from Facebook. Add a SCA until version 3.3.8, newer version doesn't have anymore
* [PHP Manipulator](https://github.com/schmittjoh/php-manipulator) - Library for Analyzing and Modifying PHP Source Code (105 stars; updated 2014-09-27; [repo](https://github.com/schmittjoh/php-manipulator); [packagist](https://packagist.org/packages/jms/php-manipulator))
* [PHPQA](https://edgedesigncz.github.io/phpqa/) - A Wrapper to a lot of PHP tools reported into a single HTML file
