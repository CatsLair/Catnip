import subprocess


def run_script(file_path: str, extension: str = 'js') -> None:
    try:
        if extension == 'py':
            output = subprocess.check_output(["python3", str(file_path)], stderr=subprocess.STDOUT, text=True)
        elif extension == 'js':
            output = subprocess.check_output(["node", str(file_path)], stderr=subprocess.STDOUT, text=True)
        else:
            raise ValueError(f"Unsupported script extension: {extension}")
    except subprocess.CalledProcessError as e:
        output = e.output

    return output
