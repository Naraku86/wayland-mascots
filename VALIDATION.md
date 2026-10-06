# Review and validation

## Scope

Reviewed the fork's Makefile targets, SVG embedding script, mascot checks, preview renderer and CI changes. Comments, identifiers and diagnostic messages are in English. The C engine is inherited unchanged; this is not a complete security audit of upstream.

The fork uses Python's standard library, compile-time SVG packs and the existing animation engine. No new runtime dependency, plugin framework or animation engine was added. ImageMagick is only used to regenerate documentation GIFs. Mascot names are passed through an environment variable and checked against a fixed allowlist, rather than interpolated into shell code. SVG encoding and parse errors produce readable failures before generated C is written. The preview renderer invokes ImageMagick without a shell and checks exit status.

## Verified locally

- All four packs compiled in release mode on Fedora 44; staged user installation succeeded.
- Engine unit tests and strict validation of `mascot.conf.example` passed.
- `make test-mascots` passed, including a regression check against shell execution through mascot selection.
- Four looping GIFs were generated with seven frames each and visually inspected; both READMEs link to them.
- Documentation links and `git diff --check` passed.

## Remaining limits

`make format-check` could not complete locally because clang-format's shared libraries are unavailable. `make clean && make debug` compiled objects but failed to link because libasan.so.8.0.0 is missing. CI is configured to install dependencies and run format, debug, sanitizer tests and static analysis; those checks are not claimed as passing without CI results.

IPC tests require permission to create local sockets. Nix packaging and every pack in an independent graphical session have not been verified locally. The staged installation did not replace the active desktop mascot.
