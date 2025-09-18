# Customer Churn Prediction - Telecom (Limited)

The provided dataset has a target column 'Churn Category' which contains only a single class (no variation). Because of this, supervised model training (classification) cannot proceed — models require at least two classes in the target variable.

Value counts: {0: 7043}

What you can do next:
- Verify the dataset and ensure the target column has both classes (e.g., 'Yes'/'No' for churn).
- If you have a cleaned dataset with both classes, replace `data/Telecom_Customer_Churn.csv` with it and run the scripts:
  ```bash
  pip install -r requirements.txt
  python scripts/model_training.py
  ```

Assets generated:
- assets/target_distribution.png

Notes for reviewers: This repository is packaged as a ready-to-run project. Please replace the dataset with a balanced dataset containing both churn classes to train and evaluate models.
