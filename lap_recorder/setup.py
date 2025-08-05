from setuptools import find_packages, setup

package_name = 'lap_recorder'

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
    maintainer='saku',
    maintainer_email='nakamura.shotaro.e8@s.gifu-u.ac.jp',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'lap_timer_node = lap_recorder.lap_timer_node:main',
            'web_publisher_node = lap_recorder.web_publisher_node:main',
        ],
    },
)
