from setuptools import setup

setup(name='jupyter_MyMyKotlin_kernel',
      version='0.0.1',
      description='Minimalistic Kotlin kernel for Jupyter',
      author='nufeng',
      author_email='18478162@qq.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
      ],
      url='https://github.com/nufeng1999/jupyter-MyKotlin-kernel/',
      download_url='https://github.com/nufeng1999/jupyter-MyKotlin-kernel/tarball/0.0.1',
      packages=['jupyter_MyKotlin_kernel'],
      scripts=['jupyter_MyKotlin_kernel/install_MyKotlin_kernel'],
      keywords=['jupyter', 'notebook', 'kernel', 'kotlin'],
      include_package_data=True
      )
