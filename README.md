# pete_tpl

A Python binding for [libpetetpl](https://github.com/pete-tpl/libpetetpl).

__The project is under development!__

## Usage

```python
import pete_tpl

pete_tpl.init()

engine = pete_tpl.Engine()
result = engine.render("Hello, {# comment #} world! {{ 2 * 9}}")

print(result)
```

## TODO:
- Pass parameters to template rendering function