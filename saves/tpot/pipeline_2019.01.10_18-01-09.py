import numpy as np
import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline, make_union
from tpot.builtins import StackingEstimator, ZeroCount

# NOTE: Make sure that the class is labeled 'target' in the data file
tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
features = tpot_data.drop('target', axis=1).values
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'].values, random_state=42)

# Average CV score on the training set was:0.8399518554581846
exported_pipeline = make_pipeline(
    ZeroCount(),
    StackingEstimator(estimator=GradientBoostingClassifier(learning_rate=0.01, max_depth=7, max_features=0.1, min_samples_leaf=7, min_samples_split=4, n_estimators=800, subsample=0.7000000000000001)),
    ExtraTreesClassifier(bootstrap=True, criterion="entropy", max_features=0.45, min_samples_leaf=7, min_samples_split=3, n_estimators=400)
)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)