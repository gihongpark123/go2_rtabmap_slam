from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    return LaunchDescription([
        # Declare arguments for configuration
        DeclareLaunchArgument(
            name='use_rviz',
            default_value='true',
            choices=['true', 'false'],
            description='Open RVIZ for visualization'
        ),
        DeclareLaunchArgument(
            name='localize_only',
            default_value='true',
            choices=['true', 'false'],
            description='Localize only, do not change loaded map'
        ),
        DeclareLaunchArgument(
            name='restart_map',
            default_value='false',
            choices=['true', 'false'],
            description='Delete previous map and restart'
        ),

      # [수정] rslidar_sdk 호출부 삭제 후 아래 내용으로 교체
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                PathJoinSubstitution([
                    FindPackageShare('hesai_ros_driver'), # 패키지 이름
                    'launch',
                    'start.py'                           # 아까 공유해주신 파일명
                ])
            )
        ),

        # Include rslidar_robosense.launch.py
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                PathJoinSubstitution([
                    FindPackageShare('go2_slam_nav'),
                    'launch',
                    'rtab_lidar.launch.py'
                ])
            ),
            launch_arguments=[
                ('use_rviz', LaunchConfiguration('use_rviz')),
                ('localize_only', LaunchConfiguration('localize_only')),
                ('restart_map', LaunchConfiguration('restart_map')),
            ],
        ),
    ])
