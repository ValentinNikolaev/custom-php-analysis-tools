# Static analysis tools for PHP

Based on https://github.com/exakat/php-static-analysis-tools

A list of static analysis tools for PHP. Without not-popular or old tools.

### Bugs finders

* [Psalm](https://getpsalm.org/) - Vimeo анализатор кода. Ошибки,phpdoc. Выглядит весьма прилично
* [Phan](https://github.com/etsy/phan) - The static analyzer by Rasmus, PHP Creator. Анализирует разные штуки, в т.ч. аннотации. Не понимает переопределение аннотаций родительских классов в дочерних. Сильный проект.
* [PHP SA](https://github.com/ovr/phpsa) - A development tool aimed at bringing complex analysis for PHP applications and libraries. Проверяет синтаксические ошибки, phpdoc, алиасы, пропущенные свойства
и т.д. Не работает с php-parser 4ой версии.     
* [PHP Stan](https://github.com/phpstan/phpstan) - Focuses on finding errors in code without actually running it.
* [PHPCodeFixer](https://github.com/wapmorgan/PhpCodeFixer) -  Finds usage of deprecated functions, variables and ini directives. Использовать при переезде на новую версию PHP
* [PHPCPD](https://github.com/sebastianbergmann/phpcpd) - Spots copy/pasted code, and help enforcing DRY rule.
* [PHP Magic Number Detector](https://github.com/povils/phpmnd) - Ищет куски кода, где вместо констант с числами используются числа.
* [PHP Mess Detector](http://phpmd.org/) - Находит проблемы с Cyclomatic и NPath complexity, дает рекомендации по улучшению кода

## Coding standards
* [PHP Code Sniffer](https://github.com/squizlabs/PHP_CodeSniffer) - PHPCS checks the code for a large range of coding standard.
 [EasyCodingStandard](https://github.com/Symplify/EasyCodingStandard) - An easy to use tool, that allows to use CodeSniffer and PHP-CS-Fixer in simple way.
 
## DIY
* [Better Reflection](https://github.com/Roave/BetterReflection) - Reflection library with additional features such as parsing docblock type hints, uses nikic's PHP Parser under the hood. 

## Fixers
* [PHP CS Fixer](https://github.com/FriendsOfPHP/PHP-CS-Fixer) - Analyzes and tries to fix coding standards issues (PSR-1 and PSR-2 compatible).

## Metrics
* [Quality Analyzer](https://github.com/Qafoo/QualityAnalyzer.git) - Quality Analyzer is a tool to visualize metrics and source code. Включает в себя следующие анализаторы: source, coverage, pdepend, dependencies, phpmd, checkstyle, tests, cpd, phploc, git,gitDetailed
* [churn-php](https://github.com/bmitch/churn-php) - Helps discover good candidates for refactoring [score = SUM(commits) & (cyclomatic complexity) ]
* [PHPLOC](https://github.com/sebastianbergmann/phploc) - Utility to measures PHP application size and count various structures.
* [PHP Metrics](https://github.com/Halleck45/PhpMetrics) - Calculates all sorts of metrics, and display them in a gorgeous interface. 
* [PhpDependencyAnalysis](https://github.com/mamuz/PhpDependencyAnalysis) - Static code analysis to provide and verify a dependency graph against a defined architecture.
* [dePHPend](https://github.com/mihaeu/dephpend) - dePHPend helps analyze dependencies & architecture and allows you to define constraints for both.

# Misc

* [devbug](http://www.devbug.co.uk/) - Ongoing work on PHP Analysis in Rascal (PHP AiR).
* [HHVM](http://hhvm.com/) - Hack Language from Facebook. Add a SCA until version 3.3.8, newer version doesn't have anymore.
* [PHP Manipulator](https://github.com/schmittjoh/php-manipulator) - A library for analysing and modifying PHP Source Code.
* [PHP Parser](https://github.com/glayzzle/php-parser) - A NodeJS library for parsing PHP and extracting tokens and AST.
* [PHPQA](https://edgedesigncz.github.io/phpqa/) - A Wrapper to a lot of PHP tools reported into a single HTML file.
* [Fixtro](https://github.com/karlosagudo/fixtro) - A wrapper that allow to run in each precommit. It install itself all the dependencies for the runners with a lot of them (phpunit, phpmd, php-cs-fixer, etc..)
* [Coverage Checker](https://github.com/exussum12/coverageChecker) - A tool which allows some of the tools here to be enforced on changed code only. Good for moving towards new standards
* [Composer Require Checker](https://github.com/maglnet/ComposerRequireChecker) - A CLI tool to check whether a specific composer package uses imported symbols that aren't part of its direct composer dependencies
