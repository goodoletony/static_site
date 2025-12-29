import os
import logging
import shutil

logging.basicConfig(level=logging.INFO)


def replace_public(begun=False, current_dir='static'):
    if not begun:
        logging.info(f"Removing public directory")
        shutil.rmtree('public')
        logging.info("Creating public directory")
        os.mkdir('public')

    for item in os.listdir(current_dir):
        src_path = os.path.join(current_dir, item)
        rel_path = os.path.relpath(src_path, "static")
        dest_path = os.path.join("public", rel_path)
        if os.path.isfile(src_path):
            logging.info(f"Copying {item} to public directory...")
            shutil.copy(src_path, dest_path)
            continue
        else:
            logging.info(f"Creating {item} directory in public...")
            os.mkdir(dest_path)
            replace_public(begun=True, current_dir=src_path)
# replace_public()
