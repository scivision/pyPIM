
from glob import glob
from numpy.distutils.core import Extension, setup
from os.path import dirname, join, realpath

name = 'pypim'
sources = []
sourcePath = 'source'
sourceFiles = ['pimne.pyf', 'pimsub.f']
for src in sourceFiles:
    sources.append(join(sourcePath, src))

objects = []
objects.append(join(sourcePath, 'libpim.a')) 

ext = Extension(extra_objects=objects, f2py_options=['--quiet'], name='pimne', sources=sources)

cgmData = glob(join(join('data', 'cgmdb'), '*.*'))
llfData = glob(join(join(join('data', 'llfdb'), 'unform'), '*.*'))
lmeData = glob(join(join(join('data', 'lmedb'), 'unform'), '*.*'))
mlfData = glob(join(join(join('data', 'mlfdb'), 'unform'), '*.*'))
ursiData = glob(join(join(join('data', 'ursidb'), 'unform'), '*.*'))
usuData = glob(join(join(join('data', 'usudb'), 'unform'), '*.*'))

pimDataFiles = [
    (join(name, join('data', 'cgmdb')), cgmData),
    (join(name, join(join('data', 'llfdb'), 'unform')), llfData),
    (join(name, join(join('data', 'lmedb'), 'unform')), lmeData),
    (join(name, join(join('data', 'mlfdb'), 'unform')), mlfData),
    (join(name, join(join('data', 'ursidb'), 'unform')), ursiData),
    (join(name, join(join('data', 'usudb'), 'unform')), usuData)
    ]

if __name__ == '__main__':

    setup(        
        author='Ronald Ilma', 
        author_email='rri5@cornell.edu',
        data_files=pimDataFiles, 
        description='Parameterized Ionospheric Model (PIM)', 
        ext_modules=[ ext ],
        ext_package=name, 
        name=name, 
        packages=[name],  
        url='https://github.com/rilma/pyPIM', 
        version='0.0.2',        
    )  