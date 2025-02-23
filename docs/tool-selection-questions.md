Questions:

1) will the datafile get large enough that we want a separate repository for them?

2) What version of python are we using?

3) what package manage are we using (I normally use `pip`; many projects like this use `conda`)

4) are using `requirement.txt` or `pyproject.toml` for the libraries

5) which test frame works are going to use.

For assertion based testing, I normally use `pytest`

I don't have an relevant with the tools for

* Model Evaluation & Performance Testing

* Data Validation & Consistency Checks

* Model Debugging & Explainability

* Model Reproducibility & Experiment Tracking

* Integration & CI/CD Testing

6) are we going to be using `docker`

7) for typehints, are we using them at all, using them only structurally, using them semantically

8) are we sticking with `pandas` or using something faster & more scaleable

I normally use `pandas.`  `polars` is presumably a lot faster

9) which machine learning library set are we starting with `scikit-learn`



Answers:

1) Not too sure. I have never experienced any issues like this before. Happy to take your advice on this. 

2) 3.13

3) I also normally use pip so lets stick to pip

4) requirements.txt

5) I also usually use  `pytest`

6) I don't have enough experience to answer this. I know one of the aims we discussed was to set up project in Google Collab, Azure ML and AWS to give people looking for jobs exposure to all of these tools. 

7) To be used only structurally.

8) I am more experienced in `pandas`, but I am open to using `polars`. My team at work are looking to switch to polars, so open to using it. 

9) Happy for you to advise on this