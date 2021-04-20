import os

PLOT_ARGUMENTS = {}
PLOT_ARGUMENTS[0] = {}
PLOT_ARGUMENTS[1] = {}
PLOT_ARGUMENTS[2] = {}
PLOT_ARGUMENTS[3] = {}
PLOT_ARGUMENTS[4] = {}
PLOT_ARGUMENTS[5] = {}
PLOT_ARGUMENTS[0]['title']          = 'Angle Plot'
PLOT_ARGUMENTS[0]['legend']         = 'Angle Legend'
PLOT_ARGUMENTS[0]['xlabel']         = 'Angle'
PLOT_ARGUMENTS[0]['xunits']         = 'deg'
PLOT_ARGUMENTS[0]['ncheck_cycle']   = False
PLOT_ARGUMENTS[0]['normal_x_var']   = 2
PLOT_ARGUMENTS[0]['extras_x_var']   = 1
PLOT_ARGUMENTS[1]['title']          = 'Time Plot'
PLOT_ARGUMENTS[1]['legend']         = 'Time Legend'
PLOT_ARGUMENTS[1]['xlabel']         = 'Time'
PLOT_ARGUMENTS[1]['xunits']         = 'sec'
PLOT_ARGUMENTS[1]['ncheck_cycle']   = True
PLOT_ARGUMENTS[1]['normal_x_var']   = 3
PLOT_ARGUMENTS[1]['extras_x_var']   = 2
PLOT_ARGUMENTS[2]['title']          = 'RPM Plot'
PLOT_ARGUMENTS[2]['legend']         = 'RPM Legend'
PLOT_ARGUMENTS[2]['xlabel']         = 'RPM'
PLOT_ARGUMENTS[2]['xunits']         = ''
PLOT_ARGUMENTS[2]['ncheck_cycle']   = False
PLOT_ARGUMENTS[2]['normal_x_var']   = 2
PLOT_ARGUMENTS[2]['extras_x_var']   = 1
PLOT_ARGUMENTS[3]['title']          = 'Cycle Plot'
PLOT_ARGUMENTS[3]['legend']         = 'Cycle Legend'
PLOT_ARGUMENTS[3]['xlabel']         = 'Cycle'
PLOT_ARGUMENTS[3]['xunits']         = ''
PLOT_ARGUMENTS[3]['ncheck_cycle']   = False
PLOT_ARGUMENTS[3]['normal_x_var']   = 2
PLOT_ARGUMENTS[3]['extras_x_var']   = 1
PLOT_ARGUMENTS[4]['title']          = 'Space Plot'
PLOT_ARGUMENTS[5]['title']          = 'Free Plot'

def dir_size(start, follow_links = True, start_depth = 0):
    """
    Given a directory, returns its size in bytes
    """
    # from exception_handling import handle_exception
    # Get a list of all names of files and subdirectories in directory start
    try: 
        dir_list = os.listdir(start)
        # from exception_handling import CURRENT_EXCEPTION
        # assert(not CURRENT_EXCEPTION)
    except Exception as e:
        print(e)
        # handle_exception('Cannot list directory %s'%start)
        return

    total = 0
    for item in dir_list:
        # Get statistics on each item--file and subdirectory--of start
        path = os.path.join(start, item)
        try: 
            stats = os.stat(path)
            # from exception_handling import CURRENT_EXCEPTION
            # assert(not CURRENT_EXCEPTION)
        except:
            # handle_exception('Cannot list directory %s'%path)
            return
        # The size in bytes is in the seventh item of the stats tuple, so:
        total += stats[6]
        # recursive descent if warranted
        if os.path.isdir(path) and (follow_links or not os.path.islink(path)):
            bytes = dir_size(path, follow_links, start_depth+1)
            total += bytes
    return total