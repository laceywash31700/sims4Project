import services
import sims4.commands
from services.cheat_service import CheatService
from protocolbuffers import Consts_pb2

def modify_fund_helper(amount, reason, sim):
    if amount > 0:
        sim.family_funds.add(amount, reason, sim)
    else:
        sim.family_funds.try_remove(-amount, reason, sim)



@sims4.commands.Command('motherlode_plus', command_type=sims4.commands.CommandType.Live, console_type=sims4.commands.CommandType.Cheat)
def motherlode_plus(amount:int=0, _connection=None):
    tgt_client = services.client_manager().get(_connection)
    modify_fund_helper(amount, Consts_pb2.TELEMETRY_MONEY_CHEAT, tgt_client.active_sim)


@sims4.commands.Command('hellow', command_type=sims4.commands.CommandType.Live)
def _hellow(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    output('This is my first script mod')

@sims4.commands.Command('add_my_cheats', command_type=sims4.commands.CommandType.Live, console_type=sims4.commands.CommandType.Cheat)
def add_my_cheats(_connection=None):
    CheatService.enable_cheats()
