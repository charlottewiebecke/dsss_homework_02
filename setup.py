from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    packages=find_packages(),
    install_requires=[], 
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:math_quiz',  
        ],
    },
    author="dsss_team",
    description="A math quiz game",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/charlottewiebecke/dsss_homework_02.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
