from playwright.sync_api import Frame
from typing import Dict,List
from dotenv import load_dotenv
from pathlib import Path
from os import getenv

load_dotenv(dotenv_path=Path("../.env"))


def dump_frame_tree(frame: Frame, frame_name: str):
    if frame.name == frame_name:
        return frame
    frames = [dump_frame_tree(child, frame_name) for child in frame.child_frames]
    frame_to_return = next((item for item in frames if item != None), None)
    return frame_to_return


def filter_models(models:List[Dict[str, str]]):
    filtred_models:List[str] = []
    try:
        for model in models:
            if model["text"].find(";") > -1:
                _, year = model["text"].split(";")
                start, end = year.split("-")
                start = int(start) if start != "" else None
                end = int(end) if end != "" else None
                if start >= int(getenv("STARTING_SCRAP_YEAR")) or (end and int(getenv("STARTING_SCRAP_YEAR")) <= end):
                    filtred_models.append(model['value'])
    except Exception as e:
        raise ValueError("Error: error while filtering models : {e}")
    return filtred_models