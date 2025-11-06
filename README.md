# Decision Trees, Random Forests and SVMs

A tabular classification study using custom decision-tree/random-forest implementations and scikit-learn SVM baselines on Titanic data.

Maintained by [Ahmed Jawed](https://github.com/ahmedjawedaj).

## Methods and engineering work

- Data cleaning and categorical feature preparation.
- Split criteria and recursive decision-tree construction.
- Bootstrap samples and custom random-forest aggregation.
- Kernel/C comparisons with SVC and comparative classification evaluation.

## Repository contents

- [`titanic_classification.ipynb`](notebooks/titanic_classification.ipynb)
- [`data/README.md`](data/README.md): required external inputs and data handling.
- [`PROVENANCE.md`](PROVENANCE.md): original source-date evidence, attribution and publication changes.
- [`scripts/validate_sources.py`](scripts/validate_sources.py): notebook/Python syntax and exclusion checks.

## Recorded observations

- The original notebook has 33 executed code cells and no saved exception outputs.
- This publication does not promote the exploratory split into a generalization or competition claim.

## Setup and use

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cd notebooks
jupyter lab
```

Select the intended kernel and run the notebook top to bottom after providing its required inputs. GPU notebooks can consume substantial runtime; validation below does not start training.

## Data and weights

Place an authorized Titanic training CSV at notebooks/titanic.csv before running. The notebook expects the customary Survived, Pclass, Sex, Age, SibSp, Parch, Fare and Embarked fields. No passenger rows are committed.

## Validation

```bash
python -m pip install -r requirements-validation.txt
python scripts/validate_sources.py
```

The publication checks validate notebook structure and compile source cells/Python modules. They do not reproduce training, GPU timing or ROS hardware behaviour. Cleaned notebooks have no captured outputs or stale execution counters.

## Scope and limitations

- Educational implementation and small-dataset evaluation.
- Dataset redistribution rights are not assumed.
- Publication checks validate source structure, not a new model-training run.

## References and attribution

- [Titanic dataset source](https://www.kaggle.com/competitions/titanic/data)

See PROVENANCE.md for the distinction between original work dates and actual publication dates. This repository excludes instructor handouts, raw data, model weights and private records.
