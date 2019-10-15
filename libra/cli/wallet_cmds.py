from libra.cli.command import *
from libra.wallet_library import WalletLibrary
from libra.json_print import json_print


class WalletCmd(Command):
    def get_aliases(self):
        return ["wallet", "w"]

    def get_description(self):
        return "show account information of a wallet derived from mnemonic file"

    def execute(self, client, params):
        commands = [
            WalletCmdShow(),
            WalletCmdAccount(),
            WalletCmdBalance(),
            WalletCmdCreate()
        ]
        self.subcommand_execute(params[0], commands, client, params[1:])


class WalletCmdShow(Command):
    def get_aliases(self):
        return ["show", "s"]

    def get_params_help(self):
        return "<mnemonic_file_path>"

    def get_description(self):
        return "Show the mnemonic words, seed and addresses of a wallet"

    def execute(self, client, params):
        try:
            wallet = WalletLibrary.recover(params[1])
            json_print(wallet)
        except Exception as err:
            report_error("Failed to get balance", err, client.verbose)


class WalletCmdAccount(Command):
    def get_aliases(self):
        return ["account", "a"]

    def get_params_help(self):
        return "<mnemonic_file_path>"

    def get_description(self):
        return "Show the keypair and address of accounts in a wallet"

    def execute(self, client, params):
        try:
            wallet = WalletLibrary.recover(params[1])
            print("[")
            for account in wallet.accounts:
                json_print(account)
                print(",", end='')
            print("\b]")
        except Exception as err:
            report_error("Failed to get balance", err, client.verbose)


class WalletCmdBalance(Command):
    def get_aliases(self):
        return ["balance", "b"]

    def get_params_help(self):
        return "<mnemonic_file_path>"

    def get_description(self):
        return "Get the balance of all accounts in a wallet"

    def execute(self, client, params):
        try:
            wallet = WalletLibrary.recover(params[1])
            maps = {}
            for account in wallet.accounts:
                maps[account.address_hex] = client.get_balance(account.address_hex)
                #TODO: multi query combine to one
            maps["total_balance"] = sum(maps.values())
            json_print(maps)
        except Exception as err:
            report_error("Failed to get balance", err, client.verbose)


class WalletCmdCreate(Command):
    def get_aliases(self):
        return ["create", "c"]

    def get_params_help(self):
        return "<mnemonic_file_path>"

    def get_description(self):
        return "create a new wallet and save the mnemonic file to <mnemonic_file_path>"

    def execute(self, client, params):
        try:
            wallet = WalletLibrary.new()
            json_print(wallet)
            wallet.write_recovery(params[1])
            print(f"Wallet mnemonic file saved to '{params[1]}'.")
        except Exception as err:
            report_error("Failed to get balance", err, client.verbose)
