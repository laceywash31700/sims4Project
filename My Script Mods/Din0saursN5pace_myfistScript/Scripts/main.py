import services
import sims4.commands
from services.cheat_service import CheatService
from protocolbuffers import Consts_pb2
from server_commands.argument_helpers import get_tunable_instance


def modify_fund_helper(amount, reason, sim):
    if amount > 0:
        sim.family_funds.add(amount, reason, sim)
    else:
        sim.family_funds.try_remove(-amount, reason, sim)


@sims4.commands.Command('motherlode_plus', command_type=sims4.commands.CommandType.Live, console_type=sims4.commands.CommandType.Cheat)
def motherlode_plus(amount: int = 0, _connection=None):
    CheatService.enable_cheats()
    tgt_client = services.client_manager().get(_connection)
    modify_fund_helper(amount, Consts_pb2.TELEMETRY_MONEY_CHEAT, tgt_client.active_sim)


@sims4.commands.Command('hellow', command_type=sims4.commands.CommandType.Live)
def _hellow(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    output('Whats up, you successfully connected to the command console Good job me!')


@sims4.commands.Command('make_sims_sheepy', command_type=sims4.commands.CommandType.Live)
def make_household_sleepy(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    active_household = services.active_household()
    if active_household is None:
        output('No household active to make sheepy.')
        return False
    for sim in active_household:
        if sim.is_human and not sim.is_npc:
            cur_stat = get_tunable_instance(sims4.resources.Types.STATISTIC, 'motive_energy', exact_match=True)
            tracker = sim.get_tracker(cur_stat)
            cur_value = tracker.get_value(cur_stat) if tracker is not None else -999
            sim.commodity_tracker.set_all_commodities_to_best_value(visible_only=True)
            if cur_value != -999:
                output('{} {}\'s energy is {:.0f}'.format(sim.first_name, sim.last_name, cur_value))
                sim.commodity_tracker.set_value(cur_stat, -51)
            else:
                output('Unable to get current energy value for {} {}'.format(sim.first_name, sim.last_name))