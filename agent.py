def infer_modules(content_blocks):
    modules = []
    current_module = None
    last_submodule = None

    for tag, text in content_blocks:
        if tag == "h1":
            current_module = {
                "module": text,
                "Description": "",
                "Submodules": {}
            }
            modules.append(current_module)

        elif tag == "h2" and current_module:
            current_module["Submodules"][text] = ""
            last_submodule = text

        elif tag == "p" and current_module:
            if not current_module["Description"]:
                current_module["Description"] = text
            elif last_submodule:
                current_module["Submodules"][last_submodule] += " " + text

    return modules

