import numpy as np
import pandas as pd
import subprocess
from tqdm import tqdm
import re
import os
from datetime import datetime


def ts2mp4(ts_file, mp4_file, log_file):
    # transcode ts to mp4, single file

    process = subprocess.run(
        [   
            # "sudo",
            "ffmpeg",
            "-i",
            ts_file,
            "-c:v",
            "libx264",
            "-crf",
            "23",
            "-preset",
            "medium",
            "-c:a",
            "aac",
            "-b:a",
            "128k",
            mp4_file,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    # make file if not exist
    if not os.path.exists(log_file):
        with open(log_file, "w") as f:
            f.write("")
    with open(log_file, "a") as f:
        f.write(process.stdout)
        f.write("==================ERROR==================\n")
        f.write(process.stderr)
        f.write("==================END==================\n")
    

def batch(ts_dir, mp4_dir, re_tag=True):
    # transcode ts to mp4, batch
    ts_files = []
    today_date = datetime.today().strftime('%Y-%m-%d')
    yesterday_date = (datetime.today() - pd.Timedelta(days=1)).strftime('%Y-%m-%d')
    
    for root, dirs, files in os.walk(ts_dir):
        for file in files:
            if file.endswith(".ts"):
                # match yesterday's date
                search = re.search(r"(\d{4}-\d{2}-\d{2})", file)
                if re_tag and search and search.group(1) == yesterday_date:
                    ts_files.append(os.path.join(root, file))
                    
    log_dir = os.path.join(mp4_dir, "log")
    subprocess.run(["mkdir", "-p", log_dir])
    for ts_file in tqdm(ts_files):
        mp4_file = os.path.join(mp4_dir, os.path.basename(ts_file).replace(".ts", ".mp4"))
        log_file = os.path.join(mp4_dir, "log", today_date + ".log")
        ts2mp4(ts_file, mp4_file, log_file)
    print(f"Transcode {len(ts_files)} files completed.")


if __name__ == "__main__":
    input_dir = "/home/zqy/learningFile/docker/chaturbate/videos-dvr"
    output_dir = "/home/zqy/media/videos-dvr-mp4"
    batch(input_dir, output_dir)
