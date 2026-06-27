총 필요한 터미널 2개
1. 터미널켜서 아래의 명령어 모두 입력
   cd ws
   colcon build
   source install/setup.bash
   source /opt/ros/humble/setup.bash
2. 새로운 터미널 켜서 아래의 명령어 모두 입력
   ssh unitree@192.168.123.18
   123 #젯슨 비밀번호
   123 #젯슨 비밀번호
   source ~/unitree_ros2/install/setup.bash

   이후 slam및 nav 명령어
   매핑
   ros2 launch go2_slam_nav mapping.launch.py ​​localize_only:=false restart_map:=true
   매핑이 완료되었다면 맵 저장은 ctrl + c로 해당 명령어 종료시 자동저장
   
   만약 터미널창에 노란색글씨의 warning이 뜰 경우
   스크린샷처럼 모드를 mapping으로 바꿔주어야함
   <img width="1278" height="756" alt="스크린샷 2026-06-27 18-29-16" src="https://github.com/user-attachments/assets/cde81d08-e2c9-4fc3-ab2d-0c804153ac83" />

   nav
   ros2 launch go2_slam_nav nav.launch.py ​​localize_only:=true restart_map:=false
   실행시 greedmap이 만들어지는 것을 기다린 후 맵이 완성되고 navigation에 active가 뜬다면 해당 스크린샷처럼 골지점을 정해주면 됨
   <img width="1542" height="963" alt="image" src="https://github.com/user-attachments/assets/081f9021-f545-4672-86a8-b15282365685" />


  
