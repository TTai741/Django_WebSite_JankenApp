#from .local import *
#try:
#    from .base import *
#except:
#    pass

#from .allauth import *

import os

# '.env.local' ファイルが存在するかどうかをチェックします。
if os.path.exists('.env.local'):
    # ローカル環境用の設定をインポートします。
    from .local import *
else:
    # それ以外の環境では、ベース設定をインポートします。
    from .base import *

# allauth関連の設定をインポートします。
from .allauth import *

