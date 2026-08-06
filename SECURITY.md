# Security Policy

## Supported Versions

This project is maintained on the `master` branch. Security fixes are applied
to that branch; older commits and forks are not supported.

This repository publishes a catalog of third-party PHP analysis tools. It does
not distribute or operate those tools. Vulnerabilities in a listed tool or
service should be reported directly to that project's maintainers.

## Reporting a Vulnerability

Please do not disclose suspected vulnerabilities in a public issue,
discussion, pull request, or comment.

Report vulnerabilities in this repository privately to the maintainer using a
contact method listed on the
[@ValentinNikolaev GitHub profile](https://github.com/ValentinNikolaev). If no
private contact method is available, open a public issue asking the maintainer
to contact you, but do not include any sensitive details.

Include as much of the following information as possible:

- the affected file, workflow, generated site page, or URL;
- the type and potential impact of the vulnerability;
- the steps and prerequisites needed to reproduce it;
- a proof of concept, logs, or screenshots with secrets removed;
- any known mitigations or suggested fixes; and
- whether the vulnerability has been disclosed elsewhere.

You should receive an acknowledgment within seven days. After the report is
validated, the maintainer will coordinate remediation and disclosure with you.
Please allow a reasonable amount of time for a fix before publishing details.
Reporter credit will be given unless anonymity is requested.

## Scope

Examples of issues that are in scope include vulnerabilities in:

- the catalog maintenance and site-generation scripts;
- the GitHub Actions workflows;
- the generated GitHub Pages site; and
- repository configuration that could expose secrets or permit unauthorized
  changes.

The following are out of scope:

- vulnerabilities in third-party tools or services listed in the catalog;
- inaccurate or outdated catalog metadata without a security impact;
- reports based only on automated scanner output without a reproducible impact;
- social engineering, denial-of-service testing, or destructive testing; and
- attacks requiring access to another person's account, credentials, or
  private data.

When researching a vulnerability, avoid disrupting the project or accessing,
modifying, or deleting data that does not belong to you.
