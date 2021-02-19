from setuptools import setup

setup(
    name="elyra",
    packages=["elyra"],
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "elyra = elyra.cli:cli",
            "elyra-pipeline = elyra.pipeline.cli:pipeline",
            "elyra-metadata = elyra.metadata.cli:metadata",
        ]
    },
    version="0.0.1",
    description="bloop",
    author="Nick",
)
