import socket

host = socket.gethostname()

# environment specific constants

DATA_ROOT = '/data'
RESULTS_ROOT = '/results'

if host == 'asimov':
    DATA_ROOT = '/home/u1116888/docker/ZetaPolicy/data'
    RESULTS_ROOT = '/home/u1116888/projects/Zeta-Policy/rl-files'

if host == 'Thejans-MacBook-Pro.local':
    DATA_ROOT = '/Users/jayaneetha/Research/PycharmProjects/iemocap_dataset/pkl'
    RESULTS_ROOT = '/Users/jayaneetha/Research/PycharmProjects/Zeta-Policy/rl-files'

if host == 'Thejans-MacBook-Pro-13.local':
    DATA_ROOT = '/Users/jayaneetha/PycharmProjects/iemocap_dataset/pkl'
    RESULTS_ROOT = '/Users/jayaneetha/PycharmProjects/Zeta-Policy/rl-files'

if host == 'Thejans-Servian-MacBook-Pro.local':
    DATA_ROOT = '/Users/thejanrajapakshe/Research/PycharmProjects/TAC_RL_DA_analysis/data'
    RESULTS_ROOT = '/Users/thejanrajapakshe/Research/PycharmProjects/Zeta-Policy/rl-files'

EMOTIONS = ['hap', 'sad', 'ang', 'neu']
GENDERS = ['M', 'F']
NUM_MFCC = 40
DURATION = 2
SR = 22050
NO_features = 87  # sr22050&2sec

WINDOW_LENGTH = 1
