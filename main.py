import argparse
import json
import sys
from pathlib import Path

import cv2
import mediapipe as mp


def load_image(image_path):
    image = cv2.imread(str(image_path))
    if image is None:
        raise ValueError(f"Cannot read image: {image_path}")
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def run_pose(image):
    mp_pose = mp.solutions.pose
    with mp_pose.Pose(static_image_mode=True, model_complexity=2) as pose:
        result = pose.process(image)
    return result.pose_landmarks


def landmarks_to_json(landmarks):
    if landmarks is None:
        return {}

    mp_pose = mp.solutions.pose
    output = {}

    for idx, landmark in enumerate(landmarks.landmark):
        name = mp_pose.PoseLandmark(idx).name.lower()
        output[name] = {
            "x": float(landmark.x),
            "y": float(landmark.y),
            "score": float(landmark.visibility),
        }

    return output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True)
    args = parser.parse_args()

    image_path = Path(args.image)
    if not image_path.exists():
        print(f"Image not found: {image_path}", file=sys.stderr)
        sys.exit(1)

    image = load_image(image_path)
    landmarks = run_pose(image)
    result = landmarks_to_json(landmarks)

    with open("output.json", "w") as f:
        json.dump(result, f, indent=2)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()