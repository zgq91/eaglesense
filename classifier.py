"""

EagleSense interaction classifier (XGBoost wrapper)

===
EagleSense: Tracking People and Devices in Interactive Spaces using Real-Time Top-View Depth-Sensing
Copyright © 2016 Chi-Jui Wu

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

import xgboost as xgb


class TopviewInteractionClassifier(object):
    def __init__(self):
        self.classifier = None

    def load(self, model):
        self.classifier = xgb.Booster(model_file=model)

    def predict(self, X):
        X_dmatrix = xgb.DMatrix(X)
        return self.classifier.predict(X_dmatrix).astype(int)
