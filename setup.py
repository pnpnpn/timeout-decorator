"""Setup script for timeoutd."""
import setuptools

if __name__ == "__main__":
    setuptools.setup(
        package_data={"timeoutd": ["py.typed"]},
    )
