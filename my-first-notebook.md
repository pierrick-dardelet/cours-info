---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.5
kernelspec:
  name: python3
  display_name: Python 3 (ipykernel)
  language: python
---

```{code-cell} ipython3
def fact(n):
    return 1 if n <= 1 else n * fact(n-1)


# on affiche quelques résultats
for n in [4, 25]:
    print(f"fact({n}) = {fact(n)}")


fact(3)
```

```{code-cell} ipython3
fact(6)
```
