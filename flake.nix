{
  description = "A collection of random gadgets written in Cairo";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-22.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in {
        packages = rec {
          default = cairogadget;

          cairogadget = pkgs.python3Packages.buildPythonPackage {
            pname = "cairogadget";
            version = "0.1.0";

            src = nixpkgs.lib.cleanSource ./.;

            nativeBuildInputs = with pkgs; [
              gobject-introspection
              gtk3
              wrapGAppsHook

              pylint
              python3Packages.flake8
              python3Packages.mypy
              python3Packages.types-setuptools
            ];

            propagatedBuildInputs = with pkgs; [
              python3Packages.pygobject3
              python3Packages.pycairo
            ];
           };
        };
      }
    );
}
