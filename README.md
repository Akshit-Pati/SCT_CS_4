# SCT_CS_4

# Keyboard Event Logger — Ethical / Consent-First Tool

**Short description**  
A small, consent-first keyboard event logger intended solely for authorized testing, debugging, accessibility research, and developer tools. This project *does not* aim to be stealthy or run without a user's knowledge. Use only on devices you own or where you have explicit written permission.

**Important — read before using**  
This tool is designed for **legitimate** uses only. Do **not** use it to capture keystrokes from other people without their informed consent. The author(s) and repository maintainers are not responsible for misuse.

## Use cases
- Visualizing keyboard events during presentations or demos.
- Collecting typing speed and error statistics for research with participant consent.
- Debugging keyboard shortcuts in application development.
- Accessibility testing for assistive technologies.

## Key features
- Shows key events in real time (press/release) while running in the foreground.
- Optionally saves anonymized timing/metrics to a local file **only** when explicitly enabled.
- Clear on-screen indication when logging is active.
- Simple configuration to limit which keys/events are captured.
- Built-in consent notice that must be accepted before any logging begins.

## Security & privacy
- No background/stealth mode — runs only while the program window is active.
- Local-only storage by default; no network transmission.
- Optional anonymization and aggregation modes to avoid storing raw sensitive input.
- Logging must be explicitly enabled by the operator each run (no persistence).

## License & legal
Use this software at your own risk. By using it you confirm you will comply with all applicable laws and obtain necessary permissions from all affected parties. Consider consulting legal counsel for organizational or human-subject testing.

## Getting started
1. Clone the repo.
2. Read and accept the built-in consent/warning on first run.
3. Run the program on a machine you own or where you have explicit permission.
4. Use logging controls in the UI to start/stop data capture.

## Contributing
Contributions are welcome for accessibility features, better anonymization, and improved UX — provided they preserve the consent-first design.

## Alternatives / Related projects
If your goal is education or security research, consider:
- A keyboard **visualizer** (displays keys when pressed for demos).
- A **typing tutor** that measures speed and accuracy with user consent.
- Tools that detect and remove unauthorized keyloggers from a machine (defensive tools).

