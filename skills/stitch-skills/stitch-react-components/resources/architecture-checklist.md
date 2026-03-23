# Architecture Quality Gate

## Structural integrity
- [ ] Logic in custom hooks under `src/hooks/`.
- [ ] Modular components; no single monolithic file.
- [ ] Static text, image URLs, lists in `src/data/mockData.ts`.

## Type safety and syntax
- [ ] Props use `Readonly<ComponentNameProps>`.
- [ ] Valid TypeScript; no placeholders (e.g. `StitchComponent` replaced with real name).

## Styling and theming
- [ ] Dark mode (`dark:`) where applicable.
- [ ] Theme-mapped Tailwind classes; avoid hardcoded hex.
