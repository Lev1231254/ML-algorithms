# Project description
Educational machine learning project implementing several classical algorithms from scratch.

The algorithms are implemented from scratch using NumPy only.
No machine learning libraries such as scikit-learn are used for training or prediction.

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


# Installation
## Requirements

- Python 3.10+
- Git

## Windows
### 1. Clone the repository

```powershell
git clone https://github.com/Lev1231254/ML-algorithms.git
cd ML-algorithms
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

```powershell
.venv\Scripts\activate
```

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

### 5. Run the project

```powershell
python LogisticRegressionTestIRIS.py
```
## Linux
### 1. Clone the repository

```bash
git clone https://github.com/Lev1231254/ML-algorithms.git
cd ML-algorithms
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the project

```bash
python3 LogisticRegressionTestIRIS.py
```
