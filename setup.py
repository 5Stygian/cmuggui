from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
  name = "cmuggui",
  version = "0.0.7",
  authors = [
    { name="5Stygian", email="rlcrafistohard@gmail.com" },
  ],
  description = "A library for making GUIs in CMU Graphics",
  long-description = long-description,
  keywords = ["cmu graphics", "gui"],
  readme = "README.md",
  requires-python = ">=3.12.1",
  classifiers = [
      "Programming Language :: Python :: 3",
      "Operating System :: OS Independent",
  ],
  license = "CC0-1.0",
  license-files = ["LICEN[CS]E*"]
)
