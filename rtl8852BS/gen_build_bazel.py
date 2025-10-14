import re

def parse_variable(file_content, var_name):
    """parsing specific variables"""
    pattern = rf"{var_name}\s*=\s*(.+)"
    match = re.search(pattern, file_content)
    if match:
        return match.group(1).strip()
    return ""

def parse_filegroup(file_content, var_name):
    """parsing makefile_var then generate filegroup"""
    srcs = parse_variable(file_content, var_name).split()
    if not srcs:
        return ""

    srcs = list(set([s.replace('.o', '.c') for s in srcs]))
    return f'filegroup(\n    name = "{var_name}",\n    srcs = [\n' + ''.join([f'        "{src}",\n' for src in srcs]) + '    ],\n)'

def process_extra_cflags(extra_cflags):
    """parsing EXTRA_CFLAGS then generate INCLUDE and COPTS"""
    includes = []
    copts = []
    flags = extra_cflags.split()
    for flag in flags:
        if flag.startswith('-I'):
            # remove ./ then add to includes
            include_path = flag[2:]
            if include_path.startswith('./'):
                include_path = include_path[2:]
            includes.append(include_path)
        else:
            # process quotation marks in EXTRA_CFLAGS
            if '"' in flag:
                flag = re.sub(r'([^\\])"', r'\1\\"', flag)
            copts.append(flag)
    include_str = ' '.join(includes)
    return include_str, copts

def format_list(prefix, items, indent="    "):
    """format output"""
    if items:
        return f'{prefix} = [\n' + ''.join([f'{indent}"{item}",\n' for item in items]) + f'{indent[:-4]}],'
    return f'{prefix} = []'

def generate_ddk_module(filegroup_list, include, copts, module_name, kernel_build, dep, text_hdrs):
    """generate ddk_module"""
    hdrs_list = f'glob(["**/*.h"]{text_hdrs})'
    includes_list = include.split()
    srcs_list = [':' + var_name for var_name in set(filegroup_list.split())]
    deps_list = dep.split() if dep else []

    return f"""ddk_module(
    name = "{module_name}",
    {format_list('srcs', srcs_list)}
    hdrs = {hdrs_list},
    {format_list('includes', includes_list)}
    {format_list('copts', copts)}
    out = "{module_name}.ko",
    kernel_build = "{kernel_build}",
    {format_list('deps', deps_list)}
)"""

def main():
    try:
        with open('makefile_var', 'r') as file:
            makefile_content = file.read()
    except FileNotFoundError:
        print("Error: The file 'makefile_var' was not found.")
        return

    filegroup_list = parse_variable(makefile_content, "FILEGROUP_LIST")
    extra_cflags = parse_variable(makefile_content, "EXTRA_CFLAGS")
    module_name = parse_variable(makefile_content, "MODULE_NAME") or "default_module_name"
    kernel_build = parse_variable(makefile_content, "KERNEL_BUILD") or "//common:rtkstb"
    dep = parse_variable(makefile_content, "DEP")
    text_hdrs_string = parse_variable(makefile_content, "TEXT_HDRS")
    drv_folder = parse_variable(makefile_content, "DRV_FOLDER")
    
    # transform text_hdrs to list string
    if text_hdrs_string.strip():
        text_hdrs_list = [f'"{hdr}"' for hdr in text_hdrs_string.split()]
        text_hdrs = f' + [{", ".join(text_hdrs_list)}]'
    else:
        text_hdrs = ""

    print("Parsed Variables:")
    print(f"FILEGROUP_LIST = {filegroup_list}")
    print(f"EXTRA_CFLAGS = {extra_cflags}")
    print(f"MODULE_NAME = {module_name}")
    print(f"KERNEL_BUILD = {kernel_build}")
    print(f"DEP = {dep}")
    print()

    unique_filegroup_list = list(set(filegroup_list.split()))
    filegroup_contents = []
    for var_name in unique_filegroup_list:
        fg_content = parse_filegroup(makefile_content, var_name)
        if fg_content:
            filegroup_contents.append(fg_content)

    # parsing EXTRA_CFLAGS
    include, copts = process_extra_cflags(extra_cflags)

    # generate ddk_module content
    ddk_module_content = generate_ddk_module(filegroup_list, include, copts, module_name, kernel_build, dep, text_hdrs)

    # load related bazel module
    load_statements = (
        'load("@kleaf//build/kernel/kleaf:kernel.bzl", "ddk_module")\n'
        'load("//build/kernel/kleaf:kernel.bzl", "ddk_headers")\n\n'
    )

    # generate BUILD.bazel content
    build_bazel_content = load_statements + "\n\n".join(filegroup_contents) + "\n\n" + ddk_module_content
    print("Generated BUILD.bazel Content:")
    #print(build_bazel_content)

    try:
        with open('BUILD.bazel', 'w') as outfile:
            outfile.write(build_bazel_content)
        print("Content successfully written to 'BUILD.bazel'.")
        print(f"tools/bazel build //common-modules/{drv_folder}:{module_name} --verbose_failures --sandbox_debug")
    except IOError as e:
        print(f"Error: Failed to write to file 'BUILD.bazel'.\n{e}")

if __name__ == "__main__":
    main()

