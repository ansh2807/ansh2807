# DRAG / visual identity

The public portfolio uses a quiet technical aesthetic: near-black (#0b1014), off-white (#eef2f0), emerald (#70e4b4), and a project-specific accent. Strong, stationary typography is paired with restrained line-art motion.

## Assets

- `assets/brand/cover.gif`: 1200 × 440, seamless four-second loop; no moving text or flashing effects.
- `assets/brand/cover.png`: still alternative. READMEs request it when the viewer prefers reduced motion and also provide a direct link.
- `assets/avatar.jpg`: illustrated portrait created with ImageGen from a user-provided Instagram reference.
- Each project keeps its own covers in `assets/brand/` so it does not depend on another repository or a badge service.

## Regenerate the covers

Use Python 3.10+ with Pillow (`python -m pip install Pillow`). Clone the project repositories alongside this profile repository, then run:

```sh
python tools/generate_brand.py --root ..
```

Add `--only keyforge` (or another repository name) to render one cover. The script uses local Bahnschrift/Consolas on Windows or DejaVu Sans/Mono on Linux. Set `BRAND_FONT` and `BRAND_MONO` to font paths to override. Fonts are not redistributed.

## Voice

Lead with what the tool does. Use concrete capabilities, accurate project status, and short sentences. Do not imply certification, independent security audits, adoption figures, or results that have not been demonstrated.
