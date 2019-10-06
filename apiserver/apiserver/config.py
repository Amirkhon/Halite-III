from passlib.context import CryptContext

# General coordinator settings
COMPETITION_OPEN = False
# Original PHP: "compState", "finalsPairing"
COMPETITION_FINALS_PAIRING = False
# Final open game id, set this to the id of last game played in the open stage
LAST_OPEN_GAME = None
# Rank cutoff schedule during finals
# In each entry the first value is number of games to start the cutoff and
# second value is the rank cutoff to use.
FINALS_CUTOFF_SCHEDULE = [ # For 6000 bots
    (0, 4500),      # Everyone starts
    (55200, 3800),  # When everyone has ~40 games
    (105900, 3000), # 80 games
    (146100, 2100), # 120 games, starter bots end
    (188400, 1500), # 180 games
    (223700, 1000), # 250 games
    (257300, 500),  # 350 games
    (299300, 250), # 600 games
    (349900, 150), # 1200 games
]

# Max number of games a bot version can error out in before being
# stopped from playing
MAX_ERRORS_PER_BOT = 50
MAX_ERROR_PERCENTAGE = 0.1

# How many minutes old a compilation job must be to be considered stuck.
COMPILATION_STUCK_THRESHOLD = 30

# How many times we will try to compile
MAX_COMPILATION_ATTEMPTS = 3

# Flask settings
# Max size of an upload, in bytes
MAX_BOT_UPLOAD_SIZE = 20 * 1024 * 1024
# Needs to match corresponding value in worker configuration
MAX_COMPILED_BOT_UPLOAD_SIZE = 100 * 1024 * 1024
# Max bot file size
MAX_BOT_FILE_SIZE = 100 * 1024 * 1024
# Secret key for Flask session cookies
FLASK_SECRET_KEY = "24secret24"
# Where to look for API keys
API_KEY_HEADER = "X-Api-Key"
# What session cookie to use
SESSION_COOKIE = "user_id"
SESSION_SECRET = "s24secret"

# Google Cloud
GCLOUD_PROJECT = 'Students24'
GCLOUD_PROJECT_ID = 'dynamic-concept-254710'
GCLOUD_ZONE = 'us-east1-b'

GCLOUD_COMPILATION_BUCKET = 's24_cb'
GCLOUD_BOT_BUCKET = 's24_ub'
# Replays are saved in different buckets based on player level
GCLOUD_REPLAY_BUCKETS = {
    # 0 is the normal bucket
    0: 's24_r',
    # 1 is the bucket for gold and above players
    1: 's24_gr',
}
GCLOUD_ONDEMAND_REPLAY_BUCKET = "s24_or"
# Bucket for pre-assembled bots that players fight in the
# tutorial/online editor
GCLOUD_GYM_BUCKET = "s24_g"
GCLOUD_ERROR_LOG_BUCKET = 's24_el'
GCLOUD_DEPLOYED_ARTIFACTS_BUCKET = 's24_da'
GCLOUD_EDITOR_BUCKET = 's24_e'
GCLOUD_WORKER_LOG_BUCKET = 's24_wl'

# The name of the worker source blob in the object storage bucket.
WORKER_ARTIFACT_KEY = "Halite.tgz"

DATABASE_PROJECT_ID = "dynamic-concept-254710"
DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:{port}/halite3"
DATABASES = [
    # Read-write master
    ("us-east1-b", "dynamic-concept-254710:us-east1:halite3", 3307),
    # Read replica
    ("us-east1-b", "dynamic-concept-254710:us-east1:halite3-replica", 3308),
]

# OAuth
OAUTH_GITHUB_CONSUMER_KEY = "3738a242abdf56ace0bd"
OAUTH_GITHUB_CONSUMER_SECRET = "5175d8e4c838c07a24845af8fcc7bc974b8c0887"

# CORS setup
SITE_URL = "http://35.237.189.116"
API_URL = "http://35.237.189.116"
CORS_ORIGINS = [SITE_URL]

# API Key authentication
api_key_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto",
)

# Discourse SSO
DISCOURSE_SSO_SECRET = b""
DISCOURSE_URL = "https://forums.halite.io/sso"

# SendGrid
SENDGRID_API_KEY = "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"
SENDGRID_SANDBOX_MODE = True

# Emails
COMPILATION_SUCCESS_TEMPLATE = ""
COMPILATION_FAILURE_TEMPLATE = ""
VERIFY_EMAIL_TEMPLATE = ""
FIRST_TIMEOUT_TEMPLATE = ""
BOT_DISABLED_TEMPLATE = ""
CONFIRMATION_TEMPLATE = ""
NEW_SUBSCRIBER_TEMPLATE = ""
INVITE_FRIEND_TEMPLATE = ""

RESEARCH_EMAILS = 10307
GAME_ERROR_MESSAGES = 10445
NEWSLETTERS_ARTICLES = 10447
GOODNEWS_ACCOMPLISHMENTS = 10449

C_NEWSLETTER_SUBSCRIPTION = "Newsletter_Subscription"
C_REGISTRATION_CONFIRMATION = "d-5a9a95aabc7d4a2c891ac8f4a86635c0"
C_BOT_DISABLED = "Bot disabled ="
C_BOT_TIMED_OUT = "Bot timed out"
C_COMPILATION_ERROR = "Compilation error"
C_COMPLIATION_SUCCESS = "Compilation success "
C_EMAIL_VERIFICATION = "d-6c76edb882c140389598b88b67b1f579"
C_INVITE_FRIEND = "Invite friend"

# Ranking Tiers
TIER_0_NAME = "Diamond"
TIER_0_PERCENT = 1/512
TIER_1_NAME = "Platinum"
TIER_1_PERCENT = 1/256
TIER_2_NAME = "Gold"
TIER_2_PERCENT = 1/128
TIER_3_NAME = "Silver"
TIER_3_PERCENT = 1/64
TIER_4_NAME = "Bronze"
# What tier a player must be in to be eligible for GPUs
GPU_TIER_NAME = TIER_2_NAME

TIER_0_STAY_BADGE = "A"
TIER_1_STAY_BADGE = "B"
TIER_2_STAY_BADGE = "C"
TIER_3_STAY_BADGE = "D"

# Whether GPU workers should preferentially seed is_gpu_enabled players.
ENFORCE_GPU_SEEDING = False
