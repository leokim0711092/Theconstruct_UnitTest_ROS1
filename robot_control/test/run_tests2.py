import rosunit
import rotate_robot_test_cases2

# rosunit
rosunit.unitrun('robot_control', 'rotate_robot_test_cases',
                'rotate_robot_test_cases2.MyTestSuite.test_CaseA')
rosunit.unitrun('robot_control', 'rotate_robot_test_cases',
                'rotate_robot_test_cases2.MyTestSuite.test_CaseB')