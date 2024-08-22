from setuptools import find_packages, setup

package_name = 'autoware_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hyconsoft_rnd',
    maintainer_email='hyconsoft_rnd@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'pub = autoware_pubsub.autowarepub:main',
		'sub = autoware_pubsub.autowaresub:main',
        ],
    },
)
