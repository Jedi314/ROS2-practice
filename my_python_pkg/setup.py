import os
from glob import glob
from setuptools import setup

package_name = 'my_python_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
        (os.path.join('share', package_name, 'launch'), 
         glob('launch/*.launch.py')),
        
        (os.path.join('share', package_name, 'config'),
         glob('config/*.yaml')),
        
        (os.path.join('share', package_name, 'rviz'), 
         glob('rviz/*.rviz')),
        
        (os.path.join('share', package_name, 'maps'),
         glob('maps/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=False,
    maintainer='vboxuser',
    maintainer_email='vboxuser@todo.todo',
    description='Package for robot localization',
    license='TODO',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)
