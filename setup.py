from setuptools import find_packages, setup

package_name = 'random_exploration_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/random_exploration.launch.py']),
        # Executables must live under lib/<package_name>/ so that `ros2 run`
        # can find them in ROS 2 Jazzy (it only scans lib/<pkg>/).
        ('lib/' + package_name, ['scripts/random']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jay',
    maintainer_email='jaygajjar890@gmail.com',
    description='Random gap-based exploration node for TurtleBot3',
    license='Apache-2.0',
    tests_require=['pytest'],
)