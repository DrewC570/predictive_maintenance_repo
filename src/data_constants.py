import pandas as pd
from joblib import dump
from sklearn.linear_model import LogisticRegression

errors_df = pd.read_csv('../data/PdM_errors.csv')
failures_df = pd.read_csv('../data/PdM_failures.csv')
machines_df = pd.read_csv('../data/PdM_machines.csv')
maintenance_df = pd.read_csv('../data/PdM_maint.csv')
telemetry_df = pd.read_csv('../data/PdM_telemetry.csv')
master_df = pd.read_csv('../data/master_df.csv')
master_df_cleaned = pd.read_csv('../data/master_df_cleaned.csv')
errors_dummy_df = pd.read_csv('../data/errors_dummy_df.csv')
models_dummy_df = pd.read_csv('../data/models_dummy_df.csv')


if __name__ == '__main__':
    regression_df = master_df_cleaned.join(errors_dummy_df, how = 'left', rsuffix= 'errors')
    regression_df = regression_df.join(models_dummy_df, how = 'left', rsuffix= 'model')
    X = regression_df[['volt','rotate', 'pressure', 'vibration', 'age',
                            'error_error1', 'error_error2', 'error_error3', 'error_error4', 'error_error5', 'error_nan'
                            , 'model_model1', 'model_model2', 'model_model3', 'model_model4'
                        ]]
    y = regression_df['future_fail']
    model_regression = LogisticRegression(max_iter= 1000).fit(X, y)
    with open("../artifacts/model_regression.joblib", "wb") as f:
        dump(model_regression, f, protocol=5)