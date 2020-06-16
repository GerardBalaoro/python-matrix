# Python Matrix

A simple matrix library for Python 3


## Usage

Initialize a matrix object by passing the number of rows and columns. Rows and columns must be at least 2.

```python
from matrix import Matrix

mat = Matrix(3, 3)

mat.fillRow(0, ['a', 'b', 'c'])
mat.fillRow(1, ['d', 'e', 'f'])
mat.fillRow(2, ['g', 'h', 'i'])

print(mat.getRows())
# [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
```

## Methods

* **get** (`row:int`, `col:int`, `default=None`)
    - Get cell value by row and column
* **set** (`row:int`, `col:int`, `value`)
	- Set cell value by row and column
* **fillRow** (`row:int`, `values:list`)
    * Fill row with specified values
* **fillColumns** (`col:int`, `values:list`)
    * Fill row with specified values
* **getRow** (`row:int`)
    * Get row by index
* **getColumn** (`col:int`)
    * Get column by index
* **getDiagonal** (`row:int`, `col:int`, `forward=False`)
    * Get diagonal values that intersects with `row` and `col`
    * Retrieve forward diagonal values by passing `True` as the third parameter
* **getRows**
    * Get all rows
* **getColumns**
    * Get all columns
* **getDiagonals** (`forward=True`)
    * Get all diagonal values, direction is determined by the `forward` parameter

## Properties

* **numRows** - Total number of rows
* **numColumns** - Total number of columns
