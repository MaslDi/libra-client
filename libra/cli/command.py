import abc
import sys
import os
import traceback
from libra.cli.color import print_color, bcolors


class Command(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def get_aliases(self):
        pass

    def get_params_help(self):
        return ""

    @abc.abstractmethod
    def get_description(self):
        pass

    @abc.abstractmethod
    def execute(self, client, params):
        pass

    def subcommand_execute(self, parent_command_name, commands, client, params):
        if len(params) == 0:
            self.print_subcommand_help(parent_command_name, commands)
            return
        commands_map = {}
        for i, cmd in enumerate(commands):
            for alias in cmd.get_aliases():
                if commands_map.__contains__(alias):
                    raise AssertionError(f"Duplicate alias {alias}")
                commands_map[alias] = i
        idx = commands_map.get(params[0])
        if idx is not None:
            if not params_valid(commands[idx].get_params_help(), params[1:]):
                print_color("\n\tParams number mismatch: ", bcolors.WARNING, end='')
                print_color(f"{' '.join(params)}", bcolors.OKGREEN)
                print_color("\n\t                  with: ", bcolors.WARNING, end='')
                commands[idx].print_params_help_no_desc()
                self.print_subcommand_help(parent_command_name, commands)
                return
            commands[idx].execute(client, params)
        else:
            self.print_subcommand_help(parent_command_name, commands)

    def print_subcommand_help(self, parent_command, commands):
        print("USAGE: ")
        print_color(f"\t{parent_command} <arg>\n", bcolors.OKGREEN)
        print("Use one of the following args for this command:\n")
        if "get_notice" in dir(self):
            print_color("\t" + self.get_notice(), bcolors.WARNING)
            print("")
        print_commands(commands)
        print("")

    def print_params_help(self):
        self.print_params_help_no_desc()
        print("\t" + self.get_description())
        if "get_notice" in dir(self):
            print_color("\t" + self.get_notice(), bcolors.WARNING)

    def print_params_help_no_desc(self):
        print_color(" | ".join(self.get_aliases()), bcolors.OKGREEN, end='')
        print_color(" " + self.get_params_help(), bcolors.OKBLUE)


def params_valid(spec: str, params: list) -> bool:
    """
    check the params in valid according to the spec.
    required params syntax: <param>
    optional params syntax: [param]
    any params syntax(MUST BE LAST ONE): [params ...]
    """
    spec_arr = spec.split()
    real_params_len = len(params)
    required_len = len([x for x in spec_arr if x[0]=='<'])
    if real_params_len < required_len:
        return False
    if spec.endswith("...]"):
        return True
    optionals = [x for x in spec_arr if x[0]=='[']
    optional_len = len(optionals)
    if real_params_len > required_len + optional_len:
        return False
    return True

def get_commands_alias(commands):
    alias_to_cmd = {}
    for command in commands:
        for alias in command.get_aliases():
            alias_to_cmd[alias] = command
    return (commands, alias_to_cmd)


def report_error(msg, err, verbose):
    print(f"[ERROR] {msg}: {err}")
    if verbose:
        traceback.print_exc()

def parse_cmd(cmd_str: str):
    return cmd_str.split()

def parse_bool(para_str):
    para = para_str.lower()
    if para == "true" or para == "t":
        return True
    elif para == "false" or para == "f":
        return False
    else:
        raise IOError(f"Unknown support bool str: {para_str}")


def print_commands(commands):
    for cmd in commands:
        cmd.print_params_help()

def blocking_cmd(cmd: str) -> bool:
    return cmd.endswith('b')


def debug_format_cmd(cmd: str) -> bool:
    return cmd.endswith('?')
