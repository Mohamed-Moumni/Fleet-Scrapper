from playwright.sync_api import Frame

def dump_frame_tree(frame: Frame):
    if frame.name == "frame_aint_d":
        return frame
    frames = [dump_frame_tree(child) for child in frame.child_frames]
    frame_to_return = next((item for item in frames if item != None), None)
    return frame_to_return