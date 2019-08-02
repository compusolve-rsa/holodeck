import holodeck
import uuid

cfg = {
        "name": "test_viewport_capture",
        "world": "TestWorld",
        "main_agent": "sphere0",
        "agents": [
            {
                "agent_name": "sphere0",
                "agent_type": "SphereAgent",
                "sensors": [
                    {
                        "sensor_type": "LocationTask"
                    },
                    {
                        "sensor_type": "CupGameTask",
                        "configuration": {
                            "Speed": 3,
                            "NumShuffles": 3,
                            "Seed": 0
                        }
                    },
                    {
                        "sensor_type": "BallLocationSensor"
                    }
                ],
                "control_scheme": 0,
                "location": [-.4, -.9, 1.8],
                "rotation": [90, 0, 0]
            }
        ],
        "window_width": 1024,
        "window_height": 1024
    }


def test_ball_location_and_reward():
    """Shuffle the ball using a seed. Ensure that after shuffling the ball location sensor
    detects the correct position and move the sphere agent forward to collide with the correct cup.
    Make sure it receives a reward of 1.
    """

    # binary_path = holodeck.packagemanager.get_binary_path_for_package("Dexterity")

    with holodeck.environments.HolodeckEnvironment(scenario=cfg,
                                                   # binary_path=binary_path,
                                                   # show_viewport=False,
                                                   start_world=False,
                                                   uuid="") as env:

        env.reset()

        env.tick(300)
        for _ in range(30):
            state, reward, terminal, _ = env.step([0])
            if reward == 1:
                touched_cup = True
        assert touched_cup and state["BallLocationSensor"] == 2
