def get_thetas():
    thetas = [0, 0]
    try:
        file = open("result_thetas.txt", "r")
    except FileNotFoundError:
        return thetas
    except PermissionError:
        raise AssertionError("The program doesn't have the permissions to \
open the file")
    document = file.read()
    file.close()
    new_lines = document.splitlines()
    assert len(new_lines) == 1, "Format error found in result_thetas.txt"
    assert document.count(",") == 1, "Format error found in result_thetas.txt"
    splitted_data = document.split(",")
    assert len(splitted_data) == 2, "Format error found in result_thetas.txt"
    try:
        thetas[0] = float(splitted_data[0])
        thetas[1] = float(splitted_data[1])
    except (ValueError, OverflowError):
        raise AssertionError("Format error found in result_thetas.txt")
    return thetas
