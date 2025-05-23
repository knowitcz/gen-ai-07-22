from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

try:
    from packaging.requirements import Requirement
except ModuleNotFoundError:  # pragma: no cover
    Requirement = None

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover
    try:
        import tomli as tomllib
    except ModuleNotFoundError:  # pragma: no cover
        print("Error: tomllib or tomli is required to run this script.")
        exit(1)


def main() -> None:
    pyproject_path = Path(__file__).with_name("pyproject.toml")
    with pyproject_path.open("rb") as pyproject_file:
        project = tomllib.load(pyproject_file)["project"]

    package_names = []
    for dependency in project.get("dependencies", []):
        package_name = dependency
        if Requirement is not None:
            package_name = Requirement(dependency).name
        package_names.append(package_name)

    label_width = max((len(package_name) for package_name in package_names), default=0)

    for package_name in package_names:
        dotted_label = f"Package {package_name} ".ljust(label_width + len("Package  "), ".")

        try:
            package_version = version(package_name)
            print(f"{dotted_label} [OK] (version {package_version})")
        except PackageNotFoundError:
            print(f"{dotted_label} [MISSING]")


if __name__ == "__main__":
    main()