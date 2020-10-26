# pete_tpl

A Python binding for [libpetetpl](https://github.com/pete-tpl/libpetetpl).

__The project is under development!__

## Usage

```python
import pete_tpl

engine = pete_tpl.Engine()
result = engine.render(
    "Hello,{# comment #} {{ user }}! Number is {{ some_number }}\nCalculation: {{ 2 * 9 }}\nPercentage: {{ percentage }}%",
    {
        'user': 'John Doe',
        'some_number': 4443,
        'percentage': 23.41234,
    })

print(result)

# Output:
# Hello, John Doe! Number is 4443
# Calculation: 18
# Percentage: 23.41234%
```