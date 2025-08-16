from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ppt-to-md",
    version="1.0.0",
    author="KiloCode",
    author_email="kilocode@example.com",
    description="一个将PowerPoint文件转换为Markdown格式的工具",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bamboodew/ppt-to-md",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    install_requires=[
        "python-pptx>=0.6.0",
    ],
    entry_points={
        "console_scripts": [
            "ppt-to-md=ppt_to_md.main:main",
        ],
    },
)