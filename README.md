# Project description
Educational machine learning project implementing several classical algorithms from scratch.

The algorithms are implemented from scratch using NumPy only.
No machine learning libraries such as scikit-learn are used for training or prediction.

Implemented:
- Linear Regression
- Logistic Regression
- KNN


# Installation
## Requirements

- Python 3.10+
- Git

## Windows (Powershell)

```powershell
git clone https://github.com/Lev1231254/ML-algorithms.git
cd ML-algorithms
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python LogisticRegressionTestIRIS.py
```

## Linux (Bash)

```bash
git clone https://github.com/Lev1231254/ML-algorithms.git
cd ML-algorithms
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 LogisticRegressionTestIRIS.py
```

## After running the example a window with graphs describing a Logistic Regression model should appear:
<img width="1536" height="852" alt="logitstic regression figure whaterver" src="https://github.com/user-attachments/assets/eccb11f0-7de8-4297-af45-2895a4ee560d" />


# Details
### Linear Regression
Example: 
```
LinearRegressionTestIRIS.py
```
Implemented 
- Gradient Descent
- L1 and L2 Regularization
- Validation loss
- Visualization
  
### Logistic Regression
Example: 
```
LogisticRegressionTestIRIS.py
```
Implemented
- Gradient Descent
- Decision boundary
- Probability heatmap

### K-nearest neighbours
Example: 
```
KNNTestIRIS.py
KNNTestIRIS.ipynb
```
Implemented
- Algorithm
- Search for best K (see KNNTestIRIS.ipynb)

### API:
**Regression classes:**
- LinearRegressionFromScratch.*LinearRegressionModel(self, lr, epochs, batch_size, L1_potency, L2_potency)*
  - .fit(...)
  - .predict(...)
  - .paint_data(...)
- LogisticRegressionFromScratch.*LogisticRegressionModel(self, lr, batch_size, epochs, ridge_rate)*
  - .fit(...)
  - .calculate_probs(...)

**KNN function:**
- KNNFromScratch.*knn_predict(k : int, target_coordinates : list[int], data : np.array, labels : np.array)*
