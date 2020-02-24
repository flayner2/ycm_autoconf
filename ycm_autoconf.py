import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument("path", type=str, help="Path to the project folder. The 'env' folder should "
                    "be at the root")

args = parser.parse_args()

in_path = args.path + "/"
libs_path = in_path + "env/lib/python3.8/site-packages/"
env_path = in_path + "env/bin/python"

with open(in_path + ".ycm_extra_conf.py", "w") as cfg:
    final_libs = ""
    first = True

    for directory in os.listdir(libs_path):
        if ("-info" not in directory) and ("__" not in directory):
            if first == True:
                first = False
                if directory.endswith(".py"):
                    final_libs = final_libs + "\n\t\t\t'" + libs_path + directory + "'"
                else:
                    final_libs = final_libs + "\n\t\t\t'" + libs_path + directory + "/'"
            else:
                if directory.endswith(".py"):
                    final_libs = final_libs + ",\n\t\t\t'" + libs_path + directory + "'"
                else:
                    final_libs = final_libs + ",\n\t\t\t'" + libs_path + directory + "/'"

    cfg.write("def Settings(**kwargs):\n\treturn {\n\t\t'interpreter_path': '" + env_path + "',\n\t\t'sys_path': [" + final_libs + "\n\t\t]\n\t}")

    print("Done")
