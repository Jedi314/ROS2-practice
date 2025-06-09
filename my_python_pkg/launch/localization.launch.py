from launch import LaunchDescription
from launch_ros.actions import Node, LifecycleNode
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    
    return LaunchDescription([
        # Map Server
        LifecycleNode(
            package='nav2_map_server',
            executable='map_server',
            name='map_server',
            namespace='',
            parameters=[{
                'use_sim_time': False,
                'yaml_filename': [PathJoinSubstitution([
                    FindPackageShare('my_python_pkg'),
                    'maps',
                    'map.yaml'
                ])]
            }],
            output='screen'
        ),
        
        # AMCL
        LifecycleNode(
            package='nav2_amcl',
            executable='amcl',
            name='amcl',
            namespace='',
            parameters=[PathJoinSubstitution([
                FindPackageShare('my_python_pkg'),
                'config',
                'amcl_params.yaml'
            ])],
            output='screen'
        ),
        
        # Lifecycle Manager
        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='lifecycle_manager_localization',
            namespace='',
            parameters=[{
                'autostart': True,
                'node_names': ['map_server', 'amcl', 'collision_monitor']
            }],
            output='screen'
        ),
        
        # RViz
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            namespace='',
            arguments=['-d', PathJoinSubstitution([
                FindPackageShare('my_python_pkg'),
                'rviz',
                'localization.rviz'
            ])]
        ),
        
        # Collision Monitor Node
        Node(
            package='nav2_collision_monitor',
            executable='collision_monitor',
            name='collision_monitor',
            namespace='',
            parameters=[PathJoinSubstitution([
                FindPackageShare('my_python_pkg'),
                'config',
                'collision_monitor_params.yaml'
            ])],
            output='screen'
        ),
        
        # Joystick Node
        Node(
            package='teleop_twist_joy',
            executable='teleop_node',
            name='teleop_twist_joy',
            namespace='',
            remappings=[
                ('cmd_vel', 'cmd_vel_raw')
            ],
            parameters=[PathJoinSubstitution([
                FindPackageShare('my_python_pkg'),
                'config',
                'joystick_params.yaml'
            ])]
        )
    ])
