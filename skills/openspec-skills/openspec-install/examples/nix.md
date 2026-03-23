# Install OpenSpec via nix

## One-time (no global install)

```bash
nix run github:Fission-AI/OpenSpec -- init
```

## Persistent install

```bash
nix profile install github:Fission-AI/OpenSpec
openspec --version
```

## In flake.nix

```nix
{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    openspec.url = "github:Fission-AI/OpenSpec";
  };
  outputs = { nixpkgs, openspec, ... }: {
    devShells.x86_64-linux.default = nixpkgs.legacyPackages.x86_64-linux.mkShell {
      buildInputs = [ openspec.packages.x86_64-linux.default ];
    };
  };
}
```

Then use **openspec-initial** to run `openspec init` in your project.
