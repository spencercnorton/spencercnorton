<p align="center">
  <a href="https://norvitech.com"><img alt="NorviTech Suite — open-source apps for the Linux desktop and the self-hosted stack" src="https://norvitech.com/assets/banner.svg" width="800"></a>
</p>

<p align="center">
  <a href="https://norvitech.com"><img alt="norvitech.com" src="https://img.shields.io/badge/norvitech.com-FD8024.svg"></a>
  <a href="https://buy.stripe.com/8x26oH2U44f65TRe574wM04"><img alt="Donate" src="https://img.shields.io/badge/donate-Stripe-635bff.svg?logo=stripe&logoColor=white"></a>
</p>

NorviTech is the name Spencer Norton publishes software under: open-source
apps for the Linux desktop and the self-hosted stack. Each one is small, does
one job and ships as a tagged release you can read end to end. No telemetry,
no accounts, no hosted service; each README says exactly what leaves the
machine.

## The suite

| Product | What it is | Install | Licence |
|---|---|---|---|
| **[Helios](https://github.com/spencercnorton/helios)** | The desktop that sees everything your coding agents do. A native GTK4/libadwaita workbench for Claude Code, OpenAI Codex and OpenRouter models on Ubuntu. | APT (Ubuntu 26.04) · source | [MIT](https://github.com/spencercnorton/helios/blob/main/LICENSE) |
| **[BitAgent](https://github.com/spencercnorton/bitagent)** | A self-hosted BitTorrent DHT crawler and indexer built for the \*arr stack. Evidence-driven classification, curation and opt-in LLM stages, with the operator console and public library in the same image. Descended from bitmagnet. | Docker Compose · source | [MIT](https://github.com/spencercnorton/bitagent/blob/main/LICENSE) |
| **[XNote](https://github.com/spencercnorton/xnote)** | Modern GTK4 sticky notes for GNOME. Descended from Xpad, with a colour picker, layout presets and Wayland-safe placement. | from source | [GPL-3.0-or-later](https://github.com/spencercnorton/xnote/blob/main/COPYING) |
| **[XNote Placement](https://github.com/spencercnorton/xnote-placement)** | Puts every XNote sticky note back where you left it. A GNOME Shell extension that restores each note's position, monitor and workspace on Wayland, where the app cannot do it itself. | APT (Ubuntu 26.04) · source | [GPL-3.0-or-later](https://github.com/spencercnorton/xnote-placement/blob/main/LICENSE) |
| **[SnipSnap](https://github.com/spencercnorton/snipsnap)** | Screenshot any region of any monitor on GNOME Wayland, with no permission dialog. A Qt 6 capture-and-annotate tool whose GNOME Shell extension draws the selection inside the compositor. Descended from Flameshot. | APT (Ubuntu 26.04) · source | [GPL-3.0-or-later](https://github.com/spencercnorton/snipsnap/blob/main/LICENSE) |
| **[NorviOS](https://github.com/spencercnorton/norvi-os)** | The NorviTech look for Ubuntu 26.04, from the boot splash to the window glass. A reversible layer over stock Ubuntu and GNOME 50, applied only through the override points Ubuntu provides, so updates keep working and one command puts the original back. | from source | [GPL-3.0-or-later](https://github.com/spencercnorton/norvi-os/blob/main/LICENSE) |

Every README's `Install` section is the install page for that product.
Helios installs from an APT repository on Ubuntu 26.04 ([how](https://github.com/spencercnorton/helios#install)); BitAgent ships as a Docker Compose file; the desktop tools build from source with the
commands CI runs; the extension installs from the same APT repository into GNOME Shell;
NorviOS installs from source with two scripts, one of them per-user, and removes the same way.

## How these repositories work

- **Release mirrors.** Development happens in a private tree; every tagged
  release is exported here through an automated gate that checks the tree for
  anything that should not be public. Pull requests are reviewed here, applied
  to the development tree and ship in the next tag, with your name in the
  release notes.
- **Same shape everywhere.** Every repository has the same README layout, the
  same badge row, an issue chooser, a `SECURITY.md`, a `SUPPORT.md` and a
  `CONTRIBUTING.md`. If you know one, you know them all.
- **No e-mail.** Bugs and ideas go to each repository's issues and
  Discussions; security reports go through GitHub private vulnerability
  reporting. That is deliberate.
- **Forks stay honest.** BitAgent and XNote keep their upstream licences,
  notices and authors; each README says exactly what is upstream's and what
  is new.

## Support the work

If one of these saves you time, you can
[support its development](https://buy.stripe.com/8x26oH2U44f65TRe574wM04).
The whole suite, with links to every product, lives at
[norvitech.com](https://norvitech.com).

---

<p align="center">
  <a href="https://github.com/spencercnorton/helios">Helios</a> ·
  <a href="https://github.com/spencercnorton/bitagent">BitAgent</a> ·
  <a href="https://github.com/spencercnorton/xnote">XNote</a> ·
  <a href="https://github.com/spencercnorton/xnote-placement">XNote Placement</a> ·
  <a href="https://github.com/spencercnorton/snipsnap">SnipSnap</a> ·
  <a href="https://github.com/spencercnorton/norvi-os">NorviOS</a> ·
  <a href="https://norvitech.com">norvitech.com</a>
</p>
