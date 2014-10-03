from setuptools import setup
from distutils.core import Extension
from setuptools import Command
from setuptools.command.build_ext import build_ext as _build_ext
from Cython.Compiler.Main import compile as compile_pyx
import shutil
import re
import os

class BuildPyxCommand(_build_ext):
    '''A custom Cython compiler command
    
    We use this instead of the distutils built-in one because pip
    fails to compile cython.
    '''
    def pyrex_sources(self, sources, ext):
        '''Fake out cythonize if not in pip'''
        return sources
        
    def build_extension(self, ext):
        for i in range(len(ext.sources)):
            source = ext.sources[i]
            if os.path.splitext(source)[1] == ".pyx":
                result = compile_pyx(
                    source,
                    cplus=True,
                    generate_pxi=True,
                    full_module_name=ext.name)
                if result.num_errors == 0:
                    ext.sources[i] = result.c_file
        return _build_ext.build_extension(self, ext)
    
def get_version():
    """Get version from git or file system.

    If this is a git repository, try to get the version number by
    running ``git describe``, then store it in
    javabridge/_version.py. Otherwise, try to load the version number
    from that file. If both methods fail, quietly return None.

    """
    git_version = None
    if os.path.exists(os.path.join(os.path.dirname(__file__), '.git')):
        import subprocess
        try:
            git_version = subprocess.Popen(['git', 'describe'], 
                                           stdout=subprocess.PIPE).communicate()[0].strip()
        except:
            pass

    version_file = os.path.join(os.path.dirname(__file__), 'pyemd', 
                                '_version.py')
    if os.path.exists(version_file):
        with open(version_file) as f:
            cached_version_line = f.read().strip()
        try:
            # From http://stackoverflow.com/a/3619714/17498
            cached_version = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", 
                                       cached_version_line, re.M).group(1)
        except:
            raise RuntimeError("Unable to find version in %s" % version_file)
    else:
        cached_version = None

    if git_version and git_version != cached_version:
        with open(version_file, 'w') as f:
            print >>f, '__version__ = "%s"' % git_version

    return git_version or cached_version

def get_ext_modules():
    from numpy import get_include
    fast_emd_path = os.path.join(os.path.dirname(__file__), "FastEMD")
    include_path = os.path.join(os.path.dirname(__file__), "pyemd", "include")
    sources = ["pyemd/_pyemd.pyx"]
    extension = Extension(
        "_pyemd",
        sources,
        language = "c++",
        include_dirs = [get_include(), fast_emd_path, include_path])
    #
    # Have to patch to keep distutils from grabbing .pyx files
    #
    extension.sources = sources
    return [extension]

root = os.path.dirname(__file__)
readme_md = os.path.join(root, "README.md")

if os.path.isfile(readme_md):
    readme_txt = os.path.join(root, "README.txt")
    shutil.copy(readme_md, readme_txt)
else:
    readme_txt = None
setup(name="pyemd",
      version=get_version(),
      author="Lee Kamentsky",
      author_email="leek@broadinstitute.org",
      url="http://cellprofiler.org",
      packages=["pyemd"],
      description="Python wrapper for FastEMD",
      long_description="""PyEMD is a Python wrapper for the fast earth mover's
distance algorithm described in Pele, "Fast and Robust Earth Mover's Distances",
ICCV2009, doi: 10.1109/ICCV.2009.5459199""",
      license='BSD License',
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: BSD License",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7"],
      cmdclass= { "build_ext": BuildPyxCommand },
      ext_modules=get_ext_modules())
if readme_txt is not None:
    os.remove(os.path.join(root, "README.txt"))      

      
        