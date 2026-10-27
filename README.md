# ScanTot

**ScanTot** is a fast, modular web security scanner for penetration testers,
bug bounty hunters, and security researchers. It performs reconnaissance,
port discovery, header analysis, SSL inspection, and content discovery
in a single, lightweight CLI.

![version](https://img.shields.io/badge/version-3.1.0-blue)
![python](https://img.shields.io/badge/python-3.8%2B-green)
![license](https://img.shields.io/badge/license-MIT-lightgrey)

---

## Features

- **DNS Recon** — A, AAAA, PTR, MX, TXT records
- **Port Scan** — 1000+ common ports, TCP connect scan
- **HTTP Probe** — headers, status, redirect chain, server banner
- **SSL Inspector** — certificate chain, expiry, subject, issuer
- **Security Headers** — CSP, HSTS, X-Frame-Options, X-Content-Type-Options
- **Tech Detection** — CMS, framework, server, language
- **Content Discovery** — common paths (admin, backup, config)
- **Subdomain Enum** — 50+ common prefixes
- **Multi-format Output** — terminal, JSON, HTML report
- **Fast** — async I/O, threaded scanning

## Installation

```bash
pip install scantot
```

Or from source:

```bash
git clone https://github.com/cocovjet03/scantot.git
cd scantot
pip install -e .
```

## Quick Start

```bash
scantot scan https://example.com
scantot scan https://example.com --full
scantot scan https://example.com --ports 1-1000
scantot scan https://example.com --output report.html --format html
```

## Usage

```
scantot scan <url> [options]

Options:
  --full                Run all checks (ports, headers, ssl, tech, paths)
  --ports RANGE         Port range (e.g. 1-1000)
  --timeout SECONDS     Per-request timeout (default: 5)
  --threads N           Worker threads (default: 50)
  --output FILE         Save report to file
  --format FORMAT       Output format: text, json, html
  --silent              Minimal output
  --verbose             Debug output
  --version             Show version
  --help                Show help
```

See [docs/USAGE.md](docs/USAGE.md) for the full reference.

## Examples

```bash
# Quick scan
scantot scan https://target.com

# Full audit
scantot scan https://target.com --full

# Custom port range + HTML output
scantot scan https://target.com --ports 1-65535 --output report.html --format html

# Batch mode
cat targets.txt | scantot scan --stdin
```

## Disclaimer

ScanTot is intended for **authorized security testing only**. You must have
explicit permission to scan any target. The authors are not responsible for
misuse.

## License

MIT © ScanTot Contributors
