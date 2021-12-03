# MyKotlin kernel for Jupyter
[Example](https://github.com/nufeng1999/jupyter-MyKotlin-kernel/blob/master/example/jupyter_kotlin_readme.ipynb "Example")
* Make sure you have the following requirements installed:
  * kotlin
  * jupyter
  * python 3
  * pip

### Step-by-step

```bash
git clone https://github.com/nufeng1999/jupyter-MyKotlin-kernel.git
cd jupyter-MyKotlin-kernel
pip install -e .  # for system install: sudo install .
cd jupyter_MyKotlin_kernel && install_MyKotlin_kernel --user # for sys install: sudo install_dart_kernel
# now you can start the notebook
jupyter notebook
```

## License

[MIT](LICENSE.txt)
