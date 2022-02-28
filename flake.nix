{
  description = "A collection of random gadgets written in Cairo";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-21.11";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in rec {
        packages = flake-utils.lib.flattenTree {
          cairogadget = pkgs.python3Packages.buildPythonPackage {
            pname = "cairogadget";
            version = "0.1.0";
            src = nixpkgs.lib.cleanSource ./.;
            nativeBuildInputs = [
              pkgs.gobject-introspection
              pkgs.gtk3
              pkgs.wrapGAppsHook
            ];
            propagatedBuildInputs = [
              pkgs.python3Packages.pygobject3
              pkgs.python3Packages.pycairo
            ];
           };
        };
        defaultPackage = packages.cairogadget;
      });
}
