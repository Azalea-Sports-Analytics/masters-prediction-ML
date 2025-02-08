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
